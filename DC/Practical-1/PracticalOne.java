import java.io.*;

public class PracticalOne {

   @SuppressWarnings("deprecation")
   public static void main(String args[]) {
      Process mainProcess = null;
      BufferedReader inStream = null;

      try {
         // execute command (compile namaste.java file)
         Runtime.getRuntime().exec("javac Namaste.java");
         // run Namaste file
         mainProcess = Runtime.getRuntime().exec("java Namaste");

      } catch (IOException e) {

         e.printStackTrace();
      }

      try {
         inStream = new BufferedReader(
               new InputStreamReader(mainProcess.getInputStream()));
         // read lines
         System.out.println(inStream.readLine());
         // exit the program once completed
         System.exit(0);
      } catch (IOException e) {
         System.err.println("Error on inStream.readLine()");
         e.printStackTrace();
      }
   }
}