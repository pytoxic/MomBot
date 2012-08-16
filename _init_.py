import sys
import os
from twisted.internet import *
from YourMomDotCom import *
from brain import *

if __name__ == "__main__":
    try:
        chan = '#python-forum'   
    except IndexError:
        print "Please specify a channel name."
        print "Example:"
        print "  python yourmomdotcom.py django-hotclub"
    if os.path.exists('training_text.txt'):
        f = ('training_text.txt', 'r')
        for line in f:
            add_to_brain(line, chain_length)
        print 'Brain Reloaded'
        f.close()
    reactor.connectTCP('irc.freenode.net', 6667, MomBotFactory(chan,
        'YourMomDotCom', 2, chattiness=2.05))
    reactor.run()

