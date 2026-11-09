---
symbol: "PDE4C"
type: "gene"
col: 2637
ensembl_id: "ENSG00000105650"
name: "phosphodiesterase 4C"
location: "19p13.11"
module: 53
arm: "+"
pooled_cpm: 5.67
n_lines_expressing: 47
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# PDE4C

*phosphodiesterase 4C* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 19.3× (z +35.9, q 0e+00, up in 35 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.588× (z -4.6, q 0.002, down in 19 of 43 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.05 µM: 0.590× (z -4.5, q 0.002, down in 19 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA4A]] (+0.70, fdr 7e-06), [[CATSPERD]] (+0.66, fdr 1e-05), [[LINC02580]] (+0.65, fdr 7e-06); moves opposite to [[NTAQ1]] (-0.56, fdr 3e-05), [[ADPGK]] (-0.54, fdr 3e-05), [[WHAMMP1]] (-0.53, fdr 7e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); 3 go from it, the strongest it → [[SEPTIN9-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2637.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **19.3×** | +35.9 | 0e+00 | 35/37 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.74×** | +16.4 | 0e+00 | 26/37 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +10.7 | 2e-24 | 24/37 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.27×** | +9.8 | 2e-20 | 6/12 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.53×** | +8.0 | 2e-13 | 11/25 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.60×** | +7.9 | 3e-13 | 21/40 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.41×** | +7.5 | 4e-12 | 28/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +7.5 | 4e-12 | 24/43 (LoVo, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.26×** | +7.0 | 2e-10 | 22/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +7.0 | 2e-10 | 7/13 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +6.2 | 4e-08 | 22/42 (SW480, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.97×** | +5.8 | 3e-07 | 20/41 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.6 | 2e-04 | 8/25 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.54×** | +4.2 | 0.001 | 3/10 (A498, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +3.8 | 0.006 | 12/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2637.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.588×** | -4.6 | 0.002 | 19/43 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.590×** | -4.5 | 0.002 | 19/41 (LoVo, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.649×** | -3.7 | 0.039 | 15/42 (SW1417, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **0.642×** | -3.6 | 0.046 | 7/43 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.668×** | -3.5 | 0.060 | 17/42 (RPMI-7951, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.659×** | -3.4 | 0.069 | 11/42 (HT-29, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.611× | -3.0 | 0.21 | 8/44 (LoVo, RKO, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 26.3 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +29.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0965× (z -15.9) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.266× (z -9.0) |
| [[KATO III (line)]] | alt | 8.40 | 0 | 3 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0454× (z -11.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 3.03 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 69.8× (z +19.7) | — |
| [[C32 (line)]] | wt | 3.60 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 454× (z +14.6) | — |
| [[HS-578T (line)]] | alt | 1.87 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 177× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 14.0 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0850× (z -10.0) ⚠ toxic · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0909× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 9.02 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 55.7× (z +16.5) | — |
| [[NCI-H23 (line)]] | alt | 7.42 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 29.2× (z +19.4) | [[Digitoxin (drug)]] 5 µM 0.108× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 3.68 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 69.2× (z +18.1) | — |
| [[PANC-1 (line)]] | alt | 4.93 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +14.2) | [[Digitoxin (drug)]] 5 µM 0.166× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 1.96 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 71.9× (z +17.2) | — |
| [[A-172 (line)]] | wt | 2.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +10.6) | — |
| [[A549 (line)]] | wt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.6× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 2.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 5.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.1× (z +14.8) | — |
| [[HCT15 (line)]] | alt | 5.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 56.0× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 2.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.0× (z +15.6) | — |
| [[HOP62 (line)]] | alt | 2.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 71.3× (z +16.1) | — |
| [[J82 (line)]] | alt | 1.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 2.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 60.1× (z +14.4) | — |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.185× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 2.94 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 17.7× (z +8.5) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[NCI-H1573 (line)]] | alt | 3.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 65.2× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +15.4) | — |
| [[SNU-423 (line)]] | alt | 2.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.0× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0600× (z -12.9) |
| [[SW48 (line)]] | wt | 3.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.3× (z +10.1) | — |
| [[A-427 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.944 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.901 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA4A]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[CATSPERD]] | +0.66 | +0.77 / +0.57 | both halves | 1e-05 |  |
| [[LINC02580]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[EPHA1-AS1]] | +0.64 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[EFNA2]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[CCNP]] | +0.62 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[GRAMD2A]] | +0.62 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PLB1]] | +0.61 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[MTNR1A]] | +0.61 | +0.69 / +0.49 | both halves | 1e-05 | pathway: G alpha (i) signalling events |
| [[LINC02363]] | +0.61 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[GRIK5]] | +0.61 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[FER1L6]] | +0.61 | +0.67 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTAQ1]] | -0.56 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ADPGK]] | -0.54 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[WHAMMP1]] | -0.53 | -0.63 / -0.38 | both halves | 7e-05 |  |
| [[NUP43]] | -0.52 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[EEF1AKMT2]] | -0.52 | -0.66 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises PDE4C's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NPHS1]] | C | NPHS1 activity strengthens PDE4C's drug response | lines that do not express NPHS1 (4) vs lines expressing it (40) | the lines without NPHS1 respond the other way (z diff +2.88); strongest at Harringtonine 5 µM: 0.19x vs 2.91x (z diff +8.0) | 0.059 | ⚠ few lines (4 vs 46); across organs; co-occurs with CTNNB1; also absent: FSD1L, MYO5A, DPF1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEPTIN9-DT]] | C | PDE4C activity lowers SEPTIN9-DT's level | lines that do not express PDE4C (3) vs lines expressing it (47) | 3.11× higher at baseline in the lines without PDE4C | 0.047 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: ZDHHC1, DBNDD1, CDKL5; maybe low, not absent |
| [[KCNAB1]] | C | PDE4C activity strengthens KCNAB1's drug response | lines that do not express PDE4C (3) vs lines expressing it (44) | the lines without PDE4C respond 0.64× as strongly (z diff +1.70); strongest at Homoharringtonine 0.5 µM: 1.26x vs 6.35x (z diff +4.8) | 0.059 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: ZDHHC1, DBNDD1, CDKL5; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IL2RG]] | C | PDE4C activity lowers IL2RG's level | lines that do not express PDE4C (3) vs lines expressing it (47) | 4.20× higher at baseline in the lines without PDE4C | 0.088 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: ZDHHC1, DBNDD1, CDKL5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.9, -14.3); signed map (21.3, 12.7). **Vector** length 87.5, 17.2% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.8 | +35.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +16.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +5.6 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 4C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,207,965-18,248,200 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DPDE1 |
| Gene groups (HGNC) | Phosphodiesterases |
| Reactome | 6 pathways, smallest: DARPP-32 events; Opioid Signalling; G alpha (s) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08493](https://www.uniprot.org/uniprotkb/Q08493) (3',5'-cyclic-AMP phosphodiesterase 4C):

> Hydrolyzes the second messenger cAMP, which is a key regulator of many important physiological processes.

**Summary**, from NCBI Gene [5143](https://www.ncbi.nlm.nih.gov/gene/5143):

> The protein encoded by this gene belongs to the cyclic nucleotide phosphodiesterase (PDE) family, and PDE4 subfamily. This PDE hydrolyzes the second messenger, cAMP, which is a regulator and mediator of a number of cellular responses to extracellular signals. Thus, by regulating the cellular concentration of cAMP, this protein plays a key role in many important physiological processes. Alternatively spliced transcript variants encoding different isoforms have been described for this …

**Accessions** — [HGNC:8782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8782) · Entrez [5143](https://www.ncbi.nlm.nih.gov/gene/5143) · UniProt [Q08493](https://www.uniprot.org/uniprotkb/Q08493) · Ensembl [ENSG00000105650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105650)

## Data

Gene col 2637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2637); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2637]; `tensor/DDL_lfc|DDL_z.npy` [2637]; `embed/gene_vectors.npy` [2637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2637 or target_col == 2637). Every well: [[PDE4C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE4C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
