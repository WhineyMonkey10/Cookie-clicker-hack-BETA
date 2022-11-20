// Security code so people dont accidentaly delete their game
// This is a very simple security code, but it works
// This code is not meant to be a security code, but a way to prevent people from accidentaly deleting their game

import java.io.File;
import java.io.IOException;
import java.io.FileWriter;
//Main class
class SecurityCode {
    //Main method
    // Method to get the security code

    public static String getSecurityCode() {
        //Gets the current time
        long time = System.currentTimeMillis();
        //Converts the time to a string
        String timeString = String.valueOf(time);
        //Gets the last 4 digits of the time
        String securityCode = timeString.substring(timeString.length() - 4);
        //Returns the security code
        return securityCode;
    }
}
public class Main{
public static void main(String[] args) {
    //Prints out the security code
    String securityCode = SecurityCode.getSecurityCode();
    System.out.println("Security code: " + securityCode);

    // Save the security code to a file
    // Checks if the file exists
    File file = new File("securityCode.txt");
    if (file.exists()) {
        // If the file exists, delete it
        file.delete();
    }
    // Creates a new file
    // Writes the security code to the file
    try {
        // Creates a new file writer
        FileWriter fileWriter = new FileWriter(file);
        // Writes the security code to the file
        fileWriter.write(securityCode);
        // Closes the file writer
        fileWriter.close();
    } catch (IOException e) {
        // Prints out the error
        e.printStackTrace();
    }

}}