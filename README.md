# 🍻 MyLittleBeer

맥주 추천 웹서비스  

<br />

# 📃 프로젝트 정보

### 1. 제작기간

> 2022.06.02 ~ 06.13

### 2. 참여 인원

> |                    Name                    |  Position   |
> | :----------------------------------------: | :---------: |
> | [김동우](https://github.com/kimphysicsman) | Back, Front |
> |   [김진수](https://github.com/creamone)    |    Back     |
> |     [이윤지](https://github.com/yunji3)     |    Back     |
> |    [최민기](https://github.com/mankic)     |    Back     |

### 3. 역할 분담

> - 김동우 : 사용자가 선호하는 맥주 특징을 고르면 그것과 비슷한 유형의 맥주를 추천 (저장가능)
> - 김진수 : 로그인 / 회원가입 / 회원수정 / 회원탈퇴
> - 이윤지 : 저장된 추천 받은 검색 기록 리스팅 / 삭제 페이지
> - 최민기 : 맥주 정보를 볼 수 있는 리스팅 페이지 (조건을 걸어서 종류별로 리스팅할 수 있게)

<br />

# 📚 기술 스택

### 1. Back-end

> python3  
> Django  

### 2. Front-end
  
> Javascript

<br />

# 📊 ERD & Structure

<details>
<summary>ERD</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://user-images.githubusercontent.com/68724828/186067947-f255f9a4-d92d-45cd-ab7c-419ec92943f8.png" width="800px"/>
</div>
</details>

<br />

<details>
<summary>Structure</summary>
<div markdown="1" style="padding-left: 15px;">
<img src="https://user-images.githubusercontent.com/68724828/186079270-28793ba1-466e-421f-baf2-563b890c926f.png" />
</div>
</details>

<br />

# 🔑 핵심기능

### 1. 로그인 / 회원 가입 / 회원 수정 / 회원 탈퇴

> 사용자가 여행장소를 검색하면 DB에서 여행장소를 검색하고  
> DB에 없는 장소이면 네이버지도에서 검색하여 최상단의 장소의 정보를 가져오고 DB에 저장합니다.  
> [코드 보러가기](https://github.com/nbcamp-AI-2-fantastic4/MyLittelTrip_backend/blob/d9eba0efc4567cbaef9ec19eea76e76495190a69/recommend/functions/parsing.py#L70)

### 2. 최단 여행경로 찾기 & 여행일정 만들기

> 사용자가 입력한 여행장소들을 바탕으로 여행일정을 만듭니다.  
> [코드 보러가기](https://github.com/nbcamp-AI-2-fantastic4/MyLittelTrip_backend/blob/d9eba0efc4567cbaef9ec19eea76e76495190a69/recommend/functions/schedule.py#L14)

<br />

# 📕 기타 자료

### 1. 기획문서

> [MyLittleBeer - Notion](https://www.notion.so/kimphysicsman/MLB-MyLittleBeer-3c4edfa70eb24593ab1cc9b05f8e6e61)

### 2. 데이터셋 77종류의 맥주 정보

> [Beer_dataset - Github](https://github.com/ghgit1798/Crawling-Preprocessing/blob/main/CBF_Beer/%EB%A7%A5%EC%A3%BC_cbf_data.csv)

### 3. 발표영상

<table>
  <tbody>
      <td>
        <p align="center"> 22.08.05 발표 </p>
        <a href="https://www.youtube.com/watch?v=FcY93t-2oMI" title="MyLittleBeer 최종발표">
          <img align="center" src="https://user-images.githubusercontent.com/68724828/186087151-e0f0ebed-08c1-4a99-9af0-a8c48c536205.png" width="300" >
        </a>
      </td>
  </tbody>
</table>
