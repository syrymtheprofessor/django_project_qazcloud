$(document).ready(function () {
	$(".owl-carousel").owlCarousel({
		loop: true,
		margin: 10,
		nav: true,
		autoplay: true,
		autoplayTimeout: 5000000000,
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
		autoplayTimeout: 500000000,
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