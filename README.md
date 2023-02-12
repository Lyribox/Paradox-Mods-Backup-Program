# Paradox-Mods-Backup-Program
A python program to create a snapshot of mods downloaded for a Paradox game and format them to be used locally.

# Why?
Paradox Interactive is notorious for breaking available mods every time there is a major update (which is about every quarter). Honestly, can't fault them for that. However, they also allow downgrading their games to previous updates to accommodate for mods that take a while to update to new systems. The wise choice is to backup all mods in their working state. However, using mods without workshop required file creation and editing specific to the user folder configuration. Doing this for all mods is tedious and repetitive. Hence the creation of this program

# Functionality
The program takes the path to the Stellaris workshop folder and copies all mods there to the Documents location of Stellaris mods.
It then iterates over ever folder to perform the following actions:
Finds the descriptor file in the folder and copy it back to the parent folder,
Opens the descriptor file now in parent folder
Finds the name of the mod and creates required paths from that ensuring no damaging character appear
Finds the remote id line and replaces with the paths created prior
Renames the descriptor mod to the mod name found earlier with appropriate alterations for each case
Renames the corresponding mod folder to the mod name found earlier
Then rinse and repeat for every mod folder

# Use
Change variables to corresponding paths of the Documents Stellaris folder and the workshop folder
