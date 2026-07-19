# TODO:
# - db_oracle
# - launch_darkly
# - rtp.io (needs patch for shared librtpproxy)
# - system wolfssl in tls_wolfssl module
#
# Conditional build:
%bcond_without	radius		# radius aaa support
%bcond_without	aws		# AWS services support (DynamoDB cachedb, SQS event)
%bcond_with	couchbase	# couchbase cachedb support
%bcond_without	memcached	# memcached cachedb support
%bcond_with	mongodb		# mongodb cachedb support
%bcond_without	redis		# Redis cachedb support
%bcond_without	mysql		# MySQL DB support
%bcond_without	pgsql		# PostgreSQL DB support
%bcond_without	sqlite		# Sqlite3 DB support
%bcond_without	odbc		# ODBC DB support
%bcond_without	kafka		# Apache Kafka event support
%bcond_without	rabbitmq	# Rabbit MQ event support
%bcond_without	carrierroute	# carrierroute support
%bcond_without	http2		# HTTP/2 support
%bcond_without	json		# JSON support (multiple modules)
%bcond_without	geoip		# MaxMind GeoIP support
%bcond_with	launchdarkly	# Launch Darkly support
%bcond_without	ldap		# LDAP support
%bcond_without	microhttpd	# httpd support
%bcond_with	osp		# ETSI OSP VoIP Peering support
%bcond_with	rtpproxy	# rtpproxy support (rtp.io module)
%bcond_with	sngtc		# Sangoma transcoding module support
%bcond_with	wolfssl		# WolfSSL tls support (builds internal WolfSSL :( )

Summary:	SIP proxy, redirect and registrar server
Summary(pl.UTF-8):	Serwer SIP przekazujący (proxy), przekierowujący i rejestrujący
Name:		opensips
Version:	3.6.7
Release:	1
License:	GPL v2
Group:		Networking/Daemons
Source0:	https://opensips.org/pub/opensips/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c94e57be3992d77e2e0969a59e0d9341
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.service
Patch0:		x32.patch
URL:		https://opensips.org/
%{?with_osp:BuildRequires:	OSPToolkit}
%{?with_sngtc:BuildRequires:    TODO-SNGTC-BRs}
%{?with_aws:BuildRequires:	aws-sdk-cpp-devel}
BuildRequires:	bison
BuildRequires:	curl-devel
BuildRequires:	db-devel
# for jabber/xmpp
BuildRequires:	expat-devel
BuildRequires:	flex
%{?with_redis:BuildRequires:	hiredis-devel}
%{?with_json:BuildRequires:	json-c-devel}
%{?with_launchdarkly:BuildRequires:	launchdarkly-c-client-sdk-devel}
%{?with_carrierroute:BuildRequires:	libconfuse-devel}
%{?with_couchbase:BuildRequires:    libcouchbase-devel}
%{?with_http2:BuildRequires:	libevent-devel}
%{?with_geoip:BuildRequires:	libmaxminddb-devel}
%{?with_memcached:BuildRequires:	libmemcached-devel}
%{?with_microhttpd:BuildRequires:	libmicrohttpd-devel}
BuildRequires:	libmnl-devel
%{?with_kafka:BuildRequires:	librdkafka-devel}
%{?with_rtpproxy:BuildRequires:	librtpproxy-devel}
BuildRequires:	libsctp-devel
%{?with_osp:BuildRequires:	libutf8proc-devel}
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-progs
BuildRequires:	lua54-devel >= 5.4
#BuildRequires:	lynx
%{?with_mongodb:BuildRequires:	mongo-c-driver-devel >= 1.0}
%{?with_mysql:BuildRequires:	mysql-devel}
BuildRequires:	net-snmp-devel
%{?with_http2:BuildRequires:	nghttp2-devel >= 1.62.1}
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	pcre2-8-devel
BuildRequires:	perl-devel
BuildRequires:	perl-tools-devel
BuildRequires:	pkgconfig
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	python-devel >= 1:2.5
%{?with_rabbitmq:BuildRequires:	rabbitmq-c-devel}
%{?with_radius:BuildRequires:	radiusclient-ng-devel}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.671
%{?with_sqlite:BuildRequires:	sqlite3-devel >= 3}
%{?with_odbc:BuildRequires:	unixODBC-devel}
BuildRequires:	which
BuildRequires:	zlib-devel
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
Requires:	systemd-units >= 38
Suggests:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# aaa_diameter requires 'freeDiameter/extension.h'
# cachedb_cassandra requires 'protocol/TBinaryProtocol.h' (thrift?)
%define		exclude_modules		aaa_diameter auth_jwt db_oracle cachedb_cassandra

