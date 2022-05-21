import turtle as t # 그래픽 관련 라이브러리
import random # 난수 관련 라이브러리

# 변수 c는 coordinate를 의미합니다: (x, y)

t.setup(500, 500) # 화면 크기 지정
r = 100 # 반지름 지정

# 두 점(c1, c2)을 지나는 직선
def line(c1, c2):
    t.penup()
    t.goto(c1[0], c1[1])
    t.pendown()
    t.goto(c2[0], c2[1])
    t.penup()

# 점 c를 찍음
def dot(c, color='red'):
	t.goto(c[0], c[1])
	t.dot(5, color)

# 점 c가 원 안에 있는지 확인
"""
x^2 + y^2 에 점 (x1, y1)을 대입했을 때 r^2보다 작다면 점이 원 안에 위치함.
"""
def in_circle(c, r):
    return (c[0] ** 2 + c[1] ** 2) <= r ** 2

# 원주율 구하기
def pi(pos, total):
    return pos/total * 4



# 좌표평면 그리기
t.speed('fastest')
line((-500, 0), (500, 0))
line((0, -500), (0, 500))

# 원 그리기
t.goto(0, -r)
t.pendown()
t.circle(r) # x^2 + y^2 = r^2 (중심이 0,0 반지름이 r인 원)
t.penup()

# 원에 외접하는 정사각형 그리기
line((r,r), (-r,r))
line((-r,r), (-r,-r))
line((-r,-r), (r,-r))
line((r,-r), (r,r))

positive = 0 # 점이 원 안에 있음
negative = 0 # 점이 원 밖에 있음

for i in range(1, 10000):
    x = random.randint(-r, r)
    y = random.randint(-r, r)
    if in_circle((x, y), r):
        res = 'pos'
        positive += 1
    else:
        res = 'neg'
        negative += 1
    print(f'#{i} ({x}, {y}) => {res} : {pi(positive, i)}')
    dot((x,y))

print(positive, negative)

t.done()