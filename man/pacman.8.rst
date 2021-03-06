pacman(8)
==================

名称
--------

pacman - パッケージマネージャユーティリティ

書式
--------

*pacman* <operation> [options] [targets]

説明
-----------

Pacman は Linux 環境にインストールされたパッケージを追跡するパッケージ管理ユーティリティです。依存関係を解決したり、パッケージグループを扱うことができ、インストール・アンインストールスクリプトを実行したり、リモートのリポジトリとローカルマシンを同期して自動的にパッケージをアップグレードすることが可能です。Pacman のパッケージは圧縮された tar 形式です。

バージョン 3.0.0 から、pacman は :doc:`libalpm.3` ("Arch Linux Package Management" ライブラリ) のフロントエンドとなりました。このライブラリのおかげで他のフロントエンドを書くことができるようになっています (例えば、GUI フロントエンドなど)。

pacman を呼び出すときは操作とオプション、操作の対象となるターゲットを指定します。*target* はパッケージ名やファイル名、URL、あるいは検索文字列などです。ターゲットはコマンドンライン引数として指定することができます。さらに、ターミナルから入力しない場合はハイフン (-) を引数として指定することで、ターゲットを標準入力から読み込むことが可能です。

操作
----------

.. option:: -D, --database

   パッケージデータベースを操作します。この操作では pacman のデータベースにあるインストール済みのパッケージの特定の属性を変更することができます。データベースの内部的な一貫性をチェックすることもできます。下のデータベースオプションを見てください。

.. option:: -Q, --query

   パッケージデータベースに問い合わせを行います。この操作ではインストールしたパッケージとファイルを表示したり、パッケージのメタデータ (依存関係や衝突、インストール日付、ビルド日付、容量) を閲覧することができます。ローカルのパッケージデータベースに対して問い合わせたり、個別のパッケージファイルで使うことができます。前者の場合、コマンドラインにパッケージ名を指定しなかった場合、全てのインストール済みのパッケージを問い合わせます。さらに、パッケージリストに様々なフィルタを適用することができます。下のクエリオプションを見てください。

.. option:: -R, --remove

   システムからパッケージを削除します。削除するグループも指定することができ、その場合はグループに含まれている全てのパッケージが削除されます。指定したパッケージに属しているファイルが削除され、データベースが更新されます。*--nosave* オプションを使用しないかぎり、ほとんどの設定ファイルは *.pacsave* 拡張子の付いたファイルとして保存されます。下の削除オプションを見てください。

.. option:: -S, --sync

   パッケージを同期します。パッケージはリモートのリポジトリから直接インストールされ、パッケージを実行するのに必要な依存パッケージもインストールされます。例えば、``pacman -S qt`` を実行すると qt と qt が依存している全てのパッケージがダウンロード・インストールされます。同じ名前のパッケージが複数のリポジトリに存在している場合、リポジトリを明示的に指定してパッケージをインストールすることができます: ``pacman -S testing/qt``。バージョンの要件を指定することも可能です: ``pacman -S "bash>=3.2"``。クォートは必須です。クォートを使わないと ">" がファイルへのリダイレクトとしてシェルに認識されてしまいます。

   パッケージだけでなく、グループを指定することもできます。例えば、gnome がパッケージグループとして定義されている場合、``pacman -S gnome`` を実行するとどのパッケージをインストールするか数字付きリストから選択するプロンプトが表示されます。パッケージ番号を空白あるいはカンマで区切ったリストを使うことでパッケージを選択できます。ハイフン (-) でインストール最初のパッケージと最後のパッケージの数字を指定するとその間のパッケージを連続的に指定できます。数字の範囲の前にキャレット (^) を付けることでパッケージを除外することもできます。

   他のパッケージの機能を提供するパッケージも同じように扱われます。例えば、``pacman -S foo`` を実行すると最初に foo パッケージが検索されます。foo が見つからない場合、foo と同じ機能を提供するパッケージが検索されます。パッケージが見つかったら、インストールが行われます。foo を提供するパッケージが複数見つかったときは選択プロンプトが表示されます。

   ``pacman -Su`` を使って古いバージョンのパッケージを全てアップグレードすることができます。下の同期オプションを見てください。アップグレード時、pacman はバージョンの比較を行ってアップグレードが必要なパッケージを判断します。バージョンの比較は以下のように行われます:

      英数字
         1.0a < 1.0b < 1.0beta < 1.0p < 1.0pre < 1.0rc < 1.0 < 1.0.a < 1.0.1
      数字
         1 < 1.0 < 1.1 < 1.1.1 < 1.2 < 2.0 < 3.0.0

   さらに、バージョン文字列には *epoch* 値を指定することができ、epoch の値が等価でない場合、バージョンの比較が常に上書きされます。epoch 値は epoch:version-rel という形式で指定します。例えば、2:1.0-1 は常に 1:3.6-1 よりも大きいとみなされます。

