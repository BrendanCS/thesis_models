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
 
    def init():
        focus.set('find marshmallow')

    def Mashmallow_Production_1(focus='find marshmallow'):
        print "I've found the marshmallow bag"
        focus.set('open marshmallow bag')

    def Mashmallow_Production_2(focus='open marshmallow bag'):
        print "I've opened the mashmallow bag" 
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
