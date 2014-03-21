package org.openqa.selenium.example;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.htmlunit.HtmlUnitDriver;
import org.openqa.selenium.firefox.*;
import org.openqa.selenium.chrome.ChromeDriver;
import java.util.*;
//import org.openqa.selenium.RemoteWebDriver;
public class Example  {
    public static void main(String[] args) {
    	System.setProperty("webdriver.chrome.driver", "chromedriver");
    	
    	//test all the categories
    	WebDriver driver = new ChromeDriver();
    	for (int i = 1; i <= 3; i++) {
	    	driver.get("http://virtualfittingroom.heroku.com");
	        sleep();
	        WebElement element = driver.findElement(By.className((String)("service-count"+i)));
	        element.click();
	        sleep();
	        //test the products
	        for (int j=0; j<=1; j++) {
				WebElement element2 = driver.findElement(By.id((String)("item-img"+j)));
				element2.click();
				sleep();
				driver.navigate().back();
				sleep();
	        }
	        sleep();
			driver.navigate().back();
    	}
    	sleep();
    		
    	//test top menu bar
    	String[] topMenuBar = new String[]{"home","fitting_room","wishlist","login"};
    	for (int i=0; i<topMenuBar.length; i++) {
	        WebElement element = driver.findElement(By.id(topMenuBar[i]));
	        element.click();
	        sleep();
    	}
        
    	driver.close();
    }
    
    public static void sleep() {
    	try{
        	Thread.sleep(1000);
        }catch (InterruptedException e){
        	System.out.println("going into exception");
        }
    }
}