---
symbol: "KHSRP"
type: "gene"
col: 1523
ensembl_id: "ENSG00000088247"
name: "KH-type splicing regulatory protein"
location: "19p13.3"
module: 7
arm: "+"
pooled_cpm: 71.93
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# KHSRP

*KH-type splicing regulatory protein* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.40× (z +12.6, q 2e-33, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.63× (z +5.0, q 5e-05, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAMP4]] (+0.64, fdr 7e-06), [[GIGYF1]] (+0.51, fdr 3e-05), [[VARS2]] (+0.51, fdr 3e-05); moves opposite to [[PPME1]] (-0.44, fdr 7e-05), [[SPCS1]] (-0.39, fdr 1e-04), [[SCOC]] (-0.39, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1523.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.40×** | +12.6 | 2e-33 | 49/49 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.93×** | +9.4 | 2e-18 | 41/44 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.53×** | +7.7 | 3e-12 | 43/45 (J82, A-427, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +7.4 | 2e-11 | 36/49 (A-427, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.80×** | +6.0 | 2e-07 | 40/48 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +5.8 | 8e-07 | 44/47 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +5.0 | 5e-05 | 40/48 (C32, SNU-423, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.62×** | +4.9 | 5e-05 | 36/48 (SW480, HS-578T, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.53×** | +4.3 | 9e-04 | 38/48 (RPMI-7951, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.80×** | +4.3 | 0.001 | 45/48 (LoVo, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.51×** | +4.3 | 0.001 | 32/48 (SW480, RPMI-7951, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.58×** | +4.0 | 0.003 | 37/47 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +4.0 | 0.003 | 27/48 (SNU-423, NCI-H1792, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.57×** | +4.0 | 0.003 | 29/48 (NCI-H1792, C32, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.47×** | +3.9 | 0.003 | 35/48 (NCI-H460, LoVo, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.005 | 26/48 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.059 | 31/47 (HCT15, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1523. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 39.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.07× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 77.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A498 (line)]] | wt | 88.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 49.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.32× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[J82 (line)]] | alt | 81.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 52.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 75.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-172 (line)]] | wt | 72.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 39.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HEC-1-A (line)]] | alt | 78.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 42.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HS-578T (line)]] | alt | 68.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HT-29 (line)]] | alt | 60.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[KATO III (line)]] | alt | 60.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 71.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LOX-IMVI (line)]] | wt | 80.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LS 180 (line)]] | wt | 71.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 96.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Panc 03.27 (line)]] | alt | 66.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 66.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RKO (line)]] | wt | 103 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RPMI-7951 (line)]] | alt | 62.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SHP-77 (line)]] | alt | 65.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW1417 (line)]] | alt | 96.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 95.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-427 (line)]] | wt | 94.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1523), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAMP4]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[GIGYF1]] | +0.51 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[VARS2]] | +0.51 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[MATR3-1]] | +0.50 | +0.53 / +0.47 | both halves | 2e-05 | STRING 632 |
| [[CTDNEP1]] | +0.50 | +0.42 / +0.35 | both halves | 1e-04 |  |
| [[SLC4A2]] | +0.50 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[RBM42]] | +0.48 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[MUL1]] | +0.48 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[PPP6R2]] | +0.47 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[FLOT2]] | +0.46 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[MEGF8]] | +0.45 | +0.60 / +0.30 | both halves | 2e-04 | same gene group |
| [[WDR82]] | +0.45 | +0.53 / +0.45 | both halves | 3e-05 | same gene group; STRING 431 |

## Genes that move opposite

*18 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPME1]] | -0.44 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[SPCS1]] | -0.39 | -0.36 / -0.38 | both halves | 1e-04 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[SCOC]] | -0.39 | -0.34 / -0.31 | both halves | 2e-04 |  |
| [[BOLA3]] | -0.38 | -0.21 / -0.46 | both halves | 6e-04 |  |
| [[RTRAF]] | -0.38 | -0.36 / -0.35 | both halves | 1e-04 | STRING 415 |
| [[GTF2B]] | -0.36 | -0.29 / -0.30 | both halves | 3e-04 |  |
| [[IDH2]] | -0.36 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[ORMDL1]] | -0.36 | -0.25 / -0.36 | both halves | 4e-04 |  |
| [[COA8]] | -0.36 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[CCDC181]] | -0.36 | -0.10 / -0.35 | ⚠ not reproduced | 0.003 |  |
| [[UBA6]] | -0.36 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[ACAD11]] | -0.35 | -0.15 / -0.41 | ⚠ not reproduced | 0.001 |  |
| [[DHRS7]] | -0.35 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[UBA52]] | -0.35 | -0.44 / -0.32 | both halves | 2e-04 | pathway: Regulation of mRNA stability by proteins that bind AU-rich elements |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.0819). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-21.6, -44.3); signed map (4.3, -7.3). **Vector** length 69.0, 21.2% of its response variance represented; |z| ≥ 3 in 664 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.5 | +7.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.9 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.4 | +2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +2.3 | +3.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +0.8 |
|  | [[Isocorydine (drug)]] 0.5 µM |  | +1.7 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.5 | -0.8 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -2.2 | -0.8 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.9 | -1.2 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | KH-type splicing regulatory protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:6,413,102-6,424,811 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KSRP, FBP2, FUBP2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 8 pathways, smallest: KSRP (KHSRP) binds and destabilizes mRNA; ATF4 activates genes in response to endoplasmic reticulum  stress; PERK regulates gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92945](https://www.uniprot.org/uniprotkb/Q92945) (Far upstream element-binding protein 2):

> Binds to the dendritic targeting element and may play a role in mRNA trafficking (By similarity). Part of a ternary complex that binds to the downstream control sequence (DCS) of the pre-mRNA. Mediates exon inclusion in transcripts that are subject to tissue-specific alternative splicing. May interact with single-stranded DNA from the far-upstream element (FUSE). May activate gene expression. Also involved in degradation of inherently unstable mRNAs that contain AU-rich elements (AREs) in their …

**Summary**, from NCBI Gene [8570](https://www.ncbi.nlm.nih.gov/gene/8570):

> The KHSRP gene encodes a multifunctional RNA-binding protein implicated in a variety of cellular processes, including transcription, alternative pre-mRNA splicing, and mRNA localization (Min et al., 1997 [PubMed 9136930]; Gherzi et al., 2004 [PubMed 15175153]).[supplied by OMIM, Apr 2010]

**Accessions** — [HGNC:6316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6316) · Entrez [8570](https://www.ncbi.nlm.nih.gov/gene/8570) · UniProt [Q92945](https://www.uniprot.org/uniprotkb/Q92945) · Ensembl [ENSG00000088247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088247)

## Data

Gene col 1523: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1523); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1523, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1523]; `tensor/DDL_lfc|DDL_z.npy` [1523]; `embed/gene_vectors.npy` [1523]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1523 or target_col == 1523). Every well: [[KHSRP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KHSRP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
