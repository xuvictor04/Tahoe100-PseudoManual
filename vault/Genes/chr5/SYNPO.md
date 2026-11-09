---
symbol: "SYNPO"
type: "gene"
col: 10195
ensembl_id: "ENSG00000171992"
name: "synaptopodin"
location: "5q33.1"
module: 14
arm: "+"
pooled_cpm: 17.11
n_lines_expressing: 35
n_dd_up: 22
n_dd_down: 17
n_dd_up_clean: 19
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 12
direction_downstream: 27
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SYNPO

*synaptopodin* — 5q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 8.95× (z +31.8, q 0e+00, up in 32 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.546× (z -6.2, q 2e-07, down in 23 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL3]] (+0.68, fdr 7e-06), [[TEF]] (+0.68, fdr 8e-06), [[BHLHE41]] (+0.67, fdr 7e-06); moves opposite to [[SNHG30]] (-0.65, fdr 7e-06), [[GPR89A]] (-0.62, fdr 7e-06), [[UQCRH]] (-0.61, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[CYP1B1]] → it (grade B ⚠); 27 go from it, the strongest it → [[CAV1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **8.95×** | +31.8 | 0e+00 | 32/32 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **7.97×** | +20.6 | 0e+00 | 31/33 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.09×** | +14.5 | 1e-45 | 29/32 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.35×** | +12.4 | 4e-33 | 25/33 (CFPAC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.06×** | +7.4 | 1e-11 | 23/33 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.01×** | +7.2 | 5e-11 | 21/33 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +6.8 | 1e-09 | 8/18 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.77×** | +5.7 | 1e-06 | 19/32 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +5.6 | 2e-06 | 8/26 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +5.5 | 3e-06 | 18/33 (NCI-H460, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.68×** | +5.4 | 4e-06 | 17/32 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.67×** | +5.1 | 2e-05 | 13/33 (A-172, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.55×** | +4.8 | 6e-05 | 17/33 (A-172, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.62×** | +4.8 | 7e-05 | 16/33 (A-172, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.39×** | +4.8 | 7e-05 | 17/33 (NCI-H460, A-172, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.002 | 9/33 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +3.8 | 0.004 | 9/33 (NCI-H460, A-172, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10195.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.546×** | -6.2 | 2e-07 | 23/33 (PANC-1, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.558×** | -6.0 | 5e-07 | 19/33 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.564×** | -5.6 | 4e-06 | 18/33 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.587×** | -5.5 | 5e-06 | 20/33 (SW 1088, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.619×** | -5.0 | 7e-05 | 21/30 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.619×** | -4.9 | 7e-05 | 20/33 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.667×** | -4.2 | 0.002 | 17/33 (A498, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.688×** | -3.9 | 0.007 | 16/33 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.689×** | -3.9 | 0.007 | 15/33 (Hs 766T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.710×** | -3.5 | 0.023 | 11/32 (NCI-H1792, HT-29, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.707×** | -3.4 | 0.030 | 16/33 (NCI-H23, A549, …) | rises with dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.713×** | -3.4 | 0.033 | 11/33 (HS-578T, J82, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.536×** | -3.4 | 0.033 | 12/31 (Panc 03.27, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.730×** | -3.3 | 0.046 | 12/33 (H4, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.731×** | -3.2 | 0.046 | 13/32 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **0.737×** | -3.0 | 0.087 | 6/33 (NCI-H460, SNU-423, …) | rises with dose | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 56.7 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +20.5) | [[Digitoxin (drug)]] 5 µM 0.252× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.244× (z -11.4) |
| [[A-172 (line)]] | wt | 30.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +26.2) | — |
| [[NCI-H460 (line)]] | wt | 22.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +23.0) | — |
| [[A549 (line)]] | wt | 29.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +22.9) | — |
| [[HEC-1-A (line)]] | alt | 5.25 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.9× (z +19.0) | — |
| [[Hs 766T (line)]] | wt | 64.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.207× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 22.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.46× (z +15.4) | — |
| [[KATO III (line)]] | alt | 4.43 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +12.6) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0663× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 8.25 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +17.2) | [[Clobetasol propionate (drug)]] 0.05 µM 0.0358× (z -12.6) |
| [[SW 900 (line)]] | alt | 13.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.12× (z +13.4) | — |
| [[CFPAC-1 (line)]] | alt | 8.39 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +19.1) | — |
| [[H4 (line)]] | wt | 21.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +14.5) | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.8× (z +16.1) | — |
| [[HOP62 (line)]] | alt | 25.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +18.0) | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +11.4) | — |
| [[J82 (line)]] | alt | 6.30 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.7× (z +18.6) | — |
| [[LoVo (line)]] | wt | 7.26 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.34× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.0858× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 4.41 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +12.2) | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +13.7) | — |
| [[RPMI-7951 (line)]] | alt | 8.62 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 9.78 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +16.6) | — |
| [[SW1417 (line)]] | alt | 6.25 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +8.7) | [[Oxaprozin (drug)]] 0.5 µM 0.0892× (z -8.6) |
| [[A498 (line)]] | wt | 79.7 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.245× (z -9.0) |
| [[HT-29 (line)]] | alt | 4.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.68× (z +14.5) | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +8.9) | — |
| [[SW 1088 (line)]] | alt | 202 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0502× (z -10.0) |
| [[A-427 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.86 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL3]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[TEF]] | +0.68 | +0.71 / +0.57 | both halves | 8e-06 |  |
| [[BHLHE41]] | +0.67 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[BCL9L]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SYNGAP1]] | +0.66 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[DZIP3]] | +0.65 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[CX3CL1]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[OXTR]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[NOTCH2NLC]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PRR14]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[VEZF1]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[PLXNB2]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG30]] | -0.65 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[GPR89A]] | -0.62 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[UQCRH]] | -0.61 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[TNPO3]] | -0.60 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[PPHLN1]] | -0.59 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[IQCB1]] | -0.58 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[NFATC3]] | -0.58 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[TYW1]] | -0.58 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.57 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[SHQ1]] | -0.57 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[THOC3]] | -0.57 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP1B1]] | B | CYP1B1 activity raises SYNPO's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 2.86× lower at baseline in the lines without CYP1B1 | 0.025 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849 |
| [[DPY19L2P2-1]] | B | DPY19L2P2-1 activity raises SYNPO's level | lines that do not express DPY19L2P2-1 (17) vs lines expressing it (33) | 2.42× lower at baseline in the lines without DPY19L2P2-1 | 0.030 | ⚠ within organs, on part of the lines; also absent: RNF182, ENSG00000234405, FGF2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SYNPO's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[NUAK1]] | B | NUAK1 activity raises SYNPO's level | lines that do not express NUAK1 (5) vs lines expressing it (45) | 3.76× lower at baseline in the lines without NUAK1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TGFB1, DBN1, CAVIN1 |
| [[IL15]] | B | IL15 activity raises SYNPO's level | lines that do not express IL15 (10) vs lines expressing it (40) | 2.28× lower at baseline in the lines without IL15 | 0.069 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[CAVIN1]] | B | CAVIN1 activity raises SYNPO's level | lines that do not express CAVIN1 (6) vs lines expressing it (44) | 3.35× lower at baseline in the lines without CAVIN1 | 0.075 | ⚠ within organs, on part of the lines; also absent: NUAK1, SLC25A43, BLVRA |
| [[ZC3H12A]] | B | ZC3H12A activity raises SYNPO's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 2.67× lower at baseline in the lines without ZC3H12A | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent |
| [[IL32]] | B | IL32 activity raises SYNPO's level | lines that do not express IL32 (18) vs lines expressing it (32) | 1.90× lower at baseline in the lines without IL32 | 0.086 | ⚠ within organs, on part of the lines; also absent: PODXL, APOL1, F3 |
| [[COL7A1]] | C | COL7A1 activity raises SYNPO's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 3.33× lower at baseline in the lines without COL7A1 | 0.020 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; co-absent with the target |
| [[SSPN]] | C | SSPN activity raises SYNPO's level | lines that do not express SSPN (15) vs lines expressing it (35) | 2.99× lower at baseline in the lines without SSPN | 0.023 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent; co-absent with the target |
| [[NALCN]] | C | NALCN activity raises SYNPO's level | lines that do not express NALCN (22) vs lines expressing it (28) | 3.19× lower at baseline in the lines without NALCN | 0.063 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229; co-absent with the target |
| [[IL7R]] | C | IL7R activity raises SYNPO's level | lines that do not express IL7R (30) vs lines expressing it (20) | 3.17× lower at baseline in the lines without IL7R | 0.076 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 21, C 6. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAV1]] | B | SYNPO activity raises CAV1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 3.63× lower at baseline in the lines without SYNPO | 0.007 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[IL15]] | B | SYNPO activity raises IL15's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 2.53× lower at baseline in the lines without SYNPO | 0.018 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[NUAK1]] | B | SYNPO activity raises NUAK1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 2.29× lower at baseline in the lines without SYNPO | 0.022 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[FSTL3]] | B | SYNPO activity raises FSTL3's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 2.49× lower at baseline in the lines without SYNPO | 0.031 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[ZC3H12A]] | B | SYNPO activity raises ZC3H12A's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 1.86× lower at baseline in the lines without SYNPO | 0.040 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[ATP2C2-AS1]] | B | SYNPO activity raises ATP2C2-AS1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 1.51× lower at baseline in the lines without SYNPO | 0.042 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[RFTN1]] | B | SYNPO activity raises RFTN1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 3.42× lower at baseline in the lines without SYNPO | 0.044 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[SLC41A2]] | B | SYNPO activity raises SLC41A2's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 1.96× lower at baseline in the lines without SYNPO | 0.045 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[AGRN]] | B | SYNPO activity raises AGRN's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 1.49× lower at baseline in the lines without SYNPO | 0.046 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[BHLHE41]] | B | SYNPO activity raises BHLHE41's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 2.87× lower at baseline in the lines without SYNPO | 0.047 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[RELB]] | B | SYNPO activity raises RELB's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without SYNPO | 0.057 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[TNKS1BP1]] | B | SYNPO activity raises TNKS1BP1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 1.47× lower at baseline in the lines without SYNPO | 0.058 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.2, 5.2); signed map (28.6, 7.6). **Vector** length 105, 28.6% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +12.1 | +31.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.0 | +20.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.6 | +14.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +7.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.5 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +5.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -6.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.1 | -5.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.9 | -2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.2 | -2.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -2.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.9 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | synaptopodin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:150,601,080-150,659,207 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1029, SYNPO1 |
| Hallmark sets | KRAS_SIGNALING_DN, MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3V7](https://www.uniprot.org/uniprotkb/Q8N3V7) (Synaptopodin):

> Actin-associated protein that may play a role in modulating actin-based shape and motility of dendritic spines and renal podocyte foot processes. Seems to be essential for the formation of spine apparatuses in spines of telencephalic neurons, which is involved in synaptic plasticity (By similarity).

**Summary**, from NCBI Gene [11346](https://www.ncbi.nlm.nih.gov/gene/11346):

> Synaptopodin is an actin-associated protein that may play a role in actin-based cell shape and motility. The name synaptopodin derives from the protein's associations with postsynaptic densities and dendritic spines and with renal podocytes (Mundel et al., 1997 [PubMed 9314539]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:30672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30672) · Entrez [11346](https://www.ncbi.nlm.nih.gov/gene/11346) · UniProt [Q8N3V7](https://www.uniprot.org/uniprotkb/Q8N3V7) · Ensembl [ENSG00000171992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171992)

## Data

Gene col 10195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10195); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10195]; `tensor/DDL_lfc|DDL_z.npy` [10195]; `embed/gene_vectors.npy` [10195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10195 or target_col == 10195). Every well: [[SYNPO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNPO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
