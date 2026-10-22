# AI Models Are Grown Not Built

## 一句话概括
大模型是“养”出来的：先搭脚手架、喂数据，让它自己长出看不见的公式。

## 核心内容（字数视视频长度而定，上不封顶）
- 背景与核心观点：视频一开头提醒我们别把语言模型简单化——「People that will confidently say, like, 'Ah, language models are just X or just Y.' are the people that actually haven't spent a while living inside.」作者强调「to make them is not to understand them.」也就是说，你可以把模型做出来，但并不等于真正理解它的内部原理。

- 模型的“生长式”制造：制作过程像先搭「scaffold（脚手架）」——「building this architecture, which is kind of like a scaffold」——再「pass a bunch of data through them」，模型会「grow in inscrutable ways」。技术流程层面，它「take this input… bunch of words → turn these words into numbers → do some math… again and again → final result → convert back into a word」。其中反复进行的「math（计算）」部分，正是“长出来”的能力。

- 黑箱的数学与中间态：关键点是「The math that they do… that's the part that's grown… We have no idea what they are.」团队的目标则是「study… what these formulas mean… what these intermediate results are. Can we decode them, and can we see… what the model is doing as it's doing all of this intermediate stuff.」也就是做可解释性与中间表征的解码工作。

- 类生物而非纯工程：总结性比喻是「A lot of what we do feels so much closer to biology than to engineering.」与其说是在“装配”一个机器，不如说是在“培育”一个会产生自发结构的系统。

## 记忆锚点（3-5条）
- 【脚手架养成】先搭脚手架，再喂大量数据，能力是“长”出来的；逻辑：结构+数据→反复计算→能力涌现，非逐件装配。
- 【黑箱公式】输出像说话，内里全是我们「have no idea」的公式；逻辑：中间数学是学习产物，人类暂不可见。
- 【中间态解码】盯住“路上”的中间结果做解码；逻辑：理解“在算什么”要看中间表征而非只看输入输出。
- 【更像生物】工程搭台、生物生长；逻辑：流程可控，内容自组织，因而不可简化为“just X or Y”。

## 关键要点（3-6条）
- 要点标题：别把模型简化为“just X or Y”
  - 原文引用：「People that will confidently say, like, 'Ah, language models are just X or just Y.' are the people that actually haven't spent a while living inside.」
  - 案例还原：视频描述了一个最简流程：输入是一堆词，先被转成数字，随后模型对这些数字“做数学”一遍又一遍，最后再把结果转回一个词。这个链条看似直观，但作者点明，真正“难”的在于这些反复的计算步骤里学出了哪些公式，以及它们如何协同工作。这部分恰恰是外部观察者最容易忽视、也最容易被简化为“就是X或Y”的地方。
  - 解读：提醒从业者降低还原论冲动，承认复杂性边界。

- 要点标题：模型能力是“长”出来的，不是装配出来的
  - 原文引用：「building this architecture, which is kind of like a scaffold, and then you pass a bunch of data through them and they sort of like grow in inscrutable ways.」
  - 案例还原：作者给出“先搭脚手架（架构）→喂数据→能力生长”的路径。以语言模型为例：它把词变成数字，经由多轮计算得到中间结果，再输出一个词。关键在于这套计算的具体公式不是人工写出来的，而是在学习过程中“长”出来的，人类并不清楚这些公式到底是什么，因此能力呈现出不可预设、难以完全解释的特征。
  - 解读：为研发与评估设定正确预期：可设计条件，不可预配能力。

- 要点标题：做可解释性要盯“中间态”
  - 原文引用：「The goal of my team is to… study… what these intermediate results are. Can we decode them, and can we see… what the model is doing as it's doing all of this intermediate stuff.」
  - 案例还原：同样基于输入→数字→反复计算→输出的链条，团队不满足于看最终输出，而是把注意力放在“中间结果”。这些中间表征承载了模型在每一步“在算什么”的线索。通过解码这些表征，有望理解那部分“长”出来、我们「have no idea」的公式在具体任务中的运行方式。
  - 解读：方法论转向过程可观测性，而非仅靠结果评测。

## 三大职业视角洞察（重点！）
### ① 市场调研 & 用户研究（解读/推论）
- 洞察：当能力是“生长式”的，用户体验会随数据与场景变化而漂移。调研应更重纵向追踪与情境化测试，而非一次性结论。
- 方法：构建“中间态指标”框架（如过程信号、失败类型分类）来辅助理解输出背后的不稳定来源。
- 坑点：把模型等同为“规则引擎”做简单用研假设，易误判真实可用性边界。

### ② 品牌推广 & 营销（解读/推论）
- 思路：传播上用“脚手架+养成”的比喻教育市场，降低过度承诺风险，强调持续训练与迭代。
- 手段：展示“中间态可解释”进展与安全验证过程，替代单一Benchmark炫耀，更能建立信任。

### ③ 电商运营（解读/推论）
- 策略：将模型视作会“长”的运营资产，持续喂以高质量交互数据与反馈，滚动优化场景效果。
- 转化：设计可观察的过程信号（如召回/重写/排序各步表现）来定位问题环节，而非只盯最终转化。

### ④ 智能硬件 PM（AI时代新定义）（解读/推论）
- 作用阶段：AI的“生长式”特性更适合在算法与数据环节迭代；ID/MD等确定性阶段仍以工程流程为主，但可用AI做方案生成与探索。
- 边界：能力不可被完全“装配”，PM需通过数据策略与过程可观测性来“养”，并承担解释与风险管理。
- 信号：团队对“中间结果”的关注提示PM要把可解释与观测点嵌入产品管线，而非只验最终输出。

## 精彩原句摘录（2-5条）
- 「to make them is not to understand them.」（中段）——一针见血地区分“能做出来”与“能解释清”，校准团队认知边界。
- 「they sort of like grow in inscrutable ways.」（中段）——点明“生长式黑箱”，为规划与期望管理定调。
- 「The math that they do… that's the part that's grown… We have no idea what they are.」（中段）——直指黑箱核心在“学到的公式”不可见。
- 「A lot of what we do feels so much closer to biology than to engineering.」（结尾）——最形象的类比，帮助非技术受众快速把握本质。

## 适合人群
- 想快速校准对大语言模型本质认知的产品、研发、数据与策略从业者。
- 正在做可解释性、评测或落地应用决策的人，需理解“可做不等于可懂”的边界与方法转向。