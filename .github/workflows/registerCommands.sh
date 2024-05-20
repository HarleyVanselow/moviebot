# Discord API endpoint
API_ENDPOINT="https://discord.com/api/v10/applications/1233603538651713666/commands"

# Directory containing JSON files
JSON_DIR="/commands"

# Iterate through each JSON file in the directory
for file in "$JSON_DIR"/*.json; do
    # Check if file exists and is a regular file
    if [ -f "$file" ]; then
        # Read contents of the JSON file
        json_data=$(cat "$file")
        echo "Calling for file $file" >> $GITHUB_OUTPUT
        # Make a POST request to Discord API
        response=$(curl -s -X POST -H "Content-Type: application/json" -H "Authorization: Bot ${{ secrets.DISCORD_BOT_TOKEN }}" -d "$json_data" "$API_ENDPOINT")

        # Check if the request was successful
        if [[ $response == *"success"* ]]; then
            echo "Command from file $file successfully added." >> $GITHUB_OUTPUT
        else
            echo "Failed to add command from file $file. Response: $response" >> $GITHUB_OUTPUT
        fi
    fi
done