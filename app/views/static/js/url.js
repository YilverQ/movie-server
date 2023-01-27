const url = location.href;
const tag = url.replace("http://192.168.0.110:5000/folder/", "")
const wallpaper = document.getElementById("wallpaper")

if (tag.indexOf("&") == -1){
	wallpaper.classList.add("wallpaper");
	wallpaper.style.cssText=`background-image: url("/static/img/wallpaper/${tag}.jpeg");`;
}