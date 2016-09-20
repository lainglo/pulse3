#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from json import dumps
import unicodedata

# Create your views here.
def labelview(request):

    text = u'''The application and applicability of the humanities and social sciences are not always visible
in the practical world. This is especially the case in technology-dependent areas like the marine
and maritime sectors. In these sectors, control, prediction and recommendations that rely on
technologies and their advancement are of the utmost importance. These sectors are, after all,
those on which we rely for international trade, defence and security, sources of food and other
energy requirements, like oil and gas. At first glance, it would appear that the sectors are devoid
of the humanities and social sciences and that these have a minimal, if not marginal role to
play. The humanities and social sciences consist of a number of subject fields like anthropology,
economics, history, international relations, law, philosophy and sociology. These fields of enquiry
are at times service providers to sectors when their services are needed. This relegates the fields
to the cupboard of scientific investigation when long-term strategies are developed, which
should not be the case. The humanities and social sciences should play a constant role in a
human-dominated world. The maritime sector is, after all, human constructed. Trade routes,
ports, harbours, warehouses, cranes, rail links and truck routes are not natural occurrences;
neither are the technologies that constitute and sustain them. Because of the dominance of
the human element, even in the marine environment, the humanities and social sciences can
play a more fruitful role in creating opportunities and solving problems. What is more, it is not
only the humanities and social sciences that are of importance, but also how humans view
the world and react to it either through theoretical or concrete means. Here, paradigms and
theories of various kinds from the humanities and social sciences also have their place. This chapter explores these dimensions in more detail. It starts by presenting a framework, called
PULSE 3 , for analysing the role of the humanities and social sciences in the two sectors. The
paradigms of the presentations delivered at the Integrated Marine and Maritime Technologies
Workshop in October 2013 are assessed. This chapter reviews the abstracts of the presentations
made at the workshop. The review of the abstracts is not representative of the state of research
and development in the entire sector. It is only a snapshot of it. However, it provides useful
insights into current thinking and practice in the marine and maritime sectors. The purpose
of this assessment is to determine the type of paradigm that was dominant. Two paradigms,
rationalism and interpretivism, are identified through the assessment. Rationalism views the
researcher and reality as separate, with only one reality present. Research is able to control
and predict this reality. This means that an objective reality exists beyond the human mind.
Interpretivism, however, notes that the researcher and reality are inseparable in that realities are
mentally constructed. Multiple realities exist and, as such, knowledge of the world is intentionally
constituted through researchers' lived experiences. There is no objective meaning (Wendt,
1999; Weber, 2004; Guba and Lincoln, 2005; Lincoln et al., 2011). An overview of the ethos of
analytic eclecticism is provided and how it can aid the marine and maritime sectors. After this,
the role of the humanities and social sciences in the public and government policy domain is
presented. This is followed by the setting of a number of beacons that the marine and maritime sectors could follow to expand the role of the humanities and social sciences. The repertoire of
theories plays a central role in this, the penultimate section of the chapter. The PULSE 3 framework is used to analyse water governance and politics. This forms the
foundation of the chapter. PULSE is an acronym for ‘people understanding and living in
a sustained environment’. The cube denotes three forces: thinking, shaping and causing
change. Individuals think, shape and cause changes in the environments in which they
live, be it the natural environment or the working environment (Meissner, 2013). The natural
environment shapes and affects changes that impact on human society and the way we live
in the environment (Berger and Luckmann, 1966; Giddens, 1984; Meissner, 2003; Kooiman
and Bavinck, 2005; Gillings, 2010). Although the framework is geared towards an analysis of
water governance and politics (Meissner, 2013), it is equally at home in a review of the marine
and maritime technology research landscape. This is because of the framework’s ability to
analyse issues at a paradigmatic and theoretical level, and not at a macro level. The rationale
behind PULSE 3 is that paradigms and/or theories have an impact on how humans act in the
world and subsequently the policies, programmes and projects they put in place to resolve
problems or create opportunities. A paradigm is a research tradition, which, in turn, is a set of
assumptions about how knowledge is produced (Schultz and Hatch, 1996; Sil and Katzenstein,
2010). Stated more formally, a paradigm is a world view that describes – for the person holding
that paradigm – the nature of the ‘world’, his or her place in this world, as well as the range
of potential relationships to that world and its parts (Pearse, 1983; Guba and Lincoln, 1994).
Considering this definition, it becomes clear that the ‘world’ of marine and maritime technology
has a particular nature with a range of relationships that span individuals, corporates, scientists,
government officials, operators and education specialists. If this is the case, it would hold that a
certain paradigm is present in the marine and maritime technology landscape that influences
how problems are confronted and opportunities created.
PULSE 3 consists of three components or elements. The first is a paradigm assessment index (see
Table 1), the second is the ethos of analytic eclecticism, and the third is a repertoire of theories.
The paradigm assessment index calculates the nature of the paradigm found in the marine
and maritime technology landscape and makes it visible. '''
    #sentences = dumps(text.split("."))


    #text = unicodedata.normalize('NFKD',text).encode('ascii','ignore')

    return render(request,'labelapp/labelpage.html',{ "paper" : dumps(text) })
