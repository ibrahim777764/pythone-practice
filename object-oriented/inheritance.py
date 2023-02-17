
# what's so special about a method ,methods become special when we access and modify the 
# instance variables inside of the class !

from email.mime import image
from random import random
import random
from unicodedata import name

class pcb :
    def __init__(self):
        print("i will start pcl very soon")

class psl(pcb):

    def __init__(self,name):
        super().__init__()
        print("ranking of teams in psl 2023")
        self.ranking = random.randint(1,6)
        self.name = name

    def trophy(self):
     print(f"finally {self.name} won psl 2023 edtion")


kk =psl("karachi kings")
pz =psl("peshawar zalmi")
qg =psl("quetta galaddiotors ")
lq =psl("lahore qalanders")
ms =psl("multan sultan")
iu =psl("islamabad united")

kk.trophy()
pz.trophy()
lq.trophy()
qg.trophy()
ms.trophy()
iu.trophy()


print(kk.ranking)
print(pz.ranking)
print(qg.ranking)
print(lq.ranking)
print(ms.ranking)
print(iu.ranking)
