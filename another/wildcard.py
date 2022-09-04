# C = int(input())
C = 4

w_list = ["he?p", "*p*", "*bb*",'*p*l*']
n_list = [3,3,1,3]
name_list = [
    ["help","heap", "helpp"],
    ["help","papa","hello",],
    ["babbbc"],
    ["help","papa","hello","ppplaa"]
]

def match(w_idx, s_idx) :

    if dp[w_idx][s_idx] :
        return dp[w_idx][s_idx]

    while w_idx < len_wild and s_idx < len_str and (wild_card[w_idx] == string[s_idx] or wild_card[w_idx] == '?') :
        s_idx += 1
        w_idx += 1

    if w_idx == len_wild  :
        dp[w_idx][s_idx] = (s_idx == len_str)
        return dp[w_idx][s_idx]

    if wild_card[w_idx] == '*' :

        for i in range(s_idx, len_str+1) :
            if match(w_idx+1, i) :
                dp[w_idx][s_idx] = True
                return True

    dp[w_idx][s_idx] = False
    return False
answer = []

for i in range(C) :

    wild_card = w_list[i]
    n = n_list[i]
    strings = name_list[i]

    ans = []
    for string in strings :
        len_wild = len(wild_card)
        len_str = len(string)
        dp = [[None for _ in range(110)] for _ in range(110)]
        if match(0,0) :
            ans.append(string)

    answer.extend(sorted(ans))

for str in answer :
    print(str)