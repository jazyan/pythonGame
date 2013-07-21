from sys import exit
from random import randint

class Scene(object):
   
   def enter(self):
      print "This scene is not yet configured. Subclass it and implement enter()."
      exit(1)

class Engine(object):
   
   def __init__(self, scene_map):
      self.scene_map = scene_map

   def play(self):
      current_scene = self.scene_map.opening_scene()

      while True:
         print "\n-----------"
	 next_scene_name = current_scene.enter()
	 current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
   
   quips = [
      "Gregory Goyle called, he wants his brain back. GAME OVER.",
      "Your performance has Dumbledore rolling in his grave. GAME OVER.",
      "When I think of failures, I'll remember this one. Always. GAME OVER.",
      "Your intellect rivals Dudley Dursley's. GAME OVER.",
      "A troll would have done better than you. GAME OVER."
   ]

   def enter(self):
      print Death.quips[randint(0, len(self.quips)-1)]
      exit(1)

class Hogwarts(Scene):
   
   def enter(self):
      print "You just got your letter from Hagrid. Lucky you!"
      print "Bright-eyed and eager, you enter Hogwarts."
      print "What would you like to do?"
      print "1 to visit Dumbledore in his office."
      print "2 to stroll into the Chamber of Secrets."
      print "3 to get sorted in the Great Hall."
      print "4 to check out the Forbidden Forest."
      print "5 to get a wand from Ollivander's."

      action = raw_input("> ")

      if action == '1':
         return "dumbleoffice"
      elif action == '2': 
         return "secrets"
      elif action == '3':
         return "greathall"
      elif action == '4':
         return "forest"
      elif action == '5':
         return "ollivanders"
      else:
         print "You don't know how to follow directions, do you?"
         return "death"

class DumbleOffice(Scene):
   
   def enter(self):
      print "You must think you're all that, visiting the headmaster"
      print "on your first day. You enter the office, but Dumbledore doesn't" 
      print "seem to be here. The windows are wide open, and wind howls through"
      print "the office. On his desk is a note, pinned down with a marble"
      print "elephant paperweight."
      print "It reads:"
      print "'SCORPION BAILOR, ROVING AROUND AQUARIUMS,"
      print "LEAVE GUITARISTS IN THE ROLE OF KAISER RECIPROCANT."
      print "IMAGINE: ARBUTUS SPLICES IN A CREANCE.'"
      print "What is the answer?"
      
      guess = raw_input("> ").lower()
      code = "nonmarketable"
      guesses = 0 

      while guess != code and guesses < 5:
         print "BZZzzZZzzZZEDDEDdded"
	 guesses += 1
	 guess = raw_input("> ").lower()
      
      if guess == code:
         print "Awesome!!"
	 print "Where to now?"
	 print "1 for Forbidden Forest"
	 print "2 for Great Hall"
	 print "3 for Chamber of Secrets"
	 print "4 for Ollivander's"
	 answer = raw_input("> ")
	 if answer == '1':
	    return "forest"
	 elif answer == '2':
	    return "greathall"
	 elif answer == '3':
	    return "secrets"
	 elif answer == '4':
	    return "ollivanders"
         else:
            print "You don't know how to follow directions, do you?"
            return "death"

      else:
         print "Too many tries!"
	 return "death"

class Chamber(Scene):

   def enter(self):
      print "You stroll into the Chamber of Secrets. Suddenly, a wild"
      print "basilisk appears! Suddenly, the snake starts talking."
      print "'Answer this riddle, and I will let you go:'"
      print "'I never was, am always to be;"
      print " No one has seen me, nor will they see."
      print " Close to sun's set, and far from sunrise;"
      print " I will live on, till time's own demise.'"
      print "What is your answer?"
      guess = raw_input("> ").lower()
      code = "tomorrow"
      guesses = 0

      while guess != code and guesses < 5:
         print "BzZZZZZZzZzzsszsz!"
	 guesses += 1
	 guess = raw_input("> ").lower()
	 
      if guess == code:
         print "The basilisk slinks away. You WIN!!!"
	 exit(1)
      
      else:
         print "You ate too many Chocolate Frogs on the"
         print "train, which limits both your mental and physical processes."
	 return 'death'

