$(window).on('load', function () {

	'use strict';

	/* Preloader */
    var $preloader = $('#page-preloader'),
        $spinner   = $preloader.find('.spinner');
    $spinner.fadeOut();
    $preloader.delay(350).fadeOut('slow');

$(document).ready(function() {

	'use strict';

	/* Animations Home Page*/
	function onScrollInit( items, trigger ) {
	    items.each( function() {
	    var osElement = $(this),
	    osAnimationClass = osElement.attr('data-animation'),
	    osAnimationDelay = osElement.attr('data-animation-delay');

	    osElement.css({
	    '-webkit-animation-delay':  osAnimationDelay,
	    '-moz-animation-delay':     osAnimationDelay,
	    'animation-delay':          osAnimationDelay
	    });

	    var osTrigger = ( trigger ) ? trigger : osElement;

	    osTrigger.waypoint(function() {
	    osElement.addClass('animated').addClass(osAnimationClass);
	    },{
	        triggerOnce: true,
	        offset: '90%'
	    });
	    });
	    }
		onScrollInit( $('.scroll-animation') );
	    onScrollInit( $('.staggered-animation'), $('.staggered-animation-container') );

});

// const form = document.getElementById("manage-form");
// const select = document.getElementById("register_select");
//
// form.addEventListener("submit", (event) => {
//   event.preventDefault();
//
//   let url;
//   let formData = new FormData(form);
//
//   switch (select.value) {
//     case "register":
//       url = "/register";
//       break;
//     case "extend":
//       url = "/extend";
//       break;
//     case "renew":
//       url = "/renew";
//       break;
//   }
//
//   fetch(url, {
//     method: "GET",
//     body: formData,
//   })
//     .then((response) => response.text())
//     .then((text) => {
//       document.body.innerHTML = text;
//     });
// });
