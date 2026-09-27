# 中国狮子联会官方基本法 Skill（lions-clubs-constitution）

> **GitHub 仓库描述（Description）**：中国狮子联会官方基本法 Agent 技能（多语言·可移植）：依据联会章程、工作规则、财务管理制度、会费收取办法、会员行为准则、视觉形象识别系统手册六部官方文件编制，提供制度查询、合规审查、会费解答、VI规范、文案起草。覆盖18种语言（港澳台/日韩/东南亚/中亚/欧洲/非洲/美洲/俄罗斯），适配 DSH/OpenClaw/Hermes/WorkBuddy/豆包工作/千问工作等平台。制作者：精卫服务队 于海峰 狮兄。
>
> **版本**：v1.0.0 ｜ **创建日期**：2025-09-28 ｜ **制作者：精卫服务队 于海峰 狮兄**
> 一个具有官方属性的中国狮子联会专属 Agent Skill，依据联会官方基本法编制，为每个服务队、每名会员、每类 Agent 提供制度查询、合规审查与文案起草支持。
>
> **技能标准来源（skill 标准）**：遵循 **Anthropic Agent Skills 标准**（以 `SKILL.md` 为核心、含 YAML frontmatter 的目录式技能格式）。
> **内容权威来源（官方）**：中国狮子联会官方文件（联会官方文件目录）：章程、工作规则、财务管理制度、会费收取办法、会员行为准则、视觉形象识别系统使用手册 A/B。文件版权归 **中国狮子联会** 所有，以官方原件为准。
> **许可证**：MIT（含官方文件版权特别声明，见 `LICENSE`）。

## 这是什么

`lions-cls-constitution` 是一个可移植的 **Agent Skill**（兼容 Anthropic Agent Skills 标准格式），把中国狮子联会的六部官方文件（"基本法"）结构化为 AI 可直接引用的知识库与工作流：

| 官方文件 | 版本 | 在本技能中 |
| --- | --- | --- |
| 中国狮子联会章程 | 2021-10-15 民政部核准 | `references/章程.md` |
| 中国狮子联会工作规则 | 现行 | `references/工作规则.md` |
| 中国狮子联会财务管理制度 | 2023-04-25 修订 | `references/财务管理制度.md` |
| 中国狮子联会会费收取办法 | 2023-07-01 施行 | `references/会费收取办法.md`（转录稿 + 原页图） |
| 中国狮子联会会员行为准则 | 现行 | `references/会员行为准则.md` |
| 联会视觉形象识别系统使用手册 A / B | 现行 | 文本 + `assets/vis/` 全部页面图 |

## 目录结构

```
lions-clubs-constitution/
├── SKILL.md                      # 技能主文件（Agent 加载入口）
├── README.md                     # 本说明
├── LICENSE                       # MIT + 官方文件版权特别声明
├── references/                   # 官方文件文本化全文（权威依据）
│   ├── 章程.md                   #   全文（民政部核准版）
│   ├── 工作规则.md               #   全文（12章）
│   ├── 财务管理制度.md           #   全文（23章）
│   ├── 会费收取办法.md           #   全文转录（12条）+ 速查表
│   ├── 会员行为准则.md           #   全文（18条）
│   ├── VI手册A.md                #   A册文本层/页码索引
│   ├── VI手册B.md                #   B册代表处条目
│   ├── VI规范文字版.md           #   VI 规范文字化（制图/色彩/禁用清单）
│   ├── templates.md              #   6 类官方文案模板
│   ├── 路由索引.md               #   主题→来源 路由表
│   ├── manifest.md               #   来源清单（7份官方文件全部收录核验）
│   └── assets/会费办法/          #   会费办法原件页面图
├── assets/vis/manualA|manualB/   # VI 手册全部页面图（A 23 + B 32 + 第28页放大）
├── i18n/                         # 多语言参考卡（18 种语言）
│   ├── README.md                 #   区域 → 语言覆盖矩阵与使用说明
│   ├── generate_summaries.py      #   参考卡生成脚本（统一源事实，数字全球一致）
│   └── <zh-Hant|en|ja|ko|ru|fr|de|es|pt|ar|vi|th|id|tl|my|kk|uz|sw>/
│       └── summary.md            #   对应语言的核心参考卡
└── scripts/
    └── search_clauses.py         # 条款检索脚本
```

## 能力（Agent 可完成的任务）

