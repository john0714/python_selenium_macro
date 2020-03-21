import time
from selenium import webdriver

# Chrome WebDriver를 이용해 Chrome을 실행합니다.
driver = webdriver.Chrome('C:/Users/Domangja/AppData/Local/Programs/Python/chromedriver.exe')

# 그 사이트로 이동합니다.
driver.get("https://hentaiverse.org/")
time.sleep(2)

# Login
IDElement = driver.find_element_by_name("UserName")
IDElement.send_keys("john0714")
PWElement = driver.find_element_by_name("PassWord")
PWElement.send_keys("a108106a")
IDElement.submit()
time.sleep(5)

while 1:
	try:
		# Loading
		# time.sleep(1)
		
		# Check Status
		pane=driver.find_elements_by_id("pane_effects")[0]
		
		healthpot=pane.find_elements_by_xpath("//img[contains(@src,'/y/e/healthpot.png')]")
		regen=pane.find_elements_by_xpath("//img[contains(@src,'/y/e/regen.png')]")
		heartseeker=pane.find_elements_by_xpath("//img[contains(@src,'/y/e/heartseeker.png')]")
		shadowveil=pane.find_elements_by_xpath("//img[contains(@src,'/y/e/shadowveil.png')]")
		channeling=driver.find_elements_by_xpath("//img[contains(@src,'/y/e/channeling.png')]")
		
		spiritStatus=driver.find_elements_by_xpath("//img[contains(@src,'/y/battle/spirit_a.png')]")
		
		health=driver.find_elements_by_id("vrhd")[0]
		mana=driver.find_elements_by_id("vrm")[0]
		spirit=driver.find_elements_by_id("vrs")[0]
		
		goNextArena=driver.find_elements_by_id("btcp")
		
		ponny=driver.find_elements_by_id("riddleanswer")
		
		if ponny:
			ponny.send_keys(str(random.randrange(1,3)))
			ponny.submit()
			continue
		
		if goNextArena:
			goNextArena[0].click()
		else:
			if channeling:
				spell=driver.find_elements_by_id("qb3")[0]
				spell.click()
				time.sleep(0.5)
		
			if not healthpot:
				item=driver.find_elements_by_id("ckey_items")[0]
				item.click()
				healthDraught=driver.find_elements_by_id("ikey_1")[0]
				healthDraught.click()
				time.sleep(0.5)
				
			if not regen:
				spell=driver.find_elements_by_id("qb2")[0]
				spell.click()
				time.sleep(0.5)
				
			if not heartseeker:
				spell=driver.find_elements_by_id("qb3")[0]
				spell.click()
				time.sleep(0.5)

			if not shadowveil:
				spell=driver.find_elements_by_id("qb4")[0]
				spell.click()
				time.sleep(0.5)
				
			if not spiritStatus:
				energy=driver.find_elements_by_xpath("//div[@id='vcp']/div/div")
				if len(energy) >= 10:
					driver.find_elements_by_id("ckey_spirit")[0].click()
					time.sleep(0.5)
					
			if int(health.text) < 10000:
				fullCure=driver.find_elements_by_id("qb5")
				if fullCure:
					fullCure[0].click()
					time.sleep(0.5)
				else:
					cure=driver.find_elements_by_id("qb1")
					if cure:
						cure[0].click()
						time.sleep(0.5)
					else:
						item=driver.find_elements_by_id("ckey_items")[0]
						item.click()
						healthPotion=driver.find_elements_by_id("ikey_4")[0]
						healthPotion.click()
						time.sleep(0.5)
						
			if int(mana.text) < 700:
				item=driver.find_elements_by_id("ckey_items")[0]
				item.click()
				manaDraught=driver.find_elements_by_id("ikey_2")
				if manaDraught:
					manaDraught[0].click()
					time.sleep(0.5)
				else:
					item=driver.find_elements_by_id("ckey_items")[0]
					item.click()
						
			if int(mana.text) < 300:
				item=driver.find_elements_by_id("ckey_items")[0]
				item.click()
				manaPotion=driver.find_elements_by_id("ikey_5")[0]
				manaPotion.click()
				time.sleep(0.5)
				
			if int(spirit.text) < 500:
				item=driver.find_elements_by_id("ckey_items")[0]
				item.click()
				spiritDraught=driver.find_elements_by_id("ikey_3")
				if spiritDraught:
					spiritDraught[0].click()
					time.sleep(0.5)
				else:
					item=driver.find_elements_by_id("ckey_items")[0]
					item.click()
				
			for n in range(1, 10):
				monster=driver.find_elements_by_id("mkey_" + str(n))[0]
				if monster and float(monster.value_of_css_property("opacity")) > 0.3:
					monster.click()
					break
	except:
		pass