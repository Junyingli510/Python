import requests

def download_pdf(file_url, save_file_name, retry_num=3):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        }
        r = requests.get(file_url, stream=True, headers=headers)
        with open(save_file_name, "wb") as pdf:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    pdf.write(chunk)
    except:
        if retry_num > 0:
            download_pdf(file_url=file_url, save_file_name=save_file_name, retry_num=retry_num - 1)