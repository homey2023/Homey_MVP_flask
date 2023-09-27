- 사용한 DB: 아마존 RDS 기반 MongoDB
- 사용한 백엔드 프레임워크: Flask


- 사용한 공공 데이터셋 : [assets/datasets/coordinate_based](assets/datasets/coordinate_based)
- DB로부터 데이터 가져와 점수 산출: [dataloader/dataloader.py](dataloader/dataloader.py)
- 좌표 데이터 정규화 및 오류 처리: [train/data_generator.py] (train/data_generator.py)
- 백엔드 API (회원가입, 설문조사, 안전등급 산출, 사용자의 등록된 주소 목록 등): [templates](templates)


- 데이터셋 목록: 서울특별시_유흥주점영업 인허가 정보, 경찰청 서울특별시경찰청_경찰서별 지역경찰 관서 현황, 서울시 안전센터관할 위치정보 (좌표계: WGS1984), 서울시 소방서,안전센터,구조대 위치정보, 서울특별시_(안심이) CCTV 설치 현황, 서울특별시 관악구_여성안심택배서울특별시_여성안심지킴이집 정보, 행정안전부_생활안전지도 안전비상벨

- 사용자 조사를 바탕으로 추가한 안전등급 분류 기준: 경비실 유무, 방범 창 유무, CCTV 유무, 엘리베이터 유무
 
