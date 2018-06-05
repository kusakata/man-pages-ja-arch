systemd(1)
==================

名称
--------

systemd, init - systemd システム・サービスマネージャ

書式
--------

| **/usr/lib/systemd/systemd** [OPTIONS...]
| **init** [OPTIONS...] {COMMAND}

説明
-----------

systemd は Linux オペレーティングシステム用のシステム・サービスマネージャです。起動したときの最初のプロセス (PID 1) として実行することで、ユーザー空間のサービスを立ち上げたり管理する init システムとして機能します。

SysV との互換性を保つため、systemd を **init** として呼び出したときに PID が 1 ではない場合、**telinit** を実行して全てのコマンドライン引数をそのまま渡します。通常のログインセッションから呼び出したときは **init** も **telinit** もほとんど同じとなります。詳しくは :doc:`telinit.8` を参照。

システムインスタンスとして実行した場合、systemd は system.conf 設定ファイルと system.conf.d ディレクトリのファイルを読み込みます。ユーザーインスタンスとして実行した場合、systemd は user.conf 設定ファイルと user.conf.d ディレクトリのファイルを読み込みます。詳しくは :doc:`systemd-system.conf.5` を参照してください。

オプション
----------

以下のオプションを使うことができます:

.. option:: --test

   起動シーケンスを確認して、ダンプして終了します。デバッグのときに役立つオプションです。

.. option:: --dump-configuration-items

   使用できるユニット設定アイテムをダンプします。ユニット定義アイテムで使える設定アイテムの簡潔ながら網羅的なリストを出力します。

.. option:: --unit=

   起動時にアクティベートするデフォルトユニットを設定します。指定しなかった場合、デフォルトで default.target が使われます。

.. option:: --system, --user

   **--system** を指定した場合、プロセス ID が 1 ではない (systemd を init プロセスとして実行しない) 場合でも systemd はシステムインスタンスを実行します。**--user** は逆に、プロセス ID が 1 の場合でもユーザーインスタンスを実行します。通常はこれらのオプションを指定する必要はなく、systemd は自動的に起動するべきモードを認識します。デバッグ以外では使う可能性がほとんどないオプションとなります。PID が 1 ではないのに **--system** モードで systemd を動作させシステムを起動・管理することはサポートされないので注意してください。基本的に :option:`--test` と組み合わせる場合以外で **--system** を明示的に指定する意味はありません。

.. option:: --dump-core

   クラッシュ時のコアダンプを有効にします。ユーザーインスタンスとして実行する場合、このスイッチは効果を持ちません。この設定は起動時にカーネルコマンドラインで *systemd.dump_core=* オプションを使って有効にすることもできます。下を参照。

.. option:: --crash-vt=VT

   クラッシュ時に特定の仮想端末 (VT) に切り替えます。1-63 の範囲の正数値か論理値で指定します。正数を指定した場合、指定した VT に切り替わります。**yes** を指定した場合、カーネルメッセージが書き込まれる VT が選択されます。**no** の場合、VT の切り替えは行われません。ユーザーインスタンスとして実行している場合はこのスイッチは効果を持ちません。カーネルコマンドラインで *systemd.crash_vt=* オプションを使うことで起動時に設定を有効にすることもできます。下を参照。

.. option:: --crash-shell

   クラッシュ時にシェルを起動します。ユーザーインスタンスとして実行している場合はこのスイッチは効果を持ちません。カーネルコマンドラインで *systemd.crash_shell=* オプションを使うことで起動時に設定を有効にすることもできます。下を参照。

.. option:: --crash-reboot

   クラッシュ時にシステムを自動的に再起動します。ユーザーインスタンスとして実行している場合はこのスイッチは効果を持ちません。カーネルコマンドラインで *systemd.crash_reboot=* オプションを使うことで起動時に設定を有効にすることもできます。下を参照。

.. option:: --confirm-spawn

   プロセスを生成するときに確認を要求します。ユーザーインスタンスとして実行している場合はこのスイッチは効果を持ちません。

