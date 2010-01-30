import sqlite3
import os.path
from sunspot import sunspot

class database(sunspot):
	c = sqlite3.Cursor(sqlite3.Connection('none'))
	
	def __init__(self, dbFileName):
		"""Parses the db file and cursor objects from dbFileName"""
		self.debug("-- Constructor -- " + dbFileName)
		
		elements = self.create(dbFileName)
		self.db = elements['db']
		self.c = elements['c']
		
	def create(self, dataFile):
		"""create database from dataFile"""
		#create new database and call connect
		#dataFile='F:\Dropbox\My Dropbox\programming\python\db'
		self.debug("-- Create --")
		
		elements = self.connect(dataFile)
		self.c.execute('''create table if not exists passCodes(site text unique, code)''')
		
		self.debug('table created')
		return elements
		
	def connect(self, dataFile):
		"""connect to database dataFile"""
		self.debug("-- connect -- " + dataFile)
		
		db = sqlite3.connect(dataFile)
		self.c = db.cursor()
		return {'db':db, 'c':self.c}
		
	def disconnect(self):
		"""disconnect database"""
		self.debug("-- disconnect --")
		
		self.db.close()

	def add(self, cred):
		"""add site to database"""
		self.debug ("-- add --")
		
		self.c.execute('insert or ignore into passCodes values (?,?)', cred)
		self.debug (cred[0] + ' added!')
		
		self.db.commit()

	def pull(self, site):
		"""return site from database"""
		self.debug ("-- pull --")
		
		self.debug ('pull====' + str(site))
		#print ('c' + self.c)
		
		self.c.execute('select * from passCodes where site=?', site)
		d = self.c.fetchall()
		
		self.debug ('Pull line:' + str(d))
		return d
		