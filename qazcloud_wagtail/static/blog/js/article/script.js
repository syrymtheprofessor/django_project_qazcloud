(function () {
	'use strict';

	function Content(callback) {
		let classes = {
			tab: 'tmpl-hh__content-tab',
			swiperContainer: 'tmpl-hh__swiper-container',
			tabActive: 'tmpl-hh__content-tab--active',
			content: 'tmpl-hh__content',
			contentActive: 'tmpl-hh__content--active',
			contentOpacity1: 'tmpl-hh__content--opacity-1',
		};

		let contents,
			tabs,
			classPrefix = 'tmpl-hh__content__';

		let updateActiveSwipers = function () {
			let contents = document.getElementsByClassName(classes.contentActive);

			for (let i = 0; i < contents.length; i++) {
				let swipers = contents[i].getElementsByClassName(classes.swiperContainer);
				for (let i2 = 0; i2 < swipers.length; i2++) {
					if(swipers[i2].swiper){
						swipers[i2].swiper.update();
					}
				}
			}
		};
		let change = function (contentTag) {
			let contents = document.getElementsByClassName(classPrefix + contentTag);

			hideAll(contentTag);
			deactivateAllTabs();

			if(callback){
				callback(contentTag);
			}

			setTimeout(function () {
				show(contents);
				setTimeout(updateActiveSwipers, 50);
			}, 400);

			let activeTabSelector = '.' + classes.tab + '[href="#' + contentTag + '"]',
				activeTabs = document.querySelectorAll(activeTabSelector);

			for (let i = 0; i < activeTabs.length; i++) {
				activeTabs[i]
					.classList
					.add(classes.tabActive);
			}

			if (window.location.hash.substr(1) !== contentTag) {
				window.location.hash = '#' + contentTag;
			}
		};
		let hideAll = function (exceptTag) {
			let exceptClass = classPrefix + exceptTag;
			for (let i = 0; i < contents.length; i++) {
				let content = contents[i];

				if (!content.classList.contains(exceptClass)) {
					content.classList.remove(classes.contentOpacity1);
					setTimeout(function () {
						content.classList.remove(classes.contentActive);
					}, 400);
				}
			}
		};
		let show = function (contents) {
			if (typeof contents !== "object") {
				contents = [contents];
			}

			for (let i = 0; i < contents.length; i++) {
				let content = contents[i];

				content.classList.add(classes.contentActive);
				setTimeout(function () {
					content.classList.add(classes.contentOpacity1);
				}, 50);
			}
		};
		let deactivateAllTabs = function () {
			for (let i = 0; i < tabs.length; i++) {
				tabs[i].classList.remove(classes.tabActive);
			}
		};
		let listenTabClick = function () {
			for (let i = 0; i < tabs.length; i++) {
				tabs[i].addEventListener('click', function () {
					let content = this.getAttribute('href').replace('#', '');
					change(content);
				});
			}
		};
		let getCurrentTab = function () {
			return tabs[0] && tabs[0].getAttribute('href')
				? tabs[0].getAttribute('href')
				: "";
		};
		let init = function () {
			contents = document.getElementsByClassName(classes.content);
			tabs = document.getElementsByClassName(classes.tab);

			let hash = window.location.hash;
			if (hash !== '' && hash !== getCurrentTab()) {
				setTimeout(change, 200, hash.substr(1));
			}

			listenTabClick();
		};

		init();
	}

	function closest(element, selector) {
		if (element.closest) {
			return element.closest(selector);
		}
		function closest(parentElement, selector) {
			if (!parentElement) return null;
			if (parentElement.matches(selector)) return parentElement;
			if (!parentElement.parentElement) return null;
			return closest(element.parentElement, selector);
		}

		return closest(element.parentElement, selector);
	}

	function Nav() {
		let nav, btn, opened = false;
		let classes = {
			nav: {
				base: 'tmpl-hh__nav',
				opened: 'tmpl-hh__nav--opened'
			},
			btn: {
				base: 'tmpl-hh__nav-btn',
				active: 'tmpl-hh__nav-btn--active',
				closed: 'tmpl-hh__nav-btn--closed'
			}
		};

		let close = function () {
			opened = false;
			nav.classList.remove(classes.nav.opened);
			btn.classList.remove(classes.btn.active);
			btn.classList.add(classes.btn.closed);
		};
		let open = function () {
			opened = true;
			nav.classList.add(classes.nav.opened);
			btn.classList.remove(classes.btn.closed);
			btn.classList.add(classes.btn.active);
		};
		let toggle = function () {
			if(opened){
				close();
			}else{
				open();
			}
		};
		let listenBtnClick = function () {
			btn.addEventListener('click', toggle);
		};
		let listenOutClick = function (){
			document.addEventListener('mousedown', function (event) {
				if (!event.target) return;
				if(!opened) return;
				if(event.target !== btn && !closest(event.target, '.' + classes.btn.base)){
					close();
				}
			});
		};
		let init = function () {
			nav = document.querySelector('.' + classes.nav.base);
			btn = document.querySelector('.' + classes.btn.base);

			listenOutClick();
			listenBtnClick();
		};

		init();
	}

	/*
		--------------------------------------------
		--------------------------------------------
						SLIDERS
		--------------------------------------------
		--------------------------------------------
	 */



	/*
		--------------------------------------------
		--------------------------------------------
							COMMON
		--------------------------------------------
		--------------------------------------------
	 */


	new Content();
	new Nav();

}());
