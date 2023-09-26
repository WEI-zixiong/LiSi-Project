# LiSi Project 

## Construcing Machine Learning Potentials
 
1. Preprocessing: 

   (1) convert the data sets in XCrySDen structure format (XSF) to the LAMMPS data file format.
   
2. Visualization:

   (1) monitor the training of ML potential;

   (2) visualize the distribution of the data sets.
   
## Running Molecular Dynamics Simulation

3. Construction of models:

   (0) generate Coarse-Grained (CG) particles through LAMMPS simulation;
   
   (1) replicate unit cells in 3 dimensions to form bulk structures;
   
   (2) cut spheres/nanoparticles from replicated bulk structures;
   
   (3) replace different-sized CG particles with different all-atom nanoparticles.
