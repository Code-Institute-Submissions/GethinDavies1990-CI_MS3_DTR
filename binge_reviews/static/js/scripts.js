// The form validation checks for user input and server side validation before submitting.
// Credit: https://www.youtube.com/watch?v=CYlNJpltjMM&t=6s
const form = document.getElementById('form');
const username = document.getElementById('username');
const password = document.getElementById('password');
const firstName = document.getElementById('first_name')
const lastName = document.getElementById('last_name')
const favFilm = document.getElementById('fav_film')
const filmName = document.getElementById('film_name')
const reviewTitle = document.getElementById('review_title')
// const categorySelection = document.getElementById('category_name')
const reviewDescription = document.getElementById('review_description')
// const rating = document.getElementById('rating')

form.addEventListener('submit', function (event) {
    event.preventDefault();
    if (validateInputs()) {
        form.submit();
    }
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const validateInputs = () => {
    let isValid = true;

    // Check username and password fields for both forms
    if (username) {
      const usernameValue = username.value.trim();
      if (usernameValue === '') {
        setError(username, 'Username is required');
        isValid = false;
      } else if (usernameValue.length < 5) {
        setError(username, 'Username must be at least 5 characters.');
        isValid = false;
      } else {
        setSuccess(username);
      }
    }
    if (password) {
      const passwordValue = password.value.trim();
      if (passwordValue === '') {
        setError(password, 'Password is required');
        isValid = false;
      } else if (passwordValue.length < 5) {
        setError(password, 'Password must be at least 5 characters.');
        isValid = false;
      } else {
        setSuccess(password);
      }
    }

    // Check additional fields for registration form
    if (firstName) {
      const firstNameValue = firstName.value.trim();
      if (firstNameValue === '') {
        setError(firstName, 'First name is required');
        isValid = false;
      } else if (firstNameValue.length < 1) {
        setError(firstName, 'First name must be at least 1 character.');
        isValid = false;
      } else {
        setSuccess(firstName);
      }
    }
    if (lastName) {
      const lastNameValue = lastName.value.trim();
      if (lastNameValue === '') {
        setError(lastName, 'Last name is required');
        isValid = false;
      } else if (lastNameValue.length < 1) {
        setError(lastName, 'Last name must be at least 1 character.');
        isValid = false;
      } else {
        setSuccess(lastName);
      }
    }
    if (favFilm) {
      const favFilmValue = favFilm.value.trim();
      if (favFilmValue === '') {
        setError(favFilm, 'Favorite film is required');
        isValid = false;
      } else if (favFilmValue.length < 1) {
        setError(favFilm, 'Favorite film must be at least 1 character.');
        isValid = false;
      } else {
        setSuccess(favFilm);
      }
    }
      if (filmName) {
        const filmNameValue = filmName.value.trim();
        if (filmNameValue === '') {
          setError(filmName, 'Film name is required');
          isValid = false;
        } else if (filmNameValue.length < 5) {
          setError(filmName, 'Film name must be at least 5 character.');
          isValid = false;
        } else {
          setSuccess(filmName);
        }
      }
      if (reviewTitle) {
        const reviewTitleValue = reviewTitle.value.trim();
        if (reviewTitleValue === '') {
          setError(reviewTitle, 'Review title is required');
          isValid = false;
        } else if (reviewTitleValue.length < 15) {
          setError(reviewTitle, 'Review title must be at least 15 character.');
          isValid = false;
        } else {
          setSuccess(reviewTitle);
        }
      }
      if (reviewDescription) {
        const reviewDescriptionValue = reviewDescription.value.trim();
        if (reviewDescriptionValue === '') {
          setError(reviewDescription, 'Review description is required');
          isValid = false;
        } else if (reviewDescriptionValue.length < 50) {
          setError(reviewDescription, 'Review description must be at least 50 character.');
          isValid = false;
        } else {
          setSuccess(reviewDescription);
        }
      }

    return isValid;
  };