.. option:: -T, --deptest

   依存関係をチェックします。makepkg などのスクリプトでインストール済みのパッケージをチェックするのに使われます。この操作は指定されたパッケージの依存パッケージをチェックして、システムにインストールされていない依存パッケージのリストを返します。この操作では他のオプションを指定できません。使用例: ``pacman -T qt "bash>=3.2"``。

.. option:: -U, --upgrade

   パッケージをアップグレードまたはシステムに追加して、同期リポジトリから必要な依存パッケージをインストールします。URL またはファイルのパスを指定できます。この操作は "remove-then-add" になります。下のアップグレードオプションを見てください。また、pacman が設定ファイルをどのように扱うのか説明している設定ファイルの処理も見てください。

.. option:: -F, --files

   ファイルデータベースに問い合わせを行います。この操作では特定のファイルが含まれているパッケージを検索したり、特定のパッケージに含まれているファイルを表示することができます。同期データベースに含まれているパッケージのみ検索されます。下のファイルオプションを見てください。

.. option:: -V, --version

   バージョンを表示して終了します。

.. option:: -h, --help

   指定された操作の構文を表示します。操作を指定しなかった場合、共通の構文が表示されます。

オプション
------------

.. option:: -b, --dbpath <path>

   データベースのパスを指定します (通常のデフォルトは /var/lib/pacman です)。よくわからない場合はむやみに使わないでください。

   .. note::

      指定するときは絶対パスで指定してください。ルートパスが自動的に補完されることはありません。

.. option:: -r, --root <path>

   インストールパスを指定します (デフォルトは / です)。/usr のかわりに /usr/local にソフトウェアをインストールしたいときに使用するべきオプションではありません。このオプションは他のシステムから一時的にマウントされているパーティションにパッケージをインストールしたいときに使用してください。

   .. note::

      データベースのパスやログファイルをコマンドラインや :doc:`pacman.conf.5` で指定しなかった場合、指定されたルートパスの下がデフォルトで使われます。

.. option:: -v, --verbose

   ルートパス・設定ファイル・DB パス・キャッシュディレクトリなどのパスを出力します。

.. option:: --arch <arch>

   別のアーキテクチャを指定します。

.. option:: --cachedir <dir>

   パッケージキャッシュのパスを指定します (通常のデフォルトは /var/cache/pacman/pkg です)。キャッシュディレクトリは複数指定することができ、指定した順番で pacman から使われます。

   .. note::

      指定するときは絶対パスで指定してください。ルートパスが自動的に補完されることはありません。

.. option:: --color <when>

   文字列をカラー化する条件を指定します。利用可能なオプションは *always*, *never*, *auto* です。*always* は常にカラー出力をオンにします。*never* はカラー出力をオフにします。*auto* は tty に出力するときだけカラー出力を自動で有効にします。

.. option:: --config <file>

   別の設定ファイルを指定します。

.. option:: --debug

   デバッグメッセージを表示します。バグを報告するときは、このオプションを使用することを推奨します。

.. option:: --gpgdir <dir>

   パッケージ署名を検証するときに GnuPG で使用するファイルのディレクトリを指定します (通常のデフォルトは /etc/pacman.d/gnupg)。指定するディレクトリには2つのファイルが必要です: pubring.gpg と trustdb.gpg。pubring.gpg には全てのパッケージ作成者の公開鍵を保存します。trustdb.gpg にはいわゆる信頼データベースを保存して、信頼すべき鍵が指定されます。

   .. note::

      指定するときは絶対パスで指定してください。ルートパスが自動的に補完されることはありません。

