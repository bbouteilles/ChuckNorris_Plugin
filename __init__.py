"""
/***************************************************************************
Name			 	 : Chuck Norris Plugin
Description          : Plugin d'entraînement
Date                 : 16/Octobre/2012 
copyright            : (C) 2012 by Bertrand Bouteilles
email                : bertrand.bouteilles@developpement-durable.gouv.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
# coding: utf-8

def name(): 
  return "ChuckNorris" 
def description():
  return "Plugin for training, and for fun (french)"
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "1.5"
def author():
    return "Bertrand Bouteilles" 
def email():
	return "bertrand.bouteilles@developpement-durable.gouv.fr"
def classFactory(iface): 
  from ChuckNorris import ChuckNorris 
  return ChuckNorris(iface)
