start =
  <b>hello, { $name }!</b>
    
  in this bot you can get information
  about the weather in your region or
  city. to learn more send /help

help =
  this bot will help you to always be
  aware about the weather. here is a
  list of commands i can handle:

  /start - to start the bot
  /help - get help about this bot


main =
  select what you want to do...


get_weather = 
  weather 🌦️

select_weather = 
  select date you want to know:

weather_today = 
  today ⬇️

weather_tomorrow =
  tomorrow 🔜

weather_week =
  week 7️⃣


set_location = 
  set location 🔄

wait_location = 
  okay now send me your location...

send_location =
  send location 🚩


cancel = 
  cancel ❌


invalid_message =
  sorry, i don't understand what you mean...


weather_description =
   {$weather_code ->
    [0] clear sky
    [1] mainly clear
    [2] partly cloudy
    [3] overcast
    [45] fog
    [48] depositing rime fog
    [51] light drizzle
    [53] moderate drizzle
    [55] dense intensity drizzle
    [56] light freezing drizzle
    [57] dense intensity freezing drizzle
    [61] slight rain
    [63] moderate rain
    [65] heavy rain
    [66] slight freezing rain
    [67] heavy freezing rain
    [71] slight snow fall
    [73] moderate snow fall
    [75] heavy snow fall
    [77] snow grains
    [80] slight rain showers
    [81] moderate rain showers
    [82] heavy rain showers
    [85] slight snow showers
    [86] heavy snow showers
    [95] thunderstorm
    [96] thunderstorm with slight hail
    [99] thunderstorm with heavy hail 
   *[other] undefined weather...
   }


current_weather_info =
  current weather info:
  🌡 temperature: { $temperature }{ $unit_temperature }
  💧 precipitation: { $precipitation }{ $unit_precipitation }
  🌦 description: { weather_description }
