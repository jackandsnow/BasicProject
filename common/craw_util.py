import multiprocessing
import random
import time

import requests
from lxml import etree

agent = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'
]


def get_html_text(url, params=None, proxies=None, total=3):
    """
    get the text of target url
    :param url: target url
    :param params: params dict, like {'param1': 'value1', 'param2': 'value2'}
    :param proxies: proxies dict, like {'http': 'proxy1', 'https': proxy2}, its keys are unchangeable
    :param total: repeat times if time out
    :return: html text or None
    """
    try:
        headers = {'User-Agent': random.choice(agent)}
        r = requests.get(url, params=params, proxies=proxies, headers=headers, timeout=5)
    except requests.exceptions.ConnectionError:  # connection error
        print('Connection Error:', url)
        return None
    except Exception:
        if total > 0:
            time.sleep(5)  # after 5 seconds continue to craw
            return get_html_text(url, params, proxies, total - 1)
        return None
    # get encodings of the website
    encodings = requests.utils.get_encodings_from_content(r.text)
    if len(encodings) == 0:
        r.encoding = 'gbk'
    else:
        r.encoding = encodings[0]
    return r.content


def download_file(file_url, filename, total=3):
    """
    download file, such as word, excel, ppt, pdf, mp4 file, etc.
    :param file_url: file URL
    :param filename: filename
    :param total: max download times
    :return: bool flag of success
    """
    try:
        res = requests.get(file_url)
        fp = open(filename, mode='wb')
        fp.write(res.content)
        fp.close()
    except Exception:
        if total > 0:
            return download_file(file_url, filename, total - 1)
        return False
    return True


def run_with_multiprocessing(url_list):
    """
    run craw job with multi-processes
    :param url_list: target urls
    :return: None
    """
    max_cpu_num = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(max_cpu_num - 2)
    for url in url_list:
        # craw_job_function should be defined first
        pool.apply_async('craw_job_function', args=(url, 'arg1', 'arg2',))
    pool.close()
    pool.join()


def download_paper(doi, filename=None):
    """
    Download paper by its doi
    :param doi: paper's doi, like '10.1145/3292500.3330947'
    :param filename: '/path/filename.pdf'
    :return: None
    """
    try:
        sci_hub = 'https://sci-hub.tw/'
        html_text = get_html_text(sci_hub + doi)
        if html_text:
            html = etree.HTML(html_text)
            url = html.xpath('//div[@id="article"]/iframe/@src')[0]
            url = url.replace('#view=FitH', '?download=true')
            url = url if url.contains('https:') else 'https:' + url
            filename = filename if filename else url.split('?')[0].split('/')[-1]
            flag = download_file(url, filename)
            if not flag:
                print('Download Paper DOI[' + doi + '] Failed!')
    # Verification code skipped
    except IndexError:
        print(doi + ': Error with getting download url!')
