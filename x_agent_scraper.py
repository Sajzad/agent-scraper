"""
X agent scraper
======================
Description:
        - collect agent informations and save those in a excel file.
Dependencies:
        - selenium
        - pandas
        - xlsxwriter
        - proxy_lists
"""
from selenium import webdriver
import pandas as pd
from time import sleep as s
import random
from proxy_lists import update_proxy, delete_proxy
# secure random module
random = random.SystemRandom()


def get_proxy(filename='proxy_list.txt'):
    # read proxy from text file
    proxy_list = []
    try:
        with open(filename, 'r') as f: 
            for line in f.readlines():
                proxy_list.append(line.strip('\n'))
    except Exception as e:
        print(e)
    return proxy_list


def get_user_agents(filename='user_agents.txt'):
    # collect user agents from the user_agents.txt
    user_agents = []
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                user_agents.append(line.strip('\n'))
    except Exception as e:
        print(e)
    return user_agents


def get_urls(filename='urls.txt'):
    # collect link of websites from urls.txt file and store them in urls
    urls = []
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                urls.append(line.strip('\n'))
    except Exception as e:
        print(e) 
    return urls


def collect_url(proxy_list=get_proxy(), user_agents=get_user_agents()):
    links = []
    link = ""
    total_proxy = len(proxy_list)
    page_no = 1
    # Pagination
    location_input = input("Write the Location Please\n Follow the exact name of location website suggests, \n e.g New York NY\n")
    splitting_texts = location_input.split(" ")
    if "Township" in splitting_texts not in splitting_texts[0]:
        splitting_texts.remove("Township")
    url_processing_1 = "-".join(map(str, splitting_texts))
    final_url_processing_1 = url_processing_1.lower() 
    region_id = input("please submit Region ID, \n Please go to the website and after submitting your location, Region ID will be available in the address bar\n")
    location_text = "%20".join(map(str, splitting_texts))
    n=0
    while n<30:
        for proxy in proxy_list:
            try:
                if total_proxy<=0:
                    update_proxy()
                    proxy_list = get_proxy()
                    total_proxy = len(proxy_list)
                    driver.quit()
                # initialize a new browser with new proxy and user agent for each url
                chrome_options = webdriver.ChromeOptions()
                prefs = {
                    'profile.managed_default_content_settings.images': 2,
                }
                chrome_options.add_experimental_option("prefs", prefs)
                chrome_options.add_argument('user-agent=' + random.choice(user_agents))
                # chrome_options.add_argument("--headless")
                chrome_options.add_argument('--proxy-server=%s' % proxy)
                driver = webdriver.Chrome(chrome_options=chrome_options)
                total_proxy = len(proxy_list)
                total_proxy-=1
                delete_proxy(proxy)
                print("proxy left:",total_proxy)
                if n==0:
                    try:
                        driver.get()
                    except Exception as e:
                        print(e)
                        continue                   
                else:
                    try:
                        driver.get()
                    except Exception as e:
                        print(e)
                        continue
                    try:
                        if driver.find_element_by_class_name("zsg-notification-text-confirmation").text == "Sorry! We couldn't find anyone.":
                            n=30
                            break
                            driver.quit()                            
                    except:
                        pass   
                    s(5)
                # Collecting links of every Agent
                try:
                    p_tags = driver.find_elements_by_class_name("ldb-contact-name")
                except Exception as e:
                    print(e)
                    driver.quit()
                    continue
                for p_tag in p_tags:
                    link = p_tag.find_element_by_tag_name("a").get_attribute("href")
                    links.append(link)
                print(link)
                # reassuring page not to be escaped from scraping.
                if link is not "":
                    n+=1
                    page_no+=1
                    link = "" 
                    print("page: ",page_no-1, "is successfully scraped")
                    driver.quit()
                else:
                    print("uffff...page:{}, Failed to scrape\n come on, try again....".format(page_no))
                    continue               
            except Exception as e:
                print(e)
                continue

    file_name = "urls.txt"
    urls_collected = 0
    with open(file_name, "w") as f:
        for link in links:
            urls_collected +=1
            f.write(link+"\n")
          
        f.close()
    print("total urls collected:",urls_collected)
    driver.quit()