class GreatHall(Scene):

   def enter(self):
      print "Finally decided to get sorted, eh? Good for you."
      print "Professor McGonagall places the wrinkly old Sorting Hat on"
      print "your head. It whispers: "
      print "\t'If you wish to be sorted, answer the following riddle: '"
      print "\t'What is the next number in this sequence?"
      print "\t 1 2 3 4 6 7 8 11 14 15 16 20 26'"

      guess = raw_input("> ")
      code = '30'
      guesses = 0

      while guess != code and guesses < 5:
         print "The Sorting Hat groans. Try again."
	 guesses += 1
	 guess = raw_input("> ")

      if guess == code:
         print "The Sorting Hat shouts: 'Ravenclaw!'"
	 print "The Great Hall explodes in applause. Congrats!"
	 print "Where to now?"
	 print "1 for Dumbledore's Office"
	 print "2 for Forbidden Forest"
	 print "3 for Chamber of Secrets"
	 print "4 for Ollivander's"
	 answer = raw_input("> ")
	 if answer == '1':
	    return "dumbleoffice"
	 elif answer == '2':
	    return "forest"
	 elif answer == '3':
	    return "secrets"
	 elif answer == '4':
	    return "ollivanders"
         else:
            print "You don't know how to follow directions, do you?"
            return "death"
      
      else:
         print "The Sorting Hat shouts: 'Slytherin!'"
	 return "death"

class Ollivander(Scene):

   def enter(self):
      print "You enter the shop, which is oddly dark. Suddenly, a noseless"
      print "freak appears! Oh noes, it's Voldemort!"
      print "'Hello, young wizard. Would you like to join the Dark Side?"
      print " Only the most intelligent can join. Answer the following riddle,"
      print " and I'll consider your application."
      print "\t I fly when I'm born,"
      print "\t Lay when I'm alive,"
      print "\t And run when I'm dead."
      print "\t What am I?'"

      guess = raw_input("> ").lower()
      code = "snow"
      guesses = 0

      while guess != code and guesses < 5:
         print "BZSZSasfadasfzzsszszs!"
	 guesses += 1
	 guess = raw_input("> ").lower()

      if guess == code:
         print "Voldemort looks delighted, and shakes your hand vigorously."
	 print "YOU WIN!"
         exit(1) 
      
      else:
         print "'That was disappointing,' sighed Voldemort. 'Avada Kedavra!'"
	 return 'death'

class Forest(Scene):
   
   def enter(self):
      print "You decided to venture into the Forbidden Forest. It is dark,"
      print "and you soon regret your decision. A ginormous spider appears,"
      print "and it looks hungry... It says: "
      print "'Hello, I am here to eat foolish students who wander into the"
      print " Forbidden Forest. I'll give you one more chance to prove you're"
      print " not foolish. Answer the following riddle:"
      print "\t Tossed from the window, and a lonely wife will grieve."
      print "\t Put back in the door, and someone who gives life appears."
      print "\t What am I?"

      guess = raw_input("> ").lower()
      code = "n"
      guesses = 0

      while guess != code and guesses < 5:
         print "BZSZSZSZSzzsszszs!"
	 guesses += 1
	 guess = raw_input("> ").lower()

      if guess == code:
         print "The spider looks disappointed, and creeps away."
	 print "You live! Rejoice!"
	 print "Where to next?"
	 print "1 to visit Dumbledore in his office."
         print "2 to stroll into the Chamber of Secrets."
         print "3 to get sorted in the Great Hall."
         print "4 to get a wand from Ollivander's."
         action = raw_input("> ")

         if action == '1':
            return "dumbleoffice"
         elif action == '2': 
            return "secrets"
         elif action == '3':
            return "greathall"
         elif action == '4':
            return "ollivanders"
         else:
            print "You don't know how to follow directions, do you?"
            return "death"
      else:
         print "'HAHA!' exclaims the spider. You are eaten."
	 return 'death'

class MaraudersMap(object):

   scenes = {
      'hogwarts': Hogwarts(),
      'dumbleoffice': DumbleOffice(),
      'forest': Forest(),
      'greathall': GreatHall(),
      'secrets': Chamber(),
      'ollivanders': Ollivander(),
      'death': Death()
   }

   def __init__(self, start_scene):
      self.start_scene = start_scene

   def next_scene(self, scene_name):
      return MaraudersMap.scenes.get(scene_name)

   def opening_scene(self):
      return self.next_scene(self.start_scene)

a_map = MaraudersMap('hogwarts')
a_game = Engine(a_map)
a_game.play()