.. option:: --show-status=

   論理引数あたいは特殊値 **auto** を指定します。on の場合、起動時・シャットダウン時にコンソールにユニットの状態情報が簡潔に表示されます。off の場合、状態情報は表示されません。**auto** に設定した場合の挙動は off と似ていますが、ユニットの実行が失敗したり起動に時間がかかっている場合などに自動的に on に切り替わります。ユーザーインスタンスとして実行している場合はこのスイッチは効果を持ちません。指定した場合、カーネルコマンドラインの systemd.show_status= 設定 (下を参照) と設定ファイルのオプション **ShowStatus=** が上書きされます。:doc:`systemd-system.conf.5` を参照。

.. option:: --log-target=

   ログターゲットを設定します。引数は **console**, **journal**, **kmsg**, **journal-or-kmsg**, **null** のどれかである必要があります。

.. option:: --log-level=

   ログレベルを設定します。数字のログレベルあるいは :doc:`syslog.3` のシンボル名 (小文字) を引数として指定できます: **emerg**, **alert**, **crit**, **err**, **warning**, **notice**, **info**, **debug**。

.. option:: --log-color=

   重要なログメッセージをハイライト表示します。引数は論理値です。引数を省略した場合、デフォルトでは **true** になります。

.. option:: --log-location=

   ログメッセージにコードの位置を含めます。主としてデバッグ用のオプションです。引数は論理値です。引数を省略した場合はデフォルトで **true** となります。

.. option:: --default-standard-output=, --default-standard-error=

   全てのサービスとソケットについてデフォルト出力・エラー出力を設定します。**StandardOutput=** と **StandardError=** のデフォルトを制御します (詳しくは :doc:`systemd.exec.5` を参照)。**inherit**, **null**, **tty**, **journal**, **journal+console**, **syslog**, **syslog+console**, **kmsg**, **kmsg+console** のどれかで指定します。引数を省略した場合は **--default-standard-output=** のデフォルトは **journal** に、**--default-standard-error=** のデフォルトは **inherit** になります。

.. option:: --machine-id=

   ハードドライブに設定された machine-id を上書きします。ネットワークブートやコンテナで役に立つオプションです。全てをゼロに設定することはできません。

.. option:: --service-watchdogs=

   全てのサービスのウォッチドッグタイムアウトと緊急アクションをグローバルに有効化・無効化します。この設定は起動時にカーネルコマンドラインで *systemd.service_watchdogs=* オプションを使って指定することも可能です。下を参照。デフォルトは enabled です。

.. option:: -h, --help

   短いヘルプテキストを出力して終了します。

.. option:: --version

   短いバージョン文字列を出力して終了します。

概念
-----------

systemd は11の異なるタイプの「ユニット」と呼ばれるエンティティ間の依存システムを提供します。ユニットではシステムの起動やメンテナンスに関連する様々なオブジェクトがカプセル化されています。ユニットの多くはユニット設定ファイルで設定を行います。設定構文や基本的なオプションについては :doc:`systemd.unit.5` で説明していますが、他の設定から自動的に作成されたり、システムの状態や実行時にプログラムに従って動的に生成されるユニットも存在します。ユニットには "active" 状態 (起動済み・バインド済み・接続済みなどユニットのタイプによって意味は変わります、下を参照) と "inactive" 状態 (停止済み・バインド解除・未接続...) があり、さらにそのふたつの状態に遷移する途中の中間状態が存在します ("activating" または "deactivating" と呼ばれます)。また、特殊な "failed" 状態も存在します。"failed" は "inactive" とよく似ており、何らかの理由でサービスの実行が失敗した場合 (プロセスがエラーコードで終了した、クラッシュした、操作がタイムアウトした、何度も再起動が発生している、など) に遷移します。この状態になったときは、後で確認できるように原因がログに保存されます。ユニットタイプによってはさらに他の状態が存在する場合があり、上記の一般的な5つのユニット状態にマッピングされます。

