---
symbol: "VPS45"
type: "gene"
col: 5884
ensembl_id: "ENSG00000136631"
name: "vacuolar protein sorting 45 homolog"
location: "1q21.2"
module: 36
arm: "+"
pooled_cpm: 51.16
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# VPS45

*vacuolar protein sorting 45 homolog* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.54× (z +9.4, q 4e-18, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.633× (z -8.9, q 3e-16, down in 35 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.813× (z -6.4, q 5e-08, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELMOD3]] (+0.65, fdr 7e-06), [[ALG14]] (+0.60, fdr 1e-05), [[MEF2B]] (+0.57, fdr 3e-05); moves opposite to [[MMP15]] (-0.55, fdr 1e-05), [[RYBP]] (-0.49, fdr 3e-05), [[GJA3]] (-0.47, fdr 5e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +9.4 | 4e-18 | 38/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +6.7 | 4e-09 | 31/48 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +6.5 | 2e-08 | 29/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.32×** | +5.6 | 2e-06 | 29/48 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +5.6 | 2e-06 | 31/47 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.27×** | +4.6 | 3e-04 | 24/46 (SW480, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +4.6 | 3e-04 | 17/48 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.6 | 3e-04 | 22/48 (LS 180, PANC-1, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.3 | 0.001 | 15/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.20× | +4.1 | 0.003 | 11/49 (NCI-H1573, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.21×** | +4.0 | 0.003 | 21/48 (NCI-H23, HOP62, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.20× | +3.9 | 0.005 | 16/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.9 | 0.005 | 0/49 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.7 | 0.007 | 20/48 (RKO, SW480, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.013 | 12/47 (C32, HS-578T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.20× | +3.5 | 0.013 | 12/48 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.013 | 22/48 (AsPC-1, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.014 | 13/49 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.014 | 14/47 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.014 | 8/49 (MIA PaCa-2, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.046 | 7/48 (SW48, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5884.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.633×** | -8.9 | 3e-16 | 35/47 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -6.4 | 5e-08 | 28/48 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.785×** | -5.3 | 3e-05 | 30/49 (LS 180, SHP-77, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.818×** | -4.4 | 0.002 | 23/48 (NCI-H2030, Hs 766T, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.693×** | -4.2 | 0.004 | 22/48 (C32, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.824×** | -3.9 | 0.010 | 19/44 (SK-MEL-2, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | 0.862× | -3.2 | 0.100 | 22/47 (HepG2/C3A, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Aprepitant (drug)]] 0.05 µM |  | 0.866× | -3.1 | 0.14 | 12/48 (Panc 03.27, SW 1088, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.823× | -3.0 | 0.16 | 14/48 (HCT15, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 84.1 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.303× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 73.4 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.309× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 59.8 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0883× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~80% of this change |
| [[A-427 (line)]] | wt | 58.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 43.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 38.0 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.294× (z -8.8) |
| [[LoVo (line)]] | wt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -11.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 41.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.58× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 56.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 62.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.377× (z -9.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 51.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 77.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[SHP-77 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.440× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 62.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -12.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 69.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.114× (z -9.3) ⚠ toxic |
| [[A-172 (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 49.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELMOD3]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ALG14]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[MEF2B]] | +0.57 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[PPWD1]] | +0.55 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ERCC8]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[RAB28]] | +0.54 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[TRAPPC13]] | +0.54 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SLC38A6]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[XPNPEP3]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[BBS1]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[POLR3F]] | +0.53 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[FBXO36]] | +0.53 | +0.54 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP15]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[RYBP]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[GJA3]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[IL17RD]] | -0.47 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[LINC00598]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[RERE]] | -0.46 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[NT5DC3]] | -0.46 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[FYN]] | -0.45 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[TPPP]] | -0.44 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[DISP3]] | -0.44 | -0.22 / -0.45 | both halves | 6e-04 |  |
| [[PPP1R14C]] | -0.44 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[ZDHHC11B]] | -0.44 | -0.30 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.340). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-30.8, 26.6); signed map (-19.5, -23.6). **Vector** length 93.8, 21.3% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.4 | +5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +5.0 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +3.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.3 | -6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.2 | -5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.8 | -8.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -4.2 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | vacuolar protein sorting 45 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:150,067,279-150,145,329 (+) |
| Ensembl biotype | protein_coding |
| Also known as | h-vps45, H1; previously VPS45B, VPS45A |
| Gene groups (HGNC) | SM family of SNARE chaperones |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 11 pathways, smallest: SARS-CoV-2 modulates autophagy; Intra-Golgi traffic; Factors involved in megakaryocyte development and platelet production |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRW7](https://www.uniprot.org/uniprotkb/Q9NRW7) (Vacuolar protein sorting-associated protein 45):

> May play a role in vesicle-mediated protein trafficking from the Golgi stack through the trans-Golgi network.

**Summary**, from NCBI Gene [11311](https://www.ncbi.nlm.nih.gov/gene/11311):

> Vesicle mediated protein sorting plays an important role in segregation of intracellular molecules into distinct organelles. Genetic studies in yeast have identified more than 40 vacuolar protein sorting (VPS) genes involved in vesicle transport to vacuoles. This gene is a member of the Sec1 domain family, and shows a high degree of sequence similarity to mouse, rat and yeast Vps45. The exact function of this gene is not known, but its high expression in peripheral blood mononuclear cells …

**Accessions** — [HGNC:14579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14579) · Entrez [11311](https://www.ncbi.nlm.nih.gov/gene/11311) · UniProt [Q9NRW7](https://www.uniprot.org/uniprotkb/Q9NRW7) · Ensembl [ENSG00000136631](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136631)

## Data

Gene col 5884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5884); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5884]; `tensor/DDL_lfc|DDL_z.npy` [5884]; `embed/gene_vectors.npy` [5884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5884 or target_col == 5884). Every well: [[VPS45 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS45.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
