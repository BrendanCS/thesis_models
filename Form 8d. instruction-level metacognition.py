    


#################################### ∴ FORM 8d. INSTRUCTION-LEVEL METACOGNITION ∴ #####################################

    #   In this example, an COGNITIVE-LEVEL referent is paired with another COGNITIVE-LEVEL referent   


import ccm      
# log=ccm.log(html=True)   

from ccm.lib.actr import *  


class MentalEnvironment(ccm.Model):                                                                 # Mental Environment 
        scientific_method=ccm.Model(isa='scientific_method',location='in_mind',state='unapplied')     


class MotorModule(ccm.Model):

    def science(self):
        print "I will being applying the scientific method..."
        self.parent.parent.scientific_method.state='applied'



class MyDmModule(ccm.ProductionSystem):    
    production_time=0.08                        
                                                   
    def Fire_Off_Knowledge_Chunk(DMbuffer='knowledge:?knowledge'):   # This production fires off the knowledge chunk.
        print " "                                                      # The chunk fires a cognitive action to apply the scientific method.  
        action.science()                                                 # Knowledge with a COGNITIVE REFERENT triggers COGNITIVE-LEVEL productions. 
        focus.set('done')                                            # This triggers the production below "done."     


class MyAgent(ACTR):   

    focus=Buffer()
    action=MotorModule
    DMbuffer=Buffer()                    
    DM=Memory(DMbuffer)  
    knowledge=MyDmModule()              

 
    def init():
        DM.add('knowledge:scientific_method')          
        focus.set('knowledge unknown')      


    def Problem(focus='knowledge unknown'):
        print "(In this example, an COGNITIVE-LEVEL referent (knowledge) is paired with another COGNITIVE-LEVEL referent (sceintific method))"      
        print " "
        print "When desiring knowledge, should I consult my feelings, the supernatural, or the scientific method?"
        print "I'll request knowledge paired with pursuing knowledge....."
        DM.request('knowledge:?')                                           # KNOWLEDGE REQUEST
        focus.set('knowledge request')

    def Request(focus='knowledge request', DMbuffer='knowledge:?knowledge'):    
        print " "    
        print "When pursuing knowledge I should apply..."             
        print knowledge 
        DMbuffer.clear()            
        #  Here there is no "focus.set" - the next production fires off the retrieved knowledge chunk (above) which then triggers the production below. 

    
    def Done(focus='done'):       # this is cued by production above tited "Fires_Off_Knowledge_Chunk" (above) 
        print " "                   
        self.stop()


Julian=MyAgent()
env=MentalEnvironment()
env.agent=Julian
# ccm.log_everything(env)

env.run()
ccm.finished()