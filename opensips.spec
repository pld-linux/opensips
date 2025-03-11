# TODO: oracle, system wolfssl
#
# Conditional build:
%bcond_without	mysql		# MySQL support
%bcond_without	pgsql		# PostgreSQL support
%bcond_without	sqlite		# Sqlite3 support
%bcond_without	odbc		# ODBC support
%bcond_without	radius		# radius support
%bcond_without	carrierroute	# carrierroute support
%bcond_without	ldap		# LDAP support
%bcond_with	osp		# ETSI OSP VoIP Peering support
%bcond_without	geoip		# GeoIP
%bcond_without	json		# json support
%bcond_without	memcached	# memcached support
%bcond_without	microhttpd	# httpd support
%bcond_without	kafka		# Apache Kafka support
%bcond_without	redis		# Redis support
%bcond_with	couchbase	# couchbase support
%bcond_with	mongodb		# mongodb support
%bcond_with	sngtc		# Sangoma transcoding module support
%bcond_without	rabbitmq	# Rabbit MQ support
%bcond_with	wolfssl		# WolfSSL support (builds internal WolfSSL :( )

Summary:	SIP proxy, redirect and registrar server
Summary(pl.UTF-8):	Serwer SIP przekazujący (proxy), przekierowujący i rejestrujący
Name:		opensips
Version:	3.4.1
Release:	5
License:	GPL v2
Group:		Networking/Daemons
Source0:	https://opensips.org/pub/opensips/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e889ffaddf770e945e77ebeca5f30fa4
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.service
Patch0:		x32.patch
Patch1:		make-4.4.patch
URL:		https://opensips.org/
%{?with_osp:BuildRequires:	OSPToolkit}
%{?with_sngtc:BuildRequires:    TODO-SNGTC-BRs}
BuildRequires:	bison
BuildRequires:	curl-devel
BuildRequires:	db-devel
BuildRequires:	expat-devel
BuildRequires:	flex
%{?with_redis:BuildRequires:	hiredis-devel}
%{?with_json:BuildRequires:	json-c-devel}
%{?with_carrierroute:BuildRequires:	libconfuse-devel}
%{?with_couchbase:BuildRequires:    libcouchbase-devel}
%{?with_geoip:BuildRequires:	libmaxminddb-devel}
%{?with_memcached:BuildRequires:	libmemcached-devel}
%{?with_microhttpd:BuildRequires:	libmicrohttpd-devel}
%{?with_pgsql:BuildRequires:	libpqxx-devel}
%{?with_kafka:BuildRequires:	librdkafka-devel}
BuildRequires:	libsctp-devel
%{?with_osp:BuildRequires:	libutf8proc-devel}
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-progs
BuildRequires:	lua54-devel
#BuildRequires:	lynx
%{?with_mongodb:BuildRequires:	mongo-c-driver-devel >= 1.0}
%{?with_mysql:BuildRequires:	mysql-devel}
BuildRequires:	net-snmp-devel
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	perl-devel
BuildRequires:	perl-tools-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
%{?with_rabbitmq:BuildRequires:	rabbitmq-c-devel}
%{?with_radius:BuildRequires:	radiusclient-ng-devel}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.671
%{?with_sqlite:BuildRequires:	sqlite3-devel >= 3}
#BuildRequires:	subversion
%{?with_odbc:BuildRequires:	unixODBC-devel}
BuildRequires:	which
BuildRequires:	xmlrpc-c-devel >= 1.10.0
BuildRequires:	zlib-devel
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
Requires:	systemd-units >= 38
Suggests:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# aaa_diameter requires 'freeDiameter/extension.h'
# cachedb_cassandra requires 'protocol/TBinaryProtocol.h'
%define	exclude_modules	aaa_diameter auth_jwt db_oracle cachedb_cassandra

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

%package mysql
Summary:	openSIPS MySQL module
Summary(pl.UTF-8):	Moduł MySQL do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description mysql
MySQL module for openSIPS.

%description mysql -l pl.UTF-8
Moduł MySQL do openSIPS.

%package postgres
Summary:	openSIPS PostgreSQL module
Summary(pl.UTF-8):	Moduł PostgreSQL do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description postgres
PostgreSQL module for openSIPS.

%description postgres -l pl.UTF-8
Moduł PostgreSQL do openSIPS.

