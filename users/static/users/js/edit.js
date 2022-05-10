$(window).on('load', function () {
    $('.loader').fadeOut(500, function () {
        // $(this).remove();
    });      
});

/*global $ */
$(document).ready(function ($) {
    'use strict';
 

    // Header cart 
    $('.middle-header .cart-header').click(function(){
        $('.middle-header .cart-dropdown').toggleClass('showcart');
    });

    $('.middle-header .cart-dropdown .close').click(function(){
        $('.middle-header .cart-dropdown').removeClass('showcart');
    });

    // $(document).on('click',function(){
    //     $('.middle-header .cart-dropdown').removeClass('showcart');
    // });

    // $('.middle-header .cart-header , .middle-header .cart-dropdown ').click(function(e){
    //     e.stopPropagation();
    // });


    // Header filter category
    $('.middle-header .filter-box').click(function(){
        $('.middle-header .search-categ li ul').slideUp();
        $('.middle-header .search-categ').toggleClass('show-cat');
    });

    $('.middle-header .search-categ p span').click(function(){
        $(this).parent().next().slideToggle();
        $(this).toggleClass('minus');
    });

    $('.middle-header .search-categ .expand').click(function(){
        $('.middle-header .search-categ li ul').slideDown();
        $('.middle-header .search-categ p span').addClass('minus');
    });

    $('.middle-header .search-categ .colapse').click(function(){
        $('.middle-header .search-categ li ul').slideUp();
        $('.middle-header .search-categ p span').removeClass('minus');
    });

    $(document).on('click',function(){
        $('.middle-header .search-categ').removeClass('show-cat');
    });

    $('.middle-header .filter-box , .middle-header .search-categ').click(function(e){
        e.stopPropagation();
    });


    // PC HEADER  MENUE 
    $('.bootom-header .btn-menu').click(function(){
        $('.bootom-header .main-list').toggleClass('show-menue');
    });

    $(document).on('click',function(){
        $('.bootom-header .main-list').removeClass('show-menue');
    });

    $('.bootom-header .btn-menu , .bootom-header .main-list').click(function(e){
        e.stopPropagation();
    });

    $('.bootom-header .show-more-cat').click(function(){
        $(this).toggleClass('minus');
        $('.bootom-header .main-ul').toggleClass('fixed-height');
    });

    // HEADER TABS 
    $('.bootom-header .side-menue .tab-link').click(function (e) {
        e.preventDefault();
        
        var itemId = $(this).attr("href");
        
        $('.bootom-header .cotents .block-contnet').removeClass('active-content'); 
        $(itemId).addClass('active-content');
        
        $('.bootom-header .side-menue .tab-link').removeClass('active-tap');
        $(this).addClass('active-tap')
    });

    // SEARCH POPUP 
    $('.open-search').click(function(){
        $('.search-popup').toggleClass('show');
    });

    $('.close-search').click(function(){
        $('.search-popup').removeClass('show');
    });

    
    // SIDE MENUE 
    $('.mobile-side-menu .main-ul .colapse-body').slideUp();

    $('.mobile-header .side-menu-btn').click(function(){
        $('.mobile-side-menu .main-ul').toggleClass('show');
        $('.mobile-side-menu .overlay').toggleClass('show');
        $('body').css('overflow','hidden');
    });

    $('.mobile-side-menu .colapse-btn').on('click',function(){
        $('.mobile-side-menu .main-ul .colapse-body').slideUp();
        $('.mobile-side-menu .icon').removeClass('rotate');
        if($(this).parent().find('.colapse-body').is(':visible')){
            $(this).parent().find('.colapse-body').slideUp();
        }else{
            $(this).parent().find('.colapse-body').slideDown();
        }
        $(this).find('.icon').addClass('rotate');
    });

    $('.mobile-side-menu .overlay').click(function(){
        $('.mobile-side-menu .main-ul').removeClass('show');
        $('.mobile-side-menu .overlay').removeClass('show');
        $('body').css('overflow-y','auto');
    });

    $('.mobile-side-menu .main-ul').click(function(e){
        e.stopPropagation();
    });


    // PRODUCTS TABS SLIDER 
    $('.products-section .tablist-slider a').click(function (e) {
        e.preventDefault();     
        var itemId = $(this).attr("href");
        var tablist = $(this).closest('.tablist-slider'); 

        tablist.closest('.products-section').find('.tab_content').removeClass('active'); 
        $(itemId).addClass('active');     

        tablist.find('a').removeClass('active-item');
        $(this).addClass('active-item')
    });

    // PRODUCT VIEW PICS
    $('.owl-hash-nav .item').click(function(){
        $('.owl-hash-nav .item').removeClass('active');
        $(this).addClass('active');
    });

    // SHOW BLOG SHARE 
    $('.show-share').click(function(){
        $(this).parent().find('.share-box').toggleClass('show');
    });

    // DELETE COMPARE PRODUCT 
    $('.main-side .compare-products .delete').click(function(){
        $(this).parent('.prod').remove();
    });


    // FAQ QUESTIONS SHOW ANSWER
    var quest   =  $('.question-box');
    var q_btn   =  quest.find('.question');
    var answer  =  quest.find('.answer');
    q_btn.click(function(){
        $(this).parent(quest).find(answer).slideToggle();
        $(this).find('.icon').toggleClass('plus');
    });


    // FAQ QUESTIONS CHANGE CONTENT
    $('.faq-side-cats .faqcat-link').click(function (e) {
        e.preventDefault();
        
        var itemId  =  $(this).attr("href");
        
        $('.all-Faq-cate .faq-cat').removeClass('active'); 
        $(itemId).addClass('active'); 
    });


    // RANGE SLIDER 
    $('#range-slider').slider({
        range: "max",
        min: 1,
        max: 500,
        isRTL: false,
        value: 1,
        slide: function( event, ui ) {
        $('#amount').val( ui.value );
        }
    });
    $('#amount').val( $('#range-slider').slider("value") );

    $('.reset-range').click(function(){
        $('#range-slider').slider("value", $('#range-slider').slider("option", "min") );
    });

    
    // STORE LOCATOR SEARCH 
    $('.locator-search-options .tabs-list a').click(function (e) {
        e.preventDefault();
        
        var itemId = $(this).attr("href");
        
        $('.locator-search-options .single-content').removeClass('active'); 
        $(itemId).addClass('active');
        
        $('.locator-search-options .tabs-list a').removeClass('active');
        $(this).addClass('active');
    });

    // SHOW CHANGE EMAIL FORM WHEN CHECKED 
    var email_ckbox = $('#change_email');
    email_ckbox.on('click',function () {
        if (email_ckbox.is(':checked')) {
            $('#change-email-form').addClass('show-form');
        } else {
            $('#change-email-form').removeClass('show-form');
        }
    });

    // SHOW CHANGE PASSWORD FORM WHEN CHECKED 
    var pass_ckbox = $('#change-password');
    pass_ckbox.on('click',function () {
        if (pass_ckbox.is(':checked')) {
            $('#change-password-form').addClass('show-form');
        } else {
            $('#change-password-form').removeClass('show-form');
        }
    });

    // DeELETE WISHLIST PRODUCT  
    $('.delete-whish-item').on('click',function () {
        $(this).closest('.whislist-product').remove();
    });


    //  PRODUCTS RANGE FILTER 
    $('#range-bar').slider({
        range: true,
        min: 0,
        max: 500,
        values: [ 75, 300 ],
        slide: function( event, ui ) {
            $('#range-min').val("$" + ui.values[ 0 ]);
            $('#range-max').val( "$" + ui.values[ 1 ]);
        }
    });
    $('#range-min').val("$" + $('#range-bar').slider( "values", 0 ));
    $('#range-max').val("$" + $('#range-bar').slider( "values", 1 ));


    // SHOW SELLER CATEGOREY
    $('.seller-categ-filter .cats_box .cat_head').click(function(){
        $(this).parent('.cats_box').find('.cat_body').toggle();
    });

    // DELETE PRODUCT ITEM FROM CART-MENU 
    $('.cart-page .delete-cart-prod').click(function(e){
        e.preventDefault();
        $(this).parent('.cart-page .cart-item').remove();
    });


    // SHOW GIFT CONTENT
    $('.cart-gift .head').click(function(){
        $(this).siblings('.cart-gift .gift-cont').toggle();
        $(this).find('i').toggleClass('rotate');
    });

    // SHOW BRAND FILTER 
    var filter_item  =  $('.brand-side-filter .filter-item-box');
    var filter_btn   =  filter_item.find('.filter-item-head');
    var filter_body  =  filter_item.find('.filter-item-body');
    filter_btn.click(function(){
        $(this).parent(filter_item).find(filter_body).slideToggle();
        $(this).find('.icon').toggleClass('plus');
    });




    // OWL 
    $('.main-owl').owlCarousel({
        rtl: true,
        margin: 0,
        autoplay: true,
        loop: true,
        nav: false,
        dots:true,
        autoplaySpeed: 3000,
        smartSpeed: 3000,
        dragEndSpeed: 3000,
        slidSpeed: 900,
        paginationSpeed: 900,
        navText: ["<i class='icofont-thin-right'></i>", "<i class='icofont-thin-left'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    });

    $('.brands-owl').owlCarousel({
        rtl: true,
        margin: 0,
        autoplay: true,
        loop: true,
        nav: true,
        dots:false,
        autoplaySpeed: 2000,
        navText: ["<i class='icofont-thin-right'></i>", "<i class='icofont-thin-left'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 4
            }
        }
    });

    $('.tablist-owl').owlCarousel({
        rtl: true,
        margin: 0,
        autoplay: false,
        loop: true,
        nav: true,
        dots:false,
        autoplaySpeed: 2000,
        navText: ["<i class='icofont-circled-right'></i>", "<i class='icofont-circled-left'></i>"],
        responsive: {
            0: {
                items: 2
            },
            600: {
                items: 3
            },
            1000: {
                items: 3
            }
        }
    });

    $('.tabcontent-owl').owlCarousel({
        rtl: true,
        margin: 20,
        autoplay: false,
        loop: true,
        nav: true,
        dots:false,
        autoplaySpeed: 2000,
        navText: ["<i class='icofont-thin-right'></i>", "<i class='icofont-thin-left'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 5
            }
        }
    });

    $('.owl-hash-slider').owlCarousel({
        items:1,
        loop:true,
        nav: false,
        rtl:true,
        navText: ["<i class='icofont-circled-right'></i>", "<i class='icofont-circled-left'></i>"],
        URLhashListener:true,
        autoplayHoverPause:true,
        margin:10,
        animateOut: 'fadeOut',
        startPosition: 'URLHash',
    });

    $('.blog-owl').owlCarousel({
        rtl: true,
        margin: 0,
        autoplay: true,
        loop: true,
        nav: true,
        dots:false,
        autoplaySpeed: 2000,
        navText: ["<i class='icofont-thin-right'></i>", "<i class='icofont-thin-left'></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 4
            }
        }
    });

    $('.featured-brands-owl').owlCarousel({
        rtl: true,
        margin: 10,
        autoplay: true,
        loop: true,
        nav: true,
        dots:false,
        autoplaySpeed: 2000,
        navText: ["<i class='icofont-thin-right'></i>", "<i class='icofont-thin-left'></i>"],
        responsive: {
            0: {
                items: 2
            },
            600: {
                items: 2
            },
            1000: {
                items: 4
            }
        }
    });
});

