# The Blueprint
## category: OSINT ("Ohio")
## author: segal

## Description
always respect the blueprint (she's never coming back lil bro (i am heartbroken)). anyways, what street are we on?

flag will look like: UMDCTF{Campus Dr, College Park, MD 20742}

## Attachments
-> One .jpg image: `the-blueprint.jpg` 

## Solution
![distortion on top and bottom, only the center is authentic](the-blueprint.jpg)
Because the image has a weird look (probably a 360 degrees camera edited into a flat image), many parts (mainly bottom and top) seem distorted. The only parts which seem untouched is the center. Uploading the center of the image (including most of the tree, the street and the connection point of the pavement with the grass) to a reverse image lookup tool reveals yet again the correct location!

![solved challenge; image showing the answer in google maps](solved_blueprint.png)

Now, getting the flag is purely a matter of formatting.

## Flag
`UMDCTF{Bryn Du Dr, Granville, OH 43023}`