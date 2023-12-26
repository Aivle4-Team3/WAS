$(window).ready((e) => {
    snowDiv = $(".snow-wrapper");
    $(window).keydown(function (e) {
        const keyCode = e.keyCode;

        if (e.shiftKey && keyCode == 83) {
            snowDiv.toggle();
            localStorage.setItem("snow-off", snowDiv.is(":hidden"));
        }
    });
    snowDiv.toggle(!JSON.parse(localStorage.getItem("snow-off")));
});
