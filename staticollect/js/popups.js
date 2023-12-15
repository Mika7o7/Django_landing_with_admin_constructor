function openForm() {
    document.getElementById("popup").classList.toggle("popup-open");
    document.getElementById("popup_close").style.display = "block";
  }
function closeForm() {
    document.getElementById("popup").classList.toggle("popup-open");
    document.getElementById("popup_close").style.display = "none";
  }

// function myFunction() {
//     var x = document.getElementById("myLinks");
//     if (x.style.display === "block") {
//       x.style.display = "none";
//     } else {
//       x.style.display = "block";
//     }
//   }

function openbar() {
    document.getElementById("myLinks").classList.toggle("myLinks-close");
    document.getElementById("myLinks").style.display = "block";
    document.getElementById('icon').style.display = "none";
  }


function closebar() {
    document.getElementById("myLinks").classList.toggle("myLinks-close");
    document.getElementById("myLinks").style.display = "none";
    document.getElementById('icon').style.display = "block";


  }

const offset = 700;


function toLesson(x, y) {
    window.scrollTo(x, y);
};

function Course_program(x, y) {
    window.scrollTo(x, y);
};

function toContacts(x, y) {
    window.scrollTo(x, y);
};

// onScroll
window.onscroll = () => {
   if (window.scrollY > offset) {
    document.querySelector('.buttonUp').classList.add('buttonUp--active')
    // click
    document.querySelector('.buttonUp').onclick = () => {
        window.scrollTo(0, 0);
};
   } else {
    document.querySelector('.buttonUp').classList.remove('buttonUp--active')
    
   }
};

// carusel 

var slideIndex = 1;
showSlides(slideIndex);


function pluseSlides(n) {
  showSlides(slideIndex += n);
} 

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");

  if (n > slides.length) {
    slideIndex = 1
  }
  if (n < 1) {
    slideIndex=slides.length
  }
  for (i=0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i=0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace("active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += "active";
}
$(document).ready(function () {
  $('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    
})
});

  
