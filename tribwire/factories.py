import factory
from django.contrib.auth import get_user_model
from django.utils import timezone

from . import models


class UserFactory(factory.DjangoModelFactory):
    """ This only supports the real factories """
    FACTORY_FOR = get_user_model()
    first_name = factory.Sequence(lambda n: 'first name {0}'.format(n))
    last_name = factory.Sequence(lambda n: 'last name {0}'.format(n))
    username = factory.Sequence(lambda n: 'user{0}'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'test_pass')


class SourceFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Source


class WireFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Wire


class LinkFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.Link
    date_suggested = factory.LazyAttribute(lambda __: timezone.now())
    user = factory.SubFactory(UserFactory)
    source = factory.SubFactory(SourceFactory)
    wire = factory.SubFactory(WireFactory)
