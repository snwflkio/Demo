var val = ""
function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  var style = window.getComputedStyle(ev.target, null);
  var topPos = style.getPropertyValue("top");
  var leftPos = style.getPropertyValue("left");
  if(topPos == "auto") topPos = 0;
  if(leftPos == "auto") topPos = 0;
  console.log(topPos + " " + leftPos)
  var data = ev.target.id + "," + topPos + "," + leftPos
  ev.dataTransfer.setData("text", data);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text").split(',');
  var design = document.getElementById("section-column");
  var width = window.getComputedStyle(design).width;
  console.log(data)
  var item = document.getElementById(data[0]);
  ev.target.appendChild(item);
  item.style.position = "relative";
  item.style.display = "inline";
  
  item.style.left = ((ev.clientX - width.replace("px","")  - 50) + 'px');
  item.style.top = ((ev.clientY)+ 'px');


   document.getElementById(data[0].split('-')[0] + '-setter').style["display"] = "block";
   return false;
}

function getInfo()
{
	return val;
}
