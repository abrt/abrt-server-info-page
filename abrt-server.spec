Summary: Web page with summary of ABRT services
Name: abrt-server-info-page
Version: 1.2
Release: 1%{?dist}
License: GPLv3+
URL: https://github.com/marusak/Abrt-server
# source is created by:
# git clone
# cd abrt-server-info-page; tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: intltool
BuildRequires: libtool
BuildRequires: texinfo
BuildRequires: asciidoc
BuildRequires: xmlto

Requires: python-flask >= 0.10
Requires: httpd
Requires: mod_wsgi

%description
Web page for use as front page of ABRT servers. Contains information about
ABRT's products.

%prep
%setup -q

%install
mkdir -p %{buildroot}
mkdir -p %{buildroot}/%{python_sitelib}/Abrt-server/static
mkdir -p %{buildroot}/%{python_sitelib}/Abrt-server/static/js
mkdir -p %{buildroot}/%{python_sitelib}/Abrt-server/static/css
mkdir -p %{buildroot}/%{python_sitelib}/Abrt-server/static/fonts
mkdir -p %{buildroot}/%{python_sitelib}/Abrt-server/templates
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
cp -a abrt_server.py %{buildroot}/%{python_sitelib}/Abrt-server
cp -a abrt_server.wsgi %{buildroot}/%{python_sitelib}/Abrt-server
cp -a config.py %{buildroot}/%{python_sitelib}/Abrt-server
cp -a config/abrt-server.conf %{buildroot}/%{_sysconfdir}/httpd/conf.d/
cp -a templates/index.html %{buildroot}/%{python_sitelib}/Abrt-server/templates
cp -a static/* %{buildroot}/%{python_sitelib}/Abrt-server/

%files
%config(noreplace) %{_sysconfdir}/httpd/conf.d/abrt-server.conf
%{python_sitelib}/Abrt-server

%post
systemctl httpd condrestart

%changelog
* Thu Jan 19 2017 Matej Marusak <mmarusak@redhat.com> 1.2-1
- initial version
