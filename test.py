from unittest import TestCase
from bikerent import (
    Rent, getquote, RATE_RENT, FAMILY_DISCOUNT_PERCENTAJE)
from datetime import datetime, timedelta

class TestQuote(TestCase):
    def setUp(self):
        self.date_start =  datetime.now()
        self.date_start_minutes =  datetime.now() + timedelta(minutes=30)
        self.date_end_4h =  datetime.now() + timedelta(hours=4)
        self.date_end_1w =  datetime.now() + timedelta(days=7)
        self.date_end_gt1w =  datetime.now() + timedelta(days=7, hours=25)        

    def test_badparameters(self):
        self.assertIsInstance(
            getquote(10, self.date_start , self.date_start),
            str)
        self.assertIsInstance(
            getquote(1, self.date_start , self.date_start_minutes),
            str)
        self.assertIsInstance(
            getquote(1, "xx", self.date_start),
            str)
        self.assertIsInstance(
            getquote(1, self.date_start, "xx"),
            str)
        self.assertIsInstance(
            getquote(1, self.date_start, 4545),
            str)
        self.assertIsInstance(
            getquote(1, self.date_end_4h, self.date_start),
            str)


    def test_good_badget(self):
        rate4h = RATE_RENT["hour"] * 4
        self.assertEqual(
            getquote(1, self.date_start, self.date_end_4h),
            rate4h)
        self.assertEqual(
            getquote(1, "2019-06-01T16:00", "2019-06-01T20:00"),
            rate4h)
        self.assertEqual(
            getquote(2, self.date_start, self.date_end_4h),
            rate4h * 2)
        self.assertEqual(
            getquote(3, self.date_start, self.date_end_4h),
            (rate4h * 3) * (1 - FAMILY_DISCOUNT_PERCENTAJE/100))

class TestClass(TestCase):
    def test_rent_ok(self):
        tested_rent = Rent("daniel", 23)
        tested_rent.add_rented_period(1, "2019-06-01T16:00", "2019-06-01T20:00")
        self.assertEqual(
            tested_rent.rented_periods[0]["paid"],
            RATE_RENT["hour"]*4)

    def test_rent_bad(self):
        tested_rent = Rent("daniel")
        with self.assertRaises(ValueError):
            tested_rent.add_rented_period(1, "00", "2010")
