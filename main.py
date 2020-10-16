"""
BeeApp Weather Station Project 2020

By Caitlin Mojica (16947371)

Special thanks to Ramon and Nidhi for helping me code this shit.
Mostly Ramon for dedicating a lot of his time and mental capacity to help me.
Also Jeff, who has been there since the beginning, for pushing me to through this,
and for gathering all the resources and people I needed for this project.

Parts of this code was based off the micro:climate kit experiments from sparkfun.
"""

current_WindDirection_List = ""
current_WindSpeed = 0
current_rain = 0
serial.redirect_to_usb()
weatherbit.start_wind_monitoring()
weatherbit.start_rain_monitoring()

header = ""
logging_data = 0
logging_data = -1

basic.show_string("ON")
#pause(1000)

while logging_data == -1:
    weatherbit.start_weather_monitoring()
    serial.redirect(SerialPin.P15, SerialPin.P14, BaudRate.BAUD_RATE9600)
    header = "Time" + "," + "Wind Speed" + "," + "Wind Direction" + "," + "Temperature" + "," + "Humidity" + "," + "Pressure" + "," + "Rain Level"
    pause(100)
    serial.write_line(header)
    logging_data = 0

def on_forever():
    # Added rain
    global current_WindSpeed, current_WindDirection_List, current_rain

    weatherbit.start_weather_monitoring()
    current_WindSpeed = (Math.round(weatherbit.wind_speed()))
    current_WindDirection_List = weatherbit.wind_direction() 
    current_temp = (Math.idiv(weatherbit.temperature(), 100))
    current_humidity = (Math.idiv(weatherbit.humidity(), 1024))
    current_pressure = (Math.idiv(weatherbit.pressure(), 25600))
    current_rain = (Math.round(weatherbit.rain()))
    current_time = 0

    #Pauses execution of the function for the specified ms
    pause(1000) 
    #For troubleshooting purposes, so we can see how long it takes per run
    basic.show_string("TT")
    # Don't know why this is here since it's already under the while loop
    serial.redirect(SerialPin.P15, SerialPin.P14, BaudRate.BAUD_RATE9600)
    # If "???" is displayed, wind direction is unknown!
    serial.write_line(str(current_time) + "," + str(current_WindSpeed) + "," + str(current_WindDirection_List) + "," + str(current_temp) + "," + str(current_humidity) + "," + str(current_pressure) + "," + str(current_rain) + "\n")

basic.forever(on_forever)