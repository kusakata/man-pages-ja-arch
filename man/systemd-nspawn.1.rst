systemd-nspawn(1)
==================

名称
--------

systemd-nspawn - デバッグ・テスト・ビルド用の名前空間コンテナを生成

書式
--------

**systemd-nspawn** [OPTIONS...] [ *COMMAND* [ARGS...] ]

**systemd-nspawn** --boot [OPTIONS...] [ARGS...]

説明
-----------

**systemd-nspawn** を使うことで軽量な名前空間コンテナの中でコマンドや OS を実行することができます。多くの点で :doc:`chroot.1` と似ていますが、ファイルシステム階層やプロセスツリー、様々な IPC サブシステムやホスト・ドメイン名まで完全に仮想化されるため、chroot よりも強力です。

**systemd-nspawn** は **--directory=** コマンドラインオプションを使うことでオペレーティングシステムツリーを含むあらゆるディレクトリツリーで呼び出すことができます。**--machine=** オプションを使用すると複数の場所から OS ツリーが自動的に検索されます。特にシステムにコンテナイメージを置くときには /var/lib/machines が推奨されています。

:doc:`chroot.1` とは対照的に、**systemd-nspawn** はコンテナの中で完全な Linux ベースのオペレーティングシステムを起動することができます。

**systemd-nspawn** はコンテナの中で様々なカーネルインターフェイスを読み取り専用に制限します。例えば /sys や /proc/sys、/sys/fs/selinux などです。コンテナの中からホストのネットワークインターフェイスやシステムクロックを変更することはできません。デバイスノードも作成不可能です。コンテナの中からホストシステムを再起動したりカーネルモジュールをロードすることも出来ないようになっています。

:doc:`dnf.8` や :doc:`debootstrap.8`、:doc:`pacman.8` などのツールを使うことで **systemd-nspawn** コンテナ用にファイルシステム階層として適した OS ディレクトリツリーをセットアップすることができます。これらのコマンドの実行方法について詳しくはサンプルセクションを見てください。

安全確認として **systemd-nspawn** はコンテナの起動前にコンテナツリーの /usr/lib/os-release や /etc/os-release が存在するか確認します (:doc:`os-release.5` を参照)。コンテナの OS が古すぎて含まれているファイルが古い場合、コンテナツリーに手動でファイルを追加する必要があります。

**systemd-nspawn** はインタラクティブなコマンドラインから直接呼び出すだけでなく、システムサービスとしてバックグラウンドで実行することができます。このモードでは各コンテナのインスタンスは各々サービスインスタンスとして実行されます。簡単に実行できるようにデフォルトのテンプレートユニットファイル systemd-nspawn@.service が存在します。インスタンス識別子としてコンテナの名前を指定します。コマンドラインでインタラクティブに実行するのではなくテンプレートユニットファイルを使って **systemd-nspawn** を起動した場合、異なるデフォルトオプションが適用されるので注意してください。特に重要なこととして、インタラクティブなコマンドラインから **systemd-nspawn** を実行したときはデフォルトではない、**--boot** がテンプレートユニットファイルによって使われます。デフォルトオプションの違いについては、サポートされている様々なオプションと共に下で説明しています。

:doc:`machinectl.1` ツールを使うことで様々なコンテナの操作を行うことができます。特に systemd-nspawn@.service テンプレートユニットファイルを使ってシステムサービスとしてコンテナを実行するときに使いやすいコマンドが揃っています。

各コンテナには拡張子が .nspawn の設定ファイルを作成でき、コンテナを実行する時の追加設定を記述できます。詳しくは :doc:`systemd.nspawn.5` を見てください。設定ファイルは systemd-nspawn@.service テンプレートユニットファイルで使われるデフォルトオプションを上書きするため、通常はテンプレートファイルに直接変更を加える必要はありません。

**systemd-nspawn** はコンテナの秘密のファイルシステムを /dev や /run などにマウントします。コンテナの外からは閲覧することができず、ファイルシステムの中身はコンテナの終了時に消去されます。

同じディレクトリツリーから **systemd-nspawn** コンテナを2つ実行したとしても、互いのコンテナのプロセスはわからないので注意してください。2つのコンテナにおける PID 名前空間の分離は完全であり、起動元のファイルシステム以外にコンテナが共有するランタイムオブジェクトはほとんどありません。実行中のコンテナでログインセッションを追加したいときは :doc:`machinectl.1` の **login** か **shell** コマンドを使ってください。

**systemd-nspawn** は **Container Interface** の仕様を実装しています。

実行時、**systemd-nspawn** で起動したコンテナは :doc:`systemd-machined.8` サービスで登録されてコンテナの実行が追跡されます。:doc:`systemd-machined.8` はコンテナを操作するためのプログラミングインターフェイスを提供します。

