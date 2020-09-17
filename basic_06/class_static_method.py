class Animal:
    instance_account = 0

    def __init__(self):
        Animal.instance_account += 1

    def __del__(self):
        print("Deleted instance.")
        Animal.instance_account -= 1

    @classmethod
    def show_account(cls):
        print("Instance account %d " % cls.instance_account)

    @staticmethod
    def print_account():
        print("Instance account %d " % Animal.instance_account)


a1 = Animal()
a1.show_account()
Animal.show_account()
Animal.print_account()
