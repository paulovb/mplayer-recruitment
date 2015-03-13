# coding: utf-8
from unittest import TestCase
from app.core.recruitment_service import RecruitmentService


class RecruitmentTest(TestCase):
    def test_is_front(self):
        recruitment_service = RecruitmentService()

        recruitment_service.values = {recruitment_service.HTML: 8, recruitment_service.CSS: 9, recruitment_service.JAVASCRIPT: 10}
        self.assertEqual(recruitment_service.is_front(), True)

        recruitment_service.values = {recruitment_service.HTML: 5, recruitment_service.CSS: 9, recruitment_service.JAVASCRIPT: 10}
        self.assertEqual(recruitment_service.is_front(), False)

        recruitment_service.values = {recruitment_service.PYTHON: 8, recruitment_service.CSS: 9, recruitment_service.JAVASCRIPT: 10}
        self.assertEqual(recruitment_service.is_front(), False)

    def test_is_back(self):
        recruitment_service = RecruitmentService()

        recruitment_service.values = {recruitment_service.DJANGO: 8, recruitment_service.PYTHON: 10}
        self.assertEqual(recruitment_service.is_back(), True)

        recruitment_service.values = {recruitment_service.DJANGO: 5, recruitment_service.PYTHON: 10}
        self.assertEqual(recruitment_service.is_back(), False)

        recruitment_service.values = {recruitment_service.PYTHON: 8, recruitment_service.CSS: 9, recruitment_service.JAVASCRIPT: 10}
        self.assertEqual(recruitment_service.is_back(), False)

    def test_is_mobile(self):
        recruitment_service = RecruitmentService()

        recruitment_service.values = {recruitment_service.ANDROID: 8, recruitment_service.IOS: 10}
        self.assertEqual(recruitment_service.is_mobile(), True)

        recruitment_service.values = {recruitment_service.IOS: 5, recruitment_service.ANDROID: 10}
        self.assertEqual(recruitment_service.is_mobile(), False)

        recruitment_service.values = {recruitment_service.ANDROID: 8, recruitment_service.JAVASCRIPT: 10}
        self.assertEqual(recruitment_service.is_mobile(), False)