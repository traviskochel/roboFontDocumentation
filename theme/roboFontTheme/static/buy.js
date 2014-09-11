jQuery(document).ready(function() {
    jQuery(".buybutton").click(function(e) {
        if (!jQuery('[value="buyAgree"]').attr("checked")) {
            e.preventDefault();
            jQuery("#buyErrorMessage").show();
            return false;
        }
        else {
            jQuery("#buyErrorMessage").hide();
        }
    });
});