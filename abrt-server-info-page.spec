Summary: Web page with summary of ABRT services
Name: abrt-server-info-page
Version: 1.2
Release: 1%{?dist}
License: GPLv3+
URL: https://github.com/marusak/abrt-server-info-page
# source is created by:
# git clone
# cd abrt-server-info-page; tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python2-devel

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
mkdir -p %{buildroot}/%{python_sitelib}/abrt-server-info-page/static
mkdir -p %{buildroot}/%{python_sitelib}/abrt-server-info-page/static/js
mkdir -p %{buildroot}/%{python_sitelib}/abrt-server-info-page/static/css
mkdir -p %{buildroot}/%{python_sitelib}/abrt-server-info-page/static/fonts
mkdir -p %{buildroot}/%{python_sitelib}/abrt-server-info-page/templates
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
cp -a abrt_server_info_page.py %{buildroot}/%{python_sitelib}/abrt-server-info-page
cp -a abrt_server_info_page.wsgi %{buildroot}/%{python_sitelib}/abrt-server-info-page
cp -a config.py %{buildroot}/%{python_sitelib}/abrt-server-info-page
cp -a config/abrt-server-info-page.conf %{buildroot}/%{_sysconfdir}/httpd/conf.d/
cp -a templates/index.html %{buildroot}/%{python_sitelib}/abrt-server-info-page/templates
cp -a static/* %{buildroot}/%{python_sitelib}/abrt-server-info-page/static

%files
%config(noreplace) %{_sysconfdir}/httpd/conf.d/abrt-server-info-page.conf
%{python_sitelib}/abrt-server-info-page
%license LICENSE

%post
systemctl condrestart httpd

%changelog
* Sat Feb 04 2017 Matej Marusak <marusak.matej@gmail.com> 1.2-1
- Add license into specfile (marusak.matej@gmail.com)
- Add BuildRequires into specfile (marusak.matej@gmail.com)
- Create LICENSE (marusak.matej@gmail.com)
- Fix wrong command in specfile (mmarusak@redhat.com)
- Add README (marusak.matej@gmail.com)
- Remove unused BuildRequires from specfile (marusak.matej@gmail.com)
* Thu Jan 19 2017 Matej Marusak <mmarusak@redhat.com> 1.1-1
- Initial package

