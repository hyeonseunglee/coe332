# Homework 4/Midterm README

This is the README for the forth homework assignment of COE 332 SP21. 

## Getting Started

For this assignmemt, both the Flask App and the redis database are containerized. Follow the following steps to deploy both the Flask app and the database:

1. Run `docker-compose build --no-cache` : build with `--no-cache` just to ensure that you are not referrecing any old images.
2. Run `docker-compose up -d`
 
## Pulling Data from animals.json to the redis database

`animals.json` contains the updated set of 20 animals, including their timestamps and uids.
Run `curl localhost:5017/redisanimals` to upload the animals in the json file to the redis database. This should also return a printed statement of all the animals and their information.

## Query a Range of Dates+Times

In order to query a set of animals that were created within the user-specific range of dates+times, run `curl "localhost:5017/query_by_dates?startdate=YYYY-MM-DDTHH:MM:SS.SS&enddate=YYYY-MM-DDTHH:MM:SS.SS"` where YYYY is year, MM is month, DD is day, T is a placeholder (short for time), HH is hour, MM is minute, SS.SS is second in decimal form. 

## Select a Particular Creature by Its Unique Identifier

In order to search and print a particular animal by its unique identifier "uid", run `curl "localhost:5017/search_by_ID?uid=XXXXXX"` where XXXXXX is the placeholder for a specific uid code.

## Edit a Particular Creatuer by Passing the UID and Updated Stats

In order to search and modify a particular animals by its UID identifier and specific stats, run `curl "localhost:5017/edit_by_ID?uid=XXXXXX&newhead=NEWHEAD&newbody=NEWBODY&newarms=INTEGER&newlegs=INTEGER&newtail=INTEGER"` where XXXXXX is a placeholder for the specific UID, NEWHEAD and NEWBODY are placeholders for user-specified head and body information, and INTEGER is a placeholder for integer values. You are not required to modify all five details of an animal; you can pick and choose which stats you would like to modify.

## Delete a selection of animals by a date+time range

This is similar to /query_by_dates, except that you are deleting the animals that fall under the specified range of date+time combinations. Run `curl "localhost:5017/delete_by_dates?startdate=YYYY-MM-DDTHH:MM:SS.SS&enddate=YYYY-MM-DDTHH:MM:SS.SS"` where YYYY is year, MM is month, DD is day, T is a placeholder (short for time), HH is hour, MM is minute, SS.SS is second in decimal form. 

## Return the average number of legs per animal

Run `curl localhost:5017/average_legs`

## Return the total count of animals

Run `curl localhost:5017/total_count`

