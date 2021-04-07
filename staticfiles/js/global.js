$(document).ready(function() {
    var _createClass = function() {
        function defineProperties(target, props) {
            for (var i = 0; i < props.length; i++) {
                var descriptor = props[i];
                descriptor.enumerable = descriptor.enumerable || false;
                descriptor.configurable = true;
                if ("value" in descriptor) descriptor.writable = true;
                Object.defineProperty(target, descriptor.key, descriptor);
            }
        }
        return function(Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; };
    }();

    function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

    var $window = $(window);
    var $body = $('body');

    var Slideshow = function() {
        function Slideshow() {
            var _this = this;

            var userOptions = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};

            _classCallCheck(this, Slideshow);

            var defaultOptions = {
                $el: $('.slideshow'),
                showArrows: false,
                showPagination: true,
                duration: 5000,
                autoplay: true
            };

            var options = Object.assign({}, defaultOptions, userOptions);

            this.$el = options.$el;
            this.maxSlide = this.$el.find($('.js-slider-home-slide')).length;
            this.showArrows = this.maxSlide > 1 ? options.showArrows : false;
            this.showPagination = options.showPagination;
            this.currentSlide = 1;
            this.isAnimating = false;
            this.animationDuration = 1200;
            this.autoplaySpeed = options.duration;
            this.interval;
            this.$controls = this.$el.find('.js-slider-home-button');
            this.autoplay = this.maxSlide > 1 ? options.autoplay : false;

            this.$el.on('click', '.js-slider-home-next', function(event) {
                return _this.nextSlide();
            });
            this.$el.on('click', '.js-slider-home-prev', function(event) {
                return _this.prevSlide();
            });
            this.$el.on('click', '.js-pagination-item', function(event) {
                if (!_this.isAnimating) {
                    _this.preventClick();
                    _this.goToSlide(event.target.dataset.slide);
                }
            });

            this.init();
        }

        _createClass(Slideshow, [{
            key: 'init',
            value: function init() {
                this.goToSlide(1);

                /* if (this.showArrows) {
                   this.$el.append(`<div class="c-header-home_footer">
                <div class="o-container">
                <div class="c-header-home_controls -nomobile o-button-group">
                      <div class="js-parallax is-inview" data-speed="1" data-position="top" data-target="#js-header">
                          <button class="o-button -white -square -left js-slider-home-button js-slider-home-prev" type="button">
                              <span class="o-button_label">
                                  <svg class="o-button_icon" role="img"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-prev"></use></svg>
                              </span>
                          </button>
                          <button class="o-button -white -square js-slider-home-button js-slider-home-next" type="button">
                              <span class="o-button_label">
                                  <svg class="o-button_icon" role="img"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#arrow-next"></use></svg>
                              </span>
                          </button>
                      </div>
                </div>
                </div>
                </div>`);
                 }
                 */
                if (this.autoplay) {
                    this.startAutoplay();
                }

                if (this.showPagination) {
                    var paginationNumber = this.maxSlide;
                    var pagination = '<div class="pagination"><div class="container">';

                    for (var i = 0; i < this.maxSlide; i++) {
                        var item = '<span class="pagination__item js-pagination-item ' + (i === 0 ? 'is-current' : '') + '" data-slide=' + (i + 1) + '>' + (i + 1) + '</span>';
                        pagination = pagination + item;
                    }

                    pagination = pagination + '</div></div>';

                    this.$el.append(pagination);
                }
            }
        }, {
            key: 'preventClick',
            value: function preventClick() {
                var _this2 = this;

                this.isAnimating = true;
                this.$controls.prop('disabled', true);
                clearInterval(this.interval);

                setTimeout(function() {
                    _this2.isAnimating = false;
                    _this2.$controls.prop('disabled', false);
                    if (_this2.autoplay) {
                        _this2.startAutoplay();
                    }
                }, this.animationDuration);
            }
        }, {
            key: 'goToSlide',
            value: function goToSlide(index) {
                this.currentSlide = parseInt(index);

                if (this.currentSlide > this.maxSlide) {
                    this.currentSlide = 1;
                }

                if (this.currentSlide === 0) {
                    this.currentSlide = this.maxSlide;
                }

                var newCurrent = this.$el.find('.js-slider-home-slide[data-slide="' + this.currentSlide + '"]');
                var newPrev = this.currentSlide === 1 ? this.$el.find('.js-slider-home-slide').last() : newCurrent.prev('.js-slider-home-slide');
                var newNext = this.currentSlide === this.maxSlide ? this.$el.find('.js-slider-home-slide').first() : newCurrent.next('.js-slider-home-slide');

                this.$el.find('.js-slider-home-slide').removeClass('is-prev is-next is-current');
                this.$el.find('.js-pagination-item').removeClass('is-current');

                if (this.maxSlide > 1) {
                    newPrev.addClass('is-prev');
                    newNext.addClass('is-next');
                }

                newCurrent.addClass('is-current');
                this.$el.find('.js-pagination-item[data-slide="' + this.currentSlide + '"]').addClass('is-current');
            }
        }, {
            key: 'nextSlide',
            value: function nextSlide() {
                this.preventClick();
                this.goToSlide(this.currentSlide + 1);
            }
        }, {
            key: 'prevSlide',
            value: function prevSlide() {
                this.preventClick();
                this.goToSlide(this.currentSlide - 1);
            }
        }, {
            key: 'startAutoplay',
            value: function startAutoplay() {
                var _this3 = this;

                this.interval = setInterval(function() {
                    if (!_this3.isAnimating) {
                        _this3.nextSlide();
                    }
                }, this.autoplaySpeed);
            }
        }, {
            key: 'destroy',
            value: function destroy() {
                this.$el.off();
            }
        }]);

        return Slideshow;
    }();

    (function() {
        var loaded = false;
        var maxLoad = 3000;

        function load() {
            var options = {
                showPagination: true
            };

            var slideShow = new Slideshow(options);
        }

        function addLoadClass() {
            $body.addClass('is-loaded');

            setTimeout(function() {
                $body.addClass('is-animated');
            }, 600);
        }

        $window.on('load', function() {
            if (!loaded) {
                loaded = true;
                load();
            }
        });

        setTimeout(function() {
            if (!loaded) {
                loaded = true;
                load();
            }
        }, maxLoad);

        addLoadClass();
    })();

    $('.webform select').selectric();

    $("input[type=file]").change(function() {
        var filename = $(this).val().replace(/C:\\fakepath\\/i, '');
        if (filename != "") {
            $(this).parent().find('p').text(filename);
        } else {
            $(this).parent().find('p').text("No file choosen");
        }
    });

    $('.webform .academic-table td input').focusout(function() {
        $('.applynow-wrap .academic-table tr').removeClass('active');
    });
    $('.webform .academic-table td input').focus(function() {
        $('.applynow-wrap .academic-table tr').removeClass('active');
        $(this).parents('tr').addClass('active');
    });





    $(document).on('click', '.hammenu-wrap .hammenu', function() {
        $('.main-menu-nav').toggleClass('menu-open');
        $(this).toggleClass('open');
    });

    $(document).on('click', '.hammenu-wrap .hammenu.open', function() {
        setTimeout(function() {
            $('.drop-menu_wrap').removeClass('menu-opened-state');
        }, 1000);
    });


    $(document).on('click', '.main-menu-nav li.menu-dropdown', function() {
        $(this).parents('.main-menu-nav').addClass('menu-opened-state');
        $(this).find('.drop-menu_wrap').addClass('menu-opened-state');
    });

    $(document).on('click', 'a.back-button-link', function(e) {
        e.stopPropagation();
        $(this).parents('.main-menu-nav').removeClass('menu-opened-state');
        $(this).parents('.drop-menu_wrap').removeClass('menu-opened-state');
    });


    /* news scroller */
    var scroll_list = $('.headnews-scroller ul li');
    var scroll_len = scroll_list.length;
    var scroll_init = 0;
    scroll_list.eq(scroll_init).addClass('active');
    // var scroll_inter = setInterval(function scrollfn(){
    //     scroll_init++;
    //     scroll_list.removeClass('active inactive');
    //     if(scroll_init < scroll_len){
    //         scroll_list.eq(scroll_init-1).addClass('inactive ');
    //         scroll_list.eq(scroll_init).addClass('active ');
    //     }
    //     else{
    //         scroll_init = 0;
    //         scroll_list.eq(scroll_len-1).addClass('inactive ');
    //         scroll_list.eq(scroll_init).addClass('active ');
    //     }
    //     //var scroll_wid =  $('.headnews-scroller ul').outerWidth();
    //     //var list_wid = scroll_list.eq(scroll_init).outerWidth();

    //     //if(list_wid > scroll_wid){
    //     //    clearInterval(scroll_inter);
    //     //    var diff_wid = list_wid - scroll_wid;
    //     //    scroll_list.eq(scroll_init).animate({
    //     //        'left': -1 * diff_wid
    //     //    },2000,'swing',function(){
    //     //        setInterval(scrollfn,2000);
    //     //    });
    //     //}
    // },4000);



    /* banner-event-slider */
    var banner_event_slider = $('.banner-content .banner-right .event-slider');
    banner_event_slider.owlCarousel({
        loop: true,
        items: 1,
        nav: true,
        dots: false,
        autoplay: true,
        autoplayTimeout: 8000,
        smartSpeed: 900,
        autoplaySpeed: 900,
        autoplayHoverPause: true,
        navText: ["<span class='web_next'></span>", "<span class='web_prev'></span>"]
    });

    /* home-ranking slider */
    $('.ranking_slider').owlCarousel({
        loop: true,
        items: 1,
        nav: true,
        dots: false,
        autoplay: true,
        autoplayTimeout: 3000,
        smartSpeed: 900,
        autoplaySpeed: 900,
        autoplayHoverPause: true,
        navText: ["<span class='web_next'></span>", "<span class='web_prev'></span>"]
    });

    /* home-achievement slider */
    $('.achieve_sec .achieve-slider .slider').owlCarousel({
        loop: true,
        items: 1,
        nav: true,
        dots: false,
        //autoplay: true,
        autoplayTimeout: 3000,
        smartSpeed: 900,
        autoplaySpeed: 900,
        autoplayHoverPause: true,
        navText: ["<span class='web_next'></span>", "<span class='web_prev'></span>"]
    });

    /* home-review slider*/
    $('.review_slider').owlCarousel({
        loop: true,
        items: 1,
        nav: false,
        dots: true,
        autoplay: true,
        autoplayTimeout: 3000,
        smartSpeed: 900,
        autoplaySpeed: 900,
        autoplayHoverPause: true
    });

    $('.board_trustes_slder').owlCarousel({
        loop: true,
        items: 3,
        margin: 30,
        nav: true,
        dots: false,
        autoplay: true,
        autoplayTimeout: 3000,
        smartSpeed: 900,
        autoplaySpeed: 900,
        autoplayHoverPause: true,
        navContainer: '.board_navslide',
        responsive: {
            0: {
                items: 2,
                mouseDrag: true,
                autoplay: true,
                loop: true,
                dots: true
            },
            480: {
                items: 3,
                mouseDrag: true,
                autoplay: true,
                loop: true
            },
            991: {
                items: 3,
                mouseDrag: true,
                autoplay: true,
                loop: true
            }
        }
    });
    $('.board_trustes_slder_hh').owlCarousel({
        loop: true,
        items: 3,
        margin: 30,
        nav: true,
        dots: false,
        autoplay: true,
        autoplayTimeout: 3000,
        smartSpeed: 900,
        autoplaySpeed: 900,
        autoplayHoverPause: true,
        navContainer: '.board_navslide',
        responsive: {
            0: {
                items: 1,
                mouseDrag: true,
                autoplay: true,
                loop: true,
                dots: true
            },
            480: {
                items: 2,
                mouseDrag: true,
                autoplay: true,
                loop: true
            },
            991: {
                items: 3,
                mouseDrag: true,
                autoplay: true,
                loop: true
            }
        }
    });

    $('.our_recruiters_slide').owlCarousel({
        loop: false,
        items: 6,
        margin: 30,
        nav: true,
        dots: false,
        autoplay: false,
        autoplayTimeout: 3000,
        smartSpeed: 900,
        autoplaySpeed: 900,
        autoplayHoverPause: false,
        navContainer: '.board_navslide',
        responsive: {
            0: {
                items: 2,
                mouseDrag: true,
                autoplay: true,
                loop: false,
                dots: true,
                margin: 10
            },
            480: {
                items: 3,
                mouseDrag: true,
                autoplay: true,
                loop: false,
                margin: 10
            },
            991: {
                items: 6,
                mouseDrag: true,
                autoplay: true,
                loop: false
            }
        }
    });



    /* home-banner hover animation */
    $('.banner-left .banner-boxcontent .row > div').each(function() {
        $(this).hoverdir();
    });


    /* home-infra hover animation */
    $('.infra_sec .col-sm-8 .great_infra .col-sm-4 > div').each(function() {
        $(this).hoverdir();
    });

    $('.gallery_page .gallery_sec ul li').each(function() {
        $(this).hoverdir();
    });

    /* SVG sprite including*/
    //$.get('img/sprite.txt', function(data) {
    //    console.log(data);
    //});


    $(document).on('click', '.main-menu-nav .container > ul > li .search-menu a', function(e) {
        e.preventDefault();
        $('.main-menu-nav .container .search-container').slideToggle();
        $('.main-menu-nav .container .search-container input').focus();
    });
    $(document).on('click', '.main-menu-nav .container .search-container span.close-search', function(e) {
        e.preventDefault();
        $('.main-menu-nav .container .search-container').slideUp();
        $('.main-menu-nav .container .search-container input').val("");
    });




    $('.fancybox').fancybox();

    $(".map_pin").click(function() {
        $('.contact_banner').toggleClass("map_class");
    });


    $('.grid-layout').masonry({
        // options
        itemSelector: '.grid-item'
    });


    $('body').append("<div class='modal-backdrop'></div>");
    $(document).on('click', '.modal-link', function(e) {
        e.preventDefault();
        var target = $(this).attr('data-target');
        $(target).addClass('modal-open');
        $('.modal-backdrop').addClass('overlay');
    });


    $('li#mega-menu-item-53 .mega-menu-link').click(function() {
        $('#car_modal').addClass("modal-open");
    });



    $('body').append("<div class='modal-backdrop'></div>");
    $(document).on('click', 'li#mega-menu-item-53 .mega-menu-link', function(e) {
        e.preventDefault();
        var target = $(this).attr('data-target');
        $('#car_modal').addClass('modal-open');
        $('.modal-backdrop').addClass('overlay');
    });


    $(document).on('click', '.web-modal.modal-open', function(e) {
        e.preventDefault();
        $('.modal-backdrop').removeClass('overlay');
        $('.web-modal').removeClass('modal-open');
    });

    $(document).on('click', '.web-modal.modal-open .modal-dialog', function(e) {
        e.stopPropagation();
    });

    $(document).on('click', '.web-modal.modal-open button.close', function(e) {
        e.preventDefault();
        $('.modal-backdrop').removeClass('overlay');
        $('.web-modal').removeClass('modal-open');
    });


    //  $(document).on('click', '.media-video .modal-link', function () {
    //    var data_url = $(this).attr('data-url');
    //    var final_url = data_url + "?start=0&amp;rel=0&amp;autoplay=1&amp;showinfo=0";
    //    $('#mediamodal').find('video').attr('src', final_url);
    //  });

    $(document).on('click', '#mediamodal.web-modal,#mediamodal button.close', function(e) {
        $('#mediamodal').find('video').attr('src', "");
    });


    $(document).on('click', 'course-tab-contain .tab-menu li a', function(e) {
        var tabindex = $(this).parent().index();
        var leftpos = 0;
        for (var i = 0; i < tabindex; i++) {
            leftpos = leftpos + $('course-tab-contain .tab-menu li').eq(i).outerWidth() - 1;
        }
        $('course-tab-contain .tab-menu').animate({
            scrollLeft: leftpos
        }, 500);
    });


    $(document).on('click', '.course-tab-contain .tab-menu ul li a', function(e) {
        var course_tabindex = $(this).parent().index();
        var course_leftpos = 0;
        for (var i = 0; i < course_tabindex; i++) {
            course_leftpos = course_leftpos + $('.course-tab-contain .tab-menu ul li').eq(i).outerWidth();
        }
        $('.course-tab-contain .tab-menu ul').animate({
            scrollLeft: course_leftpos
        }, 500);
    });


    document.addEventListener('gesturestart', function(e) {
        e.preventDefault();
    });


    //$('.news-wrapper ul').marquee({
    //    duration: 20000,
    //    duplicated: true
    //});

    //$('marquee').marquee(optionalClass);
});

