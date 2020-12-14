# ECB(Electronic CodeBook)
最も単純な暗号化  
同一の平文ブロックからは同一の暗号文が生成される  
並列処理しやすい  

### opensslコマンドを用いてECB暗号化・復号
 ```
head -n 4 image.ppm > header.txt
tail -n +5 image.ppm > body.bin
openssl enc -aes-128-ecb -nosalt -pass pass="codon-sec" -in body.bin -out body.ecb.bin
cat header.txt body.ecb.bin > image.ecb.ppm
openssl enc -aes-128-cbc -nosalt -pass pass:"codon-sec" -in body.bin
 -out body.cbc.bin
cat header.txt body.cbc.bin > image.cbc.ppm 
 ```
gimpでECBモードの画像のみ元画像の推定が可能
