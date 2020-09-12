import requests
import datetime as dt
import pytz
from datetime import datetime, timezone
from twilio.rest import Client


account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)
count=0
final_string=""
header1="""<span style="color: rgb(60, 72, 88); font-family: &quot;Trebuchet MS&quot;, Helvetica, sans-serif, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400;">"""
footer1="""</span><br style="color: rgb(60, 72, 88); font-family: &quot;Trebuchet MS&quot;, Helvetica, sans-serif, sans-serif;" />"""
footer2="""<a href="openkattis.com", target=blank">"""
footer3="""</a></span><br style="color: rgb(60, 72, 88); font-family: &quot;Trebuchet MS&quot;, Helvetica, sans-serif, sans-serif;" />"""
quote1=''
quote=quote1[0]

part1="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html data-editor-version="2" class="sg-campaigns" xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1" /><!--[if !mso]><!-->
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" /><!--<![endif]-->
    <!--[if (gte mso 9)|(IE)]>
    <xml>
    <o:OfficeDocumentSettings>
    <o:AllowPNG/>
    <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
    <!--[if (gte mso 9)|(IE)]>
    <style type="text/css">
      body {width: 600px;margin: 0 auto;}
      table {border-collapse: collapse;}
      table, td {mso-table-lspace: 0pt;mso-table-rspace: 0pt;}
      img {-ms-interpolation-mode: bicubic;}
    </style>
    <![endif]-->

    <style type="text/css">
      body, p, div {
        font-family: arial;
        font-size: 14px;
      }
      body {
        color: #000000;
      }
      body a {
        color: #1188E6;
        text-decoration: none;
      }
      p { margin: 0; padding: 0; }
      table.wrapper {
        width:100% !important;
        table-layout: fixed;
        -webkit-font-smoothing: antialiased;
        -webkit-text-size-adjust: 100%;
        -moz-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
      }
      img.max-width {
        max-width: 100% !important;
      }
      .column.of-2 {
        width: 50%;
      }
      .column.of-3 {
        width: 33.333%;
      }
      .column.of-4 {
        width: 25%;
      }
      @media screen and (max-width:480px) {
        .preheader .rightColumnContent,
        .footer .rightColumnContent {
            text-align: left !important;
        }
        .preheader .rightColumnContent div,
        .preheader .rightColumnContent span,
        .footer .rightColumnContent div,
        .footer .rightColumnContent span {
          text-align: left !important;
        }
        .preheader .rightColumnContent,
        .preheader .leftColumnContent {
          font-size: 80% !important;
          padding: 5px 0;
        }
        table.wrapper-mobile {
          width: 100% !important;
          table-layout: fixed;
        }
        img.max-width {
          height: auto !important;
          max-width: 480px !important;
        }
        a.bulletproof-button {
          display: block !important;
          width: auto !important;
          font-size: 80%;
          padding-left: 0 !important;
          padding-right: 0 !important;
        }
        .columns {
          width: 100% !important;
        }
        .column {
          display: block !important;
          width: 100% !important;
          padding-left: 0 !important;
          padding-right: 0 !important;
          margin-left: 0 !important;
          margin-right: 0 !important;
        }
      }
    </style>
    <!--user entered Head Start-->
    
     <!--End Head user entered-->
  </head>
  <body>
    <center class="wrapper" data-link-color="#1188E6" data-body-style="font-size: 14px; font-family: arial; color: #000000; background-color: #ffffff;">
      <div class="webkit">
        <table cellpadding="0" cellspacing="0" border="0" width="100%" class="wrapper" bgcolor="#ffffff">
          <tr>
            <td valign="top" bgcolor="#ffffff" width="100%">
              <table width="100%" role="content-container" class="outer" align="center" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td width="100%">
                    <table width="100%" cellpadding="0" cellspacing="0" border="0">
                      <tr>
                        <td>
                          <!--[if mso]>
                          <center>
                          <table><tr><td width="600">
                          <![endif]-->
                          <table width="100%" cellpadding="0" cellspacing="0" border="0" style="width: 100%; max-width:600px;" align="center">
                            <tr>
                              <td role="modules-container" style="padding: 0px 0px 0px 0px; color: #000000; text-align: left;" bgcolor="#ffffff" width="100%" align="left">
                                
    <table class="module preheader preheader-hide" role="module" data-type="preheader" border="0" cellpadding="0" cellspacing="0" width="100%"
           style="display: none !important; mso-hide: all; visibility: hidden; opacity: 0; color: transparent; height: 0; width: 0;">
      <tr>
        <td role="module-content">
          <p>List of coding contests happening today</p>
        </td>
      </tr>
    </table>
  
    <table class="wrapper" role="module" data-type="image" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;">
      <tr>
        <td style="font-size:6px;line-height:10px;padding:0px 0px 0px 0px;" valign="top" align="center">
          <a href="https://domain.com"><img class="max-width" border="0" style="display:block;color:#000000;text-decoration:none;font-family:Helvetica, arial, sans-serif;font-size:16px;max-width:100% !important;width:100%;height:auto !important;" src="https://marketing-image-production.s3.amazonaws.com/uploads/18e4548b148bc72896f03d3e32abc3913fe5040ed8370fef89a196d114adfe0d493a946369bb057d4499b2544ca42b6eb5b7157b27c7f098cdbbbd465e4e9520.jpg" alt="Main_Logo" width="600"></a>
        </td>
      </tr>
    </table>
  
    <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;">
      <tr>
        <td style="padding:18px 0px 18px 0px;line-height:22px;text-align:inherit;"
            height="100%"
            valign="top"
            bgcolor="">
            <h2 style="text-align: center;"><span style="font-family:trebuchet ms,helvetica,sans-serif;">All Contests For Today</span></h2>