ユニットタイプは以下が存在します:

   1. サービスユニット。サービスを構成するデーモンやプロセスを起動・制御します。詳しくは :doc:`systemd.service.5` を参照。

   2. Socket units, which encapsulate local IPC or network sockets in the system, useful for socket-based activation. For details about socket units, see systemd.socket(5), for details on socket-based activation and other forms of activation, see daemon(7).

   3. Target units are useful to group units, or provide well-known synchronization points during boot-up, see systemd.target(5).

   4. Device units expose kernel devices in systemd and may be used to implement device-based activation. For details, see systemd.device(5).

   5. Mount units control mount points in the file system, for details see systemd.mount(5).

   6. Automount units provide automount capabilities, for on-demand mounting of file systems as well as parallelized boot-up. See systemd.automount(5).

   7. Timer units are useful for triggering activation of other units based on timers. You may find details in systemd.timer(5).

   8. Swap units are very similar to mount units and encapsulate memory swap partitions or files of the operating system. They are described in systemd.swap(5).

   9. Path units may be used to activate other services when file system objects change or are modified. See systemd.path(5).

   10. Slice units may be used to group units which manage system processes (such as service and scope units) in a hierarchical tree for resource management purposes. See systemd.slice(5).

   11. Scope units are similar to service units, but manage foreign processes instead of starting them as well. See systemd.scope(5).

Units are named as their configuration files. Some units have special semantics. A detailed list is available in systemd.special(7).

systemd knows various kinds of dependencies, including positive and negative requirement dependencies (i.e. Requires= and Conflicts=) as well as ordering dependencies ( After= and Before=). NB: ordering and requirement dependencies are orthogonal. If only a requirement dependency exists between two units (e.g. foo.service requires bar.service), but no ordering dependency (e.g. foo.service after bar.service) and both are requested to start, they will be started in parallel. It is a common pattern that both requirement and ordering dependencies are placed between two units. Also note that the majority of dependencies are implicitly created and maintained by systemd. In most cases, it should be unnecessary to declare additional dependencies manually, however it is possible to do this.

Application programs and units (via dependencies) may request state changes of units. In systemd, these requests are encapsulated as 'jobs' and maintained in a job queue. Jobs may succeed or can fail, their execution is ordered based on the ordering dependencies of the units they have been scheduled for.

On boot systemd activates the target unit default.target whose job is to activate on-boot services and other on-boot units by pulling them in via dependencies. Usually, the unit name is just an alias (symlink) for either graphical.target (for fully-featured boots into the UI) or multi-user.target (for limited console-only boots for use in embedded or server environments, or similar; a subset of graphical.target). However, it is at the discretion of the administrator to configure it as an alias to any other target unit. See systemd.special(7) for details about these target units.