オプション
----------

オプション **-b** が指定されると、引数は init プログラムの引数として使われます。指定しなかった場合、*COMMAND* はコンテナの中で起動するプログラムを指定します。残りの引数はプログラムの引数として扱われます。**--boot** を使用せず引数も指定しなかった場合、コンテナの中でシェルが起動します。

以下のオプションを利用できます:

.. option:: -D, --directory=

   コンテナのルートファイルシステムとして使用するディレクトリ。

   **--directory=** も **--image=** も指定しなかった場合、**--machine=** で指定されたマシン名と同じ名前のディレクトリを検索してディレクトリが決定されます。正確な検索パスについては :doc:`machinectl.1` の "Files and Directories" セクションを参照してください。

.. option:: --template=

   コンテナのルートディレクトリのテンプレートとして使用するディレクトリあるいは "btrfs" サブボリューム。このオプションを指定していてコンテナのルートディレクトリ (**--directory=** で指定) が存在しない場合、"btrfs" スナップショット (サポートされている場合) あるいはプレーンディレクトリ (サポートされていない場合) としてディレクトリが作成されてテンプレートツリーからファイルが生成されます。理想的には、指定されたテンプレートパスが "btrfs" サブボリュームのルートだった場合、シンプルな copy-on-write スナップショットが取得され、一瞬でルートディレクトリが作成されます。指定されたテンプレートパスが "btrfs" サブボリュームのルートではなかった場合 (あるいは "btrfs" ファイルシステムでもない場合)、ツリーがコピーされるため (ファイルシステムが copy-on-write をサポートしている場合、copy-on-write が使われる可能性があります)、ディレクトリを作成するのにかかる時間が大幅に増える可能性があります。**--image=** や **--ephemeral** と一緒に指定することはできません。

   このスイッチではホスト名やマシン ID などのインスタンスを識別する設定は変わらないので注意してください。

.. option:: -x, --ephemeral

   指定した場合、ファイルシステムの一時的なスナップショットを使ってコンテナが実行され、コンテナの終了時に即座に消去されます。**--template=** と一緒に指定することはできません。

   このスイッチではホスト名やマシン ID などのインスタンスを識別する設定は変わらないので注意してください。

.. option:: -i, --image=

   コンテナのルートディレクトリをマウントするディスクイメージ。通常のファイルまたはブロックデバイスノードを指定します。ファイルまたはデバイスには以下のいずれかが含まれている必要があります:

   * MBR パーティションテーブルと、タイプ 0x83 で bootable とマークされたシングルパーティション。
   * GUID パーティションテーブル (GPT) と、タイプ 0fc63daf-8483-4772-8e79-3d69d8477de4 のシングルパーティション。
   * GUID パーティションテーブル (GPT) と、コンテナのルートディレクトリとしてマウントされるようマークしたルートパーティション。任意で、GPT イメージにはホーム・サーバーデータパーティションを含めることができ、コンテナの適切な場所にマウントされます。全てのパーティションは **Discoverable Partitions Specification** で定義されているパーティションタイプで識別します。
   * パーティションテーブルなし、イメージ全体にまたがるシングルファイルシステム。

   GPT イメージの場合、EFI システムパーティション (ESP) が発見されると、自動的に /efi (またはフォールバックの /boot) にマウントされます (同名のディレクトリが存在していて空の場合)。

   LUKS で暗号化されたパーティションは自動的に復号化されます。また、GPT イメージでは **--root-hash=** オプションによってハッシュパーティションのルートハッシュが指定されている場合、dm-verity データ整合性ハッシュパーティションが設定されます。

   他のパーティション、不明なパーティションやスワップパーティションなどはマウントされません。**--directory=** や **--template=** と一緒に指定することはできません。

.. option:: --root-hash=

   16進数でデータ整合性 (dm-verity) ルートハッシュを指定します。使用するイメージに適切な整合性データが含まれている場合 (上を参照)、このオプションによって dm-verity によるデータ整合性チェックが有効になります。指定するハッシュは整合性データのルートハッシュと一致している必要があります。通常は256ビット以上です (SHA256 の場合、16進数では64文字になります)。このオプションが指定されなかった場合、イメージファイルに "user.verity.roothash" 拡張ファイル属性が設定されていたときは (:doc:`xattr.7` を参照)、16進数の文字列としてルートハッシュが読み込まれます。拡張ファイル属性がないときは (あるいはファイルシステムによってサポートされていない場合)、イメージファイルと同じディレクトリに .roothash 拡張子のファイルが存在していてファイル名が同じ場合、同じく16進数の文字列として自動的に読み込まれて使用されます。

