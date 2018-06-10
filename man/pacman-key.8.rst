pacman-key(8)
==================

名称
--------

pacman-key - pacman の信頼鍵リストを管理

書式
--------

*pacman-key* [options] operation [targets]

説明
-----------

*pacman-key* は pacman のキーリングを管理するのに使用する GnuPG のラッパースクリプトです。pacman のキーリングには署名済みパッケージとデータベースをチェックするための PGP 鍵が含まれています。鍵をインポート・エクスポートしたり、キーサーバーから鍵を取得したり、鍵信頼データベースを更新することができます。

*--homedir* オプションを使って pacman キーリングを指定して (デフォルトでは /etc/pacman.d/gnupg に存在します) 直接 GnuPG を使うことで複雑な鍵管理を行うこともできます。

pacman-key を呼び出すときは操作とオプション、操作の対象を指定します。操作に合わせて、*target* は鍵の識別子・ファイル名・ディレクトリのどれかを指定します。

操作
----------

.. option:: -a, --add

   指定したファイルに含まれている鍵を pacman のキーリングに追加します。鍵が既に存在する場合、更新します。

.. option:: -d, --delete

   pacman のキーリングから指定した keyid で識別される鍵を削除します。

.. option:: -e, --export

   指定した keyid で識別される鍵を *stdout* にエクスポートします。keyid を指定しなかった場合、全ての鍵がエクスポートされます。

.. option:: --edit-key

   指定した keyid の鍵管理タスクのメニューを表示します。鍵の信頼レベルを変更したい場合に有用です。

.. option:: -f, --finger

   指定した keyid のフィンガープリントを一覧表示します。keyid を指定しなかった場合は全ての鍵のフィンガープリントが表示されます。

.. option:: -h, --help

   書式とコマンドラインオプションが出力されます。

.. option:: --import

   指定したディレクトリの公開キーリングに pubring.gpg の鍵をインポートします。

.. option:: --import-trustdb

   指定したディレクトリの共有信頼データベースに trustdb.gpg の信頼値をインポートします。

.. option:: --init

   キーリングを初期化して適当なアクセス権限が設定されているか確認します。

.. option:: -l, --list-keys

   公開キーリングから全てあるいは指定した鍵を一覧表示します。

.. option:: --list-sigs

   *--list-keys* と同じですが、署名も表示されます。

.. option:: --lsign-key

   指定した鍵をローカルで署名します。主として :option:`--init` によって生成されるローカル秘密鍵の信頼の輪に結びつけるときに使います。

.. option:: --nocolor

   pacman-key からのカラー出力を無効にします。

.. option:: -r, --recv-keys

   GnuPG の *--recv-keys* と同じです。

.. option:: --refresh-keys

   GnuPG の *--refresh-keys* と同じです。

.. option:: --populate

   /usr/share/pacman/keyrings の (任意で指定した) キーリングからデフォルトの鍵をリロードします。詳しくは下の `インポートするキーリングの提供`_ を参照。

.. option:: -u, --updatedb

   GnuPG の *--check-trustdb* と同じです。この操作は他の操作と一緒に指定できます。

.. option:: -V, --version

   プログラムのバージョンを表示します。

.. option:: -v, --verify

   指定したファイルを署名で検証します。

オプション
----------

.. option:: --config <file>

   デフォルトの /etc/pacman.conf の代わりに別の設定ファイルを使います。

.. option:: --gpgdir <dir>

   GnuPG の他のホームディレクトリを設定します。指定しなかった場合、/etc/pacman.conf から値が読み込まれます。

.. option:: --keyserver <keyserver>

   操作がキーサーバーを必要とする場合、指定したキーサーバーを使います。gpg.conf 設定ファイルで指定されたキーサーバーオプションよりも優先されます。このオプションと :option:`--init` を組み合わせて実行するとデフォルトキーサーバーが設定されます。

インポートするキーリングの提供
--------------------------------

ディストリビューションや他者のリポジトリはパッケージやリポジトリデータベースを署名するのに使用した PGP 鍵のセットを提供して、簡単に pacman のキーリングにインポートすることができます。/usr/share/pacman/keyrings ディレクトリの foo キーリングの鍵が含まれている PGP キーリングファイル foo.gpg を提供することで配布が可能です。

任意で、foo によって信頼されているファイルをキーリングの信頼鍵の ID のリストで提供することができます。このファイルのフォーマットは *gpg --export-ownertrust* の出力と互換性があります。このファイルはローカルの信頼の輪を作成するときにユーザーがどの鍵を検証・署名すればいいか示して、所有者の信頼値を割り当てます。

同じく任意で、foo によって無効化されたファイルをキーリングの無効化された鍵 ID のリストを含めて提供することができます。無効化は「以降の署名は無効である」として扱われるため、慎重に使う必要があります。失効した鍵はキーリングで無効化され有効な鍵としては扱われなくなります。他のキーリングの信頼状態よりも常に優先されます。

関連項目
--------

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
