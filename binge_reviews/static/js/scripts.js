const form = document.getElementById('form');
const username = document.getElementById('username');
const password = document.getElementById('password');

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
    const usernameValue = username.value.trim();
    const passwordValue = password.value.trim();

    if(usernameValue === '' ) {
        setError(username, 'Username is required');
        return false;
    } else if (usernameValue.length < 5 ) {
        setError(username, 'Username must be at least 5 characters.');
        return false;
    } else {
        setSuccess(username);
    }

    if(passwordValue === '') {
        setError(password, 'Password is required');
        return false;
    } else if (passwordValue.length < 5 ) {
        setError(password, 'Password must be at least 5 characters.');
        return false;
    } else {
        setSuccess(password);
    }

    return true;
};
