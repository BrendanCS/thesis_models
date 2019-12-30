
############################  FORM 7: KNOWLEDGE REQUEST  ############################

import ccm      
# log=ccm.log(html=True)   

from ccm.lib.actr import *  


class MyEnvironment(ccm.Model):  
        coffee=ccm.Model(isa='coffee',location='in_kitchen',state='unmade',filter='none')
        strainer=ccm.Model(isa='stainer',location='in_drawer',state='unused')

class MotorModule(ccm.Model):

    def strainer(self):                                                     
        print "I'm using the wire strainer."                                 
        self.parent.parent.strainer.state='used'


    def finish_coffee(self): 
        print "I'm finishing the coffee ..."                                                                                   
        self.parent.parent.coffee.state='made'


class MyDmModule(ccm.ProductionSystem):    
    production_time=0.08                        
                                                   
    def Fire_Off_Knowledge_Chunk(DMbuffer='substitute_filter:?substitute_filter'):   # this production fires off declarative knowledge chunk
        print " "                                                                    # the chunk fires the motor to use the substitute strainer 
        motor.strainer()
        focus.set('strainer used')      # this triggers the production below titled "Finished"     


class MyAgent(ACTR):   

    focus=Buffer()
    motor=MotorModule
    DMbuffer=Buffer()                    
    DM=Memory(DMbuffer)  
    remember=MyDmModule()              

 
    def init():
        DM.add('substitute_filter:strainer')          
        focus.set('begin making coffee')      


    def Production_1(focus='begin making coffee'):
        focus.set('no coffee filters')

    def Problem(focus='no coffee filters'):   
        print "No coffee filters ... what is the best subsitute filter?"
        print "I'm search for knowledge  ..."
        DM.request('substitute_filter:?')                                           # KNOWLEDGE REQUEST
        focus.set('next')

    def Remember(focus='next', DMbuffer='substitute_filter:?substitute_filter'):    
        print " "    
        print "I recall a good substitute filter is a ..."             
        print substitute_filter             
        # here there is no "focus.set" - the next production fires off the retrieved knowledge chunk (above) which then triggers the production below. 

    

    def Finished(focus='strainer used'):  # this is cued by production above tited "Fires_Off_Knowledge_Chunk" (above) 
        print " "                         # this demonstrates how knowledge serves as a buffer condition that triggers the next productions 
        motor.finish_coffee()
        print "The coffee is finished."
        self.stop()


Julian=MyAgent()
env=MyEnvironment()
env.agent=Julian
# ccm.log_everything(env)

env.run()
ccm.finished()
