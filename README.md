KNMI-data-import
================

Import script of daily data for a given set of weather stations into mysql.

* Create tables by using create_tables.sql
* Edit knmi_daily_data_import.py, change MySQL variables and stationcode and/or starting date.
* Edit knmi_hourly_data_import.py, change MySQL variables and stationcode and/or starting date.
* Run like "python knmi_daily_data_import.py" or "python knmi_hourly_data_import.py"

TODO:

* Clean up code
* Add configuration file
