const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form.addEventListener('submit', e => {
	e.preventDefault();
	validate();
	
	// checkInputs();
});

const sendData = (usernameValue, sRate, count) => {
	if (sRate === count){
		swal("Welcome! "+ usernameValue, "Registration Successful!", "success");
	}
}

// //final data validation

const successMsg = (usernameValue) => {
	let formCon = document.getElementsByClassName('form-control');
	var count = formCon.length - 1;
	for (var i = 0; i<formCon.length; i++){
		if(formCon[i].className === "form-control success"){
			var sRate = 0 + i;
			console.log(sRate);
						sendData(usernameValue ,sRate, count);
		} else {
			return false;
		}
	}
}


//email validate
// const isEmail = (emailValue) => {
// 	var atSymbol = emailValue.indexOf("@");
// 	if(atSymbol < 1) return false;
// 	var dot = emailValue.lastindexOf('.');
// 	if(dot <= atSymbol + 3) return false;
// 	if(dot === emailValue.length - 1) return false;
// }

// // function checkInputs() {
	// trim to remove the whitespaces
	
const validate = () => {
	const usernameValue = username.value.trim();
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();
	
	if(usernameValue === '') {
		setErrorFor(username, 'Username cannot be blank');
	} else if(usernameValue.length <= 2) {
		setErrorFor(username, 'username cannot be less than 3 character')
	} else {
		setSuccessFor(username);
	}
	
	if(emailValue === '') {
		setErrorFor(email, 'Email cannot be blank');
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, 'Not a valid email');
	} else {
		setSuccessFor(email);
	}
	
	if(passwordValue === '') {
		setErrorFor(password, 'Password cannot be blank');
	} else if(passwordValue.length <= 7){
		setErrorFor(password, 'password should be minimum of 8 character')
	} else {
		setSuccessFor(password);
	}
	
	if(password2Value === '') {
		setErrorFor(password2, 'Confirm Password cannot be blank');
	} else if(passwordValue !== password2Value) {
		setErrorFor(password2, 'Password does not match');
	} else{
		setSuccessFor(password2);
	}

	successMsg(usernameValue);
}
// }

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}
	
function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}
