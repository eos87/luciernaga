hs.graphicsDir = '/files/css/graphics/';
hs.align = 'center';
hs.transitions = ['expand', 'crossfade'];
hs.wrapperClassName = 'dark borderless floating-caption';
hs.fadeInOut = true;
hs.dimmingOpacity = .75;
hs.showCredits = false;


// create a shorthand function so we don't need to put all this in the opener's onclick
function openYouTube(opener) {

    var returnValue;

    // Safari Mobile doesn't have Flash, so we just let the device use the built-in
    // YouTube viewer.
    if (/(iPhone|iPod|iPad)/.test(navigator.userAgent)) {
        opener.href = opener.href.replace('/v/', '/watch?v=');
        returnValue = true;
    }

    else returnValue = hs.htmlExpand(opener, {
        objectType: 'swf',
        objectWidth: 480,
        objectHeight: 385,
        width: 480,
        swfOptions: {
            params: {
                allowfullscreen: 'true'
            }
        },
        slideshowGroup: 'group1',
        outlineType: 'rounded-white',
        wrapperClassName: 'draggable-header no-footer',
        fadeInOut: false,
        maincontentText: 'You need to upgrade your Flash player'
    });

    return returnValue;
}  


// Add the controlbar
hs.addSlideshow({
    wrapperClassName: 'dark borderless floating-caption',
    slideshowGroup: 'group2',
    interval: 5000,
    repeat: false,
    useControls: true,
    fixedControls: 'fit',
    overlayOptions: {
        opacity: .6,
        position: 'bottom center',
        hideOnMouseOut: true
    }
});


