""" Configuration constants
"""

from AccessControl import ModuleSecurityInfo
from Products.CMFCore.permissions import setDefaultRoles

security = ModuleSecurityInfo('hejasverige.ims.config')

PROJECTNAME = "hejasverige.ims"

security.declarePublic('UseSystem')
UseSystem = 'Heja Sverige IMS: Use System'
setDefaultRoles(UseSystem, ('Member',))

security.declarePublic('SendMessage')
SendMessage = 'Heja Sverige IMS: Send Message'
setDefaultRoles(SendMessage, ('Member',))

security.declarePublic('SendMessageToAny')
SendMessageToAny = 'Heja Sverige IMS: Send Message to Any'
setDefaultRoles(SendMessageToAny, ('Manager',))

security.declarePublic('SendMessageToMany')
SendMessageToMany = 'Heja Sverige IMS: Send Message to Many'
setDefaultRoles(SendMessageToMany, ('Manager',))
