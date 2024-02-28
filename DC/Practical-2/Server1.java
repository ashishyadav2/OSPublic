import java.io.*;
import java.net.*;
import java.lang.*;


class Server1 {
	@SuppressWarnings("deprecation")
	public static void main(String argv[]) throws Exception {

		System.out.println("Server started...");
		// Reading from
		String s = null;
		// server's port number where the client should send request
		ServerSocket welcomeSocket = new ServerSocket(6956);
		while (true) {
			Socket connectionSocket = welcomeSocket.accept();

			// Read from Client
			BufferedReader inFromClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
			String clientRequest = inFromClient.readLine();
			// System.out.println("Demand Received from Client: " + y);
			System.out.print("Demand Received from Client: ");

			int demand = Integer.parseInt(clientRequest);
			System.out.println("Demand No is : " + demand);
			// Initialization
			Process p1 = null;
			Process p2 = null;

			// if (demand==-1) {
			// 	welcomeSocket.close();
			// }
			switch (demand) {
				case 1:
					p1 = Runtime.getRuntime().exec("javac ContentsOfFolder.java");
					p2 = Runtime.getRuntime().exec("java ContentsOfFolder");
					break;

				case 2:
					p1 = Runtime.getRuntime().exec("javac DisplayFileSize.java");
					p2 = Runtime.getRuntime().exec("java DisplayFileSize");
					break;

				case 3:
					p1 = Runtime.getRuntime().exec("javac DisplayFreeSpace.java");
					p2 = Runtime.getRuntime().exec("java DisplayFreeSpace");
					break;

				case 4:
					p1 = Runtime.getRuntime().exec("javac DisplayVideoSize.java");
					p2 = Runtime.getRuntime().exec("java DisplayVideoSize");
					break;
					
				case 5:
					p1 = Runtime.getRuntime().exec("javac ReadTextFile.java");
					p2 = Runtime.getRuntime().exec("java ReadTextFile");
					break;

				default:
					System.out.println("Invalid Choice! Should be between 1 to 5");
					break;
			}
			
			String response = "Invalid Choice! Should be between 1 to 5";
			if (demand>=1 && demand <=5) {
				response = "";
				BufferedReader stdInput = new BufferedReader(new InputStreamReader(p2.getInputStream()));
				while (true) {
					String fileOutput = stdInput.readLine();
					if (fileOutput==null) {
						break;
					}
					response = response + fileOutput + "\n" ;
				}
				response += "<end>";
			}
			System.out.println("My response: " + response);
			DataOutputStream DataToClient = new DataOutputStream(connectionSocket.getOutputStream());
			// send response to the client
			DataToClient.writeBytes(response + '\n');
		}
		// welcomeSocket.close();
		// System.out.println("Closing server");
	}
}
