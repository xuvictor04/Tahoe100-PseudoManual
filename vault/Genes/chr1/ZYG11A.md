---
symbol: "ZYG11A"
type: "gene"
col: 12806
ensembl_id: "ENSG00000203995"
name: "zyg-11 family member A, cell cycle regulator"
location: "1p32.3"
module: 77
arm: "+"
pooled_cpm: 9.1
n_lines_expressing: 21
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# ZYG11A

*zyg-11 family member A, cell cycle regulator* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.90× (z +20.5, q 0e+00, up in 13 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (A498 0.119×, A-427 0.173×, NCI-H460 0.152×, NCI-H2347 0.214×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1792 0.0803×, A498 0.154×, HOP62 0.251×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 0.200×, NCI-H460 0.307×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.302×); [[Auranofin (drug)]] 5 µM in 1 line (HEC-1-A 0.194×); [[Roxadustat (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0786×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF26]] (+0.64, fdr 1e-05), [[GPR63]] (+0.60, fdr 1e-05), [[EEF2K]] (+0.57, fdr 1e-05); moves opposite to [[CHMP1B]] (-0.58, fdr 5e-05), [[LINC00174]] (-0.55, fdr 8e-05), [[TSPAN31]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DMBX1]] → it (grade B ⚠); 3 go from it, the strongest it → [[C11orf58]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12806.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.90×** | +20.5 | 0e+00 | 13/19 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +9.6 | 2e-19 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.89×** | +8.6 | 1e-15 | 15/19 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +8.1 | 6e-14 | 10/19 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +7.1 | 1e-10 | 3/18 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +7.1 | 1e-10 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.65×** | +6.8 | 7e-10 | 15/19 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.61×** | +6.5 | 7e-09 | 12/19 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.58×** | +6.3 | 3e-08 | 0/17 | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +6.2 | 3e-08 | 8/19 (Panc 03.27, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +5.9 | 2e-07 | 8/19 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +5.6 | 1e-06 | 12/18 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +5.2 | 9e-06 | 1/11 (NCI-H23) | top dose only | noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.41×** | +4.5 | 2e-04 | 2/18 (BT-474, SNU-423) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.4 | 5e-04 | 0/15 | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +4.0 | 0.002 | 7/19 (HOP62, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tazarotene (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.003 | 0/19 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.007 | 1/18 (HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.018 | 1/19 (BT-474) | inconsistent across doses |  |
| [[Orlistat (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.020 | 0/18 | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.036 | 0/18 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12806.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 5 lines (A498 0.119×, A-427 0.173×, NCI-H460 0.152×, NCI-H2347 0.214×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1792 0.0803×, A498 0.154×, HOP62 0.251×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 0.200×, NCI-H460 0.307×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.302×); [[Auranofin (drug)]] 5 µM in 1 line (HEC-1-A 0.194×); [[Roxadustat (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0786×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.760× | -3.5 | 0.29 | 1/19 (NCI-H2030) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 35.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 19.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -13.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 48.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -13.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 19.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 23.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.0803× (z -15.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.0) |
| [[H4 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.231× (z -8.5) ⚠ cell-cycle shift, explains ~20% of this change |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.194× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 3.69 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0786× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 7.16 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0691× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[NCI-H23 (line)]] | alt | 31.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -10.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.103× (z -11.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.839 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.772 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.702 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.702 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.857 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.798 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.734 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF26]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[GPR63]] | +0.60 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[EEF2K]] | +0.57 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CEP85]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[RAD51]] | +0.56 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[EPHB4]] | +0.55 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[CMC2]] | +0.55 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[ABHD12]] | +0.53 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[ZNF732]] | +0.53 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[C1orf21]] | +0.53 | +0.47 / +0.37 | both halves | 7e-05 |  |
| [[KLHL8]] | +0.53 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[POC1A]] | +0.52 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP1B]] | -0.58 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[LINC00174]] | -0.55 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[TSPAN31]] | -0.53 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CHURC1]] | -0.52 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[PIN4]] | -0.52 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[RIMOC1]] | -0.50 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[CHM]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[MFSD4B]] | -0.50 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[BROX]] | -0.50 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[USP40]] | -0.50 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[LYRM2]] | -0.50 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[PDCL3P4]] | -0.50 | -0.39 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DMBX1]] | B | DMBX1 activity raises ZYG11A's level | lines that do not express DMBX1 (11) vs lines expressing it (39) | 2.96× lower at baseline in the lines without DMBX1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ERICH2, NTN1, KCNIP3 |
| [[SCML2]] | B | SCML2 activity raises ZYG11A's level | lines that do not express SCML2 (7) vs lines expressing it (43) | 3.11× lower at baseline in the lines without SCML2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ASAP3, ENSG00000267131, LAG3 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf58]] | B | ZYG11A activity raises C11orf58's level | lines that do not express ZYG11A (29) vs lines expressing it (21) | 1.00× lower at baseline in the lines without ZYG11A | 0.051 | ⚠ within organs, on part of the lines; also absent: ANOS1, LGSN, DAW1 |
| [[TOP3A]] | B | ZYG11A activity raises TOP3A's level | lines that do not express ZYG11A (29) vs lines expressing it (21) | 1.04× lower at baseline in the lines without ZYG11A | 0.054 | ⚠ within organs, on part of the lines; also absent: ANOS1, LGSN, DAW1 |
| [[GALNT14]] | C | ZYG11A activity raises GALNT14's level | lines that do not express ZYG11A (29) vs lines expressing it (21) | 4.07× lower at baseline in the lines without ZYG11A | 0.029 | ⚠ within organs, on part of the lines; also absent: ANOS1, LGSN, DAW1; co-absent with the target |

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-19.7, 31.9); signed map (-43.9, -30.5). **Vector** length 43.5, 10.2% of its response variance represented; |z| ≥ 3 in 439 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +20.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.1 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.0 | +5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.0 | +1.6 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.4 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | -0.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | zyg-11 family member A, cell cycle regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:52,842,511-52,894,998 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZYG11 |
| Gene groups (HGNC) | ZYG11 cell cycle regulator family; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6WRX3](https://www.uniprot.org/uniprotkb/Q6WRX3) (Protein zyg-11 homolog A):

> Probably acts as a target recruitment subunit in an E3 ubiquitin ligase complex ZYGA-CUL2-elongin BC.

**Summary**, from NCBI Gene [440590](https://www.ncbi.nlm.nih.gov/gene/440590):

> Predicted to be part of Cul2-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32058](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32058) · Entrez [440590](https://www.ncbi.nlm.nih.gov/gene/440590) · UniProt [Q6WRX3](https://www.uniprot.org/uniprotkb/Q6WRX3) · Ensembl [ENSG00000203995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203995)

## Data

Gene col 12806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12806); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12806]; `tensor/DDL_lfc|DDL_z.npy` [12806]; `embed/gene_vectors.npy` [12806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12806 or target_col == 12806). Every well: [[ZYG11A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZYG11A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
