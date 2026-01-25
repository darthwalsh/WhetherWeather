# Interesting Weather APIs

## Weather
https://github.com/chubin/wttr.in#json-output

## Sunrise
JS lib: sun position, sunlight phases (times for sunrise, sunset, dusk, etc.) https://github.com/mourner/suncalc
PY lib: https://astral.readthedocs.io/en/latest/

https://www.meteomatics.com/en/api/available-parameters/sun/
## Current Marin rain map:
Novato dash: [https://marin.onerain.com/dashboard/?dashboard=a81a8621-b09c-4226-b931-7ad67ecf90d0](https://marin.onerain.com/dashboard/?dashboard=a81a8621-b09c-4226-b931-7ad67ecf90d0)  
[https://marin.onerain.com/map/?view_id=3&view=d878ca91-5a81-4cc7-8510-21576eb4b8c7](https://marin.onerain.com/map/?view_id=3&view=d878ca91-5a81-4cc7-8510-21576eb4b8c7)
has historical charts going back years
Also has https://marin.onerain.com/site/?site_id=16801&site=4d8e2f5a-380f-4ae9-bb7b-367326350038 for pacheco pond
Doesn't seem to have a download API though, and the download links don't support `curl`

*linked from [https://marinflooddistrict.org/weather-gauges/](https://marinflooddistrict.org/weather-gauges/)*
## Moon
moon position and lunar phase https://github.com/mourner/suncalc

brightness taking into account cloud cover? https://www.meteomatics.com/en/api/available-parameters/moon/
https://www.meteomatics.com/en/weather-api/#api-packages

wttr.in/Moon
## Historical weather 
https://openweathermap.org/history 
But: https://openweathermap.org/full-price#history **150 USD**/ month

Or, store values from https://openweathermap.org/current in database
## Air Quality AQI
https://openweathermap.org/api/air-pollution
## Barometric pressure
Heard from Allan that having both static and dynamic pressure might be interesting for predicting storms
## Feels-Like temperature
- [ ] See if normal weather API has this too
- [ ] See if it tracks better "feeling cold" when running

## TODO
https://www.meteomatics.com/en/api/available-parameters/#api-basic
Free API with historical 24hr rain