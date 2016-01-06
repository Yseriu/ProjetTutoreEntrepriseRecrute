db_url = ''
query_select_offre = 'SELECT * FROM offre WHERE id=?'

class list_offres(object):
	
	def __init__(self):
		ans = 'SELECT * FROM offre'
		self.dom = set()
		self.level = set()
		self.sal = None
		self.loc = None
		
		self.condition = False
		
	def add_condition(self):
		if not condition:
			self.ans += ' WHERE '
			self.condition = True
		else:
			self.ans += ' AND '
	
	def add_domaine(self, domaine):
		self.dom.add(domaine)
		return self
	
	def remove_domaine(self, domaine):
		self.dom.discard(domaine)
		return self
	
	def add_level(self, level):
		self.l.add(level)
		return self
		
	def remove_level(self, level):
		self.l.discard(level)
		return self

	def set_salaire(self, salaire):
		self.sal = salaire
		return self
	
	def set_localisation(self, localisation):
		self.loc = localisation
		return self
		
	def build(self):
		if self.dom != set():
			self.add_condition()
			for domaine in self.dom:
				ans += ' secteur_activite LIKE %'+dom+'% OR '
			ans = ans[:-3]
		if self.level != set():
			self.add_condition()
			for level in self.level:
				ans += ' niveau_etude_requis LIKE %'+dom+'% OR '
			ans = ans[:-3]
		if self.sal != None and self.sal != 0:
			self.add_condition()
			ans += ' salaire > ' + str(self.sal)
		if self.loc != None and self.loc != '':
			self.add_condition()
			ans += ' pays LIKE %' + loc + '% '
		return self
	
	def get(self):
		return self.ans
				
				
				
