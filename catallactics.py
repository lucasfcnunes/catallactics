#import time
import weakref
import random
random.seed(0)

class Spacetime():
    def __init__(self, parent):
		self.parent = weakref.ref(parent)
		self.name = ['spacetime', 'time', 'space']
        self.time = 0
        self.space = {}
    def tick(self): #travel time
		for human in parent.humans:
			human.increase_age()
        self.time+=1 #one second?
        return self.time
	def travel_time(self): #same as tick
		return tick()
	def travel_space():
		pass
        
class Universe():
    '''Scarse resources universe.'''
    def __init__(self):
        print("Hello World")
        #*all below items are scarse*
        self.spacetime = Spacetime(self)
        self.scarse_resources = [self.spacetime]
		self.humans = []
	def _del_(self):
		print('You\'ve destroyed the Universe {}... Why\'d do that?'.format(self))
uni = Universe()

class ScarceResource():
    def __init__(self, name = []):
        uni.scarse_resources.append(self)
        self.name = name
		self.location = (lat=)
[ScarceResource(random.choice(population=['land', 'food', 'gold'], weights=[0.9, 0.09, 0.01])) for _ in range(100)] #non-persons, scarcity reality, big bang


class Mind():
	def __init__(self, property, parent):
		self.parent = weakref.ref(parent)
		self.wants = [] #['fun']
		self.property = property
		self.knowledge = []
	def plan(self):
		body = self.parent.body
		for need in body.needs:
			for resource in uni.scarse_resources:
				if need is resource.name:
					
		pass
		
class Body():
	def __init__(self, parent):
		self.parent = weakref.ref(parent)
		self.alive = True
		self.needs = {'food':} # 'sex', 'drugs', etc...?
		self.body = ScarceResource(['body', random.choice(['male', 'female'])])
		self.age = 0 #-23328000 #~-9 months
	def act(self):
		pass

def _delay_end(d):
	if d<0:
		pass #raise an error?
	else:
		t0 = uni.spacetime.time
		while uni.spacetime.time-t0<d:
			yield False
	yield True
	
class Person():
    def __init__(self):
        uni.humans.append(self)
        self.body, self.mind = Body(self), None #methodological dualism
        #self.name = 'Malboro'
		#self.parents = {'biofather':,'biomother':}
	def __del__():
		print('Person {person} (age={age}) died...'.format(person=self, age=self.body.age))
		#maybe mind still lives? who knows...
	def action_axiom(self):
		self.mind.plan()
			
	def increase_age(self):
		follow_ego = action_axiom
		delay_end = _delay_end(5)
		while self.body.alive:
			if mind is None and self.body.age > 32000000: #~1yo
			'''Gets mind! :)'''
				#put maybe not occasion
				self.mind = Mind(property=[self], self)
			if mind is not None:
				if next(delay_end):
					follow_ego()
					delay_end = _delay_end(random.randint(3, 10))
				if self.body.age > 433620000: #~13.75yo
				'''Sexuality'''
					self.mind.wants.append('sex')
			if self.body.age > 1734480000: #~55yo
			'''Old age/"Natural causes" death'''
				#improve using statistics
				self.body.alive = False
				del self
			yield self.body.age
			self.body.age+=1
        