%package sqlite3
Summary:	openSIPS Sqlite3 module
Summary(pl.UTF-8):	Moduł Sqlite3 do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description sqlite3
Sqlite3 module for openSIPS.

%description sqlite3 -l pl.UTF-8
Moduł Sqlite3 do openSIPS.

%package json
Summary:	openSIPS JSON module
Summary(pl.UTF-8):	Moduł JSON do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description json
JSON module for openSIPS.

%description json -l pl.UTF-8
Moduł JSON do openSIPS.

%package cgrates
Summary:	openSIPS CGRateS module
Summary(pl.UTF-8):	Moduł CGRateS do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description cgrates
CGRateS module for openSIPS.

%description cgrates -l pl.UTF-8
Moduł CGRateS do openSIPS.

%package memcached
Summary:	openSIPS memcached module
Summary(pl.UTF-8):	Moduł memcached do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description memcached
Memcached module for openSIPS.

%description memcached -l pl.UTF-8
Moduł memcached do openSIPS.

%package radius
Summary:	openSIPS Radius module
Summary(pl.UTF-8):	Moduł Radius do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description radius
Radius module for openSIPS.

%description radius -l pl.UTF-8
Moduł Radius do openSIPS.

%package odbc
Summary:	openSIPS ODBC module
Summary(pl.UTF-8):	Moduł ODBC do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description odbc
ODBC module for openSIPS.

%description odbc -l pl.UTF-8
Moduł ODBC do openSIPS.

%package perl
Summary:	openSIPS perl and perlvdb modules
Summary(pl.UTF-8):	Moduły perl i perlvdb do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description perl
Perl modules (perl & perlvdb) for openSIPS.

%description perl -l pl.UTF-8
Moduły perl i perlvdb do openSIPS.

%package xmpp
Summary:	openSIPS XMPP/Jabber modules
Summary(pl.UTF-8):	Moduły XMPP/Jabber do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Obsoletes:	opensips-jabber

%description xmpp
XMPP/Jabber modules for openSIPS.

%description xmpp -l pl.UTF-8
Moduły XMPP/Jabber do openSIPS.

%package ldap
Summary:	openSIPS LDAP and H350 modules
Summary(pl.UTF-8):	Moduły LDAP i H350 do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description ldap
LDAP and H350 modules for openSIPS.

%description ldap -l pl.UTF-8
Moduły LDAP i H350 do openSIPS.

%package carrierroute
Summary:	openSIPS Carrierroute module
Summary(pl.UTF-8):	Moduł Carrierroute do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description carrierroute
Carrierroute module for openSIPS.

%description carrierroute -l pl.UTF-8
Moduł Carrierroute do openSIPS.

%package osp
Summary:	openSIPS OSP module
Summary(pl.UTF-8):	Moduł OSP do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description osp
OSP module for openSIPS.

%description osp -l pl.UTF-8
Moduł OSP do openSIPS.

%package mmgeoip
Summary:	openSIPS MaxMind GeoIP module
Summary(pl.UTF-8):	Moduł MaxMind GeoIP do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description mmgeoip
MaxMind GeoIP module for openSIPS.

%description mmgeoip -l pl.UTF-8
Moduł MaxMind GeoIP do openSIPS.

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
Obsoletes:	opensips-mibs

%description -n mibs-%{name}
MIBs for openSIPS.

%description -n mibs-%{name} -l pl.UTF-8
MIB-y dla openSIPS.

%package redis
Summary:	Redis interface for openSIPS
Summary(pl.UTF-8):	Moduł Redis do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description redis
Redis interface for openSIPS.

%description redis -l pl.UTF-8
Moduł Redis do openSIPS.

%package httpd
Summary:	HTTP interface to openSIPS
Summary(pl.UTF-8):	Interfejs HTTP do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description httpd
HTTP interface to openSIPS.

%description httpd -l pl.UTF-8
Interfejs HTTP do openSIPS.

%package rabbitmq
Summary:	RabbitMQ interface to openSIPS
Summary(pl.UTF-8):	Interfejs RabbitMQ do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description rabbitmq
RabbitMQ interface to openSIPS.

%description rabbitmq -l pl.UTF-8
Interfejs RabbitMQ do openSIPS.

%package kafka
Summary:	Apache Kafka interface to openSIPS
Summary(pl.UTF-8):	Interfejs Apache Kafka do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description kafka
Apache Kafka interface to openSIPS.

