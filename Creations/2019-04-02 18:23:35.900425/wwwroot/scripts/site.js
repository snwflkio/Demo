var val = ""
function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
  ev.target.innerHTML = document.getElementById(data).innerHTML;
  console.log(ev.target.innerHTML);
  val = ev.target.innerHTML;
}

function getInfo()
{
	return val;
}
