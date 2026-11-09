---
symbol: "PRKAB1"
type: "gene"
col: 3269
ensembl_id: "ENSG00000111725"
name: "protein kinase AMP-activated non-catalytic subunit beta 1"
location: "12q24.23"
module: 7
arm: "+"
pooled_cpm: 10.3
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PRKAB1

*protein kinase AMP-activated non-catalytic subunit beta 1* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.74× (z +8.2, q 1e-13, up in 24 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.691× (z -5.1, q 2e-04, down in 16 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.813× (z -4.4, q 0.003, down in 15 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBLL1]] (+0.66, fdr 1e-05), [[ZNF79]] (+0.63, fdr 1e-05), [[MRPL49]] (+0.62, fdr 1e-05); moves opposite to [[NPTN]] (-0.51, fdr 9e-05), [[BZW2]] (-0.51, fdr 3e-05), [[PTMA]] (-0.51, fdr 6e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3269.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +8.2 | 1e-13 | 24/42 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.75×** | +7.9 | 7e-13 | 24/47 (A498, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.33×** | +6.6 | 7e-09 | 21/43 (A-172, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +6.5 | 1e-08 | 22/45 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +6.2 | 7e-08 | 24/46 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +5.2 | 2e-05 | 16/47 (LOX-IMVI, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 3e-04 | 14/46 (A549, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.4 | 9e-04 | 12/46 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.21×** | +4.0 | 0.004 | 17/45 (NCI-H460, A549, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.012 | 10/47 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.4 | 0.030 | 5/47 (NCI-H2347, SW 900, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.070 | 6/47 (A-172, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.091 | 7/46 (PANC-1, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3269.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.691×** | -5.1 | 2e-04 | 16/34 (NCI-H2030, BT-474, …) | two highest doses | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -4.4 | 0.003 | 15/48 (BT-474, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.745×** | -4.3 | 0.004 | 14/20 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Silodosin (drug)]] 5 µM |  | **0.766×** | -3.9 | 0.013 | 14/43 (C-33 A, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **0.767×** | -3.9 | 0.013 | 14/43 (LOX-IMVI, LS 180, …) | top dose only |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.866× | -3.1 | 0.19 | 11/47 (SHP-77, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3269. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 10.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0716× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0752× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 10.2 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.8) ⚠ cell-cycle shift, explains ~9% of this change | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0685× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[HOP62 (line)]] | alt | 6.17 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -9.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~14% of this change |
| [[NCI-H2347 (line)]] | alt | 6.42 | 0 | 1 | — | [[Finasteride (drug)]] 0.05 µM 0.156× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 8.73 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.101× (z -8.5) |
| [[SHP-77 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3269), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBLL1]] | +0.66 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[ZNF79]] | +0.63 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[MRPL49]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[ZNF564]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ZNF623]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ZNF408]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ZNF746]] | +0.59 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[CNOT11]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ZBTB6]] | +0.58 | +0.67 / +0.38 | both halves | 6e-05 |  |
| [[ZNF543]] | +0.58 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[ZNF646]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[RNF25]] | +0.57 | +0.66 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPTN]] | -0.51 | -0.54 / -0.37 | both halves | 9e-05 | pathway: Neuronal System |
| [[BZW2]] | -0.51 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[PTMA]] | -0.51 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[PPP1R2]] | -0.50 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[SPAG9]] | -0.50 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[RFX2]] | -0.49 | -0.53 / -0.35 | both halves | 1e-04 | pathway: Organelle biogenesis and maintenance |
| [[PTMAP2]] ⚠ | -0.49 | -0.50 / -0.41 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MLF1]] | -0.49 | -0.50 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-34.7, 15.5); signed map (4.8, -30.3). **Vector** length 67.5, 10.4% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.4 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +4.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.4 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +0.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -2.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase AMP-activated non-catalytic subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:119,667,864-119,681,624 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Protein kinase AMP-activated non-catalytic subunit beta family |
| Hallmark sets | P53_PATHWAY |
| Reactome | 31 pathways, smallest: Lipophagy; Activation of PPARGC1A (PGC-1alpha) by phosphorylation; AMP and AMPK regulate the circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y478](https://www.uniprot.org/uniprotkb/Q9Y478) (5'-AMP-activated protein kinase subunit beta-1):

> Non-catalytic subunit of AMP-activated protein kinase (AMPK), an energy sensor protein kinase that plays a key role in regulating cellular energy metabolism. In response to reduction of intracellular ATP levels, AMPK activates energy-producing pathways and inhibits energy-consuming processes: inhibits protein, carbohydrate and lipid biosynthesis, as well as cell growth and proliferation. AMPK acts via direct phosphorylation of metabolic enzymes, and by longer-term effects via phosphorylation of …

**Summary**, from NCBI Gene [5564](https://www.ncbi.nlm.nih.gov/gene/5564):

> The protein encoded by this gene is a regulatory subunit of the AMP-activated protein kinase (AMPK). AMPK is a heterotrimer consisting of an alpha catalytic subunit, and non-catalytic beta and gamma subunits. AMPK is an important energy-sensing enzyme that monitors cellular energy status. In response to cellular metabolic stresses, AMPK is activated, and thus phosphorylates and inactivates acetyl-CoA carboxylase (ACC) and beta-hydroxy beta-methylglutaryl-CoA reductase (HMGCR), key enzymes …

**Accessions** — [HGNC:9378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9378) · Entrez [5564](https://www.ncbi.nlm.nih.gov/gene/5564) · UniProt [Q9Y478](https://www.uniprot.org/uniprotkb/Q9Y478) · Ensembl [ENSG00000111725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111725)

## Data

Gene col 3269: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3269); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3269, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3269]; `tensor/DDL_lfc|DDL_z.npy` [3269]; `embed/gene_vectors.npy` [3269]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3269 or target_col == 3269). Every well: [[PRKAB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKAB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
