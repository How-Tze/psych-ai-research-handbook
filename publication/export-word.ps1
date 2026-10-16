param([Parameter(Mandatory=$true)][string]$DocumentPath,[Parameter(Mandatory=$true)][string]$PdfPath)
$ErrorActionPreference = 'Stop'
$inputDocument = (Resolve-Path -LiteralPath $DocumentPath).Path
$outputPdf = [IO.Path]::GetFullPath($PdfPath)
$word = $null
$document = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $word.AutomationSecurity = 3
    $document = $word.Documents.Open($inputDocument, $false, $false, $false)
    $document.Repaginate()
    foreach ($toc in $document.TablesOfContents) { $toc.Update() }
    $null = $document.Fields.Update()
    $document.Repaginate()
    foreach ($toc in $document.TablesOfContents) { $toc.UpdatePageNumbers() }
    $document.Save()
    # PDF bookmarks follow Word headings; document structure tags are included.
    $document.ExportAsFixedFormat($outputPdf, 17, $false, 0, 0, 1, 1, 0, $true, $true, 1, $true, $true, $false)
    Write-Output ('Exported PDF; pages=' + $document.ComputeStatistics(2))
} finally {
    if ($null -ne $document) { $document.Close(0); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($document) }
    if ($null -ne $word) { $word.Quit(); [void][Runtime.InteropServices.Marshal]::ReleaseComObject($word) }
}
