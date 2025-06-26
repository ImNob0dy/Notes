rev_flag = "ocip{FTC0l_I4_t5m_ll0m_y_y3n4cdbae52ÿó}"

block = []
for i in range(0, len(rev_flag),4):
    chunk = rev_flag[i:]
    if len(chunk)>4:
        chunk = chunk[:4]
    block.append("".join(chunk))
flag = ""
for b in block:
    flag = flag + b[::-1]
print(flag)