# Simple Photoshop with PySide6 & OpenCV

PySide6와 OpenCV를 활용하여 만든 간단한 이미지 편집 프로그램입니다. 
다양한 영상 처리 알고리즘을 GUI 환경에서 직관적으로 테스트할 수 있도록 제작되었습니다.

## 주요 기능

이 프로그램은 다음과 같은 이미지 처리 기능을 제공합니다:

* **반전/색변환**: 좌우/상하 반전, 흑백 변환 등 기본 편집
* **기하학적 변환**: 확대/축소, 다양한 회전, 어핀/원근/비선형 변환
* **왜곡 효과**: 오목/볼록, 핀쿠션/배럴, 거울 왜곡 등 6종 지원
* **고급 필터**: 4종의 블러링(Blurring), 6종의 경계 검출(Edge Detection)
* **지능형 기능**: Haar Cascade 기반 얼굴 인식 및 ROI 선택형 모자이크


### 사용 방법

<img width="850" height="500" alt="photoshop_3" src="https://github.com/kkkimsuji/photoshop/assets/117288953/a44c6d4b-61a9-479d-b87b-9f90c10f3f65">


1. **이미지 열기**: 편집할 이미지를 불러옵니다.
2. **기능 실행**: 좌측 사이드바의 버튼을 클릭하여 즉시 결과를 확인합니다.
3. **새로고침**: 현재 작업 결과물을 초기화합니다.
4. **중복 적용**: 얼굴인식, 모자이크 등 일부 기능은 다른 필터와 중복 적용이 가능합니다.



---

## 사진 변환 결과 

