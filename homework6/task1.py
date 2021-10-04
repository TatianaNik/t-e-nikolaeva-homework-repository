"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls):
    setattr(cls, "instances", 0)  # set initial value
    old_init = cls.__init__

    def new_init(self):
        old_init(self)
        cls.instances += 1
        # print(self.instances)

    cls.__init__ = new_init

    def get_created_instances(*args):
        # print(cls.instances)
        return cls.instances
    setattr(cls, 'get_created_instances', get_created_instances)

    def reset_instances_counter(cls):
        old_counter = cls.instances
        cls.instances = 0
        return old_counter

    setattr(cls, 'reset_instances_counter', reset_instances_counter)
    return cls


# @instances_counter
# class User:
#     pass


if __name__ == '__main__':

    print(User.get_created_instances())  # 0
    user = User()
    user1 = User()
    user2 = User()
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3

