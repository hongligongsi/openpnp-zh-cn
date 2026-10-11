# -*- coding: utf-8 -*-
"""batch14_html2.py — 补充残留：长 HTML 提示块与剩余界面文案。"""

TABLE = {

# ---- ReferencePushPullFeederConfigurationWizard OCR 动作说明（长） ----
"<html>Determines what action should be taken when OCR detects the wrong Part ID in the feeder.<br/> \r\n<ul>\r\n<li>\r\n<strong>None</strong>: Use this setting if you don't want to use OCR.</li>\r\n<li>\r\n<strong>SwapFeeders</strong>: If a wrong part is detected but the right part is selected<br/>\r\nin a different ReferencePushPullFeeder, the locations of the two feeders are swapped. The<br/>\r\nswapped-in feeder will be enabled. This will happen, if you unload/reload/rearrange your<br/>\r\nfeeders on the machine.</li>\r\n<li>\r\n<strong>SwapOrCreate</strong>: Works like <strong>SwapFeeders</strong>, but if no<br/>\r\nother feeder with the right part is found, a new one will be created and swapped-in at the<br/>\r\ncurrent feeder's location. The current feeder is then disabled in turn (they are now sitting at<br/>\r\nthe same location and only one must be enabled).</li>\r\n<li>\r\n<strong>ChangePart</strong>: The part in the current feeder is changed. This will only<br/>\r\nwork correctly, if the tape settings etc. remain the same between the parts i.e. if you restrict<br/>\r\nany reloading/rearranging to groups of feeders with the same settings.</li>\r\n<li>\r\n<strong>ChangePartAndClone</strong>: The part in the current feeder is changed but<br/>\r\nsettings are cloned from a template feeder.</li>\r\n</ul>\r\n</html>\r\n":
"<html>决定当 OCR 在供料器中检测到错误的元件 ID 时应采取的动作。<br/> \r\n<ul>\r\n<li>\r\n<strong>无</strong>：若你不想使用 OCR，请使用此设置。</li>\r\n<li>\r\n<strong>交换供料器</strong>：若检测到错误的元件，但正确的元件已在另一个<br/>\r\nReferencePushPullFeeder 中被选中，则交换这两个供料器的位置。<br/>\r\n被换入的供料器将被启用。当你从机器上卸下/重装/重新排列<br/>\r\n供料器时，会发生这种情况。</li>\r\n<li>\r\n<strong>交换或新建</strong>：作用与<strong>交换供料器</strong>类似，但若找不到<br/>\r\n装载正确元件的其他供料器，则会在当前供料器的位置新建一个并换入。<br/>\r\n当前供料器随之被禁用（此时两者位于同一位置，只能启用其中一个）。</li>\r\n<li>\r\n<strong>更换元件</strong>：更换当前供料器中的元件。只有当各元件之间的<br/>\r\n料带设置等保持一致时，即你只将重装/重排限制在设置相同的供料器组内时，<br/>\r\n此操作才能正确工作。</li>\r\n<li>\r\n<strong>更换元件并克隆</strong>：更换当前供料器中的元件，但<br/>\r\n设置从模板供料器克隆而来。</li>\r\n</ul>\r\n</html>\r\n",

"<html>On Job Start, check that the correct parts are selected in OCR-enabled feeders at their locations. <br/>\r\nOtherwise the Job is stopped.<br/>\r\nThis will also vision-calibrate the feeders' locations, if calibration is enabled.</html>":
'<html>作业启动时，检查各位置处启用了 OCR 的供料器中是否选择了正确的元件。<br/>\r\n否则作业将停止。<br/>\r\n若已启用校准，这还会对供料器的位置进行视觉校准。</html>',

'<html>Use this feeder as a template for cloning settings to other feeders. <br/>\r\nThe templates are matched by tape & reel specification or package of the parts <br/>\r\nloaded in feeders. <br/>\r\nWhen no template matches formally, the feeder \nwith the greatest similarities <br/>\r\nis taken (feed pitch, tape width, proximity, etc.).</html>':
'<html>将此供料器用作模板，把设置克隆到其他供料器。<br/>\r\n模板依据供料器中装载元件的料带与料盘规格或封装进行匹配。<br/>\r\n<br/>\r\n当没有模板能正式匹配时，<br/>\r\n则选用相似度最高的供料器<br/>\r\n（供料间距、料带宽度、邻近程度等）。</html>',

'<html>Rotation of the part inside the tape as seen when the sprocket holes <br/>\r\nare on top. Your E-CAD part orientation is the reference.<br/>\r\nSee also: \r\n<ul>\r\n<li>EIA-481</li>\r\n<li>Component Zero Orientations for CAD Libraries</li>\r\n</ul>\r\n</html>':
'<html>当齿孔朝上时所见到的元件在料带内的旋转角度。<br/>\r\n以你的 E-CAD 元件方向为参考。<br/>\r\n另请参见：\r\n<ul>\r\n<li>EIA-481</li>\r\n<li>CAD 库的元件零度方向</li>\r\n</ul>\r\n</html>',

"<html>\n<p>The <strong>Rotation in Tape</strong> setting must be interpreted relative to the tape's orientation, <br/>\nregardless of how the feeder/tape is oriented on the machine. </p>\n<ol>\n<li>\n<p>Look at the <strong>neutral</strong> upright orientation of the part package/footprint <br/>\nas drawn inside your E-CAD <strong>library</strong>.</p>\n</li>\n<li>\n<p>Note how pin 1, polarity, cathode etc. are oriented.  <br/>\nThis is your 0° for the part.</p>\n</li>\n<li>\n<p>Look at the tape so that the sprocket holes are at the top. <br/>\nThis is your 0° tape orientation (per EIA-481 industry standard).</p>\n</li>\n<li>\n<p>Determine how the part is rotated inside the tape pocket, <em>relative</em> from  <br/>\nits upright orientation in (1).  Positive rotation goes counter-clockwise.<br/>\nThis is your <strong>Rotation in Tape</strong>.</p>\n</li>\n</ol>\n</html>":
'<html>\n<p><strong>料带内旋转</strong> 设置必须相对于料带的方向来理解，<br/>\n而与供料器/料带在机器上的朝向无关。</p>\n<ol>\n<li>\n<p>查看元件封装/外形在你 E-CAD <strong>库</strong>中绘制的<br/>\n<strong>中性</strong>正立方向。</p>\n</li>\n<li>\n<p>注意引脚 1、极性、阴极等的朝向。<br/>\n这就是该元件的 0°。</p>\n</li>\n<li>\n<p>观察料带，使齿孔位于上方。<br/>\n这就是料带的 0° 方向（依据 EIA-481 行业标准）。</p>\n</li>\n<li>\n<p>确定元件在料袋内相对于 (1) 中正立方向的<em>旋转</em>量。<br/>\n正向旋转为逆时针方向。<br/>\n这就是你的 <strong>料带内旋转</strong>。</p>\n</li>\n</ol>\n</html>',

'<html>\r\n<p>Choose the vision type, then press <strong>Reset Pipeline</strong> to assign the<br/>\r\ndefault pipeline of that type. Sprocket holes are detected as follows:</p>\r\n<ul>\r\n<li><strong>ColorKeyed</strong>: the background under the holes must be of a vivid color<br/>\r\n(green by default).</li>\r\n<li><strong>CircularSymmetry</strong>: the shape of the holes must be circular, their<br/>\r\ninside/outside must be plain.</li>\r\n</ul>\r\n<p>Both types of pipeline will further assess detected holes by size, alignment, pitch<br/>\r\nand expected distance.</p>\r\n</html>':
'<html>\r\n<p>选择视觉类型，然后按 <strong>重置管线</strong> 以分配该类型的<br/>\r\n默认管线。齿孔的检测方式如下：</p>\r\n<ul>\r\n<li><strong>ColorKeyed（色键）</strong>：孔下方的背景必须为鲜艳的颜色<br/>\r\n（默认为绿色）。</li>\r\n<li><strong>CircularSymmetry（圆对称）</strong>：孔的形状必须为圆形，其<br/>\r\n内侧/外侧必须平坦无花纹。</li>\r\n</ul>\r\n<p>两种管线都会进一步依据尺寸、对齐、孔距<br/>\r\n与预期间距来评估检测到的孔。</p>\r\n</html>',

'<html>By default, every time a script should be executed, a new instance of the appropriate script engine is created.<br><br>By enabling script engine pooling, a new instance of any script engine is only created if the pool doesn\'t contain an available instance of the appropriate type. Following executions re-use the already initialized script engines, lowering execution time for scripting hooks.This feature is only relevant if you use scripting in OpenPnP.<br><br><span style="color:red;">Script engine pooling can - depending on the script engine implementation - cause global state to be kept in following invocations. Check the wiki for further information.</span></html>':
'<html>默认情况下，每次需要执行脚本时，都会创建相应脚本引擎的一个新实例。<br><br>启用脚本引擎池后，只有当池中不含相应类型的可用实例时，才会创建任何脚本引擎的新实例。后续执行会复用已初始化的脚本引擎，从而缩短脚本钩子的执行时间。仅当你使用 OpenPnP 的脚本功能时，此功能才有意义。<br><br><span style="color:red;">脚本引擎池可能（取决于脚本引擎的实现方式）导致全局状态在后续调用中被保留。更多信息请查阅 Wiki。</span></html>',

'<html><p>You already performed the preliminary camera calibration earlier, now it is time for the <strong>Advanced Camera Calibration</strong> that includes compensating lens distortion and camera mounting tilt. A more profound and precise 3D Units per Pixel calibration is also applied.</p><br/><p>More information can be found in the Wiki (press the blue Info button below).</p><br/><p>The calibration must be performed with the same calibration rig, that you used for the preliminary calibration. Make sure it is ready, and locations (including Z) are still valid.</p><br/><p>If not, please revisit the <strong>Primary calibration fiducial position</strong> and <strong>Secondary calibration fiducial position</strong> steps first (Enable the <strong>Include Solved?</strong> checkbox above, to see revisitable solutions).</p><br/><p><strong color="red">CAUTION</strong>: The camera § will move over the calibration rig and perform a length calibration motion pattern.</p><br/></html>':
'<html><p>你此前已完成初步的相机校准，现在该进行<strong>高级相机校准</strong>了，其中包含镜头畸变与相机安装倾斜的补偿，还会应用更深入、更精确的 3D 每像素单位数校准。</p><br/><p>更多信息请查阅 Wiki（点击下方的蓝色信息按钮）。</p><br/><p>校准必须使用与初步校准时相同的校准工装。请确保它已就绪，且各位置（含 Z）仍然有效。</p><br/><p>若不然，请先重新审视<strong>主校准基准点位置</strong>与<strong>次校准基准点位置</strong>步骤（勾选上方的 <strong>包含已解决？</strong> 复选框即可看到可重新审视的方案）。</p><br/><p><strong color="red">注意</strong>：相机 § 将移动到校准工装上方，并执行一段长度校准运动。</p><br/></html>',

'<html><p>You already performed the preliminary camera calibration earlier, now it is time for the <strong>Advanced Camera Calibration</strong> that includes compensating lens distortion and camera mounting tilt. A more profound and precise 3D Units per Pixel calibration is also applied.</p><br/><p>More information can be found in the Wiki (press the blue Info button below).</p><br/><p>The calibration must be performed with the same nozzle tip, that you used for the preliminary calibration. Make sure it is loaded and its <strong>Vision Diameter</strong> is still valid. Furthermore the camera § position (including Z) must still be valid.</p><br/><p>If not, please revisit the <strong>Determine up-looking camera § position</strong> step first (Enable the <strong>Include Solved?</strong> checkbox above, to see revisitable solutions).</p><br/><p><strong color="red">CAUTION</strong>: The nozzle § will perform a lengthy calibration motion pattern all over the view area of the camera §. Before pressing <strong>Accept</strong>, you need to be sure nozzle § will not collide with anything!</p><br/></html>':
'<html><p>你此前已完成初步的相机校准，现在该进行<strong>高级相机校准</strong>了，其中包含镜头畸变与相机安装倾斜的补偿，还会应用更深入、更精确的 3D 每像素单位数校准。</p><br/><p>更多信息请查阅 Wiki（点击下方的蓝色信息按钮）。</p><br/><p>校准必须使用与初步校准时相同的吸嘴头。请确保它已装好，且其<strong>视觉直径</strong>仍然有效。此外，相机 § 的位置（含 Z）也必须仍然有效。</p><br/><p>若不然，请先重新审视<strong>确定上视相机 § 位置</strong>步骤（勾选上方的 <strong>包含已解决？</strong> 复选框即可看到可重新审视的方案）。</p><br/><p><strong color="red">注意</strong>：吸嘴 § 将在相机 § 的整个视野区域内执行一段较长的校准运动。按下 <strong>接受</strong> 之前，你必须确认吸嘴 § 不会与任何东西碰撞！</p><br/></html>',

'<html><p>With <strong>Dynamic Safe Z</strong> enabled, the nozzle needs a head-room, the so-called Safe Z Zone to lift the nozzle higher with taller parts. The maximum expected part height is specified on the nozzle tip <strong>Max. Part Height</strong>.</p><br/><p>Nozzle § with compatible tip § has a <strong>Max. Part Height</strong> of § which is larger than the Safe Z Zone of §. Note, the safe Z Zone is configured on the § axis to reach from § to § in (untransformed) coordinates.</p><br/><p>Please either enlarge the Safe Z Zone, by reducing the nozzle § Z clearance, or reduce the <strong>Max. Part Height</strong> on nozzle tip §.</p><br/><p>Reducing Z clearance is best done by revisiting the Safe Z solution for nozzle §. Enable the <strong>Include Solved?</strong> checkbox at the top, then reopen the "Set Safe Z of §" solution and redo it.</p></html>':
'<html><p>启用<strong>动态安全 Z</strong>后，吸嘴需要一定的抬升空间，即所谓的安全 Z 区，以便在元件较高时将吸嘴抬得更高。元件的最大预期高度在吸嘴头的 <strong>最大元件高度</strong> 中指定。</p><br/><p>吸嘴杆 § 配兼容吸嘴头 § 的 <strong>最大元件高度</strong> 为 §，大于 § 的安全 Z 区。注意，安全 Z 区配置在 § 轴上，（未变换的）坐标范围为 § 至 §。</p><br/><p>请通过减小吸嘴杆 § 的 Z 间隙来扩大安全 Z 区，或者减小吸嘴头 § 上的 <strong>最大元件高度</strong>。</p><br/><p>减小 Z 间隙的最佳做法是重新审视吸嘴杆 § 的安全 Z 方案。勾选顶部的 <strong>包含已解决？</strong> 复选框，然后重新打开「设置 § 的安全 Z」方案并重做。</p></html>',

'<html><p>The cam transform on axis § with non-zero §§ is deprecated.</p><br/><p><strong color="red">CAUTION:</strong> These offsets will create problems when Issues & Solutions wants to (re-)reference the Z coordinate system later. Failing to accept this solution may ultimately lead to a dead end in the machine setup process.</p><br/><p>Press <strong>Accept</strong> to remove the §§as recommended.§</p></html>':
'<html><p>轴 § 上带有非零 §§ 的凸轮变换已废弃。</p><br/><p><strong color="red">注意：</strong>当「问题与解决方案」之后想要（重新）建立 Z 坐标系参考时，这些偏移会造成问题。若不接受此方案，最终可能导致机器设置流程走入死胡同。</p><br/><p>按 <strong>接受</strong> 以按建议移除 §§。§</p></html>',

'<html>§-Switching<br/>§</html>': '<html>§-切换<br/>§</html>',

'</p><br/><p><strong>Note:</strong> this change will be compensated in the Z head offset of §§so that Z coordinates captured before effectively remain the same.':
'</p><br/><p><strong>注意：</strong>此更改将在 §§ 的 Z 机头偏移中得到补偿，使此前采集的 Z 坐标实际上保持不变。',

'<html>This will move § for one jog increment and back. <br/>§Are you sure?</html>':
'<html>这将使 § 移动一个点动增量后再返回。<br/>§你确定吗？</html>',

# ---- 其他非 HTML 可见文案 ----
'internalCapture() done in: %d': 'internalCapture() 完成，耗时：%d',
'imgSetGain() [cameraId:%d, gain:%d]': 'imgSetGain() [cameraId:%d, gain:%d]',
'{}.getPickLocation: feedCount larger then tray, limiting to maximum.': '{}.getPickLocation：feedCount 大于料盘数，已限制为最大值。',
'{} rect: xy={}, {} area={} angle= {}°': '{} 矩形：xy={}, {} 面积={} 角度= {}°',
'<<< filtered out rect with size=§, because filter size is = §x§': '<<< 已滤除尺寸为 § 的矩形，因为过滤尺寸为 §x§',
'{} empty command after pre process': '{} 预处理后命令为空',
'{} failed to write command {}': '{} 写入命令 {} 失败',
'{} got response matching "{}" after {}ms': '{} 在 {}ms 后得到匹配 "{}" 的响应',
'{}: Axis {} letter {} missing in POSITION_REPORT_REGEX groups.': '{}：轴 {} 的字母 {} 在 POSITION_REPORT_REGEX 分组中缺失。',
'{}: Error processing position report for axis {}: {}': '{}：处理轴 {} 的位置报告时出错：{}',
'{} waited {}ms for empty command queue.': '{} 等待空命令队列耗时 {}ms。',
'{} timeout while waiting for empty command queue.': '{} 等待空命令队列超时。',
'{} waited {}ms to drain command queue.': '{} 排空命令队列耗时 {}ms。',
'{} simulate actuation, sleep 5ms': '{} 模拟触发，休眠 5ms',
'{} averaged location is at {}': '{} 的平均位置位于 {}',
'{} disabled due to being empty {}': '{} 因内容为空而被禁用 {}',
'{} disabled due to feed error {}': '{} 因供料错误而被禁用 {}',
'{} disabled due to fault limit': '{} 因达到故障次数上限而被禁用',
'{}.home() nozzle tip {} calibration reset': '{}.home() 吸嘴头 {} 校准已重置',
'setUnits() not implemented for §': 'setUnits() 未针对 § 实现',
'getJogIncrement() not implemented for §': 'getJogIncrement() 未针对 § 实现',

# ---- G 代码模板注释（仅翻译注释） ----
'G21 ; Set millimeters mode\nG90 ; Set absolute positioning mode\nM82 ; Set absolute mode for extruder':
'G21 ; 设置毫米模式\nG90 ; 设置绝对定位模式\nM82 ; 为挤出机设置绝对模式',
'G28 ; Home all axes': 'G28 ; 全轴归位',
'G92 {XL}{X:%.4f} {YL}{Y:%.4f} {ZL}{Z:%.4f} {RotationL}{Rotation:%.4f} ; Reset current position to given coordinates':
'G92 {XL}{X:%.4f} {YL}{Y:%.4f} {ZL}{Z:%.4f} {RotationL}{Rotation:%.4f} ; 将当前位置重置为给定坐标',
'{Acceleration:M204 S%.1f} G0 {XL}{X:%.4f} {YL}{Y:%.4f} {ZL}{Z:%.4f} {RotationL}{Rotation:%.4f} {FeedRate:F%.1f} ; Send standard Gcode move':
'{Acceleration:M204 S%.1f} G0 {XL}{X:%.4f} {YL}{Y:%.4f} {ZL}{Z:%.4f} {RotationL}{Rotation:%.4f} {FeedRate:F%.1f} ; 发送标准 G 代码移动',
'{True:M¿ ; actuate § ON}\n{False:M¿ ; actuate § OFF}': '{True:M¿ ; 触发 § 开启}\n{False:M¿ ; 触发 § 关闭}',
'{StringValue} ; actuate § with direct string command value': '{StringValue} ; 用直接字符串命令值触发 §',
'{True:G38.2 §§ F§ ; probe down in relative coordinates until limit switch is hit}\n{True:M400            ; wait until machine has stopped}':
'{True:G38.2 §§ F§ ; 在相对坐标下向下探测，直到触碰限位开关}\n{True:M400            ; 等待机器完全停止}',
'{True:G38.2 §§ F§ ; probe down in absolute coordinates until limit switch is hit}\n{True:M400            ; wait until machine has stopped}':
'{True:G38.2 §§ F§ ; 在绝对坐标下向下探测，直到触碰限位开关}\n{True:M400            ; 等待机器完全停止}',
'G21 ; Set millimeters mode \n': 'G21 ; 设置毫米模式 \n',
'G20 ; Set inches mode \n': 'G20 ; 设置英寸模式 \n',
'G21 ; Set millimeters mode \n§': 'G21 ; 设置毫米模式 \n§',
'G20 ; Set inches mode \n§': 'G20 ; 设置英寸模式 \n§',
'{Acceleration:M204 S%.§f }': '{Acceleration:M204 S%.§f }',

# ---- 纯 SVG/XML 结构中的可读标题 ----
'<title>Travelling Salesman (§ locations, §mm, §ms)</title>\n': '<title>旅行商路线（§ 个位置，§mm，§ms）</title>\n',
'<title>Profile s[0]=§ s[7]=§ v[0]=§ v[7]=§ tMin=§': '<title>曲线 s[0]=§ s[7]=§ v[0]=§ v[7]=§ tMin=§',

}
