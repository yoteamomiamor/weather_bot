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


menu =
  menu

main =
  select what you want to do...


get_weather = 
  weather 🌦️

select_weather = 
  select date you want to know:

select_weather_placeholder =
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
  okay now send me the location where you want 
  to get weather or press the button below to
  send me your current location

send_location =
  send location 🚩

send_location_placeholder =
  send me location or press the button:

location_is_set =
  your location has been set sucessfully!
  here is info about this location:
   - latitude: { $latitude }
   - longitude: { $longitude }


cancel = 
  cancel ❌


invalid_message =
  sorry, i don't understand what you mean...


weather_description =
   { $weather_code ->
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
  🌡 temperature: { $temperature_2m }
  💧 precipitation: { $precipitation }
  🌦 description: { weather_description }


where =
  your current set location is:
   - latitude: { $latitude }
   - longitude: { $longitude }


weather_by_hours =
  <b>{ $time }</b>
    - temperature: <b>{ $temperature_2m }</b>
    - feels like: { $apparent_temperature }
    - humidity: { $relative_humidity_2m }
    - precipitation probability: <b>{ $precipitation_probability }</b>
    - precipitation: { $precipitation }
    - cloud cover: { $cloud_cover }
    - visibility: { $visibility }
    - wind speed: { $wind_speed_10m }
    - description: <b>{ weather_description }</b>


one_day_weather =
  here is the weather for { $day_name }:

week_weather =
  here is the weather for the upcoming week:


date_from_now =
  { $day ->
  [0] today
  [1] tomorrow
  [2] the day after tomorrow
  [3] in three days
  [4] in four days
  [5] in five days
  [6] in six days
 *[other] another day
  }


weekday =
  { $day ->
    [0] Monday
    [1] Tuesday
    [2] Wednesday
    [3] Thursday
    [4] Friday
    [5] Saturday
    [6] Sunday
   *[other] not set day
  }

months =
  { $month ->
    [1] January
    [2] February 
    [3] March
    [4] April
    [5] May
    [6] June
    [7] July
    [8] August
    [9] September
    [10] October
    [11] November
    [12] December
   *[other] unknown month
  }


no_set_location =
  sorry, but it seems like you haven't set the location yet ;(
  
  you can do it in the <b>{ menu } &gt; { set_location }</b> and send the location where you want to get weather
