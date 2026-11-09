---
symbol: "FBF1"
type: "gene"
col: 12059
ensembl_id: "ENSG00000188878"
name: "Fas binding factor 1"
location: "17q25.1"
module: 91
arm: "+"
pooled_cpm: 9.6
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# FBF1

*Fas binding factor 1* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (17 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.99× (z +22.5, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.569× (z -8.2, q 1e-13, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PYCR2]] (+0.61, fdr 1e-05), [[REXO5]] (+0.60, fdr 9e-06), [[PRDM5]] (+0.58, fdr 4e-05); moves opposite to [[STX7]] (-0.54, fdr 3e-05), [[UBE3D]] (-0.52, fdr 1e-04), [[TOMM20]] (-0.50, fdr 6e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Folic acid (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12059.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.99×** | +22.5 | 0e+00 | 42/44 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.00×** | +15.3 | 0e+00 | 36/44 (PANC-1, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **2.32×** | +12.2 | 6e-32 | 41/46 (SW480, A498, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.27×** | +11.8 | 3e-30 | 34/46 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.12×** | +10.5 | 1e-23 | 35/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +10.1 | 4e-22 | 30/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **2.06×** | +10.1 | 7e-22 | 26/35 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.00×** | +10.0 | 7e-22 | 38/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.8 | 3e-13 | 27/47 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.61×** | +6.9 | 3e-10 | 25/46 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.61×** | +6.9 | 3e-10 | 22/46 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **1.58×** | +6.6 | 2e-09 | 18/34 (HEC-1-A, CFPAC-1, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.53×** | +6.2 | 3e-08 | 22/45 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.55×** | +5.9 | 2e-07 | 11/22 (LoVo, SHP-77, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +5.7 | 5e-07 | 19/45 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +5.4 | 2e-06 | 14/45 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +5.1 | 9e-06 | 15/46 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 2e-05 | 14/46 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.24×** | +4.4 | 3e-04 | 16/47 (A549, A-427, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.043 | 1/46 (SW480) | all doses, flat | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 5 µM |  | **1.30×** | +2.8 | 0.090 | 3/44 (HEC-1-A, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12059.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.569×** | -8.2 | 1e-13 | 27/46 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.644×** | -6.4 | 4e-08 | 21/43 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.662×** | -6.0 | 4e-07 | 24/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.472×** | -5.7 | 2e-06 | 21/42 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.582×** | -4.1 | 0.004 | 13/38 (LOX-IMVI, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.763×** | -3.9 | 0.008 | 16/46 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.603×** | -3.8 | 0.010 | 11/46 (C-33 A, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.841× | -3.6 | 0.025 | 15/47 (NCI-H1573, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.793×** | -3.4 | 0.045 | 12/46 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tadalafil (drug)]] 5 µM |  | **0.789×** | -3.3 | 0.048 | 13/46 (HCT15, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.797×** | -3.3 | 0.048 | 9/45 (C-33 A, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -3.1 | 0.082 | 12/47 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.809×** | -3.1 | 0.087 | 9/44 (Panc 03.27, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.81 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.7 | 3 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.256× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.363× (z -8.8) |
| [[SW480 (line)]] | alt | 7.07 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +11.3) | — |
| [[A498 (line)]] | wt | 11.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 5.94 | 0 | 2 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0866× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 20.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.252× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 7.73 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +11.6) | — |
| [[RKO (line)]] | wt | 9.03 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.117× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 30.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -11.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 8.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 2.67 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0660× (z -8.9) |
| [[LoVo (line)]] | wt | 8.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 7.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 6.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[A-172 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYCR2]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[REXO5]] | +0.60 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[PRDM5]] | +0.58 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[GINS4]] | +0.57 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[PIDD1]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ESCO2]] | +0.56 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PHF2]] | +0.55 | +0.42 / +0.37 | both halves | 8e-05 |  |
| [[POLA2]] | +0.54 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[SERPINB6]] | +0.54 | +0.27 / +0.39 | both halves | 3e-04 |  |
| [[GEN1]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[WDR90]] | +0.54 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[RABL2B]] | +0.53 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX7]] | -0.54 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[UBE3D]] | -0.52 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[TOMM20]] | -0.50 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[CACUL1]] | -0.47 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[TMEM241]] | -0.47 | -0.25 / -0.35 | both halves | 4e-04 |  |
| [[FKBP7]] | -0.46 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[PLA2G12A]] | -0.46 | -0.46 / -0.29 | both halves | 3e-04 |  |
| [[ATP5F1C]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 | pathway: Organelle biogenesis and maintenance |
| [[LRBA]] | -0.46 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[HMGN3]] | -0.46 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[NCK1]] | -0.46 | -0.57 / -0.26 | both halves | 4e-04 |  |
| [[RAB4A]] | -0.45 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FBF1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.5% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CENPP]] | C | CENPP activity raises FBF1's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.28× lower at baseline in the lines without CENPP | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Folic acid (drug)]] 5 µM | C | FBF1's natural level lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | FBF1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.308 over the table, 0.059 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | FBF1's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | FBF1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.437 over the table, 0.045 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-41.5, -48.5); signed map (-43.1, -49.0). **Vector** length 73.1, 13.3% of its response variance represented; |z| ≥ 3 in 1,118 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +22.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.0 | +15.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.4 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.2 | +10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | +3.6 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.4 | +4.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.2 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | +5.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -4.3 | -3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | +1.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -2.8 | -4.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | Fas binding factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,909,574-75,941,140 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00103, FBF-1, KIAA1863, ALB |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TES7](https://www.uniprot.org/uniprotkb/Q8TES7) (Fas-binding factor 1):

> Keratin-binding protein required for epithelial cell polarization. Involved in apical junction complex (AJC) assembly via its interaction with PARD3. Required for ciliogenesis.

**Summary**, from NCBI Gene [85302](https://www.ncbi.nlm.nih.gov/gene/85302):

> Involved in apical junction assembly and establishment of epithelial cell polarity. Acts upstream of or within cilium assembly. Located in apical junction complex and cytoskeleton. Part of ciliary transition fiber. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24674) · Entrez [85302](https://www.ncbi.nlm.nih.gov/gene/85302) · UniProt [Q8TES7](https://www.uniprot.org/uniprotkb/Q8TES7) · Ensembl [ENSG00000188878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188878)

## Data

Gene col 12059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12059); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12059]; `tensor/DDL_lfc|DDL_z.npy` [12059]; `embed/gene_vectors.npy` [12059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12059 or target_col == 12059). Every well: [[FBF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
