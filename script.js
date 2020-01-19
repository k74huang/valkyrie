imageList = ['751740.jpg', '714226.png', '706022.jpg', '585805.png', '753589.png']

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