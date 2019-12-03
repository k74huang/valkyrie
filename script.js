imageList = ['EKxXikJUwAA9ZEt.jpg', 'EKxXikIU8AApcJd.jpg', '1535533435286.jpg', '1534106400778.jpg', '1515170851999.png', '1441323403530.png', '1451081115645.jpg', '1493667035461.jpg', '74584294_p0.jpg', '68580183_p0.jpg', '67379341_p0.png', '67014930_p0.png', '61215562_p0.png', '60450617_p2_master1200.jpg', '40636265_p0.jpg', '42390794_p0.jpg', '71444308_p0.png', '71462111_p0.jpg', '70336750_p0.png', '68201344_p0.png', '62299336_p0.jpg', '48595722_p0.jpg', '19ngy.png', '13rg7.png', '16aa2.jpg', '1bvi6.jpg', '1a19o.jpg', '131vl.jpg', '1bitu.jpg', '1vroe0ioenj11.png', 'ee39104b193a2abe0340c557f1474075200a9081.jpg', 'twsskbnbcf931.jpg', 'trHIiSg.jpg', 'lFvlgtI.jpg', 'IMG_20190619_105027.jpg', 'IMG_20190618_103526.jpg', 'IMG_20190521_113819.jpg', 'IMG_20190429_124129.jpg', 'IMG_20190428_095817.jpg', 'illust_74259877_20190429_000907.jpg', 'illust_68539777_20190429_001332.jpg', '72896341_p0.jpg', '72668704_p0.jpg', '71487563_p0.png', '69919245_p0.png', '69246838_p0.jpg', '68766284_p0.png', '67353068_p0.png', '67280569_p0.png', '64616348_p0.png', '64552898_p0.png', '64481371_p0.png', '63514040_p2.jpg', '63171206_p0.png', '177ls.jpg', '176nt.png', '19to3.jpg', '11vpn.png', '1bxtz.jpg', '1bbu6.png', '74228429_p0.jpg']

window.onload = function() {
    document.getElementById("dimmer").style.display = "none";
    const config = {
        rootMargin: '0px 0px 50px 0px',
        threshold: 0.5
    };

    // register the config object with an instance
    // of intersectionObserver
    let observer = new IntersectionObserver(function(entries, self) {
        // iterate over each entry
        entries.forEach(entry => {
            // process just the images that are intersecting.
            // isIntersecting is a property exposed by the interface
            if (entry.isIntersecting) {
                // custom function that copies the path to the img
                // from data-src to src
                console.log(entry.target);
                entry.target.src = entry.target.getAttribute("data-src");
                // the image is now in place, stop watching
                self.unobserve(entry.target);
            }
        });
    }, config);

    for (i = 0; i < imageList.length; i++) {

        console.log("Loaded: " + imageList[i]);

        var image = document.createElement("img");
        image.setAttribute("data-src", "thumbs/" + imageList[i]);
        image.onclick = function() {
            console.log("Opened: " + this.getAttribute("data-src"));
            var imageLarge = document.createElement("img");
            imageLarge.src = "walls/" + this.getAttribute("data-src").substring(7, this.getAttribute("data-src").length);
            imageLarge.id = "imgLarge";
            imageLarge.classList.add("imgLarge");
            document.getElementById("root").appendChild(imageLarge);
            document.getElementById("dimmer").style.display = "block";
        };

        document.getElementById("col" + (3 - (i + 1) % 3)).appendChild(image);

    }
    const imgs = document.querySelectorAll('[data-src]');
    imgs.forEach(img => {
        observer.observe(img);
    });
}

function closeImg() {
    var imageLarge = document.getElementById("imgLarge");
    console.log("Closing: " + imageLarge.src);
    imageLarge.parentNode.removeChild(imageLarge);
    document.getElementById("dimmer").style.display = "none";
}