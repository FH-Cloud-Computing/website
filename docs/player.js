(function(){
    let players = []
    const audioTags = document.getElementsByTagName("audio")
    function createPlayer(audioTag, i) {
        let player = {}
        player.audioTag = audioTag
        player.audioTag.preload = "metadata";
        player.src = player.audioTag.src
        const parent = player.audioTag.parentNode
        let previous = parent.previousSibling
        while(previous && previous.nodeType !== 1) {
            previous = previous.previousSibling
        }

        //Add the audio indicator
        if (typeof previous.id !== "undefined" && previous.id !== "") {
            //Hack: the first link is somewhere gone
            const links = document.querySelectorAll("a[href=\"#" + previous.id + "\"].md-nav__link");
            const link = links[1]
            player.link = link;
            player.linkText = link.textContent.trim();
            player.id = "player_" + previous.id;
        }
        player.number = i
        function setIcon(icon) {
            if (typeof player.link !== "undefined") {
                player.link.textContent = player.linkText + " " + icon;
            }
        }
        setIcon("🎧");
        player.audioTag.addEventListener("play", function() {
            setIcon("▶");
            for (let j = 0; j < players.length; j++) {
                if (i === j) {
                    continue
                }
                players[j].audioTag.pause();
            }
        });
        player.audioTag.addEventListener("pause", function() {
            setIcon("🎧");
        });
        player.audioTag.addEventListener("ended", function() {
            setIcon("🎧");
            if (typeof players[i+1] !== "undefined") {
                players[i+1].audioTag.play()
            }
        });

        //Drop the parent node
        parent.parentNode.replaceChild(player.audioTag, parent)

        return player;
    }

    for (let i = 0; i < audioTags.length; i++) {
        players.push(createPlayer(audioTags[i], i))
    }
})();