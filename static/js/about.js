// login icon
let subMenu=document.getElementById("subMenu");
function toggleMenu(){
  subMenu.classList.toggle("open-menu");
}



const testimonials = [
{
  name: "Eva Sawyer",
  job: "Model",
  image: "static/upload/test-4.png",
  testimonial:
    "With Thrives help, we were able to increase the functionality of our website dramatically while cutting our costs. Our website is much more easy to use, has tons of more features than before and is incredibly easy to maintain. We could not be more happy with our new website!",
},
{
  name: "Katey Topaz",
  job: "Developer, TechCrew",
  image: "static/upload/test-3.png",
  testimonial:
    "Thrive Internet Marketing excels at turning your website dreams into reality. We are so proud of the work they have done for us that we have already recommended them to many of our partners.",
},
{
  name: "Jae Robin",
  job: "UI Designer, Affinity Agency",
  image: "static/upload/test-1.png",
  testimonial:
    "The attention to detail with Thrives professional staff is incredible. The entire team has proven to be very innovative and will work with ideas that I have as well and think of new ways to bring more traffic to our site in ways I would never have considered.",
},
{
  name: "Nicola Blakely",
  job: "Stylist",
  image: "static/upload/test-2.png",
  testimonial:
    "It is a distinct pleasure for me to recommend Thrive Internet Marketing to any and all interested parties. They have been professional, comprehensive and competent throughout the process of our working together. We feel that we have established a relationship with them for years to come.",
},
];
//Current Slide
let i = 0;
//Total Slides
let j = testimonials.length;
let testimonialContainer = document.getElementById("testimonial-container");
let nextBtn = document.getElementById("next");
let prevBtn = document.getElementById("prev");
nextBtn.addEventListener("click", () => {
i = (j + i + 1) % j;
displayTestimonial();
});
prevBtn.addEventListener("click", () => {
i = (j + i - 1) % j;
displayTestimonial();
});
let displayTestimonial = () => {
testimonialContainer.innerHTML = `
  <p>${testimonials[i].testimonial}</p>
  <img src=${testimonials[i].image}>
  <h3>${testimonials[i].name}</h3>
  <h6>${testimonials[i].job}</h6>
`;
};
window.onload = displayTestimonial;

// mouseup and down events in story

function mDown(obj) {

obj.innerHTML = "Thank You for Reading";
}

function mUp(obj) {

obj.innerHTML="Our Story";
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

