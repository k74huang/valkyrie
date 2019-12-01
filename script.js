imageList = [
    "1bbu6.png",
    "1bxtz.jpg",
    "11vpn.png",
    "19to3.jpg",
    "176nt.png",
    "177ls.jpg",
    "63171206_p0.png",
    "63514040_p2.jpg",
    "64481371_p0.png",
    "64552898_p0.png",
    "64616348_p0.png",
    "67280569_p0.png",
    "67353068_p0.png",
    "68766284_p0.png",
    "69246838_p0.jpg",
    "69919245_p0.png",
    "71487563_p0.png",
    "72668704_p0.jpg",
    "72896341_p0.jpg",
    "74228429_p0.jpg"
]

window.onload = function() {
    document.getElementById("dimmer").style.display = "none";
    for (i = 0; i < imageList.length; i++) {

        console.log("Loaded: " + imageList[i]);

        var image = document.createElement("img");
        image.src = "walls/" + imageList[i];
        image.onclick = function() {
            console.log("Opened: " + this.src);
            var imageLarge = document.createElement("img");
            imageLarge.src = this.src;
            imageLarge.id = "imgLarge";
            imageLarge.classList.add("imgLarge");
            document.getElementById("root").appendChild(imageLarge);
            document.getElementById("dimmer").style.display = "block";
        };

        document.getElementById("col" + (3 - (i + 1) % 3)).appendChild(image);

    }
}

function closeImg() {
    var imageLarge = document.getElementById("imgLarge");
    console.log("Closing: " + imageLarge.src);
    imageLarge.parentNode.removeChild(imageLarge);
    document.getElementById("dimmer").style.display = "none";
}