var loaded = false;
var data = null;
function ajaxCode() {
    var edit = document.getElementById('ques');
    if(edit.value != "" && edit.value.length >5){
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        loaded = true;
          if (this.readyState == 4 && this.status == 200) {
              data = JSON.parse(this.response);
              if(!('error' in data))
              {
                var result = document.getElementById('result');
                var cont = document.getElementById('sol-container');
                result.innerHTML = data.result;
                var steps = data.steps
                for(index in steps)
                {
                  var card = document.createElement("DIV");
                  card.className ="card step";
                  var step =  document.createElement("DIV");
                  step.className ="step-no color"+(index%5+1);
                  step.appendChild(document.createTextNode(parseInt(index)+1));
                  card.appendChild(step);
                  card.appendChild(document.createTextNode(steps[index]));
                  cont.appendChild(card);
                }
                changeUI();
            }else alert(data.error);
         }
      };
      var url = "http://"+location.host+"/solve/"+edit.value;
      xhttp.open("GET",url, true);
      xhttp.send();
    }else alert("Please enter a valid question");
}
function handleKeyPress(e)
{
  if(e.keyCode == 13)
  {
    ajaxCode();
  }
}
window.onresize = function(){
  changeUI();
};
function changeUI()
{
  var edit = document.getElementById('ques');
  if(loaded)
  {
    document.body.style.paddingTop = "0px";
    var logo = document.getElementById('logo');
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
    if((w=document.body.clientWidth - logo.clientWidth) > 400 ){
      console.log(w);
      if(logo.clientHeight > 100)
    ques.style.paddingTop = "40px";
    else ques.style.paddingTop = "20px";
    logo.style.display = "inline-block";
    ques.style.display = "inline-block";
    ques.style.verticalAlign ="top";
    logo.style.marginLeft = "0px";
    logo.style.marginRight = "0px";
    w-=10;
    ques.style.width = w+"px";
    edit.style.width = (w-150)+"px";
    ques.paddingTop ="5px";
  }else{
    logo.style.display = "block";
    ques.style.display = "block";
    ques.style.paddingTop = "2px";
    logo.style.marginLeft = "auto";
    logo.style.marginRight = "auto";
    w = document.body.clientWidth-15;
    ques.style.width =w+"px";
    edit.style.width =w-document.getElementById('solve').clientWidth-35+"px";
  }
}
}
