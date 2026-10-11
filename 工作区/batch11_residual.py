# -*- coding: utf-8 -*-
"""batch11_residual.py — 第三轮残留可见文案（HTML 提示块 + 日志/标签文本）。

数据来源：sweep_en.json 全量扫描后过滤出的 358 条候选中真正的可见文案。
"""

TABLE = {

# =========================================================
# 一、HTML 提示块 —— Issues & Solutions 面板
# =========================================================

'<html><p>This platform does not support direct web browsing.</p><br/><p>However, the URI was copied to the clipboard, please paste into your favorite browser\'s address line.</p><br/><p><a href="§">§</a></p></html>':
'<html><p>当前平台不支持直接打开网页浏览。</p><br/><p>不过，该 URI 已复制到剪贴板，请粘贴到你所用的浏览器地址栏中。</p><br/><p><a href="§">§</a></p></html>',

'<html><p>Axis currently assigned in:</p><ul>§</ul><p>Are you sure you want to delete §?</p></html>':
'<html><p>该轴当前被分配给：</p><ul>§</ul><p>你确定要删除 § 吗？</p></html>',

'<html>Center the camera on the pick location and press this button to Auto-Setup <br/>If there are multiple picks per feed cycle, choose the one closest to the tape reel.</html>':
'<html>将相机对准取料位置，然后按下此按钮进行自动设置。<br/>如果每个供料周期有多次取料，请选择最靠近料盘的那一次。</html>',

'<html><p>This may overwrite all your current settings. Are you sure?</p></html>':
'<html><p>这可能会覆盖你当前的全部设置。你确定吗？</p></html>',

'<html>Discard parts left over in the (multi-part) feed cycle.<br/>\r\nStarts with a fresh feed cycle including vision calibration (if enabled). \r\n</html>':
'<html>丢弃（多次）供料周期中剩余的元件。<br/>\r\n重新开始一个全新的供料周期，并包含视觉校准（若已启用）。\r\n</html>',

'<html>Pick Location of the part. If multiple are produced by a feed operation<br/>\r\nthis must be the last one picked i.e. the one closest to the the tape reel.</html>':
'<html>元件的取料位置。如果一次供料动作会产生多个取料点，<br/>\r\n这里必须填写最后一个取料点，即最靠近料盘的那一个。</html>',

'<html>Choose Hole 1 closer to the tape reel.<br/>\r\nIf possible choose two holes that bracket the part(s) to be picked.\r\n</html>':
'<html>选择较靠近料盘的孔 1。<br/>\r\n如果可能，请选择能够夹住待取元件的两个孔。\r\n</html>',

'<html>Choose Hole 2 further away from the tape reel.<br/>\r\nIf possible choose two holes that bracket the part(s) to be picked.\r\n</html>':
'<html>选择离料盘较远的孔 2。<br/>\r\n如果可能，请选择能够夹住待取元件的两个孔。\r\n</html>',

'<html>\r\n<p>For Duble: numerical value<br/>\r\nFor Boolean: 1 = True, 0 = False</p></html>':
'<html>\r\n<p>Double 类型：填写数值<br/>\r\nBoolean 类型：1 = True，0 = False</p></html>',

'<html>Do atomic feed, i.e. not full feed based on <i>Part&Feed pitch</i>.</html>':
'<html>执行单次供料，即不按 <i>元件与供料间距</i> 进行完整供料。</html>',

'<html>\r\n<p>Select the actuator for the post pick action<br/>\r\nThis is optional: blank selection will skip the post pick operation\r\n</p></html>':
'<html>\r\n<p>选择取料后动作所使用的执行器。<br/>\r\n此为可选项：留空将跳过取料后动作。\r\n</p></html>',

'<html><p>This may overwrite all your current settings. Are you sure?</p>§</html>':
'<html><p>这可能会覆盖你当前的全部设置。你确定吗？</p>§</html>',

'<html>Locations that are included, when actuating multiple times.<br/>\r\nThe combination with the push ↓ and pull ↑ switch is taken.</html>':
'<html>多次触发时所包含的位置点。<br/>\r\n会与推 ↓ 和拉 ↑ 开关组合使用。</html>',

'<html>Before the feed is performed, the current coordinate of the Rotation axis is taken.<br/>\nRotations stated below are then added to that base angle.<br/>\nThis is typically used for peeling axes, creating a continuous cover tape spool wind-up.\n</html>':
'<html>执行供料之前，先记录旋转轴的当前坐标。<br/>\n下方所述的旋转量随后会叠加到该基准角度上。<br/>\n这通常用于撕膜轴，以实现料带盖膜的连续卷绕收卷。\n</html>',

'<html>\r\nNormalize the fiducial distances and shear to the theoretically correct <br />\r\nvalues (whole millimeter square grid). This means you trust the mechanics  <br />\r\nof your machine and of your 3D printer over the computer vision fiducial fixes.  <br />\r\nOverall absolute position and angle are still determined by vision. \r\n</html>':
'<html>\r\n将基准点间距与切变归一化到理论上正确的值<br />\r\n（整数毫米方格网）。这意味着你更信任机器与 3D 打印机的机械精度，<br />\r\n而非计算机视觉对基准点的修正。<br />\r\n整体的绝对位置与角度仍由视觉确定。\r\n</html>',

'<html><p>Use vision for fiducial calibration when the feeder is first used. </p>\r\n<p>Even if fiducial vision is disabled, vision will still be used for setup and <br />\r\ncover open checking</p><html>':
'<html><p>供料器首次使用时，使用视觉进行基准点校准。</p>\r\n<p>即使禁用了基准点视觉，视觉仍会用于设置以及<br />\r\n盖膜开启检测。</p><html>',

'<html>Size of the margin where the OCR/Barcode labels are attached.<br/>When a negative value is given, the labels are assumed to be located at the end of the feeder.':
'<html>贴附 OCR/条码标签的边距大小。<br/>若给定负值，则假定标签位于供料器的末端。',

'<html>Name of the OCR font to be recognized or [Barcode].<br/>\r\nMonospace fonts work much better, allow lower resolution and therefore faster <br/>\r\noperation. Use a font where all the used characters are easily distinguishable.<br/>\r\nFonts with clear separation between glyphs are much preferred.</html>':
'<html>要识别的 OCR 字体名称，或填 [Barcode]。<br/>\r\n等宽字体的效果要好得多，允许更低的分辨率，因此运行更快。<br/>\r\n请使用所用字符易于相互区分的字体。<br/>\r\n强烈推荐字形之间间距清晰的字体。</html>',

'<html>Reset the current rotation axis to <strong>0°</strong> for subsequent<br/>capturing/positioning using the location buttons in additive mode.</html>':
'<html>在累加模式下使用位置按钮进行后续<br/>采集/定位时，将当前旋转轴重置为 <strong>0°</strong>。</html>',

'<html>Clone the settings from this feeder to all compatible feeders.</html>':
'<html>将此供料器的设置克隆到所有兼容的供料器。</html>',

'<html>This will overwrite the selected settings in all the target feeders:<br/><br/>§<br/><br/>   Are you sure?</html>':
'<html>这会覆盖所有目标供料器中已选中的设置：<br/><br/>§<br/><br/>   你确定吗？</html>',

'<html>Perform OCR and assign the recognized part.</html>':
'<html>执行 OCR 并分配识别出的元件。</html>',

'<html>Go to all the feeders with OCR and rediscover the parts loaded in them. </html>':
'<html>遍历所有启用了 OCR 的供料器，重新识别其中装载的元件。</html>',

'<html>Add one more feeder like this one, advancing in a row.</html>':
'<html>再添加一个与此相同的供料器，按行依次排列。</html>',

'<html>Moves the camera to the vision location and lets you select the OCR region of interest.</html>':
'<html>将相机移动到视觉位置，并让你选择 OCR 感兴趣区域。</html>',

'<html><p>Files extracted to:</p><p>§</p><p>Cannot open with OpenSCAD automatically (Desktop command failed)</p>':
'<html><p>文件已解压到：</p><p>§</p><p>无法自动用 OpenSCAD 打开（桌面命令执行失败）</p>',

'<html>Clone the settings from the selected template feeder, <br/>transforming any coordinates to the pick location and orientation.</html>':
'<html>从选定的模板供料器克隆设置，<br/>并将所有坐标转换到取料位置与方向。</html>',

'<html><p>This will overwrite the selected settings with those from the template:<br/><br/>§<br/><br/>Are you sure?':
'<html><p>这会用模板中的设置覆盖当前选中的设置：<br/><br/>§<br/><br/>你确定吗？',

'<html>Auto-Focus the selected nozzle in this camera.<br/>If a part is on the nozzle, its height will be determined.</html>':
'<html>在此相机中对所选吸嘴杆执行自动对焦。<br/>若吸嘴上有元件，还会测定其高度。</html>',

'<html>After having auto-focused, adjust the camera Z coordinate<br/>to match the focal distance i.e. make sure the camera is focused.</html>':
'<html>自动对焦之后，调整相机 Z 坐标<br/>使其与焦距匹配，即确保相机已合焦。</html>',

'<html>This will overwrite the current camera Z position and therefore<br/>change the camera-to-subject distance and the subject scale.<br/><span color="red">You will need to recalibrate the Units per Pixel!</span><br/><br/>Are you sure?</html>':
'<html>这会覆盖当前相机 Z 位置，从而<br/>改变相机到目标的距离以及目标的比例。<br/><span color="red">你将需要重新校准每像素单位数！</span><br/><br/>你确定吗？</html>',

'<html><h3>Dynamic Safe Z</h3><p>If a part is on the nozzle, the nozzle is lifted to Safe Z <strong>+</strong> part height.</p><br/><p>Safe Z must only account for the tallest obstacle.</p><br/><p>This will result in faster, more optimized machine motion.</p><br/><p><strong>Recommended.</strong>.</p><br/></html>':
'<html><h3>动态安全 Z</h3><p>若吸嘴上有元件，吸嘴会抬升到安全 Z <strong>+</strong> 元件高度。</p><br/><p>安全 Z 只需考虑最高的障碍物。</p><br/><p>这样可获得更快、更优化的机器运动。</p><br/><p><strong>推荐使用。</strong></p><br/></html>',

'<html><h3>Fixed Safe Z</h3><p>Safe Z is always at a fixed level.</p><br/><p>Safe Z must account for <em>both</em> the tallest obstacle <em>and</em> the tallest part on the nozzle.</p><br/><p>This will result in slower, less optimized machine motion.</p></html>':
'<html><h3>固定安全 Z</h3><p>安全 Z 始终保持在一个固定高度。</p><br/><p>安全 Z 必须<em>同时</em>考虑最高的障碍物<em>和</em>吸嘴上最高的元件。</p><br/><p>这会导致机器运动较慢、优化程度较低。</p></html>',

'<html><p>To calibrate precision camera ↔ nozzle offsets, we let the nozzle pick, rotate and place a small test object and then measure the resulting offsets using the camera.</p><br/><p>Instructions about suitable test objects etc. must be obtained in the OpenPnP Wiki. Press the blue Info button (below) to open the Wiki.</p><br/><p>Place the calibration test object onto the calibration primary fiducial.</p><br/><p>Jog camera § over the test object. Target it with the cross-hairs.</p><br/><p>Adjust the <strong>Feature diameter</strong> up and down and see if it is detected right in the camera view. A green circle and cross-hairs should appear and hug the test object contour. Zoom the camera using the scroll-wheel.</p><br/><p><strong color="red">CAUTION</strong> The nozzle § will move to the test object and perform the calibration pick & place pattern. Make sure to load the right nozzle tip and ready the vacuum system.</p><br/><p>When ready, press Accept.</p>§</html>':
'<html><p>为校准相机 ↔ 吸嘴的精确偏移量，我们让吸嘴拾取、旋转并放置一个小测试物体，然后用相机测量由此产生的偏移。</p><br/><p>有关合适测试物体等的说明，请查阅 OpenPnP Wiki。点击下方的蓝色信息按钮可打开 Wiki。</p><br/><p>将校准测试物体放置在主校准基准点上。</p><br/><p>将相机 § 移动到测试物体上方。用十字线对准它。</p><br/><p>上下调整 <strong>特征直径</strong>，观察它在相机视图中是否被正确识别。应出现一个绿色圆圈和十字线，贴合测试物体的轮廓。可用滚轮缩放相机视图。</p><br/><p><strong color="red">注意</strong> 吸嘴 § 将移动到测试物体处并执行校准取放动作。请确保装好正确的吸嘴头，并让真空系统就绪。</p><br/><p>准备就绪后，请按「接受」。</p>§</html>',

'<html><span color="red">CAUTION:</span> This is a troubleshooting option, you should only disable G-code compression if it causes problems.</html>':
'<html><span color="red">注意：</span>这是一个故障排查选项，只有当 G 代码压缩导致问题时才应禁用它。</html>',

'<html><p>Backlash compensation is used to avoid the effects of any looseness or play in the mechanical linkages of machine axes. More information can be found in the Wiki (press the blue Info button below).</p><br/><p>Set the acceptable <strong>Tolerance ±</strong> as high as possible to allow for a more efficient backlash compensation method, avoiding extra moves and direction changes.</p><br/><p><strong color="red">CAUTION 1</strong>: The camera § will move over the primary fiducial and then perform a calibration motion pattern, moving the axis § over its full soft-limit range.</p><br/><p><strong color="red">CAUTION 2</strong>: The machine will also perform a visual homing cycle, once the new backlash compensation method is established. This is done to recalibrate the coordinate system that might be affected by the new method.</p><br/><p>When ready, press Accept.</p>§</html>':
'<html><p>反向间隙补偿用于消除机器各轴机械连接处的松动或虚位所带来的影响。更多信息请查阅 Wiki（点击下方的蓝色信息按钮）。</p><br/><p>将可接受的 <strong>容差 ±</strong> 尽可能设大，以便采用更高效的反向间隙补偿方式，避免多余的移动与换向。</p><br/><p><strong color="red">注意 1</strong>：相机 § 将移动到主基准点上方，然后执行一段校准运动，带动轴 § 走完其整个软限位范围。</p><br/><p><strong color="red">注意 2</strong>：在确立新的反向间隙补偿方式后，机器还会执行一次视觉归位循环。这是为了重新校准可能受新方式影响的坐标系。</p><br/><p>准备就绪后，请按「接受」。</p>§</html>',

'<html><p>Jog § over the tallest obstacle on your machine, including the the tallest parts that may be placed on the PCB.</p><br/><p>Then lower it down so it still has sufficient clearance§.</p><br/><p>Then press Accept to capture the Safe Z.</p>§</html>':
'<html><p>将 § 移动到机器上最高障碍物的上方，其中包括可能放置在 PCB 上的最高元件。</p><br/><p>然后将其下降，使其仍保留足够的安全间隙§。</p><br/><p>然后按「接受」以采集安全 Z。</p>§</html>',

'<html>Suggested templates for the <code>§</code>.<br/><br/>\n<strong>CAUTION:</strong> You may need to adapt these to your specific <br/>\n§, controller and/or §.<br/>\nReplace placeholders ¿ with the proper numbers/letters/designators.</html>':
'<html><code>§</code> 的建议模板。<br/><br/>\n<strong>注意：</strong>你可能需要针对具体的 <br/>\n§、控制器和/或 § 进行调整。<br/>\n请将占位符 ¿ 替换为正确的数字/字母/标识符。</html>',

'<html><p>Move axis § to the § soft limit.</p><br/><p>Jog § of § § to do so.</p><br/><p>If the axis has a limit switch, use a position close to it but still safe to not trigger the switch by accident.</p><br/><p>Then press Accept to capture the lower soft limit.</p></html>':
'<html><p>将轴 § 移动到 § 软限位。</p><br/><p>通过点动 § 的 § § 来完成。</p><br/><p>若该轴装有限位开关，请使用一个靠近它但仍能安全避免误触发开关的位置。</p><br/><p>然后按「接受」以采集下限软限位。</p></html>',

'<html><p>You must be sure that your machine supports the homing command with the proper axis end-switches wired and configured.</p><br/><p>Press <strong>Accept</strong> to perform the homing.</p><br/><p>Afterwards, press <strong>Find Issues & Solutions</strong> again.</p></html>':
'<html><p>你必须确认你的机器支持该归位命令，且各轴限位开关已正确接线与配置。</p><br/><p>按 <strong>接受</strong> 执行归位。</p><br/><p>之后，请再次按 <strong>查找问题与解决方案</strong>。</p></html>',

'<html><span color="red">CAUTION:</span> This is a troubleshooting option, you should only keep G-code comments if removing them causes problems.</html>':
'<html><span color="red">注意：</span>这是一个故障排查选项，只有当移除 G 代码注释导致问题时才应保留它们。</html>',

'<html><span color="red">CAUTION:</span> This is a troubleshooting option, you should only choose § if the current § causes problems and you want to try a simpler setting.</html>':
'<html><span color="red">注意：</span>这是一个故障排查选项，只有当当前的 § 导致问题、而你想尝试更简单的设置时，才应选择 §。</html>',

'<html><p>Switch vision settings pre-rotate usage from <strong>§</strong> to <strong>§</strong> on these parts:</p><ol><li>§</li><ol></html>':
'<html><p>对以下元件，将视觉设置的预旋转用法从 <strong>§</strong> 切换为 <strong>§</strong>：</p><ol><li>§</li><ol></html>',

'<html><p>Mount a permanent fiducial to your machine table. Choose a mounting point that is mechanically coupled to the most important parts of your machine table. Make sure it is very unlikely you will ever need to change this new frame of reference. The fiducial must be at the same Z level as the PCB surface. More information is avaible online, please press the blue Info button (below).</p><br/><p>Home the machine by means of your controller/manually. The controller must presently work in the wanted coordinate system.</p><br/><p>Jog camera § over the fiducial. Target it roughly with the cross-hairs.</p><br/><p>Adjust the <strong>Feature diameter</strong> up and down and see if it is detected right in the camera view. A green circle and cross-hairs should appear and hug the fiducial contour. Zoom the camera using the scroll-wheel.</p><br/><p>Then press Accept to detect the precise position of the fiducial and set it up for visual homing.</p><br/><p>Note: This will not change your present machine coordinate system, but rather pin it down to the fiducial. If the mechanics were to change slightly in the future (e.g. a homing end-switch slightly moved), the homing fiducial will still be able to precisely preserve the frame of reference in X and Y.</p></html>':
'<html><p>在机器台面上安装一个永久基准点。请选择一个与机器台面最重要部位在机械上刚性相连的安装点。务必确保你今后极不可能需要更改这个新的参考系。该基准点必须与 PCB 表面处于同一 Z 高度。更多信息可在线获取，请点击下方的蓝色信息按钮。</p><br/><p>通过控制器或手动方式让机器归位。控制器当前必须工作在所期望的坐标系中。</p><br/><p>将相机 § 移动到基准点上方。用十字线大致对准它。</p><br/><p>上下调整 <strong>特征直径</strong>，观察它在相机视图中是否被正确识别。应出现一个绿色圆圈和十字线，贴合基准点轮廓。可用滚轮缩放相机视图。</p><br/><p>然后按「接受」以检测基准点的精确位置，并将其设置为用于视觉归位。</p><br/><p>注意：这不会改变你当前的机器坐标系，而是将其锚定到该基准点上。如果今后机械发生轻微变化（例如归位限位开关略有移动），归位基准点仍能在 X 和 Y 方向上精确保持该参考系。</p></html>',

'<html><p>Jog § to a suitable location where you can manually exchange the nozzle tips.</p><br/><p>Even if you (plan to) use an automatic nozzle tip changer, it is useful to have this location definied, in case you want to disable automatic changing temporarily.</p><br/><p>Often it is best to move Z all the way up so the tip is well reachable. On some head designs the uppermost Z position is blocked by a limiter, so it is the best position to apply the necessary force when inserting the nozzle tip.</p><br/><p>Note for experts: the captured location will be automatically adjusted if you change the nozzle head offsets later.</p><br/><p>Press <strong>Accept</strong> to store the location.</p><br/></html>':
'<html><p>将 § 移动到便于你手动更换吸嘴头的合适位置。</p><br/><p>即使你（打算）使用自动换嘴器，定义此位置也很有用，以防你想暂时禁用自动更换。</p><br/><p>通常最好将 Z 移到最高处，使吸嘴头便于触及。在某些机头设计中，最高 Z 位置会被限位器挡住，因此那是插入吸嘴头时施加所需力气的理想位置。</p><br/><p>专家提示：如果你之后更改吸嘴头偏移，采集的位置会自动调整。</p><br/><p>按 <strong>接受</strong> 存储该位置。</p><br/></html>',

'<html><h3>Brighness and Key-Color</h3><p>The nozzle tip and/or background (shade) is color-keyed so computer vision can robustly distinguish background pixels from foreground pixels ("green-screening"). Use for green Juki style nozzles.</p></html>':
'<html><h3>亮度与色键</h3><p>对吸嘴头和/或背景（遮光板）进行色键处理，使计算机视觉能够稳健地区分背景像素与前景像素（即「绿幕抠像」）。适用于绿色的 Juki 风格吸嘴。</p></html>',

'<html><h3>Brightness</h3><p>The background is just dark, the foreground is distinguished by brighness only.</p><br/></html>':
'<html><h3>亮度</h3><p>背景只是较暗，仅凭亮度来区分前景。</p><br/></html>',

'<html><p>Select the proper background calibration.</p><br/><p><strong color="red">CAUTION</strong>: Nozzle § will move over camera § and perform a new nozzle tip calibration calibration, including the enabled background calibration. Any problems will be indicated with purple highlights.</p><br/><p>When ready, press Accept.</p>§</html>':
'<html><p>选择适当的背景校准。</p><br/><p><strong color="red">注意</strong>：吸嘴 § 将移动到相机 § 上方，并执行一次新的吸嘴头校准，其中包含已启用的背景校准。任何问题都会以紫色高亮标示。</p><br/><p>准备就绪后，请按「接受」。</p>§</html>',

'<html><p>Up-looking camera calibration can be performed automatically by looking at a nozzle tip while moving the nozzle around in a certain pattern. This solution determines the X, Y position of the camera and it performs preliminary camera calibration.</p><br/><p>Load nozzle § with the smallest nozzle tip that you can reliably detect (it may take some trial and error).</p><br/><p>Jog nozzle § over the camera §. Target it with the cross-hairs.</p><br/><p>Jog the nozzle tip point down in Z so it is in focus. This should be more or less on the same Z level as the PCB surface. If not, consider adjusting the camera focus to make it so.</p><br/><p>If enabled, auto-focus will be used to detect the precise Z location.</p><br/><p>Adjust the <strong>Feature diameter</strong> up and down and see if it is detected right in the camera view. A green circle and cross-hairs should appear and hug the wanted contour. Zoom the camera using the scroll-wheel.</p><br/><p>Make sure to target a circular edge that can be detected consistently even when seen from the side. This means it has to be a rather sharp-angled edge. Typically, the air bore contour is targeted.</p><br/><p>Then press Accept to capture the camera position.</p></html>':
'<html><p>上视相机校准可以自动完成：让吸嘴按特定轨迹移动，同时用相机观察吸嘴头。此方案会确定相机的 X、Y 位置，并执行初步的相机校准。</p><br/><p>给吸嘴杆 § 装上你能可靠检测到的最小吸嘴头（可能需要反复试几次）。</p><br/><p>将吸嘴杆 § 移动到相机 § 上方。用十字线对准它。</p><br/><p>在 Z 方向上将吸嘴头尖端点向下移动，使其处于焦点上。这大致应与 PCB 表面处于同一 Z 高度。若不然，请考虑调整相机对焦使其如此。</p><br/><p>若已启用，将使用自动对焦来检测精确的 Z 位置。</p><br/><p>上下调整 <strong>特征直径</strong>，观察它在相机视图中是否被正确识别。应出现一个绿色圆圈和十字线，贴合所期望的轮廓。可用滚轮缩放相机视图。</p><br/><p>请务必对准一个即使从侧面观察也能稳定检测到的圆形边缘。这意味着它必须是一个角度较锐的边缘。通常对准的是气孔轮廓。</p><br/><p>然后按「接受」以采集相机位置。</p></html>',

'<html><p>For precision in computer vision it is very important that the camera image has settled down after the machine has moved the camera or the subject. Some cameras exhibit a slight lag, where the frames might still show the camera in motion. Motion might also cause vibration that must abate sufficently before computer vision is performed.</p><br/><p>The simple solution is just to wait for a fixed amount of time. However, this is wasteful if there was no motion in the first place. Using an adaptive settling method can reduce the wait time in these cases, i.e. one does not need to set a large worst case settle wait time.</p><br/>§<p>When ready, press Accept.</p>§</html>':
'<html><p>为了计算机视觉的精度，机器的相机或目标移动之后，相机图像必须已经稳定下来，这一点非常重要。有些相机存在轻微延迟，画面仍可能在显示相机处于运动之中。运动还可能引起振动，必须在执行计算机视觉之前充分衰减。</p><br/><p>简单的办法就是固定等待一段时间。然而，如果本来就没有运动，这样做就浪费了时间。使用自适应稳定方法可以在这些情况下缩短等待时间，即无需设置一个很大的最坏情况稳定等待时间。</p><br/>§<p>准备就绪后，请按「接受」。</p>§</html>',

'<html><p>Camera calibration also requires looking at a secondary fiducial at different Z level. This will provide the calibration algorithm with the needed 3D/spacial information to determine the true focal length of the lens and the optical position of the camera in space.</p><br/><p>Instructions for how to create and position the secondary fiducial must be obtained in the OpenPnP Wiki. There are very important rules that must be observed, so don\'t miss it! Press the blue Info button (below) to open the Wiki.</p><br/><p>Once you have prepared the calibration secondary fiducial you can capture its position in X, Y.</p><br/><p>Jog camera § over the secondary fiducial. Target it roughly with the cross-hairs.</p><br/><p>Adjust the <strong>Feature diameter</strong> up and down and see if it is detected right in the camera view. A green circle and cross-hairs should appear and hug the fiducial contour. Zoom the camera using the scroll-wheel.</p><br/><p>Then press Accept to capture the position.</p></html>':
'<html><p>相机校准还需要观察位于不同 Z 高度的次基准点。这将为校准算法提供所需的 3D/空间信息，以确定镜头的真实焦距以及相机在空间中的光学位置。</p><br/><p>如何制作与定位次基准点的说明请查阅 OpenPnP Wiki。其中有必须遵守的非常重要规则，切勿错过！点击下方的蓝色信息按钮可打开 Wiki。</p><br/><p>准备好校准次基准点之后，你就可以采集它在 X、Y 上的位置了。</p><br/><p>将相机 § 移动到次基准点上方。用十字线大致对准它。</p><br/><p>上下调整 <strong>特征直径</strong>，观察它在相机视图中是否被正确识别。应出现一个绿色圆圈和十字线，贴合基准点轮廓。可用滚轮缩放相机视图。</p><br/><p>然后按「接受」以采集该位置。</p></html>',

'<html><h3>Detect the firmware automatically</h3><p>The M115 command must be supported by the firmware. Make sure the controller is connected to the computer and accept the solution to perform the detection.</p><br/><p>This might take a while!</p><br/><p>If the firmware is known by OpenPnP, it will be able to automatically generate G-code configuration for you.</html>':
'<html><h3>自动检测固件</h3><p>固件必须支持 M115 命令。请确保控制器已连接到计算机，并接受该方案以执行检测。</p><br/><p>这可能需要一段时间！</p><br/><p>如果 OpenPnP 认识该固件，它就能为你自动生成 G 代码配置。</html>',

'<html><h3>Assume a generic G-code controller</h3><p>When the M115 command is not supported by your controller you can let OpenPnP propose a generic G-code configuration.</p><br/><p>You will likely need to hand-tune the G-code configuration to work with your controller.</p></html>':
'<html><h3>假定为通用 G 代码控制器</h3><p>当你的控制器不支持 M115 命令时，可以让 OpenPnP 生成一套通用 G 代码配置。</p><br/><p>你很可能需要手动调整 G 代码配置，才能与你的控制器配合使用。</p></html>',

'<html><h3>Use Auto-Focus</h3><p>This is the recommended setting.</p></html>':
'<html><h3>使用自动对焦</h3><p>这是推荐设置。</p></html>',

'<html><h3>Use nozzle Z location</h3><p><span style="color:red;">CAUTION:</span> This will invalidate part height auto detection using auto focus.</p></html>':
'<html><h3>使用吸嘴 Z 位置</h3><p><span style="color:red;">注意：</span>这将使基于自动对焦的元件高度自动检测失效。</p></html>',

'<html><p>Once the calibration primary fiducial is captured you can use it to capture the camera head offsets (first approximation).</p><br/><p>Jog camera § over the primary fiducial. Target it with the cross-hairs.</p><br/><p>Adjust the <strong>Feature diameter</strong> up and down and see if it is detected right in the camera view. A green circle and cross-hairs should appear and hug the fiducial contour. Zoom the camera using the scroll-wheel.</p><br/><p>Then press Accept to capture the offsets. The camera will perform a small calibration movement </html>':
'<html><p>采集到主校准基准点之后，你就可以用它来采集相机机头偏移量（初次近似）。</p><br/><p>将相机 § 移动到主基准点上方。用十字线对准它。</p><br/><p>上下调整 <strong>特征直径</strong>，观察它在相机视图中是否被正确识别。应出现一个绿色圆圈和十字线，贴合基准点轮廓。可用滚轮缩放相机视图。</p><br/><p>然后按「接受」以采集偏移量。相机将执行一小段校准运动</html>',

'<html><p>It is recommended to enable nozzle tip calibration for run-out and precision camera offsets. For more information, press the blue Info button (below) to open the Wiki.</p><br/>§<p>Press the <strong>Center Nozzle</strong> button (below) to center nozzle § over the camera §.</p><br/><p>Adjust the <strong>Feature diameter</strong> up and down and see if it is detected right in the camera view. A green circle and cross-hairs should appear and hug the wanted contour. Zoom the camera using the scroll-wheel. Make sure to target a circular edge that can be detected consistently even when seen from the side. This means it has to be a rather sharp-angled edge. To eliminate nozzle and camera tilt errors, choose a contour that is lowest in Z on the nozzle tip. Typically, the air bore contour is targeted.</p><br/><p>Then press Accept to enable and perform the nozzle tip calibration.</p></html>':
'<html><p>建议启用吸嘴头校准，以获得偏心量与精确的相机偏移量。更多信息请点击下方的蓝色信息按钮打开 Wiki。</p><br/>§<p>按 <strong>吸嘴居中</strong> 按钮（下方），将吸嘴杆 § 居中到相机 § 上方。</p><br/><p>上下调整 <strong>特征直径</strong>，观察它在相机视图中是否被正确识别。应出现一个绿色圆圈和十字线，贴合所期望的轮廓。可用滚轮缩放相机视图。请务必对准一个即使从侧面观察也能稳定检测到的圆形边缘。这意味着它必须是一个角度较锐的边缘。为消除吸嘴与相机的倾斜误差，请选择吸嘴头上 Z 最低的轮廓。通常对准的是气孔轮廓。</p><br/><p>然后按「接受」，以启用并执行吸嘴头校准。</p></html>',

'<html><p>Once the calibration § fiducial is captured in X, Y you can use it to capture the nozzle head offsets (first approximation).</p><br/>§§<p>Jog nozzle § over the § fiducial. Lower the nozzle tip down until it touches the fiducial.</p><br/><p><strong style="color:red;">CAUTION:</strong> this is a very important Z coordinate, please capture it with care.</p><br/><p>Then press Accept to capture the nozzle head offsets.</p></html>':
'<html><p>在 X、Y 上采集到校准 § 基准点之后，你就可以用它来采集吸嘴机头偏移量（初次近似）。</p><br/>§§<p>将吸嘴杆 § 移动到 § 基准点上方。将吸嘴头下降，直到它触碰基准点。</p><br/><p><strong style="color:red;">注意：</strong>这是一个非常重要的 Z 坐标，请谨慎采集。</p><br/><p>然后按「接受」以采集吸嘴机头偏移量。</p></html>',

'<html><p>With <strong>Dynamic Safe Z</strong> enabled, the nozzles need a head-room, the so-called Safe Z Zone to lift the nozzles higher with taller parts. On nozzles with shared Z axes the part heights compete for the same head-room. The maximum expected part height is specified on the nozzle tip <strong>Max. Part Height</strong>.</p><br/><p>Nozzle § with compatible tip § has a <strong>Max. Part Height</strong> of §, furthermore, nozzle § with compatible tip § has a largest <strong>Max. Part Height</strong> of §, which in combination (and after transformation) is larger than the Safe Z Zone of §. Note, the safe Z Zone is configured on the § axis to reach from § to § in (untransformed) coordinates.</p><br/><p>Please either enlarge the Safe Z Zone, by reducing the nozzle § and § Z clearances, or reduce the <strong>Max. Part Height</strong> on nozzle tips § and §.</p><br/><p>Reducing Z clearances is best done by revisiting the Safe Z solutions for nozzles § and §. Enable the <strong>Include Solved?</strong> checkbox at the top, then reopen the "Set Safe Z of §" solution and redo it.</p></html>':
'<html><p>启用<strong>动态安全 Z</strong>后，吸嘴需要一定的抬升空间，即所谓的安全 Z 区，以便在元件较高时将吸嘴抬得更高。对于共用 Z 轴的吸嘴，各元件的高度会争用同一段抬升空间。元件的最大预期高度在吸嘴头的 <strong>最大元件高度</strong> 中指定。</p><br/><p>吸嘴杆 § 配兼容吸嘴头 § 的 <strong>最大元件高度</strong> 为 §；此外，吸嘴杆 § 配兼容吸嘴头 § 的最大 <strong>最大元件高度</strong> 为 §，两者组合（经变换后）大于 § 的安全 Z 区。注意，安全 Z 区配置在 § 轴上，（未变换的）坐标范围为 § 至 §。</p><br/><p>请通过减小吸嘴杆 § 与 § 的 Z 间隙来扩大安全 Z 区，或者减小吸嘴头 § 与 § 上的 <strong>最大元件高度</strong>。</p><br/><p>减小 Z 间隙的最佳做法是重新审视吸嘴杆 § 与 § 的安全 Z 方案。勾选顶部的 <strong>包含已解决？</strong> 复选框，然后重新打开「设置 § 的安全 Z」方案并重做。</p></html>',

'<html><span color="red">CAUTION:</span>  This is a troubleshooting option offered to remove the GcodeAsyncDriver if it causes problems, or if you don\'t want it after all. Going back to the plain GcodeDriver will lose you all the advanced configuration.</html>':
'<html><span color="red">注意：</span>这是一个故障排查选项，用于在 GcodeAsyncDriver 导致问题、或你终究不想要它时将其移除。退回普通 GcodeDriver 会丢失所有高级配置。</html>',

'<html><p>Camera calibration can be performed automatically by looking at fiducials while moving the camera around in a certain pattern. This solution determines the X, Y position of the primary fiducial and it performs preliminary camera calibration.</p><br/><p>Instructions for how to create and position the primary fiducial must be obtained in the OpenPnP Wiki. <strong>There are very important rules that must be observed!</strong> Press the blue Info button (below) to open the Wiki.</p><br/><p>Once you have prepared the calibration primary fiducial you can capture its position in X, Y.</p><br/><p>Jog camera § over the privary fiducial. Target it roughly with the cross-hairs.</p><br/><p>Adjust the <strong>Feature diameter</strong> up and down and see if it is detected right in the camera view. A green circle and cross-hairs should appear and hug the fiducial contour. Zoom the camera using the scroll-wheel.</p><br/><p>Then press Accept to capture the position. The camera will perform a small calibration movement pattern</p></html>':
'<html><p>相机校准可以自动完成：让相机按特定轨迹移动，同时观察基准点。此方案会确定主基准点的 X、Y 位置，并执行初步的相机校准。</p><br/><p>如何制作与定位主基准点的说明请查阅 OpenPnP Wiki。<strong>其中有必须遵守的非常重要规则！</strong>点击下方的蓝色信息按钮可打开 Wiki。</p><br/><p>准备好校准主基准点之后，你就可以采集它在 X、Y 上的位置了。</p><br/><p>将相机 § 移动到主基准点上方。用十字线大致对准它。</p><br/><p>上下调整 <strong>特征直径</strong>，观察它在相机视图中是否被正确识别。应出现一个绿色圆圈和十字线，贴合基准点轮廓。可用滚轮缩放相机视图。</p><br/><p>然后按「接受」以采集该位置。相机将执行一小段校准运动</p></html>',

'<html>§<p>Color-keyed computer vision needs stable, and accurate colors. Neither the unstable Auto white balance, nor the device manual white balance is suitable (typically merely a red-blue-shift).Therefore OpenPnP offers its own elaborate and static white balance. You can automatically calibrate it now.</p><br/><p>Make sure a suitable white balance calibration object is visible in the camera view. Brushed metal and paper are recommended. The camera should see all brightness levels, i.e., an assortment of metal objects with holes, bevels, shadows etc. usually provides good gradients.Conversely, make sure there are no colored objects visible. Lighting conditions must be as in operation.<p><br/><p>Alternatively, you can perform white balance on camera §\'s <strong>White Balance</strong> tab.</p><br><p>Press the blue info button (below) for more information.</p><br><p>When ready, press Accept.</p></html>':
'<html>§<p>色键计算机视觉需要稳定而准确的色彩。无论是不稳定的自动白平衡，还是设备的手动白平衡都不合适（通常只是红蓝偏移而已）。因此 OpenPnP 提供了自己精心设计的静态白平衡。你现在可以自动校准它。</p><br/><p>请确保相机视图中能看到合适的白平衡校准物体。推荐使用拉丝金属和纸张。相机应能看到所有亮度层级，即由带孔洞、倒角、阴影等的金属物件组成的组合通常能提供良好的渐变。反之，请确保视野中没有彩色物体。光照条件必须与实际作业时一致。<p><br/><p>或者，你也可以在相机 § 的 <strong>白平衡</strong> 标签页上执行白平衡。</p><br><p>点击下方的蓝色信息按钮可获取更多信息。</p><br><p>准备就绪后，请按「接受」。</p></html>',

'<html><span color="red">CAUTION:</span> This is a troubleshooting option offered to remove the ContactProbeNozzle if it causes problems, or if you don\'t want it after all. Going back to the plain ReferenceNozzle will lose you all the configuration for contact and Z probing and calibration.</html>':
'<html><span color="red">注意：</span>这是一个故障排查选项，用于在 ContactProbeNozzle 导致问题、或你终究不想要它时将其移除。退回普通 ReferenceNozzle 会丢失所有接触式探测与 Z 探测及校准的配置。</html>',

'<html>Determines, whether this transformation is a compensation transformation e.g. Non-Squareness Compensation.<br/>\r\nThis can be used by OpenPnP to optimize some motion where precision is not needed. Initial calibration <br/>and simulation are other applications. \r\n</html>':
'<html>确定此变换是否为补偿型变换，例如非垂直度补偿。<br/>\r\nOpenPnP 可利用它来优化某些不需要精度的运动。初始校准<br/>\r\n与仿真也是其他应用场景。\r\n</html>',

'<html>Choose two exemplary points on the axis that you like to map.<br/>\r\nSet the desired Input and Output to create an Offset, Scaling, Negating (etc.).<br/>\r\nNote, the range will not be limited to these points they are just examples.\r\n</html>':
'<html>在轴上选择两个要映射的示例点。<br/>\r\n设置所需的输入与输出，以建立偏移、缩放、取反（等）关系。<br/>\r\n注意，范围不会限制在这两个点上，它们只是示例。\r\n</html>',

'<html>Cam Wheel Radius and Gap are deprecated.<br/>\nIssues & Solutions can fix existing configurations <br/>\nwithout losing captured Z coordinates. </html>':
'<html>凸轮半径与间隙已废弃。<br/>\n「问题与解决方案」可以修复现有配置，<br/>\n且不会丢失已采集的 Z 坐标。</html>',

'<html>Calibrate the nozzle Z offset by contact-probing against the <strong>Touch Location</strong> defined in the Nozzle Tip.</html>':
'<html>通过接触探测吸嘴头中定义的 <strong>触碰位置</strong> 来校准吸嘴 Z 偏移。</html>',

'<html>\nReplace driver connections with a built-in GcodeServer, simulating the real driver.<br/>\nWill only become effective when you disable/enable the machine.\n</html>':
'<html>\n用内置的 GcodeServer 替换驱动器连接，以模拟真实驱动器。<br/>\n只有在你禁用/启用机器后才会生效。\n</html>',

'<html>Be aware that runout will be apparent as an offset in the cross-hairs of the Down-looking Camera, whenever the the Nozzle is positioned. This also happens when watching a Job perform.<html>':
'<html>请注意，只要吸嘴被定位，偏心量就会在下视相机的十字线中表现为一个偏移。在观察作业执行时也会出现这种情况。<html>',

'<html>\r\nCreates simulated noise in the camera image (number of sparks) <br/>\r\nto satisfy Camera Settling that the frame has changed. \r\n</html>':
'<html>\r\n在相机图像中生成模拟噪声（火花数量），<br/>\r\n以使相机稳定机制认为画面已发生变化。\r\n</html>',

'<html>\r\nSimulates an initial homing error by that offset. Used to test visial homing. <br/>\r\nSet the homing fiducial to the PCB fiducial in the lower left corner of the test image.<br/>\r\nUse coordinates 5.736, 6.112 to get original coordinates through Visual homing.\r\n</html>':
'<html>\r\n按该偏移量模拟一个初始归位误差。用于测试视觉归位。<br/>\r\n将归位基准点设为测试图像左下角的 PCB 基准点。<br/>\r\n使用坐标 5.736、6.112，即可通过视觉归位得到原始坐标。\r\n</html>',

'<html>Add a new profile.</html>':
'<html>添加新配置档。</html>',

'<html>Move the profile down one position.</html>':
'<html>将配置档下移一位。</html>',

'<html>\r\nUse a parametric template to encode non-boolean actuation values into the URL.<br/>\r\nThe {val} placeholder can be used. <br/>\r\nFormatting is possible in the form of {val:%f} etc.<br/>\r\n<br/>\r\n<strong>Note:</strong> no escaping is performed. If using String actuation values, <br/>\r\nyou can use complex URI fragments e.g. drive multiple parameters. \r\n</html>':
'<html>\r\n使用参数化模板将非布尔型触发值编码到 URL 中。<br/>\r\n可以使用 {val} 占位符。<br/>\r\n可通过 {val:%f} 等形式进行格式化。<br/>\r\n<br/>\r\n<strong>注意：</strong>不会执行任何转义。若使用字符串型触发值，<br/>\r\n你可以使用复杂的 URI 片段，例如驱动多个参数。\r\n</html>',

'<html>Delete the selected profile.</html>':
'<html>删除选中的配置档。</html>',

'<html>Probing speed factor.<br/>\r\n<strong>NOTE:</strong> this setting will only become effective, once you<br/>\r\naccept the Issues & Solutions G-code suggestion.</html>':
'<html>探测速度系数。<br/>\r\n<strong>注意：</strong>只有在你接受<br/>\r\n「问题与解决方案」的 G 代码建议后，此设置才会生效。</html>',

'<html>Contact probing start offset in Z above the nominal location.<br/>\r\nNote: for part height probing, the maximum part height on the NozzleTip <br/>\r\nis used instead, if the part height is not yet known. \r\n</html>':
'<html>接触探测在标称位置之上的 Z 起始偏移。<br/>\r\n注意：对于元件高度探测，若元件高度尚未已知，<br/>\r\n则改用吸嘴头上配置的最大元件高度。\r\n</html>',

'<html>\r\nContact probing final adjustment in Z (positive values point upwards in Z).<br/>\r\n<ul>\r\n<li>Use positive values to compensate probing overshoot.</li>\r\n<li>Use negative values to add additional nozzle tip spring tensioning.</li>\r\n</ul>\r\n</html>':
'<html>\r\n接触探测在 Z 方向的最终修正量（正值指向 Z 轴正方向）。<br/>\r\n<ul>\r\n<li>使用正值来补偿探测过冲。</li>\r\n<li>使用负值来增加吸嘴头的弹簧预紧力。</li>\r\n</ul>\r\n</html>',

'<html>Probe for feeder heights. On some feeder types, this can probe for the <strong>Part Height</strong>, when it is unknown.</html>':
'<html>探测供料器高度。对于某些供料器类型，当 <strong>元件高度</strong> 未知时，可用它来探测该高度。</html>',

'<html>Probe for placement heights. Includes probing for <strong>Part Height</strong>, when it is unknown.</html>':
'<html>探测贴装高度。当 <strong>元件高度</strong> 未知时，也包含对该高度的探测。</html>',

'<html>Enable contact probing for discard. There must be a surface that the nozzle<br/>\r\ncan probe into that is likely to brush/tilt off a part from the nozzle, like a (ESD safe) soft<br/>\r\nmaterial or a slanted surface. \r\n</html>':
'<html>为抛料启用接触探测。必须存在一个吸嘴<br/>\r\n可以探入的表面，它应能刷落/掀落吸嘴上的元件，<br/>\r\n例如（防静电的）软质材料或倾斜面。\r\n</html>',

'<html>\r\nOn interlock the actuator will be read and the numeric value compared to this range <br/>\r\n(lower/upper limit). If the value is outside the range, the interlock fails, i.e. an error is raised.\r\n</html>':
'<html>\r\n联锁时，会读取执行器的值，并将该数值与此范围<br/>\r\n（下限/上限）比较。若数值超出范围，则联锁失败，即抛出错误。\r\n</html>',

'<html>\r\nOn interlock the actuator will be read. The reading will be compared to the pattern.<br/>\r\nIf the reading does not match, the interlock fails, i.e. an error is raised. \r\n</html>':
'<html>\r\n联锁时，会读取执行器的值。该读数将与模式进行比对。<br/>\r\n若读数不匹配，则联锁失败，即抛出错误。\r\n</html>',

'<html>The interlock is only active if the effective speed factor is within this range.<br/>\r\nTypically used to allow slow movement even when the interlock confirmation failed.\r\n</html>':
'<html>仅当有效速度系数处于此范围内时，联锁才生效。<br/>\r\n通常用于在联锁确认失败时仍允许缓慢移动。\r\n</html>',

'<html>Move the profile up one position.</html>':
'<html>将配置档上移一位。</html>',

'<html><span color="red">CAUTION:</span> This is a troubleshooting option, offered to remove the ReferenceAdvancedMotionPlanner if it causes problems, or if you don\'t want it after all. Going back to the plain NullPlanner will lose you all the advanced configuration.</html>':
'<html><span color="red">注意：</span>这是一个故障排查选项，用于在 ReferenceAdvancedMotionPlanner 导致问题、或你终究不想要它时将其移除。退回普通 NullPlanner 会丢失所有高级配置。</html>',

'<html><body>Jog the camera so that an easily identifiable feature of the object (such as a sharp corner) is in the camera\'s field-of-view (FOV). It is better for the feature to be towards the edge of the FOV rather than centered. When ready, click the mouse on the feature to capture its apparent position.</body></html>':
'<html><body>移动相机，使目标上一个易于识别的特征（例如锐利的角）位于相机视场（FOV）内。该特征最好靠近视场边缘而不是居中。准备就绪后，用鼠标点击该特征以采集其表观位置。</body></html>',

'<html><body>Now jog the camera in X and/or Y so that the same feature is visible in another part of the camera\'s FOV. The farther away from the original position, the better.  When ready, click the mouse on the feature to capture its new apparent position and estimate its Z coordinate.</body></html>':
'<html><body>现在在 X 和/或 Y 方向移动相机，使同一特征出现在相机视场的另一处。离原始位置越远越好。准备就绪后，用鼠标点击该特征以采集其新的表观位置并估算其 Z 坐标。</body></html>',

'<html><body>The estimated Z coordinate of the feature is <b>%s</b>. Click Cancel if finished or Again to perform another measurment.</body></html>':
'<html><body>该特征的估算 Z 坐标为 <b>%s</b>。若已完成请点击「取消」，或点击「再次」以进行下一次测量。</body></html>',

'<html><body>Jog the nozzle so that an easily identifiable feature of the object (such as a sharp corner) is in the camera\'s field-of-view (FOV). It is better for the feature to be towards the edge of the FOV rather than centered. When ready, click the mouse on the feature to capture its apparent position.</body></html>':
'<html><body>移动吸嘴，使目标上一个易于识别的特征（例如锐利的角）位于相机视场（FOV）内。该特征最好靠近视场边缘而不是居中。准备就绪后，用鼠标点击该特征以采集其表观位置。</body></html>',

'<html><body>Now jog the nozzle in X and/or Y so that the same feature is visible in another part of the camera\'s FOV. The farther away from the original position, the better.  When ready, click the mouse on the feature to capture its new apparent position and estimate its Z coordinate.</body></html>':
'<html><body>现在在 X 和/或 Y 方向移动吸嘴，使同一特征出现在相机视场的另一处。离原始位置越远越好。准备就绪后，用鼠标点击该特征以采集其新的表观位置并估算其 Z 坐标。</body></html>',

'<html><body>Select two or more (four or more is better) easily identifiable placements in the placements table. They should be near the corners of the board. Click Next to continue and the camera will move near one of the selected placements.</body></html>':
'<html><body>在贴装表中选取两个或更多（四个或更多更好）易于识别的贴装。它们应位于板的角附近。点击「下一步」继续，相机将移动到所选贴装之一附近。</body></html>',

'<html><body>Now, manually jog the camera\'s crosshairs over the center of %s. Try to be as precise as possible. Click Next to continue to the next placement.</body></html>':
'<html><body>现在，手动将相机十字线移动到 %s 的中心上方。请尽量精确。点击「下一步」继续到下一个贴装。</body></html>',

'<html><body>The board\'s location and rotation have been set. Click Finish to position the camera at the board\'s origin, or Cancel to reject the changes.</body></html>':
'<html><body>板的位置与旋转已设置完成。点击「完成」将相机定位到板原点，或点击「取消」放弃这些更改。</body></html>',

'<html><body>Select two or more (four or more is better) easily identifiable placements in the placements table. They should be near the corners of the board. Click Next to continue.</body></html>':
'<html><body>在贴装表中选取两个或更多（四个或更多更好）易于识别的贴装。它们应位于板的角附近。点击「下一步」继续。</body></html>',

'<html><body>Camera position can be offset with jog or by selecting position in the camera view. Click Next to continue.</body></html>':
'<html><body>可通过点动或在相机视图中选择位置来偏移相机位置。点击「下一步」继续。</body></html>',

'<html><body>Click on what will become the upper left corner of your region of interest. Click again to reset and retry. Click Next to continue.</body></html>':
'<html><body>点击将成为你感兴趣区域左上角的点。再次点击可重置并重试。点击「下一步」继续。</body></html>',

'<html><body>Now, click on what will become the upper right corner of your region of interest. Click again to reset and retry. Click Next to continue.</body></html>':
'<html><body>现在，点击将成为你感兴趣区域右上角的点。再次点击可重置并重试。点击「下一步」继续。</body></html>',

'<html><body>Next, click on what will become the lower left corner of your region of interest. Click again to reset and retry. Click Next to continue.</body></html>':
'<html><body>接下来，点击将成为你感兴趣区域左下角的点。再次点击可重置并重试。点击「下一步」继续。</body></html>',

'<html><body>Finally, click to toggle beween a rectangular and parallelogrammatic region. Click Next to continue.</body></html>':
'<html><body>最后，点击以在矩形区域与平行四边形区域之间切换。点击「下一步」继续。</body></html>',

'<html><body>The region of interest has been defined. Click Finish to accept it, or Cancel to quit.</body></html>':
'<html><body>感兴趣区域已定义完成。点击「完成」接受它，或点击「取消」退出。</body></html>',

'<html><body>Processing calibration data - this may take a few seconds.</body></html>':
'<html><body>正在处理校准数据 —— 这可能需要几秒钟。</body></html>',

'<html>This will overwrite the Z reference and therefore<br/>change the meaning of previously captured Z coordinates.<br/><span color="red">You will need to recapture these locations!</span><br/><br/>Are you sure?</html>':
'<html>这会覆盖 Z 参考基准，从而<br/>改变此前已采集的 Z 坐标的含义。<br/><span color="red">你将需要重新采集这些位置！</span><br/><br/>你确定吗？</html>',

'<html>This will position the nozzle § over the camera §. <br/><br/><span style="color:red;">CAUTION:</span> Nozzle head offset, nozzle Safe Z, camera <br/>location, basic motion etc. must already be set up.<br/><br/>Are you sure?</html>':
'<html>这会将吸嘴 § 定位到相机 § 上方。<br/><br/><span style="color:red;">注意：</span>吸嘴机头偏移、吸嘴安全 Z、相机<br/>位置、基本运动等必须已设置完成。<br/><br/>你确定吗？</html>',

'<html>This will move camera § over to the position of the nozzle §. <br/><br/><span style="color:red;">CAUTION:</span> Nozzle head offset, nozzle Safe Z, basic <br/>motion etc. must already be set up.<br/><br/>Are you sure?</html>':
'<html>这会将相机 § 移动到吸嘴 § 的位置。<br/><br/><span style="color:red;">注意：</span>吸嘴机头偏移、吸嘴安全 Z、基本<br/>运动等必须已设置完成。<br/><br/>你确定吗？</html>',

# ----- 其他 HTML/半 HTML 提示 -----
'<strong color="red">Controlled by pipeline caller: §=§</strong><br/><br/>§':
'<strong color="red">由管线调用方控制：§=§</strong><br/><br/>§',

'<strong style="color:red;">CAUTION, Quick&Dirty Hack:</strong> This will auto-detect the font size upwards and downwards of your currently set pointSize. This is a one-shot option, used while editing the pipeline. Once the detection is done, the switch is cleared.<br/>The process may take a while and appear to hang, be patient. Afterwards you need to switch stages to refresh the GUI.':
'<strong style="color:red;">注意，简易临时方案：</strong>这会从你当前设置的 pointSize 起向上和向下自动检测字体大小。这是一次性选项，用于编辑管线时。一旦检测完成，该开关会被清除。<br/>该过程可能需要一段时间，看起来像卡住了，请耐心等待。之后你需要切换阶段以刷新界面。',

'<p>Feeder §: current part §, OCR part §. Action performed: §.</p>':
'<p>供料器 §：当前元件 §，OCR 识别元件 §。已执行的操作：§。</p>',

'<br/><p color="red">This feeder is marked as template. Are you really, really sure?</p>':
'<br/><p color="red">此供料器被标记为模板。你真的、真的确定吗？</p>',

'<tr><td align="right">Previous Nozzle Head Offsets:</td><td>§</td></tr><tr><td align="right">Difference:</td><td>§</td></tr>':
'<tr><td align="right">此前的吸嘴机头偏移：</td><td>§</td></tr><tr><td align="right">差值：</td><td>§</td></tr>',

'<br/><h4>Results:</h4><table><tr><td align="right">Detected Nozzle Head Offsets:</td><td>§</td></tr>§</table>':
'<br/><h4>结果：</h4><table><tr><td align="right">检测到的吸嘴机头偏移：</td><td>§</td></tr>§</table>',

'<br/><h4>Results:</h4><table><tr><td align="right">Detected Backlash:</td><td>§</td></tr><tr><td align="right">Selected Method:</td><td>§</td></tr><tr><td align="right">Sneak-up Distance:</td><td>§</td></tr><tr><td align="right">Speed Factor:</td><td>§</td></tr><tr><td align="right">Applicable Resolution:</td><td>§ mm</td></tr></table>':
'<br/><h4>结果：</h4><table><tr><td align="right">检测到的反向间隙：</td><td>§</td></tr><tr><td align="right">所选方式：</td><td>§</td></tr><tr><td align="right">逼近距离：</td><td>§</td></tr><tr><td align="right">速度系数：</td><td>§</td></tr><tr><td align="right">适用分辨率：</td><td>§ mm</td></tr></table>',

'<br/><p>Note: optimizing Safe Z will improve your overall motion speed, however your nozzles may appear unbalanced and they will sometimes see-saw during motion. If you rather prefer a strictly symmetric appearance, you might want to dismiss this solution, and setup Safe Z manually.</p>':
'<br/><p>注意：优化安全 Z 会改善整体运动速度，但你的吸嘴看起来可能不齐平，运动过程中有时会像跷跷板一样上下摆动。如果你更希望严格对称的外观，可以放弃此方案并手动设置安全 Z。</p>',

'<br/><h4>Results</h4><p style="max-width: 40em">§</p><br/><p>More information on the Calibration tab of nozzle tip §.</p>':
'<br/><h4>结果</h4><p style="max-width: 40em">§</p><br/><p>更多信息请参见吸嘴头 § 的「校准」标签页。</p>',

'<p><strong color="red">CAUTION</strong>: The camera § will move over the primary fiducial and then perform a camera settling test pattern.</p><br/>':
'<p><strong color="red">注意</strong>：相机 § 将移动到主基准点上方，然后执行一段相机稳定测试轨迹。</p><br/>',

'<p><strong color="red">CAUTION</strong>: The § § will move to the camera § and then perform a camera settling test pattern.</p><br/>':
'<p><strong color="red">注意</strong>：§ § 将移动到相机 § 处，然后执行一段相机稳定测试轨迹。</p><br/>',

'<br/><h4>Results</h4><table><tr><td>Selected method:</td><td>§</td></tr><tr><td>Compute time:</td><td>§ ms per frame</td></tr><tr><td>Settle time:</td><td>§ ms</td></tr></table><br/>§<p>More information on the Camera Settling tab of camera §.</p>':
'<br/><h4>结果</h4><table><tr><td>所选方式：</td><td>§</td></tr><tr><td>计算耗时：</td><td>每帧 § ms</td></tr><tr><td>稳定时间：</td><td>§ ms</td></tr></table><br/>§<p>更多信息请参见相机 § 的「相机稳定」标签页。</p>',

'<p>Load nozzle tip § to nozzle §.</p><br/>':
'<p>将吸嘴头 § 装到吸嘴杆 §。</p><br/>',

'<p>Nozzle tip § is already loaded on nozzle §.</p><br/>':
'<p>吸嘴杆 § 上已装有吸嘴头 §。</p><br/>',

'<p>This will also capture the calibration § fiducial Z coordinate.</p><br/>':
'<p>这还会采集校准 § 基准点的 Z 坐标。</p><br/>',

'<p>This will also equalize Z of nozzle § to Z of the default nozzle §.</p><br/>':
'<p>这还会将吸嘴杆 § 的 Z 与默认吸嘴杆 § 的 Z 对齐一致。</p><br/>',

'<p><strong color="red">CAUTION:</strong> A non-zero head offsets Z has been detected on default nozzle §. Accepting this solution will reset it to zero, creating the new reference in Z. This will change the meaning of Z coordinates that have already been captured. Do not accept this solution, unless you are confident this is OK. In the worst case, this may lead to machine collisions! <strong color="red">You have been warned!</strong></p><br/>':
'<p><strong color="red">注意：</strong>在默认吸嘴杆 § 上检测到非零的机头偏移 Z。接受此方案会将其重置为零，从而在 Z 方向建立新的参考基准。这会改变已采集的 Z 坐标的含义。除非你确信这样做没问题，否则不要接受此方案。最坏情况下，这可能导致机器碰撞！<strong color="red">已经警告过你了！</strong></p><br/>',

'<p><strong color="red">WARNING:</strong> make sure the device properties are set as recommended by Issues & Solutions. Press <strong>Find Issues & Solutions</strong> to check for the latest status. Proceed only when you are sure the properties are OK, white balance must be computed as the last step.</p><br/>':
'<p><strong color="red">警告：</strong>请确保设备属性已按「问题与解决方案」的建议设置。按 <strong>查找问题与解决方案</strong> 检查最新状态。只有在你确信属性无误时才继续，白平衡必须作为最后一步来计算。</p><br/>',

'<span style="color:red">WARNING: No move to Safe Z!</span><br/>':
'<span style="color:red">警告：未移动到安全 Z！</span><br/>',

}
