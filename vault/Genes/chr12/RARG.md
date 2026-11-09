---
symbol: "RARG"
type: "gene"
col: 10301
ensembl_id: "ENSG00000172819"
name: "retinoic acid receptor gamma"
location: "12q13.13"
module: 14
arm: "+"
pooled_cpm: 11.36
n_lines_expressing: 47
n_dd_up: 23
n_dd_down: 33
n_dd_up_clean: 17
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 3
direction_downstream: 18
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# RARG

*retinoic acid receptor gamma* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +13.8, q 2e-40, up in 25 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.425× (z -13.4, q 5e-38, down in 34 of 45 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.594× (z -7.5, q 6e-12, down in 24 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDRG2]] (+0.65, fdr 1e-05), [[CA11]] (+0.64, fdr 1e-05), [[CDKN1B]] (+0.62, fdr 1e-05); moves opposite to [[EEFSEC]] (-0.59, fdr 3e-05), [[WRN]] (-0.56, fdr 5e-05), [[RRP7BP-1]] (-0.54, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC02985]] → it (grade B ⚠); 18 go from it, the strongest it → [[NRP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10301.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +13.8 | 2e-40 | 25/43 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +7.7 | 3e-12 | 14/35 (A549, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +6.7 | 3e-09 | 23/43 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +5.5 | 6e-06 | 17/44 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +5.5 | 6e-06 | 18/42 (NCI-H1573, RKO, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.26×** | +5.1 | 3e-05 | 20/42 (J82, SNU-423, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +5.1 | 3e-05 | 15/45 (LoVo, SW480, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.35×** | +4.9 | 7e-05 | 17/45 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.9 | 7e-05 | 7/20 (PANC-1, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 9e-05 | 12/45 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.36×** | +4.8 | 9e-05 | 13/45 (SW480, A-427, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 1e-04 | 10/45 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.7 | 1e-04 | 16/45 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +4.6 | 2e-04 | 12/45 (SW480, RKO, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.32×** | +4.4 | 4e-04 | 10/45 (CFPAC-1, KATO III, …) | all doses, flat | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.8 | 0.004 | 13/45 (A-427, LOX-IMVI, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.005 | 10/43 (RKO, A-427, …) | two highest doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.013 | 10/44 (SW480, RKO, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10301.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.425×** | -13.4 | 5e-38 | 34/45 (A-172, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.485×** | -11.3 | 3e-27 | 29/45 (A-172, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.550×** | -9.4 | 2e-18 | 28/44 (SW48, A-172, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.855× | -8.2 | 4e-14 | 21/45 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.594×** | -7.5 | 6e-12 | 24/43 (BT-474, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.635×** | -7.1 | 1e-10 | 23/44 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.635×** | -7.1 | 1e-10 | 22/44 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.648×** | -6.8 | 9e-10 | 23/44 (BT-474, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.692×** | -5.7 | 6e-07 | 20/44 (BT-474, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.706×** | -5.4 | 3e-06 | 17/44 (CHP-212, SW1417, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.723×** | -5.1 | 2e-05 | 18/45 (C32, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.733×** | -4.8 | 6e-05 | 19/44 (KATO III, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.804×** | -4.8 | 7e-05 | 17/45 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.747×** | -4.6 | 2e-04 | 15/44 (BT-474, SNU-423, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.670×** | -4.5 | 3e-04 | 13/45 (KATO III, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.753×** | -4.4 | 4e-04 | 17/43 (BT-474, HT-29, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.602×** | -4.2 | 0.001 | 12/43 (SW1417, A498, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.604×** | -4.1 | 0.001 | 14/41 (A-172, Hs 766T, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.783×** | -3.8 | 0.004 | 15/42 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.632×** | -3.7 | 0.005 | 9/38 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.635×** | -3.7 | 0.005 | 9/40 (PANC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.3 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -12.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 10.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.198× (z -11.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 14.5 | 0 | 2 (1 ⚠) | — | [[Temsirolimus (drug)]] 0.5 µM 0.0931× (z -9.5) |
| [[A498 (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 6.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +8.6) | — |
| [[LoVo (line)]] | wt | 4.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0594× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LS 180 (line)]] | wt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 6.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +11.9) | — |
| [[PANC-1 (line)]] | alt | 8.12 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.232× (z -8.6) |
| [[SW480 (line)]] | alt | 7.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +14.6) | — |
| [[A-427 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG2]] | +0.65 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CA11]] | +0.64 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CDKN1B]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 | pathway: Signaling by Nuclear Receptors |
| [[GLIS2]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ATP23]] | +0.61 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[BCL3]] | +0.61 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[BCOR]] | +0.60 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[FAM111A-DT]] | +0.60 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[TEF]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[RBM24]] | +0.59 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[DENND2B]] | +0.59 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEFSEC]] | -0.59 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[WRN]] | -0.56 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[RRP7BP-1]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[DAP3]] | -0.54 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SLC30A6]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[CUTC]] | -0.52 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[FAM120B]] | -0.52 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[GPR89A]] | -0.52 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[MTG1]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[LINC02985]] | -0.51 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[GPR89B]] | -0.50 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[MECR]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02985]] | B | LINC02985 activity lowers RARG's level | lines that do not express LINC02985 (15) vs lines expressing it (35) | 1.73× higher at baseline in the lines without LINC02985 | 0.008 | ⚠ within organs, on part of the lines; also absent: GXYLT2 |
| [[TFAP2A]] | B | TFAP2A activity raises RARG's level | lines that do not express TFAP2A (5) vs lines expressing it (45) | 2.35× lower at baseline in the lines without TFAP2A | 0.040 | ⚠ within organs, on part of the lines; also absent: FAM111A, PRNP, TRIM34 |
| [[MAP2K1]] | B | MAP2K1 activity lowers RARG's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 1, C 17. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRP2]] | B | [[RARA]], [[RARB]], RARG activity raises NRP2's level | compounds that target RARA, RARB, RARG: 2 of 2 raise it (Retinoic acid, Tazarotene) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | C | RARG activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 0.70× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| cells under [[Bendamustine (drug)]] 5 µM | C | RARG activity raises the cells' numbers under Bendamustine 5 µM (protects the cells) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 0.74× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| cells under [[Tranilast (drug)]] 0.5 µM | C | RARG activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 0.74× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| cells under [[Raltitrexed (drug)]] 0.5 µM | C | RARG activity lowers the cells' numbers under Raltitrexed 0.5 µM (makes them more sensitive) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 1.36× the cells of the other lines | 0.031 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| cells under [[AT7519 (drug)]] 5 µM | C | RARG activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 0.53× the cells of the other lines | 0.043 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM | C | RARG activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 1.57× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| cells under [[Verteporfin (drug)]] 5 µM | C | RARG activity raises the cells' numbers under Verteporfin 5 µM (protects the cells) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 0.67× the cells of the other lines | 0.057 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| cells under [[Econazole (drug)]] 0.5 µM | C | RARG activity lowers the cells' numbers under Econazole 0.5 µM (makes them more sensitive) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 1.35× the cells of the other lines | 0.060 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| cells under [[PH-797804 (drug)]] 0.05 µM | C | RARG activity lowers the cells' numbers under PH-797804 0.05 µM (makes them more sensitive) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 1.36× the cells of the other lines | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| cells under [[Adenosine (drug)]] 5 µM | C | RARG activity lowers the cells' numbers under Adenosine 5 µM (makes them more sensitive) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 1.19× the cells of the other lines | 0.073 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| cells under [[PF-06260933 (drug)]] 5 µM | C | RARG activity lowers the cells' numbers under PF-06260933 5 µM (makes them more sensitive) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 1.48× the cells of the other lines | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.3, 6.5); signed map (40.8, -0.9). **Vector** length 92.0, 18.9% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +13.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +6.2 | +5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +5.2 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +6.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.1 | +5.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -7.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.8 | -13.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -7.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | retinoic acid receptor gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,210,567-53,232,980 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RARC, NR1B3, RARgamma, RAR-gamma |
| Gene groups (HGNC) | Retinoic acid receptors |
| Reactome | 5 pathways, smallest: Signaling by Retinoic Acid; Nuclear Receptor transcription pathway; Activation of HOX genes during differentiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P13631](https://www.uniprot.org/uniprotkb/P13631) (Retinoic acid receptor gamma):

> Receptor for retinoic acid. Retinoic acid receptors bind as heterodimers to their target response elements in response to their ligands, all-trans or 9-cis retinoic acid, and regulate gene expression in various biological processes. The RAR/RXR heterodimers bind to the retinoic acid response elements (RARE) composed of tandem 5'-AGGTCA-3' sites known as DR1-DR5. In the absence of ligand, acts mainly as an activator of gene expression due to weak binding to corepressors. Required for limb bud …

**Summary**, from NCBI Gene [5916](https://www.ncbi.nlm.nih.gov/gene/5916):

> This gene encodes a retinoic acid receptor that belongs to the nuclear hormone receptor family. Retinoic acid receptors (RARs) act as ligand-dependent transcriptional regulators. When bound to ligands, RARs activate transcription by binding as heterodimers to the retinoic acid response elements (RARE) found in the promoter regions of the target genes. In their unbound form, RARs repress transcription of their target genes. RARs are involved in various biological processes, including limb bud …

**Accessions** — [HGNC:9866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9866) · Entrez [5916](https://www.ncbi.nlm.nih.gov/gene/5916) · UniProt [P13631](https://www.uniprot.org/uniprotkb/P13631) · Ensembl [ENSG00000172819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172819)

## Data

Gene col 10301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10301); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10301]; `tensor/DDL_lfc|DDL_z.npy` [10301]; `embed/gene_vectors.npy` [10301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10301 or target_col == 10301). Every well: [[RARG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RARG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
