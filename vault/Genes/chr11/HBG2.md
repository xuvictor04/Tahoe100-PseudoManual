---
symbol: "HBG2"
type: "gene"
col: 12238
ensembl_id: "ENSG00000196565"
name: "hemoglobin subunit gamma 2"
location: "11p15.4"
module: 9
arm: "+"
pooled_cpm: 2.18
n_lines_expressing: 33
n_dd_up: 31
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# HBG2

*hemoglobin subunit gamma 2* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.05× (z +13.8, q 1e-40, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 4.56× (z +13.5, q 7e-39, up in 17 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.506× (z -6.0, q 9e-07, down in 12 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 0.185×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OR51B5]] (+0.88, fdr 7e-06, ⚠ read-through risk), [[LINC02220]] (+0.62, fdr 3e-05), [[LINC02241]] (+0.62, fdr 1e-05), [[CEACAM22P-1]] (+0.61, fdr 3e-05); moves opposite to [[SIRT3]] (-0.48, fdr 2e-04), [[DZANK1]] (-0.46, fdr 6e-04), [[AP4M1]] (-0.44, fdr 4e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC01885]] → it (grade B ⚠); 4 go from it, the strongest it → [[LINC02932]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.05×** | +13.8 | 1e-40 | 1/5 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.56×** | +13.5 | 7e-39 | 17/20 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.85×** | +12.0 | 1e-30 | 4/6 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.18×** | +9.8 | 1e-20 | 17/27 (SW480, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.29×** | +9.8 | 2e-20 | 1/5 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +7.1 | 1e-10 | 1/17 (A498) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.03×** | +6.3 | 3e-08 | 6/17 (SW480, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +5.8 | 4e-07 | 7/22 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +4.9 | 6e-05 | 4/26 (SW480, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +4.7 | 1e-04 | 6/13 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.7 | 2e-04 | 8/19 (A-172, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.4 | 6e-04 | 2/9 (SW480, H4) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.50×** | +4.3 | 9e-04 | 0/3 | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +4.2 | 0.001 | 9/26 (A-172, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.60×** | +4.2 | 0.001 | 1/13 (LoVo) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.009 | 7/20 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.017 | 1/18 (A498) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.024 | 2/13 (SW1417, NCI-H1573) | inconsistent across doses | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.039 | 2/28 (NCI-H1792, A498) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.039 | 11/27 (A-172, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.043 | 2/16 (RPMI-7951, A498) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12238.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-172 0.185×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.506×** | -6.0 | 9e-07 | 12/28 (LoVo, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.621×** | -4.2 | 0.007 | 7/29 (C-33 A, HCT15, …) | top dose only |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.706× | -3.1 | 0.28 | 4/26 (LS 180, BT-474, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.785× | -3.0 | 0.28 | 8/25 (hTERT-HPNE, KATO III, …) | top dose only | position effect removed |
| [[Norepinephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.711× | -3.0 | 0.28 | 2/25 (LoVo, RPMI-7951) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 19.8 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.82× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.604 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.607 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.909 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.751 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.943 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.999 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.610 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.812 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.615 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.774 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.975 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.401 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.232 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.320 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OR51B5]] | +0.88 | +0.82 / +0.83 | both halves | 7e-06 | STRING 579; ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of OR51B5 on the same strand (can correlate by spillover, not regulation) |
| [[LINC02220]] | +0.62 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[LINC02241]] | +0.62 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[CEACAM22P-1]] | +0.61 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[LINC01320]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[LINC02360]] | +0.54 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[COLEC10]] | +0.54 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[LINC02977]] | +0.54 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[CXCL13]] | +0.53 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[LINC01885]] | +0.53 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[LINC01208]] | +0.52 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[TMEM178A]] | +0.52 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[FSTL5]] | +0.52 | +0.42 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT3]] | -0.48 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[DZANK1]] | -0.46 | -0.22 / -0.37 | both halves | 6e-04 |  |
| [[AP4M1]] | -0.44 | -0.26 / -0.56 | both halves | 4e-04 |  |
| [[TERF1]] | -0.43 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[MARCHF8]] | -0.43 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[HAUS5]] | -0.42 | -0.17 / -0.43 | ⚠ not reproduced | 0.001 |  |
| [[ASH2L]] | -0.41 | -0.16 / -0.56 | ⚠ one half (not replicated) | 0.001 |  |
| [[BUD13]] | -0.41 | -0.42 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01885]] | B | LINC01885 activity raises HBG2's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 2.20× lower at baseline in the lines without LINC01885 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383 |
| [[TOP2A]] | B | TOP2A activity lowers HBG2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SNTG2]] | B | SNTG2 activity raises HBG2's level | lines that do not express SNTG2 (18) vs lines expressing it (32) | 1.65× lower at baseline in the lines without SNTG2 | 0.098 | ⚠ within organs, on part of the lines; also absent: TENM4, CRMP1, ENSG00000240086; maybe low, not absent |
| [[LINC02241]] | C | LINC02241 activity raises HBG2's level | lines that do not express LINC02241 (34) vs lines expressing it (16) | 2.69× lower at baseline in the lines without LINC02241 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000259560, LINC02616, LINC02476; maybe low, not absent; co-absent with the target |
| [[OR51B5]] | C | OR51B5 activity raises HBG2's level | lines that do not express OR51B5 (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without OR51B5 | 0.005 | ⚠ within organs, on part of the lines; also absent: HBG2, ENSG00000287231, EPS8L1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02932]] | B | HBG2 activity raises LINC02932's level | lines that do not express HBG2 (17) vs lines expressing it (33) | 1.77× lower at baseline in the lines without HBG2 | 0.035 | ⚠ within organs, on part of the lines; also absent: OR51B5, MKRN3, ENSG00000234147; maybe low, not absent |
| [[LINC01320]] | B | HBG2 activity raises LINC01320's level | lines that do not express HBG2 (17) vs lines expressing it (33) | 2.14× lower at baseline in the lines without HBG2 | 0.095 | ⚠ within organs, on part of the lines; also absent: OR51B5, MKRN3, ENSG00000234147; maybe low, not absent |
| [[TMC3-AS1]] | B | HBG2 activity raises TMC3-AS1's level | lines that do not express HBG2 (17) vs lines expressing it (33) | 1.76× lower at baseline in the lines without HBG2 | 0.097 | ⚠ within organs, on part of the lines; also absent: OR51B5, MKRN3, ENSG00000234147; maybe low, not absent |
| [[OR51B5]] | C | HBG2 activity raises OR51B5's level | lines that do not express HBG2 (17) vs lines expressing it (33) | 4.63× lower at baseline in the lines without HBG2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: OR51B5, MKRN3, ENSG00000234147; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.407). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.0, 27.6); signed map (37.1, 26.6). **Vector** length 30.2, 3.89% of its response variance represented; |z| ≥ 3 in 690 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.8 | +13.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +9.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.7 | +0.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.7 | +1.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -1.2 | +3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +1.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -0.7 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -0.6 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.7 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -2.0 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | -0.6 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | hemoglobin subunit gamma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:5,253,188-5,505,605 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HBG-T1 |
| Gene groups (HGNC) | Hemoglobin subunits |
| Reactome | 2 pathways, smallest: Factors involved in megakaryocyte development and platelet production; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P69892](https://www.uniprot.org/uniprotkb/P69892) (Hemoglobin subunit gamma-2):

> Gamma chains make up the fetal hemoglobin F, in combination with alpha chains.

**Summary**, from NCBI Gene [3048](https://www.ncbi.nlm.nih.gov/gene/3048):

> The gamma globin genes (HBG1 and HBG2) are normally expressed in the fetal liver, spleen and bone marrow. Two gamma chains together with two alpha chains constitute fetal hemoglobin (HbF) which is normally replaced by adult hemoglobin (HbA) at birth. In some beta-thalassemias and related conditions, gamma chain production continues into adulthood. The two types of gamma chains differ at residue 136 where glycine is found in the G-gamma product (HBG2) and alanine is found in the A-gamma product …

**Accessions** — [HGNC:4832](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4832) · Entrez [3048](https://www.ncbi.nlm.nih.gov/gene/3048) · UniProt [P69892](https://www.uniprot.org/uniprotkb/P69892) · Ensembl [ENSG00000196565](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196565)

## Data

Gene col 12238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12238); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12238]; `tensor/DDL_lfc|DDL_z.npy` [12238]; `embed/gene_vectors.npy` [12238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12238 or target_col == 12238). Every well: [[HBG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HBG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