<div>
<table border="0" cellpadding="0" cellspacing="0" style="color: rgb(34, 34, 34); font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif; font-size: small; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; background-color: rgb(255, 255, 255);" width="100%">
	<tbody>
		<tr style="border-collapse: collapse;">
			<td class="m_7313178048686361509rnb-force-col" style="font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif; border-collapse: collapse;" valign="top">
			<table align="left" border="0" cellpadding="0" cellspacing="0" class="m_7313178048686361509rnb-col-1" valign="top" width="100%">
				<tbody>
					<tr style="border-collapse: collapse;">
						<td class="m_7313178048686361509content-spacing" style="font-family: &quot;Palatino Linotype&quot;, &quot;Book Antiqua&quot;, Palatino, serif, sans-serif; border-collapse: collapse; font-size: 14px; color: rgb(60, 72, 88); line-height: 21px;">
						<div style="display: list-item; list-style-type: none;">Hey Coder!</div>

						<div style="display: list-item; list-style-type: none;">&nbsp;</div>

						<div style="display: list-item; list-style-type: none;">Here&#39;s a list of coding contests curated for you today. While I believe my script works fine, I would still recommend you to crosscheck the list and timing of contests to avoid discrepancy. Happy coding!</div>

						<div style="display: list-item; list-style-type: none;">&nbsp;</div>
						</td>
					</tr>
				</tbody>
			</table>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div>-----------------------------------------------------------------------------------------------------------------------------</div>

<div>
"""
part3="""</div>


  
    <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;">
      <tr>
        <td style="padding:18px 0px 18px 0px;line-height:22px;text-align:inherit;"
            height="100%"
            valign="top"
            bgcolor="">
            <div>
<div style="color: rgb(136, 136, 136); font-family: Arial, Helvetica, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; text-align: center; background-color: rgb(249, 250, 252);">You received this email because you are registered with Programming Contests Notifications</div>

<div style="color: rgb(136, 136, 136); font-family: Arial, Helvetica, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; text-align: center; background-color: rgb(249, 250, 252);">Coded by M31</div>
</div>

        </td>
      </tr>
    </table>
  <div data-role="module-unsubscribe" class="module unsubscribe-css__unsubscribe___2CDlR" role="module" data-type="unsubscribe" style="color:#444444;font-size:12px;line-height:20px;padding:16px 16px 16px 16px;text-align:center"><div class="Unsubscribe--addressLine"><p class="Unsubscribe--senderName" style="font-family:Arial, Helvetica, sans-serif;font-size:12px;line-height:20px">Jarvis, The Loyal Bot</p><p style="font-family:Arial, Helvetica, sans-serif;font-size:12px;line-height:20px"><span class="Unsubscribe--senderAddress">Stark Industries</span>, <span class="Unsubscribe--senderCity">Manhattan</span>, <span class="Unsubscribe--senderState">New York</span> <span class="Unsubscribe--senderZip">10015</span> </p></div><p style="font-family:Arial, Helvetica, sans-serif;font-size:12px;line-height:20px"><a class="Unsubscribe--unsubscribeLink" href="<%asm_group_unsubscribe_raw_url%>">Unsubscribe</a> - <a class="Unsubscribe--unsubscribePreferences" href="<%asm_preferences_raw_url%>">Unsubscribe Preferences</a></p></div>
                              </td>
                            </tr>
                          </table>
                          <!--[if mso]>
                          </td></tr></table>
                          </center>
                          <![endif]-->
                        </td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </div>
    </center>
  </body>
