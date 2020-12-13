# シフト暗号
    シーザー暗号をより汎用的に改良したもの。
    循環しているためROT**と表記することがある。

    - nkfコマンドを用いてROT13を実現
    $ cat plain.txt
    I love you.
    $ nkf -r plain.txt
    $ cat cipher.txt
    V ybir lbh.
    $ nkf -r cipher.txt
    I love you.

- 実装コード: [shift_code.py](https://github.com/codon-sec/crypto_cheet_sheet/tree/main/classical_cipher/shift_code.py)
