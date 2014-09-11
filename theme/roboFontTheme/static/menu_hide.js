$(document).ready(function() {
    $("#showSubMenu").click(function(e) {
        $('.widget ul.current ul ul ul').show();
        localStorage.setItem("docMenuState", 1);

    });
    $("#hideSubMenu").click(function(e) {
        $('.widget ul.current ul ul ul').hide();
        localStorage.setItem("docMenuState", 0);
    });
    if ($(".showHideWidgets")[0]) {
        showSubMenus = localStorage.getItem("docMenuState");
        if (showSubMenus == 1) {
            $('.widget ul.current ul ul ul').show();
        }
    }
});
