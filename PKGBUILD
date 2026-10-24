# Maintainer: Dmitry Grebenin <grebenin.dmitry@gmail.com>

_name=samsung-powertoggle
pkgname=python-samsungpowertoggle
pkgver=1.0.1
pkgrel=1
pkgdesc='Samsung Smart TV power toggle'
url='https://github.com/BoopSnoot/samsung-powertoggle'
arch=('any')
license=('LGPL-3.0')
depends=('python>=3.10' 'python-samsungtvws' 'python-requests')
makedepends=('python-build' 'python-installer' 'python-wheel')
source=("$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('197ed331b487e7de8f9240d15ff5592d4b719f57c0d09d89b556197518aea6ef')

build() {
	cd $_name-$pkgver
	python -m build --wheel --no-isolation
}

package() {
	cd $_name-$pkgver
	python -m installer --destdir="$pkgdir" dist/*.whl
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
