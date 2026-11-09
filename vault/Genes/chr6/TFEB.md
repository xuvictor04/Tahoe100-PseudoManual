---
symbol: "TFEB"
type: "gene"
col: 3379
ensembl_id: "ENSG00000112561"
name: "transcription factor EB"
location: "6p21.1"
module: 204
arm: "+"
pooled_cpm: 9.2
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# TFEB

*transcription factor EB* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 1.92× (z +9.5, q 1e-18, up in 32 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.524× (z -9.3, q 7e-18, down in 26 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.663× (z -5.9, q 4e-07, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC42EP4]] (+0.60, fdr 1e-05), [[RXRA]] (+0.60, fdr 1e-05), [[NOL4L]] (+0.59, fdr 2e-05); moves opposite to [[ALG13]] (-0.52, fdr 3e-05), [[SLC30A9]] (-0.51, fdr 3e-05), [[CHM]] (-0.50, fdr 4e-05).
> It is in [[Module 204]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CAMK2N1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3379.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **1.92×** | +9.5 | 1e-18 | 32/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +8.5 | 8e-15 | 34/47 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +8.1 | 1e-13 | 30/47 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.8 | 2e-09 | 20/43 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +5.8 | 6e-07 | 19/47 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.13×** | +5.7 | 9e-07 | 17/47 (PANC-1, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +5.7 | 9e-07 | 15/47 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +5.2 | 2e-05 | 14/46 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.40×** | +4.9 | 7e-05 | 12/47 (SW1417, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.38×** | +4.7 | 1e-04 | 14/48 (SW1417, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +4.3 | 0.001 | 15/47 (CFPAC-1, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +4.2 | 0.001 | 14/47 (LoVo, KATO III, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.015 | 6/48 (SW48, PANC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.020 | 13/47 (CFPAC-1, A549, …) | all doses, flat | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.040 | 11/47 (CFPAC-1, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.1 | 0.081 | 11/48 (LS 180, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3379.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.524×** | -9.3 | 7e-18 | 26/35 (NCI-H2347, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.575×** | -7.7 | 5e-12 | 12/15 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.598×** | -6.9 | 1e-09 | 19/26 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.663×** | -5.9 | 4e-07 | 22/47 (HOP62, CHP-212, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.730×** | -4.5 | 7e-04 | 16/47 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.757×** | -4.0 | 0.006 | 16/47 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.764×** | -3.9 | 0.009 | 16/47 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.760×** | -3.6 | 0.023 | 13/41 (RKO, NCI-H1573, …) | all doses, flat | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.624×** | -3.6 | 0.023 | 8/42 (AsPC-1, H4, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.766×** | -3.5 | 0.029 | 12/43 (hTERT-HPNE, NCI-H1573, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.787×** | -3.4 | 0.029 | 6/47 (Panc 03.27, KATO III, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.788×** | -3.4 | 0.029 | 13/47 (NCI-H460, SW48, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.789×** | -3.2 | 0.059 | 14/46 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 0.05 µM |  | **0.807×** | -3.1 | 0.083 | 10/47 (AN3 CA, LoVo, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.672×** | -3.0 | 0.098 | 11/40 (A-427, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.672×** | -3.0 | 0.098 | 10/46 (NCI-H2030, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 11.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -9.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 53.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0795× (z -11.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 9.70 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0923× (z -13.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -14.6) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 6.87 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.124× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~47% of this change |
| [[Hs 766T (line)]] | wt | 6.88 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -8.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 6.91 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0657× (z -10.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 3.57 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0660× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 3.97 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.145× (z -9.2) |
| [[PANC-1 (line)]] | alt | 5.86 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -10.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 9.24 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0715× (z -9.8) |
| [[SW1417 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -10.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 7.16 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42EP4]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[RXRA]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 | pathway: Circadian clock |
| [[NOL4L]] | +0.59 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[UBTD1]] | +0.57 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[PNKD]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ELMO2]] | +0.55 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[RPS6KA1]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 | pathway: MITF-M-regulated melanocyte development |
| [[TEAD3]] | +0.54 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[LRP5L]] | +0.54 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[CRIP2]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ABHD12]] | +0.53 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[AGAP3]] | +0.53 | +0.63 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG13]] | -0.52 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SLC30A9]] | -0.51 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[CHM]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[YIPF6]] | -0.50 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[LINC01355]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[DNAJC11]] | -0.48 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[RABL3]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[DPP8]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[ICE2]] | -0.47 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[MYSM1]] | -0.46 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[SDCBP2-AS1]] | -0.46 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[LINC02728]] | -0.46 | -0.45 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMK2N1]] | B | CAMK2N1 activity raises TFEB's level | lines that do not express CAMK2N1 (8) vs lines expressing it (42) | 1.49× lower at baseline in the lines without CAMK2N1 | 0.067 | ⚠ within organs, on part of the lines; also absent: RPLP0P2; maybe low, not absent |
| [[SSBP2]] | C | SSBP2 activity lowers TFEB's level | lines that do not express SSBP2 (4) vs lines expressing it (46) | 2.32× higher at baseline in the lines without SSBP2 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENAH, AGPAT4, ANKRD44; maybe low, not absent; its own permutation p |
| [[TMEM131L]] | C | TMEM131L activity lowers TFEB's level | lines that do not express TMEM131L (3) vs lines expressing it (47) | 2.29× higher at baseline in the lines without TMEM131L | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.7, -2.9); signed map (-19.0, 21.0). **Vector** length 79.1, 13.9% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.8 | +9.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +6.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +5.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +4.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.5 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.5 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.2 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.1 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.0 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -5.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor EB |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:41,683,978-41,736,259 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TCFEB, bHLHe35 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 4 pathways, smallest: Phosphorylated BMAL1:CLOCK (ARNTL:CLOCK) activates expression of core clock genes; Transcriptional and post-translational regulation of MITF-M expression and activity; Circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [P19484](https://www.uniprot.org/uniprotkb/P19484) (Transcription factor EB):

> Transcription factor that acts as a master regulator of lysosomal biogenesis, autophagy, lysosomal exocytosis, lipid catabolism, energy metabolism and immune response. Specifically recognizes and binds E-box sequences (5'-CANNTG-3'); efficient DNA-binding requires dimerization with itself or with another MiT/TFE family member such as TFE3 or MITF. Involved in the cellular response to amino acid availability by acting downstream of MTOR: in the presence of nutrients, TFEB phosphorylation by MTOR …

**Summary**, from NCBI Gene [7942](https://www.ncbi.nlm.nih.gov/gene/7942):

> Enables DNA-binding transcription factor activity; enzyme binding activity; and transcription cis-regulatory region binding activity. Involved in several processes, including antibacterial innate immune response; cellular response to amino acid starvation; and regulation of lysosome organization. Located in cytosol and lysosomal membrane. Is active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11753](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11753) · Entrez [7942](https://www.ncbi.nlm.nih.gov/gene/7942) · UniProt [P19484](https://www.uniprot.org/uniprotkb/P19484) · Ensembl [ENSG00000112561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112561)

## Data

Gene col 3379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3379); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3379]; `tensor/DDL_lfc|DDL_z.npy` [3379]; `embed/gene_vectors.npy` [3379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3379 or target_col == 3379). Every well: [[TFEB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFEB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
