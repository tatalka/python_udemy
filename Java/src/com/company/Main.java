package com.company;

import java.io.FileInputStream;
import java.util.Properties;

public class Main {

    public static void main(String[] args) {
        Properties prop = new Properties();
        String path = "C:\\git_repos\\olew\\Java\\src\\com\\company\\przykladowe.property";
        try {
            FileInputStream fs = new FileInputStream(path);
            prop.load((fs));
            System.out.println(prop.getProperty("name"));
            System.out.println(prop.getProperty("course"));
        }
        catch (Exception e) {
            System.out.println("there was an error opening the file");
            System.out.println(e.getMessage());
        }


    }
}
