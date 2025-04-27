# The Master
## category: OSINT ("Ohio")
## author: segal

## Description
trust me bro, i know what im talking about. im the master when it comes to these things. what street are we on?

flag will look like: UMDCTF{Campus Dr, College Park, MD 20742}

## Attachments
-> One .jpg image: `the-master.jpg` 

## Solution
![Image](the-master.jpg)
The has some buildings on it, but one stands out!
![Image of interesting building](interesting_building.jpg)
Cropping it out and running it through a reverse image lookup tool, delivers a `wikimedia.org` result. This hit includes the `camera position`. Copy-pasting the coordinates in google maps reveals the location!

![solved challenge; image showing the answer in google maps](solved_the_master.jpg)

Once more, we simply need to format!

## Flag
`UMDCTF{Main St, Lore City, OH 43755}`