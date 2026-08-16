# Recorded with vhs (https://github.com/charmbracelet/vhs):  vhs docs/demo.tape
# Uses --replay so it runs off saved pages: fast, repeatable, and it never touches TCDD.
Output docs/demo.gif
Set FontSize 15
Set Width 1180
Set Height 720
Set Padding 22
Set Theme "Builtin Dark"
Set TypingSpeed 42ms

Type "python3 koltukbul.py --replay"   Sleep 600ms   Enter
Sleep 5s
Type "clear"  Enter  Sleep 300ms
Type "python3 koltukbul.py --test"     Sleep 600ms   Enter
Sleep 4s
