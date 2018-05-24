amdgpu(4)
==================

名称
--------

amdgpu - AMD RADEON GPU ビデオドライバー

書式
--------

| **Section** **"Device"**
|   **Identifier** *"devname"*
|   **Driver "amdgpu"**
|   ...
| **EndSection**

説明
--------

amdgpu は AMD RADEON が搭載されたビデオカードのための Xorg ドライバーで以下の機能を備えています:

* 24 または 30 ビットのピクセル深度のサポート
* バージョン 1.4 までの RandR のサポート
* 3D アクセラレーション

サポートされているハードウェア
--------------------------------

**amdgpu** ドライバーは SI ファミリー以降のビデオカードをサポートしています。

設定
-----

一般的な設定オプションについては :doc:`xorg.conf.5` を参照してください。このセクションでは **amdgpu** ドライバー固有の設定だけを説明します。

ドライバーは以下の **Option** をサポートしています:

**Option "SWcursor"** *"boolean"*

   ソフトウェアカーソルを選択。デフォルトは **off**。

**Option "Accel"** *"boolean"*

   全てのハードウェアアクセラレーションを有効化または無効化。

   デフォルトは **on**。

**Option "ZaphodHeads"** *"string"*

   特定のドライバーインスタンスで zaphod モードを使用する RandR 出力の指定。このオプションを使うときはドライバーの全てのインスタンスでこのオプションを使う必要があります。

   例: **Option "ZaphodHeads" "LVDS,VGA-0"** で xrandr の出力 LVDS と VGA-0 がドライバーのインスタンスに割り当てられます。

**Option "DRI"** *"integer"*

   有効化する DRI の最大レベルを定義。DRI2 の場合は 2 を、DRI3 の場合は 3 を指定します。Xorg のバージョン 1.18.3 以上ではデフォルトで DRI3 の **3** が使われますが、古いバージョンでは DRI2 の **2** がデフォルトです。

**Option "EnablePageFlip"** *"boolean"*

   DRI2 のページフリッピングを有効化。デフォルトは **on**。

**Option "TearFree"** *"boolean"*

   出力毎の 'TearFree' プロパティのデフォルト値を設定。ハードウェアのページフリッピング機構を使ってちらつきを抑えるかどうか制御します。TearFree が on になっている出力と関連付けられている CRTC では TearFree が on になります。TearFree が on の CRTC にはそれぞれ別のスキャンアウトバッファを割り当てなければなりません。このオプションが設定されている場合、プロパティのデフォルト値が 'on' あるいは 'off' になります。このオプションが設定されていない場合、プロパティのデフォルト値は **auto** になり、回転する出力や RandR の変形が適用されている出力、RandR 1.4 スレーブ出力では TearFree on となり、他の場合は off になります。

**Option "AccelMethod"** *"string"*

   このオプションを **none** に設定すると glamor アクセラレーションアーキテクチャが使われなくなります。その場合、全ての 2D レンダリングは CPU によって行われるようになりますが、3D と動画のハードウェアアクセラレーションは動作します。主として OpenGL ドライバーを使いたい場合に使用します。

   デフォルトでは glamor が使用されます。

以下は **glamor** で使用できる **Option** です:

**Option "ShadowPrimary"** *"boolean"*

   このオプションはいわゆる「シャドウプライマリ」バッファを有効にして CPU からピクセルデータに高速にアクセスできるようにして、ディスプレイコントローラ (CRTC) ごとに別々のスキャンアウトバッファを使います。一部の 2D ワークロードのパフォーマンスが向上しますが、他のワークロード (3D や動画など) は遅くなる可能性があります。このオプションを有効にするとページフリッピングが無効化されます。デフォルトは **off**。

参照
------

:doc:`Xorg.1`,
:doc:`xorg.conf.5`,
:doc:`Xserver.1`,
:doc:`X.7`

1. | Wiki ページ:
   | https://www.x.org/wiki/radeon
2. | amdgpu の開発コードの概要:
   | https://cgit.freedesktop.org/xorg/driver/xf86-video-amdgpu/
3. | メーリングリスト:
   | https://lists.freedesktop.org/mailman/listinfo/amd-gfx
4. | IRC チャンネル:
   | #radeon on irc.freenode.net
5. | amdgpu のバグトラッカー:
   | https://bugs.freedesktop.org/query.cgi?product=xorg&component=Driver/AMDgpu
6. | バグとパッチの投稿:
   | https://bugs.freedesktop.org/enter_bug.cgi?product=xorg&component=Driver/AMDgpu

著者
-----

| 著者一覧:
| Michel Dänzer             michel@daenzer.net
| Alex Deucher              alexdeucher@gmail.com
