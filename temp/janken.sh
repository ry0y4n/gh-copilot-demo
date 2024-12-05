#!/bin/bash

# Function to determine the winner
determine_winner() {
    if [ "$1" == "$2" ]; then
        echo "引き分けです！"
    elif [ "$1" == "グー" ] && [ "$2" == "チョキ" ]; then
        echo "あなたの勝ちです！"
    elif [ "$1" == "チョキ" ] && [ "$2" == "パー" ]; then
        echo "あなたの勝ちです！"
    elif [ "$1" == "パー" ] && [ "$2" == "グー" ]; then
        echo "あなたの勝ちです！"
    else
        echo "コンピューターの勝ちです！"
    fi
}

# User input
echo "グー、チョキ、パーのいずれかを入力してください:"
read user_choice

# Validate user input
if [[ "$user_choice" != "グー" && "$user_choice" != "チョキ" && "$user_choice" != "パー" ]]; then
    echo "無効な入力です。グー、チョキ、パーのいずれかを入力してください。"
    exit 1
fi

# Computer choice
choices=("グー" "チョキ" "パー")
computer_choice=${choices[$RANDOM % 3]}

# Display choices
echo "あなたの選択: $user_choice"
echo "コンピューターの選択: $computer_choice"

# Determine the winner
determine_winner "$user_choice" "$computer_choice"