


####################################  FORM 8c. MONITOR-LEVEL METACOGNITION  #####################################

    #   In this example, an COGNITIVE-LEVEL referent (tiredness) is paired with an OBJECT-LEVEL referent (bed)   


import ccm      
# log=ccm.log(html=True)   

from ccm.lib.actr import *  


class MyEnvironment(ccm.Model):  
        bed=ccm.Model(isa='bed',location='in_bedroom',state='empty')     


class MotorModule(ccm.Model):

    def Lie_in_bed(self):
        print "I've gone to my bed."
        self.parent.parent.bed.state='full'



class MyDmModule(ccm.ProductionSystem):    
    production_time=0.08                        
                                                   
    def Fire_Off_Knowledge_Chunk(DMbuffer='tired:?tired'):   # This production fires off the knowledge chunk.
        print " "                                                # The chunk fires the motor to go to bed.  
        motor.Lie_in_bed()                                        # Knowledge with a COGNITIVE REFERENT triggers OBJECT-LEVEL productions. 
        focus.set('done')                                      # This triggers the production below "done."     


class MyAgent(ACTR):   

    focus=Buffer()
    motor=MotorModule
    DMbuffer=Buffer()                    
    DM=Memory(DMbuffer)  
    knowledge=MyDmModule()              

 
    def init():
        DM.add('tired:bed')          
        focus.set('sleepy')      


    def Problem(focus='sleepy'):
        print "(In this example, an COGNITIVE-LEVEL referent (tiredness) is paired with an OBJECT-LEVEL referent (bed))"      
        print " "
        print "I feel tired, what should I do?"
        print "I'll request knowledge paired with the memory of being tired."
        DM.request('tired:?')                                           # KNOWLEDGE REQUEST
        focus.set('knowledge request')

    def Request(focus='knowledge request', DMbuffer='tired:?tired'):    
        print " "    
        print "When tired I should move toward..."             
        print tired 
        DMbuffer.clear()            
        #  Here there is no "focus.set" - the next production fires off the retrieved knowledge chunk (above) which then triggers the production below. 

    
    def Done(focus='done'):       # this is cued by production above tited "Fires_Off_Knowledge_Chunk" (above) 
        print " "                   
        self.stop()


Julian=MyAgent()
env=MyEnvironment()
env.agent=Julian
# ccm.log_everything(env)

env.run()
ccm.finished()
