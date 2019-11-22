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
        focus.set('read book')

    def Reading_Production_1(focus='read book'):
        print "I'm reading chapter 1" 
        focus.set('read chapter 2')   



    def Reading_Production_2(focus='read chapter 2', utility=0.1):   # competes with 'read chapter 2' below
        print "I'm reading chapter 2"                                # this chain is INTERUPTED by higher utilty production below
        focus.set('read chapter 3')  

    def Reading_Production_3(focus='read chapter 3'):
        print "I'm reading chapter 3, all done!" 
        self.stop() 



    def Fire_Alarm_1(focus='read chapter 2', utility=0.2):          # competes with 'read chapter 2' above
        print "I hear the FIRE ALARM!"                              # fire alarm HAS GREATER UTILITY than competing production above
        focus.set('Leave the building')                             # this production is chosen

    def Fire_Alarm_2(focus='Leave the building'):
        print "I've left the building"
        self.stop()



Sid=MyAgent()
env=MyEnvironment()
env.agent=Sid
# ccm.log_everything(env)

env.run()
ccm.finished()
