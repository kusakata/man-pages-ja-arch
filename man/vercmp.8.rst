vercmp(8)
==================

名称
--------

vercmp - バージョン比較ユーティリティ

書式
--------

*vercmp* <version1> <version2>

説明
-----------

vercmp を使うことで指定した2つのバージョン番号の関係を判別することができます。以下の通り値を出力します:

   * < 0 : if ver1 < ver2
   
   * = 0 : if ver1 == ver2
   
   * > 0 : if ver1 > ver2

バージョンは以下のように比較されます:

   英数字:
      1.0a < 1.0b < 1.0beta < 1.0p < 1.0pre < 1.0rc < 1.0 < 1.0.a < 1.0.1
   数字:
      1 < 1.0 < 1.1 < 1.1.1 < 1.2 < 2.0 < 3.0.0

さらに、バージョン文字列には *epoch* 値を指定することができ、epoch の値が等価でない場合、バージョンの比較が常に上書きされます。epoch 値は epoch:version-rel という形式で指定します。例えば、2:1.0-1 は常に 1:3.6-1 よりも大きいとみなされます。

*pkgrel* は両方のバージョンで指定された場合にのみ比較されるので注意してください。例えば、1.5-1 と 1.5 を比較すると 0 が返ります。1.5-1 と 1.5-2 を比較すると < 0 が返ります。*pkgrel* を含まないバージョンの依存関係をサポートするためにこのような仕様になっています。

オプション
----------

.. option:: -h, --help

   指定した操作の構文を表示します。操作が指定されなかった場合、一般的な構文が表示されます。

例
----------

.. code-block:: bash

   $ vercmp 1 2
   -1

.. code-block:: bash

   $ vercmp 2 1
   1

.. code-block:: bash

   $ vercmp 2.0-1 1.7-6
   1

.. code-block:: bash

   $ vercmp 2.0 2.0-13
   0

.. code-block:: bash

   $ vercmp 4.34 1:001
   -1

設定
----------

設定はありません。

関連項目
--------

:doc:`pacman.8`,
:doc:`makepkg.8`,
:doc:`libalpm.3`

pacman とその関連ツールの最新情報は pacman ウェブサイトの https://www.archlinux.org/pacman/ を見てください。

バグ
----------

このソフトウェアにバグは存在しません。バグを発見したら、できるかぎり詳しくバグの内容を記述して pacman-dev@archlinux.org にメールを送信してください。

著者
----------

現在のメンテナ:

   * Allan McRae <allan@archlinux.org>
   * Andrew Gregory <andrew.gregory.8@gmail.com>
   * Dan McGee <dan@archlinux.org>
   * Dave Reisner <dreisner@archlinux.org>

過去の主要貢献者:

   * Judd Vinet <jvinet@zeroflux.org>
   * Aurelien Foret <aurelien@archlinux.org>
   * Aaron Griffin <aaron@archlinux.org>
   * Xavier Chantry <shiningxc@gmail.com>
   * Nagy Gabor <ngaba@bibl.u-szeged.hu>

他の貢献者については pacman.git リポジトリで git shortlog -s を使って確認できます。
