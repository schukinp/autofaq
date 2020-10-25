import subprocess
import websocket
import json


def send_message_to_bot(message):
    command = "curl 'https://chat.autofaq.ai/api/webhooks/widget/f4241354-7b39-4852-b9c5-855e18703afc/" \
              "af801330-49b4-43a0-9910-05da10fb8835/messages' \
    -H 'Connection: keep-alive' \
    -H 'Cache-Control: max-age=0' \
    -H 'Accept: application/json' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) " \
              "Chrome/86.0.4240.80 Safari/537.36' \
    -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryvQlsirybwNKUYoRG' \
    -H 'Origin: https://autofaq.ai' \
    -H 'Sec-Fetch-Site: same-site' \
    -H 'Sec-Fetch-Mode: cors' \
    -H 'Sec-Fetch-Dest: empty' \
    -H 'Referer: https://autofaq.ai/' \
    -H 'Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6' \
    --data-binary $'------WebKitFormBoundaryvQlsirybwNKUYoRG\r\nContent-Disposition: form-data; " \
              "name=\"payload\"\r\n\r\n{\"id\":\"a7ce5f49-a457-428b-b3cf-0a9aae577e13\",\"ts\":1603569435695," \
              "\"sender\":\"default\",\"text\":\"%s\",\"senderPayload\":{}}\r\n" \
              "------WebKitFormBoundaryvQlsirybwNKUYoRG--\r\n' \
    --compressed" % (message)
    subprocess.call(command, stdout=subprocess.DEVNULL, shell=True, stderr=subprocess.DEVNULL)


wss_url = "wss://chat.autofaq.ai/api/webhooks/widget/f4241354-7b39-4852-b9c5-855e18703afc" \
          "/af801330-49b4-43a0-9910-05da10fb8835/ws/1a1bed58-cee3-4413-99d1-b978a6d259fb"


def get_bot_response_to(message):
    ws = websocket.create_connection(wss_url)
    send_message_to_bot(message)
    response = json.loads(ws.recv())
    ws.close()
    return [response[i]['text'] for i in range(len(response))]
