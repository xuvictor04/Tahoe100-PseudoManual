---
symbol: "CIAO1"
type: "gene"
col: 6832
ensembl_id: "ENSG00000144021"
name: "cytosolic iron-sulfur assembly component 1"
location: "2q11.2"
module: 1
arm: "+"
pooled_cpm: 37.79
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CIAO1

*cytosolic iron-sulfur assembly component 1* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.36× (z +13.1, q 2e-36, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.472× (z -6.0, q 1e-06, down in 35 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[PH-797804 (drug)]] 5 µM in 1 line (RKO 0.0608×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (CHP-212 0.0805×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRRD]] (+0.69, fdr 7e-06), [[METTL2A]] (+0.63, fdr 7e-06), [[COA7]] (+0.63, fdr 7e-06); moves opposite to [[GNAS]] (-0.74, fdr 7e-06), [[YBX1]] (-0.60, fdr 2e-04), [[ZNF710-AS1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6832.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +13.1 | 2e-36 | 47/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +12.4 | 1e-32 | 47/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +10.9 | 2e-25 | 47/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.92×** | +10.0 | 3e-21 | 44/46 (A498, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.84×** | +8.9 | 5e-17 | 32/42 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +6.8 | 1e-09 | 40/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +6.4 | 1e-08 | 33/47 (NCI-H23, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.52×** | +5.9 | 2e-07 | 26/43 (NCI-H2030, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.7 | 9e-07 | 29/47 (NCI-H1573, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.45×** | +5.5 | 3e-06 | 28/48 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +5.4 | 4e-06 | 39/48 (PANC-1, LoVo, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.30×** | +3.9 | 0.004 | 22/47 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +3.7 | 0.009 | 20/48 (HOP62, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.27×** | +3.6 | 0.013 | 21/46 (HOP62, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.013 | 19/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.037 | 20/48 (HS-578T, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6832.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[PH-797804 (drug)]] 5 µM in 1 line (RKO 0.0608×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (CHP-212 0.0805×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.472×** | -6.0 | 1e-06 | 35/49 (SNU-1, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.563×** | -4.6 | 0.001 | 28/48 (RKO, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6832. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 31.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.84× (z +12.0) | — |
| [[SW480 (line)]] | alt | 50.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 25.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.44× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 26.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.97× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 32.8 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.18× (z +9.2) | — |
| [[A498 (line)]] | wt | 44.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[CHP-212 (line)]] | wt | 32.9 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0805× (z -8.6) |
| [[HS-578T (line)]] | alt | 27.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.19× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 36.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 38.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RKO (line)]] | wt | 56.1 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0608× (z -12.2) |
| [[A-172 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6832), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRRD]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[METTL2A]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[COA7]] | +0.63 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[WDR70]] | +0.62 | +0.57 / +0.52 | both halves | 1e-05 | same gene group |
| [[RRP7A]] | +0.62 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[KRI1]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TRMT61A]] | +0.60 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[PWP1]] | +0.59 | +0.40 / +0.58 | both halves | 5e-05 | same gene group |
| [[NSUN5]] | +0.59 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[DRG2]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[MRFAP1]] | +0.59 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CHMP6]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.74 | -0.62 / -0.75 | both halves | 7e-06 |  |
| [[YBX1]] | -0.60 | -0.29 / -0.67 | both halves | 2e-04 |  |
| [[ZNF710-AS1]] | -0.60 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[ZNF451-AS1]] | -0.60 | -0.27 / -0.53 | both halves | 3e-04 |  |
| [[KDELR1]] | -0.59 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[PRCP]] | -0.57 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[TLE2]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 | same gene group |
| [[C12orf73]] | -0.54 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[HOXB-AS3]] | -0.54 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[C12orf57]] | -0.54 | -0.23 / -0.52 | both halves | 5e-04 |  |
| [[DNAJC4]] | -0.54 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[NUCB2]] | -0.54 | -0.59 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.507). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-35.0, -1.0); signed map (2.5, -45.5). **Vector** length 73.1, 15.8% of its response variance represented; |z| ≥ 3 in 778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +13.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.7 | +5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.8 | -2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +0.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.1 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -4.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | +1.2 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.3 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +1.9 |

## What is on record

|  |  |
|---|---|
| Name | cytosolic iron-sulfur assembly component 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,266,159-96,274,173 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CIA1; previously WDR39 |
| Gene groups (HGNC) | WD repeat domain containing; Cytosolic iron-sulfur assembly components |
| Reactome | 1 pathways, smallest: Cytosolic iron-sulfur cluster assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [O76071](https://www.uniprot.org/uniprotkb/O76071) (Probable cytosolic iron-sulfur protein assembly protein CIAO1):

> Key component of the cytosolic iron-sulfur protein assembly (CIA) complex, a multiprotein complex that mediates the incorporation of iron-sulfur cluster into extramitochondrial Fe/S proteins. As a CIA complex component, interacts specifically with CIAO2A or CIAO2B and MMS19 to assist different branches of iron-sulfur protein assembly, depending of its interactors. The complex CIAO1:CIAO2B:MMS19 binds to and facilitates the assembly of most cytosolic-nuclear Fe/S proteins. CIAO1:CIAO2A …

**Summary**, from NCBI Gene [9391](https://www.ncbi.nlm.nih.gov/gene/9391):

> Involved in iron-sulfur cluster assembly and protein maturation. Located in cytoplasm. Part of MMXD complex and cytosolic [4Fe-4S] assembly targeting complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14280) · Entrez [9391](https://www.ncbi.nlm.nih.gov/gene/9391) · UniProt [O76071](https://www.uniprot.org/uniprotkb/O76071) · Ensembl [ENSG00000144021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144021)

## Data

Gene col 6832: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6832); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6832, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6832]; `tensor/DDL_lfc|DDL_z.npy` [6832]; `embed/gene_vectors.npy` [6832]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6832 or target_col == 6832). Every well: [[CIAO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIAO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
