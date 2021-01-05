from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

target_movie =db.movies.find_one({'title':"월-E"})
target_star = target_movie['star']
#print(target_star)

#조회 여러개
#same_movies = list(db.movies.find({'star': target_star}, {'_id': False}))

#for m in same_movies:
    #print(m['title'])

db.movies.update_many({'star': target_star}, { '$set': {'star': 0}})
