"""Message folders (received, sent)
"""

from zope.interface import implements
from zope.i18n import translate

from Products.CMFCore.permissions import ModifyPortalContent, DeleteObjects

from Products.Archetypes.public import *

from Products.ATContentTypes.content.base import ATCTMixin

from hejasverige.ims.config import PROJECTNAME
from hejasverige.ims.interfaces import IMessageFolder, IReceivedMessageFolder, ISentMessageFolder
from hejasverige.ims import IMSMessageFactory as _

MessageFolderSchema = BaseFolderMixin.schema.copy()
MessageFolderSchema.delField('title')

class BaseMessageFolder(BaseFolderMixin, ATCTMixin):
    """ A folder holding messages
    """
    implements(IMessageFolder)

    _at_rename_after_creation = False
    schema = BaseFolderMixin.schema.copy()
    
class ReceivedMessageFolder(BaseMessageFolder):
    """ The folder holding received messages
    """
    implements(IReceivedMessageFolder)
    
    portal_type = meta_type = "ReceivedMessageFolder"
    
    def Title(self):
        try:
            return translate(_('title_receivedmessagefolder', default=u'Mottagna Meddelanden'), context=self.REQUEST)
        except:
            return u'Mottagna Meddelanden'
    
class SentMessageFolder(BaseMessageFolder):
    """ The folder holding sent messages
    """
    implements(ISentMessageFolder)
    
    portal_type = meta_type = "SentMessageFolder"
    
    def Title(self):
        try:
            return translate(_('title_sentmessagefolder', default=u'Skickade Meddelanden'), context=self.REQUEST)
        except:
            return u'Skickade Meddelanden'
    
registerType(ReceivedMessageFolder, PROJECTNAME)
registerType(SentMessageFolder, PROJECTNAME)
    