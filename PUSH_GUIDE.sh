#!/usr/bin/env bash
# 将本目录推送到 GitHub 账号 hlyhf 的 lions-clubs-constitution 仓库。
# 用法：在已联网、且已配置 git 与 GitHub 凭据的机器上运行：
#   bash PUSH_GUIDE.sh
# 首次运行会交互要求 GitHub 用户名/令牌（Personal Access Token，需 repo 权限）。
set -e
REPO="lions-clubs-constitution"
REMOTE="https://github.com/hlyhf/${REPO}.git"

git init -q 2>/dev/null || true
git add -A
git commit -q -m "feat: lions-clubs-constitution v1.0.0 — 中国狮子联会官方基本法多语言 Agent 技能

- 六部官方基本法文本化（章程/工作规则/财务制度/会费办法/行为准则/VI手册）
- 18 种语言参考卡（港澳台/日韩/东南亚/中亚/欧洲/非洲/美洲/俄罗斯）
- 条款检索脚本、VI 文字版规范、来源清单、主题路由索引
- 制作者：精卫服务队 于海峰 狮兄" || echo "（若已提交可忽略）"

git branch -M main
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "$REMOTE"
else
  git remote add origin "$REMOTE"
fi

echo "准备推送。若仓库尚未在 GitHub 创建，请先在网页新建空仓库："
echo "  https://github.com/new  ->  Repository name: ${REPO}  ->  Create repository"
echo "然后按提示输入 GitHub 用户名与 Token。"
git push -u origin main
