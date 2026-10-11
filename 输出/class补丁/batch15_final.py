# -*- coding: utf-8 -*-
"""batch15_final.py — 收尾：审计发现的最后一批可见文案。"""

TABLE = {

# ---- 真正面向用户的文案 ----
'§ no matches found.': '§ 未找到匹配项。',
'§ changed.  Apply changes?': '§ 已更改。要应用更改吗？',
'§ Switch Linear ↔ Rotational.': '§ 切换直线 ↔ 旋转。',
'§; Home all axes\n': '§; 全轴归位\n',
'(Not yet supported)': '（尚不支持）',
'OCR changed parts: ': 'OCR 已更换元件：',

# ---- 流水线阶段校验（用户在管线编辑器里会看到） ----
'modelStageName is required.': '必须指定 modelStageName。',
'propertyName is required.': '必须指定 propertyName。',
'contoursStageName is required.': '必须指定 contoursStageName。',

# ---- 视觉设置提示（HTML，会显示在 Issues & Solutions 里） ----
'<p>The settle time is rather large, perhaps due to excessive machine vibration. Try setting stricter X/Y axes acceleration or jerk limits (if supported).</p><br/>':
'<p>稳定时间偏长，可能是机器振动过大所致。请尝试设置更严格的 X/Y 轴加速度或加加速度限制（若支持）。</p><br/>',

# ---- 日志中的英文短语（用户可在“运行日志”看到） ----
'Found {} on {} at {}': '在 {} 上的 {} 处找到 {}',
'Looking for {} at {}': '正在 {} 处查找 {}',
'    tMin not met': '    未满足 tMin',
'    retimed tMin § time §': '    已对 tMin § 重新计时 §',
'    max time § from §': '    最大时间 § 来自 §',
'[nozzleTipCalibration]measured offset: {}': '[nozzleTipCalibration] 测得偏移：{}',
'[nozzleTipCalibration] Unrecognized result §': '[nozzleTipCalibration] 无法识别结果 §',
'[nozzleTipCalibration]calculated nozzleEccentricity: {}': '[nozzleTipCalibration] 计算出的吸嘴偏心度：{}',
'[§] rescale of input = §': '[§] 输入缩放比 = §',
'definition: § changedItem: § source: §': '定义：§ 变更项：§ 来源：§',
'errorCount = {}, max allowed = {}': '错误数 = {}，最大允许 = {}',
'imgSetGain() [cameraId:%d, gain:%d]': 'imgSetGain() [cameraId:%d, gain:%d]',
'{}.toHeadLocation({}, ...) runout compensation {}': '{}.toHeadLocation({}, ...) 偏心补偿 {}',
'Align {} with {}, offsets {}': '将 {} 与 {} 对齐，偏移 {}',
'Placement {} has rank {}': '贴装 {} 的等级为 {}',
'Optimised: {} rank {} from {}': '已优化：{} 等级 {} 来自 {}',
'autoSettleAndCapture in {} ms': 'autoSettleAndCapture 耗时 {} ms',
'[{}] disconnectRequested, bye-bye.': '[{}] 已请求断开连接，再见。',
'§ $-command, waiting §ms': '§ $-命令，等待 §ms',
'{}.setFeedCount(): feedCount {}, pickLocation {}': '{}.setFeedCount()：feedCount {}，pickLocation {}',
'convertLength() unrecognized units §': 'convertLength() 无法识别的单位 §',
'[BlindsFeeder.isCoverOpenChecked] pocketPosition: {}，pocketDistance {}，error {}': '[BlindsFeeder.isCoverOpenChecked] pocketPosition：{}，pocketDistance：{}，error：{}',

# ---- 解析器显示名（下拉框/导入对话框可见） ----
'EAGLE mountsmd.ulp': 'EAGLE mountsmd.ulp 文件',
'Labcenter Proteus .pkp': 'Labcenter Proteus .pkp 文件',

}
