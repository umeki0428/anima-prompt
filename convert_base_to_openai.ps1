param(
    [string]$Source = 'C:\Users\apric\Downloads\base.json',
    [string]$Destination = (Join-Path $PSScriptRoot 'workflows\base-openai-clean.json')
)

$workflow = Get-Content -LiteralPath $Source -Raw -Encoding UTF8 | ConvertFrom-Json
$llmNode = $workflow.nodes | Where-Object { $_.id -eq 97 }

if ($null -eq $llmNode -or $llmNode.type -ne 'ClaudeCustomPrompt') {
    throw 'ClaudeCustomPrompt node (id 97) was not found in the source workflow.'
}

$systemPrompt = [string]$llmNode.widgets_values[1]
$japaneseInput = [string]$llmNode.widgets_values[2]
if ([string]::IsNullOrWhiteSpace($japaneseInput)) {
    $japaneseInput = 'ここに生成したい画像を日本語で入力してください。'
}

$llmNode.type = 'VRGDG_LLM_Multi'
$llmNode.title = '日本語→Animaプロンプト (OpenAI / gpt-5-nano)'
$llmNode.pos = @(850, 630)
$llmNode.size = @(520, 400)
$llmNode.inputs = @(
    [pscustomobject]@{ name = 'api_key'; type = 'STRING'; widget = [pscustomobject]@{ name = 'api_key' }; link = $null },
    [pscustomobject]@{ name = 'provider'; type = 'COMBO'; widget = [pscustomobject]@{ name = 'provider' }; link = $null },
    [pscustomobject]@{ name = 'model'; type = 'COMBO'; widget = [pscustomobject]@{ name = 'model' }; link = $null },
    [pscustomobject]@{ name = 'prompt'; type = 'STRING'; widget = [pscustomobject]@{ name = 'prompt' }; link = 180 },
    [pscustomobject]@{ name = 'custom_model'; type = 'STRING'; widget = [pscustomobject]@{ name = 'custom_model' }; link = $null },
    [pscustomobject]@{ name = 'image1'; shape = 7; type = 'IMAGE'; link = $null },
    [pscustomobject]@{ name = 'image2'; shape = 7; type = 'IMAGE'; link = $null },
    [pscustomobject]@{ name = 'image3'; shape = 7; type = 'IMAGE'; link = $null },
    [pscustomobject]@{ name = 'image4'; shape = 7; type = 'IMAGE'; link = $null }
)
$llmNode.outputs = @(
    [pscustomobject]@{ name = 'text'; type = 'STRING'; links = @(152, 156); slot_index = 0 },
    [pscustomobject]@{ name = 'used_provider'; type = 'STRING'; links = $null; slot_index = 1 },
    [pscustomobject]@{ name = 'used_model'; type = 'STRING'; links = $null; slot_index = 2 },
    [pscustomobject]@{ name = 'status'; type = 'STRING'; links = @(155); slot_index = 3 },
    [pscustomobject]@{ name = 'image'; type = 'IMAGE'; links = $null; slot_index = 4 }
)
$llmNode.widgets_values = @('', 'openai', 'gpt-5-nano', '', '')
$llmNode.properties = [pscustomobject]@{
    cnr_id = 'comfyui-vrgamedevgirl'
    ver = '1.0.0'
    'Node name for S&R' = 'VRGDG_LLM_Multi'
}

$statusNode = $workflow.nodes | Where-Object { $_.id -eq 99 }
if ($null -ne $statusNode) {
    $statusNode.title = 'OpenAI APIステータス'
}

$statusLink = $workflow.links | Where-Object { $_[0] -eq 155 }
if ($null -eq $statusLink) {
    throw 'Expected status preview link (id 155) was not found.'
}
$statusLink[2] = 3

$ruleNode = [pscustomobject]@{
    id = 109
    type = 'DF_DynamicPrompts_Text_Box'
    pos = @(0, 875)
    size = @(420, 300)
    flags = [pscustomobject]@{ collapsed = $true }
    order = 13
    mode = 0
    inputs = @()
    outputs = @([pscustomobject]@{ name = 'STRING'; type = 'STRING'; links = @(178) })
    title = '変換ルール（通常は変更不要）'
    properties = [pscustomobject]@{ 'Node name for S&R' = 'DF_DynamicPrompts_Text_Box' }
    widgets_values = @($systemPrompt)
}

