/**
 * Created by Jovi on 14/5/2015.
 */

if (typeof jutils == 'undefined') {
    jutils = {
        'isBulidinFormValidation': function () {
            return typeof document.createElement("input").checkValidity == "function";
        }
        , 'bindFormValidation': function (form) {

            var els = $(form).find("[required], [pattern]");
            for (var i = 0; i < els.length; i++) {
                var el = els.eq(i);
                var v = el.val();
                if (el.attr("required") && v.replace(/^\s+|^s+$/) == "") {
                    alert(el.data("required_message") || "You missed required field");
                    el.focus();
                    return false;
                }
                if (el.attr("pattern") && !new RegExp(el.attr("pattern")).test(v)) {
                    el.focus();
                    alert(el.data("pattern_message") || "invalid data");
                    return false;
                }
            }

            return true;
        }
    };


    if(!jutils.isBulidinFormValidation()){
        $('form').on('submit', function () {
            return jutils.bindFormValidation(this);
        });
    }


}


