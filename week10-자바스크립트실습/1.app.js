function getCheckboxValue(event) {
  let result = '';
  if (event.target.checked) {
    result = event.target.value;
  } else {
    result = '';
  }

  document.getElementById('result').innerText += result;
  return result;
}

const list = document.querySelector('#list');
const result = document.querySelector('#result');

function submit() {
  list.style.display = 'none';
  result.style.display = 'block';
}
