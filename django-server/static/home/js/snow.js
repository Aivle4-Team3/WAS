$(window).ready((e) => {
    snowDiv = $(".snow-wrapper");
    $(window).keydown(function (e) {
        const keyCode = e.keyCode;

        if (e.shiftKey && keyCode == 83) {
            if (localStorage.getItem("snow") == "blizzard") {
                snowDiv.filter(".front").addClass("snow--behind");
                localStorage.setItem("snow", "quit");
            } else if (localStorage.getItem("snow") == "quit") {
                snowDiv.hide();
                localStorage.setItem("snow", "off");
            } else {
                snowDiv.filter(".front").removeClass("snow--behind");
                snowDiv.show();
                localStorage.setItem("snow", "blizzard");
            }
        }
    });
    snowDiv.toggle(localStorage.getItem("snow") == "on");
    snowDiv.filter(".front").toggleClass("snow--behind", localStorage.getItem("snow") == "quit");
});
