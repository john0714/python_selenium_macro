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
		
		# 포니문제
		ponny=driver.find_elements_by_id("riddleanswer")
			
		# 다음 스테이지로 이동 체크
		goNextArena=driver.find_elements_by_id("btcp")
		
		if ponny:
			ponny.send_keys("A")
			ponny.submit()
		elif goNextArena:
			goNextArena[0].click()
		else:
			# 상태 변수 생성
			pane=driver.find_elements_by_id("pane_effects")[0]
			
			healthpot=pane.find_elements_by_xpath("//img[contains(@src,'/y/e/healthpot.png')]")
			manapot=pane.find_elements_by_xpath("//img[contains(@src,'/y/e/manapot.png')]")
			spiritpot=pane.find_elements_by_xpath("//img[contains(@src,'/y/e/spiritpot.png')]")
			regen=pane.find_elements_by_xpath("//img[contains(@src,'/y/e/regen.png')]")
			heartseeker=pane.find_elements_by_xpath("//img[contains(@src,'/y/e/heartseeker.png')]")
			shadowveil=pane.find_elements_by_xpath("//img[contains(@src,'/y/e/shadowveil.png')]")
			channeling=driver.find_elements_by_xpath("//img[contains(@src,'/y/e/channeling.png')]")
			
			spiritStatus=driver.find_elements_by_xpath("//img[contains(@src,'/y/battle/spirit_a.png')]")
			
			health=driver.find_elements_by_id("vrhd")
			if health:
				health=health[0]
			else:
				health=driver.find_elements_by_id("vrhb")[0]
			
			mana=driver.find_elements_by_id("vrm")[0]
			spirit=driver.find_elements_by_id("vrs")[0]
			
			# 타겟 몬스터 설정
			targetMonster=""
			for n in range(1, len(driver.find_elements_by_xpath("//div[@id='pane_monster']/div"))+1):
				monster=driver.find_elements_by_id("mkey_" + str(n))
				if monster:
					monster=monster[0]
					if float(monster.value_of_css_property("opacity")) <= 0.3:
						continue
					elif monster.value_of_css_property("border-color") == "rgb(92, 13, 18)":
						targetMonster=monster
						break
					elif monster.value_of_css_property("border-color") == "rgb(189, 116, 0)":
						targetMonster=monster
						break
					else:
						targetMonster=monster
			
			# 상태 변수 체크 및 행동
			# 생존력을 높이기 위해 생존관련 체크를 앞에 두고 continue를 넣음
			
			# For spiritShield
			if int(spirit.text) < 300:
				item=driver.find_elements_by_id("ckey_items")[0]
				item.click()
				spiritPoint=driver.find_elements_by_id("ikey_6")
				if spiritPoint:
					spiritPoint[0].click()
					continue
				else:
					item=driver.find_elements_by_id("ckey_items")[0]
					item.click()
			
			# For Health
			if int(health.text) < 12000:
				fullCure=driver.find_elements_by_id("qb5")
				if fullCure:
					fullCure[0].click()
					continue
				else:
					cure=driver.find_elements_by_id("qb1")
					if cure:
						cure[0].click()
						continue
					else:
						item=driver.find_elements_by_id("ckey_items")[0]
						item.click()
						healthPotion=driver.find_elements_by_id("ikey_4")
						if healthPotion:
							healthPotion[0].click()
							continue
						else:
							item=driver.find_elements_by_id("ckey_items")[0]
							item.click()
			
			# For Mana
			if int(mana.text) < 300:
				item=driver.find_elements_by_id("ckey_items")[0]
				item.click()
				manaPotion=driver.find_elements_by_id("ikey_5")
				if manaPotion:
					manaPotion[0].click()
					continue
				else:
					item=driver.find_elements_by_id("ckey_items")[0]
					item.click()

			if channeling:
				spell=driver.find_elements_by_id("qb3")[0]
				spell.click()
				continue
			
			if int(mana.text) < 700 and not manapot:
				item=driver.find_elements_by_id("ckey_items")[0]
				item.click()
				manaDraught=driver.find_elements_by_id("ikey_2")[0]
				manaDraught.click()
				continue

			if int(spirit.text) < 500 and not spiritpot:
				item=driver.find_elements_by_id("ckey_items")[0]
				item.click()
				spiritDraught=driver.find_elements_by_id("ikey_3")[0]
				spiritDraught.click()
				continue
		
			if not healthpot:
				item=driver.find_elements_by_id("ckey_items")[0]
				item.click()
				healthDraught=driver.find_elements_by_id("ikey_1")[0]
				healthDraught.click()
				continue
				
			if not regen:
				spell=driver.find_elements_by_id("qb2")[0]
				spell.click()
				continue
				
			if not heartseeker:
				spell=driver.find_elements_by_id("qb3")[0]
				spell.click()
				continue

			if not shadowveil:
				spell=driver.find_elements_by_id("qb4")[0]
				spell.click()
				continue
			
			# 스피릿 상태
			if not spiritStatus:
				energy=driver.find_elements_by_xpath("//div[@id='vcp']/div/div")
				if len(energy) >= 10:
					driver.find_elements_by_id("ckey_spirit")[0].click()
					continue
			
			# 공격
			targetMonster.click()
			
	except Exception:
		pass