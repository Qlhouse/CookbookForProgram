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
  * Enforce reasonable limits on data entered, per the data dict
