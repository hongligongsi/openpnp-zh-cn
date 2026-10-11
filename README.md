# openpnp-zh-cn

OpenPnP 简体中文全量汉化包 · 适用于 **OpenPnP 2.6**

> 在官方 OpenPnP 2.6 基础上完成 **全量中文汉化**，覆盖语言资源文件
> 与硬编码在 Java class 中的全部可见文案。

---

## 特性

| 项目 | 说明 |
|---|---|
| 汉化层数 | **两层**：语言资源文件 + class 常量池 |
| 翻译条目 | properties 1948 条 + class 常量池 **2240 条**（1913 条候选，100% 覆盖） |
| 改动 class | **497 个** |
| 交付形式 | 一个可直接替换的 JAR，或纯资源文件 |
| 许可 | GPL-3.0（与主程序一致，可自由分发） |

### 为什么需要「两层」汉化

官方自带的 `translations_zh_CN.properties` 只能覆盖用了 i18n 机制的部分。
而「**问题与解决方案**」（Issues & Solutions）面板文案、大量 GUI 标签、
错误提示、运行日志、算法参数说明等，**硬编码在 Java class 文件里**，
由代码运行时动态拼接生成，properties 完全无法触及。

本项目对这类字符串采用 **class 常量池就地重写** 的方式汉化：

```
Java class 常量池中 CONSTANT_Utf8(tag=1) = tag(1) + length(2) + bytes[length]
                                                                    ↑ 可原地重写
```

- 常量池 **条目数保持不变** → 所有索引引用无需改动
- 字节码偏移相对 `code[]` 起始 → **与常量池无关**
- 因此替换字符串数据是**完全安全**的

---

## 快速使用

### 方式一：直接用成品 JAR（最简单）

1. **完全退出** OpenPnP
2. 备份你自己的 `openpnp-gui-0.0.1-alpha-SNAPSHOT.jar`
3. 用本仓库的 JAR 覆盖：
   ```
   输出/class补丁/openpnp-gui-final.jar
     ↓ 改名为
   C:\Program Files\openpnp\openpnp-gui-0.0.1-alpha-SNAPSHOT.jar
   ```
4. 启动 OpenPnP

### 方式二：只替换语言资源文件

若你已有自己改过的 JAR，只想更新翻译文案，把
`输出/translations_zh_CN.properties` 拖进 JAR 的
`org/openpnp/translations_zh_CN.properties` 路径覆盖即可。

### 方式三：自行构建

```bash
# 1. 准备官方原版 JAR
# 2. 应用 properties 汉化 + class 常量池补丁
python 输出/class补丁/应用补丁.py

# 3. 校验（可选，强烈建议）
python 输出/class补丁/结构校验器.py <原版.jar> <输出.jar>
```

---

## 目录结构

```
├── 输出/                          # 交付物
│   ├── class补丁/
│   │   ├── openpnp-gui-final.jar      # ★ 最终成品 JAR
│   │   ├── 全量翻译映射表.json          # 1913 条中英对照
│   │   ├── 翻译映射表.py                # 首批 170 条对照
│   │   ├── class重写器.py               # 常量池重写器
│   │   ├── 翻译校验器.py                # 占位符安全校验
│   │   ├── 结构校验器.py                # class 结构完整性校验
│   │   └── 应用补丁.py                  # 一键应用
│   ├── translations_zh_CN.properties  # 语言资源文件
│   ├── 使用说明.md                     # 详细文档
│   └── SHA256.txt
├── 工作区/                        # 各批次翻译表与工具
│   ├── batch1_solutions.py ~ batch10_rest.py
│   ├── translation_pipeline.py
│   └── struct_verify.py
└── 备份/                          # 各阶段 JAR 备份（未入库）
```

---

## 质量保障

### 三重验证

