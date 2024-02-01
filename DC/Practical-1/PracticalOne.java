/*
Ref: 
https://docs.oracle.com/javase/8/docs/api/java/lang/Process.html#Process--
https://docs.oracle.com/javase/8/docs/api/java/io/BufferedReader.html
*/
/* 
import all packages inside java.io.*
"*" means all
*/
import java.io.*;

// create a public class (it should be same as filename)
public class PracticalOne {

   // main method where the code begins to execute
   // args is command line arguments
   // eg: java FileName message="hello"
   // messsage is argument

   @SuppressWarnings("deprecation")
   public static void main(String args[]) {

      //creating variable that will hold the process that will execute Namaste.java
      Process mainProcess = null;
      // creating variable to store output of the process (Namaste.java)
      BufferedReader inStream = null;

      // try catch block to handle exceptions/error (something unexpected that you
      // want to avoid at first place but handle it well when it happens)
      try {
         // execute command (compile namaste.java file)
         Runtime.getRuntime().exec("javac Namaste.java");
         // run Namaste file
         mainProcess = Runtime.getRuntime().exec("java Namaste");

      } catch (IOException e) {

         e.printStackTrace();
      }

      // read from the called program's standard output stream
      /*
       mainProcess.getInputStream()- gives output of the process in bytes
       InputStreamReader() - convert raw bytes stream to character stream
       BufferedReader() - is a class that reads text from a character-input stream
       */
      /*
      The terminology might seem a bit counterintuitive, but it's rooted in the perspective of the Java program and its interaction with external processes.

      In Java, an InputStream is a stream through which data can be read. When you're dealing with an external process, the standard output of that process is, from the process's point of view, an output stream. However, from the Java program's perspective (which is reading from this stream), it's an input stream.
       */
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