import io
import unittest.mock
import slice_simple as ex2

class TP3SliceSimpleTestCases(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_slice_simple(self, mock_stdout):
        ex2.slice_simple()
        results = mock_stdout.getvalue().splitlines()

        # Matias should contain A and I
        self.assertEqual(results[0], "awe")
        self.assertEqual(results[1], "eso")
        self.assertEqual(results[2], "awesome")

if __name__ == '__main__':
    unittest.main()
