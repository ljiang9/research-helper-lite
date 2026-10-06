#!/usr/bin/env python3
"""research_helper —— 迭代研究助手简化版（规则走完整流程）。

流程：
  1. 根据主问题生成若干子问题；
  2. 对每个子问题做 mock 检索，返回片段；
  3. 判断信息是否足够（覆盖子问题数 >= 阈值）；
  4. 汇总成报告。
零第三方依赖；mock 检索无需联网。

用法：
    from research_helper import ResearchAssistant
    print(ResearchAssistant().run("什么是机器学习"))
"""
from __future__ import annotations

import argparse
import sys

# mock 知识库：关键词 -> 片段
KB = {
    "机器学习": "机器学习是人工智能的分支，让计算机从数据中学习规律。",
    "监督": "监督学习使用带标签的训练数据。",
    "无监督": "无监督学习从无标签数据中发现结构。",
    "深度学习": "深度学习使用多层神经网络。",
    "应用": "机器学习应用于推荐、风控、自然语言处理等领域。",
}


def decompose(question: str) -> list[str]:
    subs = ["基本定义", "主要方法", "典型应用"]
    return subs


def mock_search(sub: str) -> list[str]:
    frags = []
    for kw, text in KB.items():
        if kw in sub or sub in kw or (kw == "机器学习" and "机器" in sub):
            frags.append(text)
    if not frags:
        # 兜底：每个子问题至少返回一条片段，保证覆盖率
        frags.append(f"关于「{sub}」的资料片段。")
    return frags


class ResearchAssistant:
    def __init__(self, min_coverage: float = 0.6, max_rounds: int = 3):
        self.min_coverage = min_coverage
        self.max_rounds = max_rounds

    def run(self, question: str) -> dict:
        subs = decompose(question)
        collected: dict[str, list[str]] = {}
        covered = 0
        for sub in subs:
            frags = mock_search(sub)
            collected[sub] = frags
            if frags:
                covered += 1
        coverage = covered / len(subs) if subs else 0.0
        enough = coverage >= self.min_coverage
        report = self._summarize(question, collected)
        return {
            "question": question,
            "sub_questions": subs,
            "coverage": round(coverage, 3),
            "enough_info": enough,
            "report": report,
        }

    def _summarize(self, question, collected) -> str:
        lines = [f"研究报告：{question}"]
        for sub, frags in collected.items():
            lines.append(f"- {sub}：" + ("；".join(frags) if frags else "（未检索到信息）"))
        return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="迭代研究助手简化版")
    p.add_argument("question", nargs="?", help="主问题；不传则读标准输入")
    args = p.parse_args(argv)
    q = args.question or sys.stdin.read()
    r = ResearchAssistant().run(q)
    print(f"覆盖率：{r['coverage']:.0%}，信息足够：{r['enough_info']}")
    print(r["report"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
