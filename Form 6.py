#################### MEDITATING MIND WANDERING production model ###################


import ccm      
log=ccm.log(html=True)   

from ccm.lib.actr import *  


# The environment contains "lung objects" that a MotorModule makes breath in and out. 
# The Agent pays attention to lungs for five breaths. 
# During the five breaths, the Agent's mind wanders randomly to different memories in visual memory.  
# When the agent's mind wanders, the "MetacognitiveModule" prints "PAY ATTENTION !" and the agent returns to the breath. 

# THIS MODEL CONTAINS: 
# Environment - contains "lungs" object
# MotorModule - makes "lungs" inflate and deflate
# MyAgent - pays attention to lunds expand and contract 
# MyDmModule  - makes Agent's focus wander randomly to visual memories
# MetacognitiveModule  - fires when focus wanders 
# Code by Brendan Conway-Smith March 2019



class The_Environment(ccm.Model):       
    lungs=ccm.Model(isa='lungs',state='empty')	#lungs with state of being empty		

  

class MotorModule(ccm.Model):      

    def breath_in(self):            
        # yield 0                     
        print "*Lungs inflate*"    
        self.parent.parent.lungs.state='full'       # changes lungs state from empty to full
 
    def breath_out(self):           
        # yield 0                      
        print "*Lungs deflate*"    
        self.parent.parent.lungs.state='empty'      # changes lungs state from full to empty



class MyDmModule(ccm.ProductionSystem):    
    production_time=0.08							#changine this number changes how often it fires
    												#change it to see
    def Wander(VM='busy:False'):
        VM.request('wander:?wander')				#if there Agent is doing a VM request with wander:?wander   
        print " "									#then this will fire
        print "Mind wandering"  

    def Wander_retrieve(VMbuffer='wander:?wander'):
        print " "									
        print "Mind wanders to..."
        print wander     							#this chooses a random VM.add memory and prints it


# class MetaModule(ccm.ProductionSystem):  
#     production_time=0.09							#changine this number changes how often it fires
#     												#change it to see
#     def refocus_on_breath(VMbuffer='wander:?wander'):  
#         print " "
#         print "PAY ATTENTION !"						#this notices that there is a VM mind wander request
#         											#and reminds the agent to pay attention 


class MyAgent(ACTR):    
    focus=Buffer()
    motor=MotorModule()

    DMbuffer=Buffer()                                    
    DM=Memory(DMbuffer)

    Wandering=MyDmModule()

    VMbuffer=Buffer()                             
    VM=Memory(VMbuffer)     

    # Meta_Awareness=MetaModule()     
    


    def init():
        VM.add('wander:~WEEKEND_PLANS~')
        VM.add('wander:~LAST_VACATION~')
        VM.add('wander:~EPISODE_OF_THE_SIMPSONS~')
        VM.add('wander:~WEATHER_REPORT~')
        VM.add('wander:~CHILDHOOD_FRIEND~')
        VM.add('wander:~EMBARASSING_THING~')
        VM.add('wander:~THAT_PERSONS_NAME~')
        VM.add('wander:~SONG_MEMORY~')
        focus.set('buffer 1')

    def breath_1(focus='buffer 1'):
        print " "
        motor.breath_in()
        motor.breath_out()
        print "I'm aware of breath ONE" 
        focus.set('buffer 2')

    def breath_2(focus='buffer 2'):
        print " "
        motor.breath_in()
        motor.breath_out()  
        print "I'm aware of breath TWO"     
        focus.set('buffer 3') 

    def breath_3(focus='buffer 3'):
        print " "
        motor.breath_in()
        motor.breath_out()
        print "I'm aware of breath THREE"  
        focus.set('buffer 4') 

    def breath_4(focus='buffer 4'):
        print " "
        motor.breath_in()
        motor.breath_out() 
        print "I'm aware of breath FOUR"    
        focus.set('buffer 5') 

    def breath_5(focus='buffer 5'):
        print " "
        motor.breath_in()
        motor.breath_out()
        print "I'm aware of breath FIVE"         
        focus.set('stop') 

    def stop_production(focus='stop'):
        print " "
        print "FINISHED - I have counted five breaths."
        self.stop()


Sid=MyAgent()
env=The_Environment()
env.agent=Sid

#ccm.log_everything(env)    #keeps the log details off the print page

env.run()
ccm.finished()
