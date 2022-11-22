#!/usr/bin/env python
# coding: utf-8
from SPARQLWrapper import SPARQLWrapper, JSON
import ipywidgets as widgets

#Note: DO NOT EDIT
#Function to fetch vocabulary terms.
def get_vocab(collection, graph=None):
    vocabno = SPARQLWrapper("http://vocab.met.no/collection/sparql")
    if graph is not None:
        grfstr = 'FROM ' + graph + ' '
    else:
        grfstr = ''

    prefixes = '''
        prefix skos:<http://www.w3.org/2004/02/skos/core#>
        prefix text:<http://jena.apache.org/text#>
        prefix rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix owl:<http://www.w3.org/2002/07/owl#> 
        prefix dc:<http://purl.org/dc/terms/>'''

    vocabularies = '''select distinct ?concname %(graph)s WHERE {
        ?collection skos:prefLabel "%(collection)s"@en .
        ?collection skos:member ?concept .
        ?concept skos:prefLabel ?concname .
        }'''

    vocabno.setQuery(prefixes + vocabularies % {'collection': collection, 'graph': grfstr})
    #print(prefixes + vocabularies % {'collection': collection, 'graph': grfstr})
    vocabno.setReturnFormat(JSON)
    vocabs = vocabno.query().convert()
    members = []
    for result in vocabs["results"]["bindings"]:
        members.append(result['concname']['value'])

    return(members)

#Operational status vocabulary: describe operational status of datasets handled. 
#For definitions of terms see: https://vocab.met.no/mmd/Operational_Status
operational_status = widgets.Box([
        widgets.HTML(value='Select a <a href="https://vocab.met.no/mmd/Operational_Status">value for the operational status</a> of the dataset'),
        widgets.RadioButtons(
        options=get_vocab('Operational Status'),
        disabled=False,
        value='Scientific')])

#Activity type vocabulary: describe activity types. Activity types are used to identify the origin of the dataset. 
#For definitions of terms see: https://vocab.met.no/mmd/Activity_Type
activity_type = widgets.Box([
        widgets.HTML(value='Select a <a href="https://vocab.met.no/mmd/Activity_Type">value for the activity type</a> of the dataset'),
        widgets.SelectMultiple(
        options=get_vocab('Activity Type'),
        disabled=False,
        layout=widgets.Layout(height='250px'))])

#ISO topic category vocabulary: terms defined by ISO describing data themes.
#For definitions of terms see: https://vocab.met.no/mmd/ISO_Topic_Category
iso_topic_category = widgets.Box(
    [
        widgets.HTML(value='Select a <a href="https://vocab.met.no/mmd/ISO_Topic_Category">value for the ISO topic category</a> of the dataset'),
        widgets.SelectMultiple(
        options=get_vocab('ISO Topic Category'),
        disabled=False,
        layout=widgets.Layout(height='350px'))        
    ]
)
