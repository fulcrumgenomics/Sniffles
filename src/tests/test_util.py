from unittest import TestCase

from sniffles.util import weighted_mean, mean


class Test(TestCase):
    def test_weighted_mean_equal_weight(self):
        values = [1, 2, 3]
        weights = [2, 2, 2]
        self.assertEqual(weighted_mean(values, weights), mean(values))

    def test_weighted_mean(self):
        values = [1, 2, 3]
        weights = [3, 2, 1]
        self.assertEqual(weighted_mean(values, weights), (3 + 4 + 3) / (1 + 2 + 3))


    def test_weighted_mean_zip(self):
        values = [1, 2, 3]
        weights = [3, 2, 1]
        self.assertEqual(weighted_mean(*zip(*zip(values, weights))), (3 + 4 + 3) / (1 + 2 + 3))
