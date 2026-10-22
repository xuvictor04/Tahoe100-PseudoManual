# MG53 / TRIM72 evidence map: upstream regulators and the p53 relationship

Literature workstream for the team question "MG53 (TRIM72): what may be upstream of it, and what are its
downstream effects on p53?", prompted by the Tahoe-100M finding that idarubicin 5 uM raises TRIM72 mRNA in nearly
every cancer cell line (see `/home/user/Tahoe100-PseudoManual/trim72_idarubicin/README.md`).

**How this map was built (all re-runnable).**
- `pubmed_screen.py` -> retrieved all 308 PubMed records mentioning TRIM72/MG53/mitsugumin 53 in title/abstract
  (`pubmed_trim72_records.csv`, run 2026-10-22), keyword-screened them (`pubmed_keyword_counts.csv`,
  `pubmed_keyword_hits.csv`), and ran 20 targeted co-occurrence queries (`pubmed_targeted_queries.csv`).
- `external_checks.py` -> Fischer 2017 p53-target census tables, ChIP-Atlas TP53 ChIP-seq binding, Human Protein
  Atlas tissue RNA, Europe PMC title/abstract+full-text searches, and full-text scans of the TRIM-p53 reviews and
  open-access MG53-in-cancer papers (`fischer2017_p53_census_check.csv`, `chipatlas_tp53_binding_check.csv`,
  `hpa_trim72_tissue_rna.csv`, `europepmc_queries.csv`, `trim_p53_reviews_check.csv`,
  `tachibana2025_trim72_excerpt.txt`, `cancer_fulltext_p53_check.csv`).
- Abstracts and (where open access) full texts were read for every claim below. Every citation is a paper I opened
  or saw in a search result; none is invented. Evidence levels: **replicated** = independent labs/models agree;
  **single study** = one solid primary study; **review-only** = asserted in a review/secondary source; **speculative**
  = proposed, not tested.

**Hard scope limits to keep in mind when mapping this onto Tahoe.** Tahoe is mRNA, 24 h, cancer cell lines, no
MG53 perturbation. Almost the entire MG53 literature is **protein**-level (membrane repair, E3 ligase, secreted
myokine), in **muscle/heart/kidney/lung**, usually by over-expression / knockout / recombinant protein. TRIM72
mRNA is essentially muscle/tongue-restricted in normal tissue (HPA consensus: skeletal muscle 142 nTPM, tongue 40,
heart 0.7, lung 0.2, every other tissue <=0.3 nTPM; `hpa_trim72_tissue_rna.csv`), so the near-zero baseline and
large drug-induced fold change seen across Tahoe cancer lines is itself outside the normal expression domain of
this gene. No MG53->p53 statement from Tahoe can be causal; the one causal MG53->p53 paper is in cardiomyocytes,
not cancer cells.

---

## Part 1 — What regulates TRIM72/MG53 EXPRESSION (transcription / mRNA)