%description kafka -l pl.UTF-8
Interfejs Apache Kafka do openSIPS.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1

%{__sed} -E -i -e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python3}\1,' \
      scripts/dbtextdb/dbtextdb.py

%build
exclude_modules="%{exclude_modules}"
%if %{without redis}
exclude_modules="$exclude_modules cachedb_redis"
%endif
%if %{without ldap}
exclude_modules="$exclude_modules h350 ldap"
%endif
%if %{without carrierroute}
exclude_modules="$exclude_modules carrierroute"
%endif
%if %{without osp}
exclude_modules="$exclude_modules osp"
%endif
%if %{without microhttpd}
exclude_modules="$exclude_modules httpd"
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
%if %{without geoip}
exclude_modules="$exclude_modules mmgeoip"
%endif
%if %{without radius}
exclude_modules="$exclude_modules aaa_radius"
%endif
%if %{without json}
exclude_modules="$exclude_modules json"
exclude_modules="$exclude_modules cgrates"
%endif
%if %{without memcached}
exclude_modules="$exclude_modules cachedb_memcached"
%endif
%if %{without couchbase}
exclude_modules="$exclude_modules cachedb_couchbase"
%endif
%if %{without mongodb}
exclude_modules="$exclude_modules cachedb_mongodb"
%endif
%if %{without sngtc}
exclude_modules="$exclude_modules sngtc"
%endif
%if %{without rabbitmq}
exclude_modules="$exclude_modules rabbitmq"
%endif
%if %{without wolfssl}
exclude_modules="$exclude_modules tls_wolfssl"
%endif
%if %{without kafka}
exclude_modules="$exclude_modules event_kafka"
%endif
echo "$exclude_modules" > exclude_modules
DFLAGS="%{rpmldflags}" \
LIB_LUA_NAME=lua5.4 \
%{__make} all \
	PYTHON=%{__python3} \
	Q= \
	exclude_modules="$exclude_modules" \
	prefix=%{_prefix} \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib} \
	cfg_prefix=$RPM_BUILD_ROOT \
	cfg_target=%{_sysconfdir}/opensips/ \
	RADIUSCLIENT=RADIUSCLIENT \
	CC="%{__cc}" \
	CC_EXTRA_OPTS="-I/usr/include/ncurses" \
	CFLAGS="%{rpmcflags} -Wcast-align"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{ser,sysconfig,rc.d/init.d} \
	-d $RPM_BUILD_ROOT%{systemdunitdir}

exclude_modules="$(cat exclude_modules)"
%{__make} install -j1 \
	Q= \
	exclude_modules="$exclude_modules" \
	prefix=%{_prefix} \
	PREFIX=%{_prefix} \
	LIBDIR=%{_lib} \
	BASEDIR=$RPM_BUILD_ROOT \
	cfg_prefix=$RPM_BUILD_ROOT \
