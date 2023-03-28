function passive_wisdom(wis_bonus, prof_bonus) {
    return 10 + wis_bonus + prof_bonus;
}

function testfunct() {
    return 10;
}

function toggleTopBar(elementId) {
  var element = document.getElementById(elementId);
  if (element.style.display === "none") {
    element.style.display = "block";
  } else {
    element.style.display = "none";
  }
}
