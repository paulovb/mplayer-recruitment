# coding: utf-8
from unittest import TestCase
from app.core.recruitment import Recruitment


class RecruitmentTest(TestCase):
    def test_is_front(self):
        values = {Recruitment().HTML: 8, Recruitment().CSS: 9, Recruitment().JAVASCRIPT: 10}
        self.assertEqual(Recruitment().is_front(values), True)

        values = {Recruitment().HTML: 5, Recruitment().CSS: 9, Recruitment().JAVASCRIPT: 10}
        self.assertEqual(Recruitment().is_front(values), False)

        values = {Recruitment().PYTHON: 8, Recruitment().CSS: 9, Recruitment().JAVASCRIPT: 10}
        self.assertEqual(Recruitment().is_front(values), False)

    def test_is_back(self):
        values = {Recruitment().DJANGO: 8, Recruitment().PYTHON: 10}
        self.assertEqual(Recruitment().is_back(values), True)

        values = {Recruitment().DJANGO: 5, Recruitment().PYTHON: 10}
        self.assertEqual(Recruitment().is_back(values), False)

        values = {Recruitment().PYTHON: 8, Recruitment().CSS: 9, Recruitment().JAVASCRIPT: 10}
        self.assertEqual(Recruitment().is_back(values), False)

    def test_is_mobile(self):
        values = {Recruitment().ANDROID: 8, Recruitment().IOS: 10}
        self.assertEqual(Recruitment().is_mobile(values), True)

        values = {Recruitment().IOS: 5, Recruitment().ANDROID: 10}
        self.assertEqual(Recruitment().is_mobile(values), False)

        values = {Recruitment().ANDROID: 8, Recruitment().JAVASCRIPT: 10}
        self.assertEqual(Recruitment().is_mobile(values), False)