| # | Claim | Evidence level | Model system | Citation |
|---|---|---|---|---|
|1.1|TRIM72 transcription is driven by the muscle master regulator MyoD (and myogenin) acting on two proximal E-boxes in the TRIM72 promoter; MyoD- and Akt-dependent.|single study (promoter dissection)|C2C12 myoblasts, mouse satellite cells, promoter assays|Lee CS et al. 2010, Cell Death Differ, PMID 20139895, doi 10.1038/cdd.2010.1|
|1.2|MyoD (or myogenin) and MEF2 act synergistically on juxtaposed E-box + MEF2 sites to activate the TRIM72 promoter; TRIM72 is higher in oxidative (high-MEF2) than glycolytic muscle.|single study (promoter dissection), consistent with 1.1|C2C12 differentiation, promoter mutagenesis|Jung SY et al. 2010, Biochem Biophys Res Commun, PMID 20399744, doi 10.1016/j.bbrc.2010.04.072|
|1.3|TRIM72 transcription is itself positively driven by the IRS-1/PI3K/AKT pathway (feedback), i.e. AKT activity promotes TRIM72 expression.|single study|tongue cancer cells (SCC9/SCC25)|Yin W et al. 2019, Small, PMID 30690890, doi 10.1002/smll.201805492 (also stated in Lee 2010, PMID 20139895)|
|1.4|Promoter cis-mutations explain large species differences in heart TRIM72 (high in Old World monkeys, near-absent in hominids); positive selection on the promoter.|single study (comparative/evolutionary)|primate hearts, 29 mammals, reporter assays|Feng Y et al. 2021, Mol Biol Evol, PMID 33744959, doi 10.1093/molbev/msab083|
|1.5|Glucocorticoid (dexamethasone, 1 uM, 24 h) raises TRIM72 protein; the atrophy E3 ligase MuRF1 (TRIM63) binds and stabilizes TRIM72. (Protein-level; mRNA co-upregulation of MuRF1+TRIM72 reported separately in STZ-diabetic rat muscle.)|single study (+ supporting STZ-rat mRNA)|C2C12 myotubes; MuRF1-KO|Musa I et al. 2025, FASEB J, PMID 41000062, doi 10.1096/fj.202502066RR (mRNA: Reddy SS 2018, PMID 29277369)|
|1.6|Metabolic / insulin-resistance states raise muscle MG53: MG53 is "markedly elevated" in insulin-resistance models and over-expression triggers metabolic syndrome. **Contested** (see 1.7).|replicated-but-disputed|mouse muscle, HFD/db models|Song R et al. 2013, Nature, PMID 23354051, doi 10.1038/nature11834; Liu F 2015 Circulation PMID 25637627|
|1.7|Several independent groups find MG53 expression is NOT consistently changed in insulin resistance / diabetes, and MG53 is not a critical insulin-signaling regulator — i.e. the "metabolic upregulation" of MG53 does not replicate.|replicated (contradicting 1.6)|human/mouse muscle; C2C12; db/db; HEK293|Yi JS 2013 Nat Commun PMID 23965929; Ma H 2015 PLoS One PMID 25950605; Wang Q 2020 Diabetes PMID 32139593; Philouze 2021 PLoS One PMID 33566837; Lee KE 2024 Front Endocrinol PMID 39355613|
|1.8|High glucose / nutrient overload activates MG53 (ROS->AKT S485/491 phosphorylation of AMPKα recruits MG53); this is an activity/substrate effect, and metabolic stress also drives MG53 **secretion** (see 1.14), not necessarily transcription.|single study|C2C12, mouse muscle|Jiang P et al. 2021, Mol Cell, PMID 33400924, doi 10.1016/j.molcel.2020.12.008|
|1.9|Mechanical loading/unloading changes muscle TRIM72 mRNA and protein (down with hindlimb suspension, up with reload/overload), tracking MyoD.|single study|mouse soleus|Ohno Y et al. 2014, Physiol Rep, PMID 25539835, doi 10.14814/phy2.12259|
|1.10|Exercise modulates muscle MG53: chronic swimming lowers muscle TRIM72 mRNA+protein in HFD rats; other work shows exercise raises MG53 (brain/muscle/plasma) in an AD model; prolonged treadmill running left MG53 protein unchanged. Net: context-dependent, not a single direction.|single studies, divergent|rat/mouse muscle, brain|Qi J 2016 J Diabetes Res PMID 27843952; Belviranli 2026 Arch Gerontol Geriatr PMID 41202432; Alloush 2013 Indian J Biochem Biophys PMID 24772964|
|1.11|Injury/stress raises TRIM72 in epithelia: hyperoxia, ventilator injury, acid, bleomycin, and IPF raise lung TRIM72 (mRNA+protein); hyperoxia raises TRIM72 in A549 (protein, Western, at 48/120 h) and TRIM72 then drives alveolar cell death.|single studies (several injuries), replicated direction|rat/mouse lung, A549, RLE-6TN|Cong X 2020 Respir Res PMID 32471489; Huang LT 2021 J Chin Med Assoc PMID 32796321, doi 10.1097/JCMA.0000000000000413|
|1.12|TRIM72 mRNA level is controlled post-transcriptionally by m6A methylation and mRNA stability (ALKBH5/METTL3/YTHDF2 set MG53 mRNA stability in cardiomyocytes; RBM15/YTHDF2 and MLL1/H3K4me3 set TRIM72 in trophoblasts; HDAC4 sets Trim72 mRNA decay in dystrophic muscle).|single studies (converging on "regulated mRNA stability")|rat cardiomyocytes; HTR-8/SVneo; mdx muscle|Li D 2024 J Cardiovasc Pharmacol PMID 37989146; Li Z 2025 J Cardiothorac Surg PMID 39923081; Li L 2024 Biol Direct PMID 39709463; Renzini 2022 J Cachexia Sarcopenia Muscle PMID 35170869|
|1.13|Non-coding RNAs tune MG53 mRNA (circRTN4/miR-497-5p->MG53 up in cardiomyocytes; circRNA18-658/miR-127-5p->TRIM72 in lung; SP1/MG53 lncRNA axis — the SP1 lncRNA paper was **retracted**).|single studies; one retracted|rat cardiomyocytes, lung|Li J 2022 BBRC PMID 35724457; Li Y 2025 Mol Immunol PMID 40279987; (retracted: Xu L 2020 Aging PMID 32087602, retraction PMID 36790768)|
|1.14|**Anthracyclines raise MG53.** Daunorubicin (9 wk) increases MG53 **protein** in rabbit heart; doxorubicin significantly upregulates MG53 in H9c2 cardiomyoblasts. (NB: the ferroptosis paper 3.1 instead reports DOX *lowers* MG53 in mouse heart — direction is model-dependent.)|single studies, directionally mixed|rabbit heart; H9c2|Ichikawa Y 2017 PLoS One PMID 28498861, doi 10.1371/journal.pone.0177660; Xu B 2025 Mol Pharmacol PMID 40222106, doi 10.1016/j.molpha.2025.100032|
|1.15|DNA damage specifically inducing TRIM72 transcription: **searched, not established.** No PubMed title/abstract record and no Europe PMC title/abstract hit links TRIM72/MG53 to "DNA damage"/genotoxic except a skin nitrogen-mustard paper (no p53/transcription mechanism). TRIM72 is **not** a curated or genome-wide p53 target (Part 3), so the Tahoe anthracycline induction is unlikely to be a direct p53->TRIM72 transcriptional program.|null-result (direct), inference|—|PubMed `pubmed_targeted_queries.csv` ("DNA damage"=1 hit: Li H 2023 Cells PMID 37508578); Europe PMC `europepmc_queries.csv`|

