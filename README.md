# Get roles reminder
A simple discord bot that reminds new members to get reaction roles from a designated channel.

# Usage
Install the packages, preferrably using pipx:
```sh
pipx install git+https://github.com/shenafield/get-roles-reminder
```

Create a `.env` file defining these variables or set them as envvars: `DISCORD_TOKEN`, `REMINDER_MESSAGE`, (optional) `ALLOWED_CHANNELS` (a json list of integer IDs)

Run the bot:
```sh
reaction_roles_reminder
```
