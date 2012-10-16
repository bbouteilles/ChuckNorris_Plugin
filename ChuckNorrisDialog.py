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
# chargement des modules Qt génériques
from PyQt4 import QtCore, QtGui
import fonctions
from random import choice
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis import core

# chargement du fichier d'interface graphique
from Ui_ChuckNorris import Ui_ChuckNorris



# creation de la boite de dialogue, appelée dans la méthode Run de la Classe principale
class ChuckNorrisDialog (QtGui.QDialog):
	
	def __init__(self):
		
		QtGui.QDialog.__init__(self)
		# Appel de la classe créée dans Qt Designer, importée en début de fichier
		self.ui = Ui_ChuckNorris ()
		self.ui.setupUi(self)
		fact = fonctions.choisir_facts()
		self.ui.lbl_fact.setText(unicode(fact,('cp1252')))
		self.directory = QtCore.QFileInfo(core.QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/ChuckNorris"
		#self.ui.lbl_image.setPixmap(QtGui.QPixmap('chuck.png'))
		#QMessageBox.information(self.iface.mainWindow(), QCoreApplication.translate(titre, titre), QCoreApplication.translate(texte,texte))
		#QMessageBox.warning(self,'coucou','toto')
			
			