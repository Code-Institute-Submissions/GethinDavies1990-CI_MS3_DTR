const form = document.getElementById("reg-form");
const username = document.getElementById("username");
const password = document.getElementById("password");
const firstName = document.getElementById("first_name");
const lastName = document.getElementById("last_name");
const favFilm = document.getElementById("fav_film");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  validateInputs();
});

const setError = (element, message) => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector(".error");

  errorDisplay.innerText = message;
  inputControl.classList.add("error");
  inputControl.classList.remove("success");
};

const setSuccess = (element) => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector(".error");

  errorDisplay.innerText = "";
  inputControl.classList.add("success");
  inputControl.classList.remove("error");
};

const validateInputs = () => {
  const usernameValue = username.value.trim();
  const passwordValue = password.value.trim();
  const firstNameValue = firstName.value.trim();
  const lastNameValue = lastName.value.trim();
  const favFilmValue = favFilm.value.trim();

  if (usernameValue === "") {
    setError(username, "Username is required");
  } else {
    setSuccess(username);
  }

  if (passwordValue === "") {
    setError(password, "Password is required");
  } else if (passwordValue.length < 8) {
    setError(password, "Password must be at least 8 characters long.");
  } else {
    setSuccess(password);
  }
};
