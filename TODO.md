# Corrections

## Key
* RED - Current blocker, eithe a large chunk of work or I am unsure how to progress.
* AMBER - Requires extra work but not a significant time investment
* GREEN - Simple modification/removal


## List

### Simulation experiments

* [RED][DONE] Base line of WSN sending out all data to base station without DPs, i.e. a
simple mutlihop network that sends images directly out via the
shortest route and the base station does the classification. You may
want to consider the base station having MK in one scenario and
HK in another, i.e. two baselines.
	* Adding in tracking of all observations shows 100% delivery (unless saturated), this needs checking
	* Flat routing has not yet been implemented, attempts to do so thus far have produced odd results.
	* Concern that nodes may be receiving/sending in parallel
	* Concern that nodes are processing in serial but processing time is not being taking directly into account

* [RED] Rerun all experiments with the additional scenarios. You should report
the total number of images that were generated, the number that
arrived at the base station and the (ideally) number that were
dropped.
	* Not so much a blocker as a large time commitment, when the above point has been addressed, these can be run 24/7
	* Crippling fear that addressing the above point, as well as this, may go beyond the 3 month commitment.

* [RED] Formalise the description of the experimental design clearly stating what variables were kept constant and which were measured. The simulation chapter needs to include (in addition to the verbal explanation) more formal software documentation of the simulation system, such as with appropriate UML diagramming methods and maybe also pseudo-code. This includes making clear how particular random generator parameters were set – i.e. where the values came from and how used.
	* Again, primarily due to the number of hours it will take

* [AMBER] Error bars on graphs, although box and whisker plots with the mean indicated would be more appropriate

* [GREEN][DONE] Keep figures with the text that describe them

* [GREEN][DONE] Remove claims about energy usage in the network

### Formal design of the K-HAS

* [AMBER] Separate out architecture design from scenarios of its use

* [GREEN][DONE] Make it explicit that the DA will be running on a laptop/desktop computer

* [GREEN][DONE] State what your architecture is capable of doing that OGC-SWE is not, particularly compared to deployments of OGC-SWE that have been used for capturing animal images
	* End of chapter 4

### Image classification

* [AMBER][DONE] Clarify role of image processing and use of templates. Bring this discussion into Chapter 3.
	* Discuss in chapter 3 and clarify in chapter 4?

* [AMBER][DONE?] When explaining the image processing functionality make clear the distinction between classifying an image as interesting or uninteresting and classification in the sense of determining a particular species.

* [RED][DONE?] Make a clear statement regarding what has actually been implemented and is a part of the completed system as opposed to functionality which you have experimented but not made operational – thus explain that species classification has not been implemented in any particularly effective way in the final system, but you can explain how it would be done.
	*Again, purely based on time

* [AMBER][DONE] With regard to classification with templates, how would templates be matched if objects are at different angles, distance from the camera, etc?

* [AMBER][DONE?] Throughout the thesis make it clear whether functionality relies on image classification to determine a species (that has not been implemented) or identifying potentially interesting images

* [GREEN][DONE] Provide link to Triton source repository
	- Pg 53

* [AMBER][DONE?] Correctly use your definition for accuracy (page 56)
	* Update accuracy with the equations actually used? I.e. one for TP and one for TN.

* [GREEN][DONE] Make clear that adding rules to Drools requires specialist knowledge of the drools programming language
	- Pg 76

* [GREEN][DONE] Indicate the circumstances that could lead to a rule being added to Drools – where has the required information / knowledge come from?
	- Pg 86

* [RED] The description of the architecture needs to be accompanied by software documentation diagrams or code (such as UML interaction and activity diagrams and / or pseudo-code) that makes clear the main components of the system (both software and human interventions) and how they interact with each other.

## Ontology

* [AMBER][DONE] Correction of claims about ontologies in both chapter 5 and 8

* [GREEN][DONE] SSN ontology is both sensor-centric and observation-centric.
	* create a new section to include this and extension of SUMO?

* [AMBER][DONE] Introduce SUMO as a general purpose upper ontology (with appropriate reference(s)). Then go on to state how it has been specialised for sensor network deployments