$(window).scroll(function(event) {
    var scroll = $(window).scrollTop();
    if (scroll >= 250)
        $('.main-menu-nav').addClass('sticky-head');
    else
        $('.main-menu-nav').removeClass('sticky-head');


    if (scroll >= 500)
        $('.main-menu-nav').addClass('show');
    else
        $('.main-menu-nav').removeClass('show');
});

var tween;
var init = $('.headnews-scroller .container').width();

function marq(init) {
    tween = TweenMax.fromTo($(".headnews-scroller ul"), 500, {
        x: init
    }, {
        x: -($('.headnews-scroller ul').width()),
        ease: Linear.easeNone,
        repeat: -1
    });
}
$(document).ready(function() {
    marq(init);
    $(".headnews-scroller").mouseover(function() {
        tween.pause();
    });
    $(".headnews-scroller").mouseout(function() {
        tween.play();
    });
});


// $('.content-only img').wrap('<div><div class="ach_sec"><div class="col-sm-3"><div><a class="fancybox" title="Best alumni award the best alumni of the year was awarded to dr.j.umarani,2002 batch it student who is successful in her career"></a></div></div></div></div>');

$('.content-only h4').addClass('clearfix');
$('.content-only h3').addClass('clearfix');
$('.content-only span').addClass('clearfix');




