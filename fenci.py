import stanza


from jieba import enable_paddle, posseg

import jieba

enable_paddle()
print(posseg.lcut('小基基在南海注册桂城人工智能公司'))
print(posseg.lcut('小基基在南海注册桂城人工智能公司', use_paddle=True))
