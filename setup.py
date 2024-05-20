from setuptools import find_packages, setup

def main():
    setup(
        name="fansipan_afs",
        description="Basic data models of the Analytics Feature Space for ML Detection",
        long_description=open('README.md',encoding="utf-8").read() +
        '\n\n' + open('CHANGELOG.txt',encoding="utf-8").read(),
        long_description_content_type='text/markdown',
        version=open('VERSION',encoding="utf-8").read(),
        author='linh truong',
        author_email='linh.truong@daienso.com',
        keywords=['python', 'daienso', 'fansipan','afs'],
        license='Apache 2.0',
        include_package_data=True,
        packages=find_packages(
            where='src',
            include=['fansipan_afs*']
        ),
        package_dir={'': 'src'},
        install_requires=[line.strip() for line in  open('requirements.txt',encoding="utf-8").readlines()],
        zip_safe=False,
        classifiers=[
            'Development Status :: 3 - Alpha',
        ],
    )


if __name__ == '__main__':
    main()