def hit(target_urls=get_urls(), proxy_list=get_proxy(), user_agents=get_user_agents()):
    """
    :param str target_url: url for sending hit
    :param list of str proxy_list: consists of ip:port
    :param list of str user_agents : user agent header list
    :param int count: number of hit allocated for target_url
    :return: number of successful hits.
    :rtype: int
    """
    data = []
    agent_name = ""
    agent_type = ""
    item_sales = ""
    phone = ""
    about_company = ""
    company_address = ""
    brooker_address = ""
    cell_phone = ""
    website = ""
    facebook = ""
    twitter = ""
    linkedin = ""
    screen_name = ""
    member_since = ""
    real_estate_licenses = ""
    other_licenses = ""
    languages = ""
    blog = ""
    websites = ""
    experience = ""
    profile_elements = ""
    links = ""
    joining_elements_together = ""
    element_1 = ""
    element_2 = ""
    element_3 = ""
    element_4 = ""
    element_5 = ""
    total_reviews = ""
    data_dict = ""

    total_number_of_proxy = len(proxy_list)
    print("total proxy collected: ",total_number_of_proxy)
    # loop over all the proxies in the list
    for count_url, target_url in enumerate(target_urls[200:205], 1):      
        for count_proxy, proxy in enumerate(proxy_list, 1):
            try:
                if total_number_of_proxy<=0:
                    print("proxy is updating......")
                    update_proxy()
                    proxy_list = get_proxy()
                    total_number_of_proxy = len(proxy_list)
                # initialize a new browser with new proxy and user agent for each url
                chrome_options = webdriver.ChromeOptions()
                prefs = {
                    'profile.managed_default_content_settings.images': 2,
                }
                chrome_options.add_experimental_option("prefs", prefs)
                chrome_options.add_argument('user-agent=' + random.choice(user_agents))
                # chrome_options.add_argument("--headless")
                chrome_options.add_argument('--proxy-server=%s' % proxy)
                driver = webdriver.Chrome(chrome_options=chrome_options)
                delete_proxy(proxy)
                total_number_of_proxy -=1
                print("proxy left:", total_number_of_proxy)
                print("working on url no:",count_url)
                print("working on url:",target_url)
                try:
                    driver.get(target_url)
                    # driver.get("https://www.zillow.com/profile/TheExpansionTeam/")
                except Exception as e:
                    print(e)
                    print("Please write the correct url")
                    continue               
                s(3)
                try:
                    cells = driver.find_elements_by_class_name("profile-information-cell") or driver.find_elements_by_class_name("profile-information-nobile")
                    cell_phone = cells[1].text
                except:
                    print("nothing found as cell")
                    pass
                try:
                    agent_name = driver.find_element_by_class_name("ctcd-user-name").text
                except Exception as e:
                    print(e)
                    driver.quit()
                    continue
                try:
                    agent_type = driver.find_element_by_class_name("ctcd-agent-type").text
                except Exception as e:
                    print(e)
                    pass
                try:
                    total_reviews = driver.find_element_by_class_name("ctcd-item_reviews").find_element_by_class_name("ctcd-review-number").text
                except Exception as e:
                    print(e)
                    pass
                # print(agent_type)
                try:
                    item_sales = driver.find_element_by_class_name("ctcd-item_sales").text
                except Exception as e:
                    print(e)
                    pass
                try:
                    experience = driver.find_element_by_id("profile-title").find_element_by_class_name("zsg-h3").text
                except Exception as e:
                    print(e)
                    pass
                # elements of dl
                try:
                   element_1 = driver.find_element_by_class_name("profile-specialties").text 
                except Exception as e:
                    print(e)
                    pass
                try:
                    element_2 = profile_elements[1].text.replace( ",", " ")
                except Exception as e:
                    print(e)
                    pass
                try:
                    element_3 = profile_elements[2].text.replace(",", " ")
                except Exception as e:
                    print(e)
                    pass    
                try:
                    element_4 = profile_elements[3].text.replace(",", " ")
                except Exception as e:
                    print(e)
                    pass
                try:
                    element_5 = driver.find_element_by_class_name("content-fold-content").text
                except Exception as e:
                    print(e)
                    pass
                joining_elements_together = experience +"\n"+ element_1+"\n"+ element_2+ "\n" + element_3 + "\n" + element_4 + "\n" + element_5
                about_company = "".join(map(str, joining_elements_together))
                # professional Information 
                try:                         
                    company_address = driver.find_elements_by_class_name("profile-information-websites")
                except Exception as e:
                    print(e)
                    pass
                try:
                    websites = company_address[1]
                except Exception as e:
                    print(e)
                    pass
                try:
                    links = websites.find_elements_by_tag_name("a")
                    for link in links:
                        try:
                            if link.text== "Website":
                                website = link.get_attribute("href")
                        except:
                            pass
                        try:
                            if link.text == "Blog" or link.find_element_by_tag_name("span").text=="Blog":
                                blog = link.get_attribute("href")
                        except:
                            pass
                        try:
                            if link.text=="Facebook" or link.find_element_by_class_name("facebook").text == "Facebook":
                                facebook = link.get_attribute("href")         
                        except:
                            pass
                        try:
                            if link.text == "Twitter" or link.find_element_by_class_name("twitter").text == "Twitter":
                                twitter = link.get_attribute("href")        
                        except:
                            pass
                        try:
                            if link.text == "LinkedIn" or link.find_element_by_class_name("linkedIn").text == "LinkedIn":
                                linkedin = link.get_attribute("href")
                        except:
                            pass

                except Exception as e:
                    print(e)
                    pass
                try:
                    brooker_addresses = driver.find_elements_by_class_name("profile-information-address")
                except:
                    pass
                try:
                    brooker_address = brooker_addresses[1].text
                except:
                    pass
                try:
                    brooker_phone = driver.find_elements_by_class_name("profile-information-brokerage") 
                except:
                    pass
                try:
                    phone = brooker_phone[1].text
                except:
                    pass
                try:
                    element_of_languages = driver.find_elements_by_class_name("profile-information-languages")
                except:
                    pass
                try:
                    languages = element_of_languages[1].text
                except:
                    pass
                try:
                    element_of_member_since = driver.find_elements_by_class_name("profile-information-memeber-since")
                except:
                    pass
                try:
                    member_since = element_of_member_since[1].text
                except:
                    pass
                try:
                    elements_of_screen_name = driver.find_elements_by_class_name("profile-information-screen-name")
                except:
                    pass
                try:
                    screen_name = elements_of_screen_name[1].text
                except:
                    pass
                try:
                    licenses = driver.find_element_by_class_name("zsg-g_gutterless").find_elements_by_tag_name("li")
                except Exception as e:
                    print(e)
                    pass
                try:
                    real_estate_licenses = licenses[0].text
                except Exception as e:
                    print(e)
                    pass
                try:
                    other_licenses = licenses[1].text
                except Exception as e:
                    print(e)
                    pass

                data_dict = {

                    "Agent Name":agent_name,
                    "Agent Type":agent_type,
                    "Total Reviews": total_reviews,
                    "Item Sales":item_sales,
                    "About Company":about_company,
                    "Brooker Address":brooker_address,
                    "Cell Phone":cell_phone,
                    "Brooker Phone": phone,
                    "Website": website,
                    "Blog" : blog,
                    "Facebook":facebook,
                    "Twitter":twitter,
                    "Linkedin":linkedin,
                    "Screen Name":screen_name,
                    "Member Since":member_since,
                    "Real Estate Licenses": real_estate_licenses,
                    "Other Licenses":other_licenses,
                    "Languages":languages
                }
                data.append(data_dict)
                s(1)
                # print(data_dict)
                for dict_name, dict_data in data_dict.items():
                    print(dict_name,":", dict_data)
                if data_dict is not "":
                    print("Done url:", count_url)
                    data_dict = ""
                    driver.quit()
                    break                             
                else:
                    continue
              
            except Exception as e:
                print(e)
                print("Request aborted, Trying to hit again......")
                driver.quit() 
                continue
         
    output_file = "result.xlsx"
    if data:
        df = pd.DataFrame(columns = [
                    "Agent Name", 
                    "Agent Type",
                    "Total Reviews", 
                    "Item Sales",
                    "About Company",
                    "Brooker Address",
                    "Cell Phone",
                    "Brooker Phone", 
                    "Website", 
                    "Blog",
                    "Facebook",
                    "Twitter", 
                    "Linkedin",
                    "Screen Name",
                    "Member Since",
                    "Real Estate Licenses",
                    "Other Licenses",
                    "Languages"
                    ])
        df = df.append(data, ignore_index = True)
        df.to_excel(output_file, index = False)
        driver.quit()



# update_proxy()
s(1)
# collect_url()
hit()
          






















