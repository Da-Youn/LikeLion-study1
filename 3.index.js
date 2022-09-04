const toDoList = document.querySelector('#to-do-list');
const items = toDoList.children;

// 1. upToDo 함수를 완성
function upToDo(event) {
  event.target.classList.toggle('done');
}

// 2. 반복문을 활용해서 이벤트 핸들러를 등록

for (let item of items) {
  item.addEventListener('click', upToDo);
}

// 제대로 동작하는지 확인을 위한 TEST CODE
items[3].removeEventListener('click', upToDo);
