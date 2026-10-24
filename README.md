# Iron Swarm

A side-on mech game with destructible terrain. Every explosion carves the ground. Your back pod fires a looping micro-missile swarm, and you buy swappable parts and upgrades with scrap between waves.

## Get the APK using only your phone

You need a free GitHub account. Use Chrome on your phone at github.com, not the GitHub app, because the app can't create repos or files.

1. **Create the repo.** Go to github.com/new. Name it `iron-swarm`, set it to Public (this gives you free build minutes), and tick **Add a README file**. Then tap **Create repository**.
2. **Upload the game.** In the repo, tap **Add file → Upload files**, choose `index.html`, and tap **Commit changes**.
3. **Add the build recipe.** Tap **Add file → Create new file**. For the file name, type exactly:
   `.github/workflows/build-apk.yml`
   GitHub turns each `/` into a folder as you type. Paste in the contents of `build-apk.yml`, then tap **Commit changes**.
4. **Wait for the build.** Open the **Actions** tab. A "Build APK" run starts on its own and takes about 4–6 minutes.
5. **Download the APK.** Open the finished run (it shows a green tick). Scroll to **Artifacts**, download `iron-swarm-apk`, and unzip it. The file inside is `app-debug.apk`.
6. **Install it.** Tap the APK. Android will ask you to allow your browser or Files app to install unknown apps. Allow it, then install.

Whenever you change `index.html` and commit, GitHub builds a new APK. You can also start a build by hand: go to **Actions → Build APK → Run workflow**.

## Controls

- **Left thumb:** move. Push the stick up to jump; keep holding to burn your jets.
- **Right thumb:** aim and fire your arm weapon.
- **Pod button:** fire your back weapon (Swarm, Buster or Cluster).
- **Keyboard:** A/D to move, W or Space to jet, mouse to aim, click to fire, E for the back weapon, Esc to pause.

## Parts

| Slot | Options |
|---|---|
| Legs | Strider (balanced) · Bulwark Treads (armor, climbs) · Skimmer Hover (fast, fuel-efficient) |
| Arm | Autocannon · Rail Lance (piercing beam that bores tunnels) · Mortar |
| Back | Swarm Pod (looping homing missiles) · Bunker Buster (drills in, then detonates) · Cluster Rack |
| Core | Standard · Reactor (faster recharge) · Fortress (more armor) |

Upgrades: Armor Plating, Thrusters, Warheads, Ordnance Racks, Fire Control (5 levels each).

A boss called the Warden shows up every fifth wave. Clearing a boss wave sets your checkpoint.
