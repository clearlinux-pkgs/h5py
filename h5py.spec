#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : h5py
Version  : 2.10.0
Release  : 60
URL      : https://files.pythonhosted.org/packages/5f/97/a58afbcf40e8abecededd9512978b4e4915374e5b80049af082f49cebe9a/h5py-2.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5f/97/a58afbcf40e8abecededd9512978b4e4915374e5b80049af082f49cebe9a/h5py-2.10.0.tar.gz
Summary  : Read and write HDF5 files from Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: h5py-license = %{version}-%{release}
Requires: h5py-python = %{version}-%{release}
Requires: h5py-python3 = %{version}-%{release}
Requires: numpy
Requires: six
BuildRequires : Cython-python
BuildRequires : buildreq-distutils3
BuildRequires : hdf5-dev
BuildRequires : numpy
BuildRequires : openblas
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-pkgconfig
BuildRequires : python3-dev
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
The h5py package provides both a high- and low-level interface to the HDF5
        library from Python. The low-level interface is intended to be a complete
        wrapping of the HDF5 API, while the high-level component supports  access to
        HDF5 files, datasets and groups using established Python and NumPy concepts.
        
        A strong emphasis on automatic conversion between Python (Numpy) datatypes and
        data structures and their HDF5 equivalents vastly simplifies the process of
        reading and writing data from Python.
        
        Supports HDF5 versions 1.8.4 and higher.  On Windows, HDF5 is included with
        the installer.

%package license
Summary: license components for the h5py package.
Group: Default

%description license
license components for the h5py package.


%package python
Summary: python components for the h5py package.
Group: Default
Requires: h5py-python3 = %{version}-%{release}

%description python
python components for the h5py package.


%package python3
Summary: python3 components for the h5py package.
Group: Default
Requires: python3-core
Provides: pypi(h5py)
Requires: pypi(numpy)

%description python3
python3 components for the h5py package.


%prep
%setup -q -n h5py-2.10.0
cd %{_builddir}/h5py-2.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624468133
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build  %{?_smp_mflags}

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/h5py
cp %{_builddir}/h5py-2.10.0/LICENSE %{buildroot}/usr/share/package-licenses/h5py/75e30d84df76091f6aaa16a714073a72127a8158
cp %{_builddir}/h5py-2.10.0/docs/licenses.rst %{buildroot}/usr/share/package-licenses/h5py/798e927484e8c8719ad65c03fc46e82817d81a2b
cp %{_builddir}/h5py-2.10.0/licenses/license.txt %{buildroot}/usr/share/package-licenses/h5py/0bd06351d2b2e5f425c31b1ef097c8f6079a5eb1
cp %{_builddir}/h5py-2.10.0/lzf/LICENSE.txt %{buildroot}/usr/share/package-licenses/h5py/ed783081e442176401a5234bb9073175f3e956b9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/h5py/0bd06351d2b2e5f425c31b1ef097c8f6079a5eb1
/usr/share/package-licenses/h5py/75e30d84df76091f6aaa16a714073a72127a8158
/usr/share/package-licenses/h5py/798e927484e8c8719ad65c03fc46e82817d81a2b
/usr/share/package-licenses/h5py/ed783081e442176401a5234bb9073175f3e956b9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
