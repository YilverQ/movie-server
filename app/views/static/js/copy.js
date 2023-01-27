const imagenVLC = document.querySelectorAll(".imagenVLC");
const texts = document.querySelectorAll(".hidden");
const tooltip = document.querySelectorAll(".tooltip__message");


imagenVLC.forEach( (element, i) => {
	imagenVLC[i].addEventListener("click", ()=>{
		let text = texts[i];
  		//Proceso de copiado!
  		let aux = document.createElement("input");
  		aux.setAttribute("value", text.textContent);
  		document.body.appendChild(aux);
  		aux.select();
  		document.execCommand("copy");
  		document.body.removeChild(aux);
			
			tooltip[i].classList.add("activate");
			setTimeout(function(){
					tooltip[i].classList.remove("activate");
			}, 1000);
	})
})




//Explicación del proceso de copiado!
  // Crea un campo de texto "oculto"
  // Asigna el contenido del elemento especificado al valor del campo
  // Añade el campo a la página
  // Selecciona el contenido del campo
  // Copia el texto seleccionado
  // Elimina el campo de la página