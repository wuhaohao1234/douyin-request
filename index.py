import requests
import re
import json

with open('./test.json','r',encoding='utf8')as fp:
  urlList = json.load(fp)

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
  'cookie': 'MONITOR_DEVICE_ID=5ea1bc4b-00d8-4578-a03c-9b639235f7d2; douyin.com; MONITOR_WEB_ID=59358f4c-81f7-4907-85c7-00730b315719; ttcid=a805fa6463bc4acf913c834196be499840; n_mh=GQssm0lZs-jVBO_pbDDuTQmYxr7VF1iReslsek-V5kM; sso_uid_tt=8a59bab92cc20278db22136656fbf4ab; sso_uid_tt_ss=8a59bab92cc20278db22136656fbf4ab; toutiao_sso_user=616bbf92fe91f95377bee5b5940e1f9e; toutiao_sso_user_ss=616bbf92fe91f95377bee5b5940e1f9e; _tea_utm_cache_2018=undefined; passport_csrf_token_default=356c0466287f7e1a4298e563b0af4283; passport_csrf_token=356c0466287f7e1a4298e563b0af4283; ttwid=1%7CL5oyKYxxP7x-mv6Mp7tj4E_jlGDe9pXKovR_LCVzZSw%7C1637683590%7Cd74a36f2ae28edd28ba53bf53a0d9c3efcb8dca7646e3cb00b2374f75d3bc73a; douyin.com; s_v_web_id=verify_kwdmrqvr_jNbwBOzm_qx1K_4iSZ_8jGX_L05IxjBpsCNQ; odin_tt=30a63ead36fc7bb1d77282ca853c61a016b16855806eef30489df616bf8e4596ea0e081d69d3c0131fc79a46bbb7f2b62571253f2b4101ce3f12458eae7831d8; passport_auth_status_ss=a84fe75b85ab5b8080592713c36dfde3%2C; sid_guard=da8bc2f6939f4fe4a94b1f2dbbc303fc%7C1637764693%7C5183998%7CSun%2C+23-Jan-2022+14%3A38%3A11+GMT; uid_tt=1de7076178cb275c4e52f6542e222dbc; uid_tt_ss=1de7076178cb275c4e52f6542e222dbc; sid_tt=da8bc2f6939f4fe4a94b1f2dbbc303fc; sessionid=da8bc2f6939f4fe4a94b1f2dbbc303fc; sessionid_ss=da8bc2f6939f4fe4a94b1f2dbbc303fc; sid_ucp_v1=1.0.0-KDg3YmZkOGRlNDlkMWMxMDI4MWU5MjNlM2RmMzQ2MmM4MmI1Mjg4NzAKFwjo4uDI1oz-BxDVnPmMBhjvMTgGQPQHGgJsZiIgZGE4YmMyZjY5MzlmNGZlNGE5NGIxZjJkYmJjMzAzZmM; ssid_ucp_v1=1.0.0-KDg3YmZkOGRlNDlkMWMxMDI4MWU5MjNlM2RmMzQ2MmM4MmI1Mjg4NzAKFwjo4uDI1oz-BxDVnPmMBhjvMTgGQPQHGgJsZiIgZGE4YmMyZjY5MzlmNGZlNGE5NGIxZjJkYmJjMzAzZmM; passport_auth_status=a84fe75b85ab5b8080592713c36dfde3%2C; _tea_utm_cache_6383=undefined; home_can_add_dy_2_desktop=0; _tea_utm_cache_1300=undefined; __ac_nonce=061a10af70062e6c62435; __ac_signature=_02B4Z6wo00f01HX6kjwAAIDBDTR5OzlBVbh13paAAHznjxcmBHX.YI2DotRMuUpe.6aXrl0KR1UGGHlS-hqK0HhSjJs1mQBX2Aw.0pm5h6q3PL41cIvDYsfWoECZ9rYCKQ8oUvMsHLX3Z05y41; FOLLOW_NUMBER_YELLOW_POINT_INFO=MS4wLjABAAAAdRqGLmK0hcIiFf4drOaHTUQLVnyjIsE7qcbKO51ZUJCpdFJ1tUkCSirGiBTUlnto%2F1638028800000%2F0%2F1637944057591%2F0; csrf_session_id=5e3282314a4ded825644458b5241b22e; msToken=nrxF9zPZ0YSmvfiDdFl5isD7QCvhPkMflzmd3oWsCvuSBn1oDFE4GzKCVZH269c2rw6VYE6-ghSC6klcjRFJrgtcq94EVPA9b2L4wnStHXq0rZ0mPgFMwotcuHeU; _tea_utm_cache_1243={%22utm_source%22:%22weixin%22%2C%22utm_medium%22:%22aweme_ios%22%2C%22utm_campaign%22:%22client_share%22}; msToken=2jjDylmZMT2KkFyJ2oK72Dj8dQlYLWsSAmxTjv3D3N9sZvqqGLoDfLpMgWvbImq2lpXzCOCt5Vg1B03SY6i3KAWW1SQoSgvjaG0FfUjvaTBtyeWwW2LBw1cXKXgy; tt_scid=guY-hTX5IMRu8xK8gmGSB0jPNJpOIJSUuYWqb.nq5m.tZ2nomHIPfSBTVURE8sPpde37'
}
for url in urlList:
  response = requests.get(url=url, headers=headers)
  title = re.findall('<title data-react-helmet="true">([\s\S]*)</title>', response.text)
  href = re.findall('src(.*?)vr%3D%2', response.text)[1]
  video_url = requests.utils.unquote(href).replace('":"', 'https:')

  print(title)
  print(video_url)

  video_content = requests.get(url=video_url, headers=headers).content
  with open('./video/' + title[0] +'.mp4', 'wb') as f:
    f.write(video_content)