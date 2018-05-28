debootstrap(8)
==================

名称
--------

debootstrap - ベーシックな Debian システムのブートストラップ

書式
--------

**debootstrap** [**OPTION...**] *SUITE* *TARGET* [*MIRROR* [*SCRIPT*]]

**debootstrap** [**OPTION...**] --second-stage

説明
-----------

**debootstrap** は *SCRIPT* を実行して *MIRROR* から *SUITE* の基本 Debian 環境を *TARGET* にブートストラップします。*MIRROR* には http:// または https:// の URL や file:/// URL、ssh:/// URL が指定できます。

*SUITE* にはリリースコードの名前 (例: sid, stretch, jessie) かシンボル名 (例: unstable, testing, stable, oldstable) を指定します。

file:/ URL は (RFC1738 でローカルのファイル名の正しいスキームとされている) file:/// に変換されますが、file:// は使えないので注意してください。ssh://USER@HOST/PATH URL は **scp** を使って取得されます。**ssh-agent** などを使用することを強く推奨します。

**Debootstrap** ではインストールディスクを使用せずにシステムに Debian をインストールすることができますが、インストールディスクを使って :doc:`chroot.1` 環境で異なる Debian フレーバーを動作させることも可能です。この場合、テスト目的で使えるフルの (最小) Debian 環境を作成することができます (`サンプル`_ セクションを見てください)。chroot 環境でパッケージをビルドしたい場合は **pbuilder** を参照してください。

オプション
------------

.. option:: --arch=ARCH

   対象アーキテクチャを設定します (dpkg がインストールされていない場合に使用してください)。:option:`--foreign` も参照。

.. option:: --include=alpha,beta

   ダウンロード・展開リストに追加するパッケージのリストをカンマで区切って指定します。

.. option:: --exclude=alpha,beta

   ダウンロード・展開リストから削除するパッケージのリストをカンマで区切って指定します。

   .. warning::

      重要なパッケージを誤って削除してしまう可能性もあるため、このオプションは注意して使ってください。

.. option:: --components=alpha,beta

   アーカイブのコンポーネントからパッケージを使用します。

.. option:: --no-resolve-deps

   デフォルトでは、debootstrap は欠けている依存関係を自動的に解決して、見つかった場合は警告を表示します。dpkg や apt のような完全な依存解決ではないので注意してください。また、このオプションを使うよりも完全なベースシステムを指定するほうが好ましいとされます。このオプションを設定した場合、依存解決が無効になります。

.. option:: --variant=minbase|buildd|fakechroot

   使用するブートストラップスクリプトの名前を指定します。現在のところ、サポートされているスクリプトは、必須パッケージと apt だけが含まれている minbase と、build-essential パッケージをインストールする buildd、そして root 権限を使わずにパッケージをインストールする fakechroot です。**--variant=X** 引数を指定しなかった場合、apt を含む、プライオリティが *required* および *important* の全てのパッケージが含まれたベース Debian 環境がデフォルトで作成されます。

.. option:: --merged-usr

   /{bin,sbin,lib}/ を /usr/ にまとめるシンボリックリンクを作成します。

.. option:: --no-merged-usr

   /{bin,sbin,lib}/ を /usr/ にまとめるシンボリックリンクを作成しません (デフォルト)。

.. option:: --keyring=KEYRING

   ディストリビューションをブートストラップするデフォルトのキーリングを上書きして、*KEYRING* を使用して取得したリリースファイルの gpg 署名をチェックします。

.. option:: --no-check-gpg

   取得したリリースファイルの gpg 署名のチェックを無効化します。

.. option:: --force-check-gpg

   リリースファイルの署名チェックを強制的に行い、キーリングが存在しない場合に HTTPS に自動フォールバックしないようにします。:option:`--no-check-gpg` と一緒に指定することはできません。

.. option:: --verbose

   ダウンロード情報について詳しく出力します。

.. option:: --print-debs

   インストールされるパッケージについて出力して終了します。debootstrap がパッケージファイルをダウンロードしてどのパッケージをインストールし依存関係を解決するか決定できるように、空、または存在しない TARGET を指定する必要があります。--keep-debootstrap-dir を指定しないかぎり、TARGET ディレクトリは削除されます。

.. option:: --download-only

   パッケージのダウンロードだけを行い、インストールは実行しません。

.. option:: --foreign

   ブートストラップの最初の解凍フェーズだけを行います。例えば対象アーキテクチャがホストのアーキテクチャと一致しない場合などに使います。debootstrap のコピーだけで対象ファイルシステムに /debootstrap/debootstrap としてインストールするブートストラップを完了できます。:option:`--second-stage` オプションを使って実行することでブートストラップを仕上げることが可能です。

.. option:: --second-stage

   ブートストラップを完了します。通常、他の引数は必要ありません。

.. option:: --second-stage-target=DIR

   ルートではなくサブディレクトリでセカンドステージを実行します (アーキテクチャが異なる chroot を作成することができます)。:option:`--second-stage` が必要です。

.. option:: --keep-debootstrap-dir

   インストールが完了した後にターゲットの /debootstrap ディレクトリを削除しません。

.. option:: --cache-dir=DIR

   .deb ファイルのキャッシュディレクトリ。絶対パスで指定してください。

.. option:: --unpack-tarball=FILE

   HTTP(S) でダウンロードするのではなく gzip で圧縮された tarball の *FILE* (絶対パスで指定) から .deb を取得します。

.. option:: --make-tarball=FILE

   ブートストラップするかわりに、ダウンロードしたパッケージを gzip でまとめた tarball を作成します (*FILE* に書き出します)。作成された tarball は後から **--unpack-tarball** で指定して使うことができます。debootstrap がパッケージをダウンロードして tarball を準備できるように、空、または存在しない TARGET ディレクトリを指定する必要があります。:option:`--keep-debootstrap-dir` を指定しないかぎり、TARGET ディレクトリは削除されます。

.. option:: --debian-installer

   debian-installer によって内部処理で使われます。

.. option:: --extractor=TYPE

   自動 .deb 展開ツールの選択を *TYPE* に上書きします。サポートされている展開ツール: dpkg-deb と ar。

.. option:: --no-check-certificate

   認証局に対して証明書をチェックしません。

.. option:: --certificate=FILE

   ファイルに保存されているクライアント証明書 (PEM) を使用します。

.. option:: --private-key=FILE

   ファイルから秘密鍵を読み込みます。

サンプル
----------

stretch システムをセットアップするには:

.. code-block:: console

   debootstrap stretch ./stretch-chroot http://deb.debian.org/debian

.. code-block:: console

   debootstrap stretch ./stretch-chroot file:///LOCAL_MIRROR/debian

chroot に sid (unstable) の完全な Debian 環境を作成する場合:

.. code-block:: console

   main # debootstrap sid sid-root http://deb.debian.org/debian/
   [ ... watch it download the whole system ]
   main # echo "proc sid-root/proc proc defaults 0 0" >> /etc/fstab
   main # mount proc sid-root/proc -t proc
   main # echo "sysfs sid-root/sys sysfs defaults 0 0" >> /etc/fstab
   main # mount sysfs sid-root/sys -t sysfs
   main # cp /etc/hosts sid-root/etc/hosts
   main # chroot sid-root /bin/bash

著者
----------

**debootstrap** は Anthony Towns <ajt@debian.org> によって書かれました。このマニュアルページは Matt Kraai <kraai@debian.org> によって書かれました。