$inputNode = [pscustomobject]@{
    id = 110
    type = 'DF_DynamicPrompts_Text_Box'
    pos = @(0, 630)
    size = @(420, 210)
    flags = [pscustomobject]@{}
    order = 14
    mode = 0
    inputs = @()
    outputs = @([pscustomobject]@{ name = 'STRING'; type = 'STRING'; links = @(179) })
    title = '日本語入力（ここだけ書き換える）'
    properties = [pscustomobject]@{ 'Node name for S&R' = 'DF_DynamicPrompts_Text_Box' }
    widgets_values = @($japaneseInput)
}

$promptJoinNode = [pscustomobject]@{
    id = 111
    type = 'Text Concatenate'
    pos = @(470, 650)
    size = @(330, 170)
    flags = [pscustomobject]@{}
    order = 15
    mode = 0
    inputs = @(
        [pscustomobject]@{ name = 'text_a'; shape = 7; type = 'STRING'; link = 178 },
        [pscustomobject]@{ name = 'text_b'; shape = 7; type = 'STRING'; link = 179 },
        [pscustomobject]@{ name = 'text_c'; shape = 7; type = 'STRING'; link = $null },
        [pscustomobject]@{ name = 'text_d'; shape = 7; type = 'STRING'; link = $null }
    )
    outputs = @([pscustomobject]@{ name = 'STRING'; type = 'STRING'; links = @(180) })
    title = '変換ルール＋日本語入力'
    properties = [pscustomobject]@{ 'Node name for S&R' = 'Text Concatenate' }
    widgets_values = @("`n`n--- 日本語入力 ---`n", 'false')
}

$workflow.nodes = @($workflow.nodes) + @($ruleNode, $inputNode, $promptJoinNode)
$workflow.links = @($workflow.links) + @(
    @(178, 109, 0, 111, 0, 'STRING'),
    @(179, 110, 0, 111, 1, 'STRING'),
    @(180, 111, 0, 97, 3, 'STRING')
)
$workflow.last_node_id = 111
$workflow.last_link_id = 180

$positions = @{
    44 = @(0, 20); 45 = @(0, 150); 15 = @(0, 300)
    51 = @(360, 20); 52 = @(700, 20); 53 = @(1040, 20)
    109 = @(0, 875); 110 = @(0, 630); 111 = @(470, 650); 97 = @(850, 630)
    98 = @(1420, 630); 99 = @(1420, 870); 49 = @(1780, 930); 50 = @(1810, 680)
    11 = @(2190, 620); 12 = @(2190, 930); 19 = @(2590, 400)
    8 = @(2960, 520); 46 = @(3260, 390)
    28 = @(0, 1450); 106 = @(340, 1450); 101 = @(680, 1450)
    105 = @(0, 1610); 94 = @(340, 1610); 104 = @(680, 1610)
    95 = @(0, 1770); 79 = @(340, 1770); 84 = @(680, 1770)
}
foreach ($node in $workflow.nodes) {
    if ($positions.ContainsKey([int]$node.id)) {
        $node.pos = $positions[[int]$node.id]
    }
}

($workflow.nodes | Where-Object { $_.id -eq 49 }).size = @(340, 250)

$resolutionIds = @(28, 106, 101, 105, 94, 104, 95, 79, 84)
foreach ($id in $resolutionIds) {
    $node = $workflow.nodes | Where-Object { $_.id -eq $id }
    $suffix = if ($id -eq 101) { '（使用中）' } else { '（プリセット）' }
    $title = "$($node.widgets_values[0])×$($node.widgets_values[1]) $suffix"
    if ($node.psobject.Properties.Name -contains 'title') {
        $node.title = $title
    } else {
        $node | Add-Member -NotePropertyName title -NotePropertyValue $title
    }
}

$workflow.groups = @(
    [pscustomobject]@{ id = 1; title = 'STEP 1 — モデルとLoRA'; bounding = @(-40, -40, 1400, 430); color = '#3f789e'; font_size = 24; flags = [pscustomobject]@{} },
    [pscustomobject]@{ id = 2; title = 'STEP 2 — 日本語からプロンプト生成'; bounding = @(-40, 560, 2190, 760); color = '#8b5e9e'; font_size = 24; flags = [pscustomobject]@{} },
    [pscustomobject]@{ id = 3; title = 'STEP 3 — エンコード・生成・保存'; bounding = @(2150, 340, 1620, 900); color = '#5b8c5a'; font_size = 24; flags = [pscustomobject]@{} },
    [pscustomobject]@{ id = 4; title = '画像サイズプリセット（使用する1つだけ接続）'; bounding = @(-40, 1380, 1080, 580); color = '#9a7b4f'; font_size = 24; flags = [pscustomobject]@{} }
)

$json = $workflow | ConvertTo-Json -Depth 100
Set-Content -LiteralPath $Destination -Value $json -Encoding UTF8

Write-Output $Destination
