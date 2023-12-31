# Django 메모장 
-------------

### 목차
1. 목표와 기능
2. 개발 환경 & 사용 기술
3. 프로젝트 시연
4. 프로젝트 구조
5. 개발 일정
6. 프로젝트 개선점

-----------------


## 1. 목표와 기능
목표
* Python DRF 의 CRUD 기능을 구현할 수 있는 페이지를 만들고자 하였다
* 제목 / 내용의 입력으로 DB에 권한 제한 없이 메모를 입력할 수 있는 웹페이지를 작성하였다
* DRF의 지원을 받아 주고 받는 Json 데이터의 흐름을 확인하고 Django가 처리하는 로그를 확인할 수 있었다
![DRFPostsList](https://github.com/sk7556/djangoChat/assets/109896609/237070e5-b4c3-4021-860d-f2b6eba2fa91)

## 2. 개발 환경 & 사용 기술
[FrontEnd]

![image](https://github.com/sk7556/djangoChat/assets/109896609/8a02c758-2724-4a6f-83fa-74fb2ed5cac6)
![image](https://github.com/sk7556/djangoChat/assets/109896609/f5ec4aba-16d1-443e-8d31-d785cc37227e)
![image](https://github.com/sk7556/djangoChat/assets/109896609/c522724d-677f-439c-9de0-740a769f1dca)


[BackEnd]

 ![image](https://github.com/sk7556/djangoChat/assets/109896609/a6439836-7e87-4c4e-9135-ea6f5578c028)
![image](https://github.com/sk7556/djangoChat/assets/109896609/22b5d9b2-94f8-4da4-afc7-981ce5389367)

[Tool]

 ![image](https://github.com/sk7556/djangoChat/assets/109896609/cac7225c-de4c-4c43-86ce-ae0adbc7874c)
![image](https://github.com/sk7556/djangoChat/assets/109896609/fc02f169-7e8c-480c-873e-28a7cb27e5fe)

## 3. 프로젝트 시연
* 제목 / 내용 입력

![write](https://github.com/sk7556/djangoChat/assets/109896609/66186474-9d55-4861-b0e3-62c3b4e22ac6)

* 내용 삭제

![delete](https://github.com/sk7556/djangoChat/assets/109896609/6b8eb9d1-a09c-42ec-aeed-245617f73be2)

## 4. 프로젝트 구조

![tree](https://github.com/sk7556/djangoChat/assets/109896609/3ab18ff7-ee6a-442e-8f0e-cf7332c0d898)

#### API 명세

##### * blog
  
| App       | URL                   | Http Method | File | 기능 |
|------------|------------------------|-------------|-----|------|
| blog     | blog/posts/    | '' | api.html | API Json 확인 |
| ( live server )   |  localhost:5500    | POST | index.html | 메모입력 |
|     |     | GET | index.html | List출력 |
|     |     | DELETE | index.html | 메모삭제 |

## 5. 개발 일정
![image](https://github.com/sk7556/djangoChat/assets/109896609/93dbe3ab-8bfd-4a9c-9090-702ddefde4e2)

## 6. 프로젝트 개선점
* DRF 기본 기능에 대한 이해가 부족했고, 프로젝트 몰입 미흡으로 인해 주요 기능에 대한 구현이 이루어지지 못했습니다
* AWS 와 GitHub 에 의한 배포 경험을 진행하지 못해 아쉬웠습니다









