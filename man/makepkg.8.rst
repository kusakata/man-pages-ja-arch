makepkg(8)
==================

名称
--------

makepkg - パッケージビルドユーティリティ

書式
--------

*makepkg* [options] [ENVVAR=value] [ENVVAR+=value] ...

説明
-----------

*makepkg* はパッケージのビルドを自動化するスクリプトです。スクリプトを使うにはビルドが可能な ＊nix プラットフォームとビルドしたい各パッケージのカスタムビルドスクリプト (PKGBUILD) が必要です。ビルドスクリプトの作成方法については :doc:`PKGBUILD.5` を見てください。

スクリプトによるビルドの利点としてビルド作業が一度に完了します。パッケージのビルドスクリプトさえ用意できれば、*makepkg* が後は全てやってくれます: ソースファイルのダウンロード・検証、依存関係のチェック、ビルド時の設定、パッケージのビルド、一時的なルートディレクトリへのパッケージのインストール、カスタマイズ、メタ情報の生成、pacman から使えるように全てのファイルをパッケージ化。

.. note::

   *makepkg* はデフォルトでは現在のロケールを使用し、パッケージのビルド時にロケールの設定解除は行いません。ビルドの出力を他の人と共有して助けを得たい場合は、"LC_ALL=C makepkg" として実行することでログや出力を英語にできます。

オプション
------------

.. option:: -A, --ignorearch

   ビルドスクリプトの不完全な arch フィールドを無視します。PKGBUILD が古くて arch=('yourarch') フィールドが設定されていない場合にソースからパッケージを再ビルドするときに使用してください。

.. option:: -c, --clean

   ビルドが成功した後に作業ファイルやディレクトリを消去します。

.. option:: --config <file>

   デフォルトの /etc/makepkg.conf の代わりに他の設定ファイルを使用します。

.. option:: -d, --nodeps

   依存関係のチェックを行いません。必要な依存関係を上書きしたり無視することができます。依存パッケージが全てインストールされていない場合、ビルドが上手くいかなくなる可能性があります。

.. option:: -e, --noextract

   ソースファイルを展開したり prepare() 関数を実行しません (存在する場合)。ソースが既に $srcdir/ ディレクトリに存在する場合に使用してください。$srcdir/ から手動でコードにパッチをあてて、それからパッケージを作成したい場合に有用です。他の人が同じ PKGBUILD を使うときはパッチを作成するほうが良いでしょう。

.. option:: --verifysource

   PKGBUILD の source 配列に指定されたソースファイルについて、必要なファイルをダウンロードしてから整合性のチェックを実行します。ファイルの展開やビルドは実行されません。*--syncdeps* を使用しないかぎり PKGBUILD の依存関係の処理も行われません。オフラインビルドをしたいときに有用です。

.. option:: -f, --force

   ビルド済みのパッケージが PKGDEST (:doc:`makepkg.conf.5` で設定) のディレクトリ (デフォルトではカレントディレクトリ) に存在する場合は makepkg はパッケージをビルドしなくなります。このオプションを使うことでパッケージの上書きが許可されます。

.. option:: -g, --geninteg

   PKGBUILD の source 配列に指定されたソースファイルについて、必要なファイルをダウンロードしてから整合性チェックが生成されます。整合性チェックは PKGBUILD に書かれているチェックにあわせて生成され、書かれていない場合は :doc:`makepkg.conf.5` の INTEGRITY_CHECK 配列の値が使用されます。"makepkg -g >> PKGBUILD" と出力をリダイレクトすることで PKGBUILD にソース検証を追加できます。

.. option:: --skipinteg

   ソースファイルの整合性チェック (チェックサムと PGP) を実行しません。

.. option:: --skipchecksums

   ソースファイルのチェックサムを検証しません。

.. option:: --skippgpcheck

   ソースファイルの PGP 署名を検証しません。

.. option:: -h, --help

   書式とコマンドラインオプションを出力します。

.. option:: --holdver

   VCS のソース (:doc:`PKGBUILD.5`) を使うときに、チェックアウトされているソースを最新リビジョンに更新しません。

.. option:: -i, --install

   ビルドが成功したら :doc:`pacman.8` でパッケージをインストール・アップグレードします。

.. option:: -L, --log

   ログ出力を有効にします。**tee** プログラムを使って PKGBUILD 関数の出力がコンソールとビルドディレクトリのテキストファイル (pkgbase-pkgver-pkgrel-arch-<function>.log という名前) に送信されます。上述のとおり、ログは地域化されるため、他の人とログ出力を共有するときはロケールを設定するようにしてください。

.. option:: -m, --nocolor

   出力メッセージのカラー化を無効にします。

.. option:: -o, --nobuild

   ファイルをダウンロード・展開して、prepare() 関数を実行しますが、ビルドは行いません。ビルドする前に $srcdir/ 内のファイルに手を加えたい場合に *--noextract* オプションと一緒に使うと有用です。

.. option:: -p <buildscript>

   デフォルトの PKGBUILD の代わりに指定したパッケージスクリプト buildscript を読み込みます。:doc:`PKGBUILD.5` を参照してください。buildscript は makepkg を呼び出すディレクトリに配置する必要があります。

.. option:: -r, --rmdeps

   ビルド成功時、依存関係の自動解決によって -s で makepkg によってインストールされた依存パッケージを削除します。

.. option:: -R, --repackage

   パッケージを再ビルドせずにパッケージの中身を再パッケージ化します。PKGBUILD に依存関係や install ファイルを記述し忘れたときなどにビルド自体は変わらないため有用です。

