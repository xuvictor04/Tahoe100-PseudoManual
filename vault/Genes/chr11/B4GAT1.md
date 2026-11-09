---
symbol: "B4GAT1"
type: "gene"
col: 10514
ensembl_id: "ENSG00000174684"
name: "beta-1,4-glucuronyltransferase 1"
location: "11q13.2"
module: 30
arm: "+"
pooled_cpm: 4.04
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 29
n_dd_up_clean: 5
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# B4GAT1

*beta-1,4-glucuronyltransferase 1* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.31× (z +7.2, q 3e-10, up in 8 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.55× (z +3.9, q 0.013, up in 13 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.271× (z -16.4, q 0e+00, down in 35 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA2013]] (+0.61, fdr 1e-05), [[COPS4]] (+0.58, fdr 1e-05), [[SUFU]] (+0.58, fdr 5e-05); moves opposite to [[NOTCH2NLB]] (-0.54, fdr 1e-05), [[LTO1]] (-0.53, fdr 4e-05), [[SERPINB8]] (-0.51, fdr 7e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SLC35F1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10514.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +7.2 | 3e-10 | 8/9 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +6.9 | 2e-09 | 15/23 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +3.9 | 0.013 | 6/26 (HOP62, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.013 | 13/45 (PANC-1, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.040 | 12/46 (HOP62, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.5 | 0.040 | 2/48 (MIA PaCa-2, C32) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.45×** | +3.3 | 0.060 | 7/45 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.69×** | +3.3 | 0.060 | 6/33 (SHP-77, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.061 | 4/47 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.62× | +3.1 | 0.11 | 2/38 (A549, C32) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.62× | +3.1 | 0.11 | 4/26 (hTERT-HPNE, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10514.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.271×** | -16.4 | 0e+00 | 35/37 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.187×** | -14.9 | 0e+00 | 34/37 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.239×** | -12.2 | 5e-32 | 33/43 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.369×** | -8.8 | 1e-16 | 31/46 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.385×** | -8.5 | 3e-15 | 33/46 (SW 900, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.415×** | -7.8 | 6e-13 | 29/42 (LOX-IMVI, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -6.2 | 4e-08 | 25/47 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.509×** | -6.0 | 2e-07 | 25/47 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.491×** | -6.0 | 2e-07 | 20/41 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.557×** | -5.2 | 1e-05 | 22/44 (A498, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.558×** | -5.2 | 1e-05 | 20/46 (HT-29, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.562×** | -5.1 | 2e-05 | 20/47 (NCI-H23, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.585×** | -4.7 | 9e-05 | 19/45 (SW 900, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.587×** | -4.7 | 9e-05 | 16/34 (SW 900, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.589×** | -4.7 | 1e-04 | 22/47 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.597×** | -4.6 | 2e-04 | 21/46 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10514. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.03 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0339× (z -23.2) |
| [[SW 900 (line)]] | alt | 6.03 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0381× (z -11.6) |
| [[C32 (line)]] | wt | 8.24 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0423× (z -17.1) |
| [[J82 (line)]] | alt | 5.44 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0220× (z -14.8) |
| [[NCI-H2030 (line)]] | alt | 8.35 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0659× (z -17.2) |
| [[A-172 (line)]] | wt | 4.64 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0326× (z -12.3) |
| [[A549 (line)]] | wt | 2.52 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 4.44 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0850× (z -12.7) |
| [[HS-578T (line)]] | alt | 5.66 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0575× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 5.41 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0309× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 3.83 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0516× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 2.91 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.0440× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 5.43 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -9.5) |
| [[A498 (line)]] | wt | 2.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0936× (z -8.8) |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 1 | — | [[Clopidogrel (drug)]] 0.5 µM 0.0450× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 4.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 3.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0766× (z -9.4) |
| [[HOP62 (line)]] | alt | 4.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -10.5) |
| [[Hs 766T (line)]] | wt | 5.95 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -10.6) |
| [[HT-29 (line)]] | alt | 2.60 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0518× (z -8.7) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 4.70 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0558× (z -9.2) |
| [[SNU-423 (line)]] | alt | 4.49 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -8.7) |
| [[SW1417 (line)]] | alt | 3.60 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -9.2) |
| [[SW480 (line)]] | alt | 3.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -9.8) |
| [[A-427 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10514), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA2013]] | +0.61 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[COPS4]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[SUFU]] | +0.58 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[ASAH1]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[ZFP14]] | +0.57 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[PIGS]] | +0.55 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SNRPN]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[OTX1]] | +0.54 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[PPT2]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CTSF]] | +0.54 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[HOXA6]] | +0.54 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[RFX7]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLB]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[LTO1]] | -0.53 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[SERPINB8]] | -0.51 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[SLFN5]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ACTN2]] | -0.50 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[RAPH1]] | -0.50 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[LINC01033]] | -0.49 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[KHNYN]] | -0.49 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[KBTBD8]] | -0.49 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[MAP3K20-AS1]] | -0.49 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[PEA15]] | -0.48 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[ATP2C2-AS1]] | -0.48 | -0.51 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC35F1]] | B | SLC35F1 activity raises B4GAT1's level | lines that do not express SLC35F1 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without SLC35F1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CFL2, CNN3, TPST1; maybe low, not absent |
| [[ACTN2]] | B | ACTN2 activity raises B4GAT1's level | lines that do not express ACTN2 (17) vs lines expressing it (33) | 1.47× lower at baseline in the lines without ACTN2 | 0.055 | ⚠ within organs, on part of the lines; also absent: ZNF568, LINC03041, RNF182; maybe low, not absent |
| [[FKBP7]] | B | FKBP7 activity raises B4GAT1's level | lines that do not express FKBP7 (7) vs lines expressing it (43) | 1.48× lower at baseline in the lines without FKBP7 | 0.078 | ⚠ within organs, on part of the lines; also absent: C12orf75, KCNC4, MXRA7; maybe low, not absent |
| [[P3H4]] | C | P3H4 activity raises B4GAT1's level | lines that do not express P3H4 (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without P3H4 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, TMCC2, E2F7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.430). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-1.8, -10.6); signed map (-31.8, -9.1). **Vector** length 59.1, 8.73% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +3.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +1.1 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -3.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -8.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | -14.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,4-glucuronyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:66,345,374-66,347,629 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IGnT, iGAT, BETA3GNTI, B3GN-T1; previously B3GNT6, B3GNT1 |
| Reactome | 10 pathways, smallest: Matriglycan biosynthesis on DAG1; DAG1 glycosylations; Keratan sulfate biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O43505](https://www.uniprot.org/uniprotkb/O43505) (Beta-1,4-glucuronyltransferase 1):

> Beta-1,4-glucuronyltransferase involved in O-mannosylation of alpha-dystroglycan (DAG1). Transfers a glucuronic acid (GlcA) residue onto a xylose (Xyl) acceptor to produce the glucuronyl-beta-1,4-xylose-beta disaccharide primer, which is further elongated by LARGE1, during synthesis of phosphorylated O-mannosyl glycan. Phosphorylated O-mannosyl glycan is a carbohydrate structure present in alpha-dystroglycan (DAG1), which is required for binding laminin G-like domain-containing extracellular …

**Summary**, from NCBI Gene [11041](https://www.ncbi.nlm.nih.gov/gene/11041):

> This gene encodes a member of the beta-1,3-N-acetylglucosaminyltransferase family. This enzyme is a type II transmembrane protein. It is essential for the synthesis of poly-N-acetyllactosamine, a determinant for the blood group i antigen. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15685) · Entrez [11041](https://www.ncbi.nlm.nih.gov/gene/11041) · UniProt [O43505](https://www.uniprot.org/uniprotkb/O43505) · Ensembl [ENSG00000174684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174684)

## Data

Gene col 10514: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10514); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10514, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10514]; `tensor/DDL_lfc|DDL_z.npy` [10514]; `embed/gene_vectors.npy` [10514]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10514 or target_col == 10514). Every well: [[B4GAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B4GAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
