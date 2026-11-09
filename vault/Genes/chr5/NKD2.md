---
symbol: "NKD2"
type: "gene"
col: 7000
ensembl_id: "ENSG00000145506"
name: "NKD inhibitor of Wnt signaling pathway 2"
location: "5p15.33"
module: 162
arm: "+"
pooled_cpm: 9.87
n_lines_expressing: 34
n_dd_up: 16
n_dd_down: 18
n_dd_up_clean: 12
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 9
direction_downstream: 4
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# NKD2

*NKD inhibitor of Wnt signaling pathway 2* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.84× (z +16.1, q 0e+00, up in 18 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.558× (z -6.2, q 4e-07, down in 16 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRARP]] (+0.61, fdr 1e-05), [[SPNS2]] (+0.60, fdr 4e-05), [[IQSEC1]] (+0.59, fdr 1e-05); moves opposite to [[TRAPPC13]] (-0.47, fdr 5e-05), [[NCOA2]] (-0.45, fdr 1e-04), [[ATP6V0D1-DT]] (-0.45, fdr 2e-04).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[IQGAP2]] → it (grade B ⚠); 4 go from it, the strongest it → [[MIR3667HG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.84×** | +16.1 | 0e+00 | 18/27 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.19×** | +12.1 | 4e-31 | 23/31 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.91×** | +11.7 | 4e-29 | 23/31 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.38×** | +9.1 | 1e-17 | 17/29 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.30×** | +9.1 | 1e-17 | 18/31 (HCT15, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.93×** | +7.2 | 8e-11 | 15/31 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.92×** | +7.1 | 1e-10 | 18/31 (HCT15, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +6.2 | 4e-08 | 14/30 (NCI-H2347, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +5.9 | 2e-07 | 14/31 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.60×** | +4.9 | 5e-05 | 2/13 (HOP62, NCI-H2347) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.31×** | +4.8 | 9e-05 | 8/30 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.54×** | +4.7 | 1e-04 | 9/29 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +4.6 | 2e-04 | 12/31 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.7 | 0.008 | 6/31 (A-427, RPMI-7951, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.5 | 0.020 | 6/21 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.037 | 6/27 (NCI-H460, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.051 | 5/26 (C-33 A, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7000.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.558×** | -6.2 | 4e-07 | 16/31 (SW480, COLO 205, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.631×** | -5.5 | 1e-05 | 14/32 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.686×** | -4.2 | 0.006 | 11/31 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.792×** | -3.6 | 0.036 | 10/31 (SW480, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.05 µM |  | **0.706×** | -3.6 | 0.036 | 10/31 (AN3 CA, RPMI-7951, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.739×** | -3.6 | 0.036 | 10/32 (SW480, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.777×** | -3.5 | 0.037 | 7/31 (SW480, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.803×** | -3.4 | 0.038 | 16/28 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.724×** | -3.4 | 0.038 | 13/31 (SW480, COLO 205, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.806×** | -3.4 | 0.040 | 13/31 (RKO, A-427, …) | top dose only | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.741×** | -3.3 | 0.045 | 9/31 (COLO 205, C-33 A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.771×** | -3.3 | 0.045 | 12/31 (SW48, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.745×** | -3.3 | 0.045 | 10/31 (NCI-H661, LoVo, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.727×** | -3.3 | 0.045 | 9/31 (SW480, SW1417, …) | all doses, flat |  |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -3.0 | 0.098 | 5/31 (A-427, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.98 | 11 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +15.4) | — |
| [[SW480 (line)]] | alt | 53.5 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -16.9) |
| [[A549 (line)]] | wt | 9.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0732× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 4.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 8.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 4.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 49.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -12.5) |
| [[SW48 (line)]] | wt | 14.2 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.160× (z -9.5) |
| [[A-172 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.927 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.853 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.649 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRARP]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[SPNS2]] | +0.60 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[IQSEC1]] | +0.59 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[DOT1L]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[DUSP2]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ASTL]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[NSMF]] | +0.57 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[ENTREP2]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[JPH1]] | +0.57 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[CACNA1H]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[LINC02832]] | +0.57 | +0.40 / +0.67 | both halves | 5e-05 |  |
| [[SEMA3F]] | +0.56 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC13]] | -0.47 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[NCOA2]] | -0.45 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[ATP6V0D1-DT]] | -0.45 | -0.31 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IQGAP2]] | B | IQGAP2 activity raises NKD2's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 2.24× lower at baseline in the lines without IQGAP2 | 0.016 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[NKD1]] | B | NKD1 activity raises NKD2's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 2.84× lower at baseline in the lines without NKD1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981 |
| [[PTPRZ1]] | B | PTPRZ1 activity raises NKD2's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 2.10× lower at baseline in the lines without PTPRZ1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029 |
| [[MAP2K1]] | B | MAP2K1 activity raises NKD2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ADAP1]] | B | ADAP1 activity raises NKD2's level | lines that do not express ADAP1 (7) vs lines expressing it (43) | 2.97× lower at baseline in the lines without ADAP1 | 0.062 | ⚠ within organs, on part of the lines; also absent: CCDC88C, ARRDC4, LYN; maybe low, not absent |
| [[PWWP3B]] | B | PWWP3B activity raises NKD2's level | lines that do not express PWWP3B (31) vs lines expressing it (19) | 1.76× lower at baseline in the lines without PWWP3B | 0.062 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, SLC15A5, GTF2I-AS1 |
| [[PALD1]] | C | PALD1 activity raises NKD2's level | lines that do not express PALD1 (16) vs lines expressing it (34) | 3.15× lower at baseline in the lines without PALD1 | 0.010 | ⚠ within organs, on part of the lines; also absent: NKD2, ADRA2C, IGSF9B; co-absent with the target |
| [[ADRA2C]] | C | ADRA2C activity raises NKD2's level | lines that do not express ADRA2C (19) vs lines expressing it (31) | 2.62× lower at baseline in the lines without ADRA2C | 0.020 | ⚠ within organs, on part of the lines; also absent: LRRC4B, CHD5, IGSF9B; co-absent with the target |
| [[ASTL]] | C | ASTL activity raises NKD2's level | lines that do not express ASTL (26) vs lines expressing it (24) | 2.68× lower at baseline in the lines without ASTL | 0.087 | ⚠ within organs, on part of the lines; also absent: DUSP2, HOXA11, FGF20; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR3667HG]] | B | NKD2 activity lowers MIR3667HG's level | lines that do not express NKD2 (16) vs lines expressing it (34) | 1.58× higher at baseline in the lines without NKD2 | 0.019 | ⚠ within organs, on part of the lines; also absent: CHRNA7, ASTL, PALD1 |
| [[DUSP2]] | B | NKD2 activity raises DUSP2's level | lines that do not express NKD2 (16) vs lines expressing it (34) | 1.98× lower at baseline in the lines without NKD2 | 0.049 | ⚠ within organs, on part of the lines; also absent: CHRNA7, ASTL, PALD1 |
| [[GJA3]] | B | NKD2 activity raises GJA3's level | lines that do not express NKD2 (16) vs lines expressing it (34) | 2.11× lower at baseline in the lines without NKD2 | 0.056 | ⚠ within organs, on part of the lines; also absent: CHRNA7, ASTL, PALD1 |
| [[ASTL]] | C | NKD2 activity raises ASTL's level | lines that do not express NKD2 (16) vs lines expressing it (34) | 2.12× lower at baseline in the lines without NKD2 | 0.035 | ⚠ within organs, on part of the lines; also absent: CHRNA7, ASTL, PALD1; co-absent with the target |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.699). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.2, -3.5); signed map (-2.2, 42.0). **Vector** length 71.8, 15.3% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +6.0 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +1.0 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.0 | -1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.8 | -3.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | NKD inhibitor of Wnt signaling pathway 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:1,008,802-1,038,943 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Naked2 |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 4 pathways, smallest: CHD6, CHD7, CHD8, CHD9 subfamily; CHD chromatin remodelers; ATP-dependent chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969F2](https://www.uniprot.org/uniprotkb/Q969F2) (Protein naked cuticle homolog 2):

> Cell autonomous antagonist of the canonical Wnt signaling pathway. May activate a second Wnt signaling pathway that controls planar cell polarity (By similarity). Required for processing of TGFA and for targeting of TGFA to the basolateral membrane of polarized epithelial cells.

**Summary**, from NCBI Gene [85409](https://www.ncbi.nlm.nih.gov/gene/85409):

> This gene encodes a member of a family of proteins that function as negative regulators of Wnt receptor signaling through interaction with Dishevelled family members. The encoded protein participates in the delivery of transforming growth factor alpha-containing vesicles to the cell membrane. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:17046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17046) · Entrez [85409](https://www.ncbi.nlm.nih.gov/gene/85409) · UniProt [Q969F2](https://www.uniprot.org/uniprotkb/Q969F2) · Ensembl [ENSG00000145506](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145506)

## Data

Gene col 7000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7000); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7000]; `tensor/DDL_lfc|DDL_z.npy` [7000]; `embed/gene_vectors.npy` [7000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7000 or target_col == 7000). Every well: [[NKD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NKD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
