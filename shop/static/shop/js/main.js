
$( document ).ready(function() {
	$('.header_burger').click(function(event) {
		$('.header_burger,.header_menu').toggleClass('active');
		$('body').toggleClass('lock');
	});
});
"use strict"

const isMobile = {
	Android: function () {
		return navigator.userAgent.match(/Android/i);
	},
	BlackBerry: function () {
		return navigator.userAgent.match(/BlackBerry/i);
	},
	iOS: function () {
		return navigator.userAgent.match(/iPhone|IPad|IPod/i);
	},
	Opera: function () {
		return navigator.userAgent.match(/Opera Mini/i);
	},
	Windows: function () {
		return navigator.userAgent.match(/IEMobile/i);
	},
	any: function () {
		return (
			isMobile.Android() ||
			isMobile.BlackBerry() ||
			isMobile.iOS() ||
			isMobile.Opera() ||
			isMobile.Windows());
	}
};

if (isMobile.any()) {
	document.body.classList.add('_touch');

	let menuArrows = document.querySelectorAll('.menu__arrow');
	if (menuArrows.length > 0) {
		for (let index = 0; index < menuArrows.length; index++) {
			const menuArrow = menuArrows[index];
			menuArrow.addEventListener ("click", function (e) {
				menuArrow.parentElement.classList.toggle('_active');
			});
		}
	}

}else{
	document.body.classList.add('_pc');
}

//Burger-menu

const iconMenu = document.querySelector('.menu__icon');
const menuBody = document.querySelector('.menu__body');
if (iconMenu){
	iconMenu.addEventListener("click", function(e) {
		document.body.classList.toggle('_lock');
		iconMenu.classList.toggle('_active');
		menuBody.classList.toggle('_active');
	});
}
if (document.querySelector('.slider-main__body')) {
  const swiper = new Swiper('.slider-main__body', {
    observer: true,
    observeParents: true,
    slidesPerView: 1,
    spaceBetween: 32,
    watchOverflow: true,
    speed: 800,
    loop: true,
    loopAdditionalSlides: 5,
    preloadImages: false,
    parallax: true,
    //Dotts
    pagination: {
      el: '.controls-slider-main__dotts',
      clickable: true,
    },
    //Arrows
    navigation: {
    nextEl: '.slider-main .slider-arrow_next',
    prevEl: '.slider-main .slider-arrow_prev',
    },
  });
}

$(document).ready(function() {
	if ( $(window).width() < 768 ) {
		$('.menu-footer__title').click(function(event) {
			if($('.footer__menu').hasClass('one')) {
				$('.menu-footer__title').not($(this)).removeClass('active');
				$('.menu-footer__list').not($(this).next()).slideUp(300);
			}
			$(this).toggleClass('active').next().slideToggle(300);
		});
	}
});
function ibg(){
	$.each($('.ibg'), function(index, val) {
		if($(this).find('img').length>0){
			$(this).css('background-image','url("'+$(this).find('img').attr('src')+'")');
		}
	});
}

ibg();
// Dynamic Adapt v.1
// HTML data-da="where(uniq class name),when(breakpoint),position(digi)"
// e.x. data-da=".item,992,2"
// Andrikanych Yevhen 2020
// https://www.youtube.com/c/freelancerlifestyle

"use strict";

function DynamicAdapt(type) {
	this.type = type;
}

