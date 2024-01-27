# wordcloud-template

ワードクラウドを簡単に作りたい人のためのdocker環境。
[SudachiPy](https://github.com/WorksApplications/SudachiPy) を使用。

## 使い方

1. `textList` にワードクラウドを作りたい文章の配列を入れる
1. 以下を実行する

    ```bash
    $ docker compose up 
    ```

1. `wordcloud.png` が作成される

ユーザ辞書は `user_dic.csv` に必要な情報を書けば自動で反映される。記法は [この辺り](https://github.com/WorksApplications/Sudachi/blob/develop/docs/user_dict.md) を参照。