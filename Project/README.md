#게임 소개

1. 게임의 소개
	- 제목
		메이플스토리
		![메이플스토리] ([https://raw.githubusercontent.com/areass048/2020_2DGP/master/Project/needless/ne.jpg](https://raw.githubusercontent.com/areass048/2020_2DGP/master/Project/needless/ne.jpg))
	- 게임의 목적
		몬스터를 잡고 퀘스트를 클리어하며 캐릭터를 강하게 만든다

2. GameState 종류
	- LogoState
		메이플 로고를 띄우는 State
		메이플 로고
		3초 있다가 사라짐
	- TitleState
		게임으로 들어가는 State
		화면, 로그인 버튼
		로그인 버튼위에 마우스를 올리면 변하고, 클릭으로 다음 State로 넘어갈 수 있다.
	- SelectCharState
		캐릭터를 선택할 수 있는 State
		캐릭터, 게임 시작 버튼
		마우스를 이용하여 캐릭터를 선택하면 캐릭터가 움직임
		캐릭터가 선택된 상태에서 게임시작을 클릭하면 다음 State로 넘어갈 수 있음
	- VillageState
		NPC가 있는 마을 State
		마을, 미니맵, NPC(상점/창고/퀘스트)
		상점에 가서 클릭으로 포션을 살 수 있고, 우측 클릭으로 아이템을 팔 수 있다.
		창고에서 아이템을 더블클릭으로 꺼내거나 집어 넣을 수 있다.
		alt키로 점프를 할 수 있으며, 두번 누를 경우 더블점프가 가능하다.
		상하좌우 키로 캐릭터를 움직일 수 있다.
		포탈에서 윗방향키를 누르면 다음 State 로 넘어갈 수 있다.
	- HuntingState
		몬스터가 배치되어 있는 State
		미니맵, 몬스터
		특정 키를 통해 스킬을 사용할 수 있고, 그것으로 몬스터를 공격할 수 있다.
4. 필요한 기술
	- 알파블렌딩
	- 충돌 체크
