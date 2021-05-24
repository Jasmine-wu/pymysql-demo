for i in `adb devices | grep 'device$' | awk '{print $1}'`
do
  echo $i
  udid=$i pytest -vs test_search.py &
done