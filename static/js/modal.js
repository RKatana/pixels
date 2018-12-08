showModal = (i) => {
    $("#myModal").modal("show")
    $(".mod-img").attr("src",i)
}
$(document).ready(() => {
    $(".image").mouseover(() => {
        alertI("Hey")
    })
})
showButton = () => {
    $(".modal-btn").show()
}