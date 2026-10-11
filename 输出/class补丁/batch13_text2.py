# -*- coding: utf-8 -*-
"""batch13_text2.py — 残留可见文案第二批（TEXT 类剩余部分）。"""

TABLE = {

# ---- 直线/状态机/图形 ----
'    %s -> %s [ label = %s ];\n': '    %s -> %s [ label = %s ];\n',
'FIRMWARE_NAME:GcodeServer, FIRMWARE_URL:http%3A//openpnp.org, X-SOURCE_CODE_URL:https%3A//github.com/openpnp/openpnp, FIRMWARE_VERSION:§, X-FIRMWARE_BUILD_DATE:Oct 23 2020 00:00:00': 'FIRMWARE_NAME:GcodeServer, FIRMWARE_URL:http%3A//openpnp.org, X-SOURCE_CODE_URL:https%3A//github.com/openpnp/openpnp, FIRMWARE_VERSION:§, X-FIRMWARE_BUILD_DATE:Oct 23 2020 00:00:00',

# ---- 真实日志文案 ----
'[FeederVisionHelper] calibrated hole locations are: §, §': '[FeederVisionHelper] 校准后的孔位置为：§, §',

# ---- 更多界面文本 ----
'X:%-9s Y:%-9s Z:%-9s C:%-9s': 'X:%-9s Y:%-9s Z:%-9s C:%-9s',
'(%f, %f, %f, %f %s)': '（%f, %f, %f, %f %s）',
'    +-- prop:%s %s @%08x': '    +-- 属性:%s %s @%08x',
'Placement %s @%08x defined by @%08x, location=%s, side=%s, part=%s, type=%s, rank=%s': '贴装 %s @%08x 由 @%08x 定义，location=%s，side=%s，part=%s，type=%s，rank=%s',
'%s (%s) BoardLocation:@%08x defined by @%08x child of @%08x, %s, location=%s globalLocation=%s, side=%s (%s)': '%s (%s) BoardLocation:@%08x 由 @%08x 定义，@%08x 的子项，%s，location=%s globalLocation=%s，side=%s (%s)',
'id %s, name %s, heightUnits %s, height %f, packageId (%s)': 'id %s，name %s，heightUnits %s，height %f，packageId (%s)',
'%s (%s) PanelLocation:@%08x defined by @%08x child of @%08x, %s, location=%s , globalLocation=%s side=%s (%s)': '%s (%s) PanelLocation:@%08x 由 @%08x 定义，@%08x 的子项，%s，location=%s ，globalLocation=%s side=%s (%s)',

# ---- 解析统计 ----
'%s Total %3.0f%% (%4d/%4d), Flash %3.0f%% (%4d/%4d), Line %3.0f%% (%4d/%4d), Arc %3.0f%% (%4d/%4d), Region %3.0f%% (%4d/%4d), Region line %3.0f%% (%4d/%4d), Region Arc %3.0f%% (%4d/%4d), Pads %4d': '%s 合计 %3.0f%% (%4d/%4d)，Flash %3.0f%% (%4d/%4d)，Line %3.0f%% (%4d/%4d)，Arc %3.0f%% (%4d/%4d)，Region %3.0f%% (%4d/%4d)，Region line %3.0f%% (%4d/%4d)，Region Arc %3.0f%% (%4d/%4d)，Pads %4d',
'%dpx, %dpx\n%2.3f%s, %2.3f%s': '%dpx, %dpx\n%2.3f%s, %2.3f%s',

# ---- 运行时/Java 内部（保留结构，仅译说明部分） ----
'rundll32 url.dll,FileProtocolHandler §': 'rundll32 url.dll,FileProtocolHandler §',
'{try {return java.beans.Introspector.getBeanInfo($1.getClass());} catch (java.beans.IntrospectionException ie) {throw new org.jdesktop.beansbinding.PropertyResolutionException("Exception while introspecting " + $1.getClass().getName(), ie);} }': '{try {return java.beans.Introspector.getBeanInfo($1.getClass());} catch (java.beans.IntrospectionException ie) {throw new org.jdesktop.beansbinding.PropertyResolutionException("在 introspect " + $1.getClass().getName() + " 时发生异常", ie);} }',

# ---- ReferenceNozzle 调试 ----
'{}.toHeadLocation({}, ...) rotation mode offset {}': '{}.toHeadLocation({}, ...) 旋转模式偏移 {}',
'{}.home() nozzle tip {} calibration neeeded': '{}.home() 吸嘴头 {} 需要校准',
'{}.loadNozzleTip({}): moveTo Start Location': '{}.loadNozzleTip({})：移动到起始位置',
'{}.loadNozzleTip({}): moveTo Mid Location': '{}.loadNozzleTip({})：移动到中间位置',
'{}.loadNozzleTip({}): moveTo Mid Location 2': '{}.loadNozzleTip({})：移动到中间位置 2',
'{}.loadNozzleTip({}): moveTo End Location': '{}.loadNozzleTip({})：移动到结束位置',
'{}.loadNozzleTip({}): moveTo manual Location': '{}.loadNozzleTip({})：移动到手动位置',
'{}.loadNozzleTip() nozzle tip {} calibration reset': '{}.loadNozzleTip() 吸嘴头 {} 校准已重置',
'{}.loadNozzleTip() nozzle tip {} calibration needed': '{}.loadNozzleTip() 吸嘴头 {} 需要校准',
'{}.unloadNozzleTip(): moveTo End Location': '{}.unloadNozzleTip()：移动到结束位置',
'{}.unloadNozzleTip(): moveTo Mid Location 2': '{}.unloadNozzleTip()：移动到中间位置 2',
'{}.unloadNozzleTip(): moveTo Mid Location': '{}.unloadNozzleTip()：移动到中间位置',
'{}.unloadNozzleTip(): moveTo Start Location': '{}.unloadNozzleTip()：移动到起始位置',
'{}.unloadNozzleTip({}): moveTo manual Location': '{}.unloadNozzleTip({})：移动到手动位置',
'{}.unloadNozzleTip() nozzle tip {} calibration needed': '{}.unloadNozzleTip() 吸嘴头 {} 需要校准',

# ---- 其他 ----
'§§ § has Vision Offsets §, §, compositing unsupported. ': '§§ § 含有视觉偏移 §、§，不支持组合。',
'{Acceleration:M204 S%.2f ; Initialize acceleration}\n': '{Acceleration:M204 S%.2f ; 初始化加速度}\n',

}
