Name:           mac-robber
Version:        1.02
Release:        18
Summary:        Tool to create a timeline of file activity for mounted file systems
License:        GPLv2+
URL:            http://sourceforge.net/projects/mac-robber/
Source0:        http://downloads.sourceforge.net/mac-robber/mac-robber-1.02.tar.gz
BuildRequires:  gcc

%description
mac-robber is a digital forensics and incident response tool that can be used
with The Sleuth Kit to create a timeline of file activity for mounted
file systems.

%prep
%setup -q

%build
%make_build GCC_OPT="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 mac-robber %{buildroot}%{_bindir}

%files
%doc CHANGES README
%license COPYING
%{_bindir}/mac-robber

%changelog
* Mon Dec 9 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.02-18
- Package init
