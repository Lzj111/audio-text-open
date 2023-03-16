# 调用paddlespeech百度飞浆 进行语音识别
from paddlespeech.cli.asr.infer import ASRExecutor
import time
import win32ui

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


def readText(path):  # 解析音频文本
    if path is None:
        return ""
    asr = ASRExecutor()
    result = asr(path)
    return result


# 主函数
if __name__ == "__main__":
    print("======= deepSpeech2开始解析 =======")
    # 要解析的文件路径
    filePath = "E:/models/audios/16k.wav"
    filePath = openFileRtnFilePath()
    start = time.time()
    txt = readText(filePath)
    end = time.time()
    print("解析的文本为=>" + txt)
    print("耗时%f毫秒=>" % (int(end - start) * 1000))