### MG53 PROTEIN regulation (stability, oxidation/oligomerization, secretion) — context for why mRNA is a weak proxy

| # | Claim | Evidence level | Model system | Citation |
|---|---|---|---|---|
|1.16|MG53 is a redox sensor: membrane injury exposes the cytosol to an oxidizing environment, driving Cys242 disulfide-bond formation and leucine-zipper-mediated oligomerization that nucleates the repair patch. Oxidation is required.|replicated|mouse muscle, C2C12, structural|Cai C 2009 Nat Cell Biol PMID 19043407; Hwang M 2011 Am J Physiol Cell Physiol PMID 21525429; Ma Y 2023 Nat Commun PMID 36944613; Park SH 2023 Nat Struct Mol Biol PMID 37770719|
|1.17|MG53 protein stability is tuned by oxidative post-translational modifications: S-nitrosylation at Cys144 protects MG53 from oxidation-induced degradation (cardioprotective); succinylation/ubiquitination at K130 and O-GlcNAcylation at Ser301 raise MG53 stability; GSK3β phosphorylation at Ser255 switches on its E3 activity.|single studies (converging)|HEK293, mouse heart, H9c2|Kohr 2014 JMCC PMID 24487118; Fillmore 2019 JMCC PMID 31536744; Wang Y 2023 Clin Exp Hypertens PMID 37848382; Zhu C 2026 Appl Biochem Biotechnol PMID 41830977; Lv F 2022 Circ Res PMID 36337049|
|1.18|MG53 is secreted as a myokine/cardiokine; secretion is triggered by metabolic stress (high glucose/insulin) and by ischemic preconditioning via H2O2->PKC-δ. So circulating MG53 can rise without transcriptional change.|replicated|rodent heart/muscle perfusate, human serum|Wu HK 2019 Circulation PMID 30586741; Zhuang L 2019 Circulation PMID 30742526; Shan D 2020 Circulation PMID 32677469|
|1.19|MG53 protein is scant-to-absent in human (and ovine/porcine) heart despite robust expression in rodent heart — a strong caution against transferring rodent cardiac MG53 biology to humans.|single study (rigorous, 3 antibodies)|human/rodent/ovine/porcine heart|Lemckert FA 2016 Cardiovasc Res PMID 26790476, doi 10.1093/cvr/cvw017|

