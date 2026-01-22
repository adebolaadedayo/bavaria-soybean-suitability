# Land Suitability for Soybean Cultivation in Bavaria, Germany, using Multi-Criteria GIS Analysis

# 1. Abstract
The increasing need for soybeans, as well as effective agricultural land management in Europe, has encouraged the development of land suitability calculation methods. This study presents a GIS-based multi-criteria decision analysis (MCDA) to evaluate land suitability for soybean cultivation in Bavaria, Germany, supporting sustainable agricultural expansion. Seven key environmental variables, including soil pH, organic carbon, slope, drainage, land use, temperature, and precipitation, were considered for the land suitability analysis. Each criterion was weighted by a pairwise comparison using AHP and integrated to generate a weighted overlay surface. Results indicate that 14.16% of Bavaria is highly suitable for production, particularly within the central and south-central regions, while 54.89% is moderately suitable. The model’s predictive accuracy was verified through an indirect validation using Sentinel-2 NDVI imagery, achieving a 61.08% spatial overlap with highly suitable zones. This study provides an actionable decision-support tool for stakeholders to optimize soybean yields and reduce import dependency.

# 2. Data Availability
# Data sources
This study utilised topsoil data, including Soil pH and Soil Organic Carbon (SOC) for Europe in raster format, which are available for download from the European Soil Data Centre (ESDAC) through a request form at https://esdac.jrc.ec.europa.eu/resource-type/european-soil-database-soil-properties.

Elevation and terrain derivatives (slope and drainage) were extracted from the SRTM Digital Elevation Model (DEM) provided by the European Environment Agency (https://ec.europa.eu/eurostat/web/gisco/geodata/digital-elevation-model/eu-dem). Climatic grids for temperature and precipitation were obtained from Deutscher Wetterdienst (http://www.dwd.de/).

Land Use Land Cover (LULC) data were derived from Sentinel-2 imagery (2024) acquired from ArcGIS Living Atlas (https://livingatlas.arcgis.com/landcoverexplorer/). Also, Sentinel-2 imagery, captured in August 2025 during the peak season of soybean growth, was obtained from Copernicus (https://browser.dataspace.copernicus.eu/)  and used to compute the NDVI, which served as an indirect validation of the final suitability values.

All datasets were harmonized to the ETRS 1989 UTM Zone 32N coordinate system to ensure spatial alignment and resampled to a resolution of 25 meters. In addition, the entire dataset was clipped to the study area’s boundary obtained from the Database of Global Administrative Areas (https://gadm.org/data.html).

Analytical Hierarchy Process (AHP) weightings were calculated in Microsoft Excel based on the scale presented by Saaty (1986), while the weighted overlay analysis was conducted in ArcGIS Pro software, version 3.5, developed by ESRI (https://www.esri.com/).

All reclassified rasters, along with the AHP weighting calculations and the final suitability map, are available and can be accessed on this public GitHub repository.


# File Dictionary
This repository is organized into specific directories to ensure the transparency and reproducibility of the suitability analysis.

### 1. /Weights
This folder contains the mathematical foundation for the multicriteria analysis.

· AHP_Calculation.xlsx: The Microsoft Excel spreadsheet containing the pairwise comparison matrix for the seven criteria. It includes the calculation of the Cumulative Weight Index (CWI) and the Consistency Ratio (CR) of 0.028


# 3. Methodology and Software Requirements
vvv


# 4. How to reproduce the results



# 5. Results



# 6. Credits
