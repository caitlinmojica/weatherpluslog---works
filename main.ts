/** 
BeeApp Weather Station Project 2020

By Caitlin Mojica (16947371)

Special thanks to Ramon and Nidhi for helping me code this shit.
Mostly Ramon for dedicating a lot of his time and mental capacity to help me.
Also Jeff, who has been there since the beginning, for pushing me to through this,
and for gathering all the resources and people I needed for this project.

Parts of this code was based off the micro:climate kit experiments from sparkfun.

 */
let current_WindDirection_List = ""
let current_WindSpeed = 0
let current_rain = 0
serial.redirectToUSB()
weatherbit.startWindMonitoring()
weatherbit.startRainMonitoring()
let header = ""
let logging_data = 0
logging_data = -1
basic.showString("ON")
// pause(1000)
while (logging_data == -1) {
    weatherbit.startWeatherMonitoring()
    serial.redirect(SerialPin.P15, SerialPin.P14, BaudRate.BaudRate9600)
    header = "Time" + "," + "Wind Speed" + "," + "Wind Direction" + "," + "Temperature" + "," + "Humidity" + "," + "Pressure" + "," + "Rain Level"
    pause(100)
    serial.writeLine(header)
    logging_data = 0
}
basic.forever(function on_forever() {
    //  Added rain
    
    weatherbit.startWeatherMonitoring()
    current_WindSpeed = Math.round(weatherbit.windSpeed())
    current_WindDirection_List = weatherbit.windDirection()
    let current_temp = Math.idiv(weatherbit.temperature(), 100)
    let current_humidity = Math.idiv(weatherbit.humidity(), 1024)
    let current_pressure = Math.idiv(weatherbit.pressure(), 25600)
    current_rain = Math.round(weatherbit.rain())
    let current_time = 0
    // Pauses execution of the function for the specified ms
    pause(1000)
    // For troubleshooting purposes, so we can see how long it takes per run
    basic.showString("TT")
    //  Don't know why this is here since it's already under the while loop
    serial.redirect(SerialPin.P15, SerialPin.P14, BaudRate.BaudRate9600)
    //  If "???" is displayed, wind direction is unknown!
    serial.writeLine("" + current_time + "," + ("" + current_WindSpeed) + "," + ("" + current_WindDirection_List) + "," + ("" + current_temp) + "," + ("" + current_humidity) + "," + ("" + current_pressure) + "," + ("" + current_rain) + "\n")
})
