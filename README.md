# research-helper-lite

迭代研究助手简化版：生成子问题 → mock 检索 → 判断信息是否足够 → 汇总报告。
纯规则走完整迭代流程，零第三方依赖，无需联网。

## 功能简介

- `decompose(question)`：生成子问题；
- `mock_search(sub)`：内置知识库做模拟检索；
- `ResearchAssistant().run(question)`：完整流程，输出覆盖率与报告。

## 快速开始

```bash
python3 research_helper.py "什么是机器学习"
```

作为库：

```python
from research_helper import ResearchAssistant
print(ResearchAssistant().run("机器学习")["report"])
```

## 无 API key 如何运行

mock 检索纯本地，**不需要任何 API key**。

## 目录结构

```
research-helper-lite/
├── research_helper.py
├── tests/test_research_helper.py
├── README.md / LICENSE / .gitignore
```

## 运行测试

```bash
python3 -m unittest discover -s tests -v
```

## 许可证

[MIT](./LICENSE) © 2026 ljiang9
