# wordcloud-template

ワードクラウドを簡単に作りたい人のためのdocker環境。
[SudachiPy](https://github.com/WorksApplications/SudachiPy) を使用。


## 使い方

```bash
$ chmod +x ./run.sh
$ ./run.sh
```

上記コマンド実行により `wordcloud.png` が作成される

ユーザ辞書は `user_dic.csv` に必要な情報を書けば自動で反映される。記法は [この辺り](https://github.com/WorksApplications/Sudachi/blob/develop/docs/user_dict.md) を参照。  
何も入っていないとエラーになり、エラー処理も面倒だったので最初からサンプルデータを入れてある。