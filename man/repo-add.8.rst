repo-add(8)
==================

名称
--------

repo-add - パッケージデータベース管理ユーティリティ

書式
--------

*repo-add* [options] <path-to-db> <package|delta> [<package|delta> ...]

*repo-remove* [options] <path-to-db> <packagename|delta> [<packagename|delta> ...]

説明
-----------

*repo-add* と *repo-remove* は :doc:`makepkg.8` でビルドして :doc:`pacman.8` でインストールするパッケージのパッケージデータベースの作成を補助するスクリプトです。また、:doc:`pkgdelta.8` で生成されるパッケージ差分も管理します。

*repo-add* はビルドしたパッケージやパッケージ差分ファイルを読み込んでパッケージデータベースを更新します。コマンドラインで追加したい複数のパッケージやパッケージ差分を指定することができます。

パッケージファイルと対応する “.sig” ファイルが認識されると、署名は自動的にデータベースに埋め込まれます。

*repo-remove* はコマンドラインで指定したパッケージ名あるいは差分を削除してパッケージデータベースを更新します。削除したい複数のパッケージあるいは差分をコマンドラインで指定できます。

パッケージデータベースは tar ファイルであり、任意で圧縮をかけることができます。データベースの正しい拡張子は “.db” で、圧縮拡張子として “.tar”, “.tar.gz”, “.tar.bz2”, “.tar.xz”, “.tar.Z” が後ろに付きます。ファイルは必ずしも存在しなくてもよいですが、親ディレクトリは必須です。


共通のオプション
------------------

.. option:: -q, --quiet

   プログラムの出力を抑えて、警告やエラーメッセージ以外は何も表示しないようにします。

.. option:: -s, --sign

   GnuPG を使って PGP 署名ファイルを生成します。生成されるデータベースに対して gpg --detach-sign --use-agent が実行されて独立の署名ファイルが生成されます。GPG エージェントが使える場合はエージェントが使用されます。署名ファイルの名前はデータベースのファイル名に “.sig” 拡張子が付いたものになります。

.. option:: -k, --key <key>

   パッケージに署名するときに使用する鍵を指定します。GPGKEY 環境変数で指定することもできます。指定されなかった場合、キーリングのデフォルトの鍵が使用されます。

.. option:: -v, --verify

   データベースを更新する前にデータベースの PGP 鍵を検証します。署名が不正な場合、エラーが生成され更新は行われません。

.. option:: --nocolor

   *repo-add* と *repo-remove* の出力をカラー化しないようにします。

repo-add のオプション
-----------------------

.. option:: -d, --delta

   新しいパッケージファイルと同じディレクトリに古いパッケージファイルが存在した場合に、古いエントリと新しいエントリの差分ファイルを自動的に生成して追加します。

.. option:: -n, --new

   データベースに存在しないパッケージだけを追加します。既存のパッケージを認識すると警告が表示され、再追加は行われません。

.. option:: -R, --remove

   データベースのエントリを更新するときにディスクから古いパッケージファイルを削除します。

例
---

*repo-add* foo.db.tar.xz <pkg1> [<pkg2> ...]

上記のコマンドは2つのデータベースを作成します。pacman が使用する小さなデータベースの “foo.db.tar.xz” と、他のユーティリティで使用するパッケージファイルリストが含まれた大きなデータベースの “foo.files.tar.xz” です。(db.tar* 拡張子に名前を変更することで) pacman は大きい方のデータベースを使うこともできますが、ダウンロードするサイズが大きくなるだけでメリットはありません。

関連項目
--------

:doc:`makepkg.8`,
:doc:`pacman.8`,
:doc:`pkgdelta.8`

pacman とその関連ツールの最新情報は pacman のウェブサイト https://www.archlinux.org/pacman/ を見てください。

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
