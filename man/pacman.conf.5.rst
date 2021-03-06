pacman.conf(5)
==================

名称
--------

pacman.conf - pacman パッケージマネージャ設定ファイル

書式
--------

/etc/pacman.conf

説明
-----------

Pacman は :doc:`libalpm.3` を使用して実行されるたびに pacman.conf を読み込みます。この設定ファイルはセクションやリポジトリに区分されています。各セクションには *--sync* モードでパッケージを検索するときに pacman が使用するパッケージリポジトリを定義します。ただしオプションセクションにはグローバルなオプションを定義します。

例
---

.. code-block:: pacmanconf

   #
   # pacman.conf
   #
   [options]
   NoUpgrade = etc/passwd etc/group etc/shadow
   NoUpgrade = etc/fstab
   
   [core]
   Include = /etc/pacman.d/core
   
   [custom]
   Server = file:///home/pkgs

.. note::

   各ディレクティブはキャメルケースです。大文字・小文字を無視すると、ディレクティブは認識されません。例えば noupgrade や NOUPGRADE では上手く行きません。


オプション
------------

.. option:: RootDir = path/to/root

   pacman でインストールする先のデフォルトのルートディレクトリを設定します。他のシステムによって「所有」されている一時的にマウントされたパーティションにパッケージをインストールしたり、chroot インストールする際にこのオプションを使用します。

   .. note::

      コマンドラインや :doc:`pacman.conf.5` でデータベースのパスやログファイルを指定しなかった場合、デフォルトではルートパスの中になります。

.. option:: DBPath = path/to/db/dir

   トップレベルのデータベースディレクトリのデフォルトパスを上書きします。通常のデフォルトは /var/lib/pacman/ です。大抵の場合はこのオプションを設定する必要はありません。

   .. note::

      指定する場合、絶対パスで指定する必要がありルートパスは自動的に補完されません。

.. option:: CacheDir = path/to/cache/dir

   パッケージキャッシュディレクトリのデフォルトパスを上書きします。通常のデフォルトは /var/cache/pacman/pkg/ です。複数のキャッシュディレクトリを指定することができ、設定ファイルに指定された順番で使われます。キャッシュディレクトリにファイルが存在しない場合、書き込み権限がある最初のキャッシュディレクトリにファイルがダウンロードされます。

   .. note::

      絶対パスで指定してください。ルートパスは自動的に補完されません。

.. option:: HookDir = path/to/hook/dir

   システムのフックディレクトリ (/usr/share/libalpm/hooks/) に加えて alpm フックを検索するディレクトリを追加します。通常のデフォルトは /etc/pacman.d/hooks です。複数のディレクトリを指定することができ、後に記述したディレクトリのフックのほうが先に記述したディレクトリのフックよりも優先されます。

   .. note::

      絶対パスで指定してください。ルートパスは自動的に補完されません。alpm フックについて詳しくは :doc:`alpm-hooks.5` を参照。

.. option:: GPGDir = path/to/gpg/dir

   GnuPG の設定ファイルが含まれているディレクトリのデフォルトのパスを上書きします。通常のデフォルトは /etc/pacman.d/gnupg/ です。このディレクトリには2つのファイルが必要です: pubring.gpg と trustdb.gpg。pubring.gpg には全てのパッケージ作成者の公開鍵を保存します。trustdb.gpg はいわゆる信頼データベースで、信頼できるとする鍵を指定します。

   .. note::

      絶対パスで指定してください。ルートパスは自動的に補完されません。

.. option:: LogFile = /path/to/file

   pacman のログファイルのデフォルトのパスを上書きします。通常のデフォルトは /var/log/pacman.log です。絶対パスで指定してください。ルートディレクトリは補完されません。

.. option:: HoldPkg = package ...

   ユーザーが HoldPkg に含まれているパッケージを *--remove* しようとしたとき、pacman は削除する前に確認するように表示します。シェル風の glob パターンを使うことができます。

.. option:: IgnorePkg = package ...

   *--sysupgrade* を実行したときに指定したパッケージのアップグレードを無視するように pacman を設定します。シェル風の glob パターンを使うことができます。

