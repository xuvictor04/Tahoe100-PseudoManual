---
symbol: "SPCS2"
type: "gene"
col: 3983
ensembl_id: "ENSG00000118363"
name: "signal peptidase complex subunit 2"
location: "11q13.4"
module: 49
arm: "+"
pooled_cpm: 77.66
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SPCS2

*signal peptidase complex subunit 2* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.84× (z +9.4, q 4e-18, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.584× (z -8.2, q 1e-13, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSTC]] (+0.72, fdr 7e-06), [[LMAN2]] (+0.68, fdr 7e-06), [[SLC33A1]] (+0.66, fdr 1e-05); moves opposite to [[RANGAP1]] (-0.56, fdr 1e-05), [[CYFIP1]] (-0.55, fdr 3e-05), [[ASAP1]] (-0.53, fdr 1e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3983.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.84×** | +9.4 | 4e-18 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +7.7 | 3e-12 | 41/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +6.2 | 1e-07 | 34/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +6.0 | 3e-07 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.92×** | +5.3 | 2e-05 | 33/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +4.8 | 1e-04 | 27/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +4.6 | 4e-04 | 26/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.013 | 24/48 (SHP-77, PANC-1, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.027 | 22/48 (C-33 A, C32, …) | two highest doses | position effect removed |
| [[Cyclosporin A (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.027 | 25/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Erdafitinib (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.11 | 19/48 (Panc 03.27, J82, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3983.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.584×** | -8.2 | 1e-13 | 38/48 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.610×** | -7.6 | 1e-11 | 38/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.673×** | -7.5 | 1e-11 | 41/48 (NCI-H1792, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.642×** | -6.8 | 2e-09 | 40/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.644×** | -6.7 | 2e-09 | 36/48 (KATO III, SW 1088, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.758×** | -5.3 | 9e-06 | 38/48 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.590×** | -4.2 | 0.002 | 35/49 (KATO III, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.792×** | -3.5 | 0.036 | 23/47 (HOP62, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.802×** | -3.4 | 0.045 | 21/49 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.803×** | -3.4 | 0.045 | 22/48 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.813×** | -3.2 | 0.083 | 20/48 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | **0.810×** | -3.1 | 0.086 | 22/48 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.810×** | -3.1 | 0.086 | 23/48 (NCI-H2347, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 217 | 1 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.253× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.342× (z -11.9) |
| [[PANC-1 (line)]] | alt | 74.8 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.24× (z +17.3) | — |
| [[KATO III (line)]] | alt | 162 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -13.8) |
| [[NCI-H1792 (line)]] | alt | 68.7 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -17.9) |
| [[NCI-H23 (line)]] | alt | 82.4 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +11.1) | — |
| [[SW480 (line)]] | alt | 73.0 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +13.0) | — |
| [[C-33 A (line)]] | alt | 51.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[CFPAC-1 (line)]] | alt | 98.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -10.2) |
| [[COLO 205 (line)]] | alt | 94.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.336× (z -9.5) |
| [[A-427 (line)]] | wt | 55.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | — |
| [[HT-29 (line)]] | alt | 117 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.354× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 47.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 92.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 43.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 97.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW 1088 (line)]] | alt | 85.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0578× (z -10.0) |
| [[SW1417 (line)]] | alt | 98.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.391× (z -8.6) |
| [[A-172 (line)]] | wt | 79.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 78.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 94.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 105 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 91.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 67.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSTC]] | +0.72 | +0.77 / +0.75 | both halves | 7e-06 | pathway: Adherens junctions interactions; STRING 410 |
| [[LMAN2]] | +0.68 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[SLC33A1]] | +0.66 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[DNAJC3]] | +0.66 | +0.73 / +0.63 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication |
| [[TMEM39A]] | +0.65 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[NUCB2]] | +0.65 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[DERL2]] | +0.65 | +0.63 / +0.78 | both halves | 7e-06 |  |
| [[PCGF3-AS1]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[APTR]] | +0.63 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[MCEE]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MON2]] | +0.61 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SEC61B]] | +0.61 | +0.65 / +0.65 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 790 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANGAP1]] | -0.56 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[CYFIP1]] | -0.55 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ASAP1]] | -0.53 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[TAF1B]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[MACF1]] | -0.52 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[KPNA4]] | -0.51 | -0.47 / -0.43 | both halves | 3e-05 | pathway: Dengue Virus Genome Translation and Replication |
| [[TMEM185B]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, -36.5); signed map (-54.4, 11.5). **Vector** length 102, 29.6% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | -1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | -0.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | -0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.4 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | -0.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.8 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -2.1 | -2.2 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | signal peptidase complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:74,949,261-74,979,033 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0102 |
| Reactome | 22 pathways, smallest: Synthesis, secretion, and inactivation of Glucose-dependent Insulinotropic Polypeptide (GIP); Synthesis, secretion, and deacylation of Ghrelin; Synthesis, secretion, and inactivation of Glucagon-like Peptide-1 (GLP-1) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15005](https://www.uniprot.org/uniprotkb/Q15005) (Signal peptidase complex subunit 2):

> Component of the signal peptidase complex (SPC) which catalyzes the cleavage of N-terminal signal sequences from nascent proteins as they are translocated into the lumen of the endoplasmic reticulum. Enhances the enzymatic activity of SPC and facilitates the interactions between different components of the translocation site (By similarity).

**Summary**, from NCBI Gene [9789](https://www.ncbi.nlm.nih.gov/gene/9789):

> Predicted to enable peptidase activity. Involved in obsolete signal peptide processing. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28962) · Entrez [9789](https://www.ncbi.nlm.nih.gov/gene/9789) · UniProt [Q15005](https://www.uniprot.org/uniprotkb/Q15005) · Ensembl [ENSG00000118363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118363)

## Data

Gene col 3983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3983); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3983]; `tensor/DDL_lfc|DDL_z.npy` [3983]; `embed/gene_vectors.npy` [3983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3983 or target_col == 3983). Every well: [[SPCS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPCS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
