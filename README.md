# cityscience_traffic

A (Django) RESTful API providing traffic counts for Devon, South West.


The API root (127.0.0.1:8000) Offers two means of accessing data:


"records" - Provides traffic counts per record (a record defined by location and time), with record-level filtering (year, estimation method, detailed estimation method, road and road category), and vehicle counts as a nested list.

"vehiclecounts" - Provides a traffic counts per vehicle type, with granular filtering on both record and vehicle type.


Uses Postgres

Use import_data.py to import csv data (e.g. Devon.csv) via the Django ORM into a Postgres database using Pandas for data inspection.