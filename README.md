# pyVoltic

What is it?

This is a framework for the Volz Miller equations which is an approach to static or dynamic modelling of disease on a heterogenous network. At the moment the package contains the following models;
- Volz Static Random Network Model  
- Volz Meyers Neighbour Exchange Network Model
- Edge Based Compartmental Model (EBCM): Static Configuration Model Network
- EBCM: Mean Field Social Heterogeneity
- EBCM: Dyanmic Fixed Degree

This package aims to help people make use of these very powerful models by allowing the user to pass their own probability generating functions, as well as make use of those which are included in the package. 

This package would not have been possible without the incredible work done by Erik Volz (https://github.com/emvolz), Lauren Ancel Meyers (https://scholar.google.com/citations?user=KKiQaBoAAAAJ&hl=en) and Joel C Miller (https://github.com/joelmiller). It is encouraged to follow and read their papers to better understand these models.

> [Volz Static Random Network Model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7080148/pdf/285_2007_Article_116.pdf)
    
> [Volz Mercer Neighbour Exchange Network Model](https://royalsocietypublishing.org/doi/10.1098/rspb.2007.1159)

> [Edge Based Compartmental Model Framework can found here](https://arxiv.org/pdf/1106.6320)

Further Reading:
To learn more about creating these systems the following books have been incredibly useful in developing understanding:
> [Epidemics on Networks (book and python package)](https://link.springer.com/book/10.1007/978-3-319-50806-1)
> 
> [Dynamical Systems on Networks](https://link.springer.com/book/10.1007/978-3-319-26641-1)

# Documentation

The package was designed to be easy to use out of the box, once installed you import and instantiate the model which you want to use. When instantiating the model you will need to pass it either the probability generating function and its first and second derivative - you can write this yourself or use the poisson or powerlaw with max degree cut off which is included in the package. Or you can even pass a networkx.Graph object or a dictionary which details the degree distribution. Then you will pass the max number of time steps and $epsilon$ which is the fraction who start infected.

After this it is just running `model.run_simulation(kwargs)` passing the necessary arguments for the respective model. This will return a results class, this class has visualisation methods which can display;

    - Each Compartment Over Time

    - The SIR Compartments

    - The Cumulative Incidence
    
When comparing different simulation runs there are also functions which can be used to compare each of the cumulative incidences.


The class structure VolzFramework is designed to be a flexible approach in implementing similar models which make use of ordinary differential equations and probability generating functions. Hopefully others moving forward can use this framework to create classes for more dyanmical equations and these can be included in this package.


Future Implementation Plans:

Continue Implementing Edge Based Compartmental Models:
https://royalsocietypublishing.org/doi/10.1098/rsif.2011.0403

https://arxiv.org/pdf/1106.6320

https://arxiv.org/abs/1106.6319

https://arxiv.org/abs/1106.6344


## Dependencies

- [Numpy](https://numpy.org)

- [networkx](https://networkx.org)

- [scipy](https://scipy.org)

# License

# Contribution

If you wish to contribute feel free to add an issue or create a pull request with the feature or correction which you intend and it will get looked at in due course.


