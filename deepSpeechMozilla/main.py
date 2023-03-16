# 调用deepSpeechMozilla进行语音识别
import time
import win32ui
from deepspeech import Model, version
import wave
import numpy as np
import subprocess
import shlex

try:
    from shhlex import quote
except ImportError:
    from pipes import quote

def openFileRtnFilePath():  # 打开文本对话框，选择文件后返回路径
    # 0代表另存为对话框，1代表打开文件对话框
    dlg = win32ui.CreateFileDialog(1)
    # 设置默认目录
    dlg.SetOFNInitialDir("E:/")
    # 显示对话框
    dlg.DoModal()
    # 获取用户选择的文件全路径
    filename = dlg.GetPathName()
    return filename

def convert_samplerate(audio_path, desired_sample_rate):
    sox_cmd = 'sox {} --type raw --bits 16 --channels 1 --rate {} --encoding utf-8 --endian little --compression 0.0 --no-dither - '.format(quote(audio_path), desired_sample_rate)
    try:
        output = subprocess.check_output(shlex.split(sox_cmd), stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        raise RuntimeError('SoX returned non-zero status: {}'.format(e.stderr))
    except OSError as e:
        raise OSError(e.errno, 'SoX not found, use {}hz files or install it: {}'.format(desired_sample_rate, e.strerror))

    return desired_sample_rate, np.frombuffer(output, np.int16)

def readText(path):  # 解析音频文本
    if path is None:
        return ""
    abs_file = __file__
    model_path = abs_file[:abs_file.rfind("\\")]+"\\deepspeech-0.9.3-models-zh-CN.tflite"
    ds = Model(model_path)
    fin = wave.open(path, 'rb')
    fs_orig = fin.getframerate()

    desired_sample_rate = ds.sampleRate()
    if fs_orig != desired_sample_rate:
        print('Warning: original sample rate ({}) is different than {}hz. Resampling might produce erratic speech recognition.'.format(fs_orig, desired_sample_rate), file=sys.stderr)
        fs_new, audio = convert_samplerate(path, desired_sample_rate)
    else:
        audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)

    audio_length = fin.getnframes() * (1/fs_orig)
    fin.close()
    str = ds.stt(audio)
    return str
    

# 主函数
if __name__ == "__main__":
    print("======= deepSpeechMozilla开始解析 =======")
    # 要解析的文件路径
    filePath = "E:/models/audios/16k.wav"
    filePath = openFileRtnFilePath()
    start = time.time()
    txt = readText(filePath)
    txt= txt.encode('utf-8', 'replace').decode('utf-8')
    end = time.time()
    print("解析的文本为=>" + txt)
    print("耗时%f毫秒=>" % (int(end - start) * 1000))