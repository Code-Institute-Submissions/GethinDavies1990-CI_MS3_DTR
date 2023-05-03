const username = document.getElementById("username");
const password = document.getElementById("password");
const firstName = document.getElementById("first_name");
const lastName = document.getElementById("last_name");
const favFilm = document.getElementById("fav_film");
const image = document.getElementById("upload_image");
const form = document.getElementById("form");
const errorElement = document.getElementsByClassName('error')

form.addEventListener("submit", (e) => {
  let messages = [];
  if (username.value === "" || username.value == null) {
    messages.push("Username is required");
  }
  if (messages.length > 0) {

  e.preventDefault()
  errorElement.innerText = messages.join(',')
});