* [AMBER][DONE] Remove claim that your ontology is modular. You reuse existing terms by importing them, but it is not modular.

* [RED][DONE?] Need a critical discussion as to why SSN does not meet your needs
	* Different to a tiered network?
	* Hard to show flow of knowledge?
	* Humans equal to sensors?

### Definition of local knowledge

* [AMBER] Correct and move to appropriate part of the thesis, probably chapter 3. I would suggest removing the term global knowledge.
	* Chapter 3 or 4?

* [AMBER][DONE] Fig 3.5: combine the two graphs onto a single plot.

* [AMBER][CANNOT DO] Separate out UK wet and dry and provide humidity values for the experiment (if you have them).
	-I do not think we do

* [GREEN][CANNOT DO] Include the values for when DGFC loses signal
	* Do not think I have these values

##General comments:

* [AMBER] When stating that there are multiple tools, provide more than one citation
	* Need to find these references in the thesis

* [GREEN][DONE] Remove the acronyms ‘LK’ and ‘GK’ and replace with their expanded terms

* [GREEN][DONE?] Don’t use the term scientific observation when you specifically mean an ecological observation
	* Is this for all uses of the term?
	* I am not sure if this is a find and replace issue or some uses do not fit. Darwin Core, for example, is biological and ecological observations, so scientific fits best

* [GREEN][DONE] Remove et al from references
	* Bibtex includes 'others' as et al, remove these from bib file

* [AMBER][DONE] Provide a map of the location of the field centre in its wider context, i.e. the part of the globe, in Chapter 1. Improve resolution of Fig 3.2 and highlight regions on picture.

* [GREEN][DONE] Remove claim at end of §3.3.1 that, based on your experiment, you can conclude that other experiments would give you the same results in the UK and Malaysia

* [GREEN][DONE] Field names in Listing 4.3 for set.csv don’t match those given in Listing 4.4

* [GREEN][DONE] Turn the heading ‘Findings’ in §5.1.2 into the subheading §5.1.3

* [GREEN][DONE] cite all the commercial cameras considered
	- Few commercial cameras existed and Buckeye was the main choice

* [GREEN][DONE] 6.1 provide a picture of the Buckeye cameras used with their case

* [AMBER][DONE] 6.2 State why you are only taking 2 pictures when up until this point you have been working with 3 pictures
	- Pg 120

* [GREEN][DONE] Listing 6.4 remove the setting of the scientific name as you are not sure which of the two species it is

* [AMBER] State how many rules were used in the LORIS deployment and an indication of the accuracy of the system

* [GREEN][DONE] Indicate which part of the interview in appendix E is shown in appendix F
	- Explained the extracts in more detail but the two included are from different researchers, I can change the extract to match the ful?

* [AMBER][DONE] p126 rewrite paragraph about global knowledge and local knowledge of clouded leopard sleeping patterns
	- Needs checking
	- Pg 127

* [GREEN][DONE] Citations for Weka and J48

* [GREEN] Clarify 400 hour claim on p158 (the new simulation experiments will give you a proper value for this against the baseline when there is no intelligence in the network)

