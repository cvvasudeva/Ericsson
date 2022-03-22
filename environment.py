# authors: Stephen Brooks, Evan Bechtol
import json
from selenium import webdriver
from ConfigParser import SafeConfigParser
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options as ChromeOptions

# loading configuration options from script.conf
config = SafeConfigParser()
config.read('.\CP\\script.conf')
rootdir = config.get('Settings', 'rootpath')
wdriver = config.get('Settings', 'webdriver')
webdriverpath = config.get('Settings', 'webdriverpath')


def before_scenario(context, scenario):
    if wdriver == 'IE':
        context.browser = webdriver.Ie(webdriverpath + '\\IEDriverServer.exe')

    elif wdriver == 'Chrome' or wdriver == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--disable-extentions')
        chrome_options.add_argument('--enable-automation')
        chrome_options.add_argument('test-type')
        chrome_options.add_argument('--js-flags=--expose-gc')
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_argument('--disable-default-apps')
        chrome_options.add_argument('test-type=browser')
        chrome_options.add_argument('disable-infobars')
        context.browser = webdriver.Chrome(
            chrome_options=chrome_options, executable_path=(
                webdriverpath + '\\chromedriver.exe'))

    elif wdriver == 'Firefox' or wdriver == 'firefox':
        profile = webdriver.FirefoxProfile()
        proxy = "www-proxy.exu.ericsson.se"
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", proxy)
        profile.set_preference("network.proxy.http_port", 8080)
        profile.set_preference("network.proxy.ftp", proxy)
        profile.set_preference("network.proxy.ftp_port", 8080)
        profile.set_preference("network.proxy.share_proxy_settings", True)
        profile.set_preference("network.proxy.socks", proxy)
        profile.set_preference("network.proxy.socks_port", 8080)
        profile.set_preference("network.proxy.ssl", proxy)
        profile.set_preference("network.proxy.ssl_port", 8080)
        profile.update_preferences()

        context.browser = webdriver.Firefox(firefox_profile=profile)

    context.browser.set_window_size(1024, 768)
    # context.browser.implicitly_wait(2)


def after_step(context, step):
    with open(rootdir + '\\CP_step_durations.txt', 'a+') as f:
        f.write(str(step.duration) + ',')
        

def after_scenario(context, scenario):
    context.browser.quit()


def after_all(context):
    f = open(rootdir + "\\..\\tempDurations.txt", "a")
    s = open(rootdir + "\\..\\logs\\steps\\" +
             "CP-step_timings.log", "a")
    with open("json.output") as data_file:
        json_results = json.load(data_file)

    elapsedTime = 0
    for i in json_results[0]["elements"][0]["steps"]:
        elapsedTime += i["result"]["duration"]
        s.write('{:6.3f}'.format(i["result"]["duration"]) + '  ')
    if not elapsedTime == 0:
        elapsedTime = float('%.3f' % elapsedTime)
        f.write(str(elapsedTime) + " ")
    s.write("\n")
    s.close()
    f.close()
