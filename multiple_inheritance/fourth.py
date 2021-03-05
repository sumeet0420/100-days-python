from multiple_inheritance.first import First
from multiple_inheritance.second import Second
from multiple_inheritance.third import Third


class Fourth( First,Second, Third):

    def __init__(self):
        super().__init__()
        super(First, self).__init__()
        super(Second, self).__init__()
        print("Fourth")


fourth = Fourth()
