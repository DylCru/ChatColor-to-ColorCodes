import pyperclip as pyp

while True:

    codes = {"ChatColor.DARK_RED" : "&4", "ChatColor.RED" : "&c", "ChatColor.GOLD" : "&6", "ChatColor.YELLOW" : "&e", 
    "ChatColor.DARK_GREEN" : "&2", "ChatColor.GREEN" : "&a", "ChatColor.AQUA" : "&b", "ChatColor.DARK_AQUA" : "&3", 
    "ChatColor.DARK_BLUE" : "&1", "ChatColor.BLUE" : "&9", "ChatColor.LIGHT_PURPLE" : "&d", "ChatColor.DARK_PURPLE" : "&5", 
    "ChatColor.WHITE" : "&f", "ChatColor.GRAY" : "&7", "ChatColor.DARK_GRAY" : "&8", "ChatColor.BLACK" : "&0", "ChatColor.MAGIC" : "&k", 
    "ChatColor.BOLD" : "&l", "ChatColor.STRIKETHROUGH": "&m", "ChatColor.UNDERLINE" : "&n", "ChatColor.ITALIC" : "&o", "ChatColor.RESET" : "&r"}

    def convert(string):
        for code in codes:
            string = string.replace(code, codes[code])

        string = string.replace("\"", "")
        string = string.replace("+", "")
        string = " ".join(string.split())

        return string

    string = input("Enter your string ")
    string = convert(string)
    print(f"Your new string: \"{string}\"")
    pyp.copy(f"\"{string}\"")
    print("Copied to clipboard!")

