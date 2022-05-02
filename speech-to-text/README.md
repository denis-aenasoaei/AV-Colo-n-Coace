

AV-Colo-n-Coace Speech to Text 
==============================



Instalare dependințe și configurarea mediului 
------------


1. Miniconda https://docs.conda.io/en/latest/miniconda.html Miniconda3 Windows 64-bit



.. code-block:: bash

   conda create --name deepspeech3 python=3.6.9
   conda activate deepspeech3


.. code-block:: bash

   pip install -r requirements.txt

În caz că ffmeg are erori, reinstalarea folosind conda ar trebui să ajute 

.. code-block:: bash

   conda install ffmpeg 


Modelul deepspeech antrenat pentru limba engleză trebuie descărcat (fișierele nu pot fi încarcate în codul sursa pentru că depasesc limita admisă de github):

.. code-block:: bash
    https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
    https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer


Utilizare
-----

.. code-block:: bash

   deepspeech --model ./deepspeech-0.9.3-models.pbmm --scorer ./deepspeech-0.9.3-models.scorer --audio ./audio.wav


In situatia in care autoconversia nu functioneaza (`FileNotFoundError: [Errno 2] SoX not found, use 16000hz files or install it: The system cannot find the file specified`)
Pentru fisierele audio de intrare care au un sample rate diferit de 16000 Hz este necesar o conversie:

.. code-block:: bash

   python conv.py LJ001-0001.wav

