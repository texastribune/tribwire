import factory
from django.contrib.auth import get_user_model


class UserFactory(factory.DjangoModelFactory):
    """ This only supports the real factories """
    FACTORY_FOR = get_user_model()
    first_name = factory.Sequence(lambda n: 'first name {0}'.format(n))
    last_name = factory.Sequence(lambda n: 'last name {0}'.format(n))
    username = factory.Sequence(lambda n: 'user{0}'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'test_pass')
