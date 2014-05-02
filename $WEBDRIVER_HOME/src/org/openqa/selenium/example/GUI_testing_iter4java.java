package org.openqa.selenium.example;
import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.chrome.ChromeDriver;

public class GUI_testing_iter4java {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
    driver = new FirefoxDriver();
//    driver = new ChromeDriver();
    baseUrl = "http://virtualfittingroom.herokuapp.com/";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testGUITestingIter4java() throws Exception {
    driver.get(baseUrl);
    sleep();
    driver.findElement(By.id("home")).click();
    sleep();
    driver.findElement(By.id("fitting_room")).click();
    sleep();
    driver.findElement(By.id("wishlist")).click();
    sleep();
    driver.findElement(By.id("profile")).click();
    sleep();
    driver.findElement(By.id("login")).click();
    sleep();
    driver.navigate().back();
    sleep();
    driver.findElement(By.id("home")).click();
    sleep();
    driver.findElement(By.id("img")).click();
    sleep();
    driver.findElement(By.cssSelector("img")).click();
    sleep();
    driver.findElement(By.id("home")).click();
    sleep();
    driver.findElement(By.cssSelector("li.service-count2 > a.service-link > div.inner > #img")).click();
    sleep();
    driver.findElement(By.cssSelector("img")).click();
    sleep();
    driver.findElement(By.id("home")).click();
    sleep();
    driver.findElement(By.cssSelector("li.service-count3 > a.service-link > div.inner > #img")).click();
    sleep();
    driver.findElement(By.cssSelector("img")).click();
    sleep();
    driver.findElement(By.id("home")).click();
    sleep();
    driver.findElement(By.id("img")).click();
    sleep();
    driver.findElement(By.cssSelector("img")).click();
    sleep();
    driver.findElement(By.id("add_to_wishlist")).click();
    sleep();
    driver.findElement(By.xpath("//div[6]/div/button")).click();
    sleep();
    driver.findElement(By.id("add_to_fitlist")).click();
    sleep();
    driver.findElement(By.xpath("//div[6]/div/button")).click();
    sleep();
    driver.findElement(By.id("profile")).click();
    sleep();
    driver.findElement(By.id("login")).click();
    sleep();
    driver.findElement(By.id("Email")).clear();
    sleep();
    driver.findElement(By.id("Email")).sendKeys("virtualfittingroom169@gmail.com");
    sleep();
    driver.findElement(By.id("Passwd")).clear();
    sleep();
    driver.findElement(By.id("Passwd")).sendKeys("169virtual");
    sleep();
    driver.findElement(By.id("signIn")).click();
    sleep();
    assertTrue(driver.findElement(By.cssSelector("BODY")).getText().matches("^[\\s\\S]*$"));
    sleep();
    assertTrue(driver.findElement(By.cssSelector("BODY")).getText().matches("^[\\s\\S]*$"));
    sleep();
    driver.findElement(By.id("ui-id-2")).click();
    sleep();
    assertTrue(driver.findElement(By.cssSelector("BODY")).getText().matches("^[\\s\\S]*$"));
    sleep();
    driver.findElement(By.id("ui-id-3")).click();
    sleep();
    assertTrue(driver.findElement(By.cssSelector("BODY")).getText().matches("^[\\s\\S]*$"));
    sleep();
    driver.findElement(By.id("home")).click();
    sleep();
    driver.findElement(By.id("img")).click();
    sleep();
    driver.findElement(By.cssSelector("img")).click();
    sleep();
    driver.findElement(By.id("add_to_wishlist")).click();
    sleep();
    driver.findElement(By.xpath("//div[6]/div/button")).click();
    sleep();
    driver.findElement(By.id("add_to_fitlist")).click();
    sleep();
    driver.findElement(By.xpath("//div[6]/div/button")).click();
    sleep();
    driver.findElement(By.id("home")).click();
    sleep();
    driver.findElement(By.cssSelector("li.service-count2 > a.service-link > div.inner > #img")).click();
    sleep();
    driver.findElement(By.cssSelector("img")).click();
    sleep();
    driver.findElement(By.id("add_to_wishlist")).click();
    sleep();
    driver.findElement(By.xpath("//div[6]/div/button")).click();
    sleep();
    driver.findElement(By.id("add_to_fitlist")).click();
    sleep();
    driver.findElement(By.xpath("//div[6]/div/button")).click();
    sleep();
    driver.findElement(By.id("profile")).click();
    sleep();
    assertTrue(driver.findElement(By.cssSelector("BODY")).getText().matches("^[\\s\\S]*$"));
    sleep();
    assertTrue(driver.findElement(By.cssSelector("BODY")).getText().matches("^[\\s\\S]*$"));
    sleep();
    driver.findElement(By.id("ui-id-2")).click();
    assertTrue(driver.findElement(By.cssSelector("BODY")).getText().matches("^[\\s\\S]*$"));
    sleep();
    assertTrue(driver.findElement(By.cssSelector("BODY")).getText().matches("^[\\s\\S]*$"));
    sleep();
    driver.findElement(By.id("ui-id-3")).click();
    assertTrue(driver.findElement(By.cssSelector("BODY")).getText().matches("^[\\s\\S]*$"));
    sleep();
    driver.findElement(By.id("ui-id-2")).click();
    sleep();
    driver.findElement(By.id("glasses_Rayban Glasses_1")).click();
    sleep();
    driver.findElement(By.id("hats_Adidas Cap_3")).click();
    sleep();
    driver.findElement(By.id("ui-id-1")).click();
    sleep();
    driver.findElement(By.id("Glasses_Rayban Glasses_1")).click();
    sleep();
    driver.findElement(By.id("Hats_Adidas Cap_3")).click();
    sleep();
    driver.findElement(By.id("logout")).click();
  }

  @After
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
  
  public static void sleep() {
  	try{
      	Thread.sleep(1000);
      }catch (InterruptedException e){
      	System.out.println("going into exception");
      }
  }
}