.. option:: --hookdir <dir>

   フックファイルが含まれている別のディレクトリを指定します (通常のデフォルトは /etc/pacman.d/hooks)。フックディレクトリは複数指定することができ、後に指定したディレクトリのほうが先に指定したディレクトリよりも優先されます。

   .. note::

      指定するときは絶対パスで指定してください。ルートパスが自動的に補完されることはありません。

.. option:: --logfile <file>

   別のログファイルを指定します。インストールルートの設定とは関係なく、絶対パスで指定します。

.. option:: --noconfirm

   確認メッセージを全てスキップします。スクリプトから pacman を実行したいとき以外はこのオプションは使わないほうが良いでしょう。

.. option:: --confirm

   上記の *--noconfirm* の効果をキャンセルします。

トランザクションオプション (-S, -R, -U に適用)
------------------------------------------------

.. option:: -d, --nodeps

   依存関係のバージョンチェックをスキップします。パッケージ名はチェックされます。通常時、pacman は常にパッケージの依存関係フィールドをチェックして、全ての依存パッケージがインストールされるようにして、システム内でパッケージが衝突しないように注意します。このオプションを2回指定すると全ての依存関係チェックがスキップされます。

.. option:: --assume-installed <package=version>

   依存関係を満たすために "package" という名前でバージョンが "version" の仮想パッケージをトランザクションに追加します。これによって依存関係チェックの全体に影響を与えることなく特定の依存関係チェックだけ無効化することができます。全ての依存関係チェックを無効化したいときは *--nodeps* オプションを見てください。

.. option:: --dbonly

   ファイルは全てそのままにして、データベースエントリだけ追加・削除します。

.. option:: --noprogressbar

   ファイルをダウンロードするときにプログレスバーを表示しません。pacman を呼び出して出力をキャプチャするスクリプトで有用です。

.. option:: --noscriptlet

   install スクリプトレットが存在する場合でも、実行しないようにします。よくわからない場合はこのオプションを使ってはいけません。

.. option:: -p, --print

   実際の操作 (同期・削除・アップグレード) を実行する代わりにターゲットの表示だけを行います。どのようにターゲットを表示するか指定するには *--print-format* を使ってください。デフォルトのフォーマット文字列は "%l" で、-S では URL を、-U ではファイル名を、-R では pkgname-pkgver を表示します。

.. option:: --print-format <format>

   printf のようなフォーマットで *--print* の出力を制御します。利用可能な属性: "%n" (pkgname), "%v" (pkgver), "%l" (location), "%r" (repository), "%s" (size)。このオプションを指定すると *--print* も自動的に有効になります。

アップグレードオプション (-S, -U に適用)
------------------------------------------

.. option:: --force

   ファイルの衝突チェックをスキップして衝突するファイルを上書きします。インストールしようとしているパッケージに既にインストール済みのファイルが含まれている場合、このオプションを使用すると衝突するファイルが上書きされます。*--force* を使用してもディレクトリをファイルで上書きすることはできず、ファイルとディレクトリが衝突するパッケージをインストールすることはできません。このオプションは注意して使用する必要があり、全く使わないほうが理想的です。

.. option:: --asdeps

   パッケージを非明示的にインストールします。言い換えると、インストール理由を依存パッケージとしてインストールしたように見せかけます。パッケージをビルドする前に依存パッケージをインストールする必要がある makepkg などのソースビルドツールで有用です。

.. option:: --asexplicit

   パッケージを明示的にインストールします。つまり、インストール理由を明示的にインストールしたものとします。依存パッケージを明示的にインストールしたものとすることで *--recursive* 削除操作で削除されないようにしたい場合に有用です。

.. option:: --ignore <package>

   パッケージのアップグレードがある場合でも無視するように指定します。カンマで区切ることで複数のパッケージを指定できます。

.. option:: --ignoregroup <group>

   グループの全てのパッケージのアップグレードを無視します。カンマで区切って複数のグループを指定できます。

.. option:: --needed

   最新バージョンのターゲットを再インストールしないようにします。

クエリオプション
-------------------

.. option:: -c, --changelog

   パッケージの変更履歴を表示します。

