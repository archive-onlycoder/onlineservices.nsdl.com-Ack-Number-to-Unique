import requests
import time
import random
from bs4 import BeautifulSoup


def get_cookie():
    cookies = {
        'GOTWL_MODE': '2',
        'STATEID': 'UWl3SEl6RXB6NVdjd3VZaUF6QXRSQT09',
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,he;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Referer': 'https://sarathi.parivahan.gov.in/sarathiservice/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(
        'https://sarathi.parivahan.gov.in/sarathiservice/sarathiHomePublic.do',
        cookies=cookies,
        headers=headers,
    )
    return response.cookies.get_dict()


def get_captcha(token):
    cookies = {
        'JSESSIONID': token,
        'GOTWL_MODE': '2',
    }

    headers = {
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,he;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Pragma': 'no-cache',
        'Referer': 'https://sarathi.parivahan.gov.in/sarathiservice/envaction.do',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }
    ts = time.time()
    response = requests.get(
        'https://sarathi.parivahan.gov.in/sarathiservice/jsp/common/captchaimage.jsp?'+str(ts),
        cookies=cookies,
        headers=headers,
        stream=True
    )
    
    fl='capchas/'+str(ts)+'_'+str(random.randint(0,1000))+'.jpg'
    with open(fl, 'wb') as handle:
        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
    return fl


def getLastEndorsedRtoDLserReq(token,dlno,dob,captchaByApplicant):
    cookies = {
        'JSESSIONID': token,
        'GOTWL_MODE': '2',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,he;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://sarathi.parivahan.gov.in',
        'Pragma': 'no-cache',
        'Referer': 'https://sarathi.parivahan.gov.in/sarathiservice/envaction.do',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    params = {
        'dlno': dlno,
        'dob': dob,
        'captchaByApplicant': captchaByApplicant,
    }

    response = requests.post(
        'https://sarathi.parivahan.gov.in/sarathiservice/getLastEndorsedRtoDLserReq.do',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response.text

def get_sarathi_csrf_token(token):
    cookies = {
        'GOTWL_MODE': '2',
        'STATEID': token,
    }
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,he;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Pragma': 'no-cache',
        'Referer': 'https://sarathi.parivahan.gov.in/sarathiservice/dlServicesDet.do',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }
    response = requests.get('https://sarathi.parivahan.gov.in/sarathiservice/envaction.do', cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")
    try:
        return soup.select('#envaction')[0].select('[name~=token]')[0]['value']
    except: 
        return False

def get_submitter_result(id=False,dlno=False,dob=False,capcha=False,csrf_token=False,info1_d=False):
    if(id and dlno and dob and capcha and csrf_token and info1_d):
        try:
            location=info1_d[2].split('@')[0]
            name=info1_d[2].split('@')[1]
        except:
            location=''
            name=''
        try:
            district=info1_d[3]
        except:
            district=''
        cookies = { 'JSESSIONID': id, 'GOTWL_MODE': '2'}
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,he;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'DNT': '1',
            'Origin': 'https://sarathi.parivahan.gov.in',
            'Pragma': 'no-cache',
            'Referer': 'https://sarathi.parivahan.gov.in/sarathiservice/envaction.do',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }
        data = [
            ('capToDisp', ''),
            ('captchaByApplicant', ''),
            ('dlno', dlno),
            ('dob', dob),
            ('entCaptha', capcha),
            ('dispDLDet', 'Select'),
            ('applcatgDLserReq', 'General'),
            ('PincodeDLserReq', ''),
            ('stateCodeDLTr', location),
            ('rtoCodeDLTr', '-1'),
            ('struts.token.name', 'token'),
            ('token', csrf_token),
            ('reset', 'formsubmit'),
            ('s4msg', ''),
            ('entCaptha', ''),
            ('rtoNameSelPreAppl', ''),
            ('dlno1', ''),
            ('applnotransreq', ''),
            ('dob1', ''),
            ('stEndName', location),
            ('rtoEndName', district),
            ('ApplFullNameDLSReq', name),
            ('isMatch', ''),
            ('firstCap', 'true'),
            ('CapPho', ''),
            ('idpchecked', ''),
            ('SelDiplomat', ''),
        ]
        response = requests.post(
            'https://sarathi.parivahan.gov.in/sarathiservice/envaction.do',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        soup = BeautifulSoup(response.text,"html.parser")
        try:
            soup.select('#dlSerReqPersDet fieldset')
        except:
            return {'status':False,'info':'Retry Please .Failed To Grab Data.'}
        
        data={
            "name":"",
            "fathers_name":"",
            "date_of_birth":"",
            "present_addr_data1":"",
            "present_addr_data2":"",
            "present_addr_data3":"",
            "present_addr_data4":"",
            "state":"",
            "image":"",
            "singnature":"",
            "rto":"",
            "class_of_vehicles":"",
            'validity_period':""
        }
        try:
            data['name']=soup.select('#dlSerReqPersDet fieldset tr')[0].select('td')[1].text
        except:
            pass
        try:
            data['fathers_name']=soup.select('#dlSerReqPersDet fieldset tr')[1].select('td')[1].text
        except:
            pass
        try:
            data['date_of_birth']=soup.select('#dlSerReqPersDet fieldset tr')[2].select('td')[1].text
        except:
            pass
        try:
            data['present_addr_data1']=soup.select('#dlSerReqPersDet fieldset tr')[3].select('td')[1].text
        except:
            pass
        try:
            data['present_addr_data2']=soup.select('#dlSerReqPersDet fieldset tr')[4].select('td')[1].text
        except:
            pass
        try:
            data['present_addr_data3']=soup.select('#dlSerReqPersDet fieldset tr')[5].select('td')[1].text
        except:
            pass
        try:
            data['present_addr_data4']=soup.select('#dlSerReqPersDet fieldset tr')[6].select('td')[1].text
        except:
            pass
        try:
            data['image']=soup.select('#dlSerReqPersDet fieldset #imgHid')[0]['value']
        except:
            pass
        try:
            data['singnature']=soup.select('#dlSerReqPersDet fieldset #sigHid')[0]['value']
        except:
            pass
        try:
            data['state']=soup.select('#dlSerReqPersDet fieldset fieldset div.col-md-4.text-center')[0].text.replace('State','').replace('-','').replace('\n','').replace('\t','').replace('\r','')
        except:
            pass
        try:
            data['rto']=soup.select('#dlSerReqPersDet fieldset fieldset div.col-md-4.text-center')[1].text.replace('RTO','').replace('-','').replace('\n','').replace('\t','').replace('\r','')
        except:
            pass

        try:
            data['validity_period']=soup.select('#dlSerReqPersDet fieldset fieldset .col-md-6.text-center')[0].text.replace('\n','').replace('\t','').replace('\r','')
        except:
            pass

        data
        v={}
        c=0
        for i in soup.select('#dlSerReqPersDet fieldset fieldset table tr'):
            if(c==0):
                c+=1
                continue

            try:
                name=i.select('td')[0].text.replace('\n','').replace('\t','').replace('\r','')
                location=i.select('td')[1].text.replace('\n','').replace('\t','').replace('\r','')
                v[name]=location
            except:
                pass
        data['class_of_vehicles']=v

        return {'status':True,'info':data}
        


    else:
        return {'status':False,'info':'Parameters Missing'}