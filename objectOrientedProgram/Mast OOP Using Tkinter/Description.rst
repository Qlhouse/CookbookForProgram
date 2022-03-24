======================================
 ABQ Data Entry Program Specification
======================================

Description
------------

This program facilitates entry of laboratory observations into 
a CSV file.

Requirements
---------------

Functional Requirements:
  * Allow all relevant, valid data to be entered, 
    as per the data dictionary.
  * Append entered data to a CSV file:
    - The CSV file must have a filename of 
    abq_data_record_CURRENTDATE.csv, where CURRENTDATE is the date
    of the laboratory observations in ISO formay (year-month-day).
    - The CSV file must include all fields
    listed in the data dictionary.
    - The CSV headers will avoid cryptic abbreviations.
  * Enforce correct datatypes per field
  
Non-functional Requirements:
  * Enforce reasonable limits on data entered, per the data dict.
  * Auto-fill data to save time.
  * Suggest likely correct values.
  * Provide a smooth and efficient workflow.
  * Store data in a format easily understanble by Python.

Functionality Not Required
-------------------------------

The program does not need to:

  * Allow editing of data.
  * Allow deletion of data.
  
Users can perform both actions in LibreOffice if needed.

Limitations
---------------

The program must:

  * Be efficiently operable by keyboard-only users.
  * Be accessible to color blind users.
  * Run on Debian GNU/Linux
  * Run acceptably on a low-end PC.
  
Data dictonary
------------------

+-------+--------------+---------+-----------------+-------------------+
| Field |  Type   | Unit   | Valie Values    | Description    |
+=========+======+========+=============+=================+=============+
| Date     | Date    |    |        |  Date of record|
+-------+--------------+---------+-----------------+-------------------+
| Time     | Time    |    |8:00, 12:00, 16:00, 20:00  |  Time period   |
+-------+--------------+---------+-----------------+-------------------+
| Lab     | String    |    |  A - C     |  Lab ID   |
+-------+--------------+---------+-----------------+-------------------+
| Technician     | String    |    |        |  Technician name   |
+-------+--------------+---------+-----------------+-------------------+
| Plot     | Int    |    |  1-20      |  Plot ID   |
+-------+--------------+---------+-----------------+-------------------+
| Seed Sample     | String    |    |  6-character string   |  Seed sample ID   |
+-------+--------------+---------+-----------------+-------------------+
| Fault     | Bool    |    |  True, False   |  Environmental sensor fault   |
+-------+--------------+---------+-----------------+-------------------+
| Light     | Decimal    | klx   |  0-100   |  Light at plot blank on fault   |
+-------+--------------+---------+-----------------+-------------------+
| Humidity     | Decimal    | g/m³   |  0.5-52.0   |  Abs humidity at plot blank on fault   |
+-------+--------------+---------+-----------------+-------------------+
| Temperature     | Decimal    | °C   |  4-40   |  Temperature at plot blank on fault   |
+-------+--------------+---------+-----------------+-------------------+
| Blossoms     | Int    |    |  0-1000   |  No. blossoms in plot   |
+-------+--------------+---------+-----------------+-------------------+
| Fruit     | Int    |    |  0-1000   |  No. fruits in plot   |
+-------+--------------+---------+-----------------+-------------------+
| Plants     | Int    |    |  0-20   |  No. plants in plot   |
+-------+--------------+---------+-----------------+-------------------+
| Max Height     | Decimal    | cm   |  0-1000   |  Height of tallest plant in plot   |
+-------+--------------+---------+-----------------+-------------------+
| Min Height     | Decimal    | cm   |  0-1000   |  Height of shortest plant in plot   |
+-------+--------------+---------+-----------------+-------------------+
| Median Height     | Decimal    | cm   |  0-1000   |  Median height of plants in plot   |
+-------+--------------+---------+-----------------+-------------------+
| Notes     | String    |     |      |  Miscellaneous notes   |
+-------+--------------+---------+-----------------+-------------------+
