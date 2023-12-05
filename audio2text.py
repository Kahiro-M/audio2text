# https://www.my-hacks.info/2023/05/03/%e6%99%82%e9%96%93%e3%81%a8%e3%82%b3%e3%82%b9%e3%83%88%e3%82%92%e5%89%8a%e6%b8%9b%e3%81%99%e3%82%8b%ef%bc%81python%e3%82%92%e4%bd%bf%e3%81%a3%e3%81%9f%e3%83%93%e3%82%b8%e3%83%8d%e3%82%b9%e3%81%ab/
import sys
from faster_whisper import WhisperModel
import ffmpeg
import re
import os
import tkinter, tkinter.filedialog, tkinter.messagebox
import datetime

# 一時的にカレントディレクトリのffmpeg.exeへパスを通す
cwd = os.getcwd()
bin_path = os.path.join(cwd)
os.environ['PATH'] = '{};{}'.format(bin_path, os.environ['PATH']) #セミコロン付きでPATHの先頭に追加

model_size = "large-v2"
 
 
def whisper_mp3(attach):
    for i, file in enumerate(attach):
 
        # 対象ファイル
        print('--- 対象ファイル')
        print(f'{i}:{file}')
 
        # MP3ファイル以外は変換する。
        if not file.endswith('.mp3'):
            print('  MP3に変換します。')
            file = ffmpeg_mp3(file)
            print('--- MP3変換結果 --- \n  ', file)
 
        print('------ 処理開始 '+datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')+' ------')
        result = whisper_proc(file)
        print('------ 処理完了 '+datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')+' ------')
 
        outfile = re.sub(r'\.(mp3|MP3)$', '_'+datetime.datetime.now().strftime('%Y%m%d_%H%M_%S')+'.txt', file)
        # with open(f'{dname}\\{outfile_name}', "w") as f:
        with open(outfile, "w") as f:
            f.write(result)
        return outfile
 
 
def add_line(s):
    new_s = s
    s_count = len(s)
    s_max_count = 40
    if s_count >= s_max_count:
        if (s_count - s_max_count) >= 3:
            # 15文字以上、かつ、2行目が3文字以上あれば、改行する
            # つまり、18文字以上であれば、15文字で改行する
            new_s = s[:s_max_count] + "\n" + s[s_max_count:]
    return new_s + "\n"
 
 
def whisper_proc(file):
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(file, beam_size=5)
    subs = []
    for data in segments:
        print("[%.2fs -> %.2fs] %s" % (data.start, data.end, data.text))
        text = add_line(data.text)
        subs.append(text)
    return ''.join(subs)
 
 
def ffmpeg_mp3(file):
    result_file = file + '.mp3'
    ffmpeg.run(
        ffmpeg.output(
            ffmpeg.input(file),
            result_file)
        )
    return result_file
 
 
if __name__ == '__main__':
    if(len(sys.argv)<2):
        # ファイル選択ダイアログの表示
        root = tkinter.Tk()
        root.withdraw()
        fTyp = [("","")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        # tkinter.messagebox.showinfo('文字起こし','処理ファイルを選択してください')
        file = tkinter.filedialog.askopenfilename(initialdir = iDir)
        fileList = [file]
    else:
        fileList = sys.argv[1:]
    if(len(fileList)>0):
        print('========= 文字起こし開始 '+datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')+' =========')
        textfile = whisper_mp3(fileList)
        print('========= 文字起こし完了 '+datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')+' =========\n', '以下のファイルを作成しました。\n・'+textfile)
        # tkinter.messagebox.showinfo('文字起こし処理完了', '以下のファイルを作成しました。\n'+textfile)
    
    input('何かキーを押すと終了します。')
    # print('文字起こし処理が完了しました。')