---

## Part 2 — What MG53 does downstream (substrates, partners, pathways)

| # | Claim | Evidence level | Model system | Citation |
|---|---|---|---|---|
|2.1|Core function: MG53 nucleates the cell-membrane repair machinery, trafficking PS-containing vesicles to injury sites with dysferlin, caveolin-3 and PTRF/cavin-1; this does not require E3 activity.|replicated (many labs)|muscle, multiple tissues|Cai C 2009 Nat Cell Biol PMID 19043407; Cai C 2009 JBC PMID 19380584; Zhu H 2011 JBC PMID 21343302|
|2.2|**Substrate IRS-1:** MG53 is an E3 ligase that ubiquitinates IRS-1 (with E2 UBE2H), negatively regulating myogenesis and insulin signaling.|replicated|C2C12, mouse muscle|Yi JS 2013 Nat Commun PMID 23965929; Lee CS 2010 Cell Death Differ PMID 20139895; Gupta I 2020 Biochem Biophys Rep PMID 32055715|
|2.3|**Substrate insulin receptor:** MG53 ubiquitinates the insulin receptor; drives metabolic syndrome. **Contested** by multiple groups (see 1.7).|single study + dispute|mouse muscle|Song R 2013 Nature PMID 23354051 (disputed by PMID 32139593, 33566837, 39355613)|
|2.4|**Substrate FAK (PTK2):** MG53 ubiquitinates focal adhesion kinase during myogenesis (via UBE2H); rhMG53 binds FAK and dephosphorylates Y397 to inhibit angiogenesis / EMT.|replicated|C2C12; HUVEC; colorectal cancer|Nguyen N 2014 JBC PMID 24344130; Dong J 2021 J Cell Mol Med PMID 34240802; Faleti 2024 Heliyon PMID 39315132|
|2.5|**Substrate AMPKα:** high glucose -> MG53 ubiquitinates/degrades AMPKα, deactivating AMPK; MG53 degrades AMPKα as a tumor-suppressor mechanism in bladder cancer.|single studies|C2C12, mouse muscle; bladder cancer|Jiang P 2021 Mol Cell PMID 33400924; He X 2026 Med Oncol PMID 42900341|
|2.6|**Substrate RIPK1 / RIP3:** MG53 adds ubiquitin chains to RIPK1 (K316/604/627) for degradation, inhibiting necroptosis; p55γ uses MG53 to degrade RIP3 — cardioprotective.|single studies|mouse heart, hiPSC-CM|Wang Q 2022 Front Cardiovasc Med PMID 35711363; Li Z 2023 Cardiovasc Res PMID 37527538|
|2.7|**Pathway RISK/PI3K-AKT:** MG53 is required for ischemic pre/post-conditioning cardioprotection by tethering caveolin-3 to p85-PI3K and activating RISK (PI3K-Akt-GSK3β/ERK).|replicated|mouse heart|Cao CM 2010 Circulation PMID 20516375; Zhang Y 2011 Cardiovasc Res PMID 21285295|
|2.8|**Pathway NF-κB:** MG53 enters the nucleus, binds p65/RelA (and TAK1/IκBα), suppressing NF-κB-driven inflammation (heart aging, kidney fibrosis, KChIP2 transcription, asthma, myocarditis, neuroinflammation).|replicated (several tissues)|mouse heart, kidney, lung, brain|Wang X 2021 JCI Insight PMID 34292883; Li H 2022 Kidney Int PMID 34757120; Liu W 2019 Circulation PMID 30760025; Guan F 2019 PMID 31260721|
|2.9|Other validated substrates: MG53 K48-ubiquitinates RAC1 (Lys5) in HCC; degrades cyclin D1 (G1 arrest); degrades MGMT, p62/SQSTM1 short form, NINJ1 (K111), ATF2, SRSF5; transcriptionally inhibits KIF11.|single studies (each substrate)|HCC, colorectal/gastric, UM, kidney, PDAC|Ma X 2022 Oncogenesis PMID 35858925; Fang M 2023 Signal Transduct Target Ther PMID 37414783; Li X 2022 Cancer Biomark PMID 34958003; Ye K 2026 Cell Death Differ PMID 42045681; Tian M 2026 J Adv Res PMID 40107350|
|2.10|MG53 reduces oxidative stress and apoptosis broadly (lowers ROS, raises Bcl-2, lowers Bax/cleaved-caspase-3) across many injury models.|replicated (phenotype)|many tissues|reviews: Zhang Y 2017 Mol Pharmacol PMID 28432201; Wang YF 2024 Front Physiol PMID 38681139|

