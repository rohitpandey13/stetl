#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Main ETL program.
#
# Author: Just van den Broecke
#
import os
import sys
from ConfigParser import ConfigParser
from setl.util import Util
from setl.chain import Chain
import StringIO

log = Util.get_log('ETL')

# The main class: build Chains of Components from a config and let them run
class ETL:
	def __init__(self, options_dict, args_dict=None):
		# Assume path to config .ini file is in options dict
		# args_dict is optional and is used to do string substitutions in options_dict.config file
		config_file = options_dict.get('config_file')

		if not os.path.isfile(config_file):
			print 'No config file found at: %s' % config_file
			sys.exit(1)

		log.info("Reading config_file = %s" % config_file)

		self.configdict = ConfigParser()

		try:
			if args_dict:
				log.info("Substituting %d args in config file from args_dict: %s" % (len(args_dict), str(args_dict)))
				# Get config file as string
				file = open(config_file, 'r')
				config_str = file.read()
				file.close()

				# Do replacements  see http://docs.python.org/2/library/string.html#formatstrings
				config_str = config_str.format(**args_dict)

				log.info("Substituting args OK")
				# Put Config string into buffer (readfp() needs a readline() method)
				config_buf = StringIO.StringIO(config_str)

				# Parse config from file buffer
				self.configdict.readfp(config_buf, config_file)
			else:
				# Parse config file directly
				self.configdict.read(config_file)
		except Exception, e:
			log.error("Fatal Error reading config file: err=%s" % str(e))

	def run(self):
		# The main ETL processing
		log.info("START")
		t1 = Util.start_timer("total ETL")

		# Get the ETL Chain pipeline config strings
		chains_str = self.configdict.get('etl', 'chains')
		if not chains_str:
			raise ValueError('ETL chain entry not defined in section [etl]')

		# Multiple Chains may be specified in the config
		chains_str_arr = chains_str.split(',')
		for chain_str in chains_str_arr:
			# Build single Chain of components and let it run
			chain = Chain(chain_str.strip(), self.configdict)
			chain.assemble()

			# Run the ETL for this Chain
			chain.run()

		Util.end_timer(t1, "total ETL")

		log.info("ALL DONE")