.. option:: -s, --syncdeps

   pacman を使って欠けている依存パッケージをインストールします。ビルド時・実行時の依存パッケージが存在しないときは、pacman によって依存関係の解決が試行されます。成功した場合、欠けているパッケージがダウンロード・インストールされます。

.. option:: -S, --source

   パッケージを実際にビルドするかわりに、ダウンロード URL から取得できるソースを含まないソースのみの tarball をビルドします。chroot など他のプログラムに tarball を渡したいときや tarball をアップロードするときに有用です。整合性チェックは確認されるため、パッケージのソースファイルは全て存在しているかダウンロード可能である必要があります。

.. option:: -V, --version

   バージョン情報を表示します。

.. option:: -C, --cleanbuild

   パッケージをビルドする前に $srcdir を削除します。

.. option:: --allsource

   パッケージを実際にビルドするかわりに、通常時 makepkg でダウンロードされる全てのソースを含んだソースのみの tarball をビルドします。chroot など他のプログラムやリモートのビルダーに tarball を渡したいときに有用です。バイナリパッケージを配布する場合は GPL の要件が満たされます。

.. option:: --check

   :doc:`makepkg.conf.5` の設定を上書きして PKGBUILD の check() 関数を実行します。

.. option:: --noarchive

   ビルドの最後にアーカイブを作成しません。package() 関数をテストしたい場合や対象ディストリビューションで pacman を使わない場合に有用です。

.. option:: --nocheck

   PKGBUILD の check() 関数を実行せず checkdepends も処理されません。

.. option:: --noprepare

   PKGBUILD の prepare() 関数を実行しません。

.. option:: --sign

   :doc:`makepkg.conf.5` の設定を上書きして作成されたパッケージに gpg で署名します。

.. option:: --nosign

   ビルドしたパッケージに署名を作成しません。

.. option:: --key <key>

   パッケージを署名するときに使用する鍵を指定します。:doc:`makepkg.conf.5` の GPGKEY 設定を上書きします。どこでも指定されなかった場合は、キーリングのデフォルトの鍵が使用されます。

.. option:: --noconfirm

   (pacman に渡されます) 操作を続行する前にユーザーの入力を pacman が待機しなくなります。

.. option:: --needed

   (pacman に渡されます) パッケージが最新の場合はパッケージを再インストールしないようにします (*-i* / *--install* で使用)。

.. option:: --asdeps

   (pacman に渡されます) 依存関係としてインストールされたものとしてパッケージをインストールします (*-i* / *--install* で使用)。

.. option:: --noprogressbar

   (pacman に渡されます) pacman がプログレスバーを表示しなくなります。makepkg の出力をファイルにリダイレクトする場合に有用です。

.. option:: --packagelist

   ビルドせずに生成されるパッケージを一覧表示します。表示されるパッケージの名前には PKGEXT は含まれません。

.. option:: --printsrcinfo

   SRCINFO ファイルを生成して標準出力に出力します。

追加機能
--------------------

makepkg は PKGBUILD の pkgver を手動で更新しなくても開発版のパッケージをビルドすることができます。開発用の PKGBUILD を設定する方法は :doc:`PKGBUILD.5` を見てください。

環境変数
------------

.. envvar:: PACMAN

   欠けている依存関係をチェックしてパッケージをインストール・削除するのに使用するコマンド。指定したコマンドは Pacman の -Qq, -Rns, -S, -T, -U 操作をサポートしている必要があります。変数が設定されていなかった空の場合、'pacman' が使用されます。

.. envvar:: MAKEPKG_CONF="/path/to/file"

   デフォルトの /etc/makepkg.conf の代わりに別の設定ファイルを使用します。

.. envvar:: PKGDEST="/path/to/directory"

   作成したパッケージを保存するディレクトリ。:doc:`makepkg.conf.5` で定義した値を上書きします。

.. envvar:: SRCDEST="/path/to/directory"

   ダウンロードしたソースを保存するディレクトリ。:doc:`makepkg.conf.5` で定義した値を上書きします。

.. envvar:: SRCPKGDEST="/path/to/directory"

   ソースパッケージファイルを保存するディレクトリ。:doc:`makepkg.conf.5` で定義した値を上書きします。

.. envvar:: LOGDEST="/path/to/directory"

   生成したログファイルを保存するディレクトリ。:doc:`makepkg.conf.5` で定義した値を上書きします。

.. envvar:: PACKAGER="John Doe <john@doe.com>"

   作成したパッケージの作成者を識別する文字列。:doc:`makepkg.conf.5` で定義した値を上書きします。

.. envvar:: BUILDDIR="/path/to/directory"

   パッケージがビルドされるディレクトリ。:doc:`makepkg.conf.5` で定義した値を上書きします。

.. envvar:: CARCH="(i686|x86_64)"

   指定したアーキテクチャでビルドを実行。クロスコンパイルを行いたいときに有用。:doc:`makepkg.conf.5` で定義した値を上書きします。

.. envvar:: PKGEXT=".pkg.tar.gz", SRCEXT=".src.tar.gz"

   コンパイルされたパッケージやソースパッケージを圧縮するときの拡張子を設定。:doc:`makepkg.conf.5` で定義した値を上書きします。

.. envvar:: GNUPGHOME="/path/to/directory"

   ビルドしたパッケージに署名する gpg キーリングが保存されているディレクトリ。

.. envvar:: GPGKEY="keyid"

   パッケージを署名するときに使用する鍵を指定。:doc:`makepkg.conf.5` の GPGKEY 設定が上書きされます。

設定
---------------

*makepkg.conf* ファイルを使って makepkg を設定する方法については :doc:`makepkg.conf.5` を参照してください。

関連項目
--------

:doc:`makepkg.conf.5`,
:doc:`PKGBUILD.5`,
:doc:`pacman.8`

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
