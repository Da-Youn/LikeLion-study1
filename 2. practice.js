document.getElementById("btn").addEventListener("click", function () {
  console.log("clicked!!!!!");
});

var num = 0;

document.getElementById("plus").addEventListener("click", function () {
  num++;
  document.getElementById("num").innerHTML = num;
});

document.getElementById("minus").addEventListener("click", function () {
  num--;
  document.getElementById("num").innerHTML = num;
});

//document.querySelector(".bar").addEventListener("click", function () {
//  document.querySelector(".newBar").style.display = "block";
//});

document.querySelector(".bar").addEventListener("click", function () {
  document.querySelector(".bar").innerHTML = "눌렀어!";
  document.querySelector(".newBar").classList.toggle("show");
});
