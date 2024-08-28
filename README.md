# Beer Bot: Dormitory Drinking Dashboard

## Overview
Beer Bot is a small project that mis(uses) the Turff API to create a beer consumption leaderboard for a student dormitory. It analyzes data from the Turff inventory system to determine which dormmate has consumed the most beer. The leaderboard is presented using a small Flask website.

## What is Turff?
[Turff](https://www.turff.nl/) is a service that provides an inventory management system for student dorms. It includes a tablet interface and a website for easy access and management.

## How it Works
- The script authenticates itself with a user profile.
- It extracts relevant information about beer consumption from the Turff server by (mis)using the Turff Api.
- The data is analyzed to calculate individual consumption totals.
- Results are used to create a leaderboard website using Flask.
- RaspberryPi boots and opens the website in Kiosk mode.

## Beer Bot in action

![foto](https://github.com/sjonnycapten/publicBierBot/assets/16917420/00d5f493-4bde-4971-aec2-e300a6a9be00)
