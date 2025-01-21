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