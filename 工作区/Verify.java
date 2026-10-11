import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.zip.*;

public class Verify {
    public static void main(String[] args) throws Exception {
        String jar = args[0];
        int ok = 0, fail = 0;
        List<String> errs = new ArrayList<>();
        try (ZipFile zf = new ZipFile(jar)) {
            Enumeration<? extends ZipEntry> en = zf.entries();
            while (en.hasMoreElements()) {
                ZipEntry ze = en.nextElement();
                if (!ze.getName().endsWith(".class")) continue;
                byte[] data;
                try (InputStream in = zf.getInputStream(ze)) {
                    data = in.readAllBytes();
                }
                try {
                    // 用自定义 ClassLoader 只做 defineClass，不解析依赖
                    new Loader().define(data);
                    ok++;
                } catch (Throwable t) {
                    fail++;
                    if (errs.size() < 10) errs.add(ze.getName() + " -> " + t);
                }
            }
        }
        System.out.println("CLASS VERIFY OK=" + ok + " FAIL=" + fail);
        for (String e : errs) System.out.println("  " + e);
    }
    static class Loader extends ClassLoader {
        Class<?> define(byte[] b) { return defineClass(null, b, 0, b.length); }
    }
}
