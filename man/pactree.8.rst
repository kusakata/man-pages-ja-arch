pactree(8)
==================

名称
--------

pactree - パッケージ依存ツリービューア

書式
--------

*pactree* [options] package

説明
-----------

Pactree はパッケージの依存ツリーを生成します。

デフォルトでは、ツリー状の出力が生成されますが、*--graph* オプションを使うことで Graphviz の記述を生成できます。

オプション
----------

.. option:: -a, --ascii

   ツリーの整形に ASCII 文字を使用します。デフォルトでは pactree はコンソールがサポートしているのであれば Unicode の罫線素片文字を使用します。

.. option:: -b, --dbpath

   別のデータベースのパスを指定します。

.. option:: -c, --color

   出力をカラー化します。

.. option:: -d, --depth <num>

   表示する依存のレベルを制限します。0 なら指定したパッケージだけが表示され、1 なら指定したパッケージが直接依存しているパッケージだけが表示されます。

.. option:: -g, --graph

   Graphviz の記述を生成します。このオプションが指定されたとき、*--color* と *--linear* オプションは無視されます。

.. option:: -h, --help

   書式とコマンドラインオプションを出力します。

.. option:: -l, --linear

   1行毎にパッケージの名前を出力します。

.. option:: -r, --reverse

   指定したパッケージに依存しているパッケージを表示します。

.. option:: -s, --sync

   ローカルデータベースではなく同期データベースのパッケージデータを読み込みます。

.. option:: -u, --unique

   依存パッケージを一度だけ表示します。*--linear* も有効になります。

.. option:: --config <file>

   別の pacman 設定ファイルを指定します。

関連項目
--------

:doc:`pacman.8`,
:doc:`pacman.conf.5`,
:doc:`makepkg.8`

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
