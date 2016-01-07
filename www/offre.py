from flask import Flask
from sqlite3 import *
from site_config import *
from db_config import db_url, query_select_offre

class offre(object):
	def __init__(self, number):
		self.id = number
		self.db = sqlite3.connect(db_url)
		self.hydrate()
		return self
		
	def hydrate(self):
		self.db.execute(query_select_offre, self.number)
		r = self.db.fetchone()
		for k in r.keys():
			self.setattr(k, r[k])
		return self

	def afficher(self):
		return render_template('offre.html', self)
