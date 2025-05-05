const light = document.querySelector("#light");
const body = document.body;
const loadingScreen = document.getElementById("loading-screen");

// Agrupa todos los selectores de elementos que deben cambiar con el modo
const elementsToToggle = [
  ...document.querySelectorAll(".carta"),
  ...document.querySelectorAll(".carta_title"),
  ...document.querySelectorAll(".carta_title_folder"),
  ...document.querySelectorAll(".carta_botons")
];

// Función para aplicar o quitar el modo claro según el estado (true/false)
function setLightMode(isLight) {
  body.classList.toggle("lightMode", isLight);
  elementsToToggle.forEach(el => el.classList.toggle("light", isLight));
}

// Cambia el modo claro u oscuro al hacer click y guarda el estado
light.addEventListener("click", () => {
  const isLight = light.checked;
  setLightMode(isLight);
  localStorage.setItem("lightMode", isLight);
});

// Carga el modo guardado o establece el modo por defecto
function load() {
  const isLight = localStorage.getItem("lightMode") === "true";
  light.checked = isLight;
  setLightMode(isLight);

  if (loadingScreen) {
    loadingScreen.style.display = "none";
  }
}

// Ejecutar load cuando el DOM esté listo
document.addEventListener("DOMContentLoaded", load);
