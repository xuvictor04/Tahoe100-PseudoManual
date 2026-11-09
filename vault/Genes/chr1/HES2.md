---
symbol: "HES2"
type: "gene"
col: 926
ensembl_id: "ENSG00000069812"
name: "hes family bHLH transcription factor 2"
location: "1p36.31"
module: 115
arm: "+"
pooled_cpm: 2.41
n_lines_expressing: 30
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 17
direction_downstream: 17
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# HES2

*hes family bHLH transcription factor 2* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.51× (z +13.7, q 6e-40, up in 20 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.458× (z -6.1, q 6e-07, down in 16 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 2 lines (LoVo 0.0797×, A-427 0.118×; ⚠ cell-cycle shift, explains ~54% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.179×, PANC-1 0.171×; ⚠ cell-cycle shift, explains ~26% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.134×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KANK3]] (+0.71, fdr 7e-06), [[CCDC69]] (+0.63, fdr 3e-05), [[SBK1]] (+0.62, fdr 1e-05); moves opposite to [[METTL15]] (-0.43, fdr 1e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[GBX1]] → it (grade B ⚠); 17 go from it, the strongest it → [[MMP15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 926.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.51×** | +13.7 | 6e-40 | 20/23 (LS 180, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.44×** | +11.1 | 5e-26 | 2/3 (PANC-1, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +8.2 | 7e-14 | 2/9 (SW480, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +7.6 | 5e-12 | 5/20 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.56×** | +7.2 | 5e-11 | 19/22 (LS 180, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +6.9 | 4e-10 | 2/6 (SW480, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.07×** | +5.6 | 2e-06 | 8/24 (KATO III, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.4 | 7e-04 | 5/11 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +4.2 | 0.002 | 9/24 (HOP62, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +4.1 | 0.002 | 10/23 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.12×** | +4.1 | 0.002 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.1 | 0.002 | 1/15 (NCI-H2347) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.69×** | +4.0 | 0.003 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.42×** | +3.8 | 0.007 | 7/24 (A-427, LoVo, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.010 | 6/23 (A549, NCI-H460, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.036 | 3/15 (LoVo, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +3.1 | 0.057 | 3/9 (A-427, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.057 | 5/23 (KATO III, HCT15, …) | rises with dose | cell-cycle shift (explains ~19% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 926.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 2 lines (LoVo 0.0797×, A-427 0.118×; ⚠ cell-cycle shift, explains ~54% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (LoVo 0.179×, PANC-1 0.171×; ⚠ cell-cycle shift, explains ~26% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.134×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.458×** | -6.1 | 6e-07 | 16/22 (BT-474, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.553×** | -4.6 | 0.001 | 11/24 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.591×** | -4.1 | 0.007 | 16/24 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.650× | -3.4 | 0.10 | 13/17 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.679× | -3.0 | 0.27 | 9/20 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 926. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 9.89 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0797× (z -12.7) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -10.5) |
| [[A-427 (line)]] | wt | 9.39 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -8.9) ⚠ cell-cycle shift, explains ~54% of this change |
| [[PANC-1 (line)]] | alt | 6.65 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.225 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.760 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.685 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.369 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.656 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.791 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.250 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.218 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.695 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 926), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANK3]] | +0.71 | +0.58 / +0.78 | both halves | 7e-06 |  |
| [[CCDC69]] | +0.63 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[SBK1]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ADAMTS7]] | +0.60 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[CDH23]] | +0.57 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[BMP8B]] | +0.56 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[GRIP2]] | +0.56 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[LGI4]] | +0.56 | +0.37 / +0.66 | both halves | 8e-05 |  |
| [[METTL27]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[MLXIPL]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 | same gene group |
| [[GPR153]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ACOXL]] | +0.54 | +0.60 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL15]] | -0.43 | -0.35 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 10, C 7. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBX1]] | B | GBX1 activity raises HES2's level | lines that do not express GBX1 (17) vs lines expressing it (33) | 1.64× lower at baseline in the lines without GBX1 | 0.013 | ⚠ within organs, on part of the lines; also absent: OLFML2A, FMNL1-DT, SCN5A; maybe low, not absent |
| [[ANKRD20A11P]] | B | ANKRD20A11P activity raises HES2's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.54× lower at baseline in the lines without ANKRD20A11P | 0.019 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P |
| [[ST6GALNAC2]] | B | ST6GALNAC2 activity raises HES2's level | lines that do not express ST6GALNAC2 (8) vs lines expressing it (42) | 1.80× lower at baseline in the lines without ST6GALNAC2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CELSR1, CTSD, TRIM47; maybe low, not absent |
| [[CACNG4]] | B | CACNG4 activity raises HES2's level | lines that do not express CACNG4 (21) vs lines expressing it (29) | 1.64× lower at baseline in the lines without CACNG4 | 0.033 | ⚠ within organs, on part of the lines; also absent: FRMPD3, PALM, PCSK1N |
| [[JAG2]] | B | JAG2 activity raises HES2's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without JAG2 | 0.060 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[C12orf56]] | B | C12orf56 activity raises HES2's level | lines that do not express C12orf56 (11) vs lines expressing it (39) | 1.51× lower at baseline in the lines without C12orf56 | 0.067 | ⚠ within organs, on part of the lines; also absent: DOC2A, GPR63, STC2; maybe low, not absent |
| [[MMP15]] | B | MMP15 activity raises HES2's level | lines that do not express MMP15 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without MMP15 | 0.072 | ⚠ within organs, on part of the lines; also absent: RTN4R, NOXA1, PTPN3; maybe low, not absent |
| [[PDZD4]] | B | PDZD4 activity raises HES2's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without PDZD4 | 0.083 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[RET]] | B | RET activity raises HES2's level | lines that do not express RET (28) vs lines expressing it (22) | 1.26× lower at baseline in the lines without RET | 0.091 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[ACOXL]] | B | ACOXL activity raises HES2's level | lines that do not express ACOXL (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without ACOXL | 0.0995 | ⚠ within organs, on part of the lines; also absent: ILDR1, PRKCH-AS1, LRRN1; maybe low, not absent |
| [[FBXO2]] | C | FBXO2 activity raises HES2's level | lines that do not express FBXO2 (23) vs lines expressing it (27) | 2.09× lower at baseline in the lines without FBXO2 | 0.005 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, LAMP3; co-absent with the target |
| [[B3GNT7]] | C | B3GNT7 activity raises HES2's level | lines that do not express B3GNT7 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without B3GNT7 | 0.009 | ⚠ within organs, on part of the lines; also absent: KRT23, PROM1, HSD17B2; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 11, C 6. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP15]] | B | HES2 activity raises MMP15's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.75× lower at baseline in the lines without HES2 | 0.008 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[ST6GALNAC2]] | B | HES2 activity raises ST6GALNAC2's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.59× lower at baseline in the lines without HES2 | 0.021 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[PACSIN3]] | B | HES2 activity raises PACSIN3's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without HES2 | 0.024 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[METTL27]] | B | HES2 activity raises METTL27's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.41× lower at baseline in the lines without HES2 | 0.048 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[TMC6]] | B | HES2 activity raises TMC6's level | lines that do not express HES2 (20) vs lines expressing it (30) | 2.03× lower at baseline in the lines without HES2 | 0.051 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[SLC26A5]] | B | HES2 activity raises SLC26A5's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.15× lower at baseline in the lines without HES2 | 0.061 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[BMP8B]] | B | HES2 activity raises BMP8B's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.55× lower at baseline in the lines without HES2 | 0.076 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[LYPD5]] | B | HES2 activity raises LYPD5's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.67× lower at baseline in the lines without HES2 | 0.076 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[ABLIM2]] | B | HES2 activity raises ABLIM2's level | lines that do not express HES2 (20) vs lines expressing it (30) | 2.22× lower at baseline in the lines without HES2 | 0.088 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[PDZD4]] | B | HES2 activity raises PDZD4's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.94× lower at baseline in the lines without HES2 | 0.093 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[NUDT7]] | B | HES2 activity raises NUDT7's level | lines that do not express HES2 (20) vs lines expressing it (30) | 1.32× lower at baseline in the lines without HES2 | 0.098 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[FBXO2]] | C | HES2 activity raises FBXO2's level | lines that do not express HES2 (20) vs lines expressing it (30) | 2.61× lower at baseline in the lines without HES2 | 0.002 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.612). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.7, 41.4); signed map (22.8, 22.1). **Vector** length 47.8, 10.0% of its response variance represented; |z| ≥ 3 in 583 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +1.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +1.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -2.5 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -6.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -4.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.4 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | hes family bHLH transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:6,412,418-6,424,670 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bHLHb40 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y543](https://www.uniprot.org/uniprotkb/Q9Y543) (Transcription factor HES-2):

> Transcriptional repressor of genes that require a bHLH protein for their transcription.

**Summary**, from NCBI Gene [54626](https://www.ncbi.nlm.nih.gov/gene/54626):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in anterior/posterior pattern specification; negative regulation of transcription by RNA polymerase II; and regulation of neurogenesis. Predicted to be located in chromatin. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16005) · Entrez [54626](https://www.ncbi.nlm.nih.gov/gene/54626) · UniProt [Q9Y543](https://www.uniprot.org/uniprotkb/Q9Y543) · Ensembl [ENSG00000069812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069812)

## Data

Gene col 926: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 926); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 926, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 926]; `tensor/DDL_lfc|DDL_z.npy` [926]; `embed/gene_vectors.npy` [926]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 926 or target_col == 926). Every well: [[HES2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HES2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
