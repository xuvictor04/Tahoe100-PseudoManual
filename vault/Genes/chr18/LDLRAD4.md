---
symbol: "LDLRAD4"
type: "gene"
col: 9682
ensembl_id: "ENSG00000168675"
name: "low density lipoprotein receptor class A domain containing 4"
location: "18p11.21"
module: 44
arm: "+"
pooled_cpm: 23.81
n_lines_expressing: 27
n_dd_up: 21
n_dd_down: 26
n_dd_up_clean: 17
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 10
direction_downstream: 9
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# LDLRAD4

*low density lipoprotein receptor class A domain containing 4* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.35× (z +17.3, q 0e+00, up in 7 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.543× (z -8.7, q 2e-15, down in 19 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP10B]] (+0.67, fdr 7e-06), [[ARHGAP6]] (+0.62, fdr 1e-05), [[GAS7]] (+0.61, fdr 2e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PIP5K1B]] → it (grade B ⚠); 9 go from it, the strongest it → [[TOX3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9682.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +17.3 | 0e+00 | 7/24 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.26×** | +16.4 | 0e+00 | 12/25 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.05×** | +10.2 | 3e-22 | 11/23 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +8.6 | 2e-15 | 9/25 (HepG2/C3A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.81×** | +8.5 | 2e-15 | 3/22 (HS-578T, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +8.4 | 3e-15 | 9/24 (NCI-H23, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +7.0 | 2e-10 | 7/24 (NCI-H23, HOP62, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +5.9 | 2e-07 | 4/25 (C-33 A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.9 | 5e-05 | 6/23 (HOP62, CHP-212, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.7 | 1e-04 | 3/15 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +4.6 | 2e-04 | 1/18 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +4.5 | 3e-04 | 3/25 (NCI-H23, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 6e-04 | 9/24 (AsPC-1, NCI-H23, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.33×** | +3.9 | 0.004 | 5/22 (HOP62, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.008 | 2/23 (NCI-H23, BT-474) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.013 | 3/23 (HepG2/C3A, AsPC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.038 | 10/24 (AsPC-1, A549, …) | two highest doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.056 | 6/23 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.088 | 8/23 (Hs 766T, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9682.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.543×** | -8.7 | 2e-15 | 19/23 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.583×** | -7.7 | 4e-12 | 19/24 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.625×** | -6.7 | 4e-09 | 16/23 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -6.7 | 4e-09 | 19/23 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.657×** | -5.7 | 1e-06 | 17/23 (KATO III, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.723×** | -4.6 | 4e-04 | 13/23 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.806×** | -4.3 | 0.001 | 18/25 (KATO III, C32, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.562×** | -4.3 | 0.001 | 12/23 (A-172, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.740×** | -4.3 | 0.001 | 12/24 (KATO III, C32, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.756×** | -4.0 | 0.004 | 9/23 (KATO III, A-172, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.768×** | -3.7 | 0.009 | 12/24 (KATO III, HT-29, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.771×** | -3.7 | 0.011 | 11/24 (HepG2/C3A, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.767×** | -3.6 | 0.013 | 15/23 (KATO III, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.776×** | -3.6 | 0.013 | 9/24 (KATO III, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.791×** | -3.3 | 0.033 | 3/25 (NCI-H23, Hs 766T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.794×** | -3.3 | 0.034 | 14/24 (KATO III, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.799×** | -3.2 | 0.043 | 7/24 (H4, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9682. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 124 | 0 | 24 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0801× (z -23.2) |
| [[LoVo (line)]] | wt | 50.7 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -23.4) |
| [[HepG2_C3A (line)]] | wt | 115 | 2 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -8.7) |
| [[COLO 205 (line)]] | alt | 116 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -15.8) |
| [[SHP-77 (line)]] | alt | 207 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.383× (z -8.5) |
| [[C32 (line)]] | wt | 110 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.230× (z -9.5) |
| [[A-427 (line)]] | wt | 28.4 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.51× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -10.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 39.4 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.106× (z -12.1) |
| [[HOP62 (line)]] | alt | 12.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +9.0) | — |
| [[A-172 (line)]] | wt | 173 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -10.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 6.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 22.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 7.05 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.13× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0431× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.42 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.23 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.82 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.18 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9682), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP10B]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ARHGAP6]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 | same gene group |
| [[GAS7]] | +0.61 | +0.58 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[CD200]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[TOX3]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[AGR3]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[LRP4]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[TMPRSS2]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CRACDL]] | +0.56 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[TSPAN8]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[CTTNBP2]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[PLEKHS1]] | +0.55 | +0.50 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIP5K1B]] | B | PIP5K1B activity raises LDLRAD4's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 2.13× lower at baseline in the lines without PIP5K1B | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| [[LGR5]] | B | LGR5 activity raises LDLRAD4's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 3.10× lower at baseline in the lines without LGR5 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[LINC01814]] | B | LINC01814 activity raises LDLRAD4's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 1.92× lower at baseline in the lines without LINC01814 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |
| [[C4BPB]] | B | C4BPB activity raises LDLRAD4's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.19× lower at baseline in the lines without C4BPB | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[TOX3]] | B | TOX3 activity raises LDLRAD4's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 2.13× lower at baseline in the lines without TOX3 | 0.058 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |
| [[CRACDL]] | B | CRACDL activity raises LDLRAD4's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 1.99× lower at baseline in the lines without CRACDL | 0.079 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[INPP5D]] | C | INPP5D activity raises LDLRAD4's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 3.13× lower at baseline in the lines without INPP5D | 0.021 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5; co-absent with the target |
| [[ATP10B]] | C | ATP10B activity raises LDLRAD4's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 3.37× lower at baseline in the lines without ATP10B | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises LDLRAD4's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 3.39× lower at baseline in the lines without PLA2G2A | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises LDLRAD4's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 3.29× lower at baseline in the lines without NPSR1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOX3]] | B | LDLRAD4 activity raises TOX3's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 2.39× lower at baseline in the lines without LDLRAD4 | 0.020 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958 |
| [[PIP5K1B]] | B | LDLRAD4 activity raises PIP5K1B's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 1.70× lower at baseline in the lines without LDLRAD4 | 0.047 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958 |
| [[GCNT3]] | B | LDLRAD4 activity raises GCNT3's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 1.86× lower at baseline in the lines without LDLRAD4 | 0.056 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958 |
| [[C4BPB]] | B | LDLRAD4 activity raises C4BPB's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 1.58× lower at baseline in the lines without LDLRAD4 | 0.085 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958 |
| [[GPX2]] | B | LDLRAD4 activity raises GPX2's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without LDLRAD4 | 0.093 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958 |
| [[ATP10B]] | C | LDLRAD4 activity raises ATP10B's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 2.06× lower at baseline in the lines without LDLRAD4 | 0.028 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958; co-absent with the target |
| [[INPP5D]] | C | LDLRAD4 activity raises INPP5D's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 1.84× lower at baseline in the lines without LDLRAD4 | 0.037 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958; co-absent with the target |
| [[SMIM2-AS1]] | C | LDLRAD4 activity raises SMIM2-AS1's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 1.68× lower at baseline in the lines without LDLRAD4 | 0.072 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958; co-absent with the target |
| [[MUC13]] | C | LDLRAD4 activity raises MUC13's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without LDLRAD4 | 0.087 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.578). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.1, 58.1); signed map (67.1, 2.4). **Vector** length 76.7, 19.5% of its response variance represented; |z| ≥ 3 in 771 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.1 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.9 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +17.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +16.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +0.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -4.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.3 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -2.1 | -0.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -2.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | low density lipoprotein receptor class A domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:13,217,498-13,652,755 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C18orf1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O15165](https://www.uniprot.org/uniprotkb/O15165) (Low-density lipoprotein receptor class A domain-containing protein 4):

> Functions as a negative regulator of TGF-beta signaling and thereby probably plays a role in cell proliferation, differentiation, apoptosis, motility, extracellular matrix production and immunosuppression. In the canonical TGF-beta pathway, ZFYVE9/SARA recruits the intracellular signal transducer and transcriptional modulators SMAD2 and SMAD3 to the TGF-beta receptor. Phosphorylated by the receptor, SMAD2 and SMAD3 then form a heteromeric complex with SMAD4 that translocates to the nucleus to …

**Summary**, from NCBI Gene [753](https://www.ncbi.nlm.nih.gov/gene/753):

> Enables R-SMAD binding activity. Involved in negative regulation of cell migration; negative regulation of epithelial to mesenchymal transition; and negative regulation of transmembrane receptor protein serine/threonine kinase signaling pathway. Located in early endosome membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1224](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1224) · Entrez [753](https://www.ncbi.nlm.nih.gov/gene/753) · UniProt [O15165](https://www.uniprot.org/uniprotkb/O15165) · Ensembl [ENSG00000168675](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168675)

## Data

Gene col 9682: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9682); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9682, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9682]; `tensor/DDL_lfc|DDL_z.npy` [9682]; `embed/gene_vectors.npy` [9682]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9682 or target_col == 9682). Every well: [[LDLRAD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LDLRAD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