---

## Part 3 — MG53/TRIM72 <-> p53 (the core question)

### 3A. Direct MG53 -> p53 evidence

| # | Claim | Evidence level | Model system | Citation |
|---|---|---|---|---|
|3.1|**The key paper. MG53 directly binds p53 and promotes its K48-linked polyubiquitination and proteasomal degradation, INDEPENDENT of MDM2, lowering p53 and thereby de-repressing SLC7A11/GPX4 to inhibit ferroptosis and alleviate doxorubicin cardiotoxicity.** DOX *lowered* MG53 in mouse heart; MG53 overexpression (or p53 knockdown) rescued. Co-IP + ubiquitination assays.|single solid study (one lab)|mouse heart, cardiomyocytes/NRCM/H9c2; MG53-overexpressing mice|Jiang W et al. 2024, Free Radic Biol Med 223:224-236, PMID 39111582, doi 10.1016/j.freeradbiomed.2024.08.001 (MDM2-independence corroborated by review Tachibana 2025 PMID 41226293, `tachibana2025_trim72_excerpt.txt`)|
|3.2|TRIM72 directly interacts with p53 and promotes p53 ubiquitination + proteasomal degradation (down by mRNA-seq), reducing apoptosis and raising proliferation/migration. Co-IP, ubiquitination, luciferase assays.|single study (different tissue)|trophoblasts (preeclampsia), CVMSC exosomes|Li Y et al. 2021, FASEB J 35(12):e22005, PMID 34788479, doi 10.1096/fj.202100801R|
|3.3|TRIM72 inhibits **stress-induced p53 activation** indirectly: TRIM72 repairs membrane injury, which prevents stress (stretch/bleomycin) from activating p53 (lower Ser15-P and total p53); authors explicitly report **no direct TRIM72–p53 binding** and propose MG132-reversible degradation; an Mdm2 link is called speculative.|single study|rat alveolar epithelium (RLE), A549|Cong X et al. 2020, Respir Res 21:132, PMID 32471489, doi 10.1186/s12931-020-01384-2|

**Direction consensus across 3.1–3.3:** where MG53/TRIM72 acts on p53, it **lowers p53 level/activity** and is **anti-apoptotic** (ferroptosis-protective, proliferation-promoting). All three are single studies in non-cancer or epithelial contexts; two show a direct physical interaction (3.1, 3.2) and one explicitly finds none (3.3). Mechanism in the two binding studies is **ubiquitin-dependent p53 degradation**; 3.1 states it is **MDM2-independent**.

### 3B. What was searched and NOT found (null results)

| # | Searched | Result | How to recompute |
|---|---|---|---|
|3.4|MG53/TRIM72 + MDM2 co-occurrence in title/abstract (any claim MG53 regulates MDM2, or MDM2 regulates MG53).|**Not found.** 0 PubMed title/abstract hits; 0 Europe PMC title/abstract hits. The 83 full-text "MDM2" co-hits are reviews/lists, none asserting an MG53–MDM2 interaction. The only mechanistic statement is the *negative* one: MG53->p53 is MDM2-**independent** (3.1).|`pubmed_targeted_queries.csv` row "TRIM72/MG53 AND MDM2"=0; `europepmc_queries.csv`|
|3.5|Is TRIM72 a p53 target gene (does p53 transcribe TRIM72)?|**No evidence.** TRIM72 is absent from Fischer 2017's literature-curated list (344 genes), its genome-wide direct-target table (3,661 genes), and its high-confidence list (343 genes). In ChIP-Atlas, TP53 ChIP-seq peaks sit near TRIM72 in only **2 of 393** experiments (both SW-480; avg score 1.0; rank ~14,170 of 16,173) vs CDKN1A 261/393 (rank 1), MDM2 221/393, BBC3 213/393. TRIM72 ranks like background, unlike the genuine p53-target TRIMs (TRIM22 170/393; TRIM32 82/393).|`fischer2017_p53_census_check.csv`; `chipatlas_tp53_binding_check.csv`|
|3.6|Does DNA damage / anthracycline induce TRIM72 transcription via p53?|**Not shown anywhere.** No study links TRIM72 transcription to p53 or to DNA damage. Combined with 3.5, the Tahoe anthracycline->TRIM72 mRNA rise is **not** explained by a p53->TRIM72 transcriptional program in the literature; it is more consistent with a p53-independent stress program (anthracyclines also induce ATF3/ISR and NF-κB targets that co-regulate with TRIM72 in Tahoe).|`pubmed_targeted_queries.csv`; `europepmc_queries.csv`|
|3.7|MG53 as a p53 target protein degraded in response to p53, or p53->MG53 feedback.|**Not found.** No such study.|PubMed/Europe PMC screens|

