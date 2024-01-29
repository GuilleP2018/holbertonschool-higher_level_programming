document.addEventListener('DOMContentLoaded', (event) => {
  let updateHeader = document.querySelector('#update_header');
  let header = document.querySelector('header');

  updateHeader.addEventListener('click', () => {
      header.textContent = 'New Header!!!';
  });
});
