#http://search.maven.org/remotecontent?filepath=org/python/jython-standalone/2.7-b1/jython-standalone-2.7-b1.jar
from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator
import time




class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory):
  def registerExtenderCallbacks(self, callbacks):
    self._callbacks = callbacks
    self._helpers = callbacks.getHelpers()
    callbacks.registerIntruderPayloadGeneratorFactory(self)
    return

  def getGeneratorName(self):
    return "Current Epoch Time"

  def createNewInstance(self, attack): 
    return EpochTime(self, attack)

class EpochTime(IIntruderPayloadGenerator):
  def __init__(self, extender, attack):
    self._extender = extender
    self._helpers  = extender._helpers
    self._attack   = attack
    return

  def hasMorePayloads(self):
    return True

  def getNextPayload(self,current_payload):
    payload = str(int(time.time()))
    return payload
	
  def reset(self):
    return   
