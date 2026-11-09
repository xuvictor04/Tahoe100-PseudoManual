---
symbol: "LYPD1"
type: "gene"
col: 7443
ensembl_id: "ENSG00000150551"
name: "LY6/PLAUR domain containing 1"
location: "2q21.2"
module: 9
arm: "+"
pooled_cpm: 3.9
n_lines_expressing: 29
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 7
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# LYPD1

*LY6/PLAUR domain containing 1* — 2q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.80× (z +12.3, q 8e-32, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.69× (z +11.7, q 5e-29, up in 14 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Triamcinolone (drug)]] 0.5 µM: 0.631× (z -3.9, q 0.057, down in 8 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.173×; ⚠ toxic; transcription drop); [[Tofacitinib (citrate) (drug)]] 5 µM in 1 line (SHP-77 0.126×); [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0632×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERTAD4]] (+0.66, fdr 7e-06), [[OFCC1]] (+0.61, fdr 1e-05), [[LINC02605]] (+0.61, fdr 1e-05); moves opposite to [[IMPDH1]] (-0.54, fdr 5e-05), [[WDR5]] (-0.52, fdr 2e-05), [[OXNAD1]] (-0.51, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[BAMBI]] → it (grade B ⚠); 7 go from it, the strongest it → [[DNM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.80×** | +12.3 | 8e-32 | 3/5 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.69×** | +11.7 | 5e-29 | 14/21 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.74×** | +11.0 | 7e-26 | 8/11 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.73×** | +8.4 | 9e-15 | 11/21 (A549, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +7.7 | 1e-12 | 12/22 (CFPAC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +7.6 | 3e-12 | 13/23 (A498, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.82×** | +7.0 | 2e-10 | 4/6 (SNU-423, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.97×** | +5.3 | 9e-06 | 15/22 (A-172, C32, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.88×** | +5.3 | 9e-06 | 2/16 (C32, SNU-423) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.86×** | +5.2 | 1e-05 | 9/24 (J82, SW 900, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +5.1 | 2e-05 | 7/12 (A-172, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +4.3 | 9e-04 | 8/23 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.69×** | +4.1 | 0.002 | 6/21 (SNU-423, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.60×** | +3.9 | 0.004 | 7/24 (SW 900, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +3.9 | 0.004 | 9/24 (SW 900, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.005 | 9/24 (J82, A549, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.026 | 0/17 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +2.9 | 0.085 | 7/22 (SNU-423, SW 900, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +2.9 | 0.085 | 1/11 (CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.50×** | +2.9 | 0.085 | 1/16 (A-172) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7443.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 0.173×; ⚠ toxic; transcription drop); [[Tofacitinib (citrate) (drug)]] 5 µM in 1 line (SHP-77 0.126×); [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0632×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.631×** | -3.9 | 0.057 | 8/23 (Panc 03.27, SNU-423, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 5.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +9.7) | — |
| [[A549 (line)]] | wt | 4.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.44× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 3.68 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0428× (z -8.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -10.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 9.30 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0632× (z -8.7) |
| [[SHP-77 (line)]] | alt | 7.20 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.126× (z -9.9) |
| [[SW 900 (line)]] | alt | 6.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +8.8) | — |
| [[A-172 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.880 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.553 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.620 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.840 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERTAD4]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[OFCC1]] | +0.61 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[LINC02605]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PCDH17]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ADAMTSL1]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[SOX11]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[ALDH1A2]] | +0.58 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[SOCS2]] | +0.58 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[GFRA1]] | +0.58 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ENC1]] | +0.58 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[CLDN1]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[RASEF]] | +0.57 | +0.61 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMPDH1]] | -0.54 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[WDR5]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[OXNAD1]] | -0.51 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[MSTO2P]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BAMBI]] | B | BAMBI activity raises LYPD1's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without BAMBI | 0.070 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |
| [[LINC02932]] | B | LINC02932 activity raises LYPD1's level | lines that do not express LINC02932 (5) vs lines expressing it (45) | 1.94× lower at baseline in the lines without LINC02932 | 0.089 | ⚠ within organs, on part of the lines; also absent: RBFOX1, DNAH6, ESRRB; maybe low, not absent |
| [[PGBD5]] | B | PGBD5 activity raises LYPD1's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without PGBD5 | 0.098 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2 |
| [[SLAMF7]] | C | SLAMF7 activity raises LYPD1's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 2.10× lower at baseline in the lines without SLAMF7 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17; co-absent with the target |
| [[CCN3]] | C | CCN3 activity raises LYPD1's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 2.26× lower at baseline in the lines without CCN3 | 0.035 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033; co-absent with the target |
| [[CA8]] | C | CA8 activity raises LYPD1's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without CA8 | 0.038 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2; co-absent with the target |
| [[PSG4]] | C | PSG4 activity raises LYPD1's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 2.15× lower at baseline in the lines without PSG4 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[LINC00958]] | C | LINC00958 activity raises LYPD1's level | lines that do not express LINC00958 (39) vs lines expressing it (11) | 2.05× lower at baseline in the lines without LINC00958 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SSX1, LINC01320, LINC00879; co-absent with the target |
| [[SLIT2]] | C | SLIT2 activity raises LYPD1's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without SLIT2 | 0.093 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNM3]] | B | LYPD1 activity raises DNM3's level | lines that do not express LYPD1 (21) vs lines expressing it (29) | 1.93× lower at baseline in the lines without LYPD1 | 0.021 | ⚠ within organs, on part of the lines; also absent: SETBP1, FRMPD4, NCKAP5 |
| [[PCED1B]] | B | LYPD1 activity raises PCED1B's level | lines that do not express LYPD1 (21) vs lines expressing it (29) | 2.35× lower at baseline in the lines without LYPD1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SETBP1, FRMPD4, NCKAP5 |
| [[LINC01483]] | B | LYPD1 activity raises LINC01483's level | lines that do not express LYPD1 (21) vs lines expressing it (29) | 1.56× lower at baseline in the lines without LYPD1 | 0.035 | ⚠ within organs, on part of the lines; also absent: SETBP1, FRMPD4, NCKAP5 |
| [[AMIGO2]] | B | LYPD1 activity raises AMIGO2's level | lines that do not express LYPD1 (21) vs lines expressing it (29) | 2.24× lower at baseline in the lines without LYPD1 | 0.038 | ⚠ within organs, on part of the lines; also absent: SETBP1, FRMPD4, NCKAP5 |
| [[PLCL1]] | B | LYPD1 activity raises PLCL1's level | lines that do not express LYPD1 (21) vs lines expressing it (29) | 1.74× lower at baseline in the lines without LYPD1 | 0.092 | ⚠ within organs, on part of the lines; also absent: SETBP1, FRMPD4, NCKAP5 |
| [[COL22A1]] | C | LYPD1 activity raises COL22A1's level | lines that do not express LYPD1 (21) vs lines expressing it (29) | 3.08× lower at baseline in the lines without LYPD1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SETBP1, FRMPD4, NCKAP5; co-absent with the target |
| [[LINC02930]] | C | LYPD1 activity raises LINC02930's level | lines that do not express LYPD1 (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without LYPD1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SETBP1, FRMPD4, NCKAP5; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.6, 28.2); signed map (38.7, 29.2). **Vector** length 43.7, 8.64% of its response variance represented; |z| ≥ 3 in 519 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +12.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.0 | +1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +2.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | LY6/PLAUR domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.2 — chr2:132,643,286-132,671,579 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC29643, PHTS; previously LYPDC1 |
| Gene groups (HGNC) | LY6/PLAUR domain containing |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2G4](https://www.uniprot.org/uniprotkb/Q8N2G4) (Ly6/PLAUR domain-containing protein 1):

> Believed to act as a modulator of nicotinic acetylcholine receptors (nAChRs) activity. In vitro increases receptor desensitization and decreases affinity for ACh of alpha-4:beta-2-containing nAChRs. May play a role in the intracellular trafficking of alpha-4:beta-2 and alpha-7-containing nAChRs and may inhibit their expression at the cell surface. May be involved in the control of anxiety.

**Summary**, from NCBI Gene [116372](https://www.ncbi.nlm.nih.gov/gene/116372):

> Predicted to enable acetylcholine receptor inhibitor activity. Predicted to be involved in acetylcholine receptor signaling pathway. Predicted to act upstream of or within several processes, including behavioral fear response; cholinergic synaptic transmission; and negative regulation of protein localization to plasma membrane. Predicted to be located in extracellular region and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28431](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28431) · Entrez [116372](https://www.ncbi.nlm.nih.gov/gene/116372) · UniProt [Q8N2G4](https://www.uniprot.org/uniprotkb/Q8N2G4) · Ensembl [ENSG00000150551](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150551)

## Data

Gene col 7443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7443); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7443]; `tensor/DDL_lfc|DDL_z.npy` [7443]; `embed/gene_vectors.npy` [7443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7443 or target_col == 7443). Every well: [[LYPD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYPD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
