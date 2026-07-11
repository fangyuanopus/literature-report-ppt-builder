# Literature Report PPT Builder

把论文主线、真实图源和可讲的结论组织成中文文献汇报 PPT。项目的当前入口是 [academic-slide-pragmatic-fallback](skills/academic-slide-pragmatic-fallback/SKILL.md)。

[English](docs/README.en.md) | 中文

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue)](skills/academic-slide-pragmatic-fallback/SKILL.md)
[![Template](https://img.shields.io/badge/template-editable_PPTX-orange)](skills/academic-slide-pragmatic-fallback/assets/sample-literature-report.pptx)

核心原则：**真实证据优先；明确交付路线；不把代码输出冒充成 Image2，也不把 Image2 输出冒充成可编辑模板。**

## 先选交付路线

| 路线 | 产物与定位 | 是否可编辑 | 适用条件 |
| --- | --- | --- | --- |
| A. GPT-image-2 / Image2 全页路线 | 每页为已验收的整页图像，再封装进 PPTX；视觉自由度最高 | 页面内容通常不可逐对象编辑 | 已确认可用的全页 Image2 后端，并能忠实保留论文图裁图 |
| B. 精确模板代码路线 | 直接继承内置 PPT 模板的母版、导航、页脚和文本/图片槽位，替换为当前论文内容 | 是 | 用户明确要求复刻内置模板，并接受固定导航语义 |
| C. 实用代码 fallback | 从空白页按内置红黑灰风格生成可编辑页面 | 是 | 没有可用 Image2，也没有适合继承的干净模板 |

三条路线都只允许使用论文主文、SI 或用户提供的科学图。不会生成、重绘或语义篡改实验数据图、谱图、显微图、结构图、表格或机理图。

## 两组示例，分别代表两条路线

### GPT-image-2 / Image2 全页视觉示例

以下四页是此前用 GPT-image-2 / Image2-style 全页路线制作的视觉示例。它们用于展示整页图像式交付的视觉上限；不代表代码模板输出，也不承诺对象级编辑。

![Image2 示例封面](docs/images/demo-slide-01-title.jpg)
![Image2 示例证据页](docs/images/demo-slide-02-evidence.jpg)
![Image2 示例对比页](docs/images/demo-slide-03-comparison.jpg)
![Image2 示例总结页](docs/images/demo-slide-04-summary.jpg)

### 代码生成：精确继承模板的可编辑示例

以下页面来自本仓库当前代码路线的真实运行：以油茶籽油水酶法论文图为输入，继承内置模板对象，替换文本、真实图表与图注，并通过构建、结构和模板保真三项审计。它不是 GPT-image-2 输出。

![代码路线六页总览](docs/images/demo-code-template-overview.png)

![代码路线：模板继承 + 真实柱状图](docs/images/demo-code-template-evidence.png)

![代码路线：完整响应面图 + 继承段落强调](docs/images/demo-code-template-response-surface.png)

这组截图展示的是代码能力边界：模板的导航、标题、边距、页脚、段落和红色强调 run 来自原 PPT；论文图来自原始 PDF 的确定性裁取。为避免把论文图源作为仓库素材再分发，仓库保留预览图而不打包这份测试论文的完整 PPTX。

## 代码路线可以稳定完成什么

在当前内置模板和真实图源齐备的前提下，代码路线可以稳定完成：

- 选择并重排不同的模板源页，保留对应的母版、导航、标题、页脚和留白节奏；
- 原位替换文本、图注、图片和多段正文，保留原段落与黑色/红色强调 run 的样式；
- 对论文 PDF 图进行确定性渲染、裁边、等比放置和可读性检查；
- 清理被替换图片的旧关系、旧演讲者备注、旧分节、未使用母版/版式及旧文档元数据；
- 生成可编辑 PPTX，并执行构建报告、结构审计、模板保真审计和逐页预览。

当前不承诺或主动拒绝：

- 在没有模板的情况下，靠坐标代码像素级复刻任意未知 PPT；
- 复制同一模板源页来无限扩展页数（当前稳定实现要求每页映射不同的源页）；
- 把用户任意复杂 PPT、锁定对象或未知母版自动改造成精确模板；
- 生成、补全或重绘科学数据图；
- 把 Image2 的整页位图交付说成对象级可编辑 PPT。

Route C 可以稳定生成干净、可编辑的红黑灰学术页面，但它只遵循样例的视觉语法，不应称为“精确复刻模板”。

## 怎么调用

### 默认：让 skill 自己选择路线

```text
使用 academic-slide-pragmatic-fallback，把这篇论文和 SI 制作成中文文献汇报 PPT。
只使用真实论文图；先给出证据链与页面顺序；若 Image2 不可用，先征得我同意再选择模板代码路线或实用代码 fallback。
```

### 要求 GPT-image-2 / Image2 整页交付

```text
使用 academic-slide-pragmatic-fallback，并使用已确认可用的 GPT-image-2 / Image2 全页后端生成 PPT。
每页保留真实论文图裁图，输出 image2_manifest.json 和 image-only 验证结果。
```

### 要求复刻内置模板并保持可编辑

```text
使用 academic-slide-pragmatic-fallback 的精确模板代码路线。
按内置 sample-literature-report.pptx 继承对象生成可编辑 PPT；替换所有旧论文内容；使用真实论文图；完成结构审计、模板保真审计和逐页预览。
```

## 精确模板代码路线的质量门槛

精确模板模式必须同时满足：

1. `build_fallback_template_pptx.py --strict --fail-on-warnings` 通过；
2. `audit_fallback_template_pptx.py --check-masters --exact-template --fail-on-review` 通过；
3. `audit_exact_template_fidelity.py --plan ... --build-report ... --fail-on-review` 通过；
4. 每页渲染预览与源模板对照，确认导航、标题、边距、页脚、图框和留白没有漂移；
5. PPTX 内没有旧论文图片、备注、分节、未使用母版/版式、重复 ZIP 部件或过期文档元数据。

## 安装

### Codex

```bash
git clone https://github.com/fangyuanopus/literature-report-ppt-builder.git
cp -R literature-report-ppt-builder/skills/academic-slide-pragmatic-fallback \
  ~/.codex/skills/academic-slide-pragmatic-fallback
```

重启 Codex 会话后即可按自然语言调用。

### Claude Code

```bash
git clone https://github.com/fangyuanopus/literature-report-ppt-builder.git
mkdir -p ~/.claude/skills
cp -R literature-report-ppt-builder/skills/academic-slide-pragmatic-fallback \
  ~/.claude/skills/academic-slide-pragmatic-fallback
```

## 输出与可追溯性

复杂任务至少维护以下文件：

```text
deck_order_map.md
figure_source_manifest.md
page_briefs.md
fallback_edit_plan.json
prepared_figure_manifest.json
fallback_build_report.json
structural_audit.json
fidelity_audit.json
rendered_slides/
contact_sheet.png
final_presentation.pptx
```

Image2 路线还需要 `image2_manifest.json`；代码路线则需要模板槽位清单、构建报告与两类审计报告。不要混用这两组验证声明。

## 仓库结构

```text
skills/
  academic-slide-pragmatic-fallback/   # 当前维护的入口：Image2、精确模板与实用代码 fallback
    SKILL.md
    assets/sample-literature-report.pptx
    scripts/
      build_fallback_template_pptx.py
      audit_fallback_template_pptx.py
      audit_exact_template_fidelity.py
      build_pragmatic_fallback_pptx.py
docs/
  images/
    demo-slide-*.jpg                   # GPT-image-2 / Image2 全页视觉示例
    demo-code-template-*.png           # 代码生成、模板继承示例
academic-slide-minimalist/             # 兼容性保留的旧入口；不再代表当前代码路线
```

## 致谢

- [JuneYaooo/gpt-image2-ppt-skills](https://github.com/JuneYaooo/gpt-image2-ppt-skills)
- [LINUX DO](https://linux.do/)