### 3C. Must NOT be transferred to MG53 — other TRIM family members act on p53 (TRIM72 is NOT among the curated p53-regulating TRIMs)

The two major TRIM-p53 reviews (Liu 2021 PMID 34179310; Valletti 2019 PMID 30974870) catalog ~20 TRIMs that
regulate p53 and **neither mentions TRIM72/MG53 at all** (`trim_p53_reviews_check.csv`). Do not borrow these
mechanisms for MG53 without MG53-specific evidence:

| TRIM | Effect on p53 | Citation |
|---|---|---|
|TRIM24|E3 ligase, degrades p53; itself a p53 target (feedback)|Allton 2009 PNAS PMID 19556538; Jain 2014 MCB PMID 24820418|
|TRIM25|dual (degrades p53; also stabilizes)|Zhang P 2015 Oncogene PMID 25728675|
|TRIM28/KAP1|contributes to MDM2-mediated p53 inactivation|Wang C 2005 EMBO J PMID 16107876|
|TRIM29 (ATDC)|binds p53, antagonizes (via Tip60)|Yuan Z 2010 MCB PMID 20368352; Sho 2011 PMID 21463657|
|TRIM32|E3 ligase, degrades p53; a p53 target|Liu J 2014 Cell Death Differ PMID 25146927|
|TRIM39|binds and ubiquitinates p53|Zhang L 2012 PNAS PMID 23213260|
|TRIM59|promotes p53 ubiquitination/degradation (gastric)|Zhou Z 2014 Gastroenterology PMID 25046164|
|TRIM65|ubiquitinates/degrades p53|Li Y 2016 BBRC PMID 27012201; Wang XY 2022 Front Oncol PMID 35402260|
|TRIM8, TRIM3, TRIM19(PML), TRIM67, TRIML2|positively regulate/stabilize p53 (feedback loops)|Liu J 2021 Genes Dis PMID 34179310|
|TRIM22 (Staf50)|a direct p53 target gene|Obad 2004 Oncogene PMID 15064739|

**Closest-analog caution for the anthracycline-cardiotoxicity frame:** within doxorubicin cardiotoxicity, the
*same ferroptosis-protective "E3 ligase degrades p53 -> SLC7A11/GPX4 up"* mechanism is independently reported for
**TRIM65** (Ma X 2025 Exp Cell Res PMID 40447212) and, with opposite valence, TRIM21 loss is protective (Hou 2021
EBioMedicine PMID 34233258) and Pirh2/AIG1 degrade p53 (Shi Y 2025 Theranostics PMID 40303337). MG53/TRIM72 (3.1)
fits this cardiomyocyte pattern — but it is **one study**, and these are different proteins; the convergence is
supportive context, not evidence for TRIM72 specifically.

---

## Part 4 — MG53 in cancer and in anthracycline cardiotoxicity

