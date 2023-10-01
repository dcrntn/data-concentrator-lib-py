import unittest
import dconc

...


class TestDconc(unittest.TestCase):
    def test_ip(self):
        my_dc = dconc.data_concentrator("http://127.0.0.1:8000")
        self.assertEqual(my_dc.srv_ip, "http://127.0.0.1:8000")

    def test_get_all(self):
        my_dc = dconc.data_concentrator("http://127.0.0.1:8000")
        get_all = my_dc.get_all_dnode()
        self.assertEqual(len(get_all), 2)

    def test_write_dnode(self):
        my_dc = dconc.data_concentrator("http://127.0.0.1:8000")
        change_count = my_dc.write_dnode_value("ayH7nFocwL2urRvOQOfQ", "111")
        self.assertEqual(change_count, "{'changed_count': '1'}")

    def test_read_dnode(self):
        my_dc = dconc.data_concentrator("http://127.0.0.1:8000")
        self.assertEqual("111", my_dc.get_dnode_value("ayH7nFocwL2urRvOQOfQ"))


if __name__ == "__main__":
    unittest.main()