.. option:: IgnoreGroup = group ...

   *--sysupgrade* を実行したときに指定したグループの全てのパッケージのアップグレードを無視するように pacman を設定します。シェル風の glob パターンを使うことができます。

.. option:: Include = path

   他の設定ファイルをインクルードします。リポジトリや一般的な設定オプションを読み込むことができます。指定したパスに含まれているワイルドカードは :doc:`glob.7` ルールに基づいて展開されます。

.. option:: Architecture = auto | i686 | x86_64 | ...

   設定した場合、pacman は指定されたアーキテクチャ (例: *i686*, *x86_64*) のパッケージのインストールしか行いません。特殊な値として *auto* は “uname -m” によるシステムアーキテクチャを使用します。設定しなかった場合、アーキテクチャのチェックは行われません。

   .. note::

      特殊なアーキテクチャ *any* のパッケージは常にインストールが可能です。*any* のパッケージはアーキテクチャに依存しません。

.. option:: XferCommand = /path/to/command %u

   設定した場合、外部のプログラムを使ってリモートのファイルがダウンロードされます。%u は全てダウンロード URL に置換されます。存在する場合、%o はローカルのファイル名に置き換わります。また、wget などのプログラムでファイルレジュームが機能するように “.part” 拡張子が使われます。

   このオプションは pacman の HTTP/FTP サポートで問題が発生する場合や、wget などのユーティリティに組み込まれている高度なプロキシサポートが必要な場合に有用です。

.. option:: NoUpgrade = file ...

   パッケージのインストール・アップグレード時に NoUpgrade ディレクティブで指定したファイルは変更がされず、新しいファイルは *.pacnew* 拡張子を付けてインストールされます。パッケージアーカイブの中のファイルを指定するため、ファイルを指定するときはパスの最初にスラッシュ (ルートディレクトリ) を含めてはいけません。シェル風の glob パターンを使うことができます。ファイルの前に感嘆符を付けることでマッチングを逆にすることができます。マッチングを逆にすることでブラックリストに入れられたファイルがホワイトリストに入ります。マッチングは後に記述のほうが優先されます。文字列の感嘆符やバックスラッシュはエスケープする必要があります。

.. option:: NoExtract = file ...

   NoExtract ディレクティブに指定したファイルはパッケージからファイルシステムに展開されません。パッケージの一部だけインストールしたくない場合に有用です。例えば、httpd のルートとして index.php を使用していて、apache パッケージから index.html ファイルを展開して欲しくない場合など。パッケージアーカイブの中のファイルを指定するため、ファイルを指定するときはパスの最初にスラッシュ (ルートディレクトリ) を含めてはいけません。シェル風の glob パターンを使うことができます。ファイルの前に感嘆符を付けることでマッチングを逆にすることができます。マッチングを逆にすることでブラックリストに入れられたファイルがホワイトリストに入ります。マッチングは後に記述のほうが優先されます。文字列の感嘆符やバックスラッシュはエスケープする必要があります。

.. option:: CleanMethod = KeepInstalled &| KeepCurrent

   KeepInstalled (デフォルト) に設定されている場合、-Sc コマンドではインストールされていない (ローカルデータベースに存在しない) パッケージが消去されます。KeepCurrent に設定されている場合、-Sc は (同期データベースに存在しない) 古いバージョンのパッケージが消去されます。複数のマシン間でパッケージキャッシュを共有する場合、ローカルのデータベースは通常異なりますが使用するデータベースは同一のため、後者に設定すると便利です。両方の値を指定した場合、ローカルにインストールされてなく既知の同期データベースに存在しないパッケージだけが消去されます。

.. option:: SigLevel = ...

   デフォルトの署名検証レベルを設定します。詳しくは下の `パッケージとデータベースの署名チェック`_ を見てください。

.. option:: LocalFileSigLevel = ...

   ローカルファイルで "-U" 操作を使ってパッケージをインストールするときの署名検証レベルを設定します。デフォルトでは SigLevel の値が使われます。

