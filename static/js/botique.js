// login icon
let subMenu=document.getElementById("subMenu");
function toggleMenu(){
  subMenu.classList.toggle("open-menu");
}
// changing to uppercase
function upperCase() {
  const x = document.getElementById("name");
  x.value = x.value.toUpperCase();
}


// javascripcode for selection in botique
const dropdownB = document.getElementById("validationDefault04");
      dropdownB.addEventListener("change", function() {
        const selectedText = dropdownB.options[dropdownB.selectedIndex].text;
        alert(`Are You Sure! Do You Want To Book an in ${selectedText}`);
      });


// appointment validation starts
function validateForm() {
          let name = document.getElementById("name").value;
          let phone = document.getElementById("phone").value;
          let city = document.getElementById("city").value;
          let email = document.getElementById("email").value;
          let date = document.getElementById("date").value;

          let isValid = true;

          // Validate Name (Alphabets only)
          let namePattern = /^[A-Za-z\s]+$/;
          if (!name.match(namePattern)) {
              document.getElementById("nameError").innerHTML = "Name must contain only alphabets and spaces.";
              isValid = false;
          } else {
              document.getElementById("nameError").innerHTML = "";
          }

//          // Validate Phone Number (Numeric, 10 digits)
//          let phonePattern = /^[0-9]{10}$/;
//          if (!phone.match(phonePattern)) {
//              document.getElementById("phoneError").innerHTML = "Phone number must be 10 digits long.";
//              isValid = false;
//          } else {
//              document.getElementById("phoneError").innerHTML = "";
//          }

          // Validate City (Alphabets only)
          let cityPattern = /^[A-Za-z\s]+$/;
          if (!city.match(cityPattern)) {
              document.getElementById("cityError").innerHTML = "City must contain only alphabets and spaces.";
              isValid = false;
          } else {
              document.getElementById("cityError").innerHTML = "";
          }

//          // Validate Email (Basic format)
//          let emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
//          if (!email.match(emailPattern)) {
//              document.getElementById("emailError").innerHTML = "Invalid email address.";
//              isValid = false;
//          } else {
//              document.getElementById("emailError").innerHTML = "";
//          }

          // Validate Date
          if (date === "") {
              document.getElementById("dateError").innerHTML = "Please select a date.";
              isValid = false;
          } else {
              document.getElementById("dateError").innerHTML = "";
          }

          return isValid;
          
      }
//appointment validation ends


// Function to toggle between dark and light mode
function toggleDarkLightMode() {
  const currentTheme = localStorage.getItem('theme') || 'light';
  const moonIcon = document.getElementById('moon-icon');
  const logoIcon = document.getElementById('navbar-logo');

  if (currentTheme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'light');
      moonIcon.src = 'static/upload/moon.png';
      logoIcon.src = 'static/upload/logofinal-01.png'
      localStorage.setItem('theme', 'light');
  } else {
      document.documentElement.setAttribute('data-theme', 'dark');
      moonIcon.src = 'static/upload/sun.png';
      logoIcon.src = 'static/upload/logof-darkmode.png'
      localStorage.setItem('theme', 'dark');
  }
}

// Check for the theme in local storage and set it
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
document.documentElement.setAttribute('data-theme', savedTheme);
if (savedTheme === 'dark') {
    document.getElementById('moon-icon').src = 'static/upload/sun.png';
}
}

// Add a click event listener to the moon icon
document.getElementById('moon-icon').addEventListener('click', toggleDarkLightMode);




// singin page validation
function validateLoginForm() {
    var username = document.getElementById("Lusername").value;
    var password = document.getElementById("Lpassword").value;
    var error = document.getElementById("Lerror");

    if (username === "" || password === "") {
        error.textContent = "Both fields are required.";
        return false;
    } else{
    return true
    }
}