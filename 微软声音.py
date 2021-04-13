import win32com.client
#微软这个服务器
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("你好，小姐姐，能加个微信吗？")