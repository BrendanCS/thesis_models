

import ccm      
log=ccm.log(html=True)   

from ccm.lib.actr import *  

#if noetic feeling is that understanding is POOR then agent will re-read paragraph 1
# if noetic feeling is that understanding is GOOD, the agent will read paragraph 2,3,4

class MyEnvironment(ccm.Model):  
    	sentence_1=ccm.Model(isa='sentence_1',location='on_page',state='unread')		
    	sentence_2=ccm.Model(isa='sentence_2',location='on_page',state='unread')
        sentence_3=ccm.Model(isa='sentence_3',location='on_page',state='unread')
        sentence_4=ccm.Model(isa='sentence_4',location='on_page',state='unread')

class MotorModule(ccm.Model):

    def read1(self):                                                     
        print " " 
        print "Reading FIRST sentence."
        # DM.request                                # should the MM trigger a noetic assessment?         
        self.parent.parent.sentence_1.state='read'

    def read2(self):                                                             
        print " " 
        print "Reading SECOND sentence..."   
        self.parent.parent.sentence_2.state='read'

    def read3(self):                                                         
        print " " 
        print "Reading THIRD sentence..."       
        self.parent.parent.sentence_3.state='read'

    def read4(self):                                                        
        print " " 
        print "Reading FOURTH sentence..."  
        self.parent.parent.sentence_4.state='read'

class MyAgent(ACTR):
    
    focus=Buffer()

    Nbuffer=Buffer()          # NOETIC MEMORY                           
    N=Memory(Nbuffer)
    MM=MotorModule()

    VMbuffer=Buffer()                                   
    VM=Memory(VMbuffer)     


    def init():
        N.add('understanding:poor')               
        N.add('understanding:good')                  
        focus.set('buffer_1')

    def Read_One(focus='buffer_1'):					   
        MM.read1()                                  # 1st READ
        N.request('understanding:?')              
        focus.set('buffer_2')  

    def Read_Again(focus='buffer_1b'):
    	print "Read again..."
        print " "
        MM.read1()                                  # READING AGAIN
        N.request('understanding:?')              
        focus.set('buffer_2')  
 
    def POOR(focus='buffer_2', Nbuffer='understanding:poor'):						    # if poor go back
        Nbuffer.clear()
        print " "
    	print "   NOETIC feeling? My understanding POOR."
        print " "
        focus.set('buffer_1b')       

    def GOOD(focus='buffer_2', Nbuffer='understanding:good'):
        Nbuffer.clear()
        print " " 
    	print "   NOETIC feeling? My understanding is GOOD."
        focus.set('buffer_3')     
 
    def PARAGRAPH_2(focus='buffer_3'):
        MM.read2()
        focus.set('buffer_4') 

    def PARAGRAPH_3(focus='buffer_4'):
        MM.read3()
        focus.set('buffer_5') 

    def PARAGRAPH_4(focus='buffer_5'):
        MM.read4()
        focus.set('stop')     

    def stop_production(focus='stop'):
        print " "
        print ""
        self.stop()                        # stop the agent

tim=MyAgent()                              # name the agent
home=MyEnvironment()                       # name the environment
home.agent=tim                             # put the agent in the environment
# ccm.log_everything(home)                 # print out what happens in the environment

home.run()                                 # run the environment
ccm.finished()                             # stop the environment
