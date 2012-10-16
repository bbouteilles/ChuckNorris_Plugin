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
# Import des librairies Qt (pour l'interface graphique)
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import fonctions
import resources


#. Import de la classe gérant les interactions interface graphique / fonctionnalités (voir plus loin)
from ChuckNorrisDialog import ChuckNorrisDialog


# Début de la classe principale du plugin
class ChuckNorris :

	def __init__(self, iface): # Méthode obligatoire d'initialisation de la classe
		# L'objet iface est une instance de la classe QgisInterface de l'API QGIS
		self.iface = iface # Code à laisser tel quel

	def initGui(self): # Méthode intégrant le plugin à QGIS depuis le gestionnaire d'extensions
		# Création de l'icône qui, une fois cliquée, ouvrira l'interface graphique du plugin
		self.action = QAction(QIcon(":/plugins/ChuckNorris/icon.png" ),u"&Chuck Norris" , self.iface.mainWindow())
		# Ligne qui lance le plugin (méthode « run ») au moment du clic (cf remarque ci-après)
		QObject.connect(self.action, SIGNAL("triggered()" ), self.run)

		# Ajout de l'icône dans le menu « Nom du menu » et dans la barre d'outils
		self.iface.addToolBarIcon(self.action)
		self.iface.addPluginToMenu(u"&Chuck Norris" , self.action)

	def unload(self): # Méthode enlevant les références au plugin dans QGIS
		# Suppression de l'icône dans le menu « Nom du menu » et dans la barre d'outils
		self.iface.removePluginMenu(u"&ChuckNorris" ,self.action)
		self.iface.removeToolBarIcon(self.action)
	from random import choice
	
	def run(self): # Méthode ouvrant l'interface graphique du plugin

		dlg = ChuckNorrisDialog() #le self est nécessaire pour accéder à QGIS dans le fichier ChuckNorrisDialog
		
		#Afficher l'interface graphique
		dlg.show()

		result = dlg.exec_()
		if result == 1:
			pass
