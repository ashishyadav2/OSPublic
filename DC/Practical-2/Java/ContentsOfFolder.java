// Java Program to Display all directories in a directory

import java.io.*;

public class ContentsOfFolder {

	// Driver main method
	public static void main(String[] args) {
		File folder = new File(System.getProperty("user.dir"));

		File[] listOfFiles = folder.listFiles();

		for (File file : listOfFiles) {
			if (file.isFile()) {
				System.out.println(file.getName());
			}
		}
	}
}
