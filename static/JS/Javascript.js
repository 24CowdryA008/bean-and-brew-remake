// Flip Card Function

function flipCard(card) {
    card.classList.toggle("flipped"); 
  }

// Carousel Function 

  const carouselData = [
    {
        image: url("{{ url_for('static', filename='IMG/Coffee1.png') }}")
    },
    {
        image: url("{{ url_for('static', filename='IMG/Coffee2.png') }}")
    },
    {
        image: url("{{ url_for('static', filename='IMG/Coffee3.png') }}")
    }
];

let currentIndex = 0;

function updateCarousel() {
    
    const { image /* , text  */ } = carouselData[currentIndex];

    
    const carouselElement = document.querySelector('.background-image');
    // const textElement = document.getElementById('carousel-text');

    
    carouselElement.style.backgroundImage = image;
    // textElement.innerText = text;

    
    currentIndex = (currentIndex + 1) % carouselData.length;
}

setInterval(updateCarousel, 1500);

updateCarousel();