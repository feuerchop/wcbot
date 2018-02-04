#!/usr/bin/env python

'''
Test Itchat functionalities

Author: Huang Xiao
Group: Cognitive Security Technologies
Institute: Fraunhofer AISEC
Mail: huang.xiao@aisec.fraunhofer.de
Copyright@2017
'''

import itchat
from itchat.content import *
from pprint import pprint


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def simply_print(msg):
    print 'From: %s' % (msg['FromUserName'])
    print 'To: %s' % (msg['ToUserName'])
    print 'Content: %s' % (msg['Text'])


itchat.auto_login(hotReload=True)
itchat.run(blockThread=True)
