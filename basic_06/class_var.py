class Animal:
    instance_account = 0

    def __init__(self):
        Animal.instance_account += 1

    def __del__(self):
        print("Deleted instance.")
        Animal.instance_account -= 1

    def show_account(self):
        print("Instance account %d " % Animal.instance_account)


a1 = Animal()
Animal()
a3 = Animal()
a1.show_account()
print("Account: %d" % Animal.instance_account)
