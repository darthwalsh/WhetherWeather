## 2025 plan
![[ui-closeup.png]]


1. [ ] No “now” exactly on the chart, so the diagram is good an hour after generation!
2. [ ] `def pos(time) -> int`
3. [ ] Sunrise → sunset → sunrise
4. [ ] Draw curves
5. [ ] Get temps
6. [ ] Plan for after rate limit first time
	1. [ ] Track usage in DB
	2. [ ] Alerts when usage high
	3. [ ] Plan to cache to locally (or maybe inside Fly.io)


## Initial Design Sketch

![[prototype.pdf]]

Data lines plotted
- Past
- Now (3 PM)
- +2 hour

- [ ] Sun, UV index
- [ ] AQI scale has different color
  - Green
  - Yellow
  - Orange
- [ ] Rain volume %
- [ ] Temp
- [ ] Wind

## Requested features:
- Past 24 hr
- Scroll sideways?
- Linear scale
- Pinch zoom
