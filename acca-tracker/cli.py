#!/usr/bin/python3

import click
from games import games
from teams import teams
from skybet import skybet

@click.group()
def cli():
    pass

@cli.command('skybet')
@click.option('--period', '-p', default=None, help='Specify month in YYYY-MM format')
def skybet_command(period):
    skybet(period)

@cli.command('teams')
def teams_command():
    teams()

@cli.command('games')
def games_command():
    games()

if __name__ == '__main__':
    cli()