.. option:: RemoteFileSigLevel = ...

   リモートのファイル URL で "-U" 操作を使ってパッケージをインストールするときの署名検証レベルを設定します。デフォルトでは SigLevel の値が使われます。

.. option:: UseSyslog

   syslog() 経由でアクションメッセージをログ出力します。/var/log/messages などにログエントリが挿入されます。

.. option:: Color

   tty で pacman から出力するときにカラー出力を自動的に有効化します。

.. option:: UseDelta [= ratio]

   可能であれば完全なパッケージのかわりに差分ファイルをダウンロードします。xdelta3 プログラムのインストールが必要です。ratio を指定した場合 (例: 0.5)、差分を使用するかどうか決めるカットオフ値として使われます。使用できる値は 0.0 と 2.0 の間です。0.2 から 0.9 までの値が穏当です。1.0 よりも大きな値はノーグッドです。指定しないときは 0.7 がデフォルトです。

.. option:: TotalDownload

   パッケージのダウンロード時に、個別のダウンロードファイルのパーセントを表示するかわりに、ダウンロード総量・ダウンロード速度・ETA・ダウンロードリストのW完了率を表示します。ただしプログレスバーは現在ダウンロードしているファイルのみを表すのは変わりません。XferCommand を使用している場合、このオプションは機能しません。

.. option:: CheckSpace

   パッケージをインストールする前に十分なディスク容量があるか近似的なチェックを実行します。

.. option:: VerbosePkgLists

   アップグレード・同期・削除操作でパッケージの名前・バージョン・容量を表として表示します。

リポジトリセクション
----------------------

リポジトリセクションにはそれぞれセクション名とパッケージを検索するパスを定義します。セクション名は角括弧で囲った文字列で定義します (上の2つは *core* と *custom* です)。リポジトリ名は一意である必要があり、*local* の名前はインストール済みのパッケージのデータベースとして予約されています。パスは *Server* ディレクティブで定義し URL で指定します。ローカルディレクトリを使いたいときは、フルパスに “file://” プレフィックスを付けて指定します。

DB パスを定義する一般的な方法は *Include* ディレクティブを利用することです。設定ファイルで定義する各リポジトリごとに、リポジトリのサーバーを列挙したファイルを *Include* ディレクティブで含めることができます。

.. code-block:: pacmanconf

   [core]
   # use this server first
   Server = ftp://ftp.archlinux.org/$repo/os/$arch
   # next use servers as defined in the mirrorlist below
   Include = {sysconfdir}/pacman.d/mirrorlist

設定ファイルのリポジトリの順序は重要です。2つの同じリポジトリに同じ名前のパッケージが存在した場合、先に記述されたリポジトリのほうがファイルの後のほうに記述されたリポジトリよりも優先されます。その際バージョン番号は関係ありません。

.. option:: Include = path

   他の設定ファイルを読み込みます。リポジトリや一般的な設定オプションを読み込むことができます。ワイルドカードは :doc:`glob.7` ルールに基づいて展開されます。

.. option:: Server = url

   リポジトリのデータベース・パッケージ・署名が存在する完全な URL (署名はない場合もあります)。

   パース時に、pacman は $repo 変数を現在のセクションの名前に定義します。しばしば全てのリポジトリが同じミラーファイルを使用できるように *Include* ディレクティブでファイルを指定するときに使われます。また、pacman は $arch 変数をアーキテクチャの値に定義するため、同じミラーファイルで異なるアーキテクチャを使用することができます。

.. option:: SigLevel = ...

   リポジトリの署名検証レベルを設定します。詳しくは下の `パッケージとデータベースの署名チェック`_ を見てください。

