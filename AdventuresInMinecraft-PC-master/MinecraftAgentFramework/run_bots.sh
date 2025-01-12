#!/bin/bash

# dictionary of bots
declare -A bot_classes=(
    ["builder"]="examples/run_builder_bot.py"
    ["insult"]="examples/run_insult_bot.py"
    ["oracle"]="examples/run_oracle_bot.py"
    ["tnt"]="examples/run_tnt_bot.py"
)

# function to show the menu
function show_menu {
    echo "available bots:"
    echo "  builder - run the builder bot"
    echo "  insult  - run the insult bot"
    echo "  oracle  - run the oracle bot"
    echo "  tnt     - run the tnt bot"
    echo "  exit    - quit the program"
}

# handler for sigint (ctrl+c)
function handle_sigint {
    echo -e "\ninterrupted returning to menu"
}

# set up sigint handler
trap handle_sigint SIGINT

# main loop
while true; do
    # show the menu and prompt for input
    show_menu
    read -p "enter bot type: " bot_type

    # convert input to lowercase to avoid issues
    bot_type=$(echo "$bot_type" | tr '[:upper:]' '[:lower:]')

    # check if the user wants to exit
    if [[ "$bot_type" == "exit" ]]; then
        echo "exiting program goodbye"
        break
    fi

    # check if the bot exists in the dictionary
    if [[ -n "${bot_classes[$bot_type]}" ]]; then
        bot_command="${bot_classes[$bot_type]}"
        echo "running $bot_type bot press ctrl+c to stop"

        # execute the bot and handle sigint during execution
        trap handle_sigint SIGINT
        python "$bot_command"
        trap - SIGINT  # restore default behavior for sigint

        # check the execution result
        if [[ $? -eq 0 ]]; then
            echo "$bot_type bot ran successfully"
        else
            echo "error while running $bot_type bot"
        fi
    else
        echo "unknown bot type please try again"
    fi

    echo # blank line to separate iterations
done

