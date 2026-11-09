---
symbol: "LRRC20"
type: "gene"
col: 10286
ensembl_id: "ENSG00000172731"
name: "leucine rich repeat containing 20"
location: "10q22.1"
module: 176
arm: "+"
pooled_cpm: 7.56
n_lines_expressing: 45
n_dd_up: 17
n_dd_down: 22
n_dd_up_clean: 12
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# LRRC20

*leucine rich repeat containing 20* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.36× (z +18.1, q 0e+00, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.322× (z -19.7, q 0e+00, down in 33 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D24]] (+0.72, fdr 7e-06), [[METAP1]] (+0.67, fdr 9e-06), [[PARP1]] (+0.67, fdr 1e-05); moves opposite to [[N4BP2L1]] (-0.67, fdr 4e-05), [[CHMP4A]] (-0.67, fdr 7e-06), [[LINC01004]] (-0.65, fdr 1e-05).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ABCA3]] → it (grade B ⚠); 7 go from it, the strongest it → [[CDCA7L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10286.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.36×** | +18.1 | 0e+00 | 39/42 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.74×** | +16.2 | 0e+00 | 39/42 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.73×** | +16.2 | 0e+00 | 38/42 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +10.7 | 2e-24 | 36/42 (SW480, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.94×** | +10.1 | 6e-22 | 32/42 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.65×** | +8.7 | 2e-16 | 20/38 (BT-474, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **3.88×** | +8.7 | 2e-16 | 29/41 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.89×** | +7.5 | 4e-12 | 7/11 (NCI-H2347, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +7.1 | 6e-11 | 19/39 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +6.5 | 4e-09 | 19/37 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.39×** | +5.7 | 7e-07 | 13/41 (A549, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +5.3 | 7e-06 | 12/42 (PANC-1, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.48×** | +4.8 | 6e-05 | 13/42 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +3.6 | 0.011 | 3/42 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.013 | 6/41 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.35×** | +3.5 | 0.015 | 8/39 (KATO III, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10286.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.322×** | -19.7 | 0e+00 | 33/38 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.348×** | -13.0 | 4e-36 | 29/36 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.386×** | -11.3 | 4e-27 | 24/40 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.434×** | -10.3 | 1e-22 | 32/42 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -6.5 | 9e-09 | 21/37 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.601×** | -6.3 | 3e-08 | 19/42 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.605×** | -6.2 | 5e-08 | 19/42 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.620×** | -5.9 | 3e-07 | 18/39 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.741×** | -5.2 | 1e-05 | 17/42 (SW480, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.661×** | -5.1 | 2e-05 | 19/40 (NCI-H2030, SK-MEL-2, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.673×** | -4.9 | 5e-05 | 9/42 (SK-MEL-2, AN3 CA, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -4.7 | 1e-04 | 17/40 (LS 180, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.694×** | -4.5 | 3e-04 | 16/39 (SW48, RKO, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.703×** | -4.2 | 0.001 | 13/37 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **0.726×** | -3.9 | 0.003 | 14/40 (HCT15, SK-MEL-2, …) | rises with dose |  |
| [[Clotrimazole (drug)]] 5 µM |  | **0.819×** | -3.5 | 0.017 | 8/41 (A498, NCI-H2030, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.764×** | -3.3 | 0.030 | 9/38 (NCI-H460, SW480, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.66 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10286. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.5 | 3 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.36× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -21.2) |
| [[SW48 (line)]] | wt | 20.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0795× (z -15.7) |
| [[SW480 (line)]] | alt | 8.78 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 6.39× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.3) |
| [[HOP62 (line)]] | alt | 6.46 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 10.5× (z +10.2) | [[Docetaxel (drug)]] 0.05 µM 0.108× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HEC-1-A (line)]] | alt | 19.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -16.3) |
| [[LoVo (line)]] | wt | 4.62 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 5.96 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0462× (z -12.2) |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -16.7) |
| [[C-33 A (line)]] | alt | 31.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -13.9) |
| [[J82 (line)]] | alt | 10.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 6.34 | 0 | 2 | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0676× (z -9.1) |
| [[A498 (line)]] | wt | 5.41 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.12× (z +8.7) | — |
| [[A549 (line)]] | wt | 4.81 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0584× (z -10.4) |
| [[Hs 766T (line)]] | wt | 6.55 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0570× (z -15.4) |
| [[KATO III (line)]] | alt | 7.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 6.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 9.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -14.7) |
| [[RKO (line)]] | wt | 6.83 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0464× (z -11.1) |
| [[SHP-77 (line)]] | alt | 7.46 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0874× (z -9.1) |
| [[A-172 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10286), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D24]] | +0.72 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[METAP1]] | +0.67 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[PARP1]] | +0.67 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[GLB1L2]] | +0.67 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[NUP93]] | +0.67 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[PODXL2]] | +0.67 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[RNFT2]] | +0.66 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[CCDC88C]] | +0.66 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[TMTC4]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[AIF1L]] | +0.65 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[LPCAT4]] | +0.65 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[LYPD6]] | +0.64 | +0.51 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP2L1]] | -0.67 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[CHMP4A]] | -0.67 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[LINC01004]] | -0.65 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[GTF2IRD2]] | -0.63 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[KRBOX5]] | -0.63 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[METTL6]] | -0.63 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[TSGA10]] | -0.62 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[FAM200A]] | -0.62 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ZNF764]] | -0.62 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[THAP2]] | -0.62 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[OFD1]] | -0.62 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[CDKL3]] | -0.61 | -0.55 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA3]] | B | ABCA3 activity raises LRRC20's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 2.01× lower at baseline in the lines without ABCA3 | 0.049 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[TLN2]] | B | TLN2 activity raises LRRC20's level | lines that do not express TLN2 (5) vs lines expressing it (45) | 1.63× lower at baseline in the lines without TLN2 | 0.061 | ⚠ within organs, on part of the lines; also absent: FAT3, ENSG00000232732, SLC26A2; maybe low, not absent |
| [[LMX1B]] | B | LMX1B activity raises LRRC20's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.27× lower at baseline in the lines without LMX1B | 0.075 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[SHMT1]] | C | SHMT1 activity raises LRRC20's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.93× lower at baseline in the lines without SHMT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCA7L]] | B | LRRC20 activity raises CDCA7L's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 2.86× lower at baseline in the lines without LRRC20 | 0.049 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent |
| [[MMS22L]] | B | LRRC20 activity raises MMS22L's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 2.16× lower at baseline in the lines without LRRC20 | 0.061 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent |
| [[STRBP]] | B | LRRC20 activity raises STRBP's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 2.69× lower at baseline in the lines without LRRC20 | 0.069 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent |
| [[EBPL]] | B | LRRC20 activity raises EBPL's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without LRRC20 | 0.078 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent |
| [[PACC1]] | B | LRRC20 activity raises PACC1's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without LRRC20 | 0.088 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent |
| [[CAMK2G]] | B | LRRC20 activity raises CAMK2G's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without LRRC20 | 0.099 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent |
| [[SEMA4D]] | C | LRRC20 activity raises SEMA4D's level | lines that do not express LRRC20 (5) vs lines expressing it (45) | 5.13× lower at baseline in the lines without LRRC20 | 0.057 | ⚠ within organs, on part of the lines; also absent: MCM2, MCM10, SEMA4D; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-5.4, -5.2); signed map (-41.9, -11.0). **Vector** length 88.4, 19.4% of its response variance represented; |z| ≥ 3 in 1,079 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +10.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +18.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +16.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +16.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +10.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +8.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +5.7 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.9 | +3.5 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -19.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -13.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -11.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | +0.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.4 | -3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:70,298,970-70,382,650 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10751, FLJ10844 |
| Matched by | ensembl_id |

UniProt [Q8TCA0](https://www.uniprot.org/uniprotkb/Q8TCA0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23421) · Entrez [55222](https://www.ncbi.nlm.nih.gov/gene/55222) · UniProt [Q8TCA0](https://www.uniprot.org/uniprotkb/Q8TCA0) · Ensembl [ENSG00000172731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172731)

## Data

Gene col 10286: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10286); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10286, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10286]; `tensor/DDL_lfc|DDL_z.npy` [10286]; `embed/gene_vectors.npy` [10286]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10286 or target_col == 10286). Every well: [[LRRC20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
