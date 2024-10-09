import hashlib
import time
from Crypto.Hash import SHA256

def pow(nickname, zeros):
    nonce = 0
    start_time = time.time()
    while True:
        input_str = f"{nickname}{nonce}".encode()
        hash_result = hashlib.sha256(input_str).hexdigest()
        if hash_result.startswith('0' * zeros):
            elapsed_time = time.time() - start_time
            print(f"找到满足 {zeros} 个0开头的哈希: {hash_result}，花费时间: {elapsed_time:.2f}秒")
            break
        nonce += 1


# 运行POW
pow("Ethanzhang666888", 4)
pow("Ethanzhang666888", 5)

