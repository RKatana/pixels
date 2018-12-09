showModal = (name,desc,url) => {
    console.log(name,desc,url)
    $("#label").text(name)
    $("#myModal").modal("show")
    $(".mod-img").attr("src",url)
    $("#img-desc").text(desc)
}
