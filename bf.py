#!/usr/bin/python

import argparse, feedparser

def fetchData(url):
	return feedparser.parse(url)

def getData(args):
	types = { 
		'latest'	:'version', 
		'leaked'	:'leaked',
		'added'		:'added',
		'highest'	:'version',
		'flights'	:'flight',
		'branch'	:'lab'
	}


	risk = '';

	availableFlights = ['canary', 'osg', 'msit', 'wif', 'wis']

	if args.type is 'flights':
		risk = args.risk if args.risk in availableFlights else 'wif'

	if args.type is 'branch':
		risk = args.lab

	# Fetch the data
	d = fetchData('https://buildfeed.net/rss/' + types[args.type] + '/' + risk)

	for entries in d.entries:
		print entries.title

if __name__ == '__main__':

	# Parser
	parser = argparse.ArgumentParser(prog='BuildFeed')
	parser.add_argument('--version', action='version', version='%(prog)s 0.2.1')
	subparsers = parser.add_subparsers()

	# Latest
	latest_p = subparsers.add_parser('latest')
	latest_p.set_defaults(func=getData, type='latest')

	# Leaked
	latest_p = subparsers.add_parser('leaked')
	latest_p.set_defaults(func=getData, type='leaked')

	# Added
	added_p = subparsers.add_parser('added')
	added_p.set_defaults(func=getData, type='added')

	# Highest
	highest_p = subparsers.add_parser('highest')
	highest_p.set_defaults(func=getData, type='highest')

	# Flights
	flights_p = subparsers.add_parser('flights')
	flights_p.add_argument('-r', '--risk', default='high', dest='risk')
	flights_p.set_defaults(func=getData, type='flights')

	# Branch
	branch_p = subparsers.add_parser('branch')
	branch_p.add_argument('-b', '--branch', default='winmain', dest='lab')
	branch_p.set_defaults(func=getData, type='branch')

	# Args
	args = parser.parse_args()
	args.func(args)