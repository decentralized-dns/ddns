$(window).on('load', function () {
	
	'use strict';
	
	/* Preloader */	
    var $preloader = $('#page-preloader'),
        $spinner   = $preloader.find('.spinner');
    $spinner.fadeOut();
    $preloader.delay(350).fadeOut('slow');
	
	/* Portfolio Index */
	var PORTFOLIO = (function($) {
	var $grid = $('#grid'),	$filterOptions = $('.portfolio-menu'),
		setupFilters = function() {
			var $btns = $filterOptions.children();
				$btns.on('click', function() {
				var $this = $(this),
				isActive = $this.hasClass( 'active' ),
				group = isActive ? 'all' : $this.data('group');
					if ( !isActive ) {
						$('.portfolio-menu .active').removeClass('active');
					}
			$this.toggleClass('active');
			$grid.shuffle( 'shuffle', group );
			});
			$btns = null;
		},
				init = function() {
					setupFilters();
					$grid.shuffle({
						itemSelector: '.col-md-3, .col-md-4',
					});
				};
		return {init: init};
	}(jQuery));

	PORTFOLIO.init();
});

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
