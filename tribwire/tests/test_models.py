from django.test import TestCase

from ..factories import LinkFactory


class LinkTest(TestCase):
    def test_can_create_link(self):
        link = LinkFactory()
        source = link.source
        self.assertEqual(source.link_set.count(), 1)
        link = LinkFactory(source=source)
        self.assertEqual(source.link_set.count(), 2)
    