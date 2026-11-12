# FDE模式行业观察与实践 · Codex Skill

10章：企业AI落地、前线学习、Echo/Delta与本体沉淀。基于腾讯研究院的原书或报告，面向逐章学习、概念问答、自测及实际项目诊断。

## 直接让 Codex 安装

把下面这句话发给另一台电脑上的 Codex：

    请使用 skill-installer 从 https://github.com/moonwalk6688/tencent-fde-industry-practice 安装 skills/tencent-fde-industry-practice 技能。

## 下载 ZIP 安装

从 https://github.com/moonwalk6688/tencent-fde-industry-practice/releases/tag/v1.1.0 下载 ZIP，解压后进入其中的 tencent-fde-industry-practice 目录，运行 Python 3：

    python install.py

macOS/Linux 的命令可能是 python3。默认安装到用户目录的 .agents/skills/tencent-fde-industry-practice；已有同名目录时停止，不会覆盖。可用 --skills-dir 指定技能父目录。也可把 skills/tencent-fde-industry-practice 文件夹手动复制到技能目录。安装位置见 https://developers.openai.com/codex/skills 。若未识别，请开启新对话或重启 Codex。

## 提问示例

    $tencent-fde-industry-practice 从第1章开始教我，每次讲一个判断，再用一个问题检查理解。

    $tencent-fde-industry-practice 帮我分析一个企业AI项目从Demo进入生产缺少的证据。

## 来源与限制

本仓库是独立整理的学习资料，非作者、机构或出版社官方版本；原书著作权归相应权利人。本包不含原始PDF、整本OCR或临时图片链接，不能替代阅读原著。

章节笔记可独立使用。原文行号属于用户提供的OCR版本，并非印刷页码。若拥有相同版本的OCR，可运行：

    python skills/tencent-fde-industry-practice/scripts/read_source.py --source "你的OCR.md" --chapter 1 --limit 20

工具会校验SHA-256；其他版本不能冒用此版行号。没有原文时仍可学习笔记，但不能核验精确原句或数值。行业数据、法律政策和厂商功能的现况须另查。

## 2026-11-12 修订

本次重读本地 OCR 可见文字并重写逐章决策卡、主题索引、速查和附录证据说明。原书、OCR 和图像仍不随包分发；精确引文需要使用者本人持有匹配来源。教学案例、报告估算与当前市场事实须分开使用。
