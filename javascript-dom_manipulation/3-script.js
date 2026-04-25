const toggleHeader = document.querySelector('#toggle_header');
const headerElement = document.querySelector('header');

toggleHeader.addEventListener('click', function () {
  headerElement.classList.toggle('red');
  headerElement.classList.toggle('green');
});
