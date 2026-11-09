---
symbol: "SEPSECS"
type: "gene"
col: 3066
ensembl_id: "ENSG00000109618"
name: "Sep (O-phosphoserine) tRNA:Sec (selenocysteine) tRNA synthase"
location: "4p15.2"
module: 28
arm: "+"
pooled_cpm: 14.82
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 31
n_dd_up_clean: 7
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# SEPSECS

*Sep (O-phosphoserine) tRNA:Sec (selenocysteine) tRNA synthase* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.58× (z +21.9, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.437× (z -13.3, q 1e-37, down in 42 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.536× (z -10.2, q 4e-22, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLK4]] (+0.72, fdr 7e-06), [[MRPS31]] (+0.69, fdr 7e-06), [[MKS1]] (+0.68, fdr 7e-06); moves opposite to [[RAB5C]] (-0.67, fdr 7e-06), [[GNB1L]] (-0.60, fdr 1e-05), [[CMTM8]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3066.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.58×** | +21.9 | 0e+00 | 40/47 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.15×** | +12.5 | 2e-33 | 35/44 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.99×** | +10.9 | 4e-25 | 38/46 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +7.7 | 1e-12 | 29/46 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +6.1 | 1e-07 | 22/47 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.25×** | +5.2 | 2e-05 | 20/48 (J82, SW48, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.8 | 1e-04 | 16/47 (LS 180, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +4.1 | 0.003 | 12/42 (HepG2/C3A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.27×** | +3.9 | 0.005 | 12/47 (J82, A549, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.25×** | +3.4 | 0.039 | 10/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.044 | 5/48 (Hs 766T, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.046 | 10/48 (SW480, BT-474, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.049 | 6/47 (SW1417, LoVo, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.15× | +3.2 | 0.057 | 7/48 (SW480, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3066.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.437×** | -13.3 | 1e-37 | 42/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.487×** | -11.7 | 2e-29 | 32/46 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.536×** | -10.2 | 4e-22 | 36/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.537×** | -10.2 | 4e-22 | 33/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.576×** | -9.0 | 3e-17 | 34/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.390×** | -8.0 | 1e-13 | 31/47 (A498, H4, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.618×** | -7.8 | 4e-13 | 29/47 (SW480, A498, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.418×** | -7.5 | 7e-12 | 32/44 (RPMI-7951, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.428×** | -7.2 | 3e-11 | 28/46 (MIA PaCa-2, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.637×** | -7.1 | 9e-11 | 27/42 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.650×** | -7.0 | 1e-10 | 26/47 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.664×** | -6.7 | 1e-09 | 22/37 (SW1417, A498, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.711×** | -5.6 | 1e-06 | 21/47 (PANC-1, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.701×** | -5.4 | 3e-06 | 15/31 (HEC-1-A, HCT15, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.543×** | -5.2 | 7e-06 | 22/45 (MIA PaCa-2, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.549×** | -5.1 | 1e-05 | 22/46 (LoVo, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.584×** | -4.6 | 1e-04 | 19/43 (COLO 205, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.755×** | -4.3 | 5e-04 | 14/46 (SNU-423, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.697×** | -4.2 | 8e-04 | 20/47 (CHP-212, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.627×** | -4.0 | 0.002 | 17/46 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3066. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.260× (z -9.7) |
| [[SW480 (line)]] | alt | 22.2 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.6) | [[Digitoxin (drug)]] 0.5 µM 0.170× (z -14.6) |
| [[A498 (line)]] | wt | 24.7 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.8) | [[TAK-901 (drug)]] 5 µM 0.146× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 22.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +16.7) | — |
| [[PANC-1 (line)]] | alt | 17.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +16.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -9.7) |
| [[A-427 (line)]] | wt | 16.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +12.3) | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 2 | — | [[Decitabine (drug)]] 0.05 µM 0.111× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 12.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 20.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +11.8) | — |
| [[A549 (line)]] | wt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 7.54 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0914× (z -9.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 8.21 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0772× (z -11.1) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.3) | — |
| [[H4 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0586× (z -12.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 9.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +9.5) | — |
| [[J82 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.3) | — |
| [[KATO III (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.102× (z -9.0) ⚠ toxic |
| [[LoVo (line)]] | wt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 0 | 1 | — | [[EX229 (drug)]] 5 µM 0.0432× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +11.4) | — |
| [[RKO (line)]] | wt | 9.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.76× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0767× (z -8.5) |
| [[SW 900 (line)]] | alt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 8.95 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0842× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3066), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLK4]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.69 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[MKS1]] | +0.68 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[ZNF181]] | +0.68 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[RAD52]] | +0.68 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[ARL14EP]] | +0.68 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[ZC3H6]] | +0.68 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[ETFRF1]] | +0.67 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[CCDC25]] | +0.67 | +0.78 / +0.50 | both halves | 1e-05 |  |
| [[IFT74]] | +0.67 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[ZNF773]] | +0.67 | +0.78 / +0.51 | both halves | 1e-05 |  |
| [[NFYB]] | +0.67 | +0.73 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB5C]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[GNB1L]] | -0.60 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[CMTM8]] | -0.59 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[TPST2]] | -0.59 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[TUFM]] | -0.59 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[HIRA]] | -0.58 | -0.70 / -0.45 | both halves | 3e-05 |  |
| [[PIP5KL1]] | -0.58 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[CD81]] | -0.57 | -0.64 / -0.38 | both halves | 6e-05 |  |
| [[GATAD2A]] | -0.57 | -0.54 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.1, 5.7); signed map (7.1, -22.1). **Vector** length 92.7, 20.0% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.7 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.3 | +21.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.2 | +12.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.8 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -13.3 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -10.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | -9.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | Sep (O-phosphoserine) tRNA:Sec (selenocysteine) tRNA synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:25,120,014-25,160,550 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLA/LP, SLA, SLA-p35, SecS |
| Reactome | 3 pathways, smallest: Selenocysteine synthesis; Selenoamino acid metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HD40](https://www.uniprot.org/uniprotkb/Q9HD40) (O-phosphoseryl-tRNA(Sec) selenium transferase):

> Converts O-phosphoseryl-tRNA(Sec) to selenocysteinyl-tRNA(Sec) required for selenoprotein biosynthesis.

**Summary**, from NCBI Gene [51091](https://www.ncbi.nlm.nih.gov/gene/51091):

> The amino acid selenocysteine is the only amino acid that does not have its own tRNA synthetase. Instead, this amino acid is synthesized on its cognate tRNA in a three step process. The protein encoded by this gene catalyzes the third step in the process, the conversion of O-phosphoseryl-tRNA(Sec) to selenocysteinyl-tRNA(Sec).[provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:30605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30605) · Entrez [51091](https://www.ncbi.nlm.nih.gov/gene/51091) · UniProt [Q9HD40](https://www.uniprot.org/uniprotkb/Q9HD40) · Ensembl [ENSG00000109618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109618)

## Data

Gene col 3066: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3066); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3066, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3066]; `tensor/DDL_lfc|DDL_z.npy` [3066]; `embed/gene_vectors.npy` [3066]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3066 or target_col == 3066). Every well: [[SEPSECS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPSECS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
