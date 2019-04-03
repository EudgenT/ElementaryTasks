#!/usr/bin/env python3
import unittest
import envelopes as env


class TestEnvelopes(unittest.TestCase):

    def test_constructor(self):
        envelop = env.Envelope(5, 5)
        self.assertEqual((envelop.width, envelop.height), (5, 5))

    def test_less_envelop(self):
        first_envelop = env.Envelope(4, 8)
        second_envelop = env.Envelope(10, 12)
        self.assertLess(first_envelop, second_envelop)

    def test_greater_envelop(self):
        first_envelop = env.Envelope(14, 18)
        second_envelop = env.Envelope(10, 12)
        self.assertGreater(first_envelop, second_envelop)


if __name__ == '__main__':
    unittest.main()
