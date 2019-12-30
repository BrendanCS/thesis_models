
#########################  FORM 2: CHAIN  #################################


import ccm      
# log=ccm.log(html=True)   

from ccm.lib.actr import *  


class MyEnvironment(ccm.Model):  
        page_1=ccm.Model(isa='page_1',location='in_book',state='unturned')
        page_2=ccm.Model(isa='page_2',location='in_book',state='unturned')            

class MotorModule(ccm.Model):

    def turn1(self):                                                     
        print "I've turned page 1."                                 
        self.parent.parent.page_1.state='turned'

    def turn2(self):                                                     
        print "I've turned page 2."                                 
        self.parent.parent.page_2.state='turned'


class MyAgent(ACTR):    
    focus=Buffer()
    motor=MotorModule
 
    def init():
        focus.set('finished page 1')

    def Production_1(focus='finished page 1'):
        motor.turn1()
        focus.set('finished page 2')

    def Production_2(focus='finished page 2'):
        motor.turn2()
        self.stop()



Julian=MyAgent()
env=MyEnvironment()
env.agent=Julian
# ccm.log_everything(env)

env.run()
ccm.finished()