.. option:: -d, --deps

   依存パッケージとしてインストールされたパッケージだけに出力を制限・フィルタします。このオプションを *-t* と組み合わせることで依存パッケージとしてインストールされながら既に他のパッケージから必要とされていない孤立したパッケージを表示できます。

.. option:: -e, --explicit

   明示的にインストールしたパッケージだけに出力を制限・フィルタします。このオプションを *-t* と組み合わせることで他のパッケージに必要とされていない明示的にインストールしたパッケージだけを確認できます。

.. option:: -g, --groups

   指定したグループ名のメンバーのパッケージを全て表示します。グループ名を指定しなかった場合、全てのグループパッケージが表示されます。

.. option:: -i, --info

   指定したパッケージの情報を表示します。*-p* オプションを使うことでローカルデータベースの代わりにパッケージファイルに問い合わせることができます。*--info* または *-i* フラグを二重に渡すとバックアップファイルのリストや編集状態も表示されます。

.. option:: -k --check

   指定したパッケージに含まれているシステム上の全てのファイルをチェックします。パッケージを指定しなかった場合やフィルタグラグを指定しなかった場合、インストールされているパッケージ全てがチェックされます。このオプションを2回指定すると mtree ファイルを含んでいるパッケージについて詳しいファイルチェックが実行されます (パーミッション・ファイルサイズ・編集時刻など)。

.. option:: -l, --list

   指定したパッケージに含まれている全てのファイルを表示します。コマンドラインで複数のパッケージを指定することができます。

.. option:: -m, --foreign

   同期データベースに存在しないパッケージだけに出力を制限・フィルタします。手動でダウンロードして *--upgrade* でインストールしたパッケージなどが表示されます。

.. option:: -n, --native

   同期データベースに存在するパッケージだけに出力を制限・フィルタします。*--foreign* フィルタの逆です。

.. option:: -o, --owns <file>

   指定したファイルを含んでいるパッケージを検索します。パスは相対・絶対パスで指定でき、複数のファイルを指定することもできます。

.. option:: -p, --file

   コマンドラインで指定したパッケージがデータベースのエントリではなくファイルであることを示します。ファイルは解凍されてから中身が確認されます。*--info* aと *--list* と組み合わせて使えます。

.. option:: -q, --quiet

   特定のクエリ操作で表示する情報を少なくします。pacman の出力をスクリプトで処理するときに有用です。search ではパッケージ名だけ表示し、バージョンやグループ、説明文などは表示されなくなります。owns では "file is owned by pkg" メッセージの代わりにパッケージ名だけが表示されます。groups ではパッケージ名だけ表示してグループ名は省かれます。list ではファイルだけを表示してパッケージ名は表示しなくなります。check はパッケージ名と欠けているパッケージだけが表示されます。何もオプションを付けずに問い合わせたときはバージョンを省いてパッケージ名だけ表示します。

.. option:: -s, --search <regexp>

   ローカルにインストールされているパッケージから名前や説明文が正規表現にマッチするパッケージを検索します。複数の検索キーワードを指定した場合、全ての検索キーワードにマッチするパッケージだけが返されます。

.. option:: -t, --unrequired

   現在インストールされているパッケージから必要とされていないパッケージだけに出力を絞ります。このオプションを2回指定すると任意の依存パッケージはフィルタリングされないようになります。

.. option:: -u, --upgrades

   ローカル環境でバージョンが古くなっているパッケージだけに出力を制限・フィルタします。パッケージのバージョンだけでバージョンが古いパッケージが識別されます。アップグレード後のパッケージはチェックされません。このオプションは *-Sy* で同期データベースを更新してから使用したほうが良いでしょう。

削除オプション
-------------------

.. option:: -c, --cascade

   対象パッケージとそれらのパッケージに依存するパッケージを全て削除します。この操作は再帰的であり必要なパッケージも削除してしまう可能性があるため注意して使ってください。

.. option:: -n, --nosave

   pacman がファイルのバックアップの指定を無視するようになります。通常、システムからファイルを削除したときは、ファイルの名前を変更して *.pacsave* 拡張子を付けるべきかデータベースがチェックされます。

