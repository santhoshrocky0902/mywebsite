var controller = new ScrollMagic.Controller();

/****************************** home ******************************/

/* splitting banner content */
//if($('#js_h1').length > 0){

$('.banner-content .banner-left .h1').each(function() {
    var h1_cont = $(this);
    h1_cont.html("<span>" + h1_cont.html().split("<br>").join("</span><span>"));
});

//}

/* menu - full width dropdown animation */
$('.fullwidmenu.one_time').hover(function() {
    var m_col1 = new TimelineLite();
    var m1_col1 = m_col1.fromTo('.fullwidmenu .dropmenu_link-wrap h3', 0.2, { y: 10, opacity: 0 }, { y: 0, opacity: 1 })
        .staggerFromTo('.fullwidmenu .dropmenu_link-wrap .dropmenu_links ul > li', 0.2, { y: 10, opacity: 0 }, { y: 0, opacity: 1 }, 0.01);

    var m_col2 = new TimelineLite();
    var m2_col2 = m_col2.fromTo('.fullwidmenu .dropmenu_link-wrap h3', 0.2, { y: 10, opacity: 0 }, { y: 0, opacity: 1 })
        .staggerFromTo('.fullwidmenu .dropmenu_intro >*', 0.2, { y: 10, opacity: 0 }, { y: 0, opacity: 1 }, 0.1);
});

//$(window).load(function(){

/* banner-slider */
var homecurrent = 1;
var home_totitems;
var banner_index;
var home_bnr_slider = $('.home-bnr-slider');
home_bnr_slider.owlCarousel({
    loop: true,
    items: 1,
    nav: false,
    dots: true,
    autoplay: true,
    autoplayTimeout: 4000,
    smartSpeed: 500,
    autoplaySpeed: 500,
    animateIn: 'fadeIn',
    animateOut: 'fadeOut',
    dotsContainer: '.banner-content .banner-left .dots-contain',
    onInitialized: function(e) {
        $('.banner-content .container > div .banner-left h1').addClass('active');
        home_totitems = $('.home-bnr-slider .owl-item:not(.cloned)').length;
        $('.banner-content .paginate-contain p .currrent-num').html(homecurrent);
        $('.banner-content .paginate-contain p .final-num').html(home_totitems);
    },
    onTranslated: function(e) {
        home_totitems = $('.home-bnr-slider .owl-item:not(.cloned)').length;
        banner_index = parseInt($('.home-bnr-slider .active .item').attr('data-index'));
        //if(banner_index > home_totitems){
        //	banner_index = 1;
        //}
        $('.banner-content .container > div .banner-left .h1').removeClass('active');
        $('.banner-content .container > div .banner-left .h1').eq(banner_index - 1).addClass('active');

        $('.banner-content .paginate-contain p .currrent-num').html(banner_index);
        $('.banner-content .paginate-contain p .final-num').html(home_totitems);
    }
});

if ($('.achieve_sec').length > 0) {
    /* banner animation */
    var loading_process = new TimelineLite();
    var top_sec = loading_process.fromTo('header', 0.8, { opacity: 0 }, { opacity: 1 })
        .fromTo('.headnews-scroller', 0.5, { opacity: 0 }, { opacity: 1 }, 0.5)
        .fromTo('.home-banner', 0.5, { opacity: 0 }, { opacity: 1 }, 0.6)
        .staggerFromTo('.banner-boxcontent .row > div', 0.8, { opacity: 0 }, { opacity: 1 }, 0.2)
        .fromTo('.banner-media.media-video', 0.5, { y: -10, opacity: 0 }, { y: 0, opacity: 1 }, 1.2)
        .fromTo('.event-slider-wrap', 0.5, { y: 10, opacity: 0 }, { y: 0, opacity: 1 }, 1.2)
        .fromTo('.banner-content .container > div .banner-left h1 span:first-child', 0.4, { y: -45 }, { y: 0 }, 1.4)
        .fromTo('.banner-content .container > div .banner-left h1 span:last-child', 0.4, { y: 45 }, { y: 0 }, 1.4)
        .fromTo('.banner-controls', 0.4, { opacity: 0 }, { opacity: 1 });
    new ScrollMagic.Scene({ triggerElement: '#wrapper', reverse: false, triggerHook: 'onEnter', offset: 250 }).setTween(top_sec).addTo(controller);



}
//});

function fadein(x, y) {
    var anim_elem = x;
    var trig_elem = y;
    var fadein1 = TweenMax.staggerFromTo(anim_elem, 1, { opacity: 0 }, { opacity: 1 }, 0.2);
    new ScrollMagic.Scene({ triggerElement: trig_elem, reverse: false, triggerHook: 'onEnter' }).setTween(fadein1).addTo(controller);
}

function fadeinup(x, y) {
    var anim_elem = x;
    var trig_elem = y;
    var fadeinup1 = TweenMax.staggerFromTo(anim_elem, 0.8, { y: 10 }, { y: 0, opacity: 1 }, 0.2);
    new ScrollMagic.Scene({ triggerElement: trig_elem, reverse: false, triggerHook: 'onEnter', offset: 250 }).setTween(fadeinup1).addTo(controller);
}

function fadeinleft(x, y) {
    var anim_elem = x;
    var trig_elem = y;
    var fadeinleft1 = TweenMax.staggerFromTo(anim_elem, 0.8, { x: -20 }, { x: 0, opacity: 1 }, 0.2);
    new ScrollMagic.Scene({ triggerElement: trig_elem, reverse: false, triggerHook: 'onEnter', offset: 250 }).setTween(fadeinleft1).addTo(controller);
}

function fadeinright(x, y) {
    var anim_elem = x;
    var trig_elem = y;
    var fadeinright1 = TweenMax.staggerFromTo(anim_elem, 0.8, { x: 20 }, { x: 0, opacity: 1 }, 0.2);
    new ScrollMagic.Scene({ triggerElement: trig_elem, reverse: false, triggerHook: 'onEnter', offset: 250 }).setTween(fadeinright1).addTo(controller);
}


/** dropdown menu hover arrow movement **/




//blur function
// function applyBlur()
// {
//     TweenMax.set($('.owl-item .item'), {webkitFilter:"blur(" + blurElement.a + "px)",ease: Power4.easeInOut}); 
// };

// var process_fade_in = new ScrollMagic.Scene({triggerElement: '#wrapper',reverse: false}).setTween(loading_process).addTo(controller);

var studies = new TimelineLite();
var studies1 = studies.fromTo('.card-callout ', 0.8, { y: 30, opacity: 0 }, { y: 0, opacity: 1 }, 0.2)
    .staggerFromTo('.card-flex-alt', 0.3, { y: 30, opacity: 0 }, { y: 0, opacity: 1 }, 0.05)
new ScrollMagic.Scene({ triggerElement: '.card-callout', reverse: false, triggerHook: 'onEnter', offset: 0 }).setTween(studies1).addTo(controller);

var studies2 = new TimelineLite();
var studies3 = studies2.fromTo('.view-content ', 0.3, { y: 30, opacity: 0 }, { y: 0, opacity: 1 }, 0.3)
    .staggerFromTo('.dcf-bleed', 0.3, { y: 30, opacity: 0 }, { y: 0, opacity: 1 }, 0.05)
new ScrollMagic.Scene({ triggerElement: '.view-content', reverse: false, triggerHook: 'onEnter', offset: 0 }).setTween(studies3).addTo(controller);