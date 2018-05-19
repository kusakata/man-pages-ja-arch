pkgdelta(8)
==================

名称
--------

pkgdelta - パッケージ差分生成ユーティリティ

書式
--------

*pkgdelta* [options] <package1> <package2>

説明
-----------

*pkgdelta* は同じパッケージの異なるバージョン間のパッケージ差分ファイルを作成するために使用します。差分ファイルは基本的にはバイナリパッチとなります。:doc:`pacman.8` は完全なパッケージアップグレードを実行するかわりに差分をダウンロードして、(パッケージキャッシュに存在する) 前のバージョンのパッケージに差分を適用して、パッケージをアップグレードすることができます。アップグレードに必要なダウンロード容量をかなり減らすことが可能です。

*pkgdelta* は差分を生成するのに :doc:`xdelta3.1` を必要とします。

オプション
----------

.. option:: --max-delta-size <ratio>

   差分が ratio * package_size よりも小さく場合にのみ差分ファイルを作成します。指定できる値の範囲: 0.0 から 2.0。推奨値: 0.2 から 0.9。デフォルト値: 0.7。

.. option:: --min-pkg-size <size>

   差分を作成するパッケージファイルの最小サイズ (バイト数)。デフォルト値: 1048576 バイト = 1 MiB。バイト数で絶対値を指定するか 4MiB や 3.5MB などのように人間が読みやすい形式で指定することができます。

.. option:: -q, --quiet

   出力を抑えます。警告とエラー以外は何も出力しません。

関連項目
--------

:doc:`pacman.8`,
:doc:`xdelta3.1`

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