//Open Link in new Tab


$(document).ready(function() {
    $('.acsalumni_link a').attr('target', '_blank');
});

$(document).ready(function() {
    $('.menu-item-47 a').attr('target', '_blank');
});

$(document).ready(function() {
    $('.menu-item-48 a').attr('target', '_blank');
});

$(document).ready(function() {
    $('.menu-item-4185 a').attr('target', '_blank');
});

$(document).ready(function() {
    $('.menu-item-29 a').attr('target', '_blank');
});

// $(document).ready(function() {
//     var swiper = new Swiper('.blog-slider', {
//         spaceBetween: 30,
//         effect: 'fade',
//         loop: true,
//         sensitivity: 100,
//         mousewheel: {
//             invert: true,
//         },
//         // autoHeight: true,
//         pagination: {
//             el: '.blog-slider__pagination',
//             clickable: true,
//         }
//     });

//     $("body").on("click", "a[data-href]", function() {
//         var href = $(this).data("href");
//         if (href) {
//             location.href = href;
//         }
//     });
// });

/*
 * My adaptation of:
 *   Flux 3D Carousel
 *   Author: Dean Coulter
 *   Licensed under the MIT license
 *   Version 0.1
 *
 *   - Changed from figure element cards to any html.
 *   - Removed use of id, to allow multiple carousels.
 *   - Blocking of events on cards in the background.
 *   - Dimming of cards in the background.
 *   - Fixed continuous rotation.
 *   - Added functionality for multiple carousels.
 *   - Adding clickable arrow icon buttons on the sides.
 */