// HEADER CATEG SEARCH FILTER 
var array = [];
function myCatSelect(myEl){
   var value = myEl.value;
    if(myEl.checked){
        array.push(myEl.id);
    }else{
     array.splice(array.indexOf(myEl.id) ,1 );
    }

    if(array.length === 1){
        var name = $('#'+array[0]).val();
        $('#result').html(name);
    }else if(array.length === 0){
        $('#result').html('Shop by category');
    }
    else{
        $('#result').html(array.length + ' category');
    }
}

// COUNT DOWN 
var countDownDate = new Date("Jan 5, 2019 15:37:25").getTime();
var x = setInterval(function() {
    var now = new Date().getTime();
    var distance = countDownDate - now;
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    $('#days').html( days + "/D");
    $('#hours').html(hours + "/H");
    $('#minuts').html(minutes + "/M");
    $('#seconds').html(seconds + "/S");
}, 1000);

// CLOSE ADD TO CART MODAL TIMER 
$('.add-to-cart').click(function(){
    var countdownNumberEl = document.getElementById('count-num');
    var countdown = 10;

    countdownNumberEl.textContent = countdown;

    var interval = setInterval(function() {
        countdown = --countdown <= 0 ? 10 : countdown;
        countdownNumberEl.textContent = countdown;

        if(countdown == 1)
        {
            clearInterval(interval);
            $('#cart-product-modal').modal('hide');
        }
        console.log(countdown);

    }, 1000);

});

