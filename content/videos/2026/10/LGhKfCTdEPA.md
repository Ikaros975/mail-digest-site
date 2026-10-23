# When Anthropic Asked Claude What it Was Thinking

## 一句话概括
同问不同答：模型“自述”与“直觉反应”走两条路。

## 核心内容
- 背景与核心观点：视频指出，使用者通常给出提示后只看结果，但“表面之下”模型还有中间过程。「You can literally ask in a prompt like, 'Oh, what were you just thinking about?' And then see if what the model says matches what you read in its intermediate results.」结论是：模型能口头报告的，只是内部活动的一小部分。「there's a lot going on under the surface, but there's only a small subset of things that you're actively thinking about that if I asked you, you could report on.」

- 案例1（自述 vs 中间过程核对）：做法是直接问模型「What were you just thinking about?」，再把它的回答与可读取的中间结果进行对照，检验“自述”是否匹配“内部计算”。视频强调存在不完全匹配的情形：内部发生很多事，但可报告的只是小集合。（解读/推论：这揭示出“高阶反思”与“底层处理”可能分离。）

- 案例2（语言识别 vs 续写反射）：给一段西班牙语文本，问“是什么语言”→答西班牙语；把文本换成法语→答法语。然后改成“让它继续写同一段文本”的任务：当把西语换成法语时，「this time it doesn't work」。视频据此提出：模型可能存在两套处理机制，「A higher order one and a lower order one.」前者像可报告的高阶识别，后者像自动化“反射式”续写。

- 关键结论：视频抛出核心问题：「is this equivalent to what we're finding in these models?」即：人类“能说出的想法”与“实际在想/在做的处理”之差异，是否在模型里也成立？两个案例共同指向：模型的“自述（高阶）”与“反射（低阶）”可能并不总一致。（解读/推论：评估模型时，需分别检验“会说”和“会做”。）

## 记忆锚点
- 【水面与水下】能说的是水面，计算在水下；别把“自述”等同于“全部”。对应逻辑：报告集是内部过程的子集。
- 【问心与反射】问心=高阶识别，反射=自动续写；两条管道各自成线。对应逻辑：同样的换语处理，识别行、续写不行。
- 【换皮不换骨】文字换了“皮”（语言），续写却失灵，说明底层机制没随皮走。对应逻辑：分类可随替换更新，反射未同步。
- 【先验别验收】先听自述，再看中间证据。对应逻辑：自述需与中间结果对账。

## 关键要点
- 要点标题：自述不等于全部内部处理
  - 原文引用：「there's a lot going on under the surface, but there's only a small subset... you could report on」
  - 案例还原：先让模型回答“刚才在想什么”，再对比可读取的中间结果，发现口头报告与内部计算并非一一对应，内部发生的远多于可报告内容。
  - 解读：做评测时须区分“会讲道理”和“真实在算什么”。

- 要点标题：识别任务与反射续写是两路系统
  - 原文引用：「Take a Spanish exerpt... ask the model what language this is... Swap it to French... Now do something that's more like a reflex... Just continue the text... And this time it doesn't work.」
  - 案例还原：先做语言识别，西→答西，换法→答法；再做续写，文本从西换法，续写却失败。说明分类（高阶）和续写（低阶）对同一变更反应不同。
  - 解读：不要用一个任务的好成绩推断另一个任务也可靠。

- 要点标题：研究问题的指向
  - 原文引用：「And so the question we had is, is this equivalent to what we're finding in these models?」
  - 案例还原：在人类心智中，“能说出的念头”只是整体活动一部分；视频据此追问：模型里是否也存在同样的分层处理，并用识别/续写差异做了指证。
  - 解读：为模型对齐与可解释性提供具体切口。

## 三大职业视角洞察（均为解读/推论）
### ① 市场调研 & 用户研究
- 方法启发：把“自述”和“反射”分开测。让用户先口头说明（自述），再看无提示下的即时行为（反射），对照差异。
- 具体做法：任务后追问“你刚才如何判断/选择？”；并设置无需思考的连贯操作测试（如持续完成相似项），看是否与自述一致。
- 踩坑提醒：只听用户“会说”的理由，可能错过“实际在做”的模式。

### ② 品牌推广 & 营销
- 思路：信息识别（记住slogan/理解卖点）不代表反射行为（自发转发/续看/点击）。需双轨评估。
- 手段：A/B中同时测“可报告理解”（问答/回忆）与“无意识反应”（连看率/自然续点）。若两者背离，优化“反射触发”。

### ③ 电商运营
- 策略：把“看懂（识别）”与“下单（反射）”拆开。前者用说明页测理解，后者用一键续购、连单链路测真实推动力。
- 发现：当更换页面语言/呈现方式后，理解分可能提升，但转化不动，说明底层动因未被触达，应优化“反射路径”。

## 精彩原句摘录
- 「You can literally ask... 'What were you just thinking about?'」(开头) 值得记：给出直接的自述式检验方法。
- 「there's a lot going on under the surface, but there's only a small subset... you could report on」(中段) 值得记：核心分层观点的浓缩表述。
- 「Take a Spanish exerpt... Swap the Spanish to French... And this time it doesn't work... two separate kinds of processing」(结尾) 值得记：用一个对照实验引出“两套处理”的关键结论。

## 适合人群
- 需要评测/理解大模型行为的产品、研究与数据人员。
- 关注“会讲道理”与“会做事”差异的从业者，想用小实验识别“高阶”与“低阶”机制者。