papersize(5)
==================

名称
--------

**papersize** - 使用する用紙サイズの指定

書式
--------

**/etc/papersize**

説明
-----------

**papersize** ファイルはドキュメントを生成するコマンドやプログラムで使用したい用紙サイズを指定するのに使用します。

ファイルのフォーマットは非常にシンプルです: 空白と '#' で始まる行は無視され、一番最初に認識された文字列が用紙の名前になります。用紙の名前が読み込まれない場合については下の注意事項セクションを見てください。

用紙名
-------

一般的にプログラムは次の名前を認識します: **a3, a4, a5, b5, letter, legal, executive, note, 11x17**。

さらに次の用紙名が使われることもあります: **a0, a1, a2, a6, a7, a8 , a9, a10, b0, b1 , b2, b3, b4, tabloid, statement, note, halfletter, halfexecutive, folio, quarto, ledger, archA, archB, archC, archD, archE, flsa, flse, csheet, dsheet, esheet, 10x14**。

**papersize** ファイルの値は :envvar:`PAPERSIZE` 環境変数の値や :envvar:`PAPERCONF` 環境変数でファイルを指定して上書きすることができます。**papersize** ファイルが存在しない場合、用紙ライブラリを使用するプログラムはフォールバック値としてデフォルトで **letter** を使用します。

注意事項
----------

このマニュアルページでは **libpaper** ライブラリによって読み込まれる **papersize** ファイルのフォーマットについて説明しています。このファイルを読み込むプログラムの中にはライブラリを使用しないプログラムが存在し、ファイルの中に空白やコメントが含まれていると問題が発生することがあります。また、そのようなプログラムでは用紙サイズを大文字で指定しないと認識されない場合があります。

著者
------

Yves Arrouye <arrouye@debian.org>


関連項目
--------

:doc:`paperconf.1`,
:doc:`paperconfig.8`
