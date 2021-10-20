from homework6.task1 import instances_counter

@instances_counter
class User:
    pass

def test_check_number_of_created_instances_at_the_start():
   assert(User.get_created_instances() == 0)


def test_check_number_of_created_instances_one_object():
    User.reset_instances_counter(User)
    user = User()
    assert(user.get_created_instances() == 1)


def test_check_number_of_created_instances_three_objects():
    User.reset_instances_counter(User)
    User()
    user1 = User()
    user2 = User()
    assert (User.get_created_instances() == 3)


def test_reset_instances_returns_previous_instances_number():
    assert(User.reset_instances_counter(User) == 3)