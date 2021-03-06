=======
History
=======

0.11.3  (2021-01-30)
--------------------
* Added cm.get_log function for concistency with the rest of the interface.

0.11 (2021-01-16)
-------------------
* Introduced GitProject and SvnProject to ease reference the tree, client and utility functions.

0.10 (2020-12-12)
-------------------
* Fixed handling of files with commas in the name.
* Fixed visualization of pandas example as html.
* Leveraged new pandas dtypes.
* Introduced type hints in code base.
* Switched backend to GitHub actions from travis-ci.

0.9 (2019-09-29)
------------------
* Fixed incorrect usage of subprocess.run(). See https://github.com/elmotec/codemetrics/issues/1.
* Factored common logic between git and svn. Bug fixes.
* Fixed test_core following https://github.com/pandas-dev/pandas/pull/24748 (Pandas 0.25.X)
* Added script `cm_func_stats` that generates statistics on the function passed as argument.
* Added appveyor support for Windows.
* Documentation.
* Fixed retrieval of added and removed lines when there are spaces in a file name.
* Fixed indexed input in `get_mass_changes`.
* Fixed handling of removed files in `svn.get_diff_stats`.
* Fixed handling of branches in `svn.get_diff_stats`.
* Started changing interfaces to leverage apply and groupby.
* Added lines added/removed for Subversion.

0.8 (2019-02-26)
------------------
* Added `svn.get_diff_stats` to retrieve line changes stats per diff.
* Integrated lizard to calculate average and function level cyclomatic complexity.

0.7 (2019-01-09)
----------------
* Function oriented interface.
* Visualization via Vega, Altair.
* Documentation.

0.5 (2018-05-12)
----------------
* First release on PyPI.


