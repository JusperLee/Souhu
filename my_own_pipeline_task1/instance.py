###
# Author: Kai Li
# Date: 2022-04-14 11:42:46
# Email: lk21@mails.tsinghua.edu.cn
# LastEditTime: 2022-04-14 11:42:47
###
###
# Author: Kai Li
# Date: 2022-04-12 14:48:25
# Email: lk21@mails.tsinghua.edu.cn
# LastEditTime: 2022-04-12 15:03:48
###

class ATSAInstance(object):
    polarity2index={0:0,1:1,2:2,3:3,4:4,5:5}
    sentence=None
    word_tokens = None
    bert_tokens = None
    aspect_term=None
    aspect_from=None
    aspect_to=None
    aspect_from_pos=None
    aspect_bert_tokens=None
    polarity=None



class ACSAInstance(object):
    polarity2index={'positive':0,'negative':1,'neutral':2}
    category2index={'food':0,'service':1,'staff':2,'price':3, 'ambience':4,'menu':5,'place':6, 'miscellaneous':7}
    index2category=dict(zip(category2index.values(),category2index.keys()))

    sentence=None
    word_tokens=None
    bert_tokens=None
    category=None
    polarity=None