%description
OpenSIPS (Open SIP Server) is a mature Open Source implementation of a
SIP server. OpenSIPS is more than a SIP proxy/router as it includes
application-level functionalities. OpenSIPS, as a SIP server, is the
core component of any SIP-based VoIP solution. With a very flexible
and customizable routing engine, OpenSIPS 'unifies voice, video, IM
and presence services in a highly efficient way, thanks to its
scalable (modular) design.

%description -l pl.UTF-8
OpenSIPS (Open SIP Server) to dojrzała, mająca otwarte źródła
implementacja serwera SIP. OpenSIPS to więcej niż proxy/router SIP,
jako że zawiera funkcje na poziomie aplikacji. OpenSIPS, jako serwer
SIP, jest głównym składnikiem dowolnego rozwiązania VoIP opartego na
SIP. Z bardzo elastycznym i konfigurowalnym silnikiem trasującym,
łączy usługi głosowe, wideo, komunikatorów oraz obecności w bardzo
wydajny sposób, dzięki skalowalnej, modularnej budowie.

%package radius
Summary:	openSIPS Radius module
Summary(pl.UTF-8):	Moduł Radius do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description radius
Radius auth/accounting module for openSIPS.

%description radius -l pl.UTF-8
Moduł uwierzytelniania/rozliczania Radius do openSIPS.

%package dynamodb
Summary:	openSIPS DynamoDB module
Summary(pl.UTF-8):	Moduł DynamoDB do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description dynamodb
Amazon DynamoDB cachedb module for openSIPS.

%description dynamodb -l pl.UTF-8
Moduł pamięci podręcznej Amazon DynamoDB do openSIPS.

%package memcached
Summary:	openSIPS memcached module
Summary(pl.UTF-8):	Moduł memcached do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description memcached
Memcached cachedb module for openSIPS.

%description memcached -l pl.UTF-8
Moduł pamięci podręcznej memcached do openSIPS.

%package redis
Summary:	Redis interface for openSIPS
Summary(pl.UTF-8):	Moduł Redis do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description redis
Redis cachedb module for openSIPS.

%description redis -l pl.UTF-8
Moduł pamięci podręcznej Redis do openSIPS.

%package mysql
Summary:	openSIPS MySQL module
Summary(pl.UTF-8):	Moduł MySQL do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description mysql
MySQL db module for openSIPS.

%description mysql -l pl.UTF-8
Moduł bazy danych MySQL do openSIPS.

%package postgres
Summary:	openSIPS PostgreSQL module
Summary(pl.UTF-8):	Moduł PostgreSQL do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description postgres
PostgreSQL db module for openSIPS.

%description postgres -l pl.UTF-8
Moduł bazy danych PostgreSQL do openSIPS.

%package sqlite3
Summary:	openSIPS Sqlite3 module
Summary(pl.UTF-8):	Moduł Sqlite3 do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description sqlite3
Sqlite3 db module for openSIPS.

%description sqlite3 -l pl.UTF-8
Moduł bazy danych Sqlite3 do openSIPS.

%package odbc
Summary:	openSIPS unixODBC module
Summary(pl.UTF-8):	Moduł unixODBC do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description odbc
unixODBC db module for openSIPS.

%description odbc -l pl.UTF-8
Moduł bazy danych unixODBC do openSIPS.

%package kafka
Summary:	Apache Kafka interface to openSIPS
Summary(pl.UTF-8):	Interfejs Apache Kafka do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description kafka
Apache Kafka event module for openSIPS.

