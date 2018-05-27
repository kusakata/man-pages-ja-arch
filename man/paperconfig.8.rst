paperconfig(8)
==================

名称
--------

**paperconfig** - システムのデフォルト用紙サイズを設定

書式
--------

**paperconfig** [ **-v,--version** ] [ **-h,--help** ] [ **-p, --paper papername** | **--force** ]

説明
-----------

**paperconfig** は **papersize** ファイルを使用するツールによって使われるシステム (あるいはデフォルト) の用紙を設定します。インタラクティブに使用する用紙を設定したり、スクリプトから非対話式に呼び出すことができます。

用紙サイズが変更されると、:envvar:`paperconfig` は */etc/libpaper.d* ディレクトリのスクリプトを実行して他のパッケージに変更について通知します。

オプション
-----------

.. option:: -v,--version

   **paperconfig** のバージョンを出力して終了。

.. option:: -h,--help

   使用方法のヘルプを出力して終了。

.. option:: -p, --paper papername

   指定した *papername* を使用する。*papername* が用紙の名前として有効でない場合、エラーメッセージを出力して終了。

.. option:: --force

   用紙が有効であった場合でも強制的にシステムの用紙をインタラクティブに選択する。

環境変数
----------

.. envvar:: PAPERCONF

   使用する用紙サイズが記述されているファイルのフルパス。システム用紙サイズで書き換えられます。

ファイル
----------

.. object:: /etc/papersize

   **PAPERSIZE** 変数が設定されていない場合に使用するシステム全体のデフォルト用紙サイズの名前が書かれたファイル。

.. object:: /etc/libpaper.d

   用紙サイズを変更した後に実行するスクリプトのディレクトリ。このパッケージにはスクリプトは含まれていませんが、他のパッケージに含まれている可能性があります。

著者
------

Yves Arrouye <arrouye@debian.org>


関連項目
--------

:doc:`paperconf.1`,
:doc:`papersize.5`
