(function () {
    const links = document.getElementsByTagName('a')
    for (let i = 0; i < links.length; i++) {
        if (links[i].href.endsWith('index.pdf')) {
            links[i].download = window.location.pathname.split('/')[2] + ".pdf"
        }
    }
})()
