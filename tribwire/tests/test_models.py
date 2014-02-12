from django.test import TestCase

from ..factories import LinkFactory, WireFactory


class LinkTest(TestCase):
    def test_can_create_link(self):
        link = LinkFactory()
        source = link.source
        self.assertEqual(source.link_set.count(), 1)
        link = LinkFactory(source=source)
        self.assertEqual(source.link_set.count(), 2)
    
    def test_can_add_multiple_wires_to_link(self):
        wire1 = WireFactory()
        wire2 = WireFactory()
        link = LinkFactory(wires=[wire1, wire2])
        # make sure the link can be created
        self.assertTrue(link)