# .latexmkrc

$latex = 'lualatex';
$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';

$pdf_mode = 4; # LuaLaTeX で PDF を作る

$bibtex_use = 2;

## 中間ファイル掃除
#$clean_ext = 'aux bbl bcf blg fdb_latexmk fls lof log lot out run.xml synctex.gz toc';

# PDF ビューアは環境に応じて変更
$pdf_previewer = 'start';
