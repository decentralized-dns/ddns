$(document).ready(function () {
  "use strict";

  /* Animations Home Page*/
  function onScrollInit(items, trigger) {
    items.each(function () {
      var osElement = $(this),
        osAnimationClass = osElement.attr("data-animation"),
        osAnimationDelay = osElement.attr("data-animation-delay");

      osElement.css({
        "-webkit-animation-delay": osAnimationDelay,
        "-moz-animation-delay": osAnimationDelay,
        "animation-delay": osAnimationDelay,
      });

      var osTrigger = trigger ? trigger : osElement;

      osTrigger.waypoint(
        function () {
          osElement.addClass("animated").addClass(osAnimationClass);
        },
        {
          triggerOnce: true,
          offset: "90%",
        }
      );
    });
  }
  onScrollInit($(".scroll-animation"));
  onScrollInit($(".staggered-animation"), $(".staggered-animation-container"));
});
