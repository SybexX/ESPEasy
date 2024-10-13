Import("env")
import os

# access to global construction environment
#print env

# Dump construction environment (for debug purpose)
#print env.Dump()

# append extra flags to global build environment
# which later will be used to build:
# - project source code
# - frameworks
# - dependent libraries
custom_defines = []
#env.Append(CPPDEFINES=[
  # ,"NO_HTTP_UPDATER"
  # ,("WEBSERVER_RULES_DEBUG", "0")
#])
if os.path.isfile('src/Custom.h'):
  custom_defines=["-DUSE_CUSTOM_H"]
else:
  custom_defines=[
    "-DCONTROLLER_SET_ALL",
    "-DNOTIFIER_SET_NONE",
    "-DPLUGIN_BUILD_NONE",
    "-DUSES_P001",  # Switch
    "-DUSES_P002",  # ADC
    "-DUSES_P003",  # Generic pulse counter
    "-DUSES_P004",  # Dallas DS18b20
    "-DUSES_P026",  # System info
    "-DUSES_P027",  # INA219
    "-DUSES_P028",  # BME280
    "-DUSES_P033",  # Dummy
    "-DUSES_P036",  # FrameOLED
    "-DUSES_P045",  # MPU6050
    "-DUSES_P049",  # MHZ19
    "-DUSES_P052",  # SenseAir
    "-DUSES_P056",  # SDS011-Dust
    "-DUSES_P059",  # Encoder
    "-DUSES_P080",  # Dallas iButton
    "-DUSES_P081",  # Cron
    "-DUSES_P082",  # GPS
    "-DUSES_P085",  # AcuDC24x
    "-DUSES_P098",  # PWM motor

    "-DUSES_P100",  # Pulse Counter - DS2423
#   "-DUSES_P087",  # Serial Proxy
#   "-DUSES_P094",  # CUL Reader
#   "-DUSES_P095",  # TFT ILI9341
    "-DUSES_P097",  # Touch (ESP32)
    "-DUSES_P106",  # BME680
    "-DUSES_P107",  # SI1145 UV index

    "-DUSES_P146",  # Cache Reader
    "-DUSES_P169",  # AS3935 Lightning Detector 

    "-DUSES_P173",  # Environment - SHTC3

    "-DUSES_C016",  # Cache Controller
    "-DUSES_C018",  # TTN/RN2483
#   "-DUSES_C015",  # Blynk

    "-DUSES_N001",  # E-mail

    "-DFEATURE_MQTT_TLS=1",
    "-DFEATURE_EMAIL_TLS=1",
    "-DFEATURE_EXT_RTC=1",
    "-DFEATURE_SD=1",
    "-DFEATURE_I2CMULTIPLEXER=1",
    "-DFEATURE_TRIGONOMETRIC_FUNCTIONS_RULES=1",

    "-DFEATURE_PLUGIN_STATS=1",
    "-DFEATURE_CHART_JS=1",

    "-DTESTING_FEATURE_USE_IPV6",

    "-DFEATURE_SETTINGS_ARCHIVE=1",
    "-DFEATURE_DEFINE_SERIAL_CONSOLE_PORT=1",
    "-DFEATURE_ESPEASY_P2P=1",
    "-DFEATURE_CUSTOM_PROVISIONING=1",
    "-DDISABLE_SC16IS752_SPI"
  ]



my_flags = env.ParseFlags(env['BUILD_FLAGS'])
my_defines = my_flags.get("CPPDEFINES")
env.Append(BUILD_FLAGS=custom_defines)
#defines = {k: v for (k, v) in my_defines}

print("\u001b[32m Custom PIO configuration check \u001b[0m")
# print the defines
print("\u001b[33m CPPDEFINES: \u001b[0m  {}".format(my_defines))
print("\u001b[33m Custom CPPDEFINES: \u001b[0m  {}".format(custom_defines))
print("\u001b[32m ------------------------------- \u001b[0m")


if (len(my_defines) == 0):
  print("\u001b[31m No defines are set, probably configuration error. \u001b[0m")
  raise ValueError