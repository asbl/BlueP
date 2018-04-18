import sys


class Test():
    """ New class Test"""

    global_message = "Hello world !"

    def __init__(self):
        self.default_message = "Hello everybody !"

    def print_value(self, sender):
        """DocString : this method print the default value of this instance"""
        print(sender + " say : " + self.default_message)

    def print_global_message():
        print(Test.global_message)

    def main():
        Test.print_global_message()
        test = Test()
        test.print_value("test")

if __name__ == '__main__':
        Test.main()
