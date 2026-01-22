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

### 1. [/Weights](https://github.com/bavaria-analysis/soybean-suitability/tree/main/Weights)
This folder contains the mathematical foundation for the multicriteria analysis.

· AHP Calculation.xlsx: The Microsoft Excel spreadsheet containing the pairwise comparison matrix for the seven criteria. It includes the calculation of the Cumulative Weight Index (CWI) and the Consistency Ratio (CR) of 0.028.

### 2. [/Rasters](https://github.com/bavaria-analysis/soybean-suitability/tree/main/Rasters)
This directory holds the seven reclassified thematic layers (.tiff) used as inputs for the weighted overlay analysis, embedded in zipped files. All rasters are harmonized to a 25m resolution and the ETRS 1989 UTM Zone 32N coordinate system.

· pH.zip: Reclassified soil pH based on FAO standards (Optimal: 6-7).

· Organic_Carbon.zip: Reclassified Soil Organic Carbon (Optimal: 2.4-3.5%).

· Slope.zip: Terrain slope derived from SRTM DEM (Optimal: 0-2%).

· Drainage.zip: Topographic Wetness Index (TWI) representing soil moisture.

· LULC.zip: Land use classification identifying arable vs. non-arable zones.

· Temperature.zip: Temperature suitability based on Bavarian climatic mean.

· Precipitation.zip: Precipitation suitability grids.

### 3. [/Results](https://github.com/bavaria-analysis/soybean-suitability/tree/main/Results)
· Soybean Suitability Layer.zip: the final output of the weighted overlay analysis, categorizing land into classes S1 (Highly Suitable) through N2 (Permanently Unsuitable).

· NDVI_Validation.zip: The reclassified NDVI surface used for indirect validation.

· Suitability Analysis_Statistics.xlsx: Tabular statistics of reclassified criteria, final suitability surface and overlap result from indirect validation.

# 3. How to reproduce the results
Step 1: Download the reclassified rasters from this repository.

Step 2: Open the AHP Calculation Excel file to see the criteria weights.

Step 3: Use the "Weighted Overlay" tool in ArcGIS Pro with the weights provided in the Excel file.

# 5. Results
The assessment indicated drainage and LULC as the most influential factors, followed by slope, pH, and Organic Carbon (OC). The final suitability map revealed that the Highly Suitable class covered 14.16% of the region, the Moderately and Marginally Suitable classes covered 54.89% and 27.81% of the region. Also, the Unsuitable Areas accounted for 3.14% of the study area.
Indirect validation using NDVI overlap confirmed the predictive power of the suitability analysis, showing a strong positive correlation between highly suitable zones and areas of healthy vegetation growth.

# 6. Credits
