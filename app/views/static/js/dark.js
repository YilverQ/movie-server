let light = document.querySelector("#light");
const body = document.querySelector("body");
const carta = document.querySelectorAll(".carta");
const carta_title = document.querySelectorAll(".carta_title");
const carta_title_folder = document.querySelectorAll(".carta_title_folder");
const carta_botons = document.querySelectorAll(".carta_botons");


function addLightMode(){
	body.classList.toggle("lightMode");
	//for of
	for (cart of carta){
		cart.classList.toggle("light");
	}
	
	for (title of carta_title){
		title.classList.toggle("light");
	}

	for (title of carta_title_folder){
		title.classList.toggle("light");
	}

	for (icon of carta_botons){
		icon.classList.toggle("light");
	}
}

light.addEventListener("click", e =>{
	addLightMode();
	store(body.classList.contains("lightMode"));
})

function load(){
	const dark = localStorage.getItem("lightMode");

	if (!dark){
		store("false");
	}else if (dark == "true"){
		light.checked = true;
		addLightMode();
	}
}
function store(value){
	localStorage.setItem("lightMode", value);
}

load();