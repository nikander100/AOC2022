#!/bin/bash
BASE_FILE="../base.py"
MAIN_FILE="./main.py"

if [[ -z $1 ]]; then
        DAY=$(date +%e | cut -d " " -f 2)
else
        DAY=$1
fi
mkdir -p "$DAY" && cd "$DAY"

wget -N --no-cookies --header="Cookie: $(cat ../cookie.txt)" "https://adventofcode.com/2022/day/${DAY}/input"
cp "$BASE_FILE" "$MAIN_FILE"
sed -i -e "s/%%DAY%%/$DAY/g" "$MAIN_FILE"