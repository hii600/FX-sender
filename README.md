# FX sender scraping from Yahoo web page (in Japanese)
1.
プログラムをコピーし編集
```
cd FX-sender/src
cp cron.conf.sample cron.conf
cp run-get_fx_rates.sh.sample run-get_fx_rates.sh
```
デフォルトでは日曜以外の毎日17時にメール送信するよう設定

cron.confで希望配信日時および実行ディレクトリの絶対パスを指定

run-get_fx_rates.shでは送受信メールアドレスを指定

2.
cronを実行
```
crontab cron.conf
```
ジョブの確認および取り消し
```
crontab -l
crontab -r
```