// COUNTER PLUS AND MINUS
$(document).on('click','.counter .btn',function (e) {
    e.preventDefault();
    var count = $(this).parent(),
    num = $(this).siblings(".num"),
    i = parseInt(num.text(), 10);
    
    if ($(this).hasClass("plus")) {
        if (i === 0) {
            i = i + 1;
            count.removeClass("shrink");
            num.fadeIn();
            num.text(i);
            $('.product_num').val(1);
        } else {
            i = i + 1;
            num.text(i);
            $('.product_num').val(i);
        }
    } else {
        if (i === 1) {
            i = i - 1;
            count.addClass("shrink");
            // num.fadeOut();
            num.text(i);
            $('.product_num').val(0);
        } else if (i > 1) {
            i = i - 1;
            num.text(i);
            $('.product_num').val(i);
        }
    }
});

// VALIDATE  PASSWORD 
function passwordChanged() {
    var strength = $('#strength-result');
    var strong   = new RegExp("^(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\\W).*$", "g");
    var medium   = new RegExp("^(?=.{7,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$", "g");
    var enough   = new RegExp("(?=.{6,}).*", "g");
    var password = document.getElementById('password');

    if (password.length == 0) {
        strength.html('Type Password');
    } else if (false == enough.test(password.value)) {
        strength.html('Password Strength: Weak');
        strength.css('background','#ffafae9e');
        strength.css('color','#000');
    } else if (strong.test(password.value)) {
        strength.html('Password Strength: Strong');
        strength.css('background','#12a032');
        strength.css('color','#fff');
    } else if (medium.test(password.value)) {
        strength.html('Password Strength: Medium');
        strength.css('background','orange');
        strength.css('color','#000');
    } else {
        strength.html('Password Strength: Weak');
        strength.css('background','#dc3545');
        strength.css('color','#fff');
    }
}

