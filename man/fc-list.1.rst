fc-list(1)
==================

名称
--------

fc-list - 利用可能なフォントを表示

書式
--------

**fc-list** [ **-vVh** ] [ **--verbose** ] [ **-f** *format* | **--format** *format* ] [ **-q** | **--quiet** ] [ **--version** ] [ **--help** ] [ *pattern* **[** *element* ... **]** ]

説明
-----------

**fc-list** は fontconfig を使用するアプリケーションで利用可能なシステム内のフォントとスタイルを一覧で表示します。*element* を指定した場合、指定されたプロパティだけが表示されます。指定しなかった場合はフォントファミリーとスタイルが表示されます。*verbose* 出力を要求した場合は全てのプロパティが表示されます。

オプション
----------

このプログラムは一般的な GNU のコマンドライン構文に従っており、長いオプションはダッシュ ('-') を2つ前に付けます。以下のオプションが使用できます:

.. option:: -v --verbose

   指定された場合、マッチする全てのフォントパターンについて詳細な出力を表示します。

.. option:: -f --format format

   *format* に従って出力を整形します。

.. option:: -q --quiet

   全ての通常出力を消します。フォントがマッチしなかった場合はエラーコードとして 1 を返します。

.. option:: -V --version

   プログラムのバージョンを表示して終了します。

.. option:: -h --help

   オプションの概要を表示します。

*pattern*

   この引数を指定した場合、*pattern* にマッチするフォントだけが表示されます。

*element*

   指定した場合、マッチするフォントの *element* プロパティが表示されます。

例
----------

**fc-lict**

   全てのフォントフェイスを表示。

**fc-list :lang=hi**

   ヒンディー語をカバーするフォントフェイスを表示

**fc-list : family style file spacing**

   各フォントフェイルのファイル名・間隔を表示。'':'' は全てのフォントにマッチする空のパターンです。

関連項目
--------

:doc:`fc-match.1`,
:doc:`FcFontList.3`,
:doc:`FcPatternFormat.3`,
:doc:`fc-cat.1`,
:doc:`fc-cache.1`,
:doc:`fc-pattern.1`,
:doc:`fc-query.1`,
:doc:`fc-scan.1`

HTML 形式の fontconfig ユーザーガイド::

   /usr/share/doc/fontconfig/fontconfig-user.html

著者
----------

このマニュアルページは Keith Packard <keithp@keithp.com> と Josselin Mouette <joss@debian.org> によって書かれました。
