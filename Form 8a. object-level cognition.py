
############################  FORM 8a. OBJECT-LEVEL COGNITION  ############################
# In this example, OBJECT-LEVEL knowledge triggers OBJECT-LEVEL productions.
# Knowledge applies two external objects in performing an object-level cognitive task.  

import ccm      
# log=ccm.log(html=True)   

from ccm.lib.actr import *  


class MyEnvironment(ccm.Model):  
        hammer=ccm.Model(isa='hammer',location='in_hand',state='still')     
        nail=ccm.Model(isa='nail',location='in_wall',state='protruding')

class MotorModule(ccm.Model):

    def SwingHammer(self):
        print "I hammer the nail..."
        self.parent.parent.hammer.state='swung'
        print "The hammer object strikes the nail object."
        self.parent.parent.nail.state='inserted'



class MyDmModule(ccm.ProductionSystem):    
    production_time=0.08                        
                                                   
    def Fires_Off_Knowledge_Chunk(DMbuffer='nail:?nail'):  # this production fires off declarative knowledge chunk
        print " "                                          # the chunk fires the motor to swing the hammer  
        motor.SwingHammer()                                # OBJECT-LEVEL knowledge triggers OBJECT-LEVEL productions 
        focus.set('done')                                  # triggers the production below "done"     


class MyAgent(ACTR):   

    focus=Buffer()
    motor=MotorModule
    DMbuffer=Buffer()                    
    DM=Memory(DMbuffer)  
    knowledge=MyDmModule()              

 
    def init():
        DM.add('nail:hammer')          
        focus.set('nail protruding')      


    def Problem(focus='nail protruding'):
        print "(In this example, OBJECT-LEVEL knowledge triggers OBJECT-LEVEL productions)"   
        print " "
        print "A nail (OBJECT) is protruding, what should I do?"
        print "I'm search for knowledge..."
        DM.request('nail:?')                                           # KNOWLEDGE REQUEST
        focus.set('knowledge request')

    def Request(focus='knowledge request', DMbuffer='nail:?nail'):    
        print " "    
        print "The nail knowledge request says..."             
        print nail 
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