// SHOW CHECKOUT PAY METHOD 
function radioChecked(radio_box){
    if(radio_box.checked){
        $('.pay-option-box').slideUp();
        // $(radio_box).parent('.form-check').next('.pay-option-box').slideDown();
        if($(radio_box).parent('.form-check').next('.pay-option-box').is(':visible')){
            $(radio_box).parent('.form-check').next('.pay-option-box').slideUp();
        }else{
            $(radio_box).parent('.form-check').next('.pay-option-box').slideDown();
        }
    }
}

// SHOW CHANGE CHECKOUT SHIPPING ADDRESS BOX
function itemChecked(check_box){
    if(check_box.checked){
        $(check_box).parent('.form-check').next('.change-address-box').slideUp();
    }else{
        $(check_box).parent('.form-check').next('.change-address-box').slideDown();
    }
}

// SHOW LOADER 
function showList() {
    $('.loader').fadeIn();
    setTimeout(function(){ 
        $('.loader').fadeOut();
        $('.brand-page-contnet .brand-products .col-12').addClass('list-view');
    }, 200);
}
function showGrid() {
    $('.loader').fadeIn();
    setTimeout(function(){ 
        $('.loader').fadeOut();
        $('.brand-page-contnet .brand-products .col-12').removeClass('list-view');
        $('.product-card .overlay').style.animationDuration = "3s";
    }, 200);
}

//    // SHOW LIST 
//    $('.show-list').click(function(){
//     $('.brand-page-contnet .brand-products .col-6').addClass('list-view');
// });
// $('.show-grid').click(function(){
//     $('.brand-page-contnet .brand-products .col-6').removeClass('list-view');
// });
