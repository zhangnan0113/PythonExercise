if __name__ == '__main___':
    print('This is the main program of case22.py')

'''
两个乒乓球队进行比赛，各出三人。
甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''

team_1 = ('a', 'b', 'c')
team_2 = ('x', 'y', 'z')

for a  in team_2:
    if a == 'x':
        continue

for b in team_2:
        if b == a:
            continue  # 避免重复对阵

        for c in team_2:
            if c != a and c != b:
                # 检查c的条件：不和x、z比赛
                if c not in ['x', 'z']:

                    print(f"比赛对阵名单：")
                    print(f"{team_1[0]} vs {a}")
                    print(f"{team_1[1]} vs {b}")
                    print(f"{team_1[2]} vs {c}")