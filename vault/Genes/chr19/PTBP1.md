---
symbol: "PTBP1"
type: "gene"
col: 234
ensembl_id: "ENSG00000011304"
name: "polypyrimidine tract binding protein 1"
location: "19p13.3"
module: 3
arm: "-"
pooled_cpm: 90.61
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PTBP1

*polypyrimidine tract binding protein 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.12× (z +12.6, q 1e-33, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.18× (z +6.8, q 1e-09, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.737× (z -5.2, q 1e-04, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPL]] (+0.67, fdr 7e-06), [[HNRNPUL1]] (+0.62, fdr 1e-05), [[CBX5]] (+0.62, fdr 7e-06); moves opposite to [[RBIS]] (-0.64, fdr 7e-06), [[NSA2]] (-0.63, fdr 7e-06), [[NOL7]] (-0.62, fdr 1e-05, ⚠ NOL7 in the vector space only through flagged drug-doses), [[PSMA7]] (-0.60, fdr 6e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 234.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.12×** | +12.6 | 1e-33 | 47/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.98×** | +11.4 | 7e-28 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.62×** | +11.4 | 8e-28 | 35/48 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.62×** | +7.7 | 2e-12 | 41/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.18×** | +6.8 | 1e-09 | 41/48 (C32, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.46×** | +6.4 | 2e-08 | 34/48 (RPMI-7951, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.48×** | +6.2 | 4e-08 | 36/48 (PANC-1, NCI-H1792, …) | rises with dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +6.0 | 1e-07 | 37/49 (C32, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.66×** | +5.9 | 2e-07 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **1.38×** | +5.4 | 4e-06 | 31/49 (HT-29, MIA PaCa-2, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.35×** | +5.1 | 2e-05 | 31/48 (NCI-H1792, PANC-1, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.53×** | +5.0 | 3e-05 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.2 | 1e-03 | 28/48 (C32, AN3 CA, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.25×** | +3.7 | 0.008 | 26/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.26×** | +3.6 | 0.010 | 26/50 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[Tomivosertib (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.081 | 17/48 (H4, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | 1.19× | +2.9 | 0.099 | 15/48 (SNU-1, HEC-1-A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 234.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.737×** | -5.2 | 1e-04 | 30/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.811×** | -5.0 | 1e-04 | 31/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.749×** | -4.9 | 2e-04 | 31/48 (LoVo, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.752×** | -4.8 | 2e-04 | 36/48 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.792×** | -3.8 | 0.016 | 25/47 (C32, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.817×** | -3.4 | 0.051 | 22/48 (NCI-H23, HCT15, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.808×** | -3.4 | 0.051 | 24/48 (SW 1271, COLO 205, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.823× | -3.2 | 0.10 | 21/47 (LoVo, hTERT-HPNE, …) | rises with dose |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.878× | -3.1 | 0.11 | 12/48 (NCI-H460, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 234. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.8 | 7 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.55× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[C32 (line)]] | wt | 67.0 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.7) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 7.31× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 62.0 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +18.7) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[PANC-1 (line)]] | alt | 81.2 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +12.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[AsPC-1 (line)]] | alt | 84.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.2) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[HOP62 (line)]] | alt | 72.1 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.71× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 113 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +12.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1573 (line)]] | alt | 51.4 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.30× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 140 | 2 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.33× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.463× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 91.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -13.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A549 (line)]] | wt | 67.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.3) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[CFPAC-1 (line)]] | alt | 61.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.5) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[LOX-IMVI (line)]] | wt | 99.0 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +11.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 100 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +13.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2030 (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +9.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H2347 (line)]] | alt | 109 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.9) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[RPMI-7951 (line)]] | alt | 86.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.4) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 92.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.6) ⚠ cell-cycle shift, explains ~57% of this change | [[Dinaciclib (drug)]] 5 µM 0.107× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 103 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +9.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 78.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.3) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[SW480 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +11.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 104 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.9) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[COLO 205 (line)]] | alt | 58.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.1) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[H4 (line)]] | wt | 100 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.316× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[HS-578T (line)]] | alt | 91.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.7) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[HT-29 (line)]] | alt | 70.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | — |
| [[KATO III (line)]] | alt | 68.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +11.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | — |
| [[SW 900 (line)]] | alt | 78.4 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +8.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW1417 (line)]] | alt | 92.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.7) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[SW48 (line)]] | wt | 116 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +9.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 149 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 120 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 234), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPL]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 993 |
| [[HNRNPUL1]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 501 |
| [[CBX5]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 | same gene group |
| [[TRIM28]] | +0.61 | +0.68 / +0.50 | both halves | 1e-05 | same gene group |
| [[MCM7]] | +0.61 | +0.64 / +0.61 | both halves | 7e-06 | same gene group |
| [[DDX39A]] | +0.61 | +0.50 / +0.65 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 401 |
| [[ARHGEF39]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[CNOT1]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[TMPO]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[RAVER1]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 | same gene group; STRING 882 |
| [[C5]] | +0.58 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[HNRNPK]] | +0.58 | +0.60 / +0.54 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 997 |

## Genes that move opposite

*49 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBIS]] | -0.64 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[NSA2]] | -0.63 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[NOL7]] ⚠ | -0.62 | -0.53 / -0.61 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PSMA7]] | -0.60 | -0.39 / -0.63 | both halves | 6e-05 |  |
| [[CAMLG]] | -0.60 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[ATP5MJ]] | -0.60 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[TRIP4]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[AP3S2]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 | same gene group |
| [[BLVRB]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[UQCRB]] ⚠ | -0.57 | -0.57 / -0.58 | both halves | 9e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | -0.57 | -0.51 / -0.55 | both halves | 1e-05 | same gene group |
| [[PFDN4]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SNHG6]] | -0.56 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[TOMM7]] | -0.56 | -0.52 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PTBP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.9, -32.0); signed map (-9.0, -34.8). **Vector** length 93.7, 26.8% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.3 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | +6.6 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +5.3 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | +2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | -0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | -0.3 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +2.7 | +0.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | -6.2 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | +1.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -5.7 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | +0.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -4.2 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | +0.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | +0.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | polypyrimidine tract binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:797,075-812,327 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HNRPI, HNRNP-I, PTB2, PTB3, PTB-1, PTB4, pPTB; previously PTB |
| Gene groups (HGNC) | RNA binding motif containing; MicroRNA protein coding host genes; Heterogeneous nuclear ribonucleoproteins |
| Reactome | 13 pathways, smallest: FGFR2 alternative splicing; Signaling by FGFR2; Signaling by FGFR |
| Matched by | ensembl_id |

