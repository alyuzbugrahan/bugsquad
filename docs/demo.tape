Output docs/demo.gif

Set FontSize 15
Set Width 1300
Set Height 720
Set Padding 20
Set Theme "Dracula"
Set TypingSpeed 45ms
Set PlaybackSpeed 2
Set Shell "bash"

Hide
Type "source .venv/bin/activate && clear"
Enter
Sleep 1s
Show

Type "cat benchmarks/010_misleading_issue/issue.md"
Enter
Sleep 4s

Type "bugsquad benchmarks/010_misleading_issue"
Enter
Sleep 50s
Sleep 6s