cfg_target=%{_sysconfdir}/opensips/ \
	INSTALLMIBDIR=$RPM_BUILD_ROOT%{_datadir}/mibs

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
%doc README* AUTHORS CREDITS ChangeLog INSTALL NEWS scripts examples
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
%attr(755,root,root) %{_libdir}/opensips/modules/acc.so
%attr(755,root,root) %{_libdir}/opensips/modules/alias_db.so
%attr(755,root,root) %{_libdir}/opensips/modules/auth_aaa.so
%attr(755,root,root) %{_libdir}/opensips/modules/auth_db.so
%attr(755,root,root) %{_libdir}/opensips/modules/auth.so
%attr(755,root,root) %{_libdir}/opensips/modules/avpops.so
%attr(755,root,root) %{_libdir}/opensips/modules/b2b_entities.so
%attr(755,root,root) %{_libdir}/opensips/modules/b2b_logic.so
%attr(755,root,root) %{_libdir}/opensips/modules/b2b_sca.so
%attr(755,root,root) %{_libdir}/opensips/modules/b2b_sdp_demux.so
%attr(755,root,root) %{_libdir}/opensips/modules/benchmark.so
%attr(755,root,root) %{_libdir}/opensips/modules/cachedb_local.so
%attr(755,root,root) %{_libdir}/opensips/modules/cachedb_sql.so
%attr(755,root,root) %{_libdir}/opensips/modules/call_center.so
%attr(755,root,root) %{_libdir}/opensips/modules/call_control.so
%attr(755,root,root) %{_libdir}/opensips/modules/callops.so
%attr(755,root,root) %{_libdir}/opensips/modules/cfgutils.so
%attr(755,root,root) %{_libdir}/opensips/modules/clusterer.so
%attr(755,root,root) %{_libdir}/opensips/modules/compression.so
%attr(755,root,root) %{_libdir}/opensips/modules/cpl_c.so
%attr(755,root,root) %{_libdir}/opensips/modules/db_berkeley.so
%attr(755,root,root) %{_libdir}/opensips/modules/db_cachedb.so
%attr(755,root,root) %{_libdir}/opensips/modules/db_flatstore.so
%attr(755,root,root) %{_libdir}/opensips/modules/db_http.so
%attr(755,root,root) %{_libdir}/opensips/modules/db_text.so
%attr(755,root,root) %{_libdir}/opensips/modules/db_virtual.so
%attr(755,root,root) %{_libdir}/opensips/modules/dialog.so
%attr(755,root,root) %{_libdir}/opensips/modules/dialplan.so
%attr(755,root,root) %{_libdir}/opensips/modules/dispatcher.so
%attr(755,root,root) %{_libdir}/opensips/modules/diversion.so
%attr(755,root,root) %{_libdir}/opensips/modules/dns_cache.so
%attr(755,root,root) %{_libdir}/opensips/modules/domainpolicy.so
%attr(755,root,root) %{_libdir}/opensips/modules/domain.so
%attr(755,root,root) %{_libdir}/opensips/modules/drouting.so
%attr(755,root,root) %{_libdir}/opensips/modules/emergency.so
%attr(755,root,root) %{_libdir}/opensips/modules/enum.so
%attr(755,root,root) %{_libdir}/opensips/modules/event_datagram.so
%attr(755,root,root) %{_libdir}/opensips/modules/event_flatstore.so
%attr(755,root,root) %{_libdir}/opensips/modules/event_route.so
%attr(755,root,root) %{_libdir}/opensips/modules/event_routing.so
%attr(755,root,root) %{_libdir}/opensips/modules/event_stream.so
%attr(755,root,root) %{_libdir}/opensips/modules/event_virtual.so
%attr(755,root,root) %{_libdir}/opensips/modules/event_xmlrpc.so
%attr(755,root,root) %{_libdir}/opensips/modules/exec.so
%attr(755,root,root) %{_libdir}/opensips/modules/fraud_detection.so
%attr(755,root,root) %{_libdir}/opensips/modules/freeswitch_scripting.so
%attr(755,root,root) %{_libdir}/opensips/modules/freeswitch.so
%attr(755,root,root) %{_libdir}/opensips/modules/gflags.so
%attr(755,root,root) %{_libdir}/opensips/modules/group.so
%attr(755,root,root) %{_libdir}/opensips/modules/identity.so
%attr(755,root,root) %{_libdir}/opensips/modules/imc.so
%attr(755,root,root) %{_libdir}/opensips/modules/jsonrpc.so
%attr(755,root,root) %{_libdir}/opensips/modules/load_balancer.so
%attr(755,root,root) %{_libdir}/opensips/modules/lua.so
%attr(755,root,root) %{_libdir}/opensips/modules/mangler.so
%attr(755,root,root) %{_libdir}/opensips/modules/mathops.so
%attr(755,root,root) %{_libdir}/opensips/modules/maxfwd.so
%attr(755,root,root) %{_libdir}/opensips/modules/media_exchange.so
%attr(755,root,root) %{_libdir}/opensips/modules/mediaproxy.so
%attr(755,root,root) %{_libdir}/opensips/modules/mi_datagram.so
%attr(755,root,root) %{_libdir}/opensips/modules/mid_registrar.so
%attr(755,root,root) %{_libdir}/opensips/modules/mi_fifo.so
%attr(755,root,root) %{_libdir}/opensips/modules/mi_html.so
%attr(755,root,root) %{_libdir}/opensips/modules/mi_script.so
%attr(755,root,root) %{_libdir}/opensips/modules/mi_xmlrpc_ng.so
%attr(755,root,root) %{_libdir}/opensips/modules/msilo.so
%attr(755,root,root) %{_libdir}/opensips/modules/msrp_gateway.so
%attr(755,root,root) %{_libdir}/opensips/modules/msrp_relay.so
%attr(755,root,root) %{_libdir}/opensips/modules/msrp_ua.so
%attr(755,root,root) %{_libdir}/opensips/modules/nathelper.so
%attr(755,root,root) %{_libdir}/opensips/modules/nat_traversal.so
%attr(755,root,root) %{_libdir}/opensips/modules/options.so
%attr(755,root,root) %{_libdir}/opensips/modules/path.so
%attr(755,root,root) %{_libdir}/opensips/modules/peering.so
%attr(755,root,root) %{_libdir}/opensips/modules/permissions.so
%attr(755,root,root) %{_libdir}/opensips/modules/pi_http.so
%attr(755,root,root) %{_libdir}/opensips/modules/pike.so
%attr(755,root,root) %{_libdir}/opensips/modules/presence_callinfo.so
%attr(755,root,root) %{_libdir}/opensips/modules/presence_dialoginfo.so
%attr(755,root,root) %{_libdir}/opensips/modules/presence_mwi.so
%attr(755,root,root) %{_libdir}/opensips/modules/presence.so
%attr(755,root,root) %{_libdir}/opensips/modules/presence_dfks.so
%attr(755,root,root) %{_libdir}/opensips/modules/presence_xcapdiff.so
%attr(755,root,root) %{_libdir}/opensips/modules/presence_xml.so
%attr(755,root,root) %{_libdir}/opensips/modules/prometheus.so
%attr(755,root,root) %{_libdir}/opensips/modules/proto_bin.so
%attr(755,root,root) %{_libdir}/opensips/modules/proto_bins.so
%attr(755,root,root) %{_libdir}/opensips/modules/proto_hep.so
%attr(755,root,root) %{_libdir}/opensips/modules/proto_msrp.so
%attr(755,root,root) %{_libdir}/opensips/modules/proto_sctp.so
%attr(755,root,root) %{_libdir}/opensips/modules/proto_smpp.so
%attr(755,root,root) %{_libdir}/opensips/modules/proto_tls.so
%attr(755,root,root) %{_libdir}/opensips/modules/proto_ws.so
%attr(755,root,root) %{_libdir}/opensips/modules/proto_wss.so
%attr(755,root,root) %{_libdir}/opensips/modules/pua_bla.so
%attr(755,root,root) %{_libdir}/opensips/modules/pua_dialoginfo.so
%attr(755,root,root) %{_libdir}/opensips/modules/pua_mi.so
%attr(755,root,root) %{_libdir}/opensips/modules/pua.so
%attr(755,root,root) %{_libdir}/opensips/modules/pua_usrloc.so
%attr(755,root,root) %{_libdir}/opensips/modules/python.so
%attr(755,root,root) %{_libdir}/opensips/modules/qos.so
%attr(755,root,root) %{_libdir}/opensips/modules/qrouting.so
%attr(755,root,root) %{_libdir}/opensips/modules/rate_cacher.so
%attr(755,root,root) %{_libdir}/opensips/modules/ratelimit.so
%attr(755,root,root) %{_libdir}/opensips/modules/regex.so
%attr(755,root,root) %{_libdir}/opensips/modules/registrar.so
%attr(755,root,root) %{_libdir}/opensips/modules/rest_client.so
%attr(755,root,root) %{_libdir}/opensips/modules/rls.so
%attr(755,root,root) %{_libdir}/opensips/modules/rr.so
%attr(755,root,root) %{_libdir}/opensips/modules/rtp_relay.so
%attr(755,root,root) %{_libdir}/opensips/modules/rtpengine.so
%attr(755,root,root) %{_libdir}/opensips/modules/rtpproxy.so
%attr(755,root,root) %{_libdir}/opensips/modules/script_helper.so
%attr(755,root,root) %{_libdir}/opensips/modules/signaling.so
%attr(755,root,root) %{_libdir}/opensips/modules/sipcapture.so
%attr(755,root,root) %{_libdir}/opensips/modules/sip_i.so
%attr(755,root,root) %{_libdir}/opensips/modules/sipmsgops.so
%attr(755,root,root) %{_libdir}/opensips/modules/siprec.so
%attr(755,root,root) %{_libdir}/opensips/modules/sl.so
%attr(755,root,root) %{_libdir}/opensips/modules/speeddial.so
%attr(755,root,root) %{_libdir}/opensips/modules/sql_cacher.so
%attr(755,root,root) %{_libdir}/opensips/modules/sst.so
%attr(755,root,root) %{_libdir}/opensips/modules/statistics.so
%attr(755,root,root) %{_libdir}/opensips/modules/status_report.so
%attr(755,root,root) %{_libdir}/opensips/modules/stir_shaken.so
%attr(755,root,root) %{_libdir}/opensips/modules/stun.so
%attr(755,root,root) %{_libdir}/opensips/modules/tcp_mgm.so
%attr(755,root,root) %{_libdir}/opensips/modules/textops.so
%attr(755,root,root) %{_libdir}/opensips/modules/tls_mgm.so
%attr(755,root,root) %{_libdir}/opensips/modules/tls_openssl.so
%attr(755,root,root) %{_libdir}/opensips/modules/tm.so
%attr(755,root,root) %{_libdir}/opensips/modules/topology_hiding.so
%attr(755,root,root) %{_libdir}/opensips/modules/tracer.so
%attr(755,root,root) %{_libdir}/opensips/modules/uac_auth.so
%attr(755,root,root) %{_libdir}/opensips/modules/uac_redirect.so
%attr(755,root,root) %{_libdir}/opensips/modules/uac_registrant.so
%attr(755,root,root) %{_libdir}/opensips/modules/uac.so
%attr(755,root,root) %{_libdir}/opensips/modules/userblacklist.so
%attr(755,root,root) %{_libdir}/opensips/modules/usrloc.so
%attr(755,root,root) %{_libdir}/opensips/modules/uuid.so
%attr(755,root,root) %{_libdir}/opensips/modules/xcap_client.so
%attr(755,root,root) %{_libdir}/opensips/modules/xcap.so
%attr(755,root,root) %{_libdir}/opensips/modules/xml.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/db_berkeley
%{_datadir}/%{name}/dbtext
%{_datadir}/%{name}/menuconfig_templates
%{_datadir}/%{name}/pi_http
%{_mandir}/man5/opensips.cfg.5*
%{_mandir}/man8/opensips.8*

