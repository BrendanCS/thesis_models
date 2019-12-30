

####################################  FORM 8b: OBJECT-LEVEL METACOGNITION  #####################################

    #   In this example, an OBJECT-LEVEL referent (coffee) is paired with a COGNITIVE-LEVEL referent (alertness) 


import ccm      
# log=ccm.log(html=True)   

from ccm.lib.actr import *  


class MyEnvironment(ccm.Model):  
        coffee=ccm.Model(isa='coffee',location='on_table',state='full')     


class MotorModule(ccm.Model):

    def DrinkCoffee(self):
        print "I drink the coffee ..."
        self.parent.parent.coffee.state='drank'



class MyDmModule(ccm.ProductionSystem):    
    production_time=0.08                        
                                                   
    def Fire_Off_Knowledge_Chunk(DMbuffer='coffee:?coffee'):   # this production fires off declarative knowledge chunk
        print " "                                                # the chunk fires the motor to drink the coffee 
        motor.DrinkCoffee()                                        # OBJECT-LEVEL knowledge triggers OBJECT-LEVEL productions 
        focus.set('done')                                       # triggers the production below "done"     


class MyAgent(ACTR):   

    focus=Buffer()
    motor=MotorModule
    DMbuffer=Buffer()                    
    DM=Memory(DMbuffer)  
    knowledge=MyDmModule()              

 
    def init():
        DM.add('coffee:alertness')          
        focus.set('served coffee')      


    def Problem(focus='served coffee'): 
        print "(In this example, an OBJECT-LEVEL referent (coffee) is paired with a COGNITIVE-LEVEL referent (alertness))"  
        print " "
        print "I'm being served coffee, should I drink it?"
        print "I'll search for knowledge about coffee ..."
        DM.request('coffee:?')                                           # KNOWLEDGE REQUEST
        focus.set('knowledge request')

    def Request(focus='knowledge request', DMbuffer='coffee:?coffee'):    
        print " "    
        print "Coffee creates the cognitive property of ..."             
        print coffee 
        DMbuffer.clear()            
        # here there is no "focus.set" - the next production fires off the retrieved knowledge chunk (above) which then triggers the production below. 

    
    def Done(focus='done'):       # this is cued by production above tited "Fires_Off_Knowledge_Chunk" (above) 
        print " "                   
        self.stop()


Julian=MyAgent()
env=MyEnvironment()
env.agent=Julian
# ccm.log_everything(env)

env.run()
ccm.finished()
