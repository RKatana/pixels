$(window).scroll(() => {
    if ($(document).scrollTop() > 450) {
        $("nav").addClass("shrink")
        $(".nav-form").show()
        
    } else  {
        $("nav").removeClass("shrink")
    }
})