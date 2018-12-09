showModal = (name,desc,url) => {
    console.log(name,desc,url)
    $("#label").text(name)
    $("#myModal").modal("show")
    $(".mod-img").attr("src",url)
    $("#img-desc").text(desc)
    $("#url-to-copy").val(window.location.origin + url)
}
copyUrl = () => {
    $("#url-to-copy").select()
    document.execCommand('copy');
}
