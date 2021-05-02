
#java


'''


public class AppDemo {
    private AppiumDriver driver;

    @BeforeClass
    public void setUp() throws Exception {
        //设置自动化相关参数
        DesiredCapabilities capabilities = new DesiredCapabilities();
        //使用哪种移动平台
        capabilities.setCapability("platformName", "Android");
        //启动哪种设备，是真机还是模拟器
        capabilities.setCapability("deviceName","48cd544f");
        //设置安卓系统版本
        capabilities.setCapability("platformVersion", "7.1.1");
        //不要再次安装apk
        capabilities.setCapability("noReset",true);
        //不用重新签名
        capabilities.setCapability("noSign",true);
		//设置包名
        capabilities.setCapability("appPackage","com.android.browser");
        //设置activity
        capabilities.setCapability("appActivity","com.android.browser.BrowserActivity");
        //初始化
        driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);
    }

    @Test
    public void openChrome() throws InterruptedException {
        driver.get("http://www.baidu.com");
        Thread.sleep(3000);
    }

    @AfterClass(enabled = false)
    public void tearDown() throws Exception {
        driver.quit();
    }
'''