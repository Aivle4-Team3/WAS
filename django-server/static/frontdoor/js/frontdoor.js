document.addEventListener("DOMContentLoaded", function() {
    let currentIndex = 0;
    const items = document.querySelectorAll('.carousel .carousel-item');
    const totalItems = items.length;

    function cycleItems() {
        const item = items[currentIndex];
        items.forEach(item => item.classList.remove('active'));

        item.classList.add('active');
        currentIndex = (currentIndex + 1) % totalItems;
    }

    setInterval(cycleItems, 3000); // Change 3000 to the number of milliseconds you want each slide to display
});