# template: default
%global gem_name connection_pool

Name: rubygem-%{gem_name}
Version: 2.4.1
Release: 1%{?dist}
Summary: Generic connection pool for Ruby
License: MIT
URL: https://github.com/mperham/connection_pool
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: ruby >= 2.5.0
BuildRequires: ruby >= 2.5.0
BuildRequires: rubygems-devel
BuildArch: noarch
# end specfile generated dependencies

%description
Generic connection pool for Ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/Changes.md
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%exclude %{gem_instdir}/connection_pool.gemspec

%changelog
* Sun May 21 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.4.1-1
- Update to 2.4.1

* Sun Apr 02 2023 Foreman Packaging Automation <packaging@theforeman.org> 2.4.0-1
- Update to 2.4.0

* Sun Oct 02 2022 Foreman Packaging Automation <packaging@theforeman.org> 2.3.0-1
- Update to 2.3.0

* Wed Jul 06 2022 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 2.2.5-1
- Update to 2.2.5

* Thu Mar 11 2021 Eric D. Helms <ericdhelms@gmail.com> - 2.2.2-3
- Rebuild against rh-ruby27

* Tue Apr 07 2020 Zach Huntington-Meath <zhunting@redhat.com> - 2.2.2-2
- Bump to release for EL8

* Wed Oct 16 2019 Adam Ruzicka <aruzicka@redhat.com> 2.2.2-1
- Add rubygem-connection_pool generated by gem2rpm using the scl template
