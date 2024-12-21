# Whether Weather

In-progress weather tool that renders an image for a home screen widget.

## Dev Flow

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python poc.py
echo "http://$(ifconfig | rg 'inet (192\S*)' -r '$1' -o):8000/black_circle.png"
python -m http.server
```

Then see [widget docs](docs/widgets.md) for how to use the image in a widget.

## Tasks
- [ ] PoC ⏫ 
	- [x] Create PNG image
	- [x] localhost serve image
	- [x] Some docs for showing the image in a widget
	- [ ] Call a weather API, get i.e daily max/min temps
	- [ ] Render the temps on the image
- [ ] MVP 1
	- [ ] Figure out the exact size of my android home screen for rendering
	- [ ] Deploy cron task to cloud i.e. fly.io
		- [ ] Basic secrets management
		- [ ] Install dependencies
		- [ ] Dockerize
	- [ ] Pick weather API sources and starting weather metrics
		- [ ] Hourly temp
		- [ ] Precipitation
	- [ ] Draw metrics visually
		- [ ] https://stackoverflow.com/questions/246525/how-can-i-draw-a-bezier-curve-using-pythons-pil
- [ ] v2?
	- [ ] Customizing physical location, configuring which metrics to show
	- [ ] Log time scale
	- [ ] Other metrics
		- [ ] Barometric pressure
		- [ ] AQI
		- [ ] Moon brightness / phase
		- [ ] Dawn/Sundise
		- [ ] Wind
		- [ ] UV index
		- [ ] Tides
	- [ ] Minimizing API calls, by writing to S3 as a cache or using a caching reverse-proxy
		- [ ] https://developers.cloudflare.com/r2/pricing/#free-tier
		- [ ] https://developers.cloudflare.com/cache/
	- [ ] think again about business brand / name
		- [ ] already exists: https://github.com/codersinthestorm/WhetherWeather
		- [ ] maybe pick another name or make it cute?
- [ ] Import from obsidian://open?vault=notes&file=MyNotes%2FWhetherWeather
