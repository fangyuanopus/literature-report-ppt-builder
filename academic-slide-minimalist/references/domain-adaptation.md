# Domain Adaptation

Use this reference to adapt the default paper-to-PPT structure to the scientific domain while keeping the user's sample deck rhythm.

## Core Rule

Do not force all papers into the same result-page order. Keep the top-level sections fixed, but adapt the result evidence chain to the paper type.

## Materials / Chemistry Papers

Typical result chain:

```text
synthesis/design -> phase/structure -> morphology -> composition/active site -> property -> performance -> stability -> mechanism/discussion
```

Key checks:

- sample names and preparation conditions;
- structural evidence versus property evidence;
- whether mechanism is proven or proposed;
- whether performance comparison uses fair conditions.

## Catalysis Papers

Typical result chain:

```text
catalyst design -> active-site evidence -> reaction condition -> conversion/selectivity -> comparison -> stability/reuse -> mechanism/substrate scope
```

Key checks:

- conversion, selectivity, yield, TON/TOF definitions;
- reaction temperature, solvent, time, substrate/catalyst ratio;
- deactivation and recycling;
- whether active site assignment is direct or inferred.

## Porous Materials / Adsorption / Separation Papers

Typical result chain:

```text
structure -> pore size/surface area -> adsorption isotherm -> selectivity/separation -> stability -> application scenario
```

Key checks:

- adsorption vs absorption terminology;
- units and measurement temperature;
- pore size distribution method;
- whether performance is predicted, measured, or simulated.

## Food / Polymer / Biomaterial Papers

Typical result chain:

```text
composition/formulation -> structure/property -> functional performance -> mechanism -> application/reliability
```

Key checks:

- experimental groups and controls;
- statistical significance;
- test conditions;
- whether application claims exceed lab-scale evidence.

## Computational / Theoretical Papers

Typical result chain:

```text
model/question -> assumptions -> method -> validation -> key result -> interpretation -> limitation
```

Key checks:

- assumptions and boundary conditions;
- model validation;
- whether the conclusion is simulated or experimentally verified.

## Use in Page Planning

When creating `slide_outline.md`, choose the domain chain that best matches the paper. If multiple domains apply, combine them but keep the page order logical and evidence-led.


## Domain-Specific Navigation Suggestions

Use these suggestions with `adaptive-navigation.md`.

```text
catalysis/materials: 基本信息 | 研究背景 | 设计策略 | 性能验证 | 结构证据 | 机理解释 | 总结启发 | Backup
porous materials: 基本信息 | 研究背景 | 结构构筑 | 孔道表征 | 吸附分离 | 稳定验证 | 总结启发 | Backup
food/biomaterials: 基本信息 | 研究背景 | 材料构建 | 结构表征 | 功能性质 | 应用验证 | 总结启发 | Backup
biology/mechanism: 基本信息 | 科学问题 | 实验设计 | 表型验证 | 机制解析 | 应用意义 | 总结启发 | Backup
algorithm/AI: 基本信息 | 任务背景 | 方法框架 | 实验结果 | 消融分析 | 泛化验证 | 总结启发 | Backup
computational: 基本信息 | 问题设定 | 模型方法 | 结果验证 | 机理解释 | 局限讨论 | 总结启发 | Backup
```

These are examples, not fixed templates. Choose labels that best help the audience follow the specific paper.