.. option:: -s, --recursive

   指定したターゲットと依存パッケージが削除されます。ただし削除されるのは (A) 他のパッケージによって必要とされていない (B) ユーザーによって明示的にインストールされたパッケージではないという条件を満たした場合のみです。このオプションは再帰的であり、後述の --sync 操作と似ています。このオプションを使うことでシステムに孤児が存在しないように保つことができます。条件 (B) を外したい場合、このオプションを2回指定してください。

.. option:: -u, --unneeded

   他のパッケージによって必要とされていないターゲットを削除します。依存関係を壊さないようにするため、*-c* オプションを使わずにグループを削除したいときに有用です。

同期オプション
-------------------

.. option:: -c, --clean

   インストールされていないパッケージと未使用の同期データベースをキャッシュから削除してディスク容量を増やします。pacman がパッケージをダウンロードすると、パッケージはキャッシュディレクトリに保存されます。さらに、同期 DB は全てダウンロードしたデータベースが保存されており、:doc:`pacman.conf.5` 設定ファイルから設定を削除してもデータベースは削除されません。--clean スイッチをひとつだけ指定するとインストールされていないパッケージだけ削除されます。二個指定した場合はキャッシュから全てのファイルが削除されます。どちらの場合でもパッケージや未使用のダウンロード済みデータベースの削除を yes または no で選択することになります。

   ネットワーク共有キャッシュを使っている場合、:doc:`pacman.conf.5` の *CleanMethod* オプションを見てください。

.. option:: -g, --groups

   指定したパッケージグループの全てのメンバーを表示します。グループ名を指定しなかった場合、全てのグループが表示されます。フラグを二回指定すると全てのグループとメンバーが表示されます。

.. option:: -i, --info

   指定した同期データベースのパッケージの情報を表示します。*--info* または *-i* フラグを二回指定するとパッケージに依存している全てのリポジトリのパッケージが表示されます。

.. option:: -l, --list

   指定したリポジトリの全てのパッケージが表示されます。コマンドラインには複数のリポジトリを指定できます。

.. option:: -q, --quiet

   特定の同期操作で表示する情報を少なくします。スクリプトで pacman の出力を処理する場合に有用です。search ではパッケージ名だけが表示されるようになり、リポジトリ・バージョン・グループ・説明文は表示されなくなります。list ではパッケージ名だけが表示されデータベースとバージョンは省略されます。groups ではパッケージ名だけ表示してグループ名を省略します。

.. option:: -s, --search <regexp>

   名前または説明文が正規表現にマッチするパッケージを同期データベースから検索します。検索キーワードを複数指定した場合、全ての検索キーワードにマッチするパッケージだけが返ります。

.. option:: -u, --sysupgrade

   バージョンが古いパッケージを全てアップグレードします。現在インストールされている全てのパッケージがチェックされ、新しいパッケージが存在する場合にアップグレードされます。パッケージのアップグレード情報が表示され、ユーザーが確認してからアップグレードが行われます。依存関係はこの段階で自動的に解決されて必要に応じてパッケージがインストール・アップグレードされます。

   このオプションを2回指定するとパッケージのダウングレードが有効になります。その場合、pacman はローカルのバージョンと一致しないバージョンの同期パッケージを選択します。testing リポジトリから安定版のリポジトリに切り替えるときに有用です。

   手動で追加ターゲットを指定することもでき、*-Su foo* を実行した場合、システムアップグレードが実行されてから "foo" パッケージがインストール・アップグレードされます。

.. option:: -w, --downloadonly

   サーバーから全てのパッケージを取得します。ただしインストール・アップグレードは行いません。

.. option:: -y, --refresh

   :doc:`pacman.conf.5` に定義されたサーバーからマスターパッケージデータベースのコピーをダウンロードします。コピーは通常 *--sysupgrade* や *-u* を使うときに使用されます。*--refresh* または *-y* フラグを二回指定するとデータベースが最新のときでも強制的に全てのパッケージデータベースが更新されます。

データベースオプション
-----------------------

.. option:: --asdeps <package>

   指定したパッケージを明示的にインストールしたパッケージではないと設定します。インストール理由が依存パッケージとしてインストールされたことになります。

.. option:: --asexplicit <package>

   指定したパッケージを明示的にインストールしたパッケージとします。インストール理由が明示的にインストールしたことになります。他のパッケージの依存パッケージとしてインストールしたパッケージを消したくない場合に有用です。

