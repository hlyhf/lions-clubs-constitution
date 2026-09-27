#!/usr/bin/env bash
# 在 GitHub 创建 Release 并上传技能包 zip 附件。
# 前置条件（需在联网机器、且已装 gh 并登录，或设置 GH_TOKEN）：
#   - gh auth login   （或用 Personal Access Token 设 GH_TOKEN 环境变量）
#   - 仓库已存在： github.com/hlyhf/lions-clubs-constitution
# 用法： bash release.sh v1.0.0
set -e
cd "$(dirname "$0")"

VERSION="${1:-v1.0.0}"
REPO="hlyhf/lions-clubs-constitution"
ASSET="lions-clubs-constitution-skill.zip"

if [ ! -f "$ASSET" ]; then
  echo "未找到 $ASSET，先运行 bash build_packages.sh"
  bash build_packages.sh
fi

echo ">> 校验 gh 可用性"
if ! command -v gh >/dev/null 2>&1; then
  echo "未安装 gh CLI。请安装：https://cli.github.com 或用 Personal Access Token 设 GH_TOKEN 后重试。"
  exit 1
fi

echo ">> 创建 Release $VERSION 并上传 $ASSET"
gh release create "$VERSION" \
  --repo "$REPO" \
  --title "$VERSION — 中国狮子联会官方基本法 Agent 技能" \
  --notes "$(cat <<NOTES
# lions-clubs-constitution $VERSION

中国狮子联会官方基本法 Agent 技能（多语言·可移植）。

## 内容
- 六部官方文件文本化：章程 / 工作规则 / 财务管理制度 / 会费收取办法 / 会员行为准则 / 视觉形象识别系统手册 A/B
- 18 种语言参考卡（港澳台/日韩/东南亚/中亚/欧洲/非洲/美洲/俄罗斯）
- 条款检索脚本、VI 文字版规范、来源清单、主题路由索引

## 安装
下载本 Release 的 \`$ASSET\`，解压后放入 Agent 技能目录，或上传至 SkillHub / 各 Agent 平台。

## 说明
官方文件版权归中国狮子联会所有，以官方原件为准；多语言译本为辅助参考版。
制作者：精卫服务队 于海峰 狮兄。
NOTES
)" \
  "$ASSET"

echo ">> 完成： https://github.com/$REPO/releases/tag/$VERSION"