DynamicAdapt.prototype.init = function () {
	const _this = this;
	// ???????????? ????????????????
	this.??bjects = [];
	this.daClassname = "_dynamic_adapt_";
	// ???????????? DOM-??????????????????
	this.nodes = document.querySelectorAll("[data-da]");

	// ???????????????????? ??bjects ????????????????
	for (let i = 0; i < this.nodes.length; i++) {
		const node = this.nodes[i];
		const data = node.dataset.da.trim();
		const dataArray = data.split(",");
		const ??bject = {};
		??bject.element = node;
		??bject.parent = node.parentNode;
		??bject.destination = document.querySelector(dataArray[0].trim());
		??bject.breakpoint = dataArray[1] ? dataArray[1].trim() : "767";
		??bject.place = dataArray[2] ? dataArray[2].trim() : "last";
		??bject.index = this.indexInParent(??bject.parent, ??bject.element);
		this.??bjects.push(??bject);
	}

	this.arraySort(this.??bjects);

	// ???????????? ???????????????????? ??????????-????????????????
	this.mediaQueries = Array.prototype.map.call(this.??bjects, function (item) {
		return '(' + this.type + "-width: " + item.breakpoint + "px)," + item.breakpoint;
	}, this);
	this.mediaQueries = Array.prototype.filter.call(this.mediaQueries, function (item, index, self) {
		return Array.prototype.indexOf.call(self, item) === index;
	});

	// ?????????????????????? ?????????????????? ???? ??????????-????????????
	// ?? ?????????? ?????????????????????? ?????? ???????????? ??????????????
	for (let i = 0; i < this.mediaQueries.length; i++) {
		const media = this.mediaQueries[i];
		const mediaSplit = String.prototype.split.call(media, ',');
		const matchMedia = window.matchMedia(mediaSplit[0]);
		const mediaBreakpoint = mediaSplit[1];

		// ???????????? ???????????????? ?? ???????????????????? ????????????????????????
		const ??bjectsFilter = Array.prototype.filter.call(this.??bjects, function (item) {
			return item.breakpoint === mediaBreakpoint;
		});
		matchMedia.addListener(function () {
			_this.mediaHandler(matchMedia, ??bjectsFilter);
		});
		this.mediaHandler(matchMedia, ??bjectsFilter);
	}
};

DynamicAdapt.prototype.mediaHandler = function (matchMedia, ??bjects) {
	if (matchMedia.matches) {
		for (let i = 0; i < ??bjects.length; i++) {
			const ??bject = ??bjects[i];
			??bject.index = this.indexInParent(??bject.parent, ??bject.element);
			this.moveTo(??bject.place, ??bject.element, ??bject.destination);
		}
	} else {
		for (let i = 0; i < ??bjects.length; i++) {
			const ??bject = ??bjects[i];
			if (??bject.element.classList.contains(this.daClassname)) {
				this.moveBack(??bject.parent, ??bject.element, ??bject.index);
			}
		}
	}
};

// ?????????????? ??????????????????????
DynamicAdapt.prototype.moveTo = function (place, element, destination) {
	element.classList.add(this.daClassname);
	if (place === 'last' || place >= destination.children.length) {
		destination.insertAdjacentElement('beforeend', element);
		return;
	}
	if (place === 'first') {
		destination.insertAdjacentElement('afterbegin', element);
		return;
	}
	destination.children[place].insertAdjacentElement('beforebegin', element);
}

// ?????????????? ????????????????
DynamicAdapt.prototype.moveBack = function (parent, element, index) {
	element.classList.remove(this.daClassname);
	if (parent.children[index] !== undefined) {
		parent.children[index].insertAdjacentElement('beforebegin', element);
	} else {
		parent.insertAdjacentElement('beforeend', element);
	}
}

// ?????????????? ?????????????????? ?????????????? ???????????? ????????????????
DynamicAdapt.prototype.indexInParent = function (parent, element) {
	const array = Array.prototype.slice.call(parent.children);
	return Array.prototype.indexOf.call(array, element);
};

// ?????????????? ???????????????????? ?????????????? ???? breakpoint ?? place 
// ???? ?????????????????????? ?????? this.type = min
// ???? ???????????????? ?????? this.type = max
DynamicAdapt.prototype.arraySort = function (arr) {
	if (this.type === "min") {
		Array.prototype.sort.call(arr, function (a, b) {
			if (a.breakpoint === b.breakpoint) {
				if (a.place === b.place) {
					return 0;
				}

				if (a.place === "first" || b.place === "last") {
					return -1;
				}

				if (a.place === "last" || b.place === "first") {
					return 1;
				}

				return a.place - b.place;
			}

			return a.breakpoint - b.breakpoint;
		});
	} else {
		Array.prototype.sort.call(arr, function (a, b) {
			if (a.breakpoint === b.breakpoint) {
				if (a.place === b.place) {
					return 0;
				}

				if (a.place === "first" || b.place === "last") {
					return 1;
				}

				if (a.place === "last" || b.place === "first") {
					return -1;
				}

				return b.place - a.place;
			}

			return b.breakpoint - a.breakpoint;
		});
		return;
	}
};

const da = new DynamicAdapt("max");
da.init();