from django.test import TestCase

from ..factories import LinkFactory


class LinkTest(TestCase):
	def test_fffff(self):
		link = LinkFactory()
		print link
