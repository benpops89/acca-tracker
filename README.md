# acca-tracker
Keep track of NFL bets

## Prerequisites
Before proceeding any further make sure the following are available on the system.
* Docker
* docker-compose
* Python 3.8
* Pip3

## Build
Clone the repository into $HOME/projects. Then run the `install.sh` script which will setup the python dependencies and cli command.

## Deployment
Navigate to the root of the project and run `docker-compose up -d` to bring up the docker containers

## Setup
Before bets can be added, both the teams and games (for current week) need to be added.
* Run `accatracker teams` to add the teams to the database
* Run `accatracker games` to add the current weeks games to the database

## Getting bets from SkyBet
To receive bets from SkyBet run `accatracker skybet`. It will then ask you to enter your username and pin. When you have done this the bets will be retrieved. Each bet will be shown for you to give it a name. When you have added names for all bets you will be ready to go.

## Viewing status of bets
To view the status of bets got to `http://<ip_address>/<year>/<week>`
* `ip_address` is the ip address of the machine where docker is running
* `year` is the current season for NFL e.g. 2020
* `week` the current week e.g. 1

## Updating the games
When the games have started you need to start the game updating script which updates the database with the latest scores every 30 seconds. To start this script navigate to `$HOME/projects/acca-tracker/acca-tracker` and run `python update.py`.
