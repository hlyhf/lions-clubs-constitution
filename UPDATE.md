# 持续更新机制（维护指引）

> 本文档说明：当中国狮子联会的官方文件（章程/工作规则/财务制度/会费办法/行为准则/VI手册）发生修订时，如何同步更新本技能并保持版本可追溯。

## 一、版本号规则（语义化 Semantic Versioning）

`MAJOR.MINOR.PATCH`
- **PATCH**（x.y.+1）：引用文字润色、错别字修正、路由索引补充、i18n 翻译完善——**不涉及条款实质变化**。
- **MINOR**（x.+1.0）：新增官方文件译本/语言、新增模板、新增辅助索引文件——**功能扩展但向下兼容**。
- **MAJOR**（+1.0.0）：官方基本法发生重大修订（如会费标准、会员条件、组织架构调整），或技能结构不兼容变更。

## 二、官方文件更新时的标准流程

1. **核对原件**：取得联会最新核准/修订版官方文件，确认变更点（条款号、金额、时限、人数等）。
2. **更新 `references/` 对应文件**：
   - 全文类（章程/工作规则/财务/行为准则）：替换或补登修订段落，**保留原文逐字**。
   - 会费办法：若仍为图片版，更新 `references/assets/会费办法/` 原页图并重新转录 `会费收取办法.md`。
   - VI 手册：更新 `assets/vis/` 对应页图，并同步 `references/VI规范文字版.md` 的条文与页码。
3. **同步衍生文件**：
   - 修订条款若影响"官方知识骨架"，更新 `SKILL.md` 第三节对应小节。
   - 更新 `references/路由索引.md`（若涉及主题或位置变化）。
   - 更新 `references/manifest.md` 的版本/覆盖核验行。
4. **同步多语言**：若变更的是数字/条款实质内容，运行 `i18n/generate_summaries.py` 重新生成 18 种语言的 `summary.md`（脚本从统一事实源生成，**确保各语言数字一致**）；如仅为文字润色，可手动只改受影响语种。
5. **递增版本号**：改 `SKILL.md` frontmatter 的 `version`，并同步 `README.md` / `README.en.md` 顶部版本、本文件"当前版本"行。
6. **重新打包**：`bash build_packages.sh`（生成 `lions-clubs-constitution-skill.zip` 与 `lions-clubs-constitution-github.zip`）。
7. **提交并推送**：`bash PUSH_GUIDE.sh`。
8. **发版**：`bash release.sh vX.Y.Z`（见第三节，需在联网机器执行，会创建 GitHub Release 并上传 zip）。

## 三、配套脚本

| 脚本 | 作用 | 是否在联网环境运行 |
| --- | --- | --- |
| `i18n/generate_summaries.py` | 从统一事实源重新生成 18 语言参考卡 | 本地即可 |
| `build_packages.sh` | 生成两个发布用 zip（skill 包 + github 仓库包） | 本地即可 |
| `PUSH_GUIDE.sh` | git 初始化/提交/推送至 `hlyhf/lions-clubs-constitution` | 需联网 + GitHub 凭据 |
| `release.sh` | 调用 GitHub API 创建 Release 并上传 zip 附件 | 需联网 + `gh` CLI 或 PAT |

## 四、当前版本

- **v1.0.0**（2025-09-28）：初版，六部官方文件 + 18 语言参考卡 + 检索脚本 + VI 文字版规范 + 来源清单 + 路由索引。制作者：精卫服务队 于海峰 狮兄。

## 五、注意事项

- **中文官方原件始终为唯一权威源**；任何译本/转录/摘要与原文不一致时以原文为准。
- 官方文件版权归**中国狮子联会**，收录仅用于组织内部学习与会务合规辅助。
- 推送前请在 `PUSH_GUIDE.sh` / `release.sh` 中确认 `REMOTE` 与 `REPO` 变量指向 `hlyhf/lions-clubs-constitution`。
