function openMenu(contName, elmnt, color) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName('content');
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = 'none';
  }

  tablinks = document.getElementsByClassName('tab');
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = '';
  }

  document.getElementById(contName).style.display = 'block';

  elmnt.style.backgroundColor = color;
}

document.getElementById('defaultOpen').click();
