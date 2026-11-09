---
symbol: "ZDHHC14"
type: "gene"
col: 10553
ensembl_id: "ENSG00000175048"
name: "zDHHC palmitoyltransferase 14"
location: "6q25.3"
module: 57
arm: "-"
pooled_cpm: 54.16
n_lines_expressing: 47
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# ZDHHC14

*zDHHC palmitoyltransferase 14* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.49× (z +20.9, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 0.5 µM: 0.702× (z -4.2, q 0.013, down in 22 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[E2F3]] (+0.59, fdr 1e-05), [[MFHAS1]] (+0.55, fdr 5e-05), [[SPOPL-DT]] (+0.54, fdr 3e-05); moves opposite to [[ARNT]] (-0.59, fdr 1e-05), [[DYNC2LI1]] (-0.58, fdr 3e-05), [[USP30]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10553.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.49×** | +20.9 | 0e+00 | 40/44 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +9.6 | 3e-19 | 36/44 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.4 | 2e-11 | 36/45 (HOP62, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.90×** | +6.8 | 2e-09 | 27/45 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.77×** | +6.7 | 2e-09 | 27/45 (AsPC-1, NCI-H2030, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.63×** | +5.6 | 2e-06 | 34/45 (A-172, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.5 | 3e-06 | 26/45 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +5.0 | 5e-05 | 28/44 (NCI-H23, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.14×** | +4.7 | 2e-04 | 24/45 (NCI-H2030, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.48×** | +4.6 | 2e-04 | 26/44 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.48×** | +4.6 | 2e-04 | 22/45 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.001 | 19/45 (HT-29, LS 180, …) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.42×** | +3.7 | 0.010 | 17/45 (NCI-H1792, SNU-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.35×** | +3.5 | 0.017 | 19/45 (AsPC-1, RPMI-7951, …) | two highest doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.017 | 17/45 (LS 180, CFPAC-1, …) | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.37×** | +3.3 | 0.033 | 11/45 (SNU-1, A498, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.090 | 11/45 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.090 | 14/45 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.28×** | +2.9 | 0.098 | 11/45 (HOP62, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10553.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.702×** | -4.2 | 0.013 | 22/45 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.709×** | -4.1 | 0.013 | 23/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.528×** | -3.9 | 0.015 | 21/44 (C32, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.556×** | -3.6 | 0.039 | 20/46 (A-172, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.747×** | -3.3 | 0.093 | 13/45 (hTERT-HPNE, PANC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.757×** | -3.3 | 0.093 | 22/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10553. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 424 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -18.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.179× (z -11.8) |
| [[C32 (line)]] | wt | 110 | 0 | 9 (2 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.270× (z -9.6) |
| [[PANC-1 (line)]] | alt | 95.3 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -14.1) |
| [[A-172 (line)]] | wt | 67.1 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 82.4 | 2 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.332× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.23× (z +14.6) | — |
| [[NCI-H23 (line)]] | alt | 33.1 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +9.3) | [[Harringtonine (drug)]] 5 µM 0.178× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 18.0 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.77× (z +12.7) | [[Oxaprozin (drug)]] 0.5 µM 0.0589× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 23.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 25.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +16.5) | — |
| [[HS-578T (line)]] | alt | 18.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 22.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.92× (z +13.6) | — |
| [[LoVo (line)]] | wt | 61.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 26.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 18.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.15× (z +19.1) | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.48× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 20.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +10.1) | — |
| [[A498 (line)]] | wt | 26.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.3) | — |
| [[A549 (line)]] | wt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 75.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 26.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +9.9) | — |
| [[H4 (line)]] | wt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.10× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 23.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +13.8) | — |
| [[LS 180 (line)]] | wt | 37.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +12.8) | — |
| [[SK-MEL-2 (line)]] | alt | 70.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +9.1) | — |
| [[A-427 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10553), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F3]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[MFHAS1]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[SPOPL-DT]] | +0.54 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[ASXL2]] | +0.54 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[TULP4]] | +0.54 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[HIVEP1]] | +0.54 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[SNRPB]] | +0.54 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[EHBP1]] | +0.53 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[AGO2]] | +0.53 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[EPHB2]] | +0.52 | +0.51 / +0.54 | both halves | 1e-05 | same gene group |
| [[RASGRF2]] | +0.51 | +0.44 / +0.40 | both halves | 4e-05 |  |
| [[NEK10]] | +0.51 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARNT]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[DYNC2LI1]] | -0.58 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[USP30]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[RINT1]] | -0.55 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[VAMP7]] | -0.55 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[STAM2]] | -0.55 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[FAM229B]] | -0.55 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[IFT172]] | -0.54 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[MED23]] | -0.54 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[SKIC3]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[OSBPL7]] | -0.53 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[PEX2]] | -0.53 | -0.43 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZDHHC14's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SMCO2]] | B | SMCO2 activity lowers ZDHHC14's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.88× higher at baseline in the lines without SMCO2 | 0.070 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.490). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-0.8, -10.8); signed map (-13.1, 46.0). **Vector** length 106, 28.0% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +20.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | +2.4 | +3.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.3 | +2.1 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.6 | -3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.9 | +4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.9 | +6.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | +0.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.8 | -2.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.3 | -1.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:157,381,133-157,678,157 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20984, NEW1CP |
| Gene groups (HGNC) | Zinc fingers DHHC-type; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZN3](https://www.uniprot.org/uniprotkb/Q8IZN3) (Palmitoyltransferase ZDHHC14):

> Palmitoyltransferase that could catalyze the addition of palmitate onto various protein substrates. May have a palmitoyltransferase activity toward the beta-2 adrenergic receptor/ADRB2 and thereby regulate G protein-coupled receptor signaling. May play a role in cell differentiation and apoptosis.

**Summary**, from NCBI Gene [79683](https://www.ncbi.nlm.nih.gov/gene/79683):

> Enables palmitoyltransferase activity. Involved in peptidyl-L-cysteine S-palmitoylation. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20341](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20341) · Entrez [79683](https://www.ncbi.nlm.nih.gov/gene/79683) · UniProt [Q8IZN3](https://www.uniprot.org/uniprotkb/Q8IZN3) · Ensembl [ENSG00000175048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175048)

## Data

Gene col 10553: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10553); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10553, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10553]; `tensor/DDL_lfc|DDL_z.npy` [10553]; `embed/gene_vectors.npy` [10553]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10553 or target_col == 10553). Every well: [[ZDHHC14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
