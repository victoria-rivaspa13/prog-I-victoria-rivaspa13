import io
import unittest.mock
import in_string as ex1


class TP3InStringTestCases(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_in_string(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="Matias"):
            ex1.check_vowels()
            results = mock_stdout.getvalue().splitlines()

            # Matias should contain A and I
            self.assertEqual(results[0], "Contiene a: True")
            self.assertEqual(results[1], "Contiene e: False")
            self.assertEqual(results[2], "Contiene i: True")
            self.assertEqual(results[3], "Contiene o: False")
            self.assertEqual(results[4], "Contiene u: False")

        with unittest.mock.patch('builtins.input', return_value="Augusto"):
            ex1.check_vowels()
            results = mock_stdout.getvalue().splitlines()

            # Augusto should contain A, O and U
            self.assertEqual(results[5], "Contiene a: True")
            self.assertEqual(results[6], "Contiene e: False")
            self.assertEqual(results[7], "Contiene i: False")
            self.assertEqual(results[8], "Contiene o: True")
            self.assertEqual(results[9], "Contiene u: True")

        with unittest.mock.patch('builtins.input', return_value="Ines"):
            ex1.check_vowels()
            results = mock_stdout.getvalue().splitlines()

            # Ines should contain E and I
            self.assertEqual(results[10], "Contiene a: False")
            self.assertEqual(results[11], "Contiene e: True")
            self.assertEqual(results[12], "Contiene i: True")
            self.assertEqual(results[13], "Contiene o: False")
            self.assertEqual(results[14], "Contiene u: False")

        with unittest.mock.patch('builtins.input', return_value="Juan"):
            ex1.check_vowels()
            results = mock_stdout.getvalue().splitlines()

            # Juan should contain A and U
            self.assertEqual(results[15], "Contiene a: True")
            self.assertEqual(results[16], "Contiene e: False")
            self.assertEqual(results[17], "Contiene i: False")
            self.assertEqual(results[18], "Contiene o: False")
            self.assertEqual(results[19], "Contiene u: True")


if __name__ == '__main__':
    unittest.main()
