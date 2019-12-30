
############################  FORM 3: COMPETING  ############################

import ccm      
# log=ccm.log(html=True)   

from ccm.lib.actr import *  


class MyEnvironment(ccm.Model):  
        page_1=ccm.Model(isa='page_1',location='in_book',state='unturned')
        page_2=ccm.Model(isa='page_2',location='in_book',state='unturned')    
        page_3=ccm.Model(isa='page_3',location='in_book',state='unturned')  
        coffee=ccm.Model(isa='coffee',location='in_kitchen',state='unbrewed')  

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

    def make_coffee(self):                                                     
        print "I made coffee."                                 
        self.parent.parent.coffee.state='brewed'



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

    def Coffee(focus='competing production', utility=0.3):      # this produciton has a higher utility
        print "Don't turn to page 3, instead make coffee."                          
        motor.make_coffee()                                              
        self.stop()



Julian=MyAgent()
env=MyEnvironment()
env.agent=Julian
# ccm.log_everything(env)

env.run()
ccm.finished()