.. option:: Usage = ...

   リポジトリの使用レベルを設定します。このオプションには以下のトークンのリストを指定します:

   Sync
      リポジトリの更新を有効にします。
   Search
      リポジトリの検索を有効にします。
   Install
      *--sync* 操作によるリポジトリからのパッケージのインストールを有効にします。
   Upgrade
      *--sysupgrade* を実行するときにパッケージのソースとしてリポジトリを使用できるようにします。
   All
      上記の全ての機能をリポジトリで有効にします。使用レベルを指定しなかった場合のデフォルトです。

   設定した使用レベルとは関係なく、明示的に有効なリポジトリを操作することは可能なので注意してください。

パッケージとデータベースの署名チェック
----------------------------------------

*SigLevel* ディレクティブは [options] とリポジトリセクションで利用できます。[options] で使用した場合、設定がないリポジトリのデフォルト値として設定されます。

* **Never** に設定した場合、署名チェックは行われません。
* **Optional** に設定した場合、署名がある場合はチェックされますが、署名がないデータベースやパッケージも使用できます。
* **Required** に設定した場合、全てのパッケージとデータベースで署名が必須になります。

また、以下で説明しているようにオプションとプレフィックスを組み合わせて細かく制御することが可能です。設定ファイルの全てのオプションは上から下、左から右の流れで処理され、後者のオプションが前者のオプションを上書き・補填します。リポジトリセクションで *SigLevel* を指定した場合、[options] セクションのオプションか (指定がない場合) 以下のシステムデフォルトが最初の値となります。

以下の通りオプションは2つのグループに分けられます。“marginally trusted” などの用語は GnuPG が使用している単語です。詳しくは :doc:`gpg.1` を読んでください。

チェックするタイミング
   以下のオプションはいつどのようなときに署名チェックを行うかを制御します。

   Never
      たとえ署名が存在する場合でも、全ての署名チェックが行われません。
   Optional (デフォルト)
      署名が存在する場合にチェックします。署名がなくてもエラーになりません。キーリングにない鍵の署名など、不正な署名は致命的なエラーになります。
   Required
      署名は必須になります。署名がない場合や不正な場合は致命的なエラーとなります。

許可する署名
   以下のオプションはどのような署名を許容するか制御します。不正な署名や期限切れの署名、あるいは無効化された鍵の署名は全て拒否されるので注意してください。

   TrustedOnly (デフォルト)
      署名をチェックするとき、署名がキーリングに存在し完全に信頼されている必要があります。ある程度の信頼度では条件を満たしません。
   TrustAll
      署名をチェックするとき、署名がキーリングに存在する必要がありますが、信頼度レベルは考慮されません (例: 不明あるいはある程度の信頼度も含まれます)。

どちらのグループのオプションも **Package** または **Database** を前に付けることができ、その場合は指定したオブジェクトタイプにのみ効果が適用されます。例えば、PackageTrustAll ならばパッケージについてある程度 (marginal) あるいは不明 (unknown) な信頼度レベルが許可されます。

指定しなかった場合のデフォルトは以下の通りです:

.. code-block:: pacmanconf

   SigLevel = Optional TrustedOnly

自分のリポジトリを使う
-----------------------

カスタムパッケージを大量に使用している場合、*--upgrade* オプションを使ってインストールするよりもカスタムローカルリポジトリを生成するほうが簡単です。パッケージが入ったディレクトリに圧縮したパッケージデータベースを生成するだけで --refresh を実行したときにリポジトリが検索されます。

.. code-block:: console

   repo-add /home/pkgs/custom.db.tar.gz /home/pkgs/*.pkg.tar.gz

上記のコマンドは */home/pkgs/custom.db.tar.gz* という名前の圧縮データベースを生成します。データベースは設定ファイルで定義する形式である必要があり、*{ext}* は :doc:`repo-add.8` に書かれている正しい圧縮タイプでなければなりません。後は上の設定例のように設定ファイルのカスタムセクションで設定してください。それで Pacman はあなたのパッケージリポジトリを使えるようになります。リポジトリに新しいパッケージを追加したら、データベースを再生成して pacman の *--refresh* オプションを使ってください。

repo-add コマンドについて詳しい情報は “repo-add --help” または :doc:`repo-add.8` を参照してください。

関連項目
--------

:doc:`pacman.8`,
:doc:`libalpm.3`

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