| # | Claim | Evidence level | Model system | Citation |
|---|---|---|---|---|
|4.1|**MG53 is predominantly a tumor suppressor.** Low/absent MG53 marks worse disease and MG53 restoration suppresses growth across colorectal, gastric, HCC, NSCLC, tongue, breast, pancreatic, bladder cancer (E3 degradation of cyclin D1, RAC1, AMPKα, KIF11/G3BP2; FAK/PI3K-AKT inhibition).|replicated (many cancers, mostly over-expression/rhMG53)|cell lines + xenografts|Fang 2023 PMID 37414783; Ma X 2022 PMID 35858925; Li H 2021 Mol Cancer PMID 34521423; Gupta 2022 PMID 36147477; Wang XL 2024 PMID 39265509; He X 2026 PMID 42900341; review Du Y 2023 Front Endocrinol PMID 38033997|
|4.2|Low serum/tissue TRIM72 is a candidate diagnostic/prognostic marker (lower in colon cancer; low IHC predicts relapse in stage II colon cancer).|single studies|human colon cancer cohorts|Chen Z 2018 Tohoku J Exp Med PMID 29806630; Fernández-Aceñero 2020 Pathol Oncol Res PMID 30852740|
|4.3|**Context-dependent exceptions:** high TRIM72 associates with poor OS in HCC (TCGA/TRIM-family signature) and ccRCC ubiquitin signature — MG53 is not uniformly tumor-suppressive across data sets.|single studies (bioinformatic)|TCGA HCC, ccRCC|Dai W 2021 Front Oncol PMID 35004288; Wu Y 2021 Front Cell Dev Biol PMID 34239875|
|4.4|rhMG53 + doxorubicin combination suppresses multidrug-resistant colorectal xenografts without added toxicity; MG53 can sensitize NSCLC to cisplatin and HCC to sorafenib.|single studies|mouse xenografts, cell lines|Gupta 2022 Int J Biol Sci PMID 36147477; Li H 2021 Mol Cancer PMID 34521423; Ma X 2022 Oncogenesis PMID 35858925|
|4.5|**Anthracycline cardiotoxicity — protective view:** MG53 overexpression/rhMG53 reduces doxorubicin-induced ferroptosis (via p53/SLC7A11/GPX4, 3.1) and improves cardiac function; DOX lowered cardiac MG53 in that model.|single solid study|mouse heart, cardiomyocytes|Jiang W 2024 Free Radic Biol Med PMID 39111582|
|4.6|**Anthracycline cardiotoxicity — detrimental/ambiguous view:** in H9c2, DOX *upregulated* MG53 and MG53 overexpression *exacerbated* DOX apoptosis (lower p-AKT); daunorubicin raised MG53 protein in failing rabbit heart. So MG53's role and even its direction of change under anthracyclines is model-dependent and unresolved.|single studies (conflict with 4.5)|H9c2; rabbit heart|Xu B 2025 Mol Pharmacol PMID 40222106; Ichikawa 2017 PLoS One PMID 28498861|

---

## Bottom line for the team

1. **Upstream of TRIM72 expression:** the only *promoter-level transcription factors* established are **MyoD/myogenin
   + MEF2** (muscle program, E-box/MEF2 sites) and a positive **IRS-1/PI3K/AKT** feedback. Beyond that, TRIM72 mRNA/
   protein is raised by injury/oxidative stress, mechanical load, glucocorticoids (via MuRF1, protein-level), and is
   heavily tuned post-transcriptionally (m6A/mRNA stability) and post-translationally (Cys242 oxidation,
   SNO-Cys144, Ser255-P, secretion). **No p53->TRIM72 and no DNA-damage->TRIM72 transcriptional link exists** —
   TRIM72 is not a p53 target gene (census + ChIP-Atlas, 3.5). The Tahoe anthracycline induction is therefore most
   plausibly a **p53-independent stress-response program**, which fits Tahoe's own co-regulation of TRIM72 with
   ATF3/ISR and PMAIP1/NF-κB targets rather than with the classic p53 axis.
2. **Downstream on p53:** there IS direct experimental evidence (two labs: Jiang 2024 cardiomyocytes, Li 2021
   trophoblasts) that **MG53/TRIM72 binds p53 and drives its K48-ubiquitination and degradation, MDM2-independent,
   lowering p53 and apoptosis/ferroptosis.** This is the opposite direction from "p53 activates TRIM72." It is still
   only a handful of single studies, none in the cancer lines Tahoe uses, and none testable in Tahoe (mRNA only, no
   MG53 perturbation, effect is on p53 *protein*). Every MG53->p53 statement from Tahoe is an **association, not
   causal.**
3. **Do not transfer** the well-worked TRIM24/25/28/32/39/59/65 p53 mechanisms to TRIM72 — the p53-TRIM reviews do
   not even list TRIM72, and TRIM72 is absent from p53-target censuses.
