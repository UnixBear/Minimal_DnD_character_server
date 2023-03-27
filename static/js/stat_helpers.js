function passive_wisdom(wis_bonus, prof_bonus) {
    return 10 + wis_bonus + prof_bonus;
}

function testfunct() {
    return 10;
}

function toggleTopBar() {
  var topBar = document.getElementById("top-bar");
  if (topBar.style.display === "none") {
    topBar.style.display = "block";
  } else {
    topBar.style.display = "none";
  }
}
