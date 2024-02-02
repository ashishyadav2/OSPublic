import java.io.*;
import java.net.*;

/*
   ____ _ _            _   
  / ___| (_) ___ _ __ | |_ 
 | |   | | |/ _ \ '_ \| __|
 | |___| | |  __/ | | | |_ 
  \____|_|_|\___|_| |_|\__|
                           
 */
class Server2 {
  @SuppressWarnings("deprecation")
  public static void main(String argv[]) throws Exception {
    int args_len = argv.length;

    if (args_len > 2) {
      System.out.println("Invalid argument");
      System.exit(0);
    }

    String serverIPAddress = argv[0];
    // converting string to integer
    int port = Integer.parseInt(argv[1]);
    // Run indefinitely until interrupted
    while (true) {
      System.out.println("----------------Menu---------------");
      System.out.println("Enter Choice");
      System.out.println("1. To List Contents of Directory");
      System.out.println("2. To show file size");
      System.out.println("3. To show empty space in drive.");
      System.out.println("4. To show video file size.");
      System.out.println("5. Get server system info");
      System.out.println("-1. Exit");
      System.out.print("Choice: ");

      // System.in - take inputs from the terminal
      // InputStreamReader() - is a bridge from byte streams to character streams
      // BufferedReader() - is a class that reads text from a character-input stream
      InputStreamReader inStream = new InputStreamReader(System.in);
      BufferedReader bufferReader = new BufferedReader(inStream);

      // get choice of the user
      String choice = bufferReader.readLine();
      System.out.println("");
      if (choice.equals("-1")) {
        System.out.println("Disconnected from the server");
        System.exit(0);
      }
      // servers's ip address: (string) and port number (integer)
      // Socket clientSocket = new Socket("186.168.1.163", 9999);
      try {
        Socket clientSocket = new Socket(serverIPAddress, port);
        // clientSocket.getOutputStream() returns an output stream associated with the
        // socket, and DataOutputStream is used to handle higher-level data types (like
        // int, double, etc.).
        DataOutputStream DataToServer = new DataOutputStream(clientSocket.getOutputStream());
        // This line sends data to the server.
        DataToServer.writeBytes(choice + '\n');

        BufferedReader serverResponse = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        String serverMessage;
        System.out.println("Received from Server: ");
        while ((serverMessage = serverResponse.readLine()) != null) {
          if (serverMessage.equals("<end>")) {
            serverMessage.replaceAll("<end>","");
            break;
          }
          System.out.println(serverMessage);
        }
        System.out.println("");
      } catch (Exception e) {
        System.out.println("Disconnected from the server");
        break;
      }
    }
  }
}