### 1. 기본 변환 및 회전 (Basic & Rotation)
| 좌우 반전 | 상하 반전 | 상하좌우 반전 | 흑백 변환 |
| :---: | :---: | :---: | :---: |
| ![LR](https://github.com/kkkimsuji/photoshop/assets/117288953/4d33ad8d-d94c-4b49-83a8-ab13017ed46e) | ![UD](https://github.com/kkkimsuji/photoshop/assets/117288953/bf817665-16d0-46bb-9ee7-555285d3f415) | ![UDLR](https://github.com/kkkimsuji/photoshop/assets/117288953/56508409-303e-4abd-ac79-554b02c3cdf6) | ![GRAY](https://github.com/kkkimsuji/photoshop/assets/117288953/763a76e8-9683-4c78-b36c-00b04ac65cd8) |

| 확대 | 축소 | 45도 회전 | 90도 회전 | 축소 회전 |
| :---: | :---: | :---: | :---: | :---: |
| ![Big](https://github.com/kkkimsuji/photoshop/assets/117288953/2cb9c487-5375-4685-b3fb-4f3fc6fc057a) | ![small](https://github.com/kkkimsuji/photoshop/assets/117288953/d5ec38c4-b6ff-41bb-9c28-44396bb66dca) | ![45](https://github.com/kkkimsuji/photoshop/assets/117288953/6b72abce-9ee3-4140-93ae-787c4d0510b2) | ![90](https://github.com/kkkimsuji/photoshop/assets/117288953/756edade-82f6-4377-a300-a4e9968698fc) | ![small45](https://github.com/kkkimsuji/photoshop/assets/117288953/1e9861e0-e49f-4510-8b74-af8d2859f26a) |

### 2. 기하학적 변환 및 왜곡 (Transform & Distortion)
| 어핀 변환 | 원근 변환 | 비선형 변환 |
| :---: | :---: | :---: |
| ![affine](https://github.com/kkkimsuji/photoshop/assets/117288953/c57a71ae-a47d-481e-9cc6-919f4de54b71) | ![perspective](https://github.com/kkkimsuji/photoshop/assets/117288953/872364e2-96b1-4d07-a1c6-36f98156c6c8) | ![wave](https://github.com/kkkimsuji/photoshop/assets/117288953/63cfef93-8d53-4a89-99a6-2ed139cac0d5) |

| 오목 왜곡 | 볼록 왜곡 | 핀쿠션 왜곡 | 배럴 왜곡 | 좌우 거울 | 상하 거울 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| ![conc](https://github.com/kkkimsuji/photoshop/assets/117288953/9aefa488-a3eb-459e-add8-1844714b3eea) | ![conv](https://github.com/kkkimsuji/photoshop/assets/117288953/a0ff4e18-6039-44ce-86b9-bbb90f99825e) | ![pinc](https://github.com/kkkimsuji/photoshop/assets/117288953/4704b114-ebcb-43ca-ab86-e7ecdd280e93) | ![barr](https://github.com/kkkimsuji/photoshop/assets/117288953/4e6e8435-eb2d-4091-a3ff-f145f8bdd28f) | ![mLR](https://github.com/kkkimsuji/photoshop/assets/117288953/6a3e03b4-297d-4cf7-ae8e-20b1c0513ad3) | ![mUD](https://github.com/kkkimsuji/photoshop/assets/117288953/6046c5c2-9d20-4ed4-a27b-f12ccabb87dc) |

### 3. 필터 및 경계 검출 (Blurring & Edge Detection)
| 평균 블러링 | 가우시안 블러 | 미디언 블러 | 바이레터럴 블러 |
| :---: | :---: | :---: | :---: |
| ![blur](https://github.com/kkkimsuji/photoshop/assets/117288953/677aa146-be7c-43ee-a21d-34aba253d096) | ![gauss](https://github.com/kkkimsuji/photoshop/assets/117288953/3bd20eaa-c80c-4bca-ad7a-5deb4addf13b) | ![med](https://github.com/kkkimsuji/photoshop/assets/117288953/f15edf17-9c35-49ff-a64f-f67657d0db8c) | ![bilat](https://github.com/kkkimsuji/photoshop/assets/117288953/a39c457f-cfc8-4216-a92e-831f479a915a) |

| 기본 미분 | 로버츠 교차 | 케니 엣지 | 프리윗 | 소벨 | 라플라시안 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| ![diff](https://github.com/kkkimsuji/photoshop/assets/117288953/527889ff-3f9d-48ac-85bf-2badec1a1f51) | ![rob](https://github.com/kkkimsuji/photoshop/assets/117288953/2c9047ba-1788-47e3-8199-af2031923c50) | ![can](https://github.com/kkkimsuji/photoshop/assets/117288953/4304aaea-47c0-445f-a5fb-b5dadf930551) | ![pre](https://github.com/kkkimsuji/photoshop/assets/117288953/fc76143a-466f-4cb0-98b8-f5f8052af9cc) | ![sob](https://github.com/kkkimsuji/photoshop/assets/117288953/55827539-1324-4722-b1de-b00ce53ea216) | ![lap](https://github.com/kkkimsuji/photoshop/assets/117288953/f6392b79-896b-4779-b0cb-3850a491c54d) |

### 4. 영상 분할 및 지능형 기능 (Segmentation & AI)
| 컨투어 추출 | 허프 선 변환 | 얼굴 인식 | 얼굴 자르기 |
| :---: | :---: | :---: | :---: |
| ![cont](https://github.com/kkkimsuji/photoshop/assets/117288953/f437aa17-ffea-412f-9c58-37401f884b57) | ![hough](https://github.com/kkkimsuji/photoshop/assets/117288953/6d19b0be-a47e-44ba-aa07-c7afc791a4c0) | ![reg](https://github.com/kkkimsuji/photoshop/assets/117288953/478b2362-5095-4539-836a-b05617d8cc6b) | ![crop](https://github.com/kkkimsuji/photoshop/assets/117288953/adaf7dd3-3581-46d0-b224-699506c6d5da) |

---

## 모자이크 및 ROI 선택 

모자이크 기능은 별도의 팝업창에서 사용자가 직접 영역을 지정해야 합니다.

* **방법**: 마우스 드래그로 영역 선택 후 **Enter** 키를 눌러 적용합니다.
* **종료**: 작업 창이 닫히지 않을 경우 **Esc** 키를 누른 후 창 닫기를 수행합니다.

| ROI 선택 가이드 | 일반 모자이크 결과 | 블러 모자이크 결과 |
| :---: | :---: | :---: |
| <img src="https://github.com/kkkimsuji/photoshop/assets/117288953/4c917f97-79b4-41e5-8ce4-6482510e0193" width="220"> | <img src="https://github.com/kkkimsuji/photoshop/assets/117288953/31fa860f-4f35-4d96-8159-13fea33d21ff" width="280"> | <img src="https://github.com/kkkimsuji/photoshop/assets/117288953/3c44c461-e502-42f9-a5f8-b65c38f2550e" width="280"> |



<img width="700" height="300" alt="blur_mosaic_result" src="https://github.com/kkkimsuji/photoshop/assets/117288953/3c44c461-e502-42f9-a5f8-b65c38f2550e">

