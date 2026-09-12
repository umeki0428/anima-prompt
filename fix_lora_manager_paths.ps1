$ErrorActionPreference = 'Stop'

$settingsPath = 'C:\Users\apric\AppData\Local\ComfyUI-LoRA-Manager\settings.json'
$invalidPath = 'C:/AI/ComfyUI_windows_portable/ComfyUI/output/diffusion_models'

if (-not (Test-Path -LiteralPath $settingsPath)) {
    throw "LoRA Manager settings were not found: $settingsPath"
}

$settings = Get-Content -LiteralPath $settingsPath -Raw -Encoding UTF8 | ConvertFrom-Json
$beforeTop = @($settings.folder_paths.unet)
$beforeLibrary = @($settings.libraries.comfyui.folder_paths.unet)

$settings.folder_paths.unet = @($beforeTop | Where-Object { $_ -ne $invalidPath })
$settings.libraries.comfyui.folder_paths.unet = @($beforeLibrary | Where-Object { $_ -ne $invalidPath })

$removed = ($beforeTop.Count - $settings.folder_paths.unet.Count) +
           ($beforeLibrary.Count - $settings.libraries.comfyui.folder_paths.unet.Count)

if ($removed -ne 2) {
    throw "Expected to remove 2 path entries, but found $removed. No changes were written."
}

$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$backupPath = "$settingsPath.backup-$stamp"
Copy-Item -LiteralPath $settingsPath -Destination $backupPath

$temporaryPath = "$settingsPath.tmp"
$settings | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $temporaryPath -Encoding UTF8
Move-Item -LiteralPath $temporaryPath -Destination $settingsPath -Force

$verified = Get-Content -LiteralPath $settingsPath -Raw -Encoding UTF8 | ConvertFrom-Json
$remaining = @($verified.folder_paths.unet) + @($verified.libraries.comfyui.folder_paths.unet)
if ($remaining -contains $invalidPath) {
    throw 'The invalid model path is still present after writing the settings.'
}

[pscustomobject]@{
    Settings = $settingsPath
    Backup = $backupPath
    RemovedEntries = $removed
    RemainingUNETPaths = @($verified.folder_paths.unet)
}
