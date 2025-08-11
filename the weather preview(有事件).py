import json
import bs4
import click
from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import messagebox
import hashlib
import time
now = time.asctime(time.localtime(time.time()))
h1 = {
'accept' : """text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7""",
'accept-encoding' : 'gzip, deflate, br, zstd',
'accept-language' : 'zh-CN,zh;q=0.9',
'cache-control' : "no-cache",
'cookie' : """lc2=59278; lc=59278; wc=71161; wc_n=%25u9AD8%25u8981%25u533A; BAIDU_SSP_lcr=https://www.baidu.com/link?url=7F2GCk_NUT7B5PcspgBRbdsRmnma5DFyYTVPBjlZM7RsRwrYp-HnaN3pNTI72aqlQdgLvIpGJgLGm_fpJU1-Zq&wd=&eqid=d1c665af01044f790000000667f528a3; Hm_lvt_a3f2879f6b3620a363bec646b7a8bcdd=1743420406,1744119992,1744128512,1744170384; Hm_lpvt_a3f2879f6b3620a363bec646b7a8bcdd=1744170384; HMACCOUNT=B0B99500DF2DE7EC; lastCountyId=59278; lastCountyTime=1744170384; lastCountyPinyin=zhaoqing; lastCityId=59278; lastProvinceId=15""",
'pragma' : "no-cache",
'priority' : 'u=0, i',
'referer' : "https://tianqi.2345.com/fourth-59278.htm",
'sec-ch-ua' : '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
'sec-ch-ua-mobile' : '?0',
'sec-ch-ua-platform' : '"Windows"',
'sec-fetch-dest' : 'document',
'sec-fetch-mode' : 'navigate',
'sec-fetch-site' : 'same-origin',
'sec-fetch-user' : '?1',
'upgrade-insecure-requests' :'1',
'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

url = 'https://tianqi.2345.com/fourth-59278.htm'
verify = {
'accept' : """text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7""",
'accept-encoding' : 'gzip, deflate, br, zstd',
'accept-language' : """zh-CN,zh;q=0.9""",
'cache-control' : "no-cache",
'cookie': """lc2=59278; lc=59278; wc=71161; wc_n=%25u9AD8%25u8981%25u533A; BAIDU_SSP_lcr=https://www.baidu.com/link?url=7F2GCk_NUT7B5PcspgBRbdsRmnma5DFyYTVPBjlZM7RsRwrYp-HnaN3pNTI72aqlQdgLvIpGJgLGm_fpJU1-Zq&wd=&eqid=d1c665af01044f790000000667f528a3; lastCountyId=59278; lastCountyTime=1744119992; lastCountyPinyin=zhaoqing; lastCityId=59278; lastProvinceId=15; Hm_lvt_a3f2879f6b3620a363bec646b7a8bcdd=1743324325,1743420406,1744119992; Hm_lpvt_a3f2879f6b3620a363bec646b7a8bcdd=1744119992; HMACCOUNT=B0B99500DF2DE7EC""",
'pragma' : "no-cache",
'priority' : 'u=0, i',
'referer' : """https://www.baidu.com/link?url=7F2GCk_NUT7B5PcspgBRbdsRmnma5DFyYTVPBjlZM7RsRwrYp-HnaN3pNTI72aqlQdgLvIpGJgLGm_fpJU1-Zq&wd=&eqid=d1c665af01044f790000000667f528a3""",
'sec-ch-ua' : '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
'sec-ch-ua-mobile' : '?0',
'sec-ch-ua-platform' : '"Windows"',
'sec-fetch-dest' : 'document',
'sec-fetch-mode' : 'navigate',
'sec-fetch-site' : 'cross-site',
'sec-fetch-user' : '?1',
'upgrade-insecure-requests' : '1',
'user-agent' :  """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"""
}
r = requests.get(url, headers= verify)
print(r.status_code)

begin_soup = bs4.BeautifulSoup(r.text, 'html.parser')
tips = {}
input1 = begin_soup.find('body')
input2 = input1.find('ul',class_='select-city-list')
input3 = input2.find_all('li')
the_last = {}
for x in input3:
    url = f'{x}'
    # print(x);print(x.get_text())
    soup1 = bs4.BeautifulSoup(url, 'html.parser')
    href_0 = soup1.find('a')
    url = href_0.get('href')
    # print(url)
    the_last[x.get_text()] = 'https://tianqi.2345.com{}'.format(url)
# print(the_last)
def click(event):
    if event.widget.get() == event.widget.default_text:
        event.widget.delete(0, 'end')
        event.widget.config(fg='black')

def s_e_c_o_n_d():

    def f_i_r_s_t():
        x = str(input1.get())
        messagebox.showinfo('使用界面', '输入地点可查询相关天气情况')
        # x = '北京天气'
        if x in the_last:
            output_url = the_last[x]
            # print(output_url)
            if messagebox.askyesno('确认界面','你确认吗?'):
                time.sleep(3)
                re = requests.get(output_url, headers=h1)
                soup2 = bs4.BeautifulSoup(re.text, 'html.parser')
                f1 = soup2.find('body')
                state = f1.find('p', class_='real-wea-info')
                today = f1.find('div', class_='real-today')
                yesterday = f1.find('span', class_='other-yes fl')
                state1 = state.get_text()
                today1 = today.get_text()
                yesterday1 = yesterday.get_text()

                messagebox.showinfo('', '查询中....')
                result = f'你查询的位置为{x},当前天气为{today1},昨天天气为{yesterday1}{state1}'
                messagebox.showinfo('', result)
        else:
            messagebox.showwarning('查询结果', '你的输入无效或错误！')
    def quit2():
        if messagebox.askyesno('确认界面','你确认吗？'):
            messagebox.showinfo('退出','感谢使用')
            root.destroy()
            root.quit()
    def ask_for_help():
        if messagebox.askyesno('确认界面','你确认吗？'):
            messagebox.showinfo('联系方式','加v：123')

    root = tk.Tk()
    root.geometry('500x300')
    root.title(f'天气查询工具 现在时间是....{now}')
    tk.Label(root,text='当前只支持北京，上海，杭州，广州，深圳，武汉，南京，济南，郑州，苏州地区天气').pack()
    input1 = tk.Entry(root, width=40)
    input1.default_text = '在此输入位置....'
    input1.insert(0, input1.default_text)
    input1.bind('<FocusIn>', click)
    input1.pack()
    button = tk.Button(root, text='下一步', command=f_i_r_s_t)
    button.pack()
    button1 = tk.Button(root,text='退出',command=quit2)
    button1.pack()
    button2 = tk.Button(root,text='帮助',command=ask_for_help)
    button2.pack()
    root.mainloop()
s_e_c_o_n_d()
