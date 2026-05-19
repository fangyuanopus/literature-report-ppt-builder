# Literature Report PPT Builder Skill

用于从论文、补充信息和真实来源图像中，构建严谨学术文献汇报 PPT 的开源 Codex Skill。

本项目内置的 Skill 为 `academic-slide-minimalist`，主要面向中文学术论文汇报、Journal Club、毕业论文答辩风格汇报，以及以整页图片为核心的 PPT 生成流程。它适合对版式稳定性、科研图像可追溯性和汇报逻辑完整性要求较高的场景。

## 功能介绍

该 Skill 可以：

- 将主论文与补充信息作为一个完整的证据系统进行阅读与分析；
- 在生成幻灯片前，构建论文逻辑图、图像来源清单、自适应导航结构和逐页页面简报；
- 使用论文、补充信息或用户提供材料中的真实图像，生成 16:9 的图片式 PPT 页面；
- 参考内置样例 PPT 的页面节奏，保持克制、稳定、学术化的视觉风格；
- 对页面顺序、图像可读性、术语一致性和汇报准备度进行检查。

## 不可违反的规则

所有科学图像必须来自真实来源材料。

该 Skill 明确禁止凭空创造、重新生成或重画实验图像、分子结构、谱图、反应机理、图表、数据表格或其他科研数据。

允许的视觉操作仅限于确定性的版式处理，例如：

- 裁剪；
- 缩放；
- 对齐；
- 遮盖边缘空白；
- 添加标注框；
- 添加箭头；
- 添加标签；
- 整页排版。

## 项目结构

```text
academic-slide-minimalist/
  SKILL.md
  agents/openai.yaml
  assets/sample-literature-report.pptx
  references/
```

`SKILL.md` 包含核心工作流程。

`references/` 文件夹提供分阶段的补充指导，包括精读论文、自适应导航、页面顺序规划、逐页简报、图像一致性检查、质量门槛和最终交付检查等内容。

`assets/sample-literature-report.pptx` 仅作为版式风格和页面节奏参考，不是科研证据来源，也不应被复用为新论文的科学材料。

## 安装方法

将 Skill 文件夹复制到 Codex skills 目录中：

```powershell
Copy-Item -Recurse .\academic-slide-minimalist "$env:USERPROFILE\.codex\skills\academic-slide-minimalist"
```

然后启动一个新的 Codex 会话，使 Skill 元数据能够被发现。

## 示例提示词

```text
Use the academic-slide-minimalist skill to turn this paper and SI into a 20+ page Chinese literature-report PPT.
```

```text
按照这份样例 PPT 的节奏，帮我重构这篇论文的文献汇报，要求只使用论文真实图片。
```

```text
先诊断我这个已有文献汇报 PPT 的问题，再给出需要重画的页面清单。
```

## 验证方法

如果可用，可以使用 Codex Skill 验证脚本进行检查：

```powershell
$env:PYTHONUTF8 = "1"
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\academic-slide-minimalist
```

##  社区
- [LINUX DO](https://linux.do/)

本项目认可并感谢 LINUX DO 社区在中文开发者开源交流、项目分享和技术讨论中的价值。除非社区另有明确说明，此处仅为社区致谢和链接，不代表官方背书。

## License

MIT License. See LICENSE.
