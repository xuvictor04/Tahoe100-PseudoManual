---
symbol: "FADS3"
type: "gene"
col: 13324
ensembl_id: "ENSG00000221968"
name: "fatty acid desaturase 3"
location: "11q12.2"
module: 100
arm: "+"
pooled_cpm: 11.77
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 15
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# FADS3

*fatty acid desaturase 3* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.81× (z +10.7, q 5e-24, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.561× (z -7.0, q 1e-09, down in 26 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC39A14]] (+0.68, fdr 7e-06), [[FOXO6]] (+0.62, fdr 2e-05), [[MKNK2]] (+0.62, fdr 1e-05); moves opposite to [[DECR1]] (-0.54, fdr 9e-05), [[ALG8]] (-0.51, fdr 5e-05), [[ASH2L]] (-0.50, fdr 4e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SLC29A4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13324.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +10.7 | 5e-24 | 37/47 (C32, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +9.1 | 3e-17 | 34/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +8.5 | 5e-15 | 28/46 (LoVo, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +8.2 | 4e-14 | 29/46 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +6.6 | 5e-09 | 24/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +6.1 | 1e-07 | 27/45 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +5.6 | 2e-06 | 22/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.012 | 15/47 (A-172, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.6 | 0.021 | 14/38 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.021 | 9/47 (J82, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.024 | 10/47 (A498, J82, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +3.4 | 0.025 | 4/46 (Hs 766T, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.025 | 9/46 (NCI-H460, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +3.3 | 0.035 | 9/47 (A-172, J82, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.035 | 11/45 (SNU-423, HOP62, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.050 | 11/45 (J82, SW 900, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.18× | +3.0 | 0.080 | 8/47 (A498, H4, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13324.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.561×** | -7.0 | 1e-09 | 26/43 (SNU-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.704×** | -6.3 | 1e-07 | 25/44 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.605×** | -6.1 | 2e-07 | 24/45 (HOP62, BT-474, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.613×** | -6.0 | 3e-07 | 25/45 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.883× | -5.5 | 4e-06 | 11/47 (SW48, SHP-77, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.653×** | -5.4 | 6e-06 | 23/45 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.711×** | -4.3 | 0.001 | 18/46 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.534×** | -4.2 | 0.002 | 17/46 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.578×** | -3.6 | 0.018 | 16/41 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.762×** | -3.4 | 0.033 | 17/44 (SNU-1, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **0.755×** | -3.4 | 0.033 | 17/40 (SW 900, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.766×** | -3.4 | 0.036 | 19/44 (MIA PaCa-2, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.832×** | -3.3 | 0.047 | 20/47 (HT-29, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.778×** | -3.2 | 0.061 | 5/46 (H4, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 21.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -12.1) |
| [[HT-29 (line)]] | alt | 13.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -13.4) |
| [[SNU-1 (line)]] | wt | 15.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0760× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 3.74 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0578× (z -9.1) |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 8.60 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0744× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0502× (z -12.2) |
| [[LoVo (line)]] | wt | 9.64 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.48× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 7.16 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 9.70 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A14]] | +0.68 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[FOXO6]] | +0.62 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[MKNK2]] | +0.62 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[PEDS1]] | +0.61 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[MAST1]] | +0.60 | +0.43 / +0.59 | both halves | 4e-05 |  |
| [[CAMKK1]] | +0.59 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[MAST3]] | +0.59 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[CFD]] | +0.58 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[PRKAG2]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[LZTS3]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[NRTN]] | +0.57 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[KIF1A]] | +0.56 | +0.36 / +0.53 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.54 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[ALG8]] | -0.51 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ASH2L]] | -0.50 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[GEN1]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[LATS1]] | -0.50 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[DNAAF10]] | -0.50 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[CSTF3]] | -0.49 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[EFCAB6]] | -0.49 | -0.32 / -0.40 | both halves | 1e-04 |  |
| [[MORN1]] | -0.48 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[PDHX]] | -0.48 | -0.31 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC29A4]] | B | SLC29A4 activity raises FADS3's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.96× lower at baseline in the lines without SLC29A4 | 0.013 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[ASAP3]] | B | ASAP3 activity raises FADS3's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 2.02× lower at baseline in the lines without ASAP3 | 0.049 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |
| [[RNF220]] | B | RNF220 activity raises FADS3's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 1.75× lower at baseline in the lines without RNF220 | 0.068 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises FADS3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[IFITM10]] | C | IFITM10 activity raises FADS3's level | lines that do not express IFITM10 (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without IFITM10 | 0.027 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CTSD, FLVCR2; maybe low, not absent |
| [[SMARCD3]] | C | SMARCD3 activity raises FADS3's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 1.96× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.1, -2.4); signed map (-27.6, 22.2). **Vector** length 102, 22.7% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +6.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.1 | +5.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +9.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -2.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.1 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.3 | -2.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | fatty acid desaturase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,873,519-61,892,051 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CYB5RP; previously LLCDL3 |
| Gene groups (HGNC) | Fatty acid desaturases; Cytochrome b5 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5Q0](https://www.uniprot.org/uniprotkb/Q9Y5Q0) (Fatty acid desaturase 3):

> Mammals have different sphingoid bases that differ in their length and/or pattern of desaturation and hydroxyl groups. The predominant sphingoid base that comprises mammalian ceramides is sphing-4-enine (sphingosine or SPH) which has a trans (E) desaturation at carbon 4. FADS3 is a desaturase that introduces a cis (Z) double bond between carbon 14 and carbon 15 of the sphingoid base (also known as long chain base, LCB), producing LCBs such as sphinga-4,14-dienine (SPD, d18:2(4E,14Z)) from SPH. …

**Summary**, from NCBI Gene [3995](https://www.ncbi.nlm.nih.gov/gene/3995):

> The protein encoded by this gene is a member of the fatty acid desaturase (FADS) gene family. Desaturase enzymes regulate unsaturation of fatty acids through the introduction of double bonds between defined carbons of the fatty acyl chain. FADS family members are considered fusion products composed of an N-terminal cytochrome b5-like domain and a C-terminal multiple membrane-spanning desaturase portion, both of which are characterized by conserved histidine motifs. This gene is clustered with …

**Accessions** — [HGNC:3576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3576) · Entrez [3995](https://www.ncbi.nlm.nih.gov/gene/3995) · UniProt [Q9Y5Q0](https://www.uniprot.org/uniprotkb/Q9Y5Q0) · Ensembl [ENSG00000221968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221968)

## Data

Gene col 13324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13324); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13324]; `tensor/DDL_lfc|DDL_z.npy` [13324]; `embed/gene_vectors.npy` [13324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13324 or target_col == 13324). Every well: [[FADS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FADS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
