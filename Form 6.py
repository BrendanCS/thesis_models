
############################  FORM 6: KNOWLEDGE SEARCH  ############################

import ccm      
# log=ccm.log(html=True)   

from ccm.lib.actr import *  


class MyEnvironment(ccm.Model):  
        pass

class SearchModule(ccm.Model):

    def alternatives(self):                                                     
        print "Search around for other methods of straining the coffee." 




class MyDmModule(ccm.ProductionSystem):    
    production_time=0.25                        
                                                   
    def SearchAlternatives(DMbuffer='no_filter:?no_filter'):   # this production fires off the knowledge search                                                             # the chunk fires the motor to use the substitute strainer 
        searching.alternatives()
        DMbuffer.clear()
        focus.set('search around')      # this triggers the production below titled "SearchAround"     



class MyAgent(ACTR):   

    focus=Buffer()
    searching=SearchModule
    DMbuffer=Buffer()                    
    DM=Memory(DMbuffer)  
    remember=MyDmModule()              

 
    def init():
        DM.add('no_filter:search_alternatives')      
        focus.set('begin making coffee')      


    def Production_1(focus='begin making coffee'):
        focus.set('no coffee filters')

    def Problem(focus='no coffee filters'):   
        print "No coffee filters ... what should I do?"
        DM.request('no_filter:?')                                     
        focus.set('next')

    def Remember(focus='next', DMbuffer='no_filter:?no_filter'):    
        print " "    
        print "To help resolve this problem I should ..."             
        print no_filter
        DMbuffer.clear()             
        # here there is no "focus.set" - the next production is guided by the knowledge search which then triggers the production below. 

    

    def SearchAround(focus='search around'): 
        print " "                         
        print "I will search for alternatives."
        focus.set('search')

    def Searching1(focus='search'):
        print "Looking in drawer ..."
        focus.set('search more')

    def Searching2(focus='search more'):
        print "Looking on shelves ..."
        self.stop()


Julian=MyAgent()
env=MyEnvironment()
env.agent=Julian
# ccm.log_everything(env)

env.run()
ccm.finished()
