# ========文字起こしツール===========
- audio2text.exe
- audio2text_faster.exe

## ■exeの違い
- audio2text.exe  
    文字起こしの時間は長いですが、より精度が高い文章を生成できます。
- audio2text_faster.exe  
    文章生成の精度は低いですが、より高速で文章を生成できます。


## ■使い方
- audio2text.exe / audio2text_faster.exe　と同じ階層にffmpeg.exeを配置してください。  
    以下からFFmpegの実行ファイルをダウンロードし、audio2textと同じ階層に保存してください。  
    https://github.com/BtbN/FFmpeg-Builds/releases
- 起動し10秒ほど待つと、ファイル選択画面が表示されます。  
    mp3ファイルを選択してください。  
    選択したmp3ファイルと同じ階層に文字起こししたテキストファイルが生成されます。
- 複数ファイルを一度に処理したい場合は、コマンドラインからの起動してください。  
`$ audio2text.exe [ファイル1のフルパス] [ファイル2のフルパス] [ファイル2のフルパス] ...`


## ■生成にかかる時間の目安
### 20秒の音声の場合
|||
|:--|:--|
| audio2text.exe | 1分程度 |
| audio2text_faster.exe | 10秒程度 |

## ■参考
[時間とコストを削減する！Pythonを使ったビジネスにおすすめの文字起こし方法](https://www.my-hacks.info/2023/05/03/%e6%99%82%e9%96%93%e3%81%a8%e3%82%b3%e3%82%b9%e3%83%88%e3%82%92%e5%89%8a%e6%b8%9b%e3%81%99%e3%82%8b%ef%bc%81python%e3%82%92%e4%bd%bf%e3%81%a3%e3%81%9f%e3%83%93%e3%82%b8%e3%83%8d%e3%82%b9%e3%81%ab/
)