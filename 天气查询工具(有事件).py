import tkinter as tk
from tkinter import messagebox
import time
import requests
from bs4 import BeautifulSoup
import json
import hashlib
# import pandas as pd

# text = '1dsdsds'
# text.hashlib.sha256(text.encode('utf-8')).hexdigest()
now = time.asctime(time.localtime(time.time()))
class User:
    def __init__(self):
        self.total = {}
    def a_d_d(self,account,code):
        if account is None or len(account) == 0:
            if code is None or len(code) == 0:
                self.total[account] = code
user = User()
user.total['user321'] = 'code654'
user.total['user322'] = 'code654'
print(user.total)

def click(event):
    if event.widget.get() == event.widget.default_text:
        event.widget.delete(0, 'end')
        event.widget.config(fg='black')

def f_i_r_s_t():
    def human_verify():
        answer = str(asw.get())
        if answer == 'qwerty':
            if messagebox.askyesno('确认界面', '确认？'):
                messagebox.showinfo('Congratulations!!!', '你通过了人坤验证！')
                main.destroy()
                def exit():
                    if messagebox.askyesno('确认界面','确认退出？'):
                        main.destroy()
                        main.quit()
                def login():
                    input1 = str(log.get())
                    input2 = str(log1.get())
                    if messagebox.askyesno('确认界面','确认？'):
                        if user.total[input1] == input2:
                            messagebox.showinfo('结果', '登录成功！')
                            root.destroy()

                            def check_the_weather():
                                y = int(year.get())
                                m = int(month.get())
                                url = 'https://tianqi.2345.com/Pc/GetHistory'
                                headers = {
                                    # ':authority': 'tianqi.2345.com',
                                    # ':method':'GET',
                                    # ':path' : """/Pc/GetHistory?areaInfo%5BareaId%5D=54511&areaInfo%5BareaType%5D=2&date%5Byear%5D=2011&date%5Bmonth%5D=3""",
                                    # ':scheme':"https",
                                    'accept': "application/json, text/javascript, */*; q=0.01",
                                    'accept-encoding': "gzip, deflate, br, zstd",
                                    'accept-language': "zh-CN,zh;q=0.9",
                                    'cache-control': "no-cache",
                                    'cookie': "lc2=59278; lc=59278; wc=71161; wc_n=%25u9AD8%25u8981%25u533A; Hm_lvt_a3f2879f6b3620a363bec646b7a8bcdd=1743324325; HMACCOUNT=B0B99500DF2DE7EC; BAIDU_SSP_lcr=https://www.baidu.com/link?url=xPJrUpZubKf0HstmfbVcA1RbP5kTAkwZ3dmqbg7wCOCf-GXgk3gGzWoM6IaQ0by6&wd=&eqid=c77932570086e7430000000667e90789; lastCountyId=54511; lastCountyPinyin=beijing; lastProvinceId=12; lastCityId=54511; lastCountyTime=1743328558; Hm_lpvt_a3f2879f6b3620a363bec646b7a8bcdd=1743328558",
                                    'pragma': "no-cache",
                                    'priority': "u=1, i",
                                    'referer': "https://tianqi.2345.com/wea_history/54511.htm",
                                    'sec-ch-ua': """"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134""""",
                                    'sec-ch-ua-mobile': '?0',
                                    'sec-ch-ua-platform': '"Windows"',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                                    'x-requested-with': 'XMLHttpRequest'
                                }
                                params = {'areaInfo[areaId]': 54511,
                                          'areaInfo[areaType]': 2,
                                          'date[year]': y,
                                          'date[month]': m}
                                r = requests.get(url, headers=headers, params=params)
                                check_the_stage = r.status_code
                                if check_the_stage == 200:
                                    with open('ttt_hhh.json', 'w', encoding='utf-8') as f:
                                        json.dump(r.json(), f, ensure_ascii=False)
                                    with open('ttt_hhh.json', 'r', encoding='utf-8') as f:
                                        json_data = json.load(f)
                                        later = str(json_data)
                                        soup = BeautifulSoup(later, 'html.parser')
                                        f1 = soup.find('ul', class_='history-msg').get_text()
                                        if messagebox.askyesno('确认界面','确认？'):
                                            messagebox.showinfo('访问成功！', '当前天气为{}'.format(f1))
                                else:
                                    messagebox.showwarning('系统错误！', '如需可向后台寻求帮助')

                            root1 = tk.Tk()
                            root1.geometry('300x300')
                            root1.title('天气查询')

                            year = tk.Entry(root1)
                            year.default_text = '在此输入年份...'
                            year.insert(0, year.default_text)
                            year.bind('<FocusIn>', click)
                            year.pack()

                            month = tk.Entry(root1)
                            month.default_text = '在此输入月份...'
                            month.insert(0, month.default_text)
                            month.bind('<FocusIn>', click)
                            month.pack()

                            button1 = tk.Button(root1, text='下一步', command=check_the_weather)
                            button1.pack()
                            root1.mainloop()



                        else:
                            messagebox.showwarning('结果', '登录失败！')

                root = tk.Tk()
                root.geometry('300x300')
                root.title('登陆界面')
                # text = tk.Text(root)
                # str11 = '欢迎使用该程序，现在时间是.....{}'.format(now)
                # text.insert(tk.END, str11)
                # text.pack()

                log = tk.Entry(root)
                log.default_text = '在此输入账号....'
                log.insert(0, log.default_text)
                log.bind('<FocusIn>', click)
                log.pack()

                log1 = tk.Entry(root)
                log1.default_text = '在此输入密码....'
                log1.insert(0, log1.default_text)
                log1.bind('<FocusIn>', click)
                log1.pack()

                button = tk.Button(root, text='下一步', command=login)
                button.pack()

                button3 = tk.Button(root,text='退出',command=exit)
                button3.pack()
                root.mainloop()
        else:
            messagebox.showwarning('ERROR', '你是仁坤吗？')

    main = tk.Tk()
    main.geometry('300x300')
    main.title('人坤验证')
    tk.Label(main,text='请输入"qwerty"').pack()
    asw = tk.Entry(main)
    asw.default_text='在此输入答案'
    asw.insert(0, asw.default_text)
    asw.bind('<FocusIn>', click)
    asw.pack()

    button2 = tk.Button(main, text='下一步', command=human_verify)
    button2.pack()
    main.mainloop()
f_i_r_s_t()
