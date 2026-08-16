# TCDD Koltuk Bul installer for Windows.
#
# Run it from anywhere in PowerShell:
#   irm https://raw.githubusercontent.com/Coflazo/TCDD-Koltuk-Bul/main/install.ps1 | iex
#
# Where it puts things:
#   already inside a folder under the Desktop  ->  installs right here
#   sitting on the Desktop itself              ->  makes a folder here
#   anywhere else (home, C:\, a random path)   ->  goes to the Desktop and makes it there

$ErrorActionPreference = "Stop"
$Name = "TCDD-Koltuk-Bul"
$Zip  = "https://github.com/Coflazo/TCDD-Koltuk-Bul/archive/refs/heads/main.zip"

function Say  ($m) { Write-Host "  $m" }
function Step ($m) { Write-Host "";  Write-Host "  $m" -ForegroundColor White }
function Die  ($m) { Write-Host ""; Write-Host "  $m" -ForegroundColor Red; exit 1 }

# ---------------------------------------------------------------- where to install
# GetFolderPath handles OneDrive redirected Desktops and localised names by itself.
$Desktop = [Environment]::GetFolderPath("Desktop")
$Here    = (Get-Location).Path

if ($Here -eq $Desktop) {
  $Target = Join-Path $Desktop $Name
} elseif ($Here.StartsWith($Desktop + [IO.Path]::DirectorySeparatorChar)) {
  $Target = $Here
} else {
  $Target = Join-Path $Desktop $Name
}

Write-Host ""
Write-Host "  TCDD Koltuk Bul" -ForegroundColor White
Say "installing into: $Target"

# ---------------------------------------------------------------- python
Step "1/4  checking python"
$Py = $null
foreach ($c in @("py", "python3", "python")) {
  if (Get-Command $c -ErrorAction SilentlyContinue) {
    try {
      & $c -c "import sys; sys.exit(0 if sys.version_info>=(3,8) else 1)" 2>$null
      if ($LASTEXITCODE -eq 0) { $Py = $c; break }
    } catch { }
  }
}
if (-not $Py) {
  Die "Python 3.8+ not found. Install it from https://www.python.org/downloads/ (tick 'Add python.exe to PATH') and run this again."
}
Say "found $(& $Py --version 2>&1)"

# ---------------------------------------------------------------- get the code
Step "2/4  downloading"
New-Item -ItemType Directory -Force -Path $Target | Out-Null
if (Test-Path (Join-Path $Target "koltukbul.py")) {
  Say "already here, updating"
  if (Test-Path (Join-Path $Target ".git")) { Push-Location $Target; git pull --quiet; Pop-Location }
} else {
  $tmp = Join-Path $env:TEMP ("tkb-" + [Guid]::NewGuid().ToString("N"))
  New-Item -ItemType Directory -Force -Path $tmp | Out-Null
  try {
    Invoke-WebRequest -Uri $Zip -OutFile (Join-Path $tmp "main.zip") -UseBasicParsing
  } catch {
    Die "download failed. Check your internet connection."
  }
  Expand-Archive -Path (Join-Path $tmp "main.zip") -DestinationPath $tmp -Force
  Copy-Item -Path (Join-Path $tmp "$Name-main\*") -Destination $Target -Recurse -Force
  Remove-Item -Recurse -Force $tmp
}
Say "code is in $Target"

# ---------------------------------------------------------------- dependencies
Step "3/4  installing the browser it drives (this is the slow part, about a minute)"
Set-Location $Target
& $Py -m venv .venv
$VenvPy = Join-Path $Target ".venv\Scripts\python.exe"
& $VenvPy -m pip install --quiet --upgrade pip
& $VenvPy -m pip install --quiet -r requirements.txt
& $VenvPy -m patchright install chromium
if ($LASTEXITCODE -ne 0) { & $VenvPy -m playwright install chromium }

# ---------------------------------------------------------------- launcher
Step "4/4  making it double-clickable"
$bat = @"
@echo off
rem Double-click this to run TCDD Koltuk Bul.
cd /d "%~dp0"
".venv\Scripts\python.exe" koltukbul.py
echo.
pause
"@
Set-Content -Path (Join-Path $Target "Baslat.bat") -Value $bat -Encoding ASCII

Write-Host ""
Write-Host "  Done." -ForegroundColor Green
Write-Host ""
Say "To start it, double-click:  $Target\Baslat.bat"
Say "Or from PowerShell:         cd `"$Target`"; .\.venv\Scripts\python.exe koltukbul.py"
Write-Host ""