Processes systemd spawns are placed in individual Linux control groups named after the unit which they belong to in the private systemd hierarchy. (see cgroups.txt [#]_ for more information about control groups, or short "cgroups"). systemd uses this to effectively keep track of processes. Control group information is maintained in the kernel, and is accessible via the file system hierarchy (beneath /sys/fs/cgroup/systemd/), or in tools such as systemd-cgls(1) or ps(1) ( ps xawf -eo pid,user,cgroup,args is particularly useful to list all processes and the systemd units they belong to.).

systemd is compatible with the SysV init system to a large degree: SysV init scripts are supported and simply read as an alternative (though limited) configuration file format. The SysV /dev/initctl interface is provided, and compatibility implementations of the various SysV client tools are available. In addition to that, various established Unix functionality such as /etc/fstab or the utmp database are supported.

systemd has a minimal transaction system: if a unit is requested to start up or shut down it will add it and all its dependencies to a temporary transaction. Then, it will verify if the transaction is consistent (i.e. whether the ordering of all units is cycle-free). If it is not, systemd will try to fix it up, and removes non-essential jobs from the transaction that might remove the loop. Also, systemd tries to suppress non-essential jobs in the transaction that would stop a running service. Finally it is checked whether the jobs of the transaction contradict jobs that have already been queued, and optionally the transaction is aborted then. If all worked out and the transaction is consistent and minimized in its impact it is merged with all already outstanding jobs and added to the run queue. Effectively this means that before executing a requested operation, systemd will verify that it makes sense, fixing it if possible, and only failing if it really cannot work.

systemd contains native implementations of various tasks that need to be executed as part of the boot process. For example, it sets the hostname or configures the loopback network device. It also sets up and mounts various API file systems, such as /sys or /proc.

For more information about the concepts and ideas behind systemd, please refer to the Original Design Document [#]_.

Note that some but not all interfaces provided by systemd are covered by the Interface Stability Promise [#]_.

Units may be generated dynamically at boot and system manager reload time, for example based on other configuration files or parameters passed on the kernel command line. For details, see systemd.generator(7).

Systems which invoke systemd in a container or initrd environment should implement the Container Interface [#]_ or initrd Interface [#]_ specifications, respectively.

ディレクトリ
-------------

システムユニットディレクトリ
   The systemd system manager reads unit configuration from various directories. Packages that want to install unit files shall place them in the directory returned by pkg-config systemd --variable=systemdsystemunitdir. Other directories checked are /usr/local/lib/systemd/system and /usr/lib/systemd/system. User configuration always takes precedence. pkg-config systemd --variable=systemdsystemconfdir returns the path of the system configuration directory. Packages should alter the content of these directories only with the enable and disable commands of the systemctl(1) tool. Full list of directories is provided in systemd.unit(5).

ユーザーユニットディレクトリ
   Similar rules apply for the user unit directories. However, here the XDG Base Directory specification [6]_ is followed to find units. Applications should place their unit files in the directory returned by pkg-config systemd --variable=systemduserunitdir. Global configuration is done in the directory reported by pkg-config systemd --variable=systemduserconfdir. The enable and disable commands of the systemctl(1) tool can handle both global (i.e. for all users) and private (for one user) enabling/disabling of units. Full list of directories is provided in systemd.unit(5).

SysV init スクリプトディレクトリ
   The location of the SysV init script directory varies between distributions. If systemd cannot find a native unit file for a requested service, it will look for a SysV init script of the same name (with the .service suffix removed).

SysV ランレベルリンクファームディレクトリ
   The location of the SysV runlevel link farm directory varies between distributions. systemd will take the link farm into account when figuring out whether a service shall be enabled. Note that a service unit with a native unit configuration file cannot be started by activating it in the SysV runlevel link farm.

シグナル
----------

SIGTERM
   Upon receiving this signal the systemd system manager serializes its state, reexecutes itself and deserializes the saved state again. This is mostly equivalent to systemctl daemon-reexec.

   systemd user managers will start the exit.target unit when this signal is received. This is mostly equivalent to systemctl --user start exit.target --job-mode=replace-irreversible.

SIGINT
   Upon receiving this signal the systemd system manager will start the ctrl-alt-del.target unit. This is mostly equivalent to systemctl start ctrl-alt-del.target --job-mode=replace-irreversible. If this signal is received more than 7 times per 2s, an immediate reboot is triggered. Note that pressing Ctrl-Alt-Del on the console will trigger this signal. Hence, if a reboot is hanging, pressing Ctrl-Alt-Del more than 7 times in 2s is a relatively safe way to trigger an immediate reboot.

   systemd user managers treat this signal the same way as SIGTERM.

SIGWINCH
   When this signal is received the systemd system manager will start the kbrequest.target unit. This is mostly equivalent to systemctl start kbrequest.target.

   This signal is ignored by systemd user managers.

SIGPWR
   When this signal is received the systemd manager will start the sigpwr.target unit. This is mostly equivalent to systemctl start sigpwr.target.

SIGUSR1
   When this signal is received the systemd manager will try to reconnect to the D-Bus bus.

SIGUSR2
   When this signal is received the systemd manager will log its complete state in human-readable form. The data logged is the same as printed by systemd-analyze dump.

SIGHUP
   Reloads the complete daemon configuration. This is mostly equivalent to systemctl daemon-reload.

SIGRTMIN+0
   Enters default mode, starts the default.target unit. This is mostly equivalent to systemctl isolate default.target.

SIGRTMIN+1
   Enters rescue mode, starts the rescue.target unit. This is mostly equivalent to systemctl isolate rescue.target.

SIGRTMIN+2
   Enters emergency mode, starts the emergency.service unit. This is mostly equivalent to systemctl isolate emergency.service.

SIGRTMIN+3
   Halts the machine, starts the halt.target unit. This is mostly equivalent to systemctl start halt.target --job-mode=replace-irreversible.

SIGRTMIN+4
   Powers off the machine, starts the poweroff.target unit. This is mostly equivalent to systemctl start poweroff.target --job-mode=replace-irreversible.

SIGRTMIN+5
   Reboots the machine, starts the reboot.target unit. This is mostly equivalent to systemctl start reboot.target --job-mode=replace-irreversible.

SIGRTMIN+6
   Reboots the machine via kexec, starts the kexec.target unit. This is mostly equivalent to systemctl start kexec.target --job-mode=replace-irreversible.

SIGRTMIN+13
   Immediately halts the machine.

SIGRTMIN+14
   Immediately powers off the machine.

SIGRTMIN+15
   Immediately reboots the machine.

SIGRTMIN+16
   Immediately reboots the machine with kexec.

SIGRTMIN+20
   Enables display of status messages on the console, as controlled via systemd.show_status=1 on the kernel command line.

SIGRTMIN+21
   Disables display of status messages on the console, as controlled via systemd.show_status=0 on the kernel command line.

SIGRTMIN+22, SIGRTMIN+23
   Sets the log level to "debug" (or "info" on SIGRTMIN+23), as controlled via systemd.log_level=debug (or systemd.log_level=info on SIGRTMIN+23) on the kernel command line.

SIGRTMIN+24
   Immediately exits the manager (only available for --user instances).

SIGRTMIN+26, SIGRTMIN+27, SIGRTMIN+28
   Sets the log target to "journal-or-kmsg" (or "console" on SIGRTMIN+27, "kmsg" on SIGRTMIN+28), as controlled via systemd.log_target=journal-or-kmsg (or systemd.log_target=console on SIGRTMIN+27 or systemd.log_target=kmsg on SIGRTMIN+28) on the kernel command line.

環境変数
----------

.. envvar:: $SYSTEMD_LOG_LEVEL

   systemd reads the log level from this environment variable. This can be overridden with --log-level=.

.. envvar:: $SYSTEMD_LOG_TARGET

   systemd reads the log target from this environment variable. This can be overridden with --log-target=.

.. envvar:: $SYSTEMD_LOG_COLOR

   Controls whether systemd highlights important log messages. This can be overridden with --log-color=.

.. envvar:: $SYSTEMD_LOG_LOCATION

   Controls whether systemd prints the code location along with log messages. This can be overridden with --log-location=.

.. envvar:: $XDG_CONFIG_HOME, $XDG_CONFIG_DIRS, $XDG_DATA_HOME, $XDG_DATA_DIRS

   The systemd user manager uses these variables in accordance to the XDG Base Directory specification [6]_ to find its configuration.

.. envvar:: $SYSTEMD_UNIT_PATH

   Controls where systemd looks for unit files.

.. envvar:: $SYSTEMD_SYSVINIT_PATH

   Controls where systemd looks for SysV init scripts.

.. envvar:: $SYSTEMD_SYSVRCND_PATH

   Controls where systemd looks for SysV init script runlevel link farms.

.. envvar:: $SYSTEMD_COLORS

   The value must be a boolean. Controls whether colorized output should be generated. This can be specified to override the decision that systemd makes based on $TERM and what the console is connected to.

.. envvar:: $LISTEN_PID, $LISTEN_FDS, $LISTEN_FDNAMES

   Set by systemd for supervised processes during socket-based activation. See sd_listen_fds(3) for more information.

.. envvar:: $NOTIFY_SOCKET

   Set by systemd for supervised processes for status and start-up completion notification. See sd_notify(3) for more information.

カーネルコマンドライン
-----------------------

When run as system instance systemd parses a number of kernel command line arguments [7]_:

systemd.unit=, rd.systemd.unit=
   Overrides the unit to activate on boot. Defaults to default.target. This may be used to temporarily boot into a different boot unit, for example rescue.target or emergency.service. See systemd.special(7) for details about these units. The option prefixed with "rd." is honored only in the initial RAM disk (initrd), while the one that is not prefixed only in the main system.

systemd.dump_core
   Takes a boolean argument or enables the option if specified without an argument. If enabled, the systemd manager (PID 1) dumps core when it crashes. Otherwise, no core dump is created. Defaults to enabled.

systemd.crash_chvt
   Takes a positive integer, or a boolean argument. Can be also specified without an argument, with the same effect as a positive boolean. If a positive integer (in the range 1–63) is specified, the system manager (PID 1) will activate the specified virtual terminal (VT) when it crashes. Defaults to disabled, meaning that no such switch is attempted. If set to enabled, the VT the kernel messages are written to is selected.

systemd.crash_shell
   Takes a boolean argument or enables the option if specified without an argument. If enabled, the system manager (PID 1) spawns a shell when it crashes, after a 10s delay. Otherwise, no shell is spawned. Defaults to disabled, for security reasons, as the shell is not protected by password authentication.

systemd.crash_reboot
   Takes a boolean argument or enables the option if specified without an argument. If enabled, the system manager (PID 1) will reboot the machine automatically when it crashes, after a 10s delay. Otherwise, the system will hang indefinitely. Defaults to disabled, in order to avoid a reboot loop. If combined with systemd.crash_shell, the system is rebooted after the shell exits.

systemd.confirm_spawn
   Takes a boolean argument or a path to the virtual console where the confirmation messages should be emitted. Can be also specified without an argument, with the same effect as a positive boolean. If enabled, the system manager (PID 1) asks for confirmation when spawning processes using /dev/console. If a path or a console name (such as "ttyS0") is provided, the virtual console pointed to by this path or described by the give name will be used instead. Defaults to disabled.

systemd.service_watchdogs=
   Takes a boolean argument. If disabled, all service runtime watchdogs ( WatchdogSec=) and emergency actions (e.g. OnFailure= or StartLimitAction=) are ignored by the system manager (PID 1); see systemd.service(5). Defaults to enabled, i.e. watchdogs and failure actions are processed normally. The hardware watchdog is not affected by this option.

systemd.show_status
   Takes a boolean argument or the constant auto. Can be also specified without an argument, with the same effect as a positive boolean. If enabled, the systemd manager (PID 1) shows terse service status updates on the console during bootup. auto behaves like false until a unit fails or there is a significant delay in boot. Defaults to enabled, unless quiet is passed as kernel command line option, in which case it defaults to auto. If specified overrides the system manager configuration file option ShowStatus=, see systemd-system.conf(5). However, the process command line option --show-status= takes precedence over both this kernel command line option and the configuration file option.

systemd.log_target=, systemd.log_level=, systemd.log_location=, systemd.log_color
   Controls log output, with the same effect as the $SYSTEMD_LOG_TARGET, $SYSTEMD_LOG_LEVEL, $SYSTEMD_LOG_LOCATION, $SYSTEMD_LOG_COLOR environment variables described above. systemd.log_color can be specified without an argument, with the same effect as a positive boolean.

systemd.default_standard_output=, systemd.default_standard_error=
   Controls default standard output and error output for services, with the same effect as the --default-standard-output= and --default-standard-error= command line arguments described above, respectively.

systemd.setenv=
   Takes a string argument in the form VARIABLE=VALUE. May be used to set default environment variables to add to forked child processes. May be used more than once to set multiple variables.

systemd.machine_id=
   Takes a 32 character hex value to be used for setting the machine-id. Intended mostly for network booting where the same machine-id is desired for every boot.

systemd.unified_cgroup_hierarchy
   When specified without an argument or with a true argument, enables the usage of unified cgroup hierarchy [8]_ (a.k.a. cgroups-v2). When specified with a false argument, fall back to hybrid or full legacy cgroup hierarchy.

   If this option is not specified, the default behaviour is determined during compilation (the --with-default-hierarchy= option). If the kernel does not support unified cgroup hierarchy, the legacy hierarchy will be used even if this option is specified.

systemd.legacy_systemd_cgroup_controller
   Takes effect if the full unified cgroup hierarchy is not used (see previous option). When specified without an argument or with a true argument, disables the use of "hybrid" cgroup hierarchy (i.e. a cgroups-v2 tree used for systemd, and legacy cgroup hierarchy [9]_, a.k.a. cgroups-v1, for other controllers), and forces a full "legacy" mode. When specified with a false argument, enables the use of "hybrid" hierarchy.

   If this option is not specified, the default behaviour is determined during compilation (the --with-default-hierarchy= option). If the kernel does not support unified cgroup hierarchy, the legacy hierarchy will be used even if this option is specified.

quiet
   Turn off status output at boot, much like systemd.show_status=false would. Note that this option is also read by the kernel itself and disables kernel log output. Passing this option hence turns off the usual output from both the system manager and the kernel.

debug
   Turn on debugging output. This is equivalent to systemd.log_level=debug. Note that this option is also read by the kernel itself and enables kernel debug output. Passing this option hence turns on the debug output from both the system manager and the kernel.

emergency, rd.emergency, -b
   Boot into emergency mode. This is equivalent to systemd.unit=emergency.target or rd.systemd.unit=emergency.target, respectively, and provided for compatibility reasons and to be easier to type.

rescue, rd.rescue, single, s, S, 1
   Boot into rescue mode. This is equivalent to systemd.unit=rescue.target or rd.systemd.unit=rescue.target, respectively, and provided for compatibility reasons and to be easier to type.

2, 3, 4, 5
   Boot into the specified legacy SysV runlevel. These are equivalent to systemd.unit=runlevel2.target, systemd.unit=runlevel3.target, systemd.unit=runlevel4.target, and systemd.unit=runlevel5.target, respectively, and provided for compatibility reasons and to be easier to type.

locale.LANG=, locale.LANGUAGE=, locale.LC_CTYPE=, locale.LC_NUMERIC=, locale.LC_TIME=, locale.LC_COLLATE=, locale.LC_MONETARY=, locale.LC_MESSAGES=, locale.LC_PAPER=, locale.LC_NAME=, locale.LC_ADDRESS=, locale.LC_TELEPHONE=, locale.LC_MEASUREMENT=, locale.LC_IDENTIFICATION=
   Set the system locale to use. This overrides the settings in /etc/locale.conf. For more information, see locale.conf(5) and locale(7).

For other kernel command line parameters understood by components of the core OS, please refer to kernel-command-line(7).

ソケットと FIFO
------------------

/run/systemd/notify
   Daemon status notification socket. This is an AF_UNIX datagram socket and is used to implement the daemon notification logic as implemented by sd_notify(3).

/run/systemd/private
   Used internally as communication channel between systemctl(1) and the systemd process. This is an AF_UNIX stream socket. This interface is private to systemd and should not be used in external projects.

/dev/initctl
   Limited compatibility support for the SysV client interface, as implemented by the systemd-initctl.service unit. This is a named pipe in the file system. This interface is obsolete and should not be used in new applications.

関連項目
--------

**systemd ホームページ** [10]_,
:doc:`systemd-system.conf.5`,
:doc:`locale.conf.5`,
:doc:`systemctl.1`,
:doc:`journalctl.1`,
:doc:`systemd-notify.1`,
:doc:`daemon.7`,
:doc:`sd-daemon.3`,
:doc:`systemd.unit.5`,
:doc:`systemd.special.5`,
:doc:`pkg-config.1`,
:doc:`kernel-command-line.7`,
:doc:`bootup.7`,
:doc:`systemd.directives.7`

注釈
-------

.. [#] https://www.kernel.org/doc/Documentation/cgroup-v1/cgroups.txt
.. [#] http://0pointer.de/blog/projects/systemd.html
.. [#] https://www.freedesktop.org/wiki/Software/systemd/InterfaceStabilityPromise
.. [#] https://www.freedesktop.org/wiki/Software/systemd/ContainerInterface
.. [#] https://www.freedesktop.org/wiki/Software/systemd/InitrdInterface
.. [#] http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
.. [#] If run inside a Linux container these arguments may be passed as command line arguments to systemd itself, next to any of the command line options listed in the Options section above. If run outside of Linux containers, these arguments are parsed from /proc/cmdline instead.
.. [#] https://www.kernel.org/doc/Documentation/cgroup-v2.txt
.. [#] https://www.kernel.org/doc/Documentation/cgroup-v1/
.. [#] https://www.freedesktop.org/wiki/Software/systemd/
