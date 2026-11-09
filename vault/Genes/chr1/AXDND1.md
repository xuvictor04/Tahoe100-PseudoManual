---
symbol: "AXDND1"
type: "gene"
col: 8579
ensembl_id: "ENSG00000162779"
name: "axonemal dynein light chain domain containing 1"
location: "1q25.2"
module: 53
arm: "+"
pooled_cpm: 4.27
n_lines_expressing: 46
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# AXDND1

*axonemal dynein light chain domain containing 1* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.72× (z +22.9, q 0e+00, up in 29 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.122×; ⚠ toxic; transcription drop); [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0863×; ⚠ transcription drop; unreliable plate only); [[Silodosin (drug)]] 5 µM in 1 line (SW480 0.0845×); [[Bendamustine (drug)]] 5 µM in 1 line (HEC-1-A 0.0994×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP50]] (+0.83, fdr 7e-06), [[DPYS]] (+0.83, fdr 7e-06), [[GARIN1B]] (+0.82, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[AOX1]] → it (grade B ⚠); 6 go from it, the strongest it → [[KPNA7]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8579.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.72×** | +22.9 | 0e+00 | 29/31 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.91×** | +15.8 | 0e+00 | 23/31 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.43×** | +12.9 | 1e-35 | 38/42 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.32×** | +12.0 | 3e-31 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.85×** | +10.1 | 6e-22 | 4/7 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.62×** | +10.0 | 1e-21 | 9/14 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +9.5 | 2e-19 | 29/40 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +8.2 | 1e-14 | 15/28 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +8.0 | 8e-14 | 17/34 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.15×** | +8.0 | 8e-14 | 22/37 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.72×** | +8.0 | 9e-14 | 17/40 (SK-MEL-2, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +7.4 | 7e-12 | 13/29 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.01×** | +7.3 | 1e-11 | 20/37 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +7.0 | 1e-10 | 19/40 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.1 | 5e-08 | 13/41 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +5.2 | 7e-06 | 10/42 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +4.2 | 7e-04 | 11/38 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.004 | 9/37 (A-172, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8579.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.122×; ⚠ toxic; transcription drop); [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0863×; ⚠ transcription drop; unreliable plate only); [[Silodosin (drug)]] 5 µM in 1 line (SW480 0.0845×); [[Bendamustine (drug)]] 5 µM in 1 line (HEC-1-A 0.0994×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.532× | -3.5 | 0.11 | 7/24 (HOP62, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.721× | -3.4 | 0.11 | 10/37 (J82, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 0.722× | -3.4 | 0.11 | 5/33 (hTERT-HPNE, A498, …) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.737× | -3.2 | 0.18 | 5/42 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Delamanid (drug)]] 5 µM |  | 0.747× | -3.1 | 0.23 | 3/42 (C32, SW 900, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM |  | 0.818× | -3.0 | 0.25 | 3/41 (SW1417, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 40.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -13.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 5.29 | 0 | 2 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0863× (z -9.6) ⚠ transcription drop; unreliable plate only · without an alert: [[Bendamustine (drug)]] 5 µM 0.0994× (z -8.7) |
| [[SW480 (line)]] | alt | 2.18 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.09× (z +8.7) | [[Silodosin (drug)]] 5 µM 0.0845× (z -8.9) |
| [[A-172 (line)]] | wt | 3.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +10.3) | — |
| [[A498 (line)]] | wt | 2.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.62× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 1.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.11× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 2.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +9.0) | — |
| [[A-427 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.940 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP50]] | +0.83 | +0.84 / +0.75 | both halves | 7e-06 |  |
| [[DPYS]] | +0.83 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.82 | +0.81 / +0.69 | both halves | 7e-06 |  |
| [[CATSPERD]] | +0.81 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[LINC00393]] | +0.78 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[KIF17]] | +0.76 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[OIT3]] | +0.76 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[XG]] | +0.76 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[IMPA1P1]] | +0.76 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[L3MBTL2-AS1]] | +0.76 | +0.77 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AOX1]] | B | AOX1 activity raises AXDND1's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without AOX1 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[EPHA1-AS1]] | B | EPHA1-AS1 activity lowers AXDND1's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 2.22× higher at baseline in the lines without EPHA1-AS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers AXDND1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01348]] | B | LINC01348 activity weakens AXDND1's drug response | lines that do not express LINC01348 (9) vs lines expressing it (33) | the lines without LINC01348 respond 1.05× as strongly (z diff -0.25); strongest at Homoharringtonine 5 µM: 3.73x vs 2.46x (z diff -2.2) | 0.033 | ⚠ within organs, on part of the lines; also absent: ARHGAP42, RIPK4, ABCC3; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[LINC01348]] | B | LINC01348 activity lowers AXDND1's level | lines that do not express LINC01348 (10) vs lines expressing it (40) | 1.99× higher at baseline in the lines without LINC01348 | 0.038 | ⚠ within organs, on part of the lines; also absent: ARHGAP42, RIPK4, ABCC3; maybe low, not absent |
| [[CALCRL]] | B | CALCRL activity raises AXDND1's level | lines that do not express CALCRL (18) vs lines expressing it (32) | 1.55× lower at baseline in the lines without CALCRL | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000259363, NRG1, SPOCK3 |
| [[FBXW10B]] | B | FBXW10B activity lowers AXDND1's level | lines that do not express FBXW10B (11) vs lines expressing it (39) | 1.64× higher at baseline in the lines without FBXW10B | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KPNA7]] | C | AXDND1 activity lowers KPNA7's level | lines that do not express AXDND1 (4) vs lines expressing it (46) | 3.21× higher at baseline in the lines without AXDND1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TMCC2, HACE1, P3H4; maybe low, not absent; its own permutation p |
| [[SPON2]] | C | AXDND1 activity lowers SPON2's level | lines that do not express AXDND1 (4) vs lines expressing it (46) | 2.61× higher at baseline in the lines without AXDND1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TMCC2, HACE1, P3H4; maybe low, not absent; its own permutation p |
| [[LINC01030]] | C | AXDND1 activity raises LINC01030's level | lines that do not express AXDND1 (4) vs lines expressing it (46) | 2.00× lower at baseline in the lines without AXDND1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TMCC2, HACE1, P3H4; maybe low, not absent; co-absent with the target |
| [[SMG1-DT]] | C | AXDND1 activity lowers SMG1-DT's level | lines that do not express AXDND1 (4) vs lines expressing it (46) | 1.81× higher at baseline in the lines without AXDND1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TMCC2, HACE1, P3H4; maybe low, not absent; its own permutation p |
| [[PTCH2]] | C | AXDND1 activity raises PTCH2's level | lines that do not express AXDND1 (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without AXDND1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TMCC2, HACE1, P3H4; maybe low, not absent; its own permutation p |
| [[LINC00486]] | C | AXDND1 activity raises LINC00486's level | lines that do not express AXDND1 (4) vs lines expressing it (46) | 1.39× lower at baseline in the lines without AXDND1 | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TMCC2, HACE1, P3H4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.838). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.5, -13.3); signed map (19.6, 10.0). **Vector** length 50.1, 6.29% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +22.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +15.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +7.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +0.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.4 | -2.1 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | axonemal dynein light chain domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.2 — chr1:179,365,720-179,554,735 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32940; previously C1orf125 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T1B0](https://www.uniprot.org/uniprotkb/Q5T1B0) (Axonemal dynein light chain domain-containing protein 1):

> May be essential for spermiogenesis and male fertility probably by regulating the manchette dynamics, spermatid head shaping and sperm flagellum assembly.

**Summary**, from NCBI Gene [126859](https://www.ncbi.nlm.nih.gov/gene/126859):

> Predicted to be involved in manchette assembly. Predicted to act upstream of or within several processes, including axoneme assembly; male gonad development; and spermatogonial cell division. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26564](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26564) · Entrez [126859](https://www.ncbi.nlm.nih.gov/gene/126859) · UniProt [Q5T1B0](https://www.uniprot.org/uniprotkb/Q5T1B0) · Ensembl [ENSG00000162779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162779)

## Data

Gene col 8579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8579); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8579]; `tensor/DDL_lfc|DDL_z.npy` [8579]; `embed/gene_vectors.npy` [8579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8579 or target_col == 8579). Every well: [[AXDND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AXDND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