.. option:: -a, --as-pid2

   PID 1 (init) ではなく ID (PID) 2 プロセスとしてシェルまたは指定したプログラムを起動します。デフォルトでは、このオプションや **--boot** が使われなかった場合、選択したプログラムは PID 1 のプロセスとして実行されます。UNIX では PID 1 は特殊な意味を持ちます。例えば、PID 1 プロセスは親となった全てのプロセスを回収して、**sysvinit** 互換のシグナル処理を実装する必要があります (例えば SIGINT では再起動、SIGTERM では再実行、SIGHUP では設定のリロードなどを行います)。**--as-pid2** を使用すると最小限のスタブ init プロセスが PID 1 で起動して、選択したプログラムは PID 2 で実行されます (特殊な機能を実装する必要がなくなります)。スタブ init プロセスは必要に応じてプロセスを回収してシグナルに反応します。コンテナの中で任意のコマンドを実行するときはこのモードを使用することを推奨します。使用しないときはコマンドを PID 1 として正しく実行できるように改造しなければなりません。つまり、コマンドが init やシェル実装でないかぎり、ほとんど全てのコマンドでこのスイッチを使用するべきです。init やシェルは大抵 PID 1 として実行できるようになっています。このオプションは **--boot** と組み合わせることができません。

.. option:: -b, --boot

   シェルやユーザー指定のプログラムの代わりに、自動的に init プログラムを検索して PID 1 として実行します。このオプションを使用した場合、コマンドラインの引数は init プログラムの引数として使われます。このオプションは **--as-pid2** と組み合わせることができません。

   以下の表は様々な実行モードと **--as-pid2** (上を参照) の関係を説明しています:

   **表 1. 実行モード**

   ================================================= ========================================================================================
   スイッチ                                          説明
   ================================================= ========================================================================================
   **--as-pid2** と **--boot** のどちらも指定しない  指定したパラメータはコマンドラインとして解釈され、コンテナの中で PID 1 として実行される。
   **--as-pid2** を指定する                          指定したパラメータはコマンドラインとして解釈され、コンテナの中で PID 2 として実行される。
                                                     スタブ init プロセスが PID 1 として実行される。
   **--boot** を指定する                             init プログラムが自動的に検索されて、コンテナの中で PID 1 として実行される。
                                                     指定したパラメータはプロセスの実行パラメータとして使用される。
   ================================================= ========================================================================================

   .. note::

      systemd-nspawn@.service テンプレートユニットファイルを使用するときは **--boot** がデフォルトの実行モードです。

.. option:: --chdir=

   コンテナの中でプロセスを実行する前に指定した作業ディレクトリに移動します。コンテナのファイルシステム名前空間の絶対パスで指定します。

.. option:: --pivot-root=

   指定したディレクトリをコンテナの中の / にして、コンテナの古いルートはアンマウントするか、他の指定したディレクトリの中心になります。パスをひとるだけ指定した場合、指定したパスが / になって古いルートはアンマウントされます。もしくは新しいルートパスをコロンで区切って古いルートのマウント先を指定した場合、新しいルートパスが / になり、古い / は別のディレクトリになります。パスはどちらも絶対パスで、コンテナのファイルシステム名前空間で解決されます。

   このオプションはブートするディレクトリが複数存在するコンテナのためにあります。例えば、複数の **OSTree** をデプロイする場合など。通常時にルートとしてマウントするディレクトリを選択してコンテナの PID 1 を起動する、ブートローダーと初期 RAM ディスクの挙動をエミュレートしています。

.. option:: -u, --user=

   コンテナに移行後、コンテナのユーザーデータベースで定義されている指定ユーザーに変わります。他の systemd-nspawn の機能と同じように、これはセキュリティ機能ではなく偶発的に破壊的な操作を行ってしまわないための防護として用意されています。

.. option:: -M, --machine=

   コンテナのマシンの名前を設定します。この名前は実行時に (:doc:`machinectl.1` などのツールで) コンテナを識別するのに使うことができます。また、コンテナのホスト名を初期化するのにも使われます (ただしコンテナによって上書きされる可能性はあります)。指定しなかった場合、コンテナのルートディレクトリのパスの最後の部分が使われます。**--ephemeral** モードが選択されているときはランダムな識別子が後ろに付きます。選択されたルートディレクトリがホストのルートディレクトリの場合はホストのホスト名がデフォルトで使用されます。

