Download and place CVideos.py in the same folder as the python file to augment frames.
Import CVideos into your program:
```
from CVideos import videofeed
```
Pass a function (that takes in a frame and returns an augmented frame to be displayed) to videofeed as such
```
videofeed(exampleFunction)
```
Don't call the function when passing it to videofeed (i.e. don't do this 
```
videofeed(exampleFunction())
```
)