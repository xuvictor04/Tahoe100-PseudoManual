---
symbol: "PTPRU"
type: "gene"
col: 690
ensembl_id: "ENSG00000060656"
name: "protein tyrosine phosphatase receptor type U"
location: "1p35.3"
module: 132
arm: "+"
pooled_cpm: 13.54
n_lines_expressing: 43
n_dd_up: 8
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# PTPRU

*protein tyrosine phosphatase receptor type U* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.37× (z +6.0, q 1e-06, up in 19 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.544× (z -8.2, q 1e-13, down in 24 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.581× (z -6.9, q 2e-09, down in 26 of 38 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAG2]] (+0.60, fdr 1e-05), [[ADAMTS7]] (+0.57, fdr 9e-05), [[SHANK3]] (+0.56, fdr 1e-05); moves opposite to [[TM9SF5P]] (-0.52, fdr 4e-05), [[IQCK]] (-0.51, fdr 3e-05), [[ZCWPW2]] (-0.48, fdr 7e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LAPTM5]] → it (grade B ⚠); 4 go from it, the strongest it → [[TTLL12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 690.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +6.0 | 1e-06 | 19/41 (LOX-IMVI, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +5.7 | 3e-06 | 21/40 (MIA PaCa-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +5.2 | 4e-05 | 19/41 (NCI-H23, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.021 | 17/40 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.021 | 13/41 (Hs 766T, NCI-H1573, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.29×** | +3.4 | 0.062 | 9/40 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.3 | 0.085 | 5/41 (LoVo, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.085 | 13/40 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.28× | +3.1 | 0.13 | 2/21 (RPMI-7951, SW480) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.25× | +3.0 | 0.13 | 14/41 (Hs 766T, NCI-H1573, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | 1.25× | +3.0 | 0.13 | 8/41 (Hs 766T, SW 1088, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 690.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.544×** | -8.2 | 1e-13 | 24/39 (SNU-423, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.581×** | -6.9 | 2e-09 | 26/38 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.620×** | -6.4 | 2e-08 | 23/36 (RPMI-7951, SNU-423, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.644×** | -5.9 | 5e-07 | 24/40 (C32, CFPAC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.664×** | -5.5 | 4e-06 | 19/41 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.677×** | -5.2 | 1e-05 | 20/40 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.777×** | -4.8 | 1e-04 | 23/38 (Hs 766T, HOP62, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.689×** | -4.7 | 2e-04 | 17/40 (NCI-H1792, C32, …) | rises with dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.709×** | -4.6 | 2e-04 | 20/41 (LoVo, RPMI-7951, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -4.6 | 3e-04 | 21/38 (CFPAC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.732×** | -4.2 | 0.001 | 15/40 (CFPAC-1, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.751×** | -3.9 | 0.005 | 16/41 (NCI-H2030, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.779×** | -3.4 | 0.033 | 12/41 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -3.3 | 0.041 | 12/38 (SK-MEL-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.785×** | -3.3 | 0.043 | 9/41 (SW48, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.651×** | -3.0 | 0.075 | 12/40 (Panc 03.27, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 20.9 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -13.0) |
| [[LoVo (line)]] | wt | 32.8 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.320× (z -10.2) |
| [[SNU-423 (line)]] | alt | 6.10 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0483× (z -11.1) |
| [[C-33 A (line)]] | alt | 28.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[CFPAC-1 (line)]] | alt | 40.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 18.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.4) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.274× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 26.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0739× (z -9.3) |
| [[BT-474 (line)]] | alt | 6.61 | 0 | 1 | — | [[Osimertinib (mesylate) (drug)]] 5 µM 0.0531× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.7) ⚠ cell-cycle shift, explains ~97% of this change |
| [[Hs 766T (line)]] | wt | 35.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -13.3) ⚠ cell-cycle shift, explains ~97% of this change |
| [[NCI-H1792 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -11.5) ⚠ cell-cycle shift, explains ~97% of this change |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0390× (z -15.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -9.6) |
| [[SW48 (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAG2]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ADAMTS7]] | +0.57 | +0.36 / +0.70 | both halves | 9e-05 |  |
| [[SHANK3]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[OTULINL]] | +0.55 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[MINK1]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PACSIN2]] | +0.53 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[LAPTM5]] | +0.53 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ARHGAP45]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[SMARCD3]] | +0.52 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ZDHHC9]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[SHROOM2]] | +0.52 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[DAB2IP]] | +0.52 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM9SF5P]] | -0.52 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[IQCK]] | -0.51 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[ZCWPW2]] | -0.48 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[GPATCH2]] | -0.48 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[FTX]] | -0.47 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[DOCK10]] | -0.44 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[ANKHD1-EIF4EBP3]] | -0.43 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[NEK11]] | -0.42 | -0.44 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAPTM5]] | B | LAPTM5 activity raises PTPRU's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.84× lower at baseline in the lines without LAPTM5 | 0.023 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PTPRU's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[IQSEC1]] | C | IQSEC1 activity raises PTPRU's level | lines that do not express IQSEC1 (3) vs lines expressing it (47) | 4.13× lower at baseline in the lines without IQSEC1 | 0.085 | ⚠ few lines (3 vs 47); across organs; also absent: CD99, CLTCL1, ANO7; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTLL12]] | B | PTPRU activity raises TTLL12's level | lines that do not express PTPRU (7) vs lines expressing it (43) | 1.30× lower at baseline in the lines without PTPRU | 0.069 | ⚠ within organs, on part of the lines; also absent: FBXO16, RNF144A |
| [[RHOBTB2]] | B | PTPRU activity raises RHOBTB2's level | lines that do not express PTPRU (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without PTPRU | 0.069 | ⚠ within organs, on part of the lines; also absent: FBXO16, RNF144A |
| [[RNF175]] | B | PTPRU activity raises RNF175's level | lines that do not express PTPRU (7) vs lines expressing it (43) | 1.10× lower at baseline in the lines without PTPRU | 0.087 | ⚠ within organs, on part of the lines; also absent: FBXO16, RNF144A |
| [[TRIM35]] | B | PTPRU activity raises TRIM35's level | lines that do not express PTPRU (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without PTPRU | 0.088 | ⚠ within organs, on part of the lines; also absent: FBXO16, RNF144A |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.550). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-1.6, 40.6); signed map (-24.0, 35.6). **Vector** length 85.1, 18.2% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.0 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | +2.8 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | +2.8 | -1.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.4 | +1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.9 | +1.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.4 | -6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | -2.1 | -3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -5.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type U |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:29,236,516-29,326,813 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTPRO, hPTP-J, PCP-2, FMI, PTP |
| Gene groups (HGNC) | Fibronectin type III domain containing; Protein tyrosine phosphatases receptor type |
| Reactome | 2 pathways, smallest: Signaling by SCF-KIT; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92729](https://www.uniprot.org/uniprotkb/Q92729) (Receptor-type tyrosine-protein phosphatase U):

> Tyrosine-protein phosphatase which dephosphorylates CTNNB1. Regulates CTNNB1 function both in cell adhesion and signaling. May function in cell proliferation and migration and play a role in the maintenance of epithelial integrity. May play a role in megakaryocytopoiesis.

**Summary**, from NCBI Gene [10076](https://www.ncbi.nlm.nih.gov/gene/10076):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region, a single transmembrane region, and two tandem intracellular catalytic domains, and thus represents a receptor-type PTP. The extracellular region contains a meprin-A5 antigen-PTP (MAM) …

**Accessions** — [HGNC:9683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9683) · Entrez [10076](https://www.ncbi.nlm.nih.gov/gene/10076) · UniProt [Q92729](https://www.uniprot.org/uniprotkb/Q92729) · Ensembl [ENSG00000060656](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060656)

## Data

Gene col 690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 690); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 690]; `tensor/DDL_lfc|DDL_z.npy` [690]; `embed/gene_vectors.npy` [690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 690 or target_col == 690). Every well: [[PTPRU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
