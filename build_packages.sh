#!/usr/bin/env bash
# 生成本技能的发布用打包文件（本地即可运行，无需联网）。
# 仓库根目录（本脚本所在目录）即技能根（SKILL.md 在根）。
#   - 技能包 lions-clubs-constitution-skill.zip    = 技能内容（不含维护脚本与 zip 自身），供 SkillHub / DSH 等直接加载
#   - 仓库包 lions-clubs-constitution-github.zip   = 完整仓库内容（含维护脚本），供 GitHub 上传
# 用法： bash build_packages.sh
set -e
cd "$(dirname "$0")"

SKILL_ZIP="lions-clubs-constitution-skill.zip"
GITHUB_ZIP="lions-clubs-constitution-github.zip"

echo ">> 清理旧包"
rm -f "$SKILL_ZIP" "$GITHUB_ZIP"

echo ">> 打包技能包（排除维护脚本与 zip 自身）"
zip -qr "$SKILL_ZIP" . \
  -x '*.zip' \
  -x 'PUSH_GUIDE.sh' -x 'release.sh' -x 'build_packages.sh'

echo ">> 打包仓库包（含维护脚本，仅排除 zip 自身）"
zip -qr "$GITHUB_ZIP" . \
  -x '*.zip'

echo ">> 完成"
ls -lh "$SKILL_ZIP" "$GITHUB_ZIP"
