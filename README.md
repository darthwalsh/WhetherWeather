# Whether Weather

In-progress weather tool that renders an image for a home screen widget.

See the image hosted for free on fly.io:
![server](https://whetherweather.fly.dev/render)

## Dev Flow

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python app.py
```

Then see [widget docs](docs/widgets.md) for how to use the image in a widget.

## Running locally

Uvicorn is a ASGI server:

```bash
python -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Insider docker:

```bash
docker build -t whetherweather .
docker run -p 8000:8000 whetherweather
```

## Tasks
- [x] PoC
	- [x] Create PNG image
	- [x] localhost serve image
	- [x] Some docs for showing the image in a widget
	- [x] Call a weather API, get i.e daily max/min temps
	- [x] Render the temps on the image
- [ ] MVP 1
	- [x] Deploy cron task to cloud i.e. fly.io
		- [x] Install dependencies
		- [x] Dockerize
	- [ ] fly.io secrets management
	- [ ] Pick weather API sources and starting weather metrics
		- [ ] Hourly temp
		- [ ] Precipitation
	- [ ] Figure out the exact size of my android home screen for rendering
	- [ ] Draw metrics visually
		- [ ] https://stackoverflow.com/questions/246525/how-can-i-draw-a-bezier-curve-using-pythons-pil
- [ ] v2?
	- [ ] https://fly.io/docs/app-guides/continuous-deployment-with-github-actions/
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
