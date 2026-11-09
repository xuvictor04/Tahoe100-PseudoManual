---
symbol: "COPS7B"
type: "gene"
col: 6889
ensembl_id: "ENSG00000144524"
name: "COP9 signalosome subunit 7B"
location: "2q37.1"
module: 171
arm: "+"
pooled_cpm: 17.23
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# COPS7B

*COP9 signalosome subunit 7B* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.34× (z +10.0, q 8e-21, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Entrectinib (drug)]] 5 µM: 0.738× (z -4.0, q 0.039, down in 17 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Alpelisib (drug)]] 0.05 µM in 1 line (HS-578T 0.0963×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.186×); [[Tomivosertib (drug)]] 0.05 µM in 1 line (Hs 766T 0.132×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIPC]] (+0.76, fdr 7e-06), [[NUDT21]] (+0.73, fdr 7e-06), [[CUL2]] (+0.73, fdr 7e-06); moves opposite to [[NBPF10]] (-0.67, fdr 7e-06), [[TUT7]] (-0.64, fdr 7e-06), [[METTL23]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6889.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.34×** | +10.0 | 8e-21 | 43/48 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.12×** | +7.8 | 2e-12 | 34/45 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +7.1 | 3e-10 | 35/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +5.4 | 1e-05 | 26/48 (NCI-H2347, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +5.2 | 2e-05 | 28/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +4.9 | 9e-05 | 20/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.4 | 0.001 | 18/47 (SW48, BT-474, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.002 | 19/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.36×** | +4.0 | 0.004 | 18/48 (LoVo, PANC-1, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.36×** | +4.0 | 0.004 | 16/47 (LoVo, A-427, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.005 | 18/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.007 | 16/47 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.009 | 16/48 (C32, SW48, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.012 | 17/48 (HOP62, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.5 | 0.016 | 2/48 (MIA PaCa-2, NCI-H2030) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.041 | 13/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6889.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Alpelisib (drug)]] 0.05 µM in 1 line (HS-578T 0.0963×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.186×); [[Tomivosertib (drug)]] 0.05 µM in 1 line (Hs 766T 0.132×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entrectinib (drug)]] 5 µM |  | **0.738×** | -4.0 | 0.039 | 17/47 (NCI-H1573, CHP-212, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.791× | -3.1 | 0.47 | 12/47 (A549, HEC-1-A, …) | inconsistent across doses |  |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.850× | -3.0 | 0.47 | 11/48 (HS-578T, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6889. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 8.18 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0856× (z -9.4) |
| [[H4 (line)]] | wt | 14.6 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0806× (z -9.4) |
| [[Hs 766T (line)]] | wt | 14.6 | 0 | 1 | — | [[Tomivosertib (drug)]] 0.05 µM 0.132× (z -9.7) |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0963× (z -11.5) |
| [[LoVo (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 24.1 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.186× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.203× (z -9.0) |
| [[SW480 (line)]] | alt | 23.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +10.3) | — |
| [[A-172 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6889), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIPC]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[NUDT21]] | +0.73 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[CUL2]] | +0.73 | +0.79 / +0.68 | both halves | 7e-06 | pathway: Neddylation; STRING 882 |
| [[SUMO1]] | +0.73 | +0.74 / +0.68 | both halves | 7e-06 | pathway: Global Genome Nucleotide Excision Repair (GG-NER) |
| [[NAXD]] | +0.72 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[RPP30]] | +0.71 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[MRS2]] | +0.70 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[PPT1]] | +0.68 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[RNPEP]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[TMEM183A]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[RPA1]] | +0.68 | +0.74 / +0.67 | both halves | 7e-06 | pathway: Global Genome Nucleotide Excision Repair (GG-NER) |
| [[SKP2]] | +0.68 | +0.76 / +0.69 | both halves | 7e-06 | pathway: Neddylation |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF10]] | -0.67 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[TUT7]] | -0.64 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[METTL23]] | -0.63 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[OFD1]] | -0.63 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[ZNF503]] | -0.63 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.59 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[SLC22A1]] | -0.59 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[ZSWIM6]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | -0.58 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[BTG1]] | -0.57 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[MIDN]] | -0.57 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[C6orf62]] | -0.57 | -0.59 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.790). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-9.0, -13.0); signed map (-34.0, -18.2). **Vector** length 76.2, 14.7% of its response variance represented; |z| ≥ 3 in 799 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | +2.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.8 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +7.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +4.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[(S)-Crizotinib (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | COP9 signalosome subunit 7B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:231,781,671-231,809,254 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CSN7B |
| Gene groups (HGNC) | COP9 signalosome |
| Reactome | 11 pathways, smallest: DNA Damage Recognition in GG-NER; Formation of TC-NER Pre-Incision Complex; Transcription-Coupled Nucleotide Excision Repair (TC-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9Q2](https://www.uniprot.org/uniprotkb/Q9H9Q2) (COP9 signalosome complex subunit 7b):

> Component of the COP9 signalosome (CSN), a master regulator of the ubiquitin conjugation pathway. CSN mediates the deneddylation of the cullin subunits of all cullin-RING ligases. By reversing the activating neddylation on the cullin-RING ligase, the COP9 signalosome restores the ligase to its inactive state and resets it for substrate recognition. CSN is also involved in phosphorylation of p53/TP53, c-jun/JUN, IkappaBalpha/NFKBIA, ITPK1 and IRF8/ICSBP, possibly via its association with CK2 and …

**Summary**, from NCBI Gene [64708](https://www.ncbi.nlm.nih.gov/gene/64708):

> Involved in protein deneddylation. Located in nucleoplasm. Part of COP9 signalosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16760) · Entrez [64708](https://www.ncbi.nlm.nih.gov/gene/64708) · UniProt [Q9H9Q2](https://www.uniprot.org/uniprotkb/Q9H9Q2) · Ensembl [ENSG00000144524](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144524)

## Data

Gene col 6889: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6889); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6889, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6889]; `tensor/DDL_lfc|DDL_z.npy` [6889]; `embed/gene_vectors.npy` [6889]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6889 or target_col == 6889). Every well: [[COPS7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPS7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
