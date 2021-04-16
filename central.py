from response import *
from dictionary import *

class Central:
    def __init__(self,name): #name?
        self.name = name
        self.dictionary = Dictionary()
        self.res_random = Random(self.dictionary)　#質問１、self.dictionary = Dictionary()で生成したself.dictionaryはですが、なぜRandomクラスの引数にいれるだけで辞書を起動出来るのか？
        self.res_repeat = Repeat(self.dictionary)

    def output(self,input):
        x = random.randint(0,10)
        if x <= 6:
            self.responder = self.res_random
        else:
            self.responder = self.res_repeat
        return self.responder.response(input)
a = Central("central")
while True:
    var = input('Enter:')
    b = a.output(var)
    if not var:
        break
    print(b)
