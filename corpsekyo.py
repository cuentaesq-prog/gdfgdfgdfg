import pylast
import time
import warnings
import sys
import os

warnings.filterwarnings("ignore")

API_KEY = '49452d64180d104ac22e571cc5d0c0f0'
API_SECRET = '4ff0c076a69291d506c761b7dfecd083'
USERNAME = 'o4h'
PASSWORD_HASH = pylast.md5('Naxo1337_')


network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=USERNAME,
    password_hash=PASSWORD_HASH
)

TARGET = 3000
count = 0

def scrobble_batch(batch, start_number, max_retries=3):
    timestamp = int(time.time())
    scrobbles = []

    for i, track_data in enumerate(batch):
        scrobbles.append({
            "artist": track_data["artist"],
            "title": track_data["track"],
            "album": track_data["album"],
            "timestamp": timestamp + i
        })

    for attempt in range(max_retries):
        try:
            network.scrobble_many(scrobbles)
            for i, t in enumerate(scrobbles):
                print(f"[{start_number + i}] > {t['artist']} - {t['title']} (scrobbled)")
            return len(scrobbles)

        except pylast.WSError as e:
            if "Rate Limit" in str(e):
                print("⚠️ Rate limit, esperando 15 segundos...")
                time.sleep(15)
            else:
                print(f"> error: {e} retry {attempt+1}/{max_retries}")
                time.sleep(10)

        except pylast.NetworkError:
            print("> network error, retrying...")
            time.sleep(5)

    return 0


canciones = [
  { "artist": "corpsekyo", "track": "ela pregunto como eu ando tao chapado", "album": "backhoods mixtape vl.1" },
  { "artist": "corpsekyo", "track": "ela pregunto como eu ando tao chapado", "album": "backhoods mixtape vl.1" },
  { "artist": "corpsekyo", "track": "ela pregunto como eu ando tao chapado", "album": "backhoods mixtape vl.1" },
  { "artist": "corpsekyo", "track": "ela pregunto como eu ando tao chapado", "album": "backhoods mixtape vl.1" },

]

index = 0
BATCH_SIZE = 2

while count < TARGET:
    batch = canciones[index:index + BATCH_SIZE]

    if not batch:
        index = 0
        continue

    added = scrobble_batch(batch, count + 1)
    count += added

    if count >= TARGET:
        print("🎯 Llegué a 3000 scrobbles, cerrando")
        sys.exit(0)

    index += BATCH_SIZE
    time.sleep(2.5)

print("✅ Finalizado correctamente")
sys.exit(0)
