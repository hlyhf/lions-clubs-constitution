#!/usr/bin/env bash
# 将本目录（已是技能根，含 SKILL.md）推送到 GitHub 账号 hlyhf 的仓库。
# 前置：联网机器，已配 git 与 GitHub 凭据（PAT，需 repo 权限）。
# 用法： bash PUSH_GUIDE.sh
set -e
cd "$(dirname "$0")"

REPO="lions-clubs-constitution"
REMOTE="https://github.com/hlyhf/${REPO}.git"

# 若尚未初始化 git，则初始化并提交；若已是 git 仓库则增量提交
if [ ! -d .git ]; then
  git init -q
  git add -A
  git commit -q -m "feat: lions-clubs-constitution v1.0.0 — 中国狮子联会官方基本法多语言 Agent 技能

- 六部官方基本法文本化（章程/工作规则/财务制度/会费办法/行为准则/VI手册）
- 18 种语言参考卡（港澳台/日韩/东南亚/中亚/欧洲/非洲/美洲/俄罗斯）
- 条款检索脚本、VI 文字版规范、来源清单、主题路由索引
- 制作者：精卫服务队 于海峰 狮兄" || true
else
  git add -A
  git commit -q -m "chore: update lions-clubs-constitution (see references/manifest.md)" || echo "（无变更可提交）"
fi

git branch -M main
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REMOTE"
else
  git remote add origin "$REMOTE"
fi

echo "准备推送至 $REMOTE"
echo "若提示登录：用户名填 hlyhf，密码/令牌粘贴 GitHub Personal Access Token（需 repo 权限）。"
git push -u origin main
echo ">> 完成： https://github.com/$REMOTE"
