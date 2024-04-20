import java.io.File;
import java.nio.file.Paths;
import java.lang.*;

public class DisplayFileSize {
   public static long getFileSize(String filename) {
      File file = new File(filename);
      if (!file.exists() || !file.isFile()) {
         System.out.println("File doesn\'t exist");
         return -1;
      }
      return file.length();
   }
   public static void main(String[] args) 
     {
      String file = "Server1.java";
      long size = getFileSize(Paths.get(System.getProperty("user.dir"),file).toString());      
      System.out.println("File size in Kilo Bytes: " + size/(1024) +"KB");
     }
}