// navbar selection
$(function(){
    $('ul li a').filter(function(){return this.href==location.href}).parent().addClass('active').siblings().removeClass('active')
    $('ul li a').click(function(){
        $(this).parent().addClass('active').siblings().removeClass('active')    
    })
})

// payment method form
$('select').on('change', function() {
   if (this.value=="Credit Card"){
    $('.payment-with-cc').css('display','table-row');
   }else{
    $('.payment-with-cc').css('display','none');
   }

   if (this.value=="E-Money"){
    $('.scanqr').css('display','block');
   }else{
    $('.scanqr').css('display','none');
   }

   if (this.value=="Paypal"){
    $('.paypal').css('display','block');
   }else{
    $('.paypal').css('display','none');
   }
  });

// cart
$('.show-cart').on('click', function() {
  $('.order-item').animate({
    'width': 'toggle'
}, 1000);

});

$(window).scroll(function(){
  var y_scroll_pos = window.pageYOffset;
  var scroll_pos_test = 150;   
  var x = window.matchMedia("(min-width: 1261px)")
  if(x.matches) {
    setTimeout(function(){
      if(y_scroll_pos > scroll_pos_test){
        $('.hide').css('display','block');
        $('.hide').css('position','relative');
        $('.head').css('grid-template-columns','50% 50%');
        $('.head').css('background-color','var(--color-text-normal)');
        $('.head').css('position','fixed');
        $('.head').css('width','100%');
        $('.head').css('z-index','9');
        $('.head .left a').css('color','#fff');
        $('.head .middle').css('display','none');
        $('.big').css('display','none');
        $('.order-item').css('transform','translateY(15%)');


      }else{
        $('.hide').css('display','none');
        $('.head').css('grid-template-columns','30% 40% 30%');
        $('.head').css('position','relative');
        $('.head').css('width','auto');
        $('.head').css('background-color','transparent');
        $('.head .left a').css('color','var(--color-text-normal)');
        $('.head .middle').css('display','grid');
        $('.big').css('display','grid');
        $('.order-item').css('transform','translateY(-5%)');
      }
    }, 100)};
});


ScrollReveal({
  reset: true,
  distance: '60px',
  duration:2500,
  delay:400
});

ScrollReveal().reveal('.main-left h3', {delay:500, origin:'left'});
ScrollReveal().reveal('.main-left h1', {delay:600, origin:'left'});
ScrollReveal().reveal('.main-left p', {delay:700, origin:'left'});
ScrollReveal().reveal('.main-left .button', {delay:700, origin:'left'});
ScrollReveal().reveal('.main-right img', {delay:700, origin:'right'});
ScrollReveal().reveal('.sosmed a', {delay:700, origin:'bottom',interval:400});
ScrollReveal().reveal('.menu .card-wrapper', {delay:200, origin:'bottom',interval:200});
ScrollReveal().reveal('.insights div, .navbar h1', {delay:100, origin:'bottom',interval:250});
ScrollReveal().reveal('main .recent-orders ', {delay:50, origin:'bottom'});



$('#openNav').on('click', function() {
  $('aside').css({
    'width': '100%',
    'height': '100vh',
}, 1000);
});

$('#hide').on('click', function() {
  $('aside').css({
    'width': '0%'
}, 1000);

});

