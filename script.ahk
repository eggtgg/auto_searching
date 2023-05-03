Var_a := ["phap", "anh", "argentina", "ha lan", "my", "espana", "moroco", "viet nam", "a rap", "qatar"]
Var_b := ["thua", "thang", "hoa", "tap luyen cung", "da", "mua", "chung ket", "would cup", "ve nuoc", "ngoai giao", "phat trien", "kinh te"]

F1::
    loop ,25
    {
       Send, {ctrl down}{k down}{k up}{ctrl up}
       Random, tmp1 , 1, 10
       Random, tmp2 , 1, 12
       Sendraw, % Var_a[tmp1]
       Send, {space}
       Sendraw, % Var_b[tmp2]
       Send, {enter}
       Sleep, 100
    }
Return