</html>"""
breaker="""<span style="color: rgb(60, 72, 88); font-family: &quot;Trebuchet MS&quot;, Helvetica, sans-serif, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400;">------------------------------</span><wbr style="color: rgb(60, 72, 88); font-family: &quot;Trebuchet MS&quot;, Helvetica, sans-serif, sans-serif;" /><span style="color: rgb(60, 72, 88); font-family: &quot;Trebuchet MS&quot;, Helvetica, sans-serif, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400;">------------------------------</span><wbr style="color: rgb(60, 72, 88); font-family: &quot;Trebuchet MS&quot;, Helvetica, sans-serif, sans-serif;" /><span style="color: rgb(60, 72, 88); font-family: &quot;Trebuchet MS&quot;, Helvetica, sans-serif, sans-serif; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400;">----</span><br style="color: rgb(60, 72, 88); font-family: &quot;Trebuchet MS&quot;, Helvetica, sans-serif, sans-serif;" />
"""

response=requests.get('https://clist.by:443/api/v1/contest/?limit=200&order_by=-start', headers={''})
json_response=response.json()
for i in range(200):
  event_name=json_response['objects'][i]['event']
  event_start_time=json_response['objects'][i]['start']
  event_organization=json_response['objects'][i]['resource']['name']
  event_duration=int(json_response['objects'][i]['duration'])
  year=int((event_start_time[0:4]))
  date=int((event_start_time[8:10]))
  month=int((event_start_time[5:7]))
  hour=int((event_start_time[11:13]))
  minute=int((event_start_time[14:16]))
  second=int((event_start_time[17:19]))
  #fmt = '%Y-%m-%d %H:%M:%S'
  in_minutes=event_duration/60
  in_hour=int(in_minutes/60)
  rem_min=int(in_minutes%60)

  event_date = datetime(year, month, date, hour, minute, second).replace(tzinfo=pytz.UTC)
  user_timezone = pytz.timezone('Asia/Kolkata')
  local_date = event_date.astimezone(user_timezone)
  #print (local_date.strftime('%m/%d/%Y %H:%M:%S %Z'))
  newdate=(local_date.strftime('%m/%d/%Y %H:%M:%S %Z'))
  #print(event_start_time)
  #print(newdate)
  #date_str = year+"-"+month+"-"+date+" "+hour+":"+minute+":"+second
  #amsterdam = pytz.timezone('Asia/Kolkata')
  #dt = datetime.datetime.strptime(date_str, fmt)
  #am_dt = amsterdam.localize(dt)
  #newdate=am_dt.astimezone(utc).strftime(fmt)
  title, handle, mandle = newdate.split()
  #print(title)
  #print(handle)
  #print(mandle)
  #print (am_dt.astimezone(utc).strftime(fmt))
  #print (am_dt.astimezone(utc).strftime(fmt))
  newyear=(title[6:10])
  newmonth=int((title[0:2]))
  newdate=int((title[3:5]))
  newhour=(handle[0:2])
  newminute=(handle[3:5])
  newsecond=(handle[6:8])
  #print(newyear)
  #print(newmonth)
  #print(newdate)
  #print(newhour)
  #print(newminute)
  #print(newsecond)
  utc_dt = datetime.now(timezone.utc) # UTC time
  dt = utc_dt.astimezone() # local time

  tz2 = pytz.timezone('Asia/Kolkata')
  berlin_now = datetime.now(tz2)
  curr=str(berlin_now)
  currdate, currtime=curr.split()
  curr_year=int(curr[0:4])
  curr_month=int(currdate[5:7])
  curr_day=int(currdate[8:10])
  curr_hour=int(currtime[0:2])
  curr_minute=int(currtime[3:5])
  curr_second=int(currtime[6:8])
  if newmonth==curr_month and newdate==curr_day:
    count=count+1
    
    contest_string=header1+"Contest #"+str(count)+footer1+" \n"+ header1+"Name: "+event_name+footer1+" \n"+ header1+"Organizer: "+"""<a href="""+quote+event_organization+quote+""", target=blank">"""+event_organization+footer3+" \n"+header1+"Start Time: "+newhour+":"+newminute+ footer1+" \n"+ header1+"Duration: "+ str(in_hour)+" Hours and "+str(rem_min)+" Minutes"+footer1+"\n"+breaker+"\n"
    final_string=final_string + contest_string

    

html_string=part1+final_string+part3    
file = open('html.html','w', encoding='utf8')
file.write(html_string)
file.close()

with open('html.html', 'r',encoding="utf8") as f:
    html_string = f.read()

email_list=[""]
cnt=0
for items in email_list:
  def send_simple_message():
          return requests.post(
                  "https://api.mailgun.net/v3/mail.domain.com/messages",
                  auth=("api", ""),
                  data={"from": "Jarvis The Bot",
                          "to": [email_list[cnt]],
                          "subject": str(count) + " Coding Contests Today",
                          "html" :html_string})


  send_simple_message()
  cnt=cnt+1
print("ALL DONE!")