**Function**, from UniProt [P26599](https://www.uniprot.org/uniprotkb/P26599) (Polypyrimidine tract-binding protein 1):

> Plays a role in pre-mRNA splicing and in the regulation of alternative splicing events. Activates exon skipping of its own pre-mRNA during muscle cell differentiation. Binds to the polypyrimidine tract of introns. May promote RNA looping when bound to two separate polypyrimidine tracts in the same pre-mRNA. May promote the binding of U2 snRNP to pre-mRNA. Cooperates with RAVER1 to modulate switching between mutually exclusive exons during maturation of the TPM1 pre-mRNA. Represses the splicing …

**Summary**, from NCBI Gene [5725](https://www.ncbi.nlm.nih.gov/gene/5725):

> This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA-binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the nucleus, some seem to shuttle between the nucleus and the cytoplasm. The hnRNP proteins have …

**Accessions** — [HGNC:9583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9583) · Entrez [5725](https://www.ncbi.nlm.nih.gov/gene/5725) · UniProt [P26599](https://www.uniprot.org/uniprotkb/P26599) · Ensembl [ENSG00000011304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011304)

## Data

Gene col 234: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 234); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 234, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 234]; `tensor/DDL_lfc|DDL_z.npy` [234]; `embed/gene_vectors.npy` [234]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 234 or target_col == 234). Every well: [[PTBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
