# -*- coding: utf-8 -*-
"""问题与解决方案面板 class 常量池中文补丁映射表。
规则：只替换常量池中的 UTF-8 字符串字面量；保持 <html> 标记、\x01 占位符、%d/%s 格式符不变。
"""

# 完整字符串替换（静态文本，无参数）
FULL = {
 # --- 机器状态 ---
 "To continue, the machine must be enabled and homed.": "请先启用并归位（Home）机器，然后继续。",
 "Home the machine now.": "立即归位（Home）机器。",
 "Machine is not enabled and homed.": "机器未启用或未归位。",
 "machine is disabled": "机器已禁用",
 "machine is disabled": "机器已禁用",

 # --- 吸嘴 / 零件直径 ---
 "Nozzle tip \x01 has an invalid Min. Part Diameter of \x01.": "吸嘴 \x01 的最小零件直径无效，当前为 \x01。",
 "Nozzle tip \x01 has a Max. Part Diameter that is not larger than the Min. Part Diameter.":
   "吸嘴 \x01 的最大零件直径未大于最小零件直径。",
 "Make the Min. Part Diameter at least as big as the nozzle tip air bore plus two times the Max. Pick Tolerance of \x01. Press the blue info button (below) for more information.":
   "请将最小零件直径设置为至少「吸嘴气孔 + 2 倍最大取料公差(\x01)」的大小。点击下方蓝色信息按钮可了解更多。",
 "Make sure the Max. Part Diameter is larger than the Min. Part Diameter. Press the blue info button (below) for more information.":
   "请确保最大零件直径大于最小零件直径。点击下方蓝色信息按钮可了解更多。",
 "Set background calibration method for \x01.": "为 \x01 设置背景校准方法。",
 "Depending on the type of nozzle tip or shade, select the proper background calibration.":
   "请根据吸嘴嘴头或遮罩的类型，选择合适的背景校准。",
 "Set the Max. Pick Tolerance to the actual pick errors you expect. Press the blue info button (below) for more information.":
   "请将最大取料公差设置为实际预期的取料误差。点击下方蓝色信息按钮可了解更多。",
 "Nozzle Offset Calibration": "吸嘴偏移校准",
 "Nozzle Offset Calibration ": "吸嘴偏移校准 ",
 "Center Nozzle": "居中吸嘴",

 # --- 相机校准 ---
 "Advanced camera \x01 calibration.": "相机 \x01 高级校准。",
 "Automatically calibrates the camera \x01 using the primary and secondary calibration fiducials.":
   "使用主、副校准基准点自动校准相机 \x01。",
 "Automatically calibrates the camera \x01 using the nozzle \x01.": "使用吸嘴 \x01 自动校准相机 \x01。",
 "Primary Fiducial & Camera Calibration": "主基准点与相机校准",
 "Primary calibration fiducial position and initial camera calibration.": "主校准基准点位置与初始相机校准。",
 "Camera Positional Calibration": "相机位置校准",
 "Secondary Fiducial Calibration": "副基准点校准",
 "Secondary calibration fiducial position.": "副校准基准点位置。",
 "Primary/secondary calibration fiducial Z too close together.": "主/副校准基准点的 Z 高度太接近。",
 "Move the camera over the primary calibration fiducial and capture its position.":
   "将相机移到主校准基准点上方，并采集其位置。",
 "Move the camera over the secondary calibration fiducial and capture its position.":
   "将相机移到副校准基准点上方，并采集其位置。",
 "Determine the camera head offsets.": "测量相机头部偏移。",
 "Adjust the feature diameter that should be detected.": "调整需要识别的特征直径。",
 "Cycle to the next auto-detected contour": "切换到下一个自动识别的轮廓",
 "Camera Positional Calibration ": "相机位置校准 ",

 # --- 白平衡 / 渲染 ---
 "Calibrate static white balance for camera \x01.": "为相机 \x01 校准静态白平衡。",
 "For best results with color-keyed computer vision, it is recommended to use static white balance.":
   "为使颜色识别视觉达到最佳效果，建议使用静态白平衡。",
 "revert to the default setting. Issues & Solutions will propose calibrating static white balance instead":
   "恢复为默认设置。问题与解决方案将改为建议校准静态白平衡。",
 "revert to the default setting": "恢复为默认设置",
 "white balance": "白平衡",
 "Auto Exposure": "自动曝光",
 "The preview rendering quality can be improved.": "预览渲染质量可以提升。",
 "Set to Rendering Quality to High (right click the Camera View to see other options).":
   "将渲染质量设为「高」（右键点击相机视图可查看其他选项）。",
 "A high Preview FPS value might create undue CPU load.": "过高的预览帧率可能造成不必要的 CPU 负载。",
 "Set to 5 FPS.": "设为 5 FPS。",

 # --- 轴 / 运动控制 ---
 "Align nozzle \x01 rotation with part.": "将吸嘴 \x01 的旋转与零件对齐。",
 "Enable part aligned nozzle rotation mode, so camera view cross-hairs and DRO-coordinates show the bottom vision aligned part rotation instead of the unadjusted nozzle rotation.":
   "启用「零件对齐吸嘴旋转模式」，使相机视图的十字准线与 DRO 坐标显示底部视觉对齐后的零件旋转，而非未调整的吸嘴旋转。",
 "Pre-rotate bottom vision must be enabled, because the machine has a limited articulation nozzle.":
   "由于机器使用有限关节吸嘴，必须启用底部视觉预旋转。",
 "Pre-rotate bottom vision must be allowed on all vision settings, because the machine has a limited articulation nozzle.":
   "由于机器使用有限关节吸嘴，所有视觉设置都必须允许底部视觉预旋转。",
 "Enable Pre-Rotate.": "启用预旋转。",
 "Rotation cannot be wrapped-around on a limited articulation axis.": "有限关节轴无法进行旋转环绕。",
 "Rotation must be limited on a limited articulation axis.": "有限关节轴必须限制旋转范围。",
 "Rotation can be optimized by wrapping-around the shorter way. Best combined with Limit ±180°.":
   "可通过「沿较短路径环绕」优化旋转，建议与限定 ±180° 配合使用。",
 "Rotation can be optimized by limiting angles to ±180°. Best combined with Wrap Around.":
   "可通过将角度限定在 ±180° 优化旋转，建议与环绕配合使用。",
 "Enable Wrap Around.": "启用环绕。",
 "Disable Wrap Around.": "禁用环绕。",
 "Enable Limit to Range.": "启用范围限制。",
 "Axis is not assigned to a driver.": "轴未分配驱动器。",
 "Axis letter is missing. Assign the letter to continue.": "缺少轴字母。请指定字母后继续。",
 "Axis letter must not be empty": "轴字母不能为空",
 "Axis letter as used in G-code sent to the controller.": "发送给控制器的 G-code 中所用的轴字母。",
 "Axis Letter": "轴字母",
 "Please assign a proper Z axis. You might need to create one first.": "请指定正确的 Z 轴，可能需要先创建一个。",
 "Please assign a proper Rotation axis. You might need to create one first.":
   "请指定正确的旋转轴，可能需要先创建一个。",
 "Please assign a different Z axis.": "请指定其他 Z 轴。",
 "Please assign the correct controller axis letter. Choose from the list or enter a custom letter (some contoller may support an extended range of letters).":
   "请指定正确的控制器轴字母。可从列表中选择，或输入自定义字母（部分控制器可能支持更多字母）。",
 "Assign the unique axis letter where wrong, press Accept, then press Find Issues & Solutions again to clear the correct one.":
   "在错误处指定唯一的轴字母，点击「接受」，然后再次点击「查找问题与解决方案」以清除正确的那一个。",
 "Avoid axis letter E, if possible. Use proper rotation axes instead.":
   "如有可能，避免使用轴字母 E，请改用正确的旋转轴。",
 "Assign a driver as described in the Wiki.": "按 Wiki 说明分配驱动器。",
 "Assign a driver.": "分配驱动器。",
 "Connect the driver to your controller.": "将驱动器连接到控制器。",
 "Axis should be treated as a linear for detected firmware (all-primary axes mode).":
   "对于检测到的固件，该轴应按直线轴处理（全主轴模式）。",
 "Axes should be configured as linear in feedrate calculations on the RepRapFirmware controller. See the linked web page.":
   "在 RepRapFirmware 控制器上，进给率计算时轴应配置为直线轴。请参阅链接的网页。",
 "Remove driver Maximum Feed Rate.": "移除驱动器最大进给率限制。",
 "Axis velocity limited by driver Maximum Feed Rate. ": "轴速度受驱动器最大进给率限制。 ",
 "Feed-rate, acceleration, jerk etc. can now be set individually per axis.":
   "进给率、加速度、加加速度（Jerk）等现在可按轴单独设置。",
 "It is OK to share rotation axes. If intentional, just dismiss this issue. Otherwise assign a different Rotation axis.":
   "共用旋转轴是可以的。若为有意为之，忽略此问题即可；否则请指定不同的旋转轴。",
 "Check axis letters and make sure use a proper 6-axis configuration without extruders.":
   "请检查轴字母，确保使用不含挤出机的正确 6 轴配置。",
 "Check axis letters and make sure the controller is capable to use extra axes (i.e. not extruders).":
   "请检查轴字母，确保控制器能够使用额外轴（即非挤出机）。",
 "Check if your controller supports proper axes A B C (etc.) instead of \"extruder\" E. Press the blue info button (below) for more information.":
   "请检查控制器是否支持以 A B C 等正确轴代替「挤出机」E。点击下方蓝色信息按钮可了解更多。",
 "$H ; Home all axes": "$H ; 归位所有轴",
 "G21 ; Set millimeters mode \\n": "G21 ; 设为毫米模式 \\n",
 "G4 P0 ; Wait for moves to complete before returning": "G4 P0 ; 等待运动完成后返回",
 "M400 ; Wait for moves to complete before returning": "M400 ; 等待运动完成后返回",
 "{TimeMS:G4 P%d} ; Delay for given time in [ms]": "{TimeMS:G4 P%d} ; 按给定时间(ms)延时",
 "G-code standard": "G-code 标准",
 "; Unsupported driver unit ": "; 不支持的驱动器单位 ",

 # --- 驱动器 / G-code ---
 "Use the GcodeAsyncDriver for advanced features. Accept or Dismiss to continue.":
   "使用 GcodeAsyncDriver 以获得高级功能。点击「接受」或「拒绝」以继续。",
 "Use the GcodeDriver for simpler setup. Accept or Dismiss to continue.":
   "使用 GcodeDriver 以获得更简单的设置。点击「接受」或「拒绝」以继续。",
 "Convert to GcodeAsyncDriver.": "转换为 GcodeAsyncDriver。",
 "Convert to GcodeDriver.": "转换为 GcodeDriver。",
 "Compress Gcode for superior communications speed.": "压缩 G-code 以获得更快的通信速度。",
 "Enable Compress Gcode.": "启用压缩 G-code。",
 "Disable Compress G-code.": "禁用压缩 G-code。",
 "Disable G-code compression for trouble-free operation with incompatible controllers.":
   "禁用 G-code 压缩，以便与不兼容的控制器无故障运行。",
 "Keep G-code comments for better debugging.": "保留 G-code 注释，便于调试。",
 "Enable Remove Comments.": "启用移除注释。",
 "Disable Remove Comments.": "禁用移除注释。",
 "Remove Gcode comments for superior communications speed.": "移除 G-code 注释以获得更快的通信速度。",
 "Remove the command.": "移除该命令。",
 "Delete it.": "删除它。",
 "Modify it.": "修改它。",
 "Change it.": "修改它。",
 "Use the M584 S0 option in your config.g file.": "在 config.g 文件中使用 M584 S0 选项。",
 "Accept to replace ACTUATOR_READ_COMMAND with ACTUATOR_READ_WITH_DOUBLE_COMMAND. Dismiss to remove read with double.":
   "点击「接受」将 ACTUATOR_READ_COMMAND 替换为 ACTUATOR_READ_WITH_DOUBLE_COMMAND；点击「拒绝」则移除 with double。",
 "Disallow Pre-Move Commands for automatic G-code setup and other advanced features. Accept or Dismiss to continue.":
   "禁止预移动命令以获得自动 G-code 设置等高级功能。点击「接受」或「拒绝」以继续。",
 "Disable Allow Letter Pre-Move Commands.": "禁用允许字母预移动命令。",
 "Enable Letter Variables.": "启用字母变量。",
 "Use Axis Letter Variables for simpler use, automatic G-code setup, and other advanced features.":
   "使用轴字母变量可简化使用，并支持自动 G-code 设置等高级功能。",
 " Accept if this is a true Gcode controller.": " 若这是真正的 G-code 控制器，请点击「接受」。",
 "controller may not speak Gcode": "控制器可能不支持 G-code",
 "controller reported": "控制器报告",
 ", controller has no axes": "，控制器没有轴",
 "Failure, check log": "失败，请检查日志",
 "failure, check log": "失败，请检查日志",

 # --- 通信 / 连接 ---
 "Change of serial port Flow Control recommended.": "建议更改串口流控设置。",
 ", serial flow control is not available": "，串口流控不可用",
 "Disable Connection Keep-Alive.": "禁用连接保活（Keep-Alive）。",
 "Use Keep-Alive only when necessary. It may cause hard to diagnose problems.":
   "仅在必要时使用保活（Keep-Alive），否则可能导致难以诊断的问题。",
 "Choose the right communications type and port/address settings.": "请选择正确的通信类型及端口/地址设置。",
 "Please upgrade the firmware and/or axis configuration. See the info link.":
   "请升级固件和/或轴配置。请参阅信息链接。",
 "Please upgrade to the special PnP version. See info link.": "请升级到专用的 PnP 版本。请参阅信息链接。",
 "Retry the detection by connecting to the controller or assume a generic controller.":
   "请连接控制器重试检测，或假定为通用控制器。",
 "Get the new version through the linked web page.": "请通过链接的网页获取新版本。",
 "Check out firmwares known to be well supported. See info link.": "请查看已知受良好支持的固件。请参阅信息链接。",
 "A high Preview FPS value might create undue CPU load. ": "过高的预览帧率可能造成不必要的 CPU 负载。 ",

 # --- 运动控制类型 ---
 "Choose the simplest Motion Control Type for the first basic setup.": "首次基本设置请选择最简运动控制类型。",
 "Choose an advanced Motion Control Type for your controller type.": "请根据控制器类型选择高级运动控制类型。",
 "Location Confirmation required when Confirmation Flow Control is off. Supports extra features in homing, contact probing, etc.":
   "关闭确认流控时需要位置确认。可支持归位、接触探测等额外功能。",
 "Location Confirmation recommended for extra features in homing, contact probing, etc.":
   "建议启用位置确认，以支持归位、接触探测等额外功能。",
 "Location Confirmation usually not available when no axes present.": "无轴时通常无法使用位置确认。",
 "Enable Location Confirmation": "启用位置确认",
 "Disable Location Confirmation": "禁用位置确认",
 "Enable Confirmation Flow Control.": "启用确认流控。",
 "Disable Confirmation Flow Control.": "禁用确认流控。",
 "Disable Confirmation Flow Control for full asynchronous operation.": "禁用确认流控以实现完全异步运行。",
 "Marlin sends location-like responses to other commands so Location Confirmation is not reliable":
   "Marlin 会对其他命令返回类似位置的响应，因此位置确认不可靠",
 "not report all axes on M114, in which case the letter might still be valid":
   "在 M114 上不报告所有轴，此时该字母可能仍然有效",
 "support an extended range of letters, in which case the letter might still be valid":
   "支持更多字母，此时该字母可能仍然有效",

 # --- 安全 Z / 回零等方案 ---
 "Enable Visual Homing.": "启用视觉归位。",
 "Visual Homing": "视觉归位",
 "Mount a permanent fiducial to your machine and use it for repeatable precision X/Y homing.":
   "在机器上安装一个永久基准点，用于可重复的高精度 X/Y 归位。",
 "Enable Auto Camera View.": "启用自动相机视图。",
 "In single camera preview OpenPnP can automatically switch the camera for you.":
   "在单相机预览中，OpenPnP 可自动为您切换相机。",
 "camera switcher": "相机切换器",
 "For a SwitcherCamera it is mandatory": "对于切换相机（SwitcherCamera）这是必需的",
 "Enable Suspend during tasks.": "在任务期间启用挂起。",
 "Enable script engine pooling.": "启用脚本引擎池。",
 "Script execuction performance can be improved by enabling engine pooling.":
   "启用引擎池可提升脚本执行性能。",

 # --- 回差 / 校准 ---
 "Backlash Calibration Speed Control Test": "回差校准速度控制测试",
 "Backlash Compensation Test Location": "回差补偿测试位置",
 "Backlash at Sneak-up Distance ": "逼近距离处的回差 ",
 "Overshoot at Distance ": "距离处的过冲 ",
 "Set the targe tolerance. By granting a larger tolerance, a more efficient backlash compensation method may be eligible.":
   "设置目标公差。放宽公差可能允许使用更高效的回差补偿方法。",
 "Tolerance ±": "公差 ±",
 "Set a suitable camera settling method automatically.": "自动设置合适的相机稳定方式。",
 "Use an adaptive camera settling method.": "使用自适应相机稳定方式。",
 "Auto-Detect Next": "自动检测下一个",
 "Auto-Detect Next ": "自动检测下一个 ",
 "Subject not found.": "未找到目标。",
 "Feature diameter": "特征直径",

 # --- 杂项 ---
 "the catch all head mountable": "通用头部可安装对象",
 "the default head mountable": "默认头部可安装对象",
 "regular expression": "正则表达式",
 "set to the minimum": "设为最小值",
 "It is recommended": "建议",
 " suggested.": " 建议。",
 " modification suggested.": " 建议修改。",
 " obsolete.": " 已过时。",
 "Therefore, ": "因此，",
 "existing ": "现有 ",
 "wheel radius, ": "轮半径，",
 "wheel gap, ": "轮间隙，",
 "high side": "高侧",
 "low side": "低侧",
 "camera light": "相机光源",
 "pump control": "泵控制",
 "Machine is not enabled and homed.": "机器未启用或未归位。",
}

# 前缀/子串替换（用于句子片段，不含 \x01 的静态后缀）
PARTIAL = {}
