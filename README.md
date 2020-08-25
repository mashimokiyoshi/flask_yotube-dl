# ヨウツベダウンローダ
Youtube動画をダウンロードすることができます。  
URL：https://thawing-mesa-77623.herokuapp.com/

## 環境構築
Docker準備
DockerfileのPORTの部分はHerokuデプロイ用のため消しておく。
```
docker build -t flask_yotube_docker .
docker run -p 5000:5000 -v /Users/~/flask_youtube-dl:/home -it flask_yotube_docker
```

## Heroku デプロイ
```
heroku container:push web -a アプリケーション名
heroku container:release web -a アプリケーション名
```