%description kafka -l pl.UTF-8
Moduł kolejki zdarzeń Apache Kafka do openSIPS.

%package rabbitmq
Summary:	RabbitMQ interface to openSIPS
Summary(pl.UTF-8):	Interfejs RabbitMQ do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description rabbitmq
RabbitMQ event module for openSIPS.

%description rabbitmq -l pl.UTF-8
Moduł kolejki zdarzeń RabbitMQ do openSIPS.

%package sqs
Summary:	openSIPS SQS module
Summary(pl.UTF-8):	Moduł SQS do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description sqs
Amazon SQS event module for openSIPS.

%description sqs -l pl.UTF-8
Moduł kolejki zdarzeń Amazon SQS do openSIPS.

%package carrierroute
Summary:	openSIPS Carrierroute module
Summary(pl.UTF-8):	Moduł Carrierroute do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description carrierroute
Carrierroute module for openSIPS.

%description carrierroute -l pl.UTF-8
Moduł Carrierroute do openSIPS.

%package cgrates
Summary:	openSIPS CGRateS module
Summary(pl.UTF-8):	Moduł CGRateS do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description cgrates
CGRateS module for openSIPS.

%description cgrates -l pl.UTF-8
Moduł CGRateS do openSIPS.

%package httpd
Summary:	HTTP interface to openSIPS
Summary(pl.UTF-8):	Interfejs HTTP do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description httpd
HTTP interface to openSIPS.

%description httpd -l pl.UTF-8
Interfejs HTTP do openSIPS.

%package http2d
Summary:	HTTP/2 interface to openSIPS
Summary(pl.UTF-8):	Interfejs HTTP/2 do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description http2d
HTTP/2 interface to openSIPS.

%description http2d -l pl.UTF-8
Interfejs HTTP/2 do openSIPS.

%package json
Summary:	openSIPS JSON module
Summary(pl.UTF-8):	Moduł JSON do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description json
JSON module for openSIPS.

%description json -l pl.UTF-8
Moduł JSON do openSIPS.

%package ldap
Summary:	openSIPS LDAP and H350 modules
Summary(pl.UTF-8):	Moduły LDAP i H350 do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description ldap
LDAP and H350 modules for openSIPS.

%description ldap -l pl.UTF-8
Moduły LDAP i H350 do openSIPS.

%package mmgeoip
Summary:	openSIPS MaxMind GeoIP module
Summary(pl.UTF-8):	Moduł MaxMind GeoIP do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description mmgeoip
MaxMind GeoIP module for openSIPS.

%description mmgeoip -l pl.UTF-8
Moduł MaxMind GeoIP do openSIPS.

%package osp
Summary:	openSIPS OSP module
Summary(pl.UTF-8):	Moduł OSP do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description osp
OSP module for openSIPS.

%description osp -l pl.UTF-8
Moduł OSP do openSIPS.

%package perl
Summary:	openSIPS perl and perlvdb modules
Summary(pl.UTF-8):	Moduły perl i perlvdb do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description perl
Perl modules (perl & perlvdb) for openSIPS.

%description perl -l pl.UTF-8
Moduły perl i perlvdb do openSIPS.

%package snmpstats
Summary:	openSIPS SNMP statistics module
Summary(pl.UTF-8):	Moduł do statystyk SNMP do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description snmpstats
openSIPS SNMP statistics module.

%description snmpstats -l pl.UTF-8
Moduł do statystyk SNMP do openSIPS.

%package -n mibs-%{name}
Summary:	MIBs for openSIPS
Summary(pl.UTF-8):	MIB-y dla openSIPS
Group:		Applications/System
Requires:	mibs-dirs
Requires:	mibs-net-snmp
Obsoletes:	opensips-mibs < 1.5.3-2

%description -n mibs-%{name}
MIBs for openSIPS.

%description -n mibs-%{name} -l pl.UTF-8
MIB-y dla openSIPS.

%package xmpp
Summary:	openSIPS XMPP/Jabber modules
Summary(pl.UTF-8):	Moduły XMPP/Jabber do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Obsoletes:	opensips-jabber < 1.4.1

