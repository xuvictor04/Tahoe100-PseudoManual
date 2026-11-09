---
symbol: "TMEM144"
type: "gene"
col: 8877
ensembl_id: "ENSG00000164124"
name: "transmembrane protein 144"
location: "4q32.1"
module: 99
arm: "+"
pooled_cpm: 32.44
n_lines_expressing: 47
n_dd_up: 1
n_dd_down: 35
n_dd_up_clean: 1
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# TMEM144

*transmembrane protein 144* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.47× (z +5.2, q 1e-04, up in 22 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HepG2/C3A 3.14×, A-172 2.56×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 2.60×).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.346× (z -20.7, q 0e+00, down in 37 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FHIP1A]] (+0.59, fdr 1e-05), [[PDK3]] (+0.59, fdr 1e-05), [[GPR160]] (+0.59, fdr 2e-05); moves opposite to [[AHNAK]] (-0.54, fdr 3e-05), [[AVEN]] (-0.53, fdr 5e-05), [[PLXNA2]] (-0.52, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[PLXNA2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8877.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HepG2/C3A 3.14×, A-172 2.56×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 2.60×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +5.2 | 1e-04 | 22/43 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.1 | 0.58 | 12/45 (CFPAC-1, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8877.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.346×** | -20.7 | 0e+00 | 37/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.266×** | -18.2 | 0e+00 | 34/44 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -13.1 | 9e-37 | 35/44 (MIA PaCa-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.409×** | -12.3 | 9e-33 | 37/43 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.412×** | -11.7 | 9e-30 | 39/44 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.442×** | -11.2 | 2e-27 | 36/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.456×** | -10.4 | 2e-23 | 31/41 (NCI-H1792, A549, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.471×** | -10.4 | 3e-23 | 39/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.534×** | -8.6 | 4e-16 | 26/45 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.572×** | -7.7 | 1e-12 | 25/43 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.581×** | -7.5 | 5e-12 | 30/43 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.357×** | -7.4 | 5e-12 | 32/42 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.586×** | -7.3 | 9e-12 | 25/45 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.364×** | -7.3 | 1e-11 | 28/45 (COLO 205, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.591×** | -7.0 | 1e-10 | 27/43 (MIA PaCa-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.673×** | -5.4 | 2e-06 | 24/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.675×** | -5.4 | 2e-06 | 26/44 (A-427, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 222 | 0 | 16 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -26.7) |
| [[MIA PaCa-2 (line)]] | alt | 58.2 | 0 | 13 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0982× (z -23.1) |
| [[HEC-1-A (line)]] | alt | 53.0 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -16.6) |
| [[PANC-1 (line)]] | alt | 16.7 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -15.0) |
| [[COLO 205 (line)]] | alt | 36.3 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 50.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0202× (z -26.3) |
| [[A549 (line)]] | wt | 21.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -16.1) |
| [[LoVo (line)]] | wt | 15.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0951× (z -24.6) |
| [[NCI-H2347 (line)]] | alt | 33.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -16.2) |
| [[A-427 (line)]] | wt | 101 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.427× (z -8.8) |
| [[C-33 A (line)]] | alt | 34.1 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 33.4 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.141× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.358× (z -8.6) |
| [[LS 180 (line)]] | wt | 33.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 34.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -20.0) |
| [[RKO (line)]] | wt | 35.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -19.5) |
| [[CFPAC-1 (line)]] | alt | 38.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -20.2) |
| [[HT-29 (line)]] | alt | 20.9 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.259× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 19.3 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0831× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0225× (z -20.8) |
| [[SW 900 (line)]] | alt | 20.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -13.0) |
| [[A-172 (line)]] | wt | 24.2 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.60× (z +9.2) | — |
| [[A498 (line)]] | wt | 9.99 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 9.93 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.247× (z -9.5) |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0639× (z -12.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 9.57 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0801× (z -10.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.2) |
| [[KATO III (line)]] | alt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 9.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0527× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 26.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.3) |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.56 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.06 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.20 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHIP1A]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[PDK3]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[GPR160]] | +0.59 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[SEPTIN6]] | +0.56 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[FRRS1]] | +0.55 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[FAM162A]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ABCB9]] | +0.54 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[ZNF516]] | +0.53 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[ALDOC]] | +0.53 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[NEXMIF]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[BCL9]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[RIMKLA]] | +0.52 | +0.51 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHNAK]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[AVEN]] | -0.53 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[PLXNA2]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[TECPR2]] | -0.51 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[HIPK3]] | -0.51 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[TTLL11]] | -0.50 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[UBTF]] | -0.50 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[ITPRIPL2]] | -0.49 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[ZNF623]] | -0.48 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[PARVA]] | -0.48 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[WDR27]] | -0.46 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[FGD5-AS1]] | -0.46 | -0.36 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TMEM144's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXNA2]] | C | TMEM144 activity lowers PLXNA2's level | lines that do not express TMEM144 (3) vs lines expressing it (47) | 4.41× higher at baseline in the lines without TMEM144 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: WNK4, RNF103-CHMP3, RBMS2; maybe low, not absent; its own permutation p |
| [[RAB3A]] | C | TMEM144 activity lowers RAB3A's level | lines that do not express TMEM144 (3) vs lines expressing it (47) | 1.89× higher at baseline in the lines without TMEM144 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: WNK4, RNF103-CHMP3, RBMS2; maybe low, not absent; its own permutation p |
| [[NEFM]] | C | TMEM144 activity lowers NEFM's level | lines that do not express TMEM144 (3) vs lines expressing it (47) | 2.65× higher at baseline in the lines without TMEM144 | 0.083 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: WNK4, RNF103-CHMP3, RBMS2; maybe low, not absent |
| [[SYNGR1]] | C | TMEM144 activity lowers SYNGR1's level | lines that do not express TMEM144 (3) vs lines expressing it (47) | 3.15× higher at baseline in the lines without TMEM144 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: WNK4, RNF103-CHMP3, RBMS2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.0, -11.7); signed map (-32.4, 22.5). **Vector** length 81.8, 18.5% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.6 | +1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +1.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +1.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.8 | -10.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -18.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -5.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.6 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 144 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:158,201,604-158,255,416 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11155, SLC35G7 |
| Matched by | ensembl_id |

UniProt [Q7Z5S9](https://www.uniprot.org/uniprotkb/Q7Z5S9) carries no function annotation.

**Summary**, from NCBI Gene [55314](https://www.ncbi.nlm.nih.gov/gene/55314):

> Predicted to enable carbohydrate transmembrane transporter activity. Predicted to be involved in carbohydrate transmembrane transport. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25633](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25633) · Entrez [55314](https://www.ncbi.nlm.nih.gov/gene/55314) · UniProt [Q7Z5S9](https://www.uniprot.org/uniprotkb/Q7Z5S9) · Ensembl [ENSG00000164124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164124)

## Data

Gene col 8877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8877); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8877]; `tensor/DDL_lfc|DDL_z.npy` [8877]; `embed/gene_vectors.npy` [8877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8877 or target_col == 8877). Every well: [[TMEM144 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM144.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