## Typos / minor corrections (90% done):
* [DONE] GLACSWEB: citation needed. 'that' -> 'at'
* [DONE] P29 Last bullet point: Should ‘collection’ be ‘collecting’?
* [DONE] P35/36 Local knowledge .... was ‘used for many years to extract information
from indigenous’ people does not sound right – do you mean that local
knowledge was extracted from indigenous people ?
* [DONE] p39 this most -> this is most
* [DONE] p40 for period -> for a period
* [DONE] P40 end of first paragraph : ‘at higher risk’ ? ‘when at higher risk’
* [DONE] p40 at higher risk, -> at higher risk locations,
* [DONE] p40 now ninety -> now ninety cameras
* [DONE] p41 DG -> DGFC
* [DONE] p41 on its validity, but it -> on its validity. This removes
* [DONE] p41 expand LKWS as this is its first use
* [DONE] p42 to nodes that are more computationally capable, e.g. Mote 2 [74], than
common sensor nodes, e.g. ...
* [DONE] p43: specs -> specifications
* [DONE] p43 line 2: “did research many” did research on many
* [DONE] p45 yield usable range -> discover usable radio range data
* [DONE] p46: wireless medium but -> wireless medium for internode communication but
* [DONE?] p48: explain how the dip to zero in the noise graph for UK may be due to variation in terrain and intervening obstacles
* [DONE] p50: in the UK, and thick -> in the UK; the thick
* [DONE] p51: This could -> The low range could
* [DONE] p56: delete determine ...empty
* [PARTIAL] p56: define TotalSets
correct all the errors in the use of false positives and false negatives on this page
(so matches with data in the tables on p57). Also phraseology in sentence starting “These preliminary results..” is peculiar regarding effective at detecting FP and FN – a strange objective to be effective at...
* [DONE] p59 para 4 : ?? “errors reading” errors in reading”
* p65: clarify the statement about users being able to classify data with a voting
system. Explain exactly what the user is able to vote on (and make clear
whether you are talking about species classification or interest
classification).
* §4.2 Correct sentence: ‘Unlike DC nodes,..., Drools...’
* [DONE] p68: URL for GBIF
* [DONE] p68: DwC is that standard set of terms -> ???
* [DONE] p68: OBOE (expand/explain)
* [DONE] p69: xml -> XML
* p70: move text to previous page so that it is not skipped over
* [DONE] p74: there are three observations of the Malay Civet in Figure 4.5
* p77: delete and make into a new sentence
* [DONE] p77 last para “described” “described”
* [DONE] p78: initiiated -> initiated
* [DONE] p78: when introducing the walkthrough make clear that this is hypothetical with respect to the proposed design of the design and does not all refer to actual implemented functionality
* [DONE] p80 are added is added
* [DONE] p81: nodes us a queue -> nodes use a queue
* [DONE] p84: it unarchived -> it is unarchived
* [DONE] p84: so this the message -> so this message
* [DONE] p88: citation for SUMO
* p92: and Figure 5.3 -> break the sentence here.
* [DONE] P93: is -> in
* [DONE] p93: [17] need to be moved into the sentence
* [DONE] p93: First sentence of final paragraph needs rewriting and breaking into
multiple sentences
* [DONE] p93: when introducing SUMO you need a reference for the high level / generic
system (in addition to you current reference which can be regarded as an
domain-specific extension of SUMO). The current text is misleading in
implying that SUMO is designed specifically for sensor data.
* [DONE] p95: observations is a -> observations in a
* [DONE] p96: SUMO (in heading) -> SHO
* P97 6 lines from end ontology 
* [DONE] p102: protege citation for wrong version
* [DONE] p107: cite Hermit
* [DONE[ p123: (end of 2 nd paragraph) clarify what is meant by a rule that starts looking
for nocturnal animals – say how that might be done (? With regard to
constraints on time)
* [DONE] p126: clarify whether Dedoose is a manual or automatic annotation system
* [DONE] p127: end of page – make clear that your explanation of rules that are based
on large amounts of collected data is hypothetical – perhaps you could
use a phrase such as “in principle ...local knowledge could be used to
make accurate classifications....” (or “the intention is that”) – the problem
here as elsewhere in thesis being that there is not a clear distinction
between what might be done, perhaps with further implementation and
deployment, and what actually has been done with your implemented
system.
* [DONE] 131: a agent -> an agent
* [DONE] 134: an actual WSN would -> a K-HAS deployment would.
* [DONE] 136: modification the -> modification of the
* [DONE] p136: do not use different terms, i.e. base station and central node, to refer to
the same thing
* [DONE] p139: what is an “extracted image”?
* 142: Keep Figure 7.2 with the text that describes it
* [DONE] 148: Table 7.4 KHAS -> MK-HK
* [DONE] 151: L-KHK -> MK-HK
* [DONE] p151 line 2 : the the -> the
* 152: with same -> with the same
* [DONE] p153: the figure of 83% correct classification does not seem right. Correct it if
necessary and refer to the relevant graph or table that presents the value
* p155: which knowledge? ‘this knowledge can be used...'
* p156: DC nodes are available for sensors, not for cameras!
	
  
