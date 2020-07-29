# Tally3.0
#### It's like paper, but better

## Introduction
Tally3.0 is a Python Flask application designed to replace paper record keeping methods
for logging patron interactions at the library. At its heart, it is a simple CRUD application with
some fancy, but not terribly complicated, reporting functionality.

## Changelog
7/29/2020
* Added export to CSV functionality
* Added CSS styling to all pages

7/24/2020
* Wrote the program

## Planned Upcoming Features
* ~~Adding CSS (ha)~~
* Filter by interaction type when running report
* ~~Export table to Excel/CSV~~
* Build out Docker deployment

## How it Works
### Tallying
The program is designed for two departments, Information Services and Youth Services. When a user navigates to
the web page, they'll be asked to select a department. From there, they are sent to identical forms with a few
simple options. After an interaction with a patron, they can select the category of interaction, select if they 
made a referral or not (IE sent someone to circulation or IT for help), and enter any notes that may be relevant.
After all this, the user clicks Tally!

The date and time of the interaction is recorded into the database, along with all the information the user entered 
and their department (as determined by which page they are recording a tally from). The user can continue to record 
interactions as often as necessary.

### Reporting
Along the top of the webpage is a reports button. Clicking on this will bring the user to a reporting form. For
convenience, the form automatically populates for the current month's worth of reports from all department, for all
referral types, and all times. This can, of course, be customized using the form. Once the report has been built,
the user can click "Run Report" to have the report built out for them.

This will generate an HTML table with all the relevant inquiries listed based on the report parameters. 
For convenience, again, the total number of interactions displayed by the current report is always listed at
the top of the table. So, if you only wanted to get the total number of interactions with patrons this month,
you can do so with two clicks. Reports>Run Report (since the date information is auto filled!)

This table can also be exported to a CSV file for opening in your spreadsheet application
of choice. This export leverages the Flask-Excel plugin and is generated directly from the
database query

## Deployment Instructions
Tally3.0 is designed to be deployed locally in a Docker container on a Linux server. 
(Docker file and scripts forthcoming)