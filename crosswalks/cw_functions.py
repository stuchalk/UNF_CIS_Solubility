from crosswalks.models import *


def getcwks():
    """get a list of contexts"""
    cwks = Crosswalks.objects.using('sciflow').all().order_by('field')
    return cwks


def getcwk(ctxid):
    """get a list of contexts"""
    cwk = Crosswalks.objects.using('sciflow').get(id=ctxid)
    return cwk


def getnsps():
    """get a list of namespaces"""
    spaces = Nspaces.objects.using('sciflow').all()
    return spaces


def getnsp(nsid):
    """get the data about a namespace"""
    space = Nspaces.objects.using('sciflow').get(id=nsid)
    return space


def getonts():
    """get the data for an ont term"""
    term = Ontterms.objects.using('sciflow').all()
    return term


def getont(otid):
    """get the data for an ont term"""
    term = Ontterms.objects.using('sciflow').get(id=otid)
    return term


def onttermsbyns(nsid):
    """get the ont terms using a namespace"""
    terms = Ontterms.objects.using('sciflow').all().filter(nspace_id=nsid)
    return terms
