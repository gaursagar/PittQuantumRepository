# Many Thanks

The Pitt Quantum Repository is possible thanks to much support, some financial and some technical.

## Financial

PQR has received financial support from multiple sources, including:

* **[Camille and Henry Dreyfus Foundation](http://www.dreyfus.org)** - A major "Special Grant in the Chemical Sciences" to begin the service.
* **[The Dietrich School of Arts and Sciences](http://www.as.pitt.edu/)** - Continuing support from the University of Pittsburgh.
* **[Department of Chemistry, University of Pittsburgh](http://www.chem.pitt.edu/)** - Continuing support from the chemistry department, a leader in molecular visualization and chemical education.

## Technical

Molecules in the PQR are systematically generated, but also come from many open databases, including:

* **[NIH PubChem](https://pubchem.ncbi.nlm.nih.gov/)** - Including all compounds on the [CID-MeSH](ftp://anonymous@ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/CID-MeSH) list
* **[MMFF94 Validation Set](http://ccl.net/cca/data/MMFF94/)**
* **[Protein Databank Ligand Expo](http://ligand-expo.rcsb.org/ld-download.html)**
* **[St. Olaf Cool Molecules](http://www.stolaf.edu/depts/chemistry/mo/struc/)**

Multiple programs and web services are used in processing and displaying the molecules, including:

* **[3Dmol.js](http://3dmol.csb.pitt.edu/)** - To visualize molecular data
* **[MOPAC 2012](http://openmopac.net/)** - For PM7 semiempirical quantum calculations
* **[Open Babel](http://openbabel.org/)** - For batch processing and cheminformatics
* **[OpenEye Lexichem TK](http://www.eyesopen.com/lexichem-tk)** - For systematic naming
* **[EZID](http://ezid.cdlib.org)** - To generate Digital Object Identifiers (DOIs)

The backend is largely written in [Flask](http://flask.pocoo.org/).  

Several key modules are used to provide users with extra data on the molecules:  
* **[ChemSpiPy](http://chemspipy.readthedocs.org/)** - To access the [ChemSpider](http://chemspider.com/) webservice  
* **[CIRPy](http://cirpy.readthedocs.org/)** - To access the [NIH Chemical Resolver](http://cactus.nci.nih.gov/chemical/structure)  
* **[PubChemPy](http://pubchempy.readthedocs.org/)** - To access the [NIH PubChem REST](https://pubchem.ncbi.nlm.nih.gov) service  
* **[mwclient](https://github.com/mwclient/mwclient)** - To search [Wikipedia](https://en.wikipedia.org/) for molecules  

