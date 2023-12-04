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


