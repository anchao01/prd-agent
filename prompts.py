PRD_ANALYSIS_PROMPT = """
你是一个高级产品经理 + 测试架构师。

请从以下PRD中提取：
1. 功能点列表
2. 用户角色
3. 核心流程
4. 边界条件
5. 潜在风险点

PRD内容：
{prd}

请输出JSON：
"""

ACCEPTANCE_PROMPT = """
基于以下PRD分析结果，生成验收标准（Acceptance Criteria）：

要求：
- 使用Given-When-Then格式
- 覆盖正常流程
- 覆盖异常流程
- 覆盖边界情况

输入：
{analysis}

输出JSON：
"""

TESTCASE_PROMPT = """
基于验收标准，生成测试用例：

要求：
1. 包含：
   - 用例ID
   - 用例名称
   - 前置条件
   - 操作步骤
   - 预期结果
   - 用例类型（正常/异常/边界）

2. 尽量全面

输入：
{acceptance}

输出JSON数组：
"""
