#!/usr/bin/python

import argparse, feedparser

def fetchData(url):
	return feedparser.parse(url)

def latest(args):
	d = fetchData('https://buildfeed.net/rss/')

	for entries in d.entries:
		print entries.title

def leaked(args):
	d = fetchData('https://buildfeed.net/rss/leaked/')

	for entries in d.entries:
		print entries.title

def added(args):
	d = fetchData('https://buildfeed.net/rss/added/')

	for entries in d.entries:
		print entries.title

def highest(args):
	d = fetchData('https://buildfeed.net/rss/version/')

	for entries in d.entries:
		print entries.title

def flights(args):
	availableFlights = ['low', 'medium', 'high']

	if args.risk not in availableFlights:
		args.risk = 'high'

	d = fetchData('https://buildfeed.net/rss/flight/' + args.risk)

	for entries in d.entries:
		print entries.title

if __name__ == '__main__':

	# Parser
	parser = argparse.ArgumentParser(prog='BuildFeed')
	parser.add_argument('--version', action='version', version='%(prog)s 0.1')
	subparsers = parser.add_subparsers()

	# Latest
	latest_p = subparsers.add_parser('latest')
	latest_p.set_defaults(func=latest)

	# Leaked
	latest_p = subparsers.add_parser('leaked')
	latest_p.set_defaults(func=leaked)

	# Added
	added_p = subparsers.add_parser('added')
	added_p.set_defaults(func=added)

	# Highest
	highest_p = subparsers.add_parser('highest')
	highest_p.set_defaults(func=highest)

	# Flights
	flights_p = subparsers.add_parser('flights')
	flights_p.add_argument('-r', '--risk', default='high', dest='risk')
	flights_p.set_defaults(func=flights)

	# Args
	args = parser.parse_args()
	args.func(args)