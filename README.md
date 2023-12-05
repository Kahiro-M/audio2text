========文字起こしツール===========
・audio2text.exe
・audio2text_faster.exe　

■exeの違い
・audio2text.exe
　文字起こしの時間は長いですが、より精度が高い文章を生成できます。
・audio2text_faster.exe　
　文章生成の精度は低いですが、より高速で文章を生成できます。


■使い方
・audio2text.exe / audio2text_faster.exe　と同じ階層にffmpeg.exeを配置してください。
　以下からFFmpegの実行ファイルをダウンロードし、audio2textと同じ階層に保存してください。
　https://github.com/BtbN/FFmpeg-Builds/releases
・起動し10秒ほど待つと、ファイル選択画面が表示されます。
　mp3ファイルを選択してください。
　選択したmp3ファイルと同じ階層に文字起こししたテキストファイルが生成されます。


■生成にかかる時間の目安
・20秒の音声の場合
　audio2text.exe　　　　 →　1分程度
　audio2text_faster.exe　→　30秒程度
