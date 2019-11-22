#################### ham cheese production model ###################

# THINGS TO INCORPORATE: 
#   DM memory of memories to wander to.
#   Vision to spot calendar.
#   Vision of calendar must provoke memory friend's birthday.   
#   If completed not completed 10 breath continue where left off.



import ccm      
# log=ccm.log(html=True)   

from ccm.lib.actr import *  


class MyEnvironment(ccm.Model):
    pass



class MyAgent(ACTR):   

    focus=Buffer()



#### NOTE - this model uses an alternative way of writing chunks using a list instead of a dictionary form
#### so the order is what gives it meaning. This is just an alternative way of writing them, they work just the same

 
    def init():
        focus.set('find food')
        # 'find food' matches both the apple and marshmallow condition



    def Apple_Production_1(focus='find food'):          # apple competes with marshmallow: 'find food' below
        print "I've found the apple"
        focus.set('lift apple')

    def Apple_Production_2(focus='lift apple'):
        print "I've lifted the apple" 
        focus.set('eat apple')   

    def Apple_Production_3(focus='eat apple'):
        print "I've eaten the apple."
        self.stop()


    def Mashmallow_Production_1(focus='find food', utility=0.3):   # utility is higher than apple above
        print "I've found the marshmallow."                        # this production is chosen
        focus.set('lift marshmallow')

    def Mashmallow_Production_2(focus='lift marshmallow'):
        print "I've lifted the marshmallow" 
        focus.set('eat mashmallow')


    def Mashmallow_Production_3(focus='eat mashmallow'):
        print "I've eaten the mashmallow"
        self.stop()



Sid=MyAgent()
env=MyEnvironment()
env.agent=Sid
# ccm.log_everything(env)

env.run()
ccm.finished()
