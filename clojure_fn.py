# 함수를 거쳐 거짓이 나오기 전까지 참인 요소만 모아 반환
def drop_while(F, COLL):
    TF_TUPLE = tuple(map(F, COLL))
    return COLL[:TF_TUPLE.index(False)] if False in TF_TUPLE else COLL