| 验证项 | 方法 | 结果 |
|---|---|---|
| 结构完整性 | 按 class 规范逐字节解析 CP→字段→方法→属性 | 原始与补丁版均 **2104/2104 合法** |
| JVM 加载 | 逐 class `defineClass` 校验 | 两版均 `OK=1427 FAIL=677`，**失败清单逐条相同**（677 条全为第三方依赖缺失） |
| 字节级 diff | 逐文件比对原始与成品 JAR | 493 个条目差异 = 492 class + 1 properties，**全部为预期替换** |

### 占位符安全校验

每条译文强制校验与原串一致：

- `\x01` 占位符数量（OpenPnP 动态拼接用的 SOH 标记）
- `%s` / `%d` 等格式符
- `{}` 花括号数量

任何不符即**拒绝应用**。本项目实际拦截并修正了 1 条漏占位符的译文。

### 实机验证

启动 OpenPnP 后日志已中文化，确认补丁生效且无启动异常：

| 汉化前 | 汉化后 |
|---|---|
| `Bonjour to OpenPnP version 2.6_...` | `Bonjour，欢迎使用 OpenPnP 版本 2.6_...` |
| `No camera found with ID ... for camera Top` | `未找到 ID 为 ... 的相机（相机 Top）` |
| `Camera Top failed to return an image after 4 tries.` | `相机 Top 在 4 次尝试后仍未返回图像。` |

这些字符串全部来自 class 常量池，是补丁生效的直接证据。

---

## 刻意保留英文的部分

以下内容**不翻译**，因为翻译后会破坏功能或无法定位问题：

- **URL / 文件名 / 类名 / 属性名**
  （如 `ACTUATOR_READ_COMMAND`、`AdvancedCalibration.pipeline`）
- **G 代码指令本体**（`G28`、`G92.1`、`G90` 等字面量）
- **变量占位符与格式符**（`\x01`、`%s`、`{}`）

---

## 覆盖范围

| 包 | 条目数 | 内容 |
|---|---|---|
| `machine/reference/feeder/` | 293 | 供料器标签、向导、OCR/推拉/百叶盖板提示 |
| `gui/` | 264 | 主界面菜单、对话框、表格 |
| `machine/reference/`（根） | 166 | 吸嘴杆、基准点定位、贴装校验 |
| `vision/pipeline/` | 220 | 管线阶段说明、参数提示（含大量 HTML 长描述） |
| vendor（neoden4/pandaplacer/photon/rapidplacer） | 180 | 各厂商供料器与驱动器 |
| `solutions/` | 128 | 问题与解决方案面板 |
| `machine/reference/camera/` | 106 | 相机驱动、IP 相机、自动对焦、MJPG 流 |
| `machine/reference/wizards/` | 75 | 各配置向导 |
| `model/`、`util/`、`spi/` 等 | 353 | 配置读写、运动规划、脚本引擎 |
| 其他 | — | 剩余全部可见文案 |

---

## 校验值

```
文件:   openpnp-gui-final.jar
大小:   11,135,052 字节
SHA256: 11e7c698a351fccdcaa6c4728e5908c000b5c2365fada61b353b5625193f4af4

文件:   translations_zh_CN.properties
大小:   240,295 字节
SHA256: 2515beae509b49a2dce6bec21f824914ac2884163a40bb0d3bf45ece62550c15
```

---

## 来源与许可

- 主程序源码：https://github.com/openpnp/openpnp （**GPL-3.0**）
- 官方下载页：https://openpnp.org/downloads/
- 语言资源目录：`src/main/resources/org/openpnp/`

本汉化包是官方资源的完整版 + 补充翻译，依 **GPL-3.0** 自由分发。
OpenPnP 版权归其原作者与贡献者所有。

---

## 还原

仓库未收录原始 JAR 备份（体积原因）。如需还原为官方原版，
请从 [openpnp.org/downloads](https://openpnp.org/downloads/) 重新下载安装。

若你之前按本项目文档操作过，本地 `备份/` 目录应存有：

| 文件 | 内容 |
|---|---|
| `.jar.bak` | 原始官方版 |
| `.jar.bak2` | 仅 properties 汉化 |
| `.jar.bak3` | + 首批 170 条 class 补丁 |
