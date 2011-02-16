function mycarousel_initCallback(carousel) {
    jQuery('#mycarousel-next').click(function() {
        carousel.next();
        return false;
    });
    jQuery('#mycarousel-prev').click(function() {
        carousel.prev();
        return false;
    });
};
$(document).ready(function(){
    $("#obras").jcarousel({
        scroll: 4,
        initCallback: mycarousel_initCallback,
        buttonNextHTML: null,
        buttonPrevHTML: null
    });
});