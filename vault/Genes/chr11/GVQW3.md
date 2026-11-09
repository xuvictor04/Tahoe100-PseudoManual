---
symbol: "GVQW3"
type: "gene"
col: 11012
ensembl_id: "ENSG00000179240"
name: "GVQW motif containing 3"
location: "11q13.5"
module: 163
arm: "+"
pooled_cpm: 4.69
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 16
n_dd_up_clean: 20
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# GVQW3

*GVQW motif containing 3* — 11q13.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.38× (z +20.8, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.321× (z -12.7, q 2e-34, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V0E2]] (+0.68, fdr 1e-05), [[SNX1]] (+0.62, fdr 3e-05), [[FOXJ3]] (+0.62, fdr 8e-05); moves opposite to [[UBXN4]] (-0.58, fdr 3e-05), [[FAM151B]] (-0.56, fdr 2e-04), [[KRBOX5]] (-0.56, fdr 2e-04).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00173]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.38×** | +20.8 | 0e+00 | 46/46 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.36×** | +18.8 | 0e+00 | 44/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.39×** | +16.6 | 0e+00 | 45/46 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.35×** | +9.6 | 1e-19 | 33/46 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +9.0 | 3e-17 | 22/35 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.53×** | +7.4 | 1e-11 | 23/43 (NCI-H23, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +6.8 | 9e-10 | 19/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.83×** | +6.8 | 1e-09 | 19/44 (KATO III, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.0 | 1e-07 | 12/22 (HEC-1-A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.70×** | +5.9 | 2e-07 | 13/46 (A-172, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +5.8 | 4e-07 | 3/11 (SW480, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.42×** | +5.5 | 2e-06 | 9/46 (KATO III, LS 180, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.54×** | +4.6 | 2e-04 | 4/24 (BT-474, A-427, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.48×** | +4.4 | 4e-04 | 6/46 (KATO III, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.47×** | +4.2 | 0.001 | 12/34 (HOP62, LS 180, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.97×** | +4.0 | 0.003 | 3/30 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.004 | 10/43 (PANC-1, HCT15, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.012 | 8/41 (Panc 03.27, A-172, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.025 | 6/46 (HT-29, KATO III, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.038 | 6/46 (SW480, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11012.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.321×** | -12.7 | 2e-34 | 35/46 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.427×** | -9.5 | 3e-19 | 21/37 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.428×** | -9.5 | 3e-19 | 25/44 (A-172, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.634×** | -7.2 | 7e-11 | 24/37 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.517×** | -7.1 | 1e-10 | 24/43 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.536×** | -7.0 | 3e-10 | 23/46 (SHP-77, A-172, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.539×** | -6.9 | 4e-10 | 22/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.582×** | -6.1 | 8e-08 | 19/42 (HT-29, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.583×** | -6.1 | 8e-08 | 20/35 (MIA PaCa-2, SW480, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.589×** | -5.9 | 2e-07 | 19/46 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.589×** | -5.9 | 2e-07 | 20/45 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.661×** | -4.6 | 2e-04 | 12/46 (NCI-H661, SW480, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.692×** | -3.9 | 0.004 | 12/39 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 0.5 µM |  | **0.741×** | -3.4 | 0.031 | 10/43 (HS-578T, RKO, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.746×** | -3.3 | 0.038 | 9/46 (SW480, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.824×** | -3.1 | 0.076 | 15/45 (KATO III, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.66 | 2 | 5 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.15× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -10.1) |
| [[PANC-1 (line)]] | alt | 5.82 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 5.67× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.0175× (z -21.0) |
| [[A-172 (line)]] | wt | 4.23 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 11.0× (z +8.8) | [[Digitoxin (drug)]] 0.5 µM 0.0628× (z -10.1) |
| [[Hs 766T (line)]] | wt | 4.93 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.05 µM 0.0680× (z -9.5) |
| [[HT-29 (line)]] | alt | 4.70 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0600× (z -9.8) |
| [[J82 (line)]] | alt | 4.78 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0540× (z -10.6) |
| [[LoVo (line)]] | wt | 4.00 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 5.14 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0446× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 2.89 | 0 | 1 | — | [[Piroxicam (drug)]] 0.05 µM 0.0409× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -8.8) |
| [[SHP-77 (line)]] | alt | 24.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.114× (z -10.9) |
| [[A-427 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0E2]] | +0.68 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SNX1]] | +0.62 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[FOXJ3]] | +0.62 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[PODXL2]] | +0.61 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[SKP2]] | +0.60 | +0.39 / +0.62 | both halves | 5e-05 |  |
| [[FAM104B]] | +0.59 | +0.65 / +0.39 | both halves | 6e-05 |  |
| [[PCYOX1L]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[PXMP4]] | +0.57 | +0.50 / +0.38 | both halves | 7e-05 |  |
| [[FAM210B]] | +0.56 | +0.57 / +0.36 | both halves | 1e-04 |  |
| [[SCAF4]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[LSM12]] | +0.56 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[NUDT21]] | +0.56 | +0.36 / +0.44 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBXN4]] | -0.58 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[FAM151B]] | -0.56 | -0.36 / -0.30 | both halves | 2e-04 |  |
| [[KRBOX5]] | -0.56 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[C6orf62]] | -0.56 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[PBDC1]] | -0.55 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[LINC03016]] | -0.54 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[NSRP1]] | -0.53 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[CLIP1]] | -0.53 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[TRIP11]] | -0.52 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[SLFN5]] | -0.52 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[RRP8]] | -0.52 | -0.42 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[KIF21A]] | -0.52 | -0.36 / -0.20 | both halves | 7e-04 |  |
| [[SLC22A1]] | -0.52 | -0.34 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00173]] | B | LINC00173 activity raises GVQW3's level | lines that do not express LINC00173 (18) vs lines expressing it (32) | 1.46× lower at baseline in the lines without LINC00173 | 0.061 | ⚠ within organs, on part of the lines; also absent: GBX1, RAB3C, NOVA2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.444). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.5, -13.7); signed map (-35.2, -10.9). **Vector** length 58.0, 8.53% of its response variance represented; |z| ≥ 3 in 1,232 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +20.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +18.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +5.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +4.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.2 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +6.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.9 | -7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -3.7 | -7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -6.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | +0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | GVQW motif containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.5 — chr11:76,381,303-76,414,619 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Mariner transposase derived genes |
| Matched by | ensembl_id |

UniProt [Q3ZCU0](https://www.uniprot.org/uniprotkb/Q3ZCU0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51239) · Entrez [100506127](https://www.ncbi.nlm.nih.gov/gene/100506127) · UniProt [Q3ZCU0](https://www.uniprot.org/uniprotkb/Q3ZCU0) · Ensembl [ENSG00000179240](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179240)

## Data

Gene col 11012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11012); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11012]; `tensor/DDL_lfc|DDL_z.npy` [11012]; `embed/gene_vectors.npy` [11012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11012 or target_col == 11012). Every well: [[GVQW3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GVQW3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
