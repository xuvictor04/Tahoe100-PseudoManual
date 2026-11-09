---
symbol: "PWWP3B"
type: "gene"
col: 8077
ensembl_id: "ENSG00000157502"
name: "PWWP domain containing 3B"
location: "Xq22.3"
module: 27
arm: "+"
pooled_cpm: 2.68
n_lines_expressing: 19
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 6
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# PWWP3B

*PWWP domain containing 3B* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.84× (z +12.4, q 2e-32, up in 12 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.111×, SW1417 0.223×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.0728×; ⚠ toxic; transcription drop); [[Binimetinib (drug)]] 5 µM in 1 line (SW480 0.105×); [[Binimetinib (drug)]] 0.05 µM in 1 line (SW480 0.204×); [[Binimetinib (drug)]] 0.5 µM in 1 line (SW480 0.239×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGFL4]] (+0.64, fdr 1e-05), [[SHISA9]] (+0.59, fdr 7e-06), [[LINC02254]] (+0.58, fdr 1e-05); moves opposite to [[S100PBP]] (-0.51, fdr 4e-05), [[PRDM10]] (-0.42, fdr 1e-04), [[MSL1]] (-0.42, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[GRIK2]] → it (grade B ⚠); 6 go from it, the strongest it → [[S100PBP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8077.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.84×** | +12.4 | 2e-32 | 12/14 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.14×** | +11.4 | 2e-27 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.56×** | +9.1 | 1e-17 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.56×** | +8.3 | 2e-14 | 3/8 (BT-474, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.18×** | +7.2 | 9e-11 | 7/11 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +5.2 | 2e-05 | 9/14 (SW1417, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.17×** | +5.0 | 4e-05 | 7/13 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +4.7 | 2e-04 | 1/7 (SW1417) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +4.6 | 3e-04 | 5/14 (NCI-H460, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +4.5 | 3e-04 | 3/6 (SW1417, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +4.4 | 6e-04 | 5/14 (SW480, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +4.3 | 7e-04 | 5/12 (BT-474, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.06×** | +4.2 | 1e-03 | 4/14 (SW1417, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.86×** | +4.0 | 0.002 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.34×** | +4.0 | 0.003 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.23×** | +3.7 | 0.007 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +3.6 | 0.012 | 5/9 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.69×** | +3.4 | 0.020 | 1/14 (BT-474) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.03×** | +3.3 | 0.028 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.64×** | +3.2 | 0.032 | 0/10 | inconsistent across doses | low cells (technical?) |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.63×** | +3.2 | 0.039 | 3/11 (BT-474, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +2.9 | 0.077 | 1/10 (NCI-H460) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8077.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.111×, SW1417 0.223×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.0728×; ⚠ toxic; transcription drop); [[Binimetinib (drug)]] 5 µM in 1 line (SW480 0.105×); [[Binimetinib (drug)]] 0.05 µM in 1 line (SW480 0.204×); [[Binimetinib (drug)]] 0.5 µM in 1 line (SW480 0.239×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.610× | -3.2 | 0.71 | 3/14 (HOP62, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8077. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 27.3 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 0.105× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 3.14 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.75× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 1.47 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.62× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.833 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.480 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.813 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.683 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.805 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8077), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGFL4]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SHISA9]] | +0.59 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[LINC02254]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[LINC00460]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[FGF19]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[PROX1]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[RIMBP2]] | +0.56 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[LINC01226]] | +0.54 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[LINC02832]] | +0.52 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[VWA2]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[LCK]] | +0.51 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[ST18]] | +0.51 | +0.51 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[S100PBP]] | -0.51 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[PRDM10]] | -0.42 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[MSL1]] | -0.42 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[PRPSAP1]] | -0.41 | -0.12 / -0.49 | ⚠ not reproduced | 0.002 |  |
| [[NDOR1]] | -0.40 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[SLC12A9]] | -0.40 | -0.21 / -0.36 | both halves | 7e-04 |  |
| [[SLC38A9]] | -0.39 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[ANXA2R-OT1]] | -0.39 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[NR2C2]] | -0.39 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[UBE2F-SCLY]] | -0.38 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[PRDM15]] | -0.38 | -0.35 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIK2]] | B | GRIK2 activity raises PWWP3B's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 1.53× lower at baseline in the lines without GRIK2 | 0.073 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B |
| [[PSG1]] | C | PSG1 activity raises PWWP3B's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 2.28× lower at baseline in the lines without PSG1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[VSIG1]] | C | VSIG1 activity raises PWWP3B's level | lines that do not express VSIG1 (33) vs lines expressing it (17) | 1.63× lower at baseline in the lines without VSIG1 | 0.017 | ⚠ within organs, on part of the lines; also absent: KRT7, GSDMC, SLC15A1; co-absent with the target |
| [[STRA6]] | C | STRA6 activity raises PWWP3B's level | lines that do not express STRA6 (26) vs lines expressing it (24) | 1.88× lower at baseline in the lines without STRA6 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000261543, CCDC33, ACKR3; co-absent with the target |
| [[PCSK1]] | C | PCSK1 activity raises PWWP3B's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 2.21× lower at baseline in the lines without PCSK1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[APCDD1]] | C | APCDD1 activity raises PWWP3B's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.53× lower at baseline in the lines without APCDD1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751; co-absent with the target |
| [[TSHZ2]] | C | TSHZ2 activity raises PWWP3B's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 1.77× lower at baseline in the lines without TSHZ2 | 0.055 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; co-absent with the target |
| [[STXBP5L]] | C | STXBP5L activity raises PWWP3B's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 2.04× lower at baseline in the lines without STXBP5L | 0.056 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent; co-absent with the target |
| [[PDLIM4]] | C | PDLIM4 activity raises PWWP3B's level | lines that do not express PDLIM4 (32) vs lines expressing it (18) | 1.44× lower at baseline in the lines without PDLIM4 | 0.064 | ⚠ within organs, on part of the lines; also absent: CARMN, CFI, IRAK3; co-absent with the target |
| [[ANO4]] | C | ANO4 activity raises PWWP3B's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.47× lower at baseline in the lines without ANO4 | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |
| [[TMEM163]] | C | TMEM163 activity raises PWWP3B's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.86× lower at baseline in the lines without TMEM163 | 0.084 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[S100PBP]] | B | PWWP3B activity lowers S100PBP's level | lines that do not express PWWP3B (31) vs lines expressing it (19) | 1.22× higher at baseline in the lines without PWWP3B | 0.031 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, SLC15A5, GTF2I-AS1 |
| [[NKD2]] | B | PWWP3B activity raises NKD2's level | lines that do not express PWWP3B (31) vs lines expressing it (19) | 1.76× lower at baseline in the lines without PWWP3B | 0.062 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, SLC15A5, GTF2I-AS1 |
| [[JAG1]] | B | PWWP3B activity raises JAG1's level | lines that do not express PWWP3B (31) vs lines expressing it (19) | 1.69× lower at baseline in the lines without PWWP3B | 0.085 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, SLC15A5, GTF2I-AS1 |
| [[VSIG1]] | C | PWWP3B activity raises VSIG1's level | lines that do not express PWWP3B (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without PWWP3B | 0.037 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, SLC15A5, GTF2I-AS1; co-absent with the target |
| [[SKAP1]] | C | PWWP3B activity raises SKAP1's level | lines that do not express PWWP3B (31) vs lines expressing it (19) | 1.50× lower at baseline in the lines without PWWP3B | 0.090 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, SLC15A5, GTF2I-AS1; co-absent with the target |
| [[PSG1]] | C | PWWP3B activity lowers PSG1's level | lines that do not express PWWP3B (31) vs lines expressing it (19) | 1.11× higher at baseline in the lines without PWWP3B | 0.097 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, SLC15A5, GTF2I-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.5, 43.2); signed map (64.0, 15.6). **Vector** length 35.5, 8.48% of its response variance represented; |z| ≥ 3 in 362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.6 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +11.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.4 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.7 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.7 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.6 | +0.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.1 | +0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -0.9 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.6 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | PWWP domain containing 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:106,168,305-106,208,956 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33516; previously MUM1L1 |
| Gene groups (HGNC) | PWWP domain containing |
| Matched by | ensembl_id |

UniProt [Q5H9M0](https://www.uniprot.org/uniprotkb/Q5H9M0) carries no function annotation.

**Summary**, from NCBI Gene [139221](https://www.ncbi.nlm.nih.gov/gene/139221):

> This gene encodes a protein which contains a mutated melanoma-associated antigen 1 domain. Proteins which contain mutated antigens are expressed at high levels on certain types of cancers. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:26583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26583) · Entrez [139221](https://www.ncbi.nlm.nih.gov/gene/139221) · UniProt [Q5H9M0](https://www.uniprot.org/uniprotkb/Q5H9M0) · Ensembl [ENSG00000157502](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157502)

## Data

Gene col 8077: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8077); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8077, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8077]; `tensor/DDL_lfc|DDL_z.npy` [8077]; `embed/gene_vectors.npy` [8077]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8077 or target_col == 8077). Every well: [[PWWP3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PWWP3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
