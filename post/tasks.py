from celery import shared_task
import time
from .models import temptable
import json
from django.core.mail import send_mail


@shared_task
def long_task():
    for i in range(20):
        print("Current value of i ==> ",i)
        time.sleep(2)
    print("Finally I am done with the execution.")
    return True


@shared_task
def store_user_data(browser):
    """referer = request["headers"].get("Referer", "N/A")
    useragent = request["META"].get('HTTP_USER_AGENT', "N/A")
    devicetype = "Mobile" if request.get("user_agent").get("is_mobile") else "Tablet" if request.get("user_agent").get("is_tablet") else "PC" if request.get("user_agent").get("is_pc") else "BOT" if request.get("user_agent").get("is_bot") else "N/A"
    #os = "{} {}".format(request.user_agent.os.family , request.user_agent.os.version_string)
    #touchsupport = str(request.user_agent.is_touch_capable)
    #browser = "{} {}".format(request.user_agent.browser.family, request.user_agent.browser.version_string)
    #devicefamily = request.user_agent.device.family
    #browser_data = dict(referer=referer, useragent=useragent,devicetype=devicetype, os=os,touchsupport=touchsupport,
    #  browser=browser, devicefamily=devicefamily)
    browser_data = dict(referer=referer, useragent=useragent,devicetype=devicetype)"""
    print(browser)
    browser_data = dict(browser=browser)
    browser_data = json.dumps(browser_data)
    data = temptable(browser_data=browser_data)
    data.save()
    return "Data Saved"


@shared_task
def async_send_mail(to, subject, text):
    try:
        a = send_mail(
                    subject,
                    text,
                    'noreply@skill-edge.com',
                    [to],
                    fail_silently=False,
                )
        print("mail sent to ",to)
        return "mail sent to {}".format(to)
    except Exception as e:
        print("Exception : ",e)
        return "Exception : {}".format(str(e))
