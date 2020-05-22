print("出力結果:")
try:
  raise Exception("開始前","Exception発生")
  print("開始")
except IOError as msg:
  print("IOError発生:",msg.args[0])
except Exception as msg:
  print("予期せぬ問題発生:",msg.args[1])
else:
  print("Else表示")