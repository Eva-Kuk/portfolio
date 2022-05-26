const currentLocation = location.href;
const menuItem = document.querySelectorAll('a');
const menuLenght = menuItem.length
for (let i = 0; i<menuLenght; i++){
    if(menuItem[i].href === currentLocation){
        menuItem[i].className = "active"
    }
}



/*const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('nav a').
forEach(link => {
    if(link.href.includes(`${activePage}`)){
        link.classList.add('active');
    }
})*/

/*const sections = document.querySelectorAll('.section');
const sectBtns = document.querySelectorAll('.icon-bar');
const sectBtn = document.querySelectorAll('.nav-icon');
const allSections = document.querySelector('.main-content');


function PageTransitions() {
    //Button click active class
    for (let i = 0; i < sectBtn.length; i++) {
        sectBtn[i].addEventListener('click', function() {
            let currentBtn = document.querySelectorAll('.active');
            currentBtn[0].className = currentBtn[0].className.replace('active', '');
            this.className += ' active';
        })
    }

    //Sections Active 
    allSections.addEventListener('click', (e) => {
        const id = e.target.dataset.id;
        if (id) {
            //remove selected from the other btns
            sectBtns.forEach((btn) => {
                btn.classList.remove('active')
            })
            e.target.classList.add('active')

            //hide other sections
            sections.forEach((section) => {
                section.classList.remove('active')
            })

            const element = document.getElementById(id);
            element.classList.add('active');
        }
    })
}

PageTransitions();*/

/*
const links = document.querySelectorAll('.link');
const sections = document.querySelectorAll('.section');

let activeLink = 0;

links.forEach((link, i) => {
    link.addEventListener('click', () => {
        if (activeLink != i) {
            links[activeLink].classList.remove('active');
            link.classList.add('active');
            sections[activeLink].classList.remove('active');

            setTimeout(() => {
                activeLink = i;
                sections[i].classList.add('active');
            }, 1000);
        }
    })
})*/