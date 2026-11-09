---
symbol: "PRSS12"
type: "gene"
col: 8867
ensembl_id: "ENSG00000164099"
name: "serine protease 12"
location: "4q26"
module: 8
arm: "+"
pooled_cpm: 13.21
n_lines_expressing: 31
n_dd_up: 13
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PRSS12

*serine protease 12* — 4q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.81× (z +14.7, q 0e+00, up in 23 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.520× (z -16.1, q 0e+00, down in 23 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAPGEF5]] (+0.62, fdr 7e-06), [[ZNF385B]] (+0.62, fdr 1e-05), [[PIK3AP1]] (+0.59, fdr 1e-05); moves opposite to [[SNX21]] (-0.46, fdr 1e-04), [[LMLN]] (-0.46, fdr 2e-04), [[LRRC27]] (-0.46, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MECOM]] → it (grade B ⚠); 8 go from it, the strongest it → [[UGT8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8867.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +14.7 | 0e+00 | 23/27 (CFPAC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.19×** | +13.7 | 4e-40 | 22/27 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +8.6 | 1e-15 | 8/16 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +7.2 | 9e-11 | 8/28 (HT-29, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.7 | 3e-09 | 11/25 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.92×** | +6.0 | 2e-07 | 6/27 (CFPAC-1, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.34×** | +5.1 | 2e-05 | 9/27 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.21×** | +4.8 | 9e-05 | 8/27 (hTERT-HPNE, SNU-423, …) | rises with dose |  |
| [[Pioglitazone (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 2e-04 | 8/27 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.002 | 5/27 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.006 | 5/27 (NCI-H1792, LoVo, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +3.8 | 0.008 | 5/27 (A498, HOP62, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.6 | 0.014 | 5/27 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.072 | 7/27 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.073 | 1/27 (A498) | top dose only |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.076 | 1/27 (HT-29) | rises with dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.083 | 6/27 (NCI-H1792, LoVo, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8867.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.520×** | -16.1 | 0e+00 | 23/27 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.426×** | -14.8 | 0e+00 | 23/28 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.513×** | -11.6 | 9e-29 | 23/27 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.524×** | -11.2 | 4e-27 | 21/27 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.563×** | -10.0 | 2e-21 | 18/27 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.589×** | -9.2 | 3e-18 | 18/27 (KATO III, AsPC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.589×** | -8.8 | 8e-17 | 18/28 (COLO 205, A498, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.611×** | -8.6 | 8e-16 | 19/27 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.683×** | -6.6 | 2e-09 | 16/27 (COLO 205, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.693×** | -6.4 | 1e-08 | 16/27 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.705×** | -6.1 | 7e-08 | 12/28 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.729×** | -5.5 | 2e-06 | 13/27 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.758×** | -4.5 | 3e-04 | 14/27 (COLO 205, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.795×** | -4.0 | 0.003 | 7/27 (A-427, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.648×** | -3.9 | 0.003 | 11/27 (LOX-IMVI, A498, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **0.736×** | -3.8 | 0.005 | 3/28 (Panc 03.27, SW1417, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 65.8 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -19.3) |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.0) |
| [[A498 (line)]] | wt | 26.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -20.9) |
| [[KATO III (line)]] | alt | 28.3 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.160× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 53.1 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.214× (z -9.6) |
| [[COLO 205 (line)]] | alt | 53.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -17.0) |
| [[SW1417 (line)]] | alt | 20.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -10.0) |
| [[CHP-212 (line)]] | wt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0853× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[RKO (line)]] | wt | 15.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0794× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 23.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -15.8) |
| [[C32 (line)]] | wt | 5.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 13.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.86× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 37.3 | 1 | 0 | [[Retinoic acid (drug)]] 5 µM 2.58× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[A-172 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.945 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAPGEF5]] | +0.62 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ZNF385B]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[PIK3AP1]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TBC1D1]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SYTL4]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MECOM]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[B3GALT5]] | +0.55 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[LYPD6]] | +0.53 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CARMIL1]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[DLG3]] | +0.50 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[UGT8]] | +0.49 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[MBOAT1]] | +0.48 | +0.43 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX21]] | -0.46 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[LMLN]] | -0.46 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[LRRC27]] | -0.46 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[GUSBP1-1]] | -0.44 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[UAP1L1]] | -0.43 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[FBXL9P]] | -0.43 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[FAM228B]] | -0.42 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[TRADD]] | -0.42 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[TMEM234]] | -0.42 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[FAM156A]] | -0.41 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[ENDOV]] | -0.41 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[NUDT16L1]] | -0.40 | -0.36 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MECOM]] | B | MECOM activity raises PRSS12's level | lines that do not express MECOM (18) vs lines expressing it (32) | 1.79× lower at baseline in the lines without MECOM | 0.035 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[LINC02474]] | B | LINC02474 activity raises PRSS12's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 2.32× lower at baseline in the lines without LINC02474 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975 |
| [[UGT8]] | B | UGT8 activity raises PRSS12's level | lines that do not express UGT8 (21) vs lines expressing it (29) | 3.04× lower at baseline in the lines without UGT8 | 0.083 | ⚠ within organs, on part of the lines; also absent: CCSER1, JPH1, ABO |
| [[ADGRF1]] | B | ADGRF1 activity raises PRSS12's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 2.12× lower at baseline in the lines without ADGRF1 | 0.095 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[SYTL4]] | B | SYTL4 activity raises PRSS12's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 2.79× lower at baseline in the lines without SYTL4 | 0.099 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UGT8]] | B | PRSS12 activity raises UGT8's level | lines that do not express PRSS12 (19) vs lines expressing it (31) | 2.51× lower at baseline in the lines without PRSS12 | 0.019 | ⚠ within organs, on part of the lines; also absent: MOXD1, TLL1, ENSG00000289884 |
| [[B3GALT5]] | B | PRSS12 activity raises B3GALT5's level | lines that do not express PRSS12 (19) vs lines expressing it (31) | 2.16× lower at baseline in the lines without PRSS12 | 0.053 | ⚠ within organs, on part of the lines; also absent: MOXD1, TLL1, ENSG00000289884 |
| [[MECOM]] | B | PRSS12 activity raises MECOM's level | lines that do not express PRSS12 (19) vs lines expressing it (31) | 2.42× lower at baseline in the lines without PRSS12 | 0.059 | ⚠ within organs, on part of the lines; also absent: MOXD1, TLL1, ENSG00000289884 |
| [[PLEKHG1]] | B | PRSS12 activity raises PLEKHG1's level | lines that do not express PRSS12 (19) vs lines expressing it (31) | 2.45× lower at baseline in the lines without PRSS12 | 0.060 | ⚠ within organs, on part of the lines; also absent: MOXD1, TLL1, ENSG00000289884 |
| [[LY75]] | B | PRSS12 activity raises LY75's level | lines that do not express PRSS12 (19) vs lines expressing it (31) | 2.52× lower at baseline in the lines without PRSS12 | 0.069 | ⚠ within organs, on part of the lines; also absent: MOXD1, TLL1, ENSG00000289884 |
| [[LINC02474]] | B | PRSS12 activity raises LINC02474's level | lines that do not express PRSS12 (19) vs lines expressing it (31) | 2.09× lower at baseline in the lines without PRSS12 | 0.078 | ⚠ within organs, on part of the lines; also absent: MOXD1, TLL1, ENSG00000289884 |
| [[C6orf132]] | B | PRSS12 activity raises C6orf132's level | lines that do not express PRSS12 (19) vs lines expressing it (31) | 2.04× lower at baseline in the lines without PRSS12 | 0.081 | ⚠ within organs, on part of the lines; also absent: MOXD1, TLL1, ENSG00000289884 |
| [[FAM156A]] | B | PRSS12 activity lowers FAM156A's level | lines that do not express PRSS12 (19) vs lines expressing it (31) | 1.32× higher at baseline in the lines without PRSS12 | 0.088 | ⚠ within organs, on part of the lines; also absent: MOXD1, TLL1, ENSG00000289884 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.439). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.8, 41.4); signed map (53.9, 15.0). **Vector** length 61.9, 12.7% of its response variance represented; |z| ≥ 3 in 727 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +14.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +4.2 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +6.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | -0.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.7 | -9.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -6.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.2 | -11.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.2 | -4.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -6.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | serine protease 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q26 — chr4:118,280,038-118,353,003 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BSSP-3, MRT1 |
| Gene groups (HGNC) | Serine proteases; Scavenger receptor cysteine rich domain containing; Kringle domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P56730](https://www.uniprot.org/uniprotkb/P56730) (Neurotrypsin):

> Plays a role in neuronal plasticity and the proteolytic action may subserve structural reorganizations associated with learning and memory operations.

**Summary**, from NCBI Gene [8492](https://www.ncbi.nlm.nih.gov/gene/8492):

> This gene encodes a member of the trypsin family of serine proteases and contains a signal peptide, a proline-rich region, a Kringle domain, four scavenger receptor cysteine-rich domains, and a trypsin-like serine protease domain. The protein, sometimes referred to as neurotrypsin or motopsin, is secreted from neuronal cells and localizes to the synaptic cleft. Studies in mice show that this protein cleaves a protein, agrin, that is important for the formation and maintenance of exitatory …

**Accessions** — [HGNC:9477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9477) · Entrez [8492](https://www.ncbi.nlm.nih.gov/gene/8492) · UniProt [P56730](https://www.uniprot.org/uniprotkb/P56730) · Ensembl [ENSG00000164099](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164099)

## Data

Gene col 8867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8867); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8867]; `tensor/DDL_lfc|DDL_z.npy` [8867]; `embed/gene_vectors.npy` [8867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8867 or target_col == 8867). Every well: [[PRSS12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRSS12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
