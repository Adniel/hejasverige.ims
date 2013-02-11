from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getMultiAdapter

from Products.CMFCore.utils import getToolByName

from hejasverige.ims.interfaces import IReceivedMessage

class HejaSverigeIMSBarViewlet(ViewletBase):
    template = ViewPageTemplateFile('templates/ims_bar.pt')

    def render(self):
        print 'Will now render the ims_bar.pt template if user is logged in...'
        mship = getToolByName(self.context, 'portal_membership')
        if mship.isAnonymousUser():
            print 'User considered anonymous'
            return ''
        
        return self.template()

    def update(self):
        print "Update before rendering viewlet for the ims_bar.pt"
        mship = getToolByName(self.context, 'portal_membership')
        if mship.isAnonymousUser():
            return
        
        super(HejaSverigeIMSBarViewlet, self).update()

        context_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_context_state')
        tools = getMultiAdapter((self.context, self.request), name=u'plone_tools')

        try: # Plone 4+
            self.ims_actions = context_state.actions(category="hejasverige.ims")
        except TypeError: # Plone 3
            self.ims_actions = context_state.actions().get('hejasverige.ims', ())
        for action in self.ims_actions:
            if action['id'] == 'receivedmessages':
                catalog = getToolByName(self.context, 'portal_catalog')
                portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
                member = portal_state.member()
                action['unread'] = len(catalog(object_provides=IReceivedMessage.__identifier__, 
                                               path={'query': '%s/received' % '/'.join(mship.getHomeFolder(member.getId()).getPhysicalPath())},
                                               read=False))

        plone_utils = getToolByName(self.context, 'plone_utils')
        self.getIconFor = plone_utils.getIconFor