%description xmpp
XMPP/Jabber modules for openSIPS.

%description xmpp -l pl.UTF-8
Moduły XMPP/Jabber do openSIPS.

%prep
%setup -q
%patch -P0 -p1

%{__sed} -E -i -e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python3}\1,' \
	scripts/dbtextdb/dbtextdb.py

%build
exclude_modules="%{exclude_modules}"
%if %{without radius}
exclude_modules="$exclude_modules aaa_radius"
%endif
%if %{without aws}
exclude_modules="$exclude_modules cachedb_dynamodb event_sqs"
%endif
%if %{without couchbase}
exclude_modules="$exclude_modules cachedb_couchbase"
%endif
%if %{without memcached}
exclude_modules="$exclude_modules cachedb_memcached"
%endif
%if %{without mongodb}
exclude_modules="$exclude_modules cachedb_mongodb"
%endif
%if %{without redis}
exclude_modules="$exclude_modules cachedb_redis"
%endif
%if %{without mysql}
exclude_modules="$exclude_modules db_mysql"
%endif
%if %{without pgsql}
exclude_modules="$exclude_modules db_postgres"
%endif
%if %{without sqlite}
exclude_modules="$exclude_modules db_sqlite"
%endif
%if %{without odbc}
exclude_modules="$exclude_modules db_unixodbc"
%endif
%if %{without kafka}
exclude_modules="$exclude_modules event_kafka"
%endif
%if %{without carrierroute}
exclude_modules="$exclude_modules carrierroute"
%endif
%if %{without json}
exclude_modules="$exclude_modules json"
exclude_modules="$exclude_modules cgrates"
%endif
%if %{without ldap}
exclude_modules="$exclude_modules h350 ldap"
%endif
%if %{without microhttpd}
exclude_modules="$exclude_modules httpd"
%endif
%if %{without http2}
exclude_modules="$exclude_modules http2d"
%endif
%if %{without launchdarkly}
exclude_modules="$exclude_modules launch_darkly"
%endif
%if %{without geoip}
exclude_modules="$exclude_modules mmgeoip"
%endif
%if %{without osp}
exclude_modules="$exclude_modules osp"
%endif
%if %{without rabbitmq}
exclude_modules="$exclude_modules rabbitmq"
%endif
%if %{without rtpproxy}
exclude_modules="$exclude_modules rtp.io"
%endif
%if %{without sngtc}
exclude_modules="$exclude_modules sngtc"
%endif
%if %{without wolfssl}
exclude_modules="$exclude_modules tls_wolfssl"
%endif
echo "$exclude_modules" > exclude_modules
DFLAGS="%{rpmldflags}" \
LIB_LUA_NAME=lua5.4 \
%{__make} all \
	CC="%{__cc}" \
	CC_EXTRA_OPTS="-I/usr/include/ncurses" \
	CFLAGS="%{rpmcflags} -Wcast-align" \
	PYTHON=%{__python3} \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib} \
	prefix=%{_prefix} \
	cfg_prefix=$RPM_BUILD_ROOT \
	cfg_target=%{_sysconfdir}/opensips/ \
	HTTP2D_USE_SYSTEM=yes \
	RADIUSCLIENT=RADIUSCLIENT \
	Q= \
	exclude_modules="$exclude_modules"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{ser,sysconfig,rc.d/init.d} \
	-d $RPM_BUILD_ROOT%{systemdunitdir}

exclude_modules="$(cat exclude_modules)"
%{__make} install -j1 \
	BASEDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	INSTALLMIBDIR=$RPM_BUILD_ROOT%{_datadir}/mibs \
	LIBDIR=%{_lib} \
	prefix=%{_prefix} \
	cfg_prefix=$RPM_BUILD_ROOT \
	cfg_target=%{_sysconfdir}/opensips/ \
	Q= \
	HTTP2D_USE_SYSTEM=yes \
	exclude_modules="$exclude_modules"

