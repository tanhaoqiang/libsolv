from glob import glob
import pip
pip.main(["install", glob("dist/*.whl")[0]])
import solv
pool = solv.Pool()
repo = pool.add_repo("repo")
repodata = repo.add_repodata()
pkg = repo.add_solvable()
pkg.name = 'example'
pkg.evr = "{epoch}:{version}-{release}".format(epoch=0,version="1.0", release="1")
pkg.arch = 'aarch64'
pkg.add_deparray(solv.SOLVABLE_PROVIDES, pool.rel2id(pkg.nameid, pkg.evrid, solv.REL_EQ))
pool.createwhatprovides()

pool.setarch('aarch64')
jobs = []
jobs.append(pool.select(pkg.name, solv.Selection.SELECTION_PROVIDES).jobs(solv.Job.SOLVER_INSTALL))

header = "<asm/example.h>"
pkg.add_deparray(solv.SOLVABLE_PROVIDES, pool.str2id(header))
pool.createwhatprovides()
jobs.append(pool.select(header, solv.Selection.SELECTION_PROVIDES).jobs(solv.Job.SOLVER_INSTALL))

dirid = repodata.str2dir("/usr/include")
repodata.add_dirstr(pkg.id, solv.SOLVABLE_FILELIST, dirid, "example.h")
repodata.internalize()
pool.addfileprovides()
pool.createwhatprovides()
jobs.append(pool.select("/usr/include/example.h", solv.Selection.SELECTION_FILELIST).jobs(solv.Job.SOLVER_INSTALL))

for i, job in enumerate(jobs):
    print(i, job)
for i, job in enumerate(jobs):
    assert len(job) > 0, f"jobs {i} is empty"
