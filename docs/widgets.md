# Displaying Image on Android Home Screen
Ideally want an Android Home Screen widget to show the weather image.

This rules out a PWA: as of 2024 [doesn't support widgets](https://issues.chromium.org/issues/40744630?pli=1).
## Android app that displays image URL
[Asked](https://android.stackexchange.com/questions/15356/how-can-i-display-an-image-from-a-url-on-a-home-screen) in 2011: most of the answers are out-of-date

**Answer:** Going forward with these suggestions, even though they can't load an [SVG](https://upload.wikimedia.org/wikipedia/commons/3/30/Vector-based_example.svg):
- https://play.google.com/store/apps/details?id=com.ibuffed.webimagewidget
	- I like that it's OSS  https://github.com/004helix/RemoteImageWidget/
- https://play.google.com/store/apps/details?id=com.yktp.betterurlimagewidget
	- Has a Better Google Play Store rating
### SVG viewer apps don't have widgets
I thought at first that I would generate an SVG file, but there's no "image on homescreen" viewer I can find.
- https://play.google.com/store/apps/details?id=cobos.svgviewer
And I don't want to use a [web browser screenshot widget app](https://play.google.com/store/apps/details?id=com.binarysmith.webclipwidget.ad) which feels too heavy.
(Maybe SVG renders are heavy?)
### Image widget apps that don't seem to support loading URL
- https://play.google.com/store/apps/details?id=com.fibelatti.photowidget
- https://play.google.com/store/apps/details?id=com.nbow.photowidget
- https://play.google.com/store/apps/details?id=com.futuretech.imagewidget
### Don't want to build Android app from source
- https://github.com/lieryan/url-image-widget
- https://web.archive.org/web/20240708214127/https://syntaxcorrect.com/Java/How_to_Build_an_Android_App_Widget_in_HTML
