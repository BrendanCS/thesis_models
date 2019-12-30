
############################  FORM 5: PROBLEM SEARCH  ############################

import ccm      
# log=ccm.log(html=True)   

from ccm.lib.actr import *  


class MyEnvironment(ccm.Model):  
        coffee=ccm.Model(isa='coffee',location='in_kitchen',state='unmade',filter='none')
        strainer=ccm.Model(isa='stainer',location='in_drawer',state='unused')
        cheese_cloth=ccm.Model(isa='cheese_cloth',location='in_drawer',state='unused')    

class MotorModule(ccm.Model):

    def strainer(self):                                                     
        print "I used the wire strainer."                                 
        self.parent.parent.strainer.state='used'

    def cheese_cloth(self):                                                     
        print "I used the cheese cloth and instantly regret this decision."                                 
        self.parent.parent.cheese_cloth.state='used'

    def make_coffee(self):                                                                                    
        self.parent.parent.coffee.state='made'



class MyAgent(ACTR):   

    focus=Buffer()
    motor=MotorModule

 
    def init():
        focus.set('begin making coffee')      


    def Production_1(focus='begin making coffee'):
            focus.set('no coffee filters')

    def Problem(focus='no coffee filters'):   
        print "No coffee filters... how do I solve the problem of making coffee?"
        print "Search for solution..."
        focus.set('substitute filter')

  #############  USE STRAINER    

    def Strainer(focus='substitute filter', utility=0.5):    # solution found 
        print "Solution found..."
        motor.strainer()
        focus.set('solution found')


  #############  USE CHEESE CLOTH    

    def Cheese_cloth(focus='substitute filter', utility=0.1): # other possible solution                       
        print "Solution found..."
        motor.cheese_cloth()                                              
        focus.set('solution found')


  #############  COFFEE FINISHED    


    def Finished(focus='solution found'):   
        motor.make_coffee() 
        print "Solved, the coffee is finished."
        self.stop()


Julian=MyAgent()
env=MyEnvironment()
env.agent=Julian
# ccm.log_everything(env)

env.run()
ccm.finished()