.. option:: -k --check

   ローカルパッケージデータベースを内部的にチェックします。必要なファイルが全て揃っていることやインストールされているパッケージに必要な依存パッケージがインストールされていること、パッケージが衝突していないこと、複数のパッケージが同じファイルを保有していないことがチェックされます。このオプションを二回指定すると同期データベースをチェックして指定された依存パッケージが全て存在しているか確認されます。

ファイルオプション
--------------------

.. option:: -y, --refresh

   サーバーから新しいパッケージデータベースをダウンロードします。二回指定するとデータベースが最新の場合でも強制的に更新を行います。

.. option:: -l, --list

   指定したパッケージに含まれているファイルを表示します。

.. option:: -s, --search

   文字列にマッチするパッケージファイル名を検索します。

.. option:: -x, --regex

   *--search* の引数を正規表現として扱います。

.. option:: -o, --owns

   指定したファイルが含まれているパッケージを検索します。

.. option:: -q, --quiet

   特定のファイル操作で表示する情報を少なくします。pacman の出力をスクリプトで処理するときに有用ですが、代わりに *--machinereadable* を使うほうが良いでしょう。

.. option:: --machinereadable

   *--list*, *--search*, *--owns* で機械が読みやすい形式を使って出力するようになります。フォーマットは repository\0pkgname\0pkgver\0path\n です (\0 は NULL 文字、\n は改行コードです)。

設定ファイルの処理
--------------------

Pacman は rpm と同じ論理を使ってファイルをバックアップするべきかどうか決定します。アップグレード時、バックアップファイルごとに3つの MD5 ハッシュを使って必要な行動を決定します: 1番目はインストールされているパッケージのオリジナルのファイル、2番目はこれからインストールする新しいファイル、3番目はファイルシステムに存在する現在のファイルです。3つのハッシュを比較すると、以下のいずれかの結果になります:

original=X, current=X, new=X
   3つのファイル全てが一致しているため、上書きしても問題ありません。新しいファイルがインストールされます。

original=X, current=X, new=Y
   現在のファイルがオリジナルと同じですが、新しいファイルのハッシュが異なっています。ユーザーによってファイルに手が加えられていないため、新しいファイルを使うことで改善が見込まれます。新しいファイルがインストールされます。

original=X, current=Y, new=X
   新旧パッケージに含まれているファイルは同じですが、ファイルシステム上のファイルに変更が加わっています。現在のファイルをそのままにしておきます。

original=X, current=Y, new=Y
   新しいファイルが現在のファイルと同じです。新しいファイルがインストールされます。

original=X, current=Y, new=Z
   3つのファイルどれもが異なっています。新しいファイルは *.pacnew* 拡張子を付けてインストールし、ユーザーに警告を表示します。ユーザーはオリジナルのファイルに行った変更を必要に応じて手動でマージする必要があります。

original=NULL, current=Y, new=Z
   パッケージを以前にインストールしておらず、ファイルシステム上に既にファイルが存在します。新しいファイルは *.pacnew* 拡張子を付けてインストールし、ユーザーに警告を表示します。ユーザーは必要な変更を手動でマージする必要があります。

例
------------

:command:`pacman -Ss ne.hack`

   パッケージデータベースを正規表現 "ne.hack" で検索します。

:command:`pacman -S gpm`

   gpm と依存パッケージをダウンロード・インストールします。

:command:`pacman -U /home/user/ceofhack-0.6-1-x86_64.pkg.tar.gz`

   ローカルファイルから ceofhack-0.6-1 パッケージをインストールします。

:command:`pacman -Syu`

   パッケージリストを更新して全てのパッケージをアップグレードします。

:command:`pacman -Syu gpm`

   パッケージリストを更新して全てのパッケージを更新して、それから gpm をインストールします (インストールされていない場合)。

設定
---------------

*pacman.conf* ファイルを使って pacman を設定する方法については :doc:`pacman.conf.5` を参照してください。

関連項目
--------

:doc:`alpm-hooks.5`,
:doc:`libalpm.3`,
:doc:`makepkg.8`,
:doc:`pacman.conf.5`

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
