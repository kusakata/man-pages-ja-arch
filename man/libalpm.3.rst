libalpm(3)
==================

名称
--------

libalpm - Arch Linux Package Management (ALPM) ライブラリ

書式
--------

読みやすいように libalpm マニュアルは複数のセクションに分割されています。

**TODO**: このマニュアルページはまだ作成途中です。Doxygen のドキュメントが作成できたら、改善されるはずです。約束します。

alpm_databases
   データベース関数
alpm_interface
   インターフェイス関数
alpm_list
   リスト関数
alpm_log
   ログ関数
alpm_misc
   その他の関数
alpm_packages
   パッケージ関数
alpm_sync
   同期関数
alpm_trans
   トランザクション関数

設定
----------

*pacman.conf* ファイルによる libalpm の設定について詳しくは :doc:`pacman.conf.5` を参照。

関連項目
--------

:doc:`alpm-hooks.5`,
:doc:`makepkg.8`,
:doc:`pacman.8`,
:doc:`pacman.conf.5`

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
