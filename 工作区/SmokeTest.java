import java.io.*;
import java.util.zip.*;
import java.lang.reflect.*;

/** 仅加载主类并触发静态初始化，验证常量池改动后类可正常链接。 */
public class SmokeTest {
    public static void main(String[] args) throws Exception {
        String jar = args[0];
        String[] probe = {
            "org.openpnp.machine.reference.solutions.NozzleTipSolutions$3",
            "org.openpnp.machine.reference.solutions.VisionSolutions$2",
            "org.openpnp.machine.reference.solutions.CameraSolutions$5",
            "org.openpnp.machine.reference.solutions.CalibrationSolutions$1",
            "org.openpnp.machine.reference.solutions.KinematicSolutions$4",
            "org.openpnp.machine.reference.ReferenceNozzle",
            "org.openpnp.machine.reference.driver.GcodeDriver",
            "org.openpnp.model.MotionProfile",
            "org.openpnp.gui.FeedersPanel",
        };
        java.net.URLClassLoader cl = new java.net.URLClassLoader(
            new java.net.URL[]{ new java.io.File(jar).toURI().toURL() });
        int ok=0, fail=0;
        for (String n : probe) {
            try {
                Class<?> c = Class.forName(n, false, cl);
                // 读取一个被翻译的常量池字符串，确认可解析
                c.getName();
                System.out.println("LOAD OK   " + n);
                ok++;
            } catch (Throwable t) {
                System.out.println("LOAD FAIL " + n + " -> " + t);
                fail++;
            }
        }
        System.out.println("SMOKE OK=" + ok + " FAIL=" + fail);
    }
}
