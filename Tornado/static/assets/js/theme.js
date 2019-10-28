;
(function($) {
  "use strict"

  /*----------------------------------------------------*/
  /*  Parallax Effect js
  /*----------------------------------------------------*/
  function parallaxEffect() {
    $('.bg-parallax').parallax();
  }
  parallaxEffect();

  /*----------------------------------------------------*/
  /*  Isotope Fillter js
  /*----------------------------------------------------*/
  function gallery_isotope() {
    if ($('.gallery_f_inner').length) {
      // Activate isotope in container
      $(".gallery_f_inner").imagesLoaded(function() {
        $(".gallery_f_inner").isotope({
          layoutMode: 'fitRows',
          animationOptions: {
            duration: 750,
            easing: 'linear'
          }
        });
      });

      // Add isotope click function
      $(".gallery_filter li").on('click', function() {
        $(".gallery_filter li").removeClass("active");
        $(this).addClass("active");

        var selector = $(this).attr("data-filter");
        $(".gallery_f_inner").isotope({
          filter: selector,
          animationOptions: {
            duration: 450,
            easing: "linear",
            queue: false,
          }
        });
        return false;
      });
    }
  }
  gallery_isotope();


  /*----------------------------------------------------*/
  /*  Testimonials Slider
  /*----------------------------------------------------*/
  function testimonials_slider() {
    if ($('.t_slider').length) {
      $('.t_slider').owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        nav: true,
        autoplay: false,
        smartSpeed: 1500,
        animateOut: 'slideOutUp',
        animateIn: 'slideInUp',
        dots: true,
        navContainer: '.testimonials_area',
        navText: ['<i class="lnr lnr-arrow-up"></i>', '<i class="lnr lnr-arrow-down"></i>'],
        responsiveClass: true,
      })
    }
  }
  testimonials_slider();

  /*----------------------------------------------------*/
  /*  MailChimp Slider
  /*----------------------------------------------------*/
  function mailChimp() {
    $('#mc_embed_signup').find('form').ajaxChimp();
  }
  mailChimp();

  $('select').niceSelect();

  /*----------------------------------------------------*/
  /*  Simple LightBox js
  /*----------------------------------------------------*/
  $('.imageGallery1 .light').simpleLightbox();

})(jQuery)
