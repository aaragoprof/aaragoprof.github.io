// Fa que el títol del lloc ("Aula d'Informàtica") de la capçalera sigui un enllaç a l'inici.
document.addEventListener("DOMContentLoaded", function () {
  var logo = document.querySelector(".md-header__button.md-logo");
  var titol = document.querySelector(".md-header__topic:first-child .md-ellipsis");
  if (!logo || !titol) return;
  var enllac = document.createElement("a");
  enllac.href = logo.href;
  enllac.className = "md-ellipsis";
  enllac.style.color = "inherit";
  enllac.style.textDecoration = "none";
  while (titol.firstChild) enllac.appendChild(titol.firstChild);
  titol.replaceWith(enllac);
});
