imageList = [
    {
        "added": 1591762748.4278646,
        "filename": "mypWLOg.jpg"
    },
    {
        "added": 1591762636.1042492,
        "filename": "yia98a7ouol41.png"
    },
    {
        "added": 1591762523.4916737,
        "filename": "EaFaX8cU4AUAzHn.jfif"
    },
    {
        "added": 1591678280.4187205,
        "filename": "1464920036809.jpg"
    },
    {
        "added": 1591678239.6209786,
        "filename": "1461003760140.jpg"
    },
    {
        "added": 1591678187.4313273,
        "filename": "77559996_p0.png"
    },
    {
        "added": 1591677904.0523412,
        "filename": "71408314_p0.jpg"
    },
    {
        "added": 1591677862.8844862,
        "filename": "70116129_p0.png"
    },
    {
        "added": 1591677834.6611638,
        "filename": "57721770_p0.png"
    },
    {
        "added": 1591677443.6211374,
        "filename": "38576223_p0.jpg"
    },
    {
        "added": 1591583230.019616,
        "filename": "1455843817363.png"
    },
    {
        "added": 1591582944.720369,
        "filename": "1416093528025.jpg"
    },
    {
        "added": 1591582870.7299714,
        "filename": "69776123_p0.png"
    },
    {
        "added": 1591304773.5860453,
        "filename": "68437285_p0.png"
    },
    {
        "added": 1591304685.0623481,
        "filename": "65897535_p0.jpg"
    },
    {
        "added": 1591304589.1480408,
        "filename": "65033438_p0.png"
    },
    {
        "added": 1591304359.6564386,
        "filename": "65714066_p0.jpg"
    },
    {
        "added": 1591304332.9799948,
        "filename": "66934858_p0.jpg"
    },
    {
        "added": 1591304288.7189226,
        "filename": "62445411_p0.jpg"
    },
    {
        "added": 1591304192.7424974,
        "filename": "61351810_p0.jpg"
    },
    {
        "added": 1591304149.7690647,
        "filename": "63514040_p2.jpg"
    },
    {
        "added": 1591304105.765535,
        "filename": "63481789_p0.jpg"
    },
    {
        "added": 1591304085.576734,
        "filename": "64552898_p0.png"
    },
    {
        "added": 1591303956.2777543,
        "filename": "62299336_p0.jpg"
    },
    {
        "added": 1591303900.0772579,
        "filename": "70336750_p0.png"
    },
    {
        "added": 1591303840.3592064,
        "filename": "71462111_p0.jpg"
    },
    {
        "added": 1591303516.6779768,
        "filename": "71849322_p0.jpg"
    },
    {
        "added": 1591303328.5349958,
        "filename": "71492160_p0.jpg"
    },
    {
        "added": 1591302365.35115,
        "filename": "66952181_p0.png"
    },
    {
        "added": 1591301914.4054093,
        "filename": "67048519_p0.png"
    },
    {
        "added": 1591301840.6409104,
        "filename": "77784528_p0.png"
    },
    {
        "added": 1591301768.0189161,
        "filename": "76900523_p0.jpg"
    },
    {
        "added": 1591300896.9980023,
        "filename": "71093249_p0.png"
    },
    {
        "added": 1591299741.5378914,
        "filename": "70549737_p3.png"
    },
    {
        "added": 1591299681.3127882,
        "filename": "20cv4.png"
    },
    {
        "added": 1591298278.3585677,
        "filename": "74078288_p0.png"
    },
    {
        "added": 1591298278.319532,
        "filename": "706022.jpg"
    },
    {
        "added": 1591298278.3155284,
        "filename": "69338333_p0.jpg"
    },
    {
        "added": 1591298278.3025172,
        "filename": "68904205_p0.png"
    },
    {
        "added": 1591298278.2895048,
        "filename": "67014930_p0.png"
    },
    {
        "added": 1591298278.263482,
        "filename": "64481371_p0.png"
    },
    {
        "added": 1591298278.2444637,
        "filename": "63727726_p0.png"
    },
    {
        "added": 1591298278.2174394,
        "filename": "50438387_p0.jpg"
    },
    {
        "added": 1591298278.2144368,
        "filename": "48424641_p0.jpg"
    },
    {
        "added": 1591298278.211434,
        "filename": "40636265_p0.jpg"
    },
    {
        "added": 1591298278.2044277,
        "filename": "1gzgo.jpg"
    },
    {
        "added": 1591298278.1864114,
        "filename": "1503871652136.png"
    },
    {
        "added": 1591298278.168395,
        "filename": "1468163715499.png"
    }
];

// ---------------------------------------------------------------------------

window.onload = function() {
    document.getElementById("dimmer").style.display = "none";
    const config = {
        rootMargin: '0px 0px 50px 0px',
        threshold: 0.2
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

        // console.log("Loaded: " + imageList[i].filename);

        var image = document.createElement("img");
        image.setAttribute("data-src", "thumbs/" + imageList[i].filename);
        image.onclick = function() {
            // console.log("Opened: " + this.getAttribute("data-src"));
            var imageLarge = document.createElement("img");
            imageLarge.src = "walls/" + this.getAttribute("data-src").substring(7, this.getAttribute("data-src").length);
            imageLarge.id = "imgLarge";
            imageLarge.classList.add("imgLarge");
            document.getElementById("root").appendChild(imageLarge);
            document.getElementById("dimmer").style.display = "block";
        };

        document.getElementById("col" + (i%3)).appendChild(image);

    }
    const imgs = document.querySelectorAll('[data-src]');
    imgs.forEach(img => {
        observer.observe(img);
    });
}

function closeImg() {
    var imageLarge = document.getElementById("imgLarge");
    // console.log("Closing: " + imageLarge.src);
    imageLarge.parentNode.removeChild(imageLarge);
    document.getElementById("dimmer").style.display = "none";
}