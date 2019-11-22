MEMBER_1 = "Yiqi has a cool sweater"
MEMBER_2 = "Mary Grace"
MEMBER_3 = "Emily"

MEMBER_1_HOME = "Hangzhou, China"
MEMBER_2_HOME = "Louisville, Kentucky"
MEMBER_3_HOME = "Grand Rapids, MI"

MEMBERS = {
    MEMBER_1:MEMBER_1_HOME,
    MEMBER_2:MEMBER_2_HOME,
    MEMBER_3:MEMBER_3_HOME,
}

for k,v in MEMBERS.items():
    print(f"{k} is from {v}")
