---
symbol: "FAAH"
type: "gene"
col: 3915
ensembl_id: "ENSG00000117480"
name: "fatty acid amide hydrolase"
location: "1p33"
module: 55
arm: "+"
pooled_cpm: 3.07
n_lines_expressing: 41
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# FAAH

*fatty acid amide hydrolase* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.12× (z +10.9, q 6e-25, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.81× (z +5.9, q 4e-07, up in 13 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.129×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPG2IT1]] (+0.56, fdr 2e-05), [[TSPOAP1]] (+0.55, fdr 5e-05), [[SLC25A25-AS1]] (+0.55, fdr 3e-05); moves opposite to [[DDT]] (-0.47, fdr 4e-05), [[CDKL5]] (-0.47, fdr 2e-04), [[COX5B]] (-0.46, fdr 1e-04).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[LINC02331]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MROH7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3915.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.12×** | +10.9 | 6e-25 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +8.9 | 2e-16 | 9/14 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +7.3 | 6e-11 | 5/8 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +5.9 | 4e-07 | 13/32 (HT-29, A-427, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.08×** | +3.8 | 0.015 | 3/29 (A498, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Valdecoxib (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.033 | 5/29 (HEC-1-A, HCT15, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.045 | 1/20 (BT-474) | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.049 | 3/19 (RKO, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.25× | +3.1 | 0.10 | 11/35 (A498, CFPAC-1, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.53× | +3.0 | 0.14 | 2/14 (KATO III, COLO 205) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3915.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.129×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.708× | -3.5 | 0.31 | 12/36 (SW480, PANC-1, …) | top dose only | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.803× | -3.1 | 0.52 | 8/35 (HT-29, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3915. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 5.65 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.959 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.610 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.681 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.899 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3915), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPG2IT1]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[TSPOAP1]] | +0.55 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[SLC25A25-AS1]] | +0.55 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[CHDH]] | +0.51 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[NPR2]] | +0.50 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[MROH6]] | +0.50 | +0.49 / +0.47 | both halves | 2e-05 | STRING 554 |
| [[GALNT8]] | +0.49 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[XK]] | +0.49 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[BCAR3-AS1]] | +0.48 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[SCARF2]] | +0.48 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[KCNE3]] | +0.48 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[SRSF1]] | +0.48 | +0.45 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDT]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[CDKL5]] | -0.47 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[COX5B]] | -0.46 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[GAB1]] | -0.46 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[OST4]] | -0.46 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[FGFR1OP2]] | -0.45 | -0.45 / -0.25 | both halves | 4e-04 |  |
| [[PSENEN]] | -0.44 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[MEA1]] | -0.44 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[MLLT3]] | -0.43 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[WDR44]] | -0.43 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[VKORC1]] | -0.42 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[GINM1]] | -0.42 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02331]] | B | LINC02331 activity raises FAAH's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 2.31× lower at baseline in the lines without LINC02331 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2 |
| [[ST6GALNAC1]] | B | ST6GALNAC1 activity raises FAAH's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 1.66× lower at baseline in the lines without ST6GALNAC1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[MROH7]] | B | MROH7 activity raises FAAH's level | lines that do not express MROH7 (15) vs lines expressing it (35) | 1.42× lower at baseline in the lines without MROH7 | 0.030 | ⚠ within organs, on part of the lines; also absent: ACOT11, PLEKHG1, FCGRT; maybe low, not absent |
| [[TSPOAP1]] | B | TSPOAP1 activity raises FAAH's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 1.50× lower at baseline in the lines without TSPOAP1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[CHDH]] | B | CHDH activity raises FAAH's level | lines that do not express CHDH (22) vs lines expressing it (28) | 1.80× lower at baseline in the lines without CHDH | 0.036 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22 |
| [[TMEM139]] | B | TMEM139 activity raises FAAH's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 2.09× lower at baseline in the lines without TMEM139 | 0.036 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A |
| [[MUC5B]] | B | MUC5B activity raises FAAH's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 1.53× lower at baseline in the lines without MUC5B | 0.064 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[VIL1]] | B | VIL1 activity raises FAAH's level | lines that do not express VIL1 (34) vs lines expressing it (16) | 1.99× lower at baseline in the lines without VIL1 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| [[TMEM184A]] | B | TMEM184A activity raises FAAH's level | lines that do not express TMEM184A (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without TMEM184A | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, ENSG00000284716, GPRC5C; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MROH7]] | B | FAAH activity raises MROH7's level | lines that do not express FAAH (9) vs lines expressing it (41) | 1.90× lower at baseline in the lines without FAAH | 0.087 | ⚠ within organs, on part of the lines; also absent: CPLX1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.432). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.2, 46.7); signed map (67.7, -0.4). **Vector** length 37.5, 4.25% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +8.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.2 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -1.2 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -1.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | fatty acid amide hydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p33 — chr1:46,394,317-46,413,848 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAAH-1, FAAH1 |
| Gene groups (HGNC) | N-arachidonoylethanolamine hydrolases |
| Reactome | 3 pathways, smallest: Arachidonate metabolism; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [O00519](https://www.uniprot.org/uniprotkb/O00519) (Fatty-acid amide hydrolase 1):

> Catalyzes the hydrolysis of endogenous amidated lipids like the sleep-inducing lipid oleamide ((9Z)-octadecenamide), the endocannabinoid anandamide (N-(5Z,8Z,11Z,14Z-eicosatetraenoyl)-ethanolamine), as well as other fatty amides, to their corresponding fatty acids, thereby regulating the signaling functions of these molecules. Hydrolyzes polyunsaturated substrate anandamide preferentially as compared to monounsaturated substrates. It can also catalyze the hydrolysis of the endocannabinoid …

**Summary**, from NCBI Gene [2166](https://www.ncbi.nlm.nih.gov/gene/2166):

> This gene encodes a protein that is responsible for the hydrolysis of a number of primary and secondary fatty acid amides, including the neuromodulatory compounds anandamide and oleamide. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3553](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3553) · Entrez [2166](https://www.ncbi.nlm.nih.gov/gene/2166) · UniProt [O00519](https://www.uniprot.org/uniprotkb/O00519) · Ensembl [ENSG00000117480](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117480)

## Data

Gene col 3915: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3915); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3915, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3915]; `tensor/DDL_lfc|DDL_z.npy` [3915]; `embed/gene_vectors.npy` [3915]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3915 or target_col == 3915). Every well: [[FAAH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAAH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
