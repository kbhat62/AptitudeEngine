function handleKeyPress(e)
{
  if(e.keyCode == 13)
  {
    changeUI();
  }
}
window.onresize = changeUI;
function changeUI()
{
  document.body.style.paddingTop = "0px";
  var logo = document.getElementById('logo');
  var edit = document.getElementById('ques');
  var ques = document.getElementById('ques-wrap');
  var help = document.getElementById('about-us');
  var sol = document.getElementById('sol');
  var question = document.getElementById('question');
  var rel = document.getElementById('rel');
  sol.style.display ="inline-block";
  rel.style.display ="inline-block";
  help.style.display ="none";
  rel.style.height = sol.clientHeight-30 +"px";
  question.innerHTML = edit.value;
  var w;
  if((w=document.body.clientWidth - logo.clientWidth) > 700 ){
  ques.style.paddingTop = "40px";
  logo.style.display = "inline-block";
  ques.style.display = "inline-block";
  ques.style.verticalAlign ="top";
  logo.style.marginLeft = "0px";
  logo.style.marginRight = "0px";
  w-=10;
  ques.style.width = w+"px";
  edit.style.width = (w-150)+"px";
  ques.paddingTop ="5px";
}
}