%files xmpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/jabber.so
%attr(755,root,root) %{_libdir}/opensips/modules/xmpp.so
%attr(755,root,root) %{_libdir}/opensips/modules/pua_xmpp.so

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/db_mysql.so
%{_datadir}/%{name}/mysql
%endif

%if %{with pgsql}
%files postgres
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/db_postgres.so
%{_datadir}/%{name}/postgres
%endif

%if %{with sqlite}
%files sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/db_sqlite.so
%{_datadir}/opensips/sqlite
%endif

%if %{with json}
%files json
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/json.so
%endif

%if %{with json}
%files cgrates
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/cgrates.so
%endif

%if %{with memcached}
%files memcached
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/cachedb_memcached.so
%endif

%if %{with radius}
%files radius
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/dictionary.opensips
%attr(755,root,root) %{_libdir}/opensips/modules/aaa_radius.so
%endif

%if %{with odbc}
%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/db_unixodbc.so
%endif

%if %{with geoip}
%files mmgeoip
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/mmgeoip.so
%endif

%if %{with ldap}
%files ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/h350.so
%attr(755,root,root) %{_libdir}/opensips/modules/ldap.so
%endif

%if %{with carrierroute}
%files carrierroute
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/carrierroute.so
%endif

%if %{with osp}
%files osp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/osp.so
%endif

%files snmpstats
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/snmpstats.so

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/db_perlvdb.so
%attr(755,root,root) %{_libdir}/opensips/modules/perl.so
%{_libdir}/opensips/perl

%files -n mibs-%{name}
%defattr(644,root,root,755)
%{_datadir}/mibs/*

%if %{with redis}
%files redis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/cachedb_redis.so
%endif

%if %{with microhttpd}
%files httpd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/httpd.so
%attr(755,root,root) %{_libdir}/opensips/modules/mi_http.so
%endif

%if %{with rabbitmq}
%files rabbitmq
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/event_rabbitmq.so
%attr(755,root,root) %{_libdir}/opensips/modules/rabbitmq.so
%attr(755,root,root) %{_libdir}/opensips/modules/rabbitmq_consumer.so
%endif

%if %{with kafka}
%files kafka
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/event_kafka.so
%endif
