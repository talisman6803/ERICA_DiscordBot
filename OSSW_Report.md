# 오픈소스 커뮤니티 체험 보고서

## discord.py 커뮤니티 선정계기

기존에 아주 간단한 기능 수준의 디스코드 봇을 제작했었고, 당시에는 한국인들의 여러 블로그를 참고하여 누더기를 만들었다.

그와 달리 오픈소스 SW 기초의 프로젝트의 일환으로 진행했던 디스코드 봇 프로젝트는 다양한 비동기식 함수들의 쓰레드 활용과 제작하려는 기능들이 Python의 OOP를 요구했다. 물론 discord.py의 wikidocs의 문서없이는 제작을 진행시킬 수가 없었다. discord.py(이하 '프로젝트')의 Commit과 Feedback이 Gihub에서 여러사람들에의해 진행되었으나, wikidocs의 문서는 해당 레포를 가지고있는 Rapptz만이 수정가능한건지 내용이 매우 불친절했다. 또한 해당 프로젝트가 비교적 최근에 1.x 버전으로 판올림하면서 기본적인 틀이라던가 메소드의 이름들이 바뀌었기때문에, 구글링으로는 현재버전과 관련된 게시글을 찾기가 매우 힘들었다.

이에 StackOverflow보다 빠른 실시간 feedback을 받을수있는 관련 커뮤니티를 찾다가, discord.py를 통해 개발을 진행하는 사람들이 모인 Discord서버를 찾게되었다. 

## 왕초보 개발자의 커뮤니티 첫인상

프로그래밍을 접한지는 오래지만, 개발은 완전 처음이었다. 교내에서 가입해있던 코딩이나 개발 관련 학회를 벗어나 수 백, 수 천이 가입해있는 거대 개발관련 커뮤니티는 당연히 처음이었다. 물론 개중에는 나와 비슷한 수준의 개발자들이 대다수고, 프로젝트를 이끌어나가는 몇몇의 인원들이 상주해있었다. 해당 Discord 서버의 초대코드는 영구적이었지만, 꽁꽁 숨겨져있었기에 찾아오는것이 신기할 정도였다. 그야말로 해당 프로젝트에선 여러의미로 '갈 데까지 간' 사람들이 다 모인곳이었다.

서버의 규칙을 안내하는 Rules채널에선 처음 온 프로젝트의 뉴비들에게 많이 바라지않았다.

1. 도배나 광고하지 않을것

2. NSFW(우리말로는 후방주의쯤?)내용물은 NSFW관련 채널에서만

3. 자유로운 분위기를 존중하나 예의를 지킬것

4. 프로그래밍(여기서는 Python에대한 작성능력)에대한 기본적인 지식과, 구글링 우선을 노력할것

이렇게 크게 4가지만을 원했다. 다른 국내 웹기반 커뮤니티들에비해 실시간으로 운영되면서도 규칙들이 느슨했다.

## 내 개발을 위한 활동들

기존의 디스코드 봇을 제작하면서, OOP를 활용하지않는 메소드만 간략하게 사용했던터였다. 당연히 OOP에 대한 개념도 이해도 없었기에, 안되면 코드가 좀 더 복잡해지더라도 반-객체 성향을 유지하려고 했던거 같았다. 그렇게 노가다식 개발을 이어나가던중 wikidocs의 주소창의 버전을 나타내는 부분이 1.3.0a 임을 알게되었고, 내가 사용하는 버전은 1.2.5였다. 여기서 커뮤니티에 던지는 나의 역사적인 첫 질문이 발생했다.

```I noticed that I worked with wikidocs 1.3.0a. Where can I get documents of 1.2.5?```

그렇게 단 하나의 질문을 마지막으로 내 개발을 위한 질문은 완성할때까진 없었다. 사실 별거없었다. 궁금하면 안내해준 1.2.5버전의 wikidocs를 참고했고, 그래도 모르겠을때에는 ```?rtfm 키워드```형식의 프로젝트 안내 커맨드를 활용했기 때문이다. 아무 쓸모짝에도 없는 구버전의 방대한 정보대신, 현재 버전의 신선한 정보들을 무한정 공급받을 수 있다는 점이 너무 좋았다. 이러한 장점을 알기전엔 구버전 정보들로 개발 의지가 꺾였고, 이러한 장점을 알고나선 든든함에 뭐든지 만들 수 있을것 같았다. 그렇게 나의 오픈소스 SW 프로젝트는 완성되었고, 개발환경인 Ubuntu뿐만아니라 어디서든 구동될수 있도록 Windows나 OS X에서의 호환성을 확보하기위해 차근차근 개인 레포에서 커밋을 이어 나가고 있다.

## 힘닫는대로 커뮤니티에 참여하기

물론 내 개발을 마치고도 서버에는 남았다. 24시간내내 새로운 그리고 서투른 질문들이 #help 채널의 알림이 끊이지 않도록 했다. 그리고 할 수 있는 한 질문들을 받아주고 도와줬다. 개중에는 영어기반 서버임에도 한글로 질문하는 한국인들도, 각자의 언어로 질문하는 여러사람들이 있었다. 1주일간 하루에 30분은 나도 그곳에 상주하면서 질문들을 처리했다. 프로젝트의 Github에서 issue로 자신의 질문을 올려 Question태그와함께 closed되려는 issuer들도 서버로 초대하여 도움을 주었다.

Python문법 질문들부터 프로젝트의 심층 소스구조까지 구글링하면 나오는 여러 질문들에 아는것들은 아는대로 모르면 검색어를 제안하며 새로운 지식들도 얻게되었다. 물론 discord.py 프로젝트에 직접적인 소스코드 기여는 못해봤지만, 프로젝트에 새롭게 접근하는 여러사람들을 도와주는 방식으로나마 기여를 했다고 스스로 위안하며 짧은 오픈소스 커뮤니티 체험 보고서를 마친다.