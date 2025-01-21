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
        document.getElementById('navbar-logo').src = 'static/upload/logof-darkmode.png';
    }
  }

  // Add a click event listener to the moon icon
  document.getElementById('moon-icon').addEventListener('click', toggleDarkLightMode);




    // login icon
    let subMenu=document.getElementById("subMenu");
    function toggleMenu(){
      subMenu.classList.toggle("open-menu");
    }



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

//fullscreen on home page
/* Get the element you want displayed in fullscreen */ 
var elem = document.documentElement;

/* Function to open fullscreen mode */
function openFullscreen() {
  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } else if (elem.mozRequestFullScreen) { /* Firefox */
    elem.mozRequestFullScreen();
  } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari & Opera */
    elem.webkitRequestFullscreen();
  } else if (elem.msRequestFullscreen) { /* IE/Edge */
    elem = window.top.document.body; //To break out of frame in IE
    elem.msRequestFullscreen();
  }
}

/* Function to close fullscreen mode */
function closeFullscreen() {
  if (document.exitFullscreen) {
    document.exitFullscreen();
  } else if (document.mozCancelFullScreen) {
    document.mozCancelFullScreen();
  } else if (document.webkitExitFullscreen) {
    document.webkitExitFullscreen();
  } else if (document.msExitFullscreen) {
    window.top.document.msExitFullscreen();
  }
}
