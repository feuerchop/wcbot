# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
Wechat bot main routine

Author: Huang Xiao
Group: Cognitive Security Technologies
Institute: Fraunhofer AISEC
Mail: huang.xiao@aisec.fraunhofer.de
Copyright@2017
'''

import itchat
from itchat.content import *
from pprint import pprint
from argparse import ArgumentParser
import os
import simplejson
from termcolor import colored
import datetime
import pdfkit
import weasyprint
import os
import numpy as np


LOVE_MSG = [
    u"你是我最初也是最后爱的人。",
    u"只要你一直在我身边，其他东西不再重要。",
    u"如果爱上你也算是一种错，我深信这会是生命中最美丽的错，我情愿错一辈子。",
    u"不管将来发生什么事，你变成什么样子，你依然是我最爱的人。",
    u"和你一起总会令我忘记时间存在。",
    u"只要和你一起，我不管要付出怎样大的代价。",
    u"没什么特别的事，只想听听你的声音。",
    u"即使你不爱我，我会一生保护你。",
    u"此刻我很挂念你，请为我小心照顾自己。",
    u"任何时候任何情况，只要你需要我，我立即赶来，尽我全力为你做事。",
    u"你在我心中永远是最有气质最特别和最具吸引力的。",
    u"每一天都为你心跳，每一刻都被你感动，每一秒都为你担心。有你的感觉真好。",
    u"美丽的你，好吗？在世界的一方我为你祝福愿你拥有一个甜蜜的情人。",
    u"请珍惜你拥有的每一个偶然，抓住属于你的每一个瞬间！！我永远属于你！想念你我的爱！",
    u"让我亲手给你沏杯茶，加进一块冰糖，再注入一腔热情，把我的爱恋，一点点地溶进茶中。",
    u"人生的路很长很长，让我陪你一起走吧。我愿与你搭建一个属于我们自己的天空。",
    u"日子在不同的空间流逝，想念在不同的时间来临，不管世事如何的变迁，你永远是我的最爱。",
    u"时间冲不淡真情的酒，距离拉不开思念的手。想你，直到地老天荒，直到永久。",
    u"有情之人，天天是节。一句叮咛，一笺相传；一份相思，一心相盼；一份爱意，一生相恋！",
    u"爱是缘分，爱是感动，爱是习惯，爱是宽容，爱是牺牲，爱是体谅，爱是一辈子的承诺。",
    u"不是因为寂寞才想你，而是因为想你才寂寞。孤独的感觉之所以如此之重，只是因为想得太深。",
    u"与你相识是一种缘，与你相恋是一种美，与你相伴是一种福，我愿和你相伴到永远！",
    u"不愿意醒来时，台灯投射在墙上只有我孤独的身影。",
    u"想你的心情实在没办法用一句话代替。",
    u"总是想念着你，，虽然我们无法同拥有每分每秒。",
    u"好想从现在开始抱着你，紧紧的抱着你，一直走到上帝面前。",
    u"这辈子最疯狂的事，就是爱上了你，最大的希望，就是有你陪我疯一辈子。",
    u"输了你，赢了世界又如何？",
    u"看着微笑的你，突然发现，我真是世界上最幸福的人。",
    u"你可知我百年的孤寂只为你一人守候千夜的恋歌只为你一人而唱。",
    u"白昼与黑夜将无法阻挡我俩的深深思念！",
    u"我是那深深的大海，你是那自海的另一边升起的曙光，永远照亮我的人生。",
    u"你看到的，就是最真的我!!一种永无止尽的感动!!感动这世界有你与我这最美的存在！",
    u"好好照顾自己我不想等到下辈子再来爱你。",
    u"每次我感到失意时，都回忆起你的浅笑，你的鼓励，它们使我坚强的面对下去，谢谢你！",
    u"愿天上的每一个流星，都为你而闪耀天际。",
    u"在认识你之后，我才发现自己可以这样情愿的付出。",
    u"以为没有你，我可以坚强一个人，终于知道我不行。",
    u"你就是我最困难时的那位永远支持我的人！",
    u"将你心再加上我的心，就算痛苦滋味也愿意尝。",
    u"直到遇见了你，我才感受到自己的存在，一直舍不得离开你，虽然你说的如此坚决。",
    u"或许我没有太阳般狂热的爱，也没有流水般绵长的情，只知道不断的爱你爱你无所□能的为你。",
    u"暗恋一个人的心情，就像是瓶中等待发芽的种子，永远不能确定未来是否是美丽的，但却真心而倔强的等待着。",
    u"当你看到这条息时，你已经中了猛烈无比的爱毒，唯一的解药就是嫁给我，不用考虑了，咱们结婚吧！",
    u"妹妹我爱你，见了你我乐呵呵又甜蜜蜜；好想过来抱抱你亲亲你，却又怕你不睬又不理，只好发条短信息。"
    u"爱一个女孩子，与其为了她的幸福而放弃她，不如留住她，为她的幸福而努力。",
    u"如果爱你是一种错误的话，那我情愿错上加错，哪怕错一辈子！",
    u"寂寞是一支烟，思念是一滴泪，迷蒙烟雾中，我看到你俊俏的脸，仿佛像我们初次相见那样动人。",
    u"紧闭的心扉终于被你开启，小小的空间只能容下你，你是我心中的唯一，因为再也容不下第二个人。",
    u"红尘中我们相遇，风雨中我们牵手，浪涛中我们并肩前行，冥冥之中上天自有安排，让我们善待这份情。",
    u"长相思，晓月寒，晚风寒，情人佳节独往还，顾影自凄然。见亦难，思亦难，长夜漫漫抱恨眠，问伊怜不怜。",
    u"开机是为了等你，关机是为了躲你，停机是为了忘记你，号码过期是为了永远忘记！",
    u"不知什么时候开始，我已离不开你。",
    u"从未奢想荣华富贵，能和我爱的人静静走过生命中所有的春夏秋冬，就是我唯一的、最大的奢侈。",
]


def convert2pdf(src_url, output):
    opt = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'image-dpi': "75",
        'load-error-handling': "skip",
        'load-media-error-handling': "skip",
        'disable-external-links': True

        # 'custom-header': [
        #     ('Accept-Encoding', 'gzip')
        # ],
    }

    if not os.path.exists('./tmp/'):
        os.makedirs('./tmp/')
    ret = pdfkit.from_url(src_url, './tmp/' + output, options=opt)
    # print src_url
    # pdf = weasyprint.HTML(src_url).write_pdf()
    # with open('.tmp/' + output, 'w') as fw:
    #     fw.write(pdf)
    return ret


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE])
def simply_print(msg):
    # print 'From: %s' % (msg['FromUserName'])
    # print 'To: %s' % (msg['ToUserName'])
    # print 'Content: %s' % (msg['Text'])
    recv_at = datetime.datetime.fromtimestamp(
        msg.createTime).strftime('%Y-%m-%d %H:%M:%S')
    sender = itchat.search_friends(userName=msg.fromUserName)
    # print sender
    print colored(sender.nickName + ' / ' + sender.remarkName + ' ' + recv_at, 'yellow')
    print msg.content

    if sender.nickName == 'Tong' and sender.starFriend or sender.nickName == u'\u8096\u714c':
        # from Tong
        # itchat.send_msg(msg=u'您的穷垃圾不在线，请耐心等待其变富有.',
        #                 toUserName=msg.fromUserName)
        if msg.content[:4] == 'pdf:':
            # convert rest url to pdf
            my_url = msg.content[4:]
            try:
                stat = convert2pdf(my_url, 'output.pdf')
            finally:
                itchat.send('@fil@./tmp/output.pdf', msg.fromUserName)
            # except IOError:
            #     itchat.send_msg(msg=u'网址转换 PDF 失败.',
            #                     toUserName=msg.fromUserName)
        else:
            itchat.send_msg(u'么么哒[可怜][可怜]', msg.fromUserName)
            itchat.send_msg(LOVE_MSG[np.random.randint(
                0, len(LOVE_MSG))], msg.fromUserName)


# login callback
def login_cb(refresh=True):
    friends_list_path = APP_DATA_PATH + '/friends.json'
    if not os.path.exists(friends_list_path):
        with open(friends_list_path, 'w') as fd:
            friends = itchat.get_friends(update=refresh)
            simplejson.dump(friends, fd)
            print colored('Friends list dumped in {:s}'.format(friends_list_path), 'green')


arg_parser = ArgumentParser(prog='Wcbot!')
arg_parser.add_argument(
    '--app_data_path', default=os.path.expanduser('~') + '/.wcbot')
args = arg_parser.parse_args()
APP_DATA_PATH = args.app_data_path

if not os.path.exists(APP_DATA_PATH):
    os.makedirs(APP_DATA_PATH)
    os.makedirs(APP_DATA_PATH + '/history/')
    os.makedirs(APP_DATA_PATH + '/files/')

itchat.auto_login(
    hotReload=True, statusStorageDir=APP_DATA_PATH + '/itchat.pkl',
    loginCallback=login_cb)

itchat.run(blockThread=True)
