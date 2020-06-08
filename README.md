# Valkyrie

A wallpaper manager that watches over a local directory, backs up files to GitHub, and displays them on a GitHub pages website. 

![](https://i.imgur.com/2CR6fFw.png)

## Features

- Automatic GitHub pushes based on folder monitoring
- Desktop client for collection management (currently only a taskbar icon)
- Thumbnail generation for images (takes up more repo space but allows site to load faster)
- Lazy loading (again to make website faster)

## How it works

The scripts can be found in the /utils/ folder

- dirWatch.py watches over the directory as well as manages desktop client
- imageHandler.py is called when dirWatch.py detects a new image in the directory
- script.js is updated with the huge JSON collection of wallpapers updated
- gitHelp.bat is called to commit the new updates and push the repository

## Contributing

Please don't contribute directly to this repo since it's meant to be a pet project of mine. 

Please **do** feel free to fork it and do literally whatever the hell else you want though. MIT license and all that. 

## Literally why did you make this

To be honest, this started as a shitpost. It also started when I wasn't aware that GitHub had a 1GB limit on repository size. 

Basically, I just wanted to have a lightweight site that I could use to store a wallpaper collection and sync it easily without having to pay for anything. I figured GitHub pages was my best option and here we are. 

In the long run it's not going to be very useful for its intended purpose but it's a fun idea to play around with and useful for Python practice. 

## Why the fuck did you name it Valkyrie

The name *Valkyrie* starts from the original name I had for it, which was simply *Wallpaper Collection*. As a reference to Kantai Collection, which is a stupid boat game I used to play quite a bit, I started abbreviating it to *WallColle* just as Kantai Collection is often abbreviated to *KanColle*. *WallColle* expressed through Japanese phoenetics becomes *Warukore*, which sounds somewhat similar to *Warukyūre*, or *ワルキューレ*, or *Walküre*, an idol group from the Macross series. *Walküre* is the German form of the word *Valkyrie*.  

I like naming my projects. Don't judge. 