サンプル
--------

   **例 1. Fedora のイメージをダウンロードしてシェルを起動**

   .. code-block:: console

      # machinectl pull-raw --verify=no \
            https://download.fedoraproject.org/pub/fedora/linux/releases/25/CloudImages/x86_64/images/Fedora-Cloud-Base-25-1.3.x86_64.raw.xz
      # systemd-nspawn -M Fedora-Cloud-Base-25-1.3.x86_64.raw

   上記のコマンドは :doc:`machinectl.1` を使ってイメージをダウンロードしてシェルを開きます。

   **例 2. コンテナの中に最小限の Fedora ディストリビューションをビルド・起動**

   .. code-block:: console

      # dnf -y --releasever=27 --installroot=/var/lib/machines/f27container \
            --disablerepo='*' --enablerepo=fedora --enablerepo=updates install \
            systemd passwd dnf fedora-release vim-minimal
      # systemd-nspawn -bD /var/lib/machines/f27container

   上記のコマンドは /var/lib/machines/f27container ディレクトリに最小限の Fedora 環境をインストールして名前空間コンテナを使って OS を起動します。インストール先が標準の /var/lib/machines/ ディレクトリの下になっているため、:command:`systemd-nspawn -M f27container` でマシンを起動できます。

   **例 3. 最小限の Debian unstable ディストリビューションのコンテナでシェルを生成**

   .. code-block:: console

      # debootstrap unstable ~/debian-tree/
      # systemd-nspawn -D ~/debian-tree/

   上記のコマンドは :file:`~/debian-tree/` ディレクトリに最小限の Debian unstable ディストリビューションをインストールして名前空間コンテナを使ってシェルを起動します。

   **debootstrap** は **Debian**, **Ubuntu**, **Tanglu** をサポートしているため、同じコマンドを使ってこれらのディストリビューションをインストールできます。Debian ファミリーの他のディストリビューションについては、ミラーを指定する必要があります。:doc:`debootstrap.8` を参照してください。

   **例 4. コンテナで最小限の Arch Linux ディストリビューションを起動**

   .. code-block:: console

      # pacstrap -c -d ~/arch-tree/ base
      # systemd-nspawn -bD ~/arch-tree/

   上記のコマンドは :file:`~/arch-tree/` ディレクトリに最小限の Arch Linux ディストリビューションをインストールして名前空間コンテナを使って OS を起動します。

   **例 5. OpenSUSE Tumbleweed ローリングディストリビューションをインストール**

   .. code-block:: console

      # zypper --root=/var/lib/machines/tumbleweed ar -c \
            https://download.opensuse.org/tumbleweed/repo/oss tumbleweed
      # zypper --root=/var/lib/machines/tumbleweed refresh
      # zypper --root=/var/lib/machines/tumbleweed install --no-recommends \
            systemd shadow zypper openSUSE-release vim
      # systemd-nspawn -M tumbleweed passwd root
      # systemd-nspawn -M tumbleweed -b

   **例 6. ホスト環境の一時的なスナップショットを起動**

   .. code-block:: console

      # systemd-nspawn -D / -xb

   上記のコマンドはホスト環境のスナップショットコピーを起動します。コンテナの終了時にコピーはすぐに消去されます。コンテナの実行時にファイルシステムに変更を行っても全てシャットダウン時に消失します。

   **例 7. SELinux サンドボックスセキュリティコンテキストでコンテナを起動**

   .. code-block:: console

      # chcon system_u:object_r:svirt_sandbox_file_t:s0:c0,c1 -R /srv/container
      # systemd-nspawn -L system_u:object_r:svirt_sandbox_file_t:s0:c0,c1 \
            -Z system_u:system_r:svirt_lxc_net_t:s0:c0,c1 -D /srv/container /bin/sh

   **例 8. OSTree でコンテナを起動**

   .. code-block:: console

      # systemd-nspawn -b -i ~/image.raw \
            --pivot-root=/ostree/deploy/$OS/deploy/$CHECKSUM:/sysroot \
            --bind=+/sysroot/ostree/deploy/$OS/var:/var

終了ステータス
---------------

コンテナの中で実行されたプログラムの終了コードが返ります。

関連項目
--------

:doc:`systemd.1`,
:doc:`systemd.nspawn.5`,
:doc:`chroot.1`,
:doc:`dnf.8`,
:doc:`debootstrap.8`,
:doc:`pacman.8`,
:doc:`zypper.8`,
:doc:`systemd.slice.5`,
:doc:`machinectl.1`,
:doc:`btrfs.8`

注釈
-------

1. Container Interface
      https://www.freedesktop.org/wiki/Software/systemd/ContainerInterface
   
2. Discoverable Partitions Specification
      https://www.freedesktop.org/wiki/Specifications/DiscoverablePartitionsSpec/
   
3. OSTree
      https://ostree.readthedocs.io/en/latest/

4. overlayfs.txt
      https://www.kernel.org/doc/Documentation/filesystems/overlayfs.txt

5. Fedora
      https://getfedora.org

6. Debian
      https://www.debian.org

7. Ubuntu
      https://www.ubuntu.com

8. Tanglu
      https://www.tanglu.org

9. Arch Linux
      https://www.archlinux.jp

10. OpenSUSE Tumbleweed
      https://software.opensuse.org/distributions/tumbleweed
