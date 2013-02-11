from Products.CMFCore.utils import getToolByName


def setupHejaSverigeIMS(context):
    print '   Setting up Heja Sverige IMS...'
    if context.readDataFile('hejasverige.ims_various.txt') is None:
        return

    portal = context.getSite()

    membership = getToolByName(portal, 'portal_membership')
    membership.memberareaCreationFlag = True
