$(document).ready(function () {
	$(".owl-carousel").owlCarousel({
		loop: true,
		margin: 10,
		nav: false,
		autoplay: true,
		autoplayTimeout: 5000,
		autoplayHoverPause: true,
		center: true,
		responsive: {
			0: {
				autoHeight: true,
				items: 1
			},
			600: {
				autoHeight: true,
				items: 1
			},
			1000: {
				items: 2.35
			}
		}
	});
});

$(document).ready(function () {
	$(".owl-carousel-block").owlCarousel({
		loop: true,
		margin: 10000,
		nav: true,
		autoplay: true,
		autoplayTimeout: 5000,
		autoplayHoverPause: true,
		center: true,
		responsive: {
			0: {
				items: 1
			},
			800: {
				items: 1
			}
		}
	});
});



$(function() {

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
	





	/*Smooth scroll*/
	$("[data-scroll]").on("click", function(event) {
		event.preventDefault();

		var $this = $(this),
			blockId = $this.data("scroll"),
			blockOffset = $(blockId).offset().top;

		$("#nav a").removeClass("active");
		$this.addClass("active");

		$("html, body").animate({
			scrollTop: blockOffset

		}, 500);
	});

	$("[data-collapse]").on("click", function(event) {
		event.preventDefault();

		var $this = $(this),
			blockId = $this.data("collapse");

		$(blockId).slideToggle();

	});


});