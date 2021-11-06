import requests
import unittest
from unittest import mock

import requests

from main import get_doc_owner_name,  add_new_doc, delete_doc, get_doc_shelf
from YA_API import create_folder

class Test(unittest.TestCase):

    def test_get_doc_owner_name(self):
        with unittest.mock.patch('builtins.input', return_value='11-2'):
            self.assertEqual(get_doc_owner_name(), "Геннадий Покемонов")

    def test_get_doc_shelf(self):
        with unittest.mock.patch('builtins.input', return_value='11-2'):
            self.assertEqual(get_doc_shelf(), "1")

    def test_add_new_doc(self):
        with unittest.mock.patch('builtins.input', return_value='11-3'):
            with unittest.mock.patch('builtins.input', return_value='invoice'):
                with unittest.mock.patch('builtins.input', return_value='Василий Пупкин'):
                    with unittest.mock.patch('builtins.input', return_value='3'):
                        self.assertEqual(add_new_doc(), "3")

    def testget_delete_doc(self):
        with unittest.mock.patch('builtins.input', return_value='11-2'):
            self.assertEqual(delete_doc(), ("11-2", True))

    def testget_create_folder(self):
        with unittest.mock.patch('builtins.input', return_value='16'):
            self.assertEqual(create_folder(), '<Response [201]>')

    def testget_create_folder_errors(self):
        with unittest.mock.patch('builtins.input', return_value='16'):
            self.assertNotEqual(create_folder(), '<Response [201]>'), print(create_folder())



if __name__=='__main__':
    unittest.main()