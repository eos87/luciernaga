$(document).ready(function(){
    $('.logo_animado').attr('src', '/files/images/logo_red.png');
    lastBlock = $('#a8');
    maxHeight = 505;
    minHeight = 28;
    $(".acordeon ul li div.title").click(
        function(){
            $(lastBlock).find('.body').hide();
            $(lastBlock).animate({
                height: minHeight+"px"
                }, {
                queue:false,
                duration:300
            });
            $(this).parent().animate({
                height: maxHeight+"px"
                }, {
                queue:false,
                duration:300
            });
            $(this).parent().find('.body').show();
            changeSymbol(lastBlock, this);
            lastBlock = $(this).parent();
            return false;
        });
});
function changeSymbol(lastBlock, newBlock){
    $(lastBlock).find('span').html('[+]');
    $(newBlock).find('span').html('[-]');
}


