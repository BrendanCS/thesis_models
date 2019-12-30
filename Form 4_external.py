
######################  FORM 4: INTERUPT - EXTERNAL  #######################

import ccm      
# log=ccm.log(html=True)   

from ccm.lib.actr import *  


class MyEnvironment(ccm.Model):  
        page_1=ccm.Model(isa='page_1',location='in_book',state='unturned')
        page_2=ccm.Model(isa='page_2',location='in_book',state='unturned')    
        page_3=ccm.Model(isa='page_3',location='in_book',state='unturned')  
        building=ccm.Model(isa='building',location='Ottawa',relation='in')  

class MotorModule(ccm.Model):

    def turn1(self):                                                     
        print "I've turned page 1."                                 
        self.parent.parent.page_1.state='turned'

    def turn2(self):                                                     
        print "I've turned page 2."                                 
        self.parent.parent.page_2.state='turned'

    def turn3(self):                                                     
        print "I've turned page 3."                                 
        self.parent.parent.page_3.state='turned'

    def run(self):                                                     
        print "I ran from the building."                                 
        self.parent.parent.building.relation='out'



class MyAgent(ACTR):   

    focus=Buffer()
    motor=MotorModule

 
    def init():
        focus.set('finished page 1')      

  #############  TURN PAGES    

    def Production_1(focus='finished page 1'):
        motor.turn1()
        focus.set('finished page 2')

    def Production_2(focus='finished page 2'):   
        motor.turn2()
        focus.set('competing production')

    def Production_3(focus='competing production', utility=0.2):    # lower utility 
        motor.turn3()
        self.stop()

  #############  FIRE ALARM

    def FireAlarm(focus='competing production', utility=0.3):      # this production has a higher utility
        print "I hear the fire alarm!"                          
        motor.run()                                              
        self.stop()



Julian=MyAgent()
env=MyEnvironment()
env.agent=Julian
# ccm.log_everything(env)

env.run()
ccm.finished()