1. **制度问答** — 按条款作答并标注"依据《X》第 Y 条"。
2. **合规审查** — 活动/募捐/宣传/财务五步合规检查，输出"通过/需修改/否决"清单。
3. **会务指引** — 服务队设立（25 人创队等）、换届（3–4 月全体会员会议、队长团队 ≤13 人）、例会、报批流程。
4. **会费解答** — 入会费/年度会费/转队费标准、缴纳时限、逾期后果、上缴规则。
5. **VI 审查** — 标识使用、组合规范、禁用情形，结合手册页面图给"可用/需整改/不可用"结论。
6. **文案起草** — 通知、入会申请、转队申请、活动方案、财务说明、处理建议报告等官方文案模板。
7. **多语言支持** — 面向多国籍会员，提供 `i18n/` 下 18 种语言参考卡（覆盖港澳台、日韩、东南亚、中亚、欧洲、非洲、美洲、俄罗斯等），Agent 按用户语言自动加载；正式判断以中文官方原件为准。

## 安装与调用

### 方式一：作为 DSH / Anthropic Agent Skill

把 `lions-clubs-constitution/` 目录放入 Agent 的技能目录（如 `~/.claude/skills/` 或 DSH 会话技能目录），Agent 会在命中狮子会相关意图时自动加载 `SKILL.md`。

### 方式二：任意 Agent / 工作流

把本目录作为知识库挂载，要求 Agent 先读 `SKILL.md`，再按其指引到 `references/` 检索条款作答。可用 `scripts/search_clauses.py` 快速定位条款：

```bash
python3 scripts/search_clauses.py 会费
python3 scripts/search_clauses.py 服务队 工作规则
python3 scripts/search_clauses.py 标识 会员行为准则
```

### 方式三：GitHub / SkillHub 发布

- 仓库根目录即 `lions-clubs-constitution/`（或把它放在仓库子目录），保持 `SKILL.md` 在技能根即可被多数平台识别。
- 建议 topic/tag：`lions`、`lions-clubs`、`china-lions`、`ngo`、`constitution`、`governance`、`compliance`、`agent-skills`。

## 多 Agent 平台调用说明

本技能采用开放标准目录结构，**不绑定任何厂商**，以下平台均可直接调用。通用加载原则：把本技能目录交给 Agent，并提示"遇到狮子会相关请求时先读取 `SKILL.md`，再按指引到 `references/` 检索条款作答"。

| Agent / 平台 | 调用方式 | 加载入口 | 备注 |
| --- | --- | --- | --- |
| **Deepseek Harness（DSH）** | 放入会话技能目录，或 `skill` 工具加载 `lions-cls-constitution` | `SKILL.md` | 命中意图自动加载 |
| **OpenClaw** | 作为 Agent Skill / 知识包挂载 | `SKILL.md` | 支持 SKILL.md 标准 |
| **Hermes** | 作为技能目录或 RAG 知识库加入 | `SKILL.md` + `references/` | 建议用 `search_clauses.py` |
| **WorkBuddy** | 作为工作流技能/知识源导入 | `SKILL.md` | 模板见 `templates.md` |
| **豆包工作（字节）** | 企业知识库/技能导入 | `SKILL.md` | 中文语境直接可用 |
| **千问工作（阿里）** | 助理知识库/插件导入 | `SKILL.md` + `references/` | 大文档走检索脚本 |

## 发布平台与分发

| 平台 | 形态 | 说明 |
| --- | --- | --- |
| **SkillHub** | 技能包 | 上传 `lions-clubs-constitution/` 或 `lions-clubs-constitution-skill.zip` |
| **GitHub** | 仓库 | 根含 `SKILL.md` + `README.md` + `LICENSE` |
| **Deepseek Harness** | 会话技能 | 直接加载目录或 zip |
| **OpenClaw / Hermes / WorkBuddy / 豆包工作 / 千问工作** | 技能或知识库 | 按上表导入 |

## 使用原则（写给调用本技能的 Agent）

1. **先查条款再回答**，并标注依据；
2. **金额、人数、时限等数字逐字核对** `references/` 原文；
3. **超出收录范围就承认**，指引咨询联会秘书处/所在代表处；
4. **VI 判断给结论**：可用 / 需整改 / 不可用，并指明违规点。

## 官方性声明

- 本技能为**精卫服务队 于海峰 狮兄**依据中国狮子联会官方基本法原文编制的**辅助性技能**，非联会官方发布的软件产品；其**内容权威性来自所收录的联会官方文件**，以官方原件为准。
- 本技能遵循 **Anthropic Agent Skills 标准** 编制，可通用分发于上述各平台；分发时请保留 `SKILL.md` 头部的版本、作者、官方来源与 `LICENSE` 信息。
- 收录文件版权归**中国狮子联会**所有，仅用于组织内部学习、会务与合规辅助；视觉形象（狮徽等）使用受《联会视觉形象识别系统使用手册》约束，**不得用于商业用途**（《会员行为准则》第八条）。
- 如官方文件更新，请以最新核准版本为准并同步更新版本号（语义化版本 `MAJOR.MINOR.PATCH`）。

---

**制作者：精卫服务队 于海峰 狮兄 ｜ 版本 v1.0.0 ｜ 创建日期 2025-09-28**
