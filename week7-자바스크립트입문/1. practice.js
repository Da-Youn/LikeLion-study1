/* ID를 탐색하여 반환
document.getElementById("Lion").style.color = "red";
document.getElementById("tiger").style.color = "blue";
document.getElementById("bear").style.color = "green"; */

/* 태그 이름을 갖는 모든 요소 노드들을 탐색하여 반환
document.getElementsByTagName("li")[0].style.color = "red";
document.getElementsByTagName("li")[1].style.color = "blue";
document.getElementsByTagName("li")[2].style.color = "green"; */

/* 클래스 값을 갖는 모든 요소 노드들을 탐색하여 반환
document.getElementsByClassName("animal")[1].style.color = "red"; */

/* 선택자를 이용하여 반환
document.querySelectorAll(".animal")[0].style.color = "red"; */

/* DOM 조작 - innerHTML, classList
document.querySelectorAll(".animal")[2].innerHTML = "dog";
const animals = document.getElementById("animals"); 

animals.innerHTML += "<li class = 'animal'>cat</li>";

document.querySelectorAll(".box")[0].classList.add("purple");
document.querySelectorAll(".box")[0].classList.remove("purple"); // 제거

document.querySelectorAll(".box")[0].classList.toggle("yellow"); // 적용됨
document.querySelectorAll(".box")[0].classList.toggle("yellow"); // 한번더 쓰면 사라짐
 */
