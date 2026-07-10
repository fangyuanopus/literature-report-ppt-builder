# Adaptive Navigation

Use this reference before creating `slide_outline.md`, `deck_order_map.md`, page briefs, or image2 pages.

## Core Rule

Do not hard-code one navigation bar for every paper. The sample deck teaches navigation style, not universal section names. Derive navigation labels from the current paper's domain, argument structure, and evidence chain.

Default fallback only:

```text
基本信息 | 研究背景 | 研究思路 | 研究结果 | 总结启发 | Backup
```

Use the fallback only when the paper has no clearer structure. If the results are long, split them into meaningful evidence sections.

## Navigation Derivation Workflow

1. Identify paper type:
   - catalysis / materials chemistry;
   - porous materials / adsorption / separation;
   - food / polymer / biomaterials;
   - biology / medicine / mechanism study;
   - algorithm / method / AI;
   - computational / theoretical;
   - review / perspective.
2. Extract the story axis:
   - what is the unresolved problem?
   - what is the strategy or method?
   - what evidence proves it?
   - where do performance, structure, mechanism, application, and limitation appear?
3. Generate 5-8 concise Chinese navigation labels.
4. Ensure each label covers a continuous page range. Do not create one navigation item for a single ordinary page unless it is a special opening/closing state.
5. Put `Backup` as the final navigation state when backup slides exist.
6. Apply the same labels and order to every image2 page in that deck.

## Useful Navigation Patterns

### Catalysis / Materials

```text
基本信息 | 研究背景 | 设计策略 | 性能验证 | 结构证据 | 机理解释 | 总结启发 | Backup
```

### Mechanism-heavy science paper

```text
基本信息 | 科学问题 | 现象发现 | 证据链 | 机制模型 | 理论解释 | 总结启发 | Backup
```

### Food / Biomaterial / Functional Material

```text
基本信息 | 研究背景 | 材料构建 | 结构表征 | 功能性质 | 应用验证 | 总结启发 | Backup
```

### Algorithm / AI / Method Paper

```text
基本信息 | 任务背景 | 方法框架 | 实验结果 | 消融分析 | 泛化验证 | 总结启发 | Backup
```

### Computational / Theoretical Paper

```text
基本信息 | 问题设定 | 模型方法 | 结果验证 | 机理解释 | 局限讨论 | 总结启发 | Backup
```

## Section Naming Rules

Prefer short labels: usually 2-4 Chinese characters, or a concise phrase when necessary.

Good:

```text
设计策略 | 性能验证 | 结构证据 | 机理解释 | 应用验证
```

Weak:

```text
研究结果一 | 研究结果二 | 研究结果三
```

Avoid:

- forcing every deck into `研究结果` if the result section has multiple major evidence layers;
- copying the sample deck's exact labels when the current paper needs more precise labels;
- changing navigation labels between pages;
- using long navigation labels that crowd the top bar.

## Required Output

Create or internally maintain:

```text
adaptive_navigation_plan.md
```

Template:

```text
paper domain:
main story axis:
navigation labels:
- label | page range | purpose | notes
backup state:
reason for this navigation:
```

Then copy the chosen labels into `deck_order_map.md` and every page brief.

## Additional Domain Examples

Use `navigation-examples-by-domain.md` for additional candidate navigation patterns. Treat those examples as a menu, not as fixed templates.
