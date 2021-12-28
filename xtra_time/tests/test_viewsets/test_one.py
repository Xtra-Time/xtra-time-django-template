from django.test import TestCase

class PostTestCase(TestCase):
    def setUp(self):
        pass
    def test_is_running(self):
        self.assertEqual(1,1)
    
    def test_other_test(self):
        self.assertFalse(False)