import requests
import random
import sqlite3

rand_list = random.sample(range(1, 4436), 500)

conn = sqlite3.connect('house.db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS houseRentPriceInfo;")

cur.execute("""CREATE TABLE HouseRentPriceInfo
(   ID      INTEGER           NOT NULL,
    LAND_CD         NVARCHAR,
    ORG_CD      NVARCHAR,
    SN      NVARCHAR,
    ACC_YEAR  NVARCHAR,
    SGG_CD    NVARCHAR,
    SGG_NM    NVARCHAR,
    BJDONG_CD NVARCHAR,
    BJDONG_NM NVARCHAR,
    BOBN  NVARCHAR,
    BUBN  NVARCHAR,
    BLDG_NM   NVARCHAR,
    FLR_NO    NVARCHAR,
    HOUSE_GBN NVARCHAR,
    HOUSE_GBN_NM  NVARCHAR,
    RENT_AREA NVARCHAR,
    RENT_CD   NVARCHAR,
    RENT_CASE_NM  NVARCHAR,
    RENT_GTN  NVARCHAR,
    RENT_FEE  NVARCHAR,
    CNTRCT_YEAR   NVARCHAR,
    CNTRCT_DE NVARCHAR,   
    BUILD_YEAR    NVARCHAR,
    PRIMARY KEY (ID)
                      );
			""")

insert_key = "4c5a667a4c6d733237376973724350"
# row = list()
# for i in range(4437):
#     if i == 4436:
#         start = (i*1000)+1
#         end = (i*1000)+795
#         url = f"http://openapi.seoul.go.kr:8088/{insert_key}/json/houseRentPriceInfo/{start}/{end}/"
#         res = requests.get(url)
#         data = res.json()
#         for j in range(736):
#             CNTRCT_YEAR = data['houseRentPriceInfo']['row'][j]['CNTRCT_YEAR']
#             if CNTRCT_YEAR in ['2019', '2020', '2021']:
#                 ID = start+j
#                 data['houseRentPriceInfo']['row'][j]['ID'] = ID
#                 ID = data['houseRentPriceInfo']['row'][j]['ID']
#                 LAND_CD = data['houseRentPriceInfo']['row'][j]['LAND_CD']
#                 ORG_CD = data['houseRentPriceInfo']['row'][j]['ORG_CD']
#                 SN = data['houseRentPriceInfo']['row'][j]['SN']
#                 ACC_YEAR = data['houseRentPriceInfo']['row'][j]['ACC_YEAR']
#                 SGG_CD = data['houseRentPriceInfo']['row'][j]['SGG_CD']
#                 SGG_NM = data['houseRentPriceInfo']['row'][j]['SGG_NM']
#                 BJDONG_CD = data['houseRentPriceInfo']['row'][j]['BJDONG_CD']
#                 BJDONG_NM = data['houseRentPriceInfo']['row'][j]['BJDONG_NM']
#                 BOBN = data['houseRentPriceInfo']['row'][j]['BOBN']
#                 BUBN = data['houseRentPriceInfo']['row'][j]['BUBN']
#                 BLDG_NM = data['houseRentPriceInfo']['row'][j]['BLDG_NM']
#                 FLR_NO = data['houseRentPriceInfo']['row'][j]['FLR_NO']
#                 HOUSE_GBN = data['houseRentPriceInfo']['row'][j]['HOUSE_GBN']
#                 HOUSE_GBN_NM = data['houseRentPriceInfo']['row'][j]['HOUSE_GBN_NM']
#                 RENT_AREA = data['houseRentPriceInfo']['row'][j]['RENT_AREA']
#                 RENT_CD = data['houseRentPriceInfo']['row'][j]['RENT_CD']
#                 RENT_CASE_NM = data['houseRentPriceInfo']['row'][j]['RENT_CASE_NM']
#                 RENT_GTN = data['houseRentPriceInfo']['row'][j]['RENT_GTN']
#                 RENT_FEE = data['houseRentPriceInfo']['row'][j]['RENT_FEE']
#                 CNTRCT_DE = data['houseRentPriceInfo']['row'][j]['CNTRCT_DE']
#                 BUILD_YEAR = data['houseRentPriceInfo']['row'][j]['BUILD_YEAR']
#                 cur.execute("INSERT INTO HouseRentPriceInfo(ID, LAND_CD, ORG_CD,SN,ACC_YEAR,SGG_CD,SGG_NM,BJDONG_CD,BJDONG_NM,BOBN,BUBN,BLDG_NM,FLR_NO,HOUSE_GBN,HOUSE_GBN_NM,RENT_AREA,RENT_CD,RENT_CASE_NM,RENT_GTN,RENT_FEE,CNTRCT_YEAR,CNTRCT_DE,BUILD_YEAR) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
#                             (ID, LAND_CD, ORG_CD, SN, ACC_YEAR, SGG_CD, SGG_NM, BJDONG_CD, BJDONG_NM, BOBN, BUBN, BLDG_NM, FLR_NO, HOUSE_GBN, HOUSE_GBN_NM, RENT_AREA, RENT_CD, RENT_CASE_NM, RENT_GTN, RENT_FEE, CNTRCT_YEAR, CNTRCT_DE, BUILD_YEAR))
#     else:
cnt = 1
for element in rand_list:
    print(cnt)
    start = (element*1000)+1
    end = start+999
    url = f"http://openapi.seoul.go.kr:8088/{insert_key}/json/houseRentPriceInfo/{start}/{end}/"
    res = requests.get(url)
    data = res.json()
    for j in range(1000):
        CNTRCT_YEAR = data['houseRentPriceInfo']['row'][j]['CNTRCT_YEAR']
        if CNTRCT_YEAR in ['2019', '2020', '2021']:
            ID = start+j
            data['houseRentPriceInfo']['row'][j]['ID'] = ID
            ID = data['houseRentPriceInfo']['row'][j]['ID']
            LAND_CD = data['houseRentPriceInfo']['row'][j]['LAND_CD']
            ORG_CD = data['houseRentPriceInfo']['row'][j]['ORG_CD']
            SN = data['houseRentPriceInfo']['row'][j]['SN']
            ACC_YEAR = data['houseRentPriceInfo']['row'][j]['ACC_YEAR']
            SGG_CD = data['houseRentPriceInfo']['row'][j]['SGG_CD']
            SGG_NM = data['houseRentPriceInfo']['row'][j]['SGG_NM']
            BJDONG_CD = data['houseRentPriceInfo']['row'][j]['BJDONG_CD']
            BJDONG_NM = data['houseRentPriceInfo']['row'][j]['BJDONG_NM']
            BOBN = data['houseRentPriceInfo']['row'][j]['BOBN']
            BUBN = data['houseRentPriceInfo']['row'][j]['BUBN']
            BLDG_NM = data['houseRentPriceInfo']['row'][j]['BLDG_NM']
            FLR_NO = data['houseRentPriceInfo']['row'][j]['FLR_NO']
            HOUSE_GBN = data['houseRentPriceInfo']['row'][j]['HOUSE_GBN']
            HOUSE_GBN_NM = data['houseRentPriceInfo']['row'][j]['HOUSE_GBN_NM']
            RENT_AREA = data['houseRentPriceInfo']['row'][j]['RENT_AREA']
            RENT_CD = data['houseRentPriceInfo']['row'][j]['RENT_CD']
            RENT_CASE_NM = data['houseRentPriceInfo']['row'][j]['RENT_CASE_NM']
            RENT_GTN = data['houseRentPriceInfo']['row'][j]['RENT_GTN']
            RENT_FEE = data['houseRentPriceInfo']['row'][j]['RENT_FEE']
            CNTRCT_DE = data['houseRentPriceInfo']['row'][j]['CNTRCT_DE']
            BUILD_YEAR = data['houseRentPriceInfo']['row'][j]['BUILD_YEAR']
            cur.execute("INSERT INTO HouseRentPriceInfo(ID, LAND_CD, ORG_CD,SN,ACC_YEAR,SGG_CD,SGG_NM,BJDONG_CD,BJDONG_NM,BOBN,BUBN,BLDG_NM,FLR_NO,HOUSE_GBN,HOUSE_GBN_NM,RENT_AREA,RENT_CD,RENT_CASE_NM,RENT_GTN,RENT_FEE,CNTRCT_YEAR,CNTRCT_DE,BUILD_YEAR) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (ID, LAND_CD, ORG_CD, SN, ACC_YEAR, SGG_CD, SGG_NM, BJDONG_CD, BJDONG_NM, BOBN, BUBN, BLDG_NM, FLR_NO, HOUSE_GBN, HOUSE_GBN_NM, RENT_AREA, RENT_CD, RENT_CASE_NM, RENT_GTN, RENT_FEE, CNTRCT_YEAR, CNTRCT_DE, BUILD_YEAR))
    cnt += 1
conn.commit()
