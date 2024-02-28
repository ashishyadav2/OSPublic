import java.io.*;
import java.net.*;

class Server2 {
  @SuppressWarnings("deprecation")
  public static void main(String argv[]) throws Exception {
    int args_len = argv.length;

    if (args_len > 2) {
      System.out.println("Invalid argument");
      System.exit(0);
    }

    String serverIPAddress = argv[0];
    int port = Integer.parseInt(argv[1]);
    while (true) {
      System.out.println("----------------Menu---------------");
      System.out.println("Enter Choice");
      System.out.println("1. To List Contents of Directory");
      System.out.println("2. To show file size");
      System.out.println("3. To show empty space in drive.");
      System.out.println("4. To show video file size.");
      System.out.println("5. Read txt file");
      System.out.println("-1. Exit");
      System.out.print("Choice: ");
      InputStreamReader inStream = new InputStreamReader(System.in);
      BufferedReader bufferReader = new BufferedReader(inStream);

      // get choice of the user
      String choice = bufferReader.readLine();
      System.out.println("");
      if (choice.equals("-1")) {
        System.out.println("Disconnected from the server");
        System.exit(0);
      }
      int choiceInt = Integer.parseInt(choice);
      if (choiceInt>5 || choiceInt<1 ){
        System.out.println("Invalid Choice! Should be between 1 to 5!");
        System.out.println("");
        continue;
      }
      try {
        Socket clientSocket = new Socket(serverIPAddress, port);
        DataOutputStream DataToServer = new DataOutputStream(clientSocket.getOutputStream());
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