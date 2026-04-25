const addItemElement = document.querySelector('#add_item');
const myList = document.querySelector('.my_list');

addItemElement.addEventListener('click', function () {
  const newListItem = document.createElement('li');
  newListItem.textContent = 'Item';
  myList.appendChild(newListItem);
});
