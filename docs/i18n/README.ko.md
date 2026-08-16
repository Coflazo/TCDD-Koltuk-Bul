# TCDD Koltuk Bul

[English](../../README.md) ·
[Türkçe](README.tr.md) ·
[Deutsch](README.de.md) ·
[Русский](README.ru.md) ·
[العربية](README.ar.md) ·
[فارسی](README.fa.md) ·
[Français](README.fr.md) ·
[Español](README.es.md) ·
[Nederlands](README.nl.md) ·
[Български](README.bg.md)

[Українська](README.uk.md) ·
[Polski](README.pl.md) ·
[Română](README.ro.md) ·
[Ελληνικά](README.el.md) ·
[Italiano](README.it.md) ·
[Azərbaycanca](README.az.md) ·
[ქართული](README.ka.md) ·
[中文](README.zh.md) ·
[日本語](README.ja.md) ·
**한국어**

---

**매진된 튀르키예 기차에서 취소석이 나오는 순간 잡아서 대신 잡아두는 봇입니다.**

지정한 열차를 계속 확인합니다. 누군가 취소하면 좌석을 선택하고 TCDD의 임시 예약을 시작한 뒤,
컴퓨터 앞으로 올 때까지 알람을 울립니다.

한 노선이 아니라 전체 노선에서 동작합니다. 460개 역, 양방향, YHT와 Anahat, Bölgesel 모두.
어떤 좌석 등급이 있는지는 해당 열차에서 직접 읽어오므로 노선도 열차도 등급도 코드에 박혀
있지 않습니다.

## 설치

프로그래밍을 몰라도 됩니다. 한 줄이면 충분합니다.

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.ps1 | iex
```

설치 위치는 이렇게 정해집니다. 바탕화면에서 실행하면 거기에 폴더를 만들고, 이미 바탕화면 안의
폴더에 있다면 그 자리에 설치하며, 그 밖의 위치에서는 바탕화면으로 이동합니다. 끝나면 더블클릭해서
실행할 파일이 남습니다. macOS와 리눅스는 **Başlat.command**, 윈도우는 **Baslat.bat** 입니다.

## 사용법

1. 출발역과 도착역을 입력합니다. 튀르키예어 문자는 필요 없고 오타도 괜찮습니다.
   `sogutlucesme` 로도 SÖĞÜTLÜÇEŞME 를 찾고, `ankra` 를 치면 ANKARA 를 제안합니다.
2. 날짜를 입력합니다. 여러 날도 됩니다. 일정이 유연하다면 `17 18 21` 이라고 치면 세 날짜를
   모두 지켜봅니다.
3. 해당 날짜의 모든 열차를 등급별 가격과 잔여 좌석 수와 함께 보여줍니다.
4. 실제로 탈 의향이 있는 열차와 등급을 고릅니다.
5. 나머지는 알아서 합니다. 좌석을 잡고 깨워 줍니다. 결제는 직접 하셔야 합니다.

## 중요

- 개인용으로만 쓰세요. 승객 한 명, 좌석 하나. 재판매용이 아닙니다.
- 결제는 절대 자동화하지 않습니다. 카드 정보를 읽거나 저장하거나 입력하지 않습니다.
- 휠체어석은 기본적으로 감시하지 않으며, 직접 선택한 경우에만 봅니다. 다른 좌석을 이용할 수
  없는 승객을 위한 자리이기 때문입니다.
- 데이터는 본인 컴퓨터에만 남습니다.
- TCDD 이용약관을 지키는 것은 사용자 본인의 책임입니다.

전체 문서: [README](../../README.md) &nbsp;·&nbsp; [DISCLAIMER](../../DISCLAIMER.md)
