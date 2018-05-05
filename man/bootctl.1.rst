bootctl(1)
==================

名称
--------

bootctl - ファームウェアとブートマネージャの設定を制御

書式
--------

**bootctl** **[OPTIONS...]** **status**

**bootctl** **[OPTIONS...]** **list**

**bootctl** **[OPTIONS...]** **update**

**bootctl** **[OPTIONS...]** **install**

**bootctl** **[OPTIONS...]** **remove**

説明
-----------

**bootctl** は現在のシステムのブートローダーをチェック・アップデート・インストール・削除します。

**bootctl status** はブートローダーバイナリのインストールバージョンと全ての EFI ブート変数をチェック・出力します。

**bootctl list** は設定されているブートローダーのエントリを全て表示します。

**bootctl update** は EFI システムパーティションにインストールされているバージョンよりも現在のバージョンが新しい場合、インストールされているバージョンの systemd-boot をアップデートします。/EFI/BOOT/BOOT*.EFI に存在する EFI のデフォルト・フォールバックローダーもアップデートされます。エントリが存在しない場合、EFI ブート変数に systemd-boot エントリが作成されます。作成されたエントリはブート順序リストの一番末尾に追加されます。

**bootctl install** は EFI システムパーティションに systemd-boot をインストールします。systemd-boot のコピーが /EFI/BOOT/BOOT*.EFI に EFI デフォルト・フォールバックローダーとして保存されます。EFI ブート変数に systemd-boot エントリが作成されブート順序リストの一番上に追加されます。

**bootctl remove** は EFI システムパーティションからインストール済みの systemd-boot を削除します。

コマンドを指定しなかった場合、**status** として実行されます。

オプション
----------

以下のオプションを利用することができます:

.. option:: -h, --help

   短いヘルプテキストを表示して終了します。

.. option:: --version

   短いバージョン文字列を表示して終了します。

.. option:: --path=

   EFI システムパーティション (ESP) のパスを指定します。指定しなかった場合 /efi, /boot, /boot/efi がこの順番でチェックされます。できるかぎり ESP は /boot にマウントすることが推奨されます。

.. option:: -p, --print-path

   このオプションは **status** の挙動を変えます。標準出力に EFI システムパーティション (ESP) のパスだけ出力して終了するようになります。

.. option:: --no-variables

   EFI ブート変数を変更しません。

終了ステータス
----------------

成功時には 0 が返ります。失敗時にはゼロ以外の値が返ります。

参照
--------

**Boot loader specification** [#]_, **systemd boot loader interface** [#]_

脚注
----------

.. [#] https://www.freedesktop.org/wiki/Specifications/BootLoaderSpec
.. [#] https://www.freedesktop.org/wiki/Software/systemd/BootLoaderInterface
