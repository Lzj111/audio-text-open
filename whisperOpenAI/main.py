# whisper open ai
import whisper
import win32ui
import time


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


def readText(path):
    # 模型下载地址：
    '''
        "tiny.en": "https://openaipublic.azureedge.net/main/whisper/models/d3dd57d32accea0b295c96e26691aa14d8822fac7d9d27d5dc00b4ca2826dd03/tiny.en.pt",
        "tiny": "https://openaipublic.azureedge.net/main/whisper/models/65147644a518d12f04e32d6f3b26facc3f8dd46e5390956a9424a650c0ce22b9/tiny.pt",
        "base.en": "https://openaipublic.azureedge.net/main/whisper/models/25a8566e1d0c1e2231d1c762132cd20e0f96a85d16145c3a00adf5d1ac670ead/base.en.pt",
        "base": "https://openaipublic.azureedge.net/main/whisper/models/ed3a0b6b1c0edf879ad9b11b1af5a0e6ab5db9205f891f668f8b0e6c6326e34e/base.pt",
        "small.en": "https://openaipublic.azureedge.net/main/whisper/models/f953ad0fd29cacd07d5a9eda5624af0f6bcf2258be67c92b79389873d91e0872/small.en.pt",
        "small": "https://openaipublic.azureedge.net/main/whisper/models/9ecf779972d90ba49c06d968637d720dd632c55bbf19d441fb42bf17a411e794/small.pt",
        "medium.en": "https://openaipublic.azureedge.net/main/whisper/models/d7440d1dc186f76616474e0ff0b3b6b879abc9d1a4926b7adfa41db2d497ab4f/medium.en.pt",
        "medium": "https://openaipublic.azureedge.net/main/whisper/models/345ae4da62f9b3d59415adc60127b97c714f32e89e936602e85993674d08dcb1/medium.pt",
        "large-v1": "https://openaipublic.azureedge.net/main/whisper/models/e4b87e7e0bf463eb8e6956e646f1e277e901512310def2c24bf0e11bd3c28e9a/large-v1.pt",
        "large-v2": "https://openaipublic.azureedge.net/main/whisper/models/81f7c96c852ee8fc832187b0132e569d6c3065a3252ed18e56effd0b6a73e524/large-v2.pt",
        "large": "https://openaipublic.azureedge.net/main/whisper/models/81f7c96c852ee8fc832187b0132e569d6c3065a3252ed18e56effd0b6a73e524/large-v2.pt",
    '''
    abs_file = __file__
    abs_dir = abs_file[:abs_file.rfind("\\")]+"\\base.pt"
    model = whisper.load_model(abs_dir)
    # audio = whisper.load_audio(path)

    # # make log-Mel spectrogram and move to the same device as the model
    # mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # # decode the audio
    # options = whisper.DecodingOptions(language='zh', fp16=False)
    # result = whisper.decode(model, mel, options)
    result = model.transcribe(path)
    return result["text"]


if __name__ == "__main__":
    print("======= whisperOpenAI开始解析 =======")
    # 要解析的文件路径
    filePath = "E:/models/audios/16k.wav"
    filePath = openFileRtnFilePath()
    start = time.time()
    txt = readText(filePath)
    end = time.time()
    print("解析的文本为=>" + txt)
    print("耗时%f毫秒=>" % (int(end - start) * 1000))
