---
symbol: "IFTAP"
type: "gene"
col: 9292
ensembl_id: "ENSG00000166352"
name: "intraflagellar transport associated protein"
location: "11p12"
module: 17
arm: "+"
pooled_cpm: 7.57
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 20
n_dd_up_clean: 17
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# IFTAP

*intraflagellar transport associated protein* — 11p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.96× (z +7.3, q 2e-10, up in 10 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.75× (z +6.3, q 6e-08, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.306× (z -13.4, q 4e-38, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT12]] (+0.70, fdr 7e-06), [[MRPS33]] (+0.68, fdr 7e-06), [[TBC1D19]] (+0.68, fdr 1e-05); moves opposite to [[TMEM11-DT]] (-0.69, fdr 2e-05), [[PRDM10]] (-0.65, fdr 1e-05), [[TOP3A]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9292.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +7.3 | 2e-10 | 10/14 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +6.3 | 6e-08 | 17/28 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +6.3 | 6e-08 | 24/45 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +6.1 | 2e-07 | 25/45 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +5.5 | 5e-06 | 19/45 (KATO III, RKO, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +5.4 | 8e-06 | 21/45 (A498, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +5.2 | 2e-05 | 20/45 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +4.6 | 3e-04 | 17/46 (KATO III, SW480, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.5 | 0.027 | 3/35 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +3.4 | 0.046 | 11/38 (LOX-IMVI, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +3.2 | 0.075 | 6/46 (PANC-1, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.081 | 12/45 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.081 | 2/45 (PANC-1, A498) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.081 | 9/46 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.0 | 0.081 | 6/47 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.081 | 11/44 (Panc 03.27, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.081 | 8/41 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.081 | 6/45 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.081 | 11/43 (SW480, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9292.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.306×** | -13.4 | 4e-38 | 42/46 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.326×** | -12.7 | 3e-34 | 38/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.386×** | -10.8 | 1e-24 | 37/45 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -8.3 | 2e-14 | 27/42 (KATO III, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.491×** | -8.0 | 1e-13 | 31/43 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.525×** | -7.3 | 3e-11 | 28/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.625×** | -5.3 | 8e-06 | 18/45 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.625×** | -5.3 | 8e-06 | 22/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.634×** | -5.2 | 2e-05 | 23/44 (SNU-423, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.432×** | -5.0 | 4e-05 | 21/40 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.470×** | -4.5 | 4e-04 | 16/45 (A-427, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.496×** | -4.1 | 0.002 | 12/28 (CFPAC-1, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.691×** | -4.0 | 0.003 | 19/43 (SW480, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.616×** | -3.9 | 0.004 | 15/46 (NCI-H460, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.705×** | -3.8 | 0.005 | 14/37 (A-427, SHP-77, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.727×** | -3.6 | 0.011 | 20/44 (SW480, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.732×** | -3.5 | 0.013 | 9/46 (PANC-1, NCI-H661, …) | rises with dose |  |
| [[Fulvestrant (drug)]] 0.05 µM |  | **0.759×** | -3.1 | 0.052 | 6/45 (SW48, A-172, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -3.0 | 0.070 | 21/42 (SW480, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9292. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.8 | 0 | 8 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.140× (z -14.1) |
| [[PANC-1 (line)]] | alt | 6.66 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.115× (z -11.6) |
| [[KATO III (line)]] | alt | 13.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 5.48 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0998× (z -8.8) |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.0454× (z -16.4) |
| [[A-427 (line)]] | wt | 9.60 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.158× (z -9.1) ⚠ toxic |
| [[H4 (line)]] | wt | 10.6 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0719× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 9.40 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 9.04 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.116× (z -10.1) |
| [[SHP-77 (line)]] | alt | 9.59 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -9.0) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 14.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.132× (z -10.2) |
| [[SNU-1 (line)]] | wt | 9.48 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0405× (z -10.5) |
| [[A-172 (line)]] | wt | 9.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9292), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT12]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[MRPS33]] | +0.68 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[TBC1D19]] | +0.68 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[COMMD8]] | +0.66 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[SNAPIN]] | +0.65 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[IRAK1BP1]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[PABIR1]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[TTC5]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[NPHP1]] | +0.64 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[KBTBD6]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[RBM18]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[ZNF22]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11-DT]] | -0.69 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[PRDM10]] | -0.65 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[TOP3A]] | -0.63 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[CCDC168]] | -0.63 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[CAPN15]] | -0.60 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[MAD1L1]] | -0.57 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[MBOAT7]] | -0.55 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[SENP5]] | -0.55 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[TRNT1]] | -0.55 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[METTL21A]] | -0.54 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[NPIPB11]] | -0.54 | -0.28 / -0.58 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers IFTAP's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[KHDC1]] | B | KHDC1 activity raises IFTAP's level | lines that do not express KHDC1 (15) vs lines expressing it (35) | 1.28× lower at baseline in the lines without KHDC1 | 0.089 | ⚠ within organs, on part of the lines; also absent: KHDC1-AS1, MAP9, C15orf48 |
| [[DYNC2H1]] | B | DYNC2H1 activity raises IFTAP's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 1.63× lower at baseline in the lines without DYNC2H1 | 0.092 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.2, 0.0); signed map (-21.4, -17.5). **Vector** length 60.7, 9.51% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.3 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -3.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p12 — chr11:36,594,369-36,675,695 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38678, HEPIS, NWC; previously C11orf74 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VG3](https://www.uniprot.org/uniprotkb/Q86VG3) (Intraflagellar transport-associated protein):

> Seems to play a role in ciliary BBSome localization, maybe through interaction with IFT-A complex.

**Summary**, from NCBI Gene [119710](https://www.ncbi.nlm.nih.gov/gene/119710):

> This gene encodes a protein that was identified as a cellular interacting partner of non-structural protein 10 of the severe acute respiratory syndrome coronavirus (SARS-CoV). The encoded protein may function as a negative regulator of transcription. There is a pseudogene for this gene on chromosome 1. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2013]

**Accessions** — [HGNC:25142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25142) · Entrez [119710](https://www.ncbi.nlm.nih.gov/gene/119710) · UniProt [Q86VG3](https://www.uniprot.org/uniprotkb/Q86VG3) · Ensembl [ENSG00000166352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166352)

## Data

Gene col 9292: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9292); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9292, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9292]; `tensor/DDL_lfc|DDL_z.npy` [9292]; `embed/gene_vectors.npy` [9292]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9292 or target_col == 9292). Every well: [[IFTAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFTAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
