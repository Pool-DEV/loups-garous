# 🐺 **Loups-garou de Thiercelieux**

An adaptation of the famous party game "Les Loups-garous de Thiercelieux" as a multiplayer networked game.

## ✨ **Features**
- **Multiplayer gameplay** over a network.
- **Roles** include Simple villager, werewolf, seer, witch, hunter, thief, little girl, cupid, sheriff and more to come.
- **Day and night cycles** with voting and special abilities.
- **Modular role system**: easily add new roles to the game.

## ⚙️ **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/Pool-DEV/loups-garou.git
   ```
2. Navigate to the project directory:

   ```bash
   cd loups-garou
   ```
3. Run the game server:

   ```bash
   python3 network/server.py
   ```
4. Run the game client:

   ```bash
   python3 network/client.py
   ```

## 🎲 **How to play**

1. Players connect to the server using their client.
   
2. Roles are assigned randomly at the start of the game.

3. During the night, players with special abilities (e.g., werewolves, seer) perform their actions.
   
4. During the day, players discuss and vote to eliminate a suspect.

5. The game continues until either the Werewolves or Villagers win.

# 🛠️ **Adding new roles**

To add a new role:
1. Create a new file in the ``roles/`` directory.

2. Define the role by inheriting from ``baseRole``.

3. Update ``roles/__init__.py`` to include the new role.

4. Add the role to the ``ROLES`` list in ``config.py``.

# 🚀 **Future Plans**
* Implement a web-based interface for better accessibility.
* Add more roles and custom game modes.

# 📜 **License**
This project is licensed under the MIT License. See ``LICENSE`` for details.