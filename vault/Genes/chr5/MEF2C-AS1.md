---
symbol: "MEF2C-AS1"
type: "gene"
col: 14530
ensembl_id: "ENSG00000248309"
name: "MEF2C antisense RNA 1"
location: "5q14.3"
module: 108
arm: "+"
pooled_cpm: 32.07
n_lines_expressing: 34
n_dd_up: 15
n_dd_down: 41
n_dd_up_clean: 15
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 10
direction_downstream: 8
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# MEF2C-AS1

*MEF2C antisense RNA 1* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.66× (z +7.3, q 2e-10, up in 23 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (18 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.376× (z -9.9, q 2e-20, down in 26 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR2F2-AS1]] (+0.63, fdr 1e-05), [[LINC01013]] (+0.62, fdr 1e-05), [[MSC-AS1]] (+0.58, fdr 1e-05); moves opposite to [[PTPN3]] (-0.55, fdr 2e-05), [[BCL2L1]] (-0.48, fdr 3e-05), [[MYORG]] (-0.45, fdr 6e-05).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LRRC7]] → it (grade B ⚠); 8 go from it, the strongest it → [[LINC01138]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14530.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +7.3 | 2e-10 | 23/32 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.74×** | +5.7 | 4e-06 | 20/32 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.73×** | +5.6 | 4e-06 | 20/32 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +5.2 | 3e-05 | 21/31 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.68×** | +5.1 | 4e-05 | 23/31 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.58×** | +4.6 | 3e-04 | 21/31 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.53×** | +4.3 | 0.001 | 19/31 (NCI-H1573, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 0.001 | 13/32 (LoVo, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.003 | 19/32 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.005 | 19/31 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.014 | 14/32 (LoVo, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.024 | 9/32 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.036 | 11/31 (SNU-423, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.043 | 14/32 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.096 | 15/31 (SNU-423, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 18 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14530.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.376×** | -9.9 | 2e-20 | 26/31 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.205×** | -8.4 | 1e-14 | 25/32 (A498, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.561×** | -8.2 | 3e-14 | 28/32 (LoVo, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.562×** | -8.2 | 3e-14 | 19/32 (A498, NCI-H1573, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.434×** | -8.1 | 6e-14 | 27/31 (LoVo, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.493×** | -7.1 | 9e-11 | 25/32 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.481×** | -7.1 | 1e-10 | 21/32 (A498, NCI-H1792, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.611×** | -7.0 | 2e-10 | 25/32 (NCI-H1573, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.498×** | -6.6 | 2e-09 | 25/32 (H4, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.522×** | -6.3 | 2e-08 | 21/30 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.548×** | -6.1 | 6e-08 | 23/31 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.318×** | -6.1 | 7e-08 | 20/31 (C32, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.526×** | -6.0 | 9e-08 | 18/27 (NCI-H1792, A498, …) | all doses, flat | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.560×** | -5.8 | 2e-07 | 25/32 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.563×** | -5.8 | 3e-07 | 23/30 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.573×** | -5.6 | 8e-07 | 21/31 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.566×** | -5.5 | 1e-06 | 22/31 (C32, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.629×** | -4.7 | 6e-05 | 20/31 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.643×** | -4.4 | 2e-04 | 18/32 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.656×** | -4.2 | 5e-04 | 17/32 (C32, PANC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.586×** | -3.8 | 0.002 | 18/32 (A-427, SK-MEL-2, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.697×** | -3.5 | 0.008 | 15/31 (PANC-1, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14530. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.7 | 0 | 17 (11 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -18.3) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.241× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 63.0 | 0 | 11 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0731× (z -16.2) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.257× (z -11.9) |
| [[A498 (line)]] | wt | 133 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0653× (z -24.0) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 79.6 | 0 | 9 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -13.2) ⚠ cell-cycle shift, explains ~64% of this change |
| [[H4 (line)]] | wt | 48.6 | 0 | 8 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0989× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0981× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 42.7 | 0 | 7 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.247× (z -9.7) ⚠ cell-cycle shift, explains ~64% of this change |
| [[NCI-H1792 (line)]] | alt | 88.0 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -13.8) ⚠ cell-cycle shift, explains ~55% of this change |
| [[LoVo (line)]] | wt | 67.4 | 2 | 4 (4 ⚠) | [[Binimetinib (drug)]] 5 µM 3.27× (z +8.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0953× (z -16.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 61.8 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0482× (z -9.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.208× (z -9.1) |
| [[A-427 (line)]] | wt | 19.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -11.9) |
| [[C32 (line)]] | wt | 80.1 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0154× (z -12.8) |
| [[Hs 766T (line)]] | wt | 32.2 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.172× (z -9.3) |
| [[HS-578T (line)]] | alt | 36.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -9.3) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0495× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 56.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.100× (z -8.5) |
| [[CHP-212 (line)]] | wt | 54.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0857× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 43.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -13.5) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H23 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.88× (z +12.0) ⚠ position not correctable | — |
| [[RPMI-7951 (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.107× (z -12.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW 900 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -11.3) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A-172 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.43 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.45 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.81 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.53 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.91 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14530), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2F2-AS1]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 | same gene group |
| [[LINC01013]] | +0.62 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[MSC-AS1]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 | same gene group |
| [[MEF2C]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PTPRD]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[MIR3171HG]] | +0.54 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[STAT4]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[ZIC1]] | +0.52 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[ANKRD7]] | +0.51 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[LINC02100]] | +0.51 | +0.55 / +0.36 | both halves | 9e-05 |  |
| [[MIR548XHG]] | +0.51 | +0.49 / +0.39 | both halves | 6e-05 |  |
| [[CCDC102B]] | +0.51 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[NREP]] | +0.51 | +0.43 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN3]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[BCL2L1]] | -0.48 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[MYORG]] | -0.45 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[STK25]] | -0.45 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[BDH1]] | -0.44 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[ANXA3]] | -0.43 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ENTPD6]] | -0.42 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC7]] | B | LRRC7 activity raises MEF2C-AS1's level | lines that do not express LRRC7 (15) vs lines expressing it (35) | 2.64× lower at baseline in the lines without LRRC7 | 0.007 | ⚠ within organs, on part of the lines; also absent: RNF150, MAP2, KCTD16; maybe low, not absent |
| [[MAPK10]] | B | MAPK10 activity raises MEF2C-AS1's level | lines that do not express MAPK10 (11) vs lines expressing it (39) | 3.97× lower at baseline in the lines without MAPK10 | 0.025 | ⚠ within organs, on part of the lines; also absent: PTPN13, HDGFL3, EML1; maybe low, not absent |
| [[ADGRB3]] | B | ADGRB3 activity raises MEF2C-AS1's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 2.68× lower at baseline in the lines without ADGRB3 | 0.026 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4 |
| [[BCL2L1]] | B | BCL2L1 activity lowers MEF2C-AS1's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 3.83× higher at baseline in the lines without BCL2L1 | 0.043 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers MEF2C-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[ANKRD7]] | B | ANKRD7 activity raises MEF2C-AS1's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 3.26× lower at baseline in the lines without ANKRD7 | 0.076 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[MEF2C]] | C | MEF2C activity raises MEF2C-AS1's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 5.34× lower at baseline in the lines without MEF2C | 0.002 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID; co-absent with the target |
| [[FLRT2]] | C | FLRT2 activity raises MEF2C-AS1's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 3.21× lower at baseline in the lines without FLRT2 | 0.030 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2; co-absent with the target |
| [[BAALC-AS1]] | C | BAALC-AS1 activity raises MEF2C-AS1's level | lines that do not express BAALC-AS1 (3) vs lines expressing it (47) | 4.64× lower at baseline in the lines without BAALC-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SATB2, LCA5, MAMDC2-AS1; maybe low, not absent; its own permutation p |
| [[LINC01138]] | C | LINC01138 activity raises MEF2C-AS1's level | lines that do not express LINC01138 (3) vs lines expressing it (47) | 3.80× lower at baseline in the lines without LINC01138 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: RGL1, PAQR8, LINC00623; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01138]] | B | MEF2C-AS1 activity raises LINC01138's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 1.74× lower at baseline in the lines without MEF2C-AS1 | 0.056 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4 |
| [[NREP]] | B | MEF2C-AS1 activity raises NREP's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 2.68× lower at baseline in the lines without MEF2C-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4 |
| [[HOXA11]] | B | MEF2C-AS1 activity raises HOXA11's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 1.12× lower at baseline in the lines without MEF2C-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4 |
| [[CYP1B1-AS1]] | B | MEF2C-AS1 activity raises CYP1B1-AS1's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 2.05× lower at baseline in the lines without MEF2C-AS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4 |
| [[PTPRD]] | B | MEF2C-AS1 activity raises PTPRD's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 3.11× lower at baseline in the lines without MEF2C-AS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4 |
| [[MEF2C]] | C | MEF2C-AS1 activity raises MEF2C's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 6.61× lower at baseline in the lines without MEF2C-AS1 | 1e-03 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4; co-absent with the target |
| [[PCDH7]] | C | MEF2C-AS1 activity raises PCDH7's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 3.91× lower at baseline in the lines without MEF2C-AS1 | 0.036 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4; co-absent with the target |
| [[NLGN1]] | C | MEF2C-AS1 activity raises NLGN1's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 5.03× lower at baseline in the lines without MEF2C-AS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.569). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.4, 25.5); signed map (36.1, 39.9). **Vector** length 98.4, 29.8% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +3.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +4.6 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.5 | -7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.4 | -8.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.3 | -5.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.3 | -5.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -4.1 | -5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.9 | -6.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.0 | -5.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | MEF2C antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q14.3 — chr5:88,883,328-89,466,398 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48908) · Entrez [101929423](https://www.ncbi.nlm.nih.gov/gene/101929423) · Ensembl [ENSG00000248309](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248309)

## Data

Gene col 14530: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14530); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14530, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14530]; `tensor/DDL_lfc|DDL_z.npy` [14530]; `embed/gene_vectors.npy` [14530]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14530 or target_col == 14530). Every well: [[MEF2C-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEF2C-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
