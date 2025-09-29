# 1st Assignment

> 이 과제는 브라우저만으로 제출 가능합니다. CLI(터미널) 설정은 선택이며, 앞으로도 원하지 않으면 사용할 필요는 없습니다. 단, 향후 Git / GitHub 을 제대로 활용함에 있어 개인 환경에서 CLI 설정을 하시는 것을 **적극** 추천합니다.

- `members/` 디렉토리에 자기소개를 작성해서 PR로 제출하세요!
    - [https://github.com/HUFS-LAI-Seungtaek/HUFS-LAI-OOP-2025-2](https://github.com/HUFS-LAI-Seungtaek/HUFS-LAI-OOP-2025-2) 접속
    - `Fork` 버튼 클릭하여 `Create Fork` 진행
    - Fork한 repository(예: [https://github.com/hist0613/HUFS-LAI-OOP-2025-2](https://github.com/hist0613/HUFS-LAI-OOP-2025-2))로 이동 확인 후
    - `Add file` > `Create new file` 클릭
    - `members/{본인이름}.md` 파일에 간단한 자기소개 작성 후 (`members/seungtaek.md` 참고) `Commit changes...` 버튼 클릭
        - 자기소개는 마크다운 문법으로 아래 구성과 형식을 지켜 작성하세요.
            - 제목: `# 자기소개`, `# TMI` (각 섹션 1단계 헤딩)
                - 2단계 헤딩 등으로 subsection 을 구성하고 싶다면 `## 프로젝트 내용` 등으로 작성해 볼 수 있음. 
            - `# TMI` 항목은 `-` 를 사용한 bullet items 로 작성
        
        - 예시 템플릿 (아래 구성을 반드시 따를 것):
            ```markdown
            # 자기소개
            한두 문장으로 간단한 소개를 작성합니다.

            # TMI
            - 취미/관심사
            - 기타 알려주고 싶은 점
            ```

        - 자기소개 내용은 [members/seungtaek.md](https://github.com/HUFS-LAI-Seungtaek/HUFS-LAI-OOP-2025-2/tree/main/members/seungtaek.md) 참고
    - 본인 repository 메인 화면에서 `Contribute` > `Open pull request` 버튼 클릭
    - 아래와 같은 포맷으로 작성 후 `Create pull request` 버튼 클릭
        - Title: `1st Assignment by {학번} ({영어 이름})`
            - 예시: `1st Assignment by 2025122 (Seungtaek Choi)`
            - 학번/이름은 제출 식별·관리(제출 체크 및 채점 기록) 자동화에 사용됩니다. 
            - 해당 포맷을 지키지 않아 생기는 문제는 본인 책임입니다. 제출 전/후로 여러번 확인해주세요. 
            - `first Assignment`, `1st assignment`, `1st Assignment by {2025122} ({Seungtaek Choi})` 같은 포맷은 허용되지 않습니다. 
        - Description: 
            ```markdown
            - `members/{학생이름}.md` 파일 제출합니다.
            ```
            - 어떤 파일이 바뀌었는지 명시적으로 작성해줘야 리뷰어가 한결 편하게 코드 리뷰를 진행할 수 있음. 
            - PR 본문도 markdown 문법을 따르기 때문에, 코드나 파일명 같은 경우 `로 감싸주면 더 깔끔하게 표시될 수 있음. (일반적으로 추천, 해당 과제에서는 **의무**)