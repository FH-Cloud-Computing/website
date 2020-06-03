(function() {
    const links = document.getElementsByTagName("a")
    for (let i = 0; i < links.length; i++) {
        if (links[i].href.startsWith("http") &&
            !links[i].href.startsWith(window.location.protocol + "//" + window.location.hostname)
        ) {
            if (links[i].target === "") {
                links[i].target = "_blank";
            }
            if (links[i].rel === "") {
                links[i].rel = "noreferer noopener";
            }
        }
    }
})();