from hello_world.formater import plain_text_upper_case
from hello_world.formater import format_to_xml
import unittest


class TestFormater(unittest.TestCase):
    def test_plain_lowercase(self):
        r = plain_text_upper_case("msg", "imie")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_format_to_xml(self):
        xml = format_to_xml("Ala ma kota", "Ala")
        message = '<greetings><name>Ala</name><msg>' \
                  'Ala ma kota</msg></greetings>'
        self.assertEqual(xml.decode("utf-8"), message)