for i in modules/*; do \
	i=$(basename $i)
	[ -f modules/$i/README ] && cp -f modules/$i/README README.$i; \
done

# contains the same files we install in %doc
%{__rm} -r  $RPM_BUILD_ROOT%{_docdir}/%{name}

#cd doc/serdev
#docbook2html serdev.sgml
#rm -f serdev.sgml
#cd ../seruser
#docbook2html seruser.sgml
#rm -f seruser.sgml
#cd ../..

cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/opensips
cp -p %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/opensips
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{systemdunitdir}/opensips.service

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add opensips
%service opensips restart "SIP Daemon"
%systemd_post opensips.service

%preun
%systemd_preun opensips.service
if [ "$1" = "0" ]; then
	%service opensips stop
	/sbin/chkconfig --del opensips
fi

%postun
%systemd_reload

%triggerpostun -- %{name} < 2.1.0-0.2
%systemd_trigger opensips.service

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog INSTALL NEWS README README.md SECURITY.md scripts examples
%attr(755,root,root) %{_sbindir}/bdb_recover
%attr(755,root,root) %{_sbindir}/opensips
%attr(755,root,root) %{_sbindir}/osipsconfig
%dir %{_sysconfdir}/opensips
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/opensips.cfg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/scenario_callcenter.xml
%dir %attr(700,root,root) %{_sysconfdir}/opensips/tls
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/tls/README
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/tls/ca.conf
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/tls/request.conf
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/tls/user.conf
%dir %attr(700,root,root) %{_sysconfdir}/opensips/tls/rootCA
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/tls/rootCA/cacert.pem
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/tls/rootCA/index.txt
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/tls/rootCA/serial
%dir %attr(700,root,root) %{_sysconfdir}/opensips/tls/rootCA/certs
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/tls/rootCA/certs/01.pem
%dir %attr(700,root,root) %{_sysconfdir}/opensips/tls/rootCA/private
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/tls/rootCA/private/cakey.pem
%dir %attr(700,root,root) %{_sysconfdir}/opensips/tls/user
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/tls/user/user-calist.pem
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/tls/user/user-cert.pem
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/tls/user/user-cert_req.pem
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/tls/user/user-privkey.pem
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/opensips
%attr(754,root,root) /etc/rc.d/init.d/opensips
%{systemdunitdir}/opensips.service
%dir %{_libdir}/opensips
%dir %{_libdir}/opensips/modules
# explict list here, no globs please (to avoid mistakes)
%{_libdir}/opensips/modules/acc.so
%{_libdir}/opensips/modules/aka_av_diameter.so
%{_libdir}/opensips/modules/alias_db.so
%{_libdir}/opensips/modules/auth_aaa.so
%{_libdir}/opensips/modules/auth_aka.so
%{_libdir}/opensips/modules/auth_db.so
# R: openssl
%{_libdir}/opensips/modules/auth.so
%{_libdir}/opensips/modules/b2b_entities.so
%{_libdir}/opensips/modules/b2b_logic.so
%{_libdir}/opensips/modules/b2b_sca.so
%{_libdir}/opensips/modules/b2b_sdp_demux.so
%{_libdir}/opensips/modules/benchmark.so
%{_libdir}/opensips/modules/cachedb_local.so
%{_libdir}/opensips/modules/cachedb_sql.so
%{_libdir}/opensips/modules/call_center.so
%{_libdir}/opensips/modules/call_control.so
%{_libdir}/opensips/modules/callops.so
%{_libdir}/opensips/modules/cfgutils.so
%{_libdir}/opensips/modules/clusterer.so
# R: zlib
%{_libdir}/opensips/modules/compression.so
%{_libdir}/opensips/modules/config.so
# R: libxml2 zlib
%{_libdir}/opensips/modules/cpl_c.so
# R: db
%{_libdir}/opensips/modules/db_berkeley.so
%{_libdir}/opensips/modules/db_cachedb.so
%{_libdir}/opensips/modules/db_flatstore.so
# R: curl
%{_libdir}/opensips/modules/db_http.so
%{_libdir}/opensips/modules/db_text.so
%{_libdir}/opensips/modules/db_virtual.so
%{_libdir}/opensips/modules/dialog.so
# R: pcre2-8
%{_libdir}/opensips/modules/dialplan.so
%{_libdir}/opensips/modules/dispatcher.so
%{_libdir}/opensips/modules/diversion.so
%{_libdir}/opensips/modules/dns_cache.so
%{_libdir}/opensips/modules/domainpolicy.so
%{_libdir}/opensips/modules/domain.so
%{_libdir}/opensips/modules/drouting.so
# R: curl
%{_libdir}/opensips/modules/emergency.so
%{_libdir}/opensips/modules/enum.so
%{_libdir}/opensips/modules/event_datagram.so
%{_libdir}/opensips/modules/event_flatstore.so
%{_libdir}/opensips/modules/event_routing.so
%{_libdir}/opensips/modules/event_stream.so
%{_libdir}/opensips/modules/event_virtual.so
%{_libdir}/opensips/modules/event_xmlrpc.so
%{_libdir}/opensips/modules/exec.so
%{_libdir}/opensips/modules/fraud_detection.so
%{_libdir}/opensips/modules/freeswitch_scripting.so
%{_libdir}/opensips/modules/freeswitch.so
%{_libdir}/opensips/modules/gflags.so
%{_libdir}/opensips/modules/group.so
# R: openssl
%{_libdir}/opensips/modules/identity.so
%{_libdir}/opensips/modules/imc.so
%{_libdir}/opensips/modules/janus.so
%{_libdir}/opensips/modules/jsonrpc.so
%{_libdir}/opensips/modules/load_balancer.so
# R: lua5.4 memcached mysql openssl zlib
%{_libdir}/opensips/modules/lua.so
%{_libdir}/opensips/modules/mangler.so
%{_libdir}/opensips/modules/mathops.so
%{_libdir}/opensips/modules/maxfwd.so
%{_libdir}/opensips/modules/media_exchange.so
%{_libdir}/opensips/modules/mediaproxy.so
%{_libdir}/opensips/modules/mi_datagram.so
%{_libdir}/opensips/modules/mid_registrar.so
%{_libdir}/opensips/modules/mi_fifo.so
%{_libdir}/opensips/modules/mi_html.so
%{_libdir}/opensips/modules/mi_script.so
# R: libxml2 zlib
%{_libdir}/opensips/modules/mi_xmlrpc_ng.so
%{_libdir}/opensips/modules/mqueue.so
%{_libdir}/opensips/modules/msilo.so
%{_libdir}/opensips/modules/msrp_gateway.so
# R: openssl
%{_libdir}/opensips/modules/msrp_relay.so
%{_libdir}/opensips/modules/msrp_ua.so
%{_libdir}/opensips/modules/nathelper.so
%{_libdir}/opensips/modules/nat_traversal.so
%{_libdir}/opensips/modules/options.so
%{_libdir}/opensips/modules/path.so
%{_libdir}/opensips/modules/peering.so
%{_libdir}/opensips/modules/permissions.so
# R: libxml2 zlib
%{_libdir}/opensips/modules/pi_http.so
%{_libdir}/opensips/modules/pike.so
%{_libdir}/opensips/modules/presence.so
%{_libdir}/opensips/modules/presence_callinfo.so
# R: libxml2
%{_libdir}/opensips/modules/presence_dfks.so
# R: libxml2 zlib
%{_libdir}/opensips/modules/presence_dialoginfo.so
%{_libdir}/opensips/modules/presence_mwi.so
# R: libxml2 zlib
%{_libdir}/opensips/modules/presence_reginfo.so
%{_libdir}/opensips/modules/presence_xcapdiff.so
# R: libxml2
%{_libdir}/opensips/modules/presence_xml.so
%{_libdir}/opensips/modules/prometheus.so
%{_libdir}/opensips/modules/proto_bin.so
%{_libdir}/opensips/modules/proto_bins.so
%{_libdir}/opensips/modules/proto_hep.so
# R: libmnl
%{_libdir}/opensips/modules/proto_ipsec.so
%{_libdir}/opensips/modules/proto_msrp.so
# R: libsctp
%{_libdir}/opensips/modules/proto_sctp.so
%{_libdir}/opensips/modules/proto_smpp.so
%{_libdir}/opensips/modules/proto_tls.so
%{_libdir}/opensips/modules/proto_ws.so
%{_libdir}/opensips/modules/proto_wss.so
%{_libdir}/opensips/modules/pua.so
# R: libxml2 zlib
%{_libdir}/opensips/modules/pua_bla.so
# R: libxml2
%{_libdir}/opensips/modules/pua_dialoginfo.so
# R: libxml2 zlib
%{_libdir}/opensips/modules/pua_mi.so
# R: libxml2 zlib
%{_libdir}/opensips/modules/pua_reginfo.so
# R: libxml2 zlib
%{_libdir}/opensips/modules/pua_usrloc.so
# R: python3-libs
%{_libdir}/opensips/modules/python.so
%{_libdir}/opensips/modules/qos.so
%{_libdir}/opensips/modules/qrouting.so
%{_libdir}/opensips/modules/rate_cacher.so
%{_libdir}/opensips/modules/ratelimit.so
# R: pcre2-8
%{_libdir}/opensips/modules/regex.so
%{_libdir}/opensips/modules/registrar.so
# R: curl
%{_libdir}/opensips/modules/rest_client.so
# R: libxml2 zlib
%{_libdir}/opensips/modules/rls.so
%{_libdir}/opensips/modules/rr.so
%{_libdir}/opensips/modules/rtp_relay.so
%{_libdir}/opensips/modules/rtpengine.so
%{_libdir}/opensips/modules/rtpproxy.so
%{_libdir}/opensips/modules/script_helper.so
%{_libdir}/opensips/modules/signaling.so
%{_libdir}/opensips/modules/sipcapture.so
%{_libdir}/opensips/modules/sip_i.so
%{_libdir}/opensips/modules/sipmsgops.so
# R: libuuid
%{_libdir}/opensips/modules/siprec.so
%{_libdir}/opensips/modules/sl.so
%{_libdir}/opensips/modules/sockets_mgm.so
%{_libdir}/opensips/modules/speeddial.so
%{_libdir}/opensips/modules/sql_cacher.so
%{_libdir}/opensips/modules/sst.so
%{_libdir}/opensips/modules/sqlops.so
%{_libdir}/opensips/modules/statistics.so
%{_libdir}/opensips/modules/status_report.so
# R: openssl
%{_libdir}/opensips/modules/stir_shaken.so
%{_libdir}/opensips/modules/stun.so
%{_libdir}/opensips/modules/tcp_mgm.so
%{_libdir}/opensips/modules/textops.so
%{_libdir}/opensips/modules/tls_mgm.so
# R: openssl
%{_libdir}/opensips/modules/tls_openssl.so
%{_libdir}/opensips/modules/tm.so
%{_libdir}/opensips/modules/topology_hiding.so
%{_libdir}/opensips/modules/tracer.so
%{_libdir}/opensips/modules/trie.so
# R: openssl
%{_libdir}/opensips/modules/uac_auth.so
%{_libdir}/opensips/modules/uac_redirect.so
%{_libdir}/opensips/modules/uac_registrant.so
%{_libdir}/opensips/modules/uac.so
%{_libdir}/opensips/modules/userblacklist.so
%{_libdir}/opensips/modules/usrloc.so
# R: libuuid
%{_libdir}/opensips/modules/uuid.so
# R: libxml2 zlib
%{_libdir}/opensips/modules/xcap.so
# R: curl libxml2 zlib
%{_libdir}/opensips/modules/xcap_client.so
# R: libxml2
%{_libdir}/opensips/modules/xml.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/db_berkeley
%{_datadir}/%{name}/dbtext
%{_datadir}/%{name}/menuconfig_templates
%{_datadir}/%{name}/pi_http
%{_mandir}/man5/opensips.cfg.5*
%{_mandir}/man8/opensips.8*

%if %{with radius}
%files radius
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/dictionary.opensips
# R: radiusclient-ng-libs
%{_libdir}/opensips/modules/aaa_radius.so
%endif

%if %{with aws}
%files dynamodb
%defattr(644,root,root,755)
# R: aws-sdk-cpp
%{_libdir}/opensips/modules/cachedb_dynamodb.so
%endif

%if %{with memcached}
%files memcached
%defattr(644,root,root,755)
# R: libmemcached
%{_libdir}/opensips/modules/cachedb_memcached.so
%endif

%if %{with redis}
%files redis
%defattr(644,root,root,755)
# R: hiredis
%{_libdir}/opensips/modules/cachedb_redis.so
%endif

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
# R: mysql-libs openssl zlib
%{_libdir}/opensips/modules/db_mysql.so
%{_datadir}/%{name}/mysql
%endif

%if %{with pgsql}
%files postgres
%defattr(644,root,root,755)
# R: postgresql-libs
%{_libdir}/opensips/modules/db_postgres.so
%{_datadir}/%{name}/postgres
%endif

%if %{with sqlite}
%files sqlite3
%defattr(644,root,root,755)
# R: sqlite3
%{_libdir}/opensips/modules/db_sqlite.so
%{_datadir}/opensips/sqlite
%endif

%if %{with odbc}
%files odbc
%defattr(644,root,root,755)
# R: unixODBC
%{_libdir}/opensips/modules/db_unixodbc.so
%endif

%if %{with aws}
%files sqs
%defattr(644,root,root,755)
# R: aws-sdk-cpp
%{_libdir}/opensips/modules/event_sqs.so
%endif

%if %{with kafka}
%files kafka
%defattr(644,root,root,755)
# R: librdkafka
%{_libdir}/opensips/modules/event_kafka.so
%endif

%if %{with rabbitmq}
%files rabbitmq
%defattr(644,root,root,755)
# R: librabbitmq-c
%{_libdir}/opensips/modules/event_rabbitmq.so
# R: librabbitmq-c
%{_libdir}/opensips/modules/rabbitmq_consumer.so
%endif

%if %{with carrierroute}
%files carrierroute
%defattr(644,root,root,755)
# R: libconfuse
%{_libdir}/opensips/modules/carrierroute.so
%endif

%if %{with json}
%files cgrates
%defattr(644,root,root,755)
# R: json-c
%{_libdir}/opensips/modules/cgrates.so
%endif

%if %{with microhttpd}
%files httpd
%defattr(644,root,root,755)
# R: libmicrohttpd
%{_libdir}/opensips/modules/httpd.so
%{_libdir}/opensips/modules/mi_http.so
%endif

%if %{with http2}
%files http2d
%defattr(644,root,root,755)
# R: nghttp2
%{_libdir}/opensips/modules/http2d.so
%endif

%if %{with json}
%files json
%defattr(644,root,root,755)
# R: json-c
%{_libdir}/opensips/modules/json.so
%endif

%if %{with ldap}
%files ldap
%defattr(644,root,root,755)
%{_libdir}/opensips/modules/h350.so
# R: openldap-libs
%{_libdir}/opensips/modules/ldap.so
%endif

%if %{with geoip}
%files mmgeoip
%defattr(644,root,root,755)
# R: libmaxminddb
%{_libdir}/opensips/modules/mmgeoip.so
%endif

%if %{with osp}
%files osp
%defattr(644,root,root,755)
%{_libdir}/opensips/modules/osp.so
%endif

%files perl
%defattr(644,root,root,755)
# R: perl-libs
%{_libdir}/opensips/modules/db_perlvdb.so
# R: perl-libs
%{_libdir}/opensips/modules/perl.so
%{_libdir}/opensips/perl

%files snmpstats
%defattr(644,root,root,755)
# R: net-snmp-libs + dependencies
%{_libdir}/opensips/modules/snmpstats.so

%files -n mibs-%{name}
%defattr(644,root,root,755)
%{_datadir}/mibs/OPENSER-*

%files xmpp
%defattr(644,root,root,755)
# R: expat
%{_libdir}/opensips/modules/jabber.so
# R: expat
%{_libdir}/opensips/modules/xmpp.so
# R: libxml2 zlib
%{_libdir}/opensips/modules/pua_xmpp.so
