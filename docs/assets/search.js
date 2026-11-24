(function () {
  var tag = document.querySelector("script[data-base]");
  var BASE = tag ? tag.getAttribute("data-base") : "";
  var input = document.getElementById("site-search");
  var data = null, loading = false, pending = [], active = -1, timer = null;

  function fold(s) {
    return s.replace(/[^\u0000-\u007f]/g, function (c) {
      return c.normalize("NFD").replace(/[̀-ͯ]/g, "");
    }).toLowerCase();
  }
  function esc(s) {
    return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function tokens(q) {
    return fold(q).split(/\s+/).filter(function (t) { return t.length >= 2; });
  }
  function ranges(ftxt, tk) {
    var r = [];
    tk.forEach(function (t) {
      var p = -1;
      while ((p = ftxt.indexOf(t, p + 1)) >= 0) r.push([p, p + t.length]);
    });
    r.sort(function (a, b) { return a[0] - b[0]; });
    var m = [];
    r.forEach(function (x) {
      var l = m[m.length - 1];
      if (l && x[0] <= l[1]) l[1] = Math.max(l[1], x[1]);
      else m.push([x[0], x[1]]);
    });
    return m;
  }

  /* ---------- Resaltat a la pàgina de destí (?q=...) ---------- */
  function highlightPage() {
    var q = new URLSearchParams(location.search).get("q");
    var root = document.querySelector(".prose");
    if (!q || !root) return;
    var tk = tokens(q);
    if (!tk.length) return;
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        return n.parentNode.closest("script, style, mark") ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
      }
    });
    var nodes = [], n;
    while ((n = walker.nextNode())) nodes.push(n);
    var marks = [];
    nodes.forEach(function (node) {
      var txt = node.nodeValue, m = ranges(fold(txt), tk);
      if (!m.length) return;
      var frag = document.createDocumentFragment(), last = 0;
      m.forEach(function (x) {
        if (x[0] > last) frag.appendChild(document.createTextNode(txt.slice(last, x[0])));
        var mk = document.createElement("mark");
        mk.textContent = txt.slice(x[0], x[1]);
        frag.appendChild(mk);
        marks.push(mk);
        last = x[1];
      });
      if (last < txt.length) frag.appendChild(document.createTextNode(txt.slice(last)));
      node.parentNode.replaceChild(frag, node);
    });
    if (!marks.length) return;
    var target = null;
    if (location.hash.length > 1) {
      try { target = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch (e) { target = null; }
    }
    var first = marks[0];
    if (target) {
      for (var i = 0; i < marks.length; i++) {
        if (target.compareDocumentPosition(marks[i]) & Node.DOCUMENT_POSITION_FOLLOWING) { first = marks[i]; break; }
      }
    }
    setTimeout(function () { first.scrollIntoView({ block: "center" }); }, 60);
  }
  highlightPage();

  if (!input) return;

  var panel = document.createElement("div");
  panel.id = "search-results";
  panel.setAttribute("role", "listbox");
  panel.hidden = true;
  document.body.appendChild(panel);

  /* ---------- Càrrega de l'índex (només la primera vegada) ---------- */
  function load(cb) {
    if (data) return cb();
    pending.push(cb);
    if (loading) return;
    loading = true;
    var s = document.createElement("script");
    s.src = BASE + "assets/search-index.js";
    s.onload = function () {
      data = (window.SEARCH_INDEX || []).map(function (p) {
        return {
          t: p.t, c: p.c, u: p.u, ft: fold(p.t),
          s: p.s.map(function (x) {
            return { id: x[0], h: x[1], x: x[2], fh: fold(x[1]), fx: fold(x[2]) };
          })
        };
      });
      var cbs = pending; pending = [];
      cbs.forEach(function (f) { f(); });
    };
    s.onerror = function () {
      loading = false; pending = [];
      show('<div class="sr-empty">No s\'ha pogut carregar el cercador.</div>');
    };
    document.head.appendChild(s);
  }

  /* ---------- Cerca ---------- */
  function search(tk) {
    var res = [];
    data.forEach(function (p) {
      var best = null;
      p.s.forEach(function (sec) {
        var score = 0, ok = true;
        for (var i = 0; i < tk.length; i++) {
          var t = tk[i];
          var inT = p.ft.indexOf(t) >= 0, inH = sec.fh.indexOf(t) >= 0, inX = sec.fx.indexOf(t) >= 0;
          if (!inT && !inH && !inX) { ok = false; break; }
          if (inT) score += 20;
          if (inH) score += 10;
          if (inX) {
            var n = 0, pos = -1;
            while (n < 20 && (pos = sec.fx.indexOf(t, pos + 1)) >= 0) n++;
            score += n;
          }
        }
        if (ok && (!best || score > best.score)) best = { sec: sec, score: score };
      });
      if (best) res.push({ p: p, sec: best.sec, score: best.score });
    });
    res.sort(function (a, b) { return b.score - a.score || (a.p.t < b.p.t ? -1 : 1); });
    return res;
  }

  function snippet(sec, tk) {
    var text = sec.x, f = sec.fx, pos = -1;
    tk.forEach(function (t) {
      var k = f.indexOf(t);
      if (k >= 0 && (pos < 0 || k < pos)) pos = k;
    });
    if (pos < 0) return esc(text.slice(0, 150)) + (text.length > 150 ? "…" : "");
    var a = Math.max(0, pos - 60), b = Math.min(text.length, pos + 120);
    if (a > 0) {
      var sp = text.indexOf(" ", a);
      if (sp >= 0 && sp < pos) a = sp + 1;
    }
    var frag = text.slice(a, b), m = ranges(f.slice(a, b), tk), out = "", last = 0;
    m.forEach(function (x) {
      out += esc(frag.slice(last, x[0])) + "<mark>" + esc(frag.slice(x[0], x[1])) + "</mark>";
      last = x[1];
    });
    out += esc(frag.slice(last));
    return (a > 0 ? "…" : "") + out + (b < text.length ? "…" : "");
  }

  function show(html) { panel.innerHTML = html; panel.hidden = false; active = -1; }
  function close() { panel.hidden = true; active = -1; }

  function render() {
    var q = input.value.trim(), tk = tokens(q);
    if (!tk.length) { close(); return; }
    load(function () {
      if (input.value.trim() !== q) return;
      var res = search(tk);
      if (!res.length) {
        show('<div class="sr-empty">Cap resultat per a «' + esc(q) + '».</div>');
        return;
      }
      var html = '<div class="sr-count">' + res.length + " resultat" + (res.length === 1 ? "" : "s") + "</div>";
      res.slice(0, 12).forEach(function (r) {
        var href = BASE + r.p.u + "?q=" + encodeURIComponent(q) + (r.sec.id ? "#" + encodeURIComponent(r.sec.id) : "");
        html += '<a class="sr-item" role="option" href="' + esc(href) + '">' +
          '<span class="sr-crumb">' + esc(r.p.c) + "</span>" +
          '<span class="sr-title">' + esc(r.p.t) + "</span>" +
          (r.sec.h ? '<span class="sr-sec"># ' + esc(r.sec.h) + "</span>" : "") +
          '<span class="sr-snip">' + snippet(r.sec, tk) + "</span></a>";
      });
      if (res.length > 12) html += '<div class="sr-count">Es mostren els 12 primers. Afegeix més paraules per afinar.</div>';
      show(html);
    });
  }

  function move(d) {
    var items = panel.querySelectorAll(".sr-item");
    if (!items.length) return;
    if (active >= 0) items[active].classList.remove("active");
    active = (active + d + items.length) % items.length;
    items[active].classList.add("active");
    items[active].scrollIntoView({ block: "nearest" });
  }

  input.addEventListener("input", function () {
    clearTimeout(timer);
    timer = setTimeout(render, 120);
  });
  input.addEventListener("focus", function () { if (tokens(input.value).length) render(); });
  input.addEventListener("keydown", function (e) {
    if (e.key === "ArrowDown") { e.preventDefault(); move(1); }
    else if (e.key === "ArrowUp") { e.preventDefault(); move(-1); }
    else if (e.key === "Escape") { close(); input.blur(); }
    else if (e.key === "Enter") {
      var items = panel.querySelectorAll(".sr-item");
      if (items.length) { e.preventDefault(); location.href = items[active >= 0 ? active : 0].href; }
    }
  });
  document.addEventListener("click", function (e) {
    if (!panel.contains(e.target) && !e.target.closest(".search-container")) close();
  });
  document.addEventListener("keydown", function (e) {
    var el = document.activeElement, tag = el ? el.tagName : "";
    if (e.key === "/" && tag !== "INPUT" && tag !== "TEXTAREA" && !e.ctrlKey && !e.metaKey) {
      e.preventDefault();
      input.focus();
    }
  });
})();
