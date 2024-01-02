$(window).ready((e) => {
    happynewyearDiv = $(".happynewyear");
    val = JSON.parse(localStorage.getItem("happynewyear"));

    $(window).keydown(function (e) {
        const keyCode = e.keyCode;

        if (e.shiftKey && keyCode == 83) {
            happynewyearDiv.toggle();
            localStorage.setItem("happynewyear", !val);
        }
    });
    happynewyearDiv.toggle(!val);
});