function cardCarousel3d(carousels) {
    var rotateHandler = function(evt) {
        var carousel = this.parentElement;
        if (carousel.classList.contains('card-carousel') === false) {
            var carousel = carousel.parentElement;
        }
        var rotate_int = parseInt(carousel.dataset.rotateInt || 0);
        if (this.classList.contains('counterclockwise')) {
            rotate_int += 1;
        } else if (this.classList.contains('clockwise')) {
            rotate_int -= 1;
        }
        carousel.dataset.rotateInt = rotate_int;
        animate_slider(carousel);
    }
    for (var i = 0; i < carousels.length; i++) {
        var carousel = carousels[i];
        var inner = carousel.querySelector('.inner-carousel');
        var cards = carousel.querySelectorAll('.inner-carousel > div');
        var size = cards.length;
        var panelSize = inner.clientWidth;
        var translateZ = Math.round((panelSize / 2) / Math.tan(Math.PI / size)) * 1.7;
        inner.style.transform = "rotateY(0deg) translateZ(-" + translateZ + "px)";
        var btnLeft = carousel.querySelector('.button-spin.counterclockwise');
        if (btnLeft !== null) {
            btnLeft.addEventListener("click", rotateHandler, false);
        }
        var btnRight = carousel.querySelector('.button-spin.clockwise');
        if (btnRight !== null) {
            btnRight.addEventListener("click", rotateHandler, false);
        }
        animate_slider(carousel);
    }

    function animate_slider(carousel) {
        var rotate_int = parseInt(carousel.dataset.rotateInt || 0);
        var inner = carousel.querySelector('.inner-carousel');
        var cards = carousel.querySelectorAll('.inner-carousel > div');
        var size = cards.length;
        var panelSize = inner.clientWidth;
        var translateZ = Math.round((panelSize / 2) / Math.tan(Math.PI / size)) * 1.7;
        var rotateY = 0;
        var ry = 360 / size;
        rotateY = ry * rotate_int;

        for (var i = 0; i < size; i++) {
            var z = (rotate_int * ry) + (i * ry);
            var child = cards[i];
            child.style.transform = "rotateY(" + z + "deg) translateZ(" + translateZ + "px) rotateY(" + (-z).toString() + "deg)";
            child.classList.remove('clockwise');
            child.classList.remove('front');
            child.classList.remove('counterclockwise');
            child.removeEventListener("click", rotateHandler, false);
            var zz = z % 360;
            if (zz === 0) {
                child.classList.add('front');
            } else if (zz === ry || zz === -360 + ry) {
                child.classList.add('clockwise');
                child.addEventListener("click", rotateHandler, false);
            } else if (zz === 360 - ry || zz === 0 - ry) {
                child.classList.add('counterclockwise');
                child.addEventListener("click", rotateHandler, false);
            }
        }
    }
}

cardCarousel3d(document.querySelectorAll('.card-carousel'));