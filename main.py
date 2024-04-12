## 라이브러리 import
import oracledb as db

## DB에 연결
con = db.connect(user= 'ADAM', password='1234', dsn='localhost:1521/XE')
cursor = con.cursor() #DB 지시자

do=True
while(do):
    print('-----------------------------------------------\n')
    print('1. 등록 | 2. 조회 | 3. 수정 | 4. 삭제 | 5. 종료\n')
    print('-----------------------------------------------\n')
    select = input('>')
    if select== '1':
        ### 정보입력
        print('환자등록\n환자정보를 입력하세요\n')
        info = [input('환자id\n'), input('이름\n'), input('번호\n')]

        ### 중복 확인
        cursor.execute(f'select id from INFO where id= {info[0]}')
        chk= cursor.fetchall()
        ### id가 같은 행 갯수 확인
        chk = cursor.rowcount
        if chk > 0:
            print('동일한 Id가 존재합니다')
        else:
            cursor.execute(f"insert into INFO values('{info[0]}','{info[1]}','{info[2]}')")
            cursor.execute('commit')

    elif select== '2':
        print('환자조회')
        cursor.execute('select * from INFO')
        result = cursor.fetchall()
        print(result)

    elif select== '3':
        print('환자수정\n')
         ### 환자명 입력
        cursor.execute(f"select * from INFO where name = '{search}'")
        print(cursor.fetchall())
        fixId = input('수정할 환자 id 입력하세요> ')
        cursor.execute(f"select * from INFO where id = {fixId}")
        modify = [input('수정항목'), input('수정값')]

    elif select== '4':
        print('환자삭제\n')
        search = input('환자 이름 입력하세요> ')
        ### 환자명 입력
        cursor.execute(f"select * from INFO where name = '{search}'")
        print(cursor.fetchall())
        delId = input('삭제할 환자 id 입력하세요> ')
        ### id 대조하여 삭제
        cursor.execute(f"delete from INFO where id = {delId}")
        cursor.execute('commit')
        print('삭제완료')

    elif select== '5':
        print('종료')
        do= False
        con.close()
