#!/usr/bin/env bash
# TCDD Koltuk Bul installer for macOS and Linux.
#
# Run it from anywhere:
#   curl -fsSL https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.sh | bash
#
# Where it puts things, which is the bit people always ask about:
#   already inside a folder under the Desktop  ->  installs right here
#   sitting on the Desktop itself              ->  makes a folder here
#   anywhere else (home, /, a random path)     ->  goes to the Desktop and makes it there
set -euo pipefail

NAME="TCDD-Koltuk-Bul"
REPO="https://github.com/Coflazo/TCDD-Koltuk-Bul.git"
ZIP="https://github.com/Coflazo/TCDD-Koltuk-Bul/archive/refs/heads/main.zip"

say()  { printf "  %s\n" "$*"; }
step() { printf "\n  \033[1m%s\033[0m\n" "$*"; }
die()  { printf "\n  %s\n\n" "$*" >&2; exit 1; }

# ---------------------------------------------------------------- where to install

find_desktop() {
  # Localised Desktop folders exist (Masaüstü, Schreibtisch...), so ask the OS first.
  if command -v xdg-user-dir >/dev/null 2>&1; then
    d=$(xdg-user-dir DESKTOP 2>/dev/null || true)
    [ -n "${d:-}" ] && [ -d "$d" ] && { printf "%s" "$d"; return; }
  fi
  for d in "$HOME/Desktop" "$HOME/Masaüstü" "$HOME/Escritorio" "$HOME/Bureau" "$HOME/Schreibtisch"; do
    [ -d "$d" ] && { printf "%s" "$d"; return; }
  done
  printf "%s" "$HOME"      # no Desktop at all, e.g. a server. Home will do.
}

# Both sides must be resolved the same way, or a symlinked path makes "am I under the
# Desktop?" answer no when it should answer yes.
resolve() { (cd "$1" 2>/dev/null && pwd -P) || printf "%s" "$1"; }
DESKTOP="$(resolve "$(find_desktop)")"
HERE="$(pwd -P)"

if [ "$HERE" = "$DESKTOP" ]; then
  TARGET="$DESKTOP/$NAME"                       # on the Desktop: make a folder
elif case "$HERE" in "$DESKTOP"/*) true;; *) false;; esac; then
  TARGET="$HERE"                                # already somewhere under the Desktop: stay
else
  TARGET="$DESKTOP/$NAME"                       # anywhere else: go to the Desktop
fi

printf "\n  \033[1mTCDD Koltuk Bul\033[0m\n"
say "installing into: $TARGET"

# ---------------------------------------------------------------- python

step "1/4  checking python"
PY=""
for c in python3 python; do
  if command -v "$c" >/dev/null 2>&1 && "$c" -c 'import sys; sys.exit(0 if sys.version_info>=(3,8) else 1)' 2>/dev/null; then
    PY="$c"; break
  fi
done
[ -n "$PY" ] || die "Python 3.8+ not found. Install it from https://www.python.org/downloads/ and run this again."
say "found $($PY --version 2>&1)"

# ---------------------------------------------------------------- get the code

step "2/4  downloading"
mkdir -p "$TARGET"
if [ -f "$TARGET/koltukbul.py" ]; then
  say "already here, updating"
  if [ -d "$TARGET/.git" ]; then (cd "$TARGET" && git pull --quiet || true); fi
elif command -v git >/dev/null 2>&1; then
  if [ -z "$(ls -A "$TARGET" 2>/dev/null)" ]; then
    git clone --quiet --depth 1 "$REPO" "$TARGET"
  else
    git clone --quiet --depth 1 "$REPO" "$TARGET/$NAME" && TARGET="$TARGET/$NAME"
  fi
else
  # No git. Fall back to the zip, which every machine can do.
  tmp="$(mktemp -d)"
  curl -fsSL "$ZIP" -o "$tmp/main.zip" || die "download failed. Check your internet connection."
  (cd "$tmp" && unzip -q main.zip)
  cp -R "$tmp/$NAME-main/." "$TARGET/"
  rm -rf "$tmp"
fi
say "code is in $TARGET"

# ---------------------------------------------------------------- dependencies

step "3/4  installing the browser it drives (this is the slow part, ~1 minute)"
cd "$TARGET"
"$PY" -m venv .venv 2>/dev/null || die "could not create a virtual environment. On Debian/Ubuntu: sudo apt install python3-venv"
# shellcheck disable=SC1091
. .venv/bin/activate
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt
python -m patchright install chromium 2>/dev/null || python -m playwright install chromium

# ---------------------------------------------------------------- launcher

step "4/4  making it double-clickable"
cat > "Başlat.command" <<LAUNCH
#!/usr/bin/env bash
# Double-click this to run TCDD Koltuk Bul.
cd "\$(dirname "\$0")"
. .venv/bin/activate
python koltukbul.py
echo
read -n 1 -s -r -p "Press any key to close..."
LAUNCH
chmod +x "Başlat.command"

printf "\n  \033[1mDone.\033[0m\n\n"
say "To start it, double-click:  $TARGET/Başlat.command"
say "Or from a terminal:         cd \"$TARGET\" && .venv/bin/python koltukbul.py"
printf "\n"
