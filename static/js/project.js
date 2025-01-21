{% if alert %}
            alert("{{ alert }}"); // Display the alert message
{% endif %}


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

// singin page validation
function validateLoginForm() {
    var username = document.getElementById("Lusername").value;
    var password = document.getElementById("Lpassword").value;
    var error = document.getElementById("Lerror");

    if (username === "" || password === "") {
        error.textContent = "Both fields are required.";
        return false;
    } else{
    return true;
    }
}




//mouse enter and leave
function bigtxt(x) {
    x.style.fontSize = "20px";
  }

  function normaltxt(x) {
    x.style.fontSize = "16px";

  }



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



// Function to display the popup
function openPopup() {
  var popup = document.getElementById('popup');
  if (popup) {
    popup.style.display = 'block';
  }
}

  // Function to close the popup
 function closePopup() {
  var popup = document.getElementById('popup');
  if (popup) {
    popup.style.display = 'none';
  }
}

  // Auto-open the popup after a delay (e.g., 5 seconds)


  // Auto-open the popup after a delay (e.g., 5 seconds)
setTimeout(openPopup, 5000);
// Close the popup when the close button is clicked
document.getElementById('close-popup').addEventListener('click', closePopup);




  // login icon
  let subMenu=document.getElementById("subMenu");
  function toggleMenu(){
    subMenu.classList.toggle("open-menu");
  }


  //chat bot

 // Define the chatbot responses
 const chatbotResponses = {
    "hello": "Hi there!",
    "how are you": "I'm just a bot, but thanks for asking!",
    "goodbye": "Goodbye! Have a great day.",
    "i want shirt":"go and search in shopping page we have multiple options",
    "whatsapp":"www.whatsapp.com"
    // Add more responses here
};

// Function to send a user message and get a response
function sendMessage() {
    const userMessage = document.getElementById("user-message").value;
    document.getElementById("chat-output").innerHTML += `<div class="user-message">You: ${userMessage}</div>`;

    if (chatbotResponses[userMessage.toLowerCase()]) {
        const botMessage = chatbotResponses[userMessage.toLowerCase()];
        document.getElementById("chat-output").innerHTML += `<div class="bot-message">Bot: ${botMessage}</div>`;
    } else {
        const botMessage = "I don't understand that. You can contact us on Facebook: <a href='https://www.facebook.com/messages/t' target='_blank'>Facebook Page</a>";
        document.getElementById("chat-output").innerHTML += `<div class="bot-message">Bot: ${botMessage}</div>`;
    }

    // Clear the user input
    document.getElementById("user-message").value = "";
}

// Event listener for the Send button
document.getElementById("send").addEventListener("click", sendMessage);

// Event listener for pressing Enter in the user input
document.getElementById("user-message").addEventListener("keyup", function (event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

function toggleChatbot() {
const chatbot = document.getElementById('chatbot');
if (chatbot.style.display === 'none' || chatbot.style.display === '') {
    chatbot.style.display = 'block';
} else {
    chatbot.style.display = 'none';
}
}

// Event listener for the chat button
document.getElementById('chat-button').addEventListener('click', toggleChatbot);

