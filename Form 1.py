
############################  FORM 1: SINGLE  ############################


import ccm      
# log=ccm.log(html=True)   

from ccm.lib.actr import *  


class MyEnvironment(ccm.Model):  
    	page_1=ccm.Model(isa='page_1',location='in_book',state='unturned')		

class MotorModule(ccm.Model):

    def turn1(self):                                                     
        print "I've turned a single page."                                 
        self.parent.parent.page_1.state='turned'

class MyAgent(ACTR):    
    focus=Buffer()
    motor=MotorModule()
 
    def init():
        focus.set('single production')

    def Single_Production(focus='single production'):
        motor.turn1()
        self.stop()



Julian=MyAgent()
env=MyEnvironment()
env.agent=Julian
# ccm.log_everything(env)

env.run()
ccm.finished()
