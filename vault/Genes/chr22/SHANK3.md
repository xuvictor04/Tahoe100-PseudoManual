---
symbol: "SHANK3"
type: "gene"
col: 14756
ensembl_id: "ENSG00000251322"
name: "SH3 and multiple ankyrin repeat domains 3"
location: "22q13.33"
module: 132
arm: "+"
pooled_cpm: 8.27
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# SHANK3

*SH3 and multiple ankyrin repeat domains 3* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.75× (z +7.9, q 1e-12, up in 26 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.432× (z -16.8, q 0e+00, down in 35 of 43 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.381× (z -13.1, q 6e-37, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAZ]] (+0.77, fdr 7e-06), [[BRSK2]] (+0.72, fdr 7e-06), [[SEPTIN5]] (+0.69, fdr 7e-06); moves opposite to [[HELQ]] (-0.61, fdr 1e-05), [[AK9]] (-0.59, fdr 4e-05), [[TRMT1L]] (-0.58, fdr 1e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[PCED1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14756.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +7.9 | 1e-12 | 26/45 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +6.0 | 6e-07 | 20/45 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +5.4 | 1e-05 | 5/14 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.1 | 0.005 | 13/30 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.019 | 9/45 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 1.18× | +3.4 | 0.075 | 6/45 (SW1417, NCI-H1792, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.0 | 0.20 | 1/46 (BT-474) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14756.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.432×** | -16.8 | 0e+00 | 35/43 (LoVo, C32, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.381×** | -13.1 | 6e-37 | 34/43 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.453×** | -11.2 | 6e-27 | 28/41 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.611×** | -7.0 | 4e-10 | 26/45 (C32, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.615×** | -6.2 | 8e-08 | 23/45 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.742×** | -6.0 | 2e-07 | 20/40 (SHP-77, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.659×** | -5.9 | 3e-07 | 18/42 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -5.4 | 4e-06 | 21/44 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -5.3 | 8e-06 | 19/44 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.539×** | -4.6 | 3e-04 | 15/44 (LoVo, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.744×** | -4.2 | 0.001 | 11/45 (HOP62, LS 180, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -4.2 | 0.002 | 15/43 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.776×** | -3.6 | 0.014 | 15/45 (NCI-H460, CHP-212, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14756. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 20.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -15.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -12.0) |
| [[A-172 (line)]] | wt | 12.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -15.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -11.2) |
| [[C32 (line)]] | wt | 20.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -15.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 4.55 | 0 | 3 (2 ⚠) | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0721× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 3 (1 ⚠) | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.144× (z -8.9) |
| [[J82 (line)]] | alt | 12.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -11.3) |
| [[LoVo (line)]] | wt | 15.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -16.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.200× (z -11.2) |
| [[PANC-1 (line)]] | alt | 6.93 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -12.7) |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 2 | — | [[Gemfibrozil (drug)]] 0.5 µM 0.0541× (z -12.4) |
| [[A-427 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 6.76 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 1 | — | [[Dexmedetomidine (drug)]] 0.05 µM 0.0575× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 8.89 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 9.62 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -12.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[hTERT-HPNE (line)]] | wt | 5.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0589× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 4.03 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0568× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 9.39 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -8.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2347 (line)]] | alt | 7.45 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -8.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 8.43 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -14.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SHP-77 (line)]] | alt | 9.19 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0764× (z -14.6) |
| [[A498 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.970 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14756), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAZ]] | +0.77 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[BRSK2]] | +0.72 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SEPTIN5]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[PDZD4]] | +0.67 | +0.55 / +0.67 | both halves | 1e-05 | same gene group |
| [[KLHL17]] | +0.67 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[DGKZ]] | +0.67 | +0.61 / +0.58 | both halves | 8e-06 | same gene group |
| [[CACNA1H]] | +0.65 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[AIF1L]] | +0.65 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[JAG2]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[POLRMT]] | +0.65 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[PARD6G]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 | same gene group |
| [[TMEM201]] | +0.64 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HELQ]] | -0.61 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[AK9]] | -0.59 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[TRMT1L]] | -0.58 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.58 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[TMEM260]] | -0.58 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[GATAD1]] | -0.57 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[ZNF226]] | -0.56 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[THAP2]] | -0.55 | -0.54 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCED1B]] | B | PCED1B activity lowers SHANK3's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 2.31× higher at baseline in the lines without PCED1B | 0.014 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[KIF26A]] | B | KIF26A activity raises SHANK3's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.99× lower at baseline in the lines without KIF26A | 0.014 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[SNTA1]] | B | SNTA1 activity raises SHANK3's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 2.74× lower at baseline in the lines without SNTA1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[B4GALNT4]] | B | B4GALNT4 activity raises SHANK3's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 1.80× lower at baseline in the lines without B4GALNT4 | 0.030 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A |
| [[SEPTIN5]] | B | SEPTIN5 activity raises SHANK3's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.80× lower at baseline in the lines without SEPTIN5 | 0.033 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[JAG2]] | B | JAG2 activity raises SHANK3's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.88× lower at baseline in the lines without JAG2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[GNAZ]] | B | GNAZ activity raises SHANK3's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without GNAZ | 0.043 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SHANK3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CTXN1]] | B | CTXN1 activity raises SHANK3's level | lines that do not express CTXN1 (8) vs lines expressing it (42) | 2.13× lower at baseline in the lines without CTXN1 | 0.045 | ⚠ within organs, on part of the lines; also absent: PARD6G, SLC29A4, CBX2; maybe low, not absent |
| [[WNK2]] | B | WNK2 activity raises SHANK3's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.70× lower at baseline in the lines without WNK2 | 0.051 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[PARD6G]] | B | PARD6G activity raises SHANK3's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.08× lower at baseline in the lines without PARD6G | 0.051 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[SEPTIN3]] | B | SEPTIN3 activity raises SHANK3's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without SEPTIN3 | 0.055 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.837). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.6, 41.2); signed map (-23.8, 36.3). **Vector** length 69.1, 11.0% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | -0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -11.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.6 | -16.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -6.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | SH3 and multiple ankyrin repeat domains 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,674,408-50,733,212 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPANK-2, prosap2, KIAA1650, PSAP2 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Sterile alpha motif domain containing; PDZ domain containing; SH3 domain containing |
| Reactome | 6 pathways, smallest: RET signaling; Neurexins and neuroligins; Protein-protein interactions at synapses |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYB0](https://www.uniprot.org/uniprotkb/Q9BYB0) (SH3 and multiple ankyrin repeat domains protein 3):

> Major scaffold postsynaptic density protein which interacts with multiple proteins and complexes to orchestrate the dendritic spine and synapse formation, maturation and maintenance. Interconnects receptors of the postsynaptic membrane including NMDA-type and metabotropic glutamate receptors via complexes with GKAP/PSD-95 and HOMER, respectively, and the actin-based cytoskeleton. Plays a role in the structural and functional organization of the dendritic spine and synaptic junction through the …

**Summary**, from NCBI Gene [85358](https://www.ncbi.nlm.nih.gov/gene/85358):

> This gene is a member of the Shank gene family. Shank proteins are multidomain scaffold proteins of the postsynaptic density that connect neurotransmitter receptors, ion channels, and other membrane proteins to the actin cytoskeleton and G-protein-coupled signaling pathways. Shank proteins also play a role in synapse formation and dendritic spine maturation. Mutations in this gene are a cause of autism spectrum disorder (ASD), which is characterized by impairments in social interaction and …

**Accessions** — [HGNC:14294](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14294) · Entrez [85358](https://www.ncbi.nlm.nih.gov/gene/85358) · UniProt [Q9BYB0](https://www.uniprot.org/uniprotkb/Q9BYB0) · Ensembl [ENSG00000251322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251322)

## Data

Gene col 14756: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14756); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14756, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14756]; `tensor/DDL_lfc|DDL_z.npy` [14756]; `embed/gene_vectors.npy` [14756]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14756 or target_col == 14756). Every well: [[SHANK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHANK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
