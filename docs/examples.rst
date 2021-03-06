Sample models
=============

CAIRIS comes with a number of different example models.  These illustrate how CAIRIS can be used, and -- in some cases -- provide templates to inspire your own use of the platform.

Exemplars
---------

CAIRIS comes with two complete system specifications.  These can be found in the cairis/examples/exemplars directory.

NeuroGrid
~~~~~~~~~

NeuroGrid is a a data grid for neuroscience research.  The sensitive of clinical data processed by NeuroGrid and its distributed nature drives the need to find secure and effective ways of accessing and managing it.  This exemplar is restricted to the upload and download of data to and from NeuroGrid.  This exemplar also comes with a physical locations file (Computing Laboratory) and an architectural pattern (WebDAV).


ACME Water
~~~~~~~~~~

ACME Water is a fictional water company concerned with the delivery of wastewater and cleanwater services in a specific geographic region of the UK.  This exemplar specifies a secure operating environment for SCADA, telemetry, and control systems associated with assets owned and operated by ACME.  This exemplar also comes with a physical localtions file (Poole Waste Water Treatment Works).

webinos
~~~~~~~

Although this is not part of the CAIRIS repository, the design data used to build `webinos <https://en.wikipedia.org/wiki/Webinos>`_ is available on `webinos-design-data GitHub repository <https://github.com/webinos/webinos-design-data>`_ and is compatible with CAIRIS.  The webinos design data repository is a good example of a non-trivial specification, with input data in a variety of formats including spreadsheets, text files, CAIRIS models.  A script is used to convert these files into CAIRIS models, which is then imported.  See the README file on the webinos-design-data repository for more information.


Threat and Vulnerability Directories
------------------------------------

These are libraries of importable threats and vulnerabilities, and can be found in the cairis/examples/directories directory.

CWE/CAPEC
~~~~~~~~~

cwecapec_directory.xml contains a selection of threats and vulnerabilities from CWE and CAPEC.  To import this, it is first necessary to import cairis/examples/threat_vulnerability_types/cwecapec_tv_types.xml.

ICS Protection Profile
~~~~~~~~~~~~~~~~~~~~~~

ics_directory.xml contains a selection of threats and vulnerabilities from the System Protection Profile - Industrial Control Systems issued by NIST.  To import this, it is first necessary to import cairis/examples/threat_vulnerability_types/ics_tv_types.xml.

OWASP
~~~~~

owasp_directory.xml contains a selection of threats and vulnerabilties drawn from the OWASP body of knowledge.  To import this, it is first necessary to import cairis/examples/threat_vulnerability_types/owasp_tv_types.xml.
