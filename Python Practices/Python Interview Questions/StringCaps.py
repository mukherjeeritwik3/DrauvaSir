a = "The series's eponymous first title was released in 2007, and it has featured eleven main games in total, the most recent being 2020's Valhalla. Main games of Assassin's Creed are set in an open world and presented from the third-person perspective where the protagonists take down targets using their combat and stealth skills with the exploitation of the environment. Players have freedom to explore the historical settings as they finish main and side quests. Apart from single-player missions, some games also provide competitive and cooperative multiplayer gameplay. A new story and occasional new time period are introduced in each entry, and gameplay elements evolve from the previous one. There are three-story arcs in the series. For the first five main games, the framing story is set in 2012 and features series protagonist Desmond Miles who uses a machine called the Animus and relives the memories of his ancestors. In games up until and including Assassin's Creed Syndicate, Abstergo employees and Assassin initiates recorded genetic memories using the Helix software, helping the Templars and Assassins find new Pieces of Eden in the modern world. The latest three games, Assassin's Creed Origins, Assassin's Creed Odyssey, and Assassin's Creed Valhalla, follow ex-Abstergo employee Layla Hassan. "
print(hash(a))

b = input()

for i in range(len(a)):
    if (a[i]!=b[i]):
        print(False)
        break
