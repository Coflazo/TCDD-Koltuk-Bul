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
**中文** ·
[日本語](README.ja.md) ·
[한국어](README.ko.md)

---

**在售罄的土耳其火车上抢下退票席位，并立刻替你锁住。**

它会不断刷新你选定的车次。一旦有人退票，它就选中座位，触发 TCDD 自带的临时占座，然后一直响铃，
直到你回到电脑前。

覆盖整个铁路网，而不是某一条线路：460 个车站，双向，YHT、Anahat 和 Bölgesel 均可。有哪些
车厢等级，它直接从该趟车读取，代码里没有写死任何线路、车次或等级。

## 安装

不需要懂编程，一行命令即可。

**macOS / Linux:**
```bash
curl -fsSL https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.ps1 | iex
```

安装位置：在桌面运行就在桌面建一个文件夹；已经在桌面下的某个文件夹里，就装在原地；在其他任何
位置运行，都会回到桌面再建文件夹。装完会留下一个双击即可运行的文件：**Başlat.command**
（macOS、Linux）或 **Baslat.bat**（Windows）。

## 使用方法

1. 输入出发站和到达站。不必输入土耳其文字符，拼错也没关系：`sogutlucesme` 能找到
   SÖĞÜTLÜÇEŞME，输入 `ankra` 会提示 ANKARA。
2. 选择日期，也可以选多天。时间灵活的话输入 `17 18 21`，三天一起盯。
3. 它会列出这些日期的全部车次，包含各等级的票价和余票数。
4. 勾选你真正愿意乘坐的车次和等级。
5. 剩下的交给它。抢到座位后会锁座并叫醒你，付款由你自己完成。

## 注意事项

- 仅供个人使用。一名乘客，一个座位，不得转售。
- 绝不自动付款。不会读取、保存或填写你的银行卡信息。
- 轮椅席位默认不监控，只有你明确选择时才会。那些席位是留给无法使用其他座位的乘客的。
- 你的数据只保存在你自己的电脑上。
- 遵守 TCDD 的使用条款是你自己的责任。

完整文档：[README](../../README.md) &nbsp;·&nbsp; [DISCLAIMER](../../DISCLAIMER.md)
