# シーザー(カエサル)暗号
    厳密にはアルファベット3文字ずらす処理のみをシーザー暗号と呼ぶ。

    trコマンドを用いてシーザー暗号を実現
    - 暗号
    $ echo AKADEMIA | tr A-Z D-ZA-C
    - 復号
    $ echo DNDGHPHLD | tr D-ZA-C A-Z