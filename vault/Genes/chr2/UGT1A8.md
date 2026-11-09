---
symbol: "UGT1A8"
type: "gene"
col: 14313
ensembl_id: "ENSG00000242366"
name: "UDP glucuronosyltransferase family 1 member A8"
location: "2q37.1"
module: 44
arm: "+"
pooled_cpm: 6.16
n_lines_expressing: 17
n_dd_up: 22
n_dd_down: 15
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 35
direction_downstream: 39
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# UGT1A8

*UDP glucuronosyltransferase family 1 member A8* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.53× (z +10.4, q 1e-22, up in 0 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.421× (z -6.9, q 3e-09, down in 13 of 14 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.464× (z -5.9, q 7e-07, down in 12 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UGT1A9]] (+0.98, fdr 7e-06, ⚠ same locus), [[UGT1A6]] (+0.88, fdr 7e-06, ⚠ same locus), [[UGT1A1]] (+0.81, fdr 7e-06, ⚠ same locus), [[PRR15]] (+0.73, fdr 7e-06), [[PIP5K1B]] (+0.71, fdr 7e-06), [[PRR15-DT]] (+0.71, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 35 arrows point to it, the strongest [[LURAP1]] → it (grade B ⚠); 39 go from it, the strongest it → [[PTPN22]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14313.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +10.4 | 1e-22 | 0/15 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.73×** | +10.0 | 3e-21 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +7.7 | 2e-12 | 1/8 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +6.4 | 2e-08 | 1/11 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.59×** | +4.3 | 0.002 | 9/15 (Hs 766T, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +4.0 | 0.007 | 2/15 (SW480, LoVo) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +3.9 | 0.008 | 1/12 (SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +3.8 | 0.011 | 1/14 (SW480) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.7 | 0.011 | 3/13 (SNU-423, COLO 205, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.016 | 9/15 (SW480, AsPC-1, …) | all doses, flat |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.90×** | +3.6 | 0.016 | 0/12 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.88×** | +3.5 | 0.018 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **2.31×** | +3.5 | 0.023 | 3/13 (AsPC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.4 | 0.024 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.024 | 13/14 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM |  | **1.51×** | +3.2 | 0.043 | 0/14 | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.52×** | +3.1 | 0.053 | 5/15 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.0 | 0.070 | 0/14 | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.076 | 9/15 (SW480, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +2.9 | 0.086 | 9/13 (SW480, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14313.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.421×** | -6.9 | 3e-09 | 13/14 (HT-29, KATO III, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.456×** | -6.3 | 1e-07 | 13/14 (HT-29, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.464×** | -5.9 | 7e-07 | 12/14 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.511×** | -5.4 | 1e-05 | 13/14 (KATO III, Hs 766T, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.524×** | -5.2 | 3e-05 | 11/14 (MIA PaCa-2, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.579×** | -4.4 | 0.001 | 12/14 (KATO III, HT-29, …) | rises with dose | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.630×** | -3.7 | 0.017 | 8/13 (LS 180, HT-29, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.736×** | -3.5 | 0.033 | 12/15 (HT-29, LS 180, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.658×** | -3.4 | 0.047 | 5/14 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.649×** | -3.3 | 0.047 | 6/13 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.662×** | -3.3 | 0.047 | 4/14 (hTERT-HPNE, KATO III, …) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.655×** | -3.3 | 0.049 | 1/14 (Panc 03.27) | top dose only | plate-row cell shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.666×** | -3.3 | 0.049 | 8/14 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.675×** | -3.0 | 0.095 | 6/15 (Hs 766T, AsPC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.688×** | -3.0 | 0.099 | 12/14 (KATO III, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 67.1 | 0 | 17 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0913× (z -21.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -19.5) |
| [[KATO III (line)]] | alt | 62.9 | 0 | 11 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0762× (z -23.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -13.6) |
| [[Hs 766T (line)]] | wt | 37.7 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -12.8) |
| [[LS 180 (line)]] | wt | 6.57 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0326× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 7.67 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0656× (z -13.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0784× (z -9.8) |
| [[COLO 205 (line)]] | alt | 16.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0379× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 17.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0903× (z -8.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 2.91 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0974× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.468 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.764 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.624 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.614 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UGT1A9]] | +0.98 | +0.97 / +0.97 | both halves | 7e-06 | same gene group; pathway: Aspirin ADME; STRING 997; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[UGT1A6]] | +0.88 | +0.89 / +0.84 | both halves | 7e-06 | same gene group; pathway: Aspirin ADME; STRING 997; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[UGT1A1]] | +0.81 | +0.81 / +0.74 | both halves | 7e-06 | same gene group; pathway: Aspirin ADME; STRING 996; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PRR15]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[PIP5K1B]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PRR15-DT]] | +0.71 | +0.65 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[MGAM2]] | +0.70 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[HNF1A-AS1]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ABO]] | +0.67 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[TSPAN8]] | +0.67 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[GNA14]] | +0.66 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[PRR15L]] | +0.66 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[BCL2L15]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[LGALS4]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[CFTR]] | +0.64 | +0.68 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 3, C 32. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LURAP1]] | B | LURAP1 activity raises UGT1A8's level | lines that do not express LURAP1 (13) vs lines expressing it (37) | 2.58× lower at baseline in the lines without LURAP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ZG16B; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers UGT1A8's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[HNMT]] | B | HNMT activity raises UGT1A8's level | lines that do not express HNMT (17) vs lines expressing it (33) | 2.41× lower at baseline in the lines without HNMT | 0.095 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[UGT1A1]] | C | UGT1A1 activity raises UGT1A8's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 7.14× lower at baseline in the lines without UGT1A1 | 2e-05 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |
| [[UGT1A6]] | C | UGT1A6 activity raises UGT1A8's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 6.20× lower at baseline in the lines without UGT1A6 | 8e-05 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |
| [[CREB3L1]] | C | CREB3L1 activity raises UGT1A8's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 3.49× lower at baseline in the lines without CREB3L1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1; co-absent with the target |
| [[PLAAT4]] | C | PLAAT4 activity raises UGT1A8's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.78× lower at baseline in the lines without PLAAT4 | 0.007 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1; co-absent with the target |
| [[LINC01133]] | C | LINC01133 activity raises UGT1A8's level | lines that do not express LINC01133 (34) vs lines expressing it (16) | 3.55× lower at baseline in the lines without LINC01133 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPH, IL33, UGT1A1; co-absent with the target |
| [[TNFSF10]] | C | TNFSF10 activity raises UGT1A8's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 2.90× lower at baseline in the lines without TNFSF10 | 0.020 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75; co-absent with the target |
| [[IL20RA]] | C | IL20RA activity raises UGT1A8's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 3.42× lower at baseline in the lines without IL20RA | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10; co-absent with the target |
| [[LINC01559]] | C | LINC01559 activity raises UGT1A8's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 4.30× lower at baseline in the lines without LINC01559 | 0.029 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises UGT1A8's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 5.74× lower at baseline in the lines without NPSR1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 6, C 33. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN22]] | B | UGT1A8, [[UGT1A9]] activity raises PTPN22's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 1.87× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.023 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent genes |
| [[GATA6]] | B | UGT1A8 activity raises GATA6's level | lines that do not express UGT1A8 (33) vs lines expressing it (17) | 3.21× lower at baseline in the lines without UGT1A8 | 0.039 | ⚠ within organs, on part of the lines; co-absent genes; also absent: UGT1A1, UGT1A6, LINC01559 |
| [[ADD3-AS1]] | B | UGT1A8, [[UGT1A9]] activity raises ADD3-AS1's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 1.80× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.064 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent genes |
| [[MECOM]] | B | UGT1A8, [[UGT1A9]] activity raises MECOM's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 2.81× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.070 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent genes |
| [[TNFRSF14]] | B | UGT1A8, [[UGT1A9]] activity raises TNFRSF14's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 1.84× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.085 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent genes |
| [[MECOM]] | B | UGT1A8, [[UGT1A9]] activity weakens MECOM's drug response | lines that do not express UGT1A8, UGT1A9 (19) vs lines expressing them (12) | the lines without UGT1A8, UGT1A9 respond 0.89× as strongly (z diff +0.52); strongest at Panobinostat 0.05 µM: 2.10x vs 1.30x (z diff -3.1) | 0.086 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; target measured in part of the lines; both ways; artifact flags; co-absent genes |
| [[UGT1A6]] | C | UGT1A8, [[UGT1A9]] activity raises UGT1A6's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 8.89× lower at baseline in the lines without UGT1A8, UGT1A9 | 5e-05 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[UGT1A1]] | C | UGT1A8, [[UGT1A9]] activity raises UGT1A1's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 4.02× lower at baseline in the lines without UGT1A8, UGT1A9 | 3e-04 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[IL20RA]] | C | UGT1A8, [[UGT1A9]] activity raises IL20RA's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 3.72× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.004 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[CLRN3]] | C | UGT1A8 activity raises CLRN3's level | lines that do not express UGT1A8 (33) vs lines expressing it (17) | 2.48× lower at baseline in the lines without UGT1A8 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target |
| [[RASSF6]] | C | UGT1A8, [[UGT1A9]] activity raises RASSF6's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 3.71× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.007 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |
| [[LINC01559]] | C | UGT1A8, [[UGT1A9]] activity raises LINC01559's level | lines that do not express UGT1A8, UGT1A9 (33) vs lines expressing them (17) | 3.05× lower at baseline in the lines without UGT1A8, UGT1A9 | 0.007 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A6, LINC01559; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.8, 51.4); signed map (63.4, 3.8). **Vector** length 65.4, 23.9% of its response variance represented; |z| ≥ 3 in 506 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.6 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +10.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.1 | -5.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -3.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.1 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -3.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.0 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -3.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | UDP glucuronosyltransferase family 1 member A8 |
| Locus type | complex locus constituent (other) |
| Location | 2q37.1 — chr2:233,617,633-233,773,300 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UGT1H |
| Gene groups (HGNC) | UDP glucuronosyltransferases |
| Reactome | 5 pathways, smallest: Glucuronidation; Aspirin ADME; Phase II - Conjugation of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAW9](https://www.uniprot.org/uniprotkb/Q9HAW9) (UDP-glucuronosyltransferase 1A8):

> [Isoform 1]: UDP-glucuronosyltransferase (UGT) that catalyzes phase II biotransformation reactions in which lipophilic substrates are conjugated with glucuronic acid to increase the metabolite's water solubility, thereby facilitating excretion into either the urine or bile. Essential for the elimination and detoxification of drugs, xenobiotics and endogenous compounds. Catalyzes the glucuronidation of endogenous steroid hormones such as androgens and estrogens. Produces dihydrotestosterone …

**Summary**, from NCBI Gene [54576](https://www.ncbi.nlm.nih.gov/gene/54576):

> This gene encodes a UDP-glucuronosyltransferase, an enzyme of the glucuronidation pathway that transforms small lipophilic molecules, such as steroids, bilirubin, hormones, and drugs, into water-soluble, excretable metabolites. This gene is part of a complex locus that encodes several UDP-glucuronosyltransferases. The locus includes thirteen unique alternate first exons followed by four common exons. Four of the alternate first exons are considered pseudogenes. Each of the remaining nine 5' …

**Accessions** — [HGNC:12540](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12540) · Entrez [54576](https://www.ncbi.nlm.nih.gov/gene/54576) · UniProt [Q9HAW9](https://www.uniprot.org/uniprotkb/Q9HAW9) · Ensembl [ENSG00000242366](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242366)

## Data

Gene col 14313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14313); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14313]; `tensor/DDL_lfc|DDL_z.npy` [14313]; `embed/gene_vectors.npy` [14313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14313 or target_col == 14313). Every well: [[UGT1A8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UGT1A8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
