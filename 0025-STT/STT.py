import pyaudio
import wave

CHUNK=1024
FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=16000
RECORD_SECONDS=int(input('输入录制时长(秒):'))
WAVE_OUTPUT_FILENAME='output.wav'

p=pyaudio.PyAudio()
stream=p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
print('*recording')
frames=[]
for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
    data=stream.read(CHUNK)
    frames.append(data)
print('*done recording')
stream.stop_stream()
stream.close()
p.terminate()

wf=wave.open(WAVE_OUTPUT_FILENAME,'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# 引入Speech SDK
from aip import AipSpeech
# 定义常量
APP_ID = '9940363'
API_KEY = 'sEi8YNZnnWFjcdsuF9GYkHFP'
SECRET_KEY = '433df84465bd8f6769dd321daa222456'
# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
# 识别本地文件
result=aipSpeech.asr(get_file_content('output.wav'), 'wav', 16000, {
    'lan': 'zh',
})
if result['err_no'] != 0:
    print('没有识别到命令')
else:
    if('浏览器' in result['result'][0]):
        import webbrowser
        webbrowser.open('www.baidu.com',new=1,autoraise=True)
    else:
        print('没有打开浏览器的命令')