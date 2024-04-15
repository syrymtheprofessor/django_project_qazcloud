
const floatingDiv = document.querySelector('.floating-block-part');
const floatingBtn = document.querySelector('.inner-btn');

window.addEventListener('scroll', () => {
  const { top } = floatingDiv.getBoundingClientRect();

  if (top <= 0) {
  floatingDiv.classList.add('color-change');
  floatingBtn.classList.add('b-visible');

  } else {
  floatingDiv.classList.remove('color-change');
  floatingBtn.classList.remove('b-visible');

  }
});