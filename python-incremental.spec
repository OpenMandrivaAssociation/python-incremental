Summary:	Library for versioning Python projects
Name:		python-incremental
Version:	24.11.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/incremental/
Source0:	https://files.pythonhosted.org/packages/source/i/incremental/incremental-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:  python-hatchling
BuildRequires:  python-pip
BuildSystem:    python

%description
Library for versioning Python projects

%files
%defattr(0644,root,root,0755)
%{_bindir}/incremental
%{py_sitedir}/incremental
%{python_sitelib}/incremental-%{version}.dist-info
