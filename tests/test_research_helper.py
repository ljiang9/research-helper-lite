import unittest

from research_helper import ResearchAssistant, decompose, mock_search


class TestHelpers(unittest.TestCase):
    def test_decompose(self):
        subs = decompose("什么是机器学习")
        self.assertGreaterEqual(len(subs), 3)

    def test_mock_search(self):
        self.assertTrue(mock_search("定义"))


class TestAssistant(unittest.TestCase):
    def test_full_flow(self):
        r = ResearchAssistant().run("什么是机器学习")
        self.assertIn("sub_questions", r)
        self.assertIn("report", r)
        self.assertGreaterEqual(r["coverage"], 0)
        self.assertLessEqual(r["coverage"], 1.0)

    def test_enough_info(self):
        r = ResearchAssistant(min_coverage=0.5).run("机器学习")
        self.assertTrue(r["enough_info"])

    def test_report_contains_question(self):
        r = ResearchAssistant().run("测试问题")
        self.assertIn("测试问题", r["report"])


if __name__ == "__main__":
    unittest.main()
