# Maintainer: Dmitry Grebenin <grebenin.dmitry@gmail.com>

_name=
pkgname=python-samsung-wakeonlan
pkgver=1.0.0
pkgrel=1
arch=('x86_64')

pkgdesc='Small script to toggle Tizen TV power'

depends=('python' 'python-requests' 'python-wakeonlan' 'python-samsungtvws')
makedepends=('cmake')

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/example/myprog/archive/v${pkgver}.tar.gz")
sha256sums=('SKIP')   # replace with real hash before publishing

# ── Optional ──
epoch=
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
noextract=()
validpgpkeys=()

# ── Functions ──
prepare() {
    cd "$srcdir/$pkgname-$pkgver"
    # apply patches, submodules, etc.
}

build() {
    cd "$srcdir/$pkgname-$pkgver"
    ./configure --prefix=/usr
    make
}

check() {
    cd "$srcdir/$pkgname-$pkgver"
    make check
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    make DESTDIR="$pkgdir/" install
}
