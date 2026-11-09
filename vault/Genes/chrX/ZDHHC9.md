---
symbol: "ZDHHC9"
type: "gene"
col: 12041
ensembl_id: "ENSG00000188706"
name: "zDHHC palmitoyltransferase 9"
location: "Xq26.1"
module: 77
arm: "+"
pooled_cpm: 46.57
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# ZDHHC9

*zDHHC palmitoyltransferase 9* — Xq26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.23× (z +5.6, q 1e-05, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.382× (z -25.5, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO31]] (+0.69, fdr 7e-06), [[TMEM120B]] (+0.68, fdr 2e-05), [[IMPDH1]] (+0.67, fdr 1e-05); moves opposite to [[TIA1]] (-0.69, fdr 2e-05), [[RIPK2-DT]] (-0.68, fdr 1e-05), [[ZFP91]] (-0.67, fdr 3e-05).
> It sits in the **+** arm of [[Module 077]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12041.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +5.6 | 1e-05 | 24/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +4.9 | 3e-04 | 24/47 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.005 | 25/48 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.005 | 17/49 (AsPC-1, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.005 | 12/48 (BT-474, J82, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.022 | 19/48 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.20× | +3.3 | 0.088 | 16/48 (A498, SNU-423, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.2 | 0.11 | 15/48 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Tranilast (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.12 | 8/48 (AsPC-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12041.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.382×** | -25.5 | 0e+00 | 45/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.523×** | -12.1 | 2e-31 | 39/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.522×** | -11.7 | 2e-29 | 37/48 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.750×** | -7.6 | 4e-12 | 33/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.796×** | -4.1 | 0.005 | 19/46 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.669×** | -3.9 | 0.008 | 15/47 (SNU-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.805×** | -3.9 | 0.008 | 16/46 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.6 | 0.024 | 17/48 (NCI-H2347, J82, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.827×** | -3.6 | 0.024 | 17/47 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | **0.830×** | -3.5 | 0.028 | 17/48 (HS-578T, A498, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.827×** | -3.4 | 0.032 | 20/48 (SK-MEL-2, C32, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.839× | -3.3 | 0.049 | 16/48 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -3.2 | 0.054 | 20/48 (SW480, SW1417, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.843× | -3.2 | 0.054 | 12/48 (A-172, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.835× | -3.2 | 0.054 | 14/47 (PANC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.849× | -3.1 | 0.078 | 12/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 104 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -23.9) |
| [[NCI-H2347 (line)]] | alt | 61.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -19.8) |
| [[NCI-H460 (line)]] | wt | 46.0 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.5) ⚠ cell-cycle shift, explains ~6% of this change | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -14.1) |
| [[A498 (line)]] | wt | 68.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -15.9) |
| [[C32 (line)]] | wt | 32.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.1) |
| [[HCT15 (line)]] | alt | 40.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.2) |
| [[HS-578T (line)]] | alt | 39.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -14.9) |
| [[KATO III (line)]] | alt | 50.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 52.1 | 1 | 2 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.16× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -16.5) |
| [[A549 (line)]] | wt | 50.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 59.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -10.4) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.590× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 39.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.3) |
| [[HOP62 (line)]] | alt | 49.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -17.7) |
| [[J82 (line)]] | alt | 43.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -17.2) |
| [[PANC-1 (line)]] | alt | 46.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -16.1) |
| [[RKO (line)]] | wt | 38.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 45.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -21.3) |
| [[SNU-423 (line)]] | alt | 68.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -19.4) |
| [[SW 900 (line)]] | alt | 29.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.0) |
| [[A-172 (line)]] | wt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.4) |
| [[AN3 CA (line)]] | alt | 72.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.6) |
| [[BT-474 (line)]] | alt | 33.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.8) |
| [[C-33 A (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.206× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[CFPAC-1 (line)]] | alt | 72.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.4) |
| [[COLO 205 (line)]] | alt | 37.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.2) |
| [[H4 (line)]] | wt | 42.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 46.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -13.6) |
| [[Hs 766T (line)]] | wt | 46.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 35.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -8.9) |
| [[LoVo (line)]] | wt | 22.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.339× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 31.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 40.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 36.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 30.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[SW1417 (line)]] | alt | 71.8 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.13× (z +9.7) | — |
| [[SW48 (line)]] | wt | 35.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -8.8) |
| [[A-427 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO31]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TMEM120B]] | +0.68 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[IMPDH1]] | +0.67 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[SEC14L2]] | +0.67 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[MMS19]] | +0.66 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[PDCD10]] | +0.64 | +0.73 / +0.43 | both halves | 3e-05 |  |
| [[MAP2K1]] | +0.64 | +0.71 / +0.43 | both halves | 4e-05 | pathway: MAPK family signaling cascades |
| [[HDAC3]] | +0.63 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[GPR155]] | +0.63 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[PACSIN2]] | +0.62 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[BMP8B]] | +0.62 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[PMS2P3-1]] | +0.61 | +0.75 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.69 | -0.73 / -0.48 | both halves | 2e-05 |  |
| [[RIPK2-DT]] | -0.68 | -0.73 / -0.49 | both halves | 1e-05 |  |
| [[ZFP91]] | -0.67 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[ZNF24]] | -0.66 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[LARP7]] | -0.65 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[TLR6]] | -0.64 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[LZIC]] | -0.64 | -0.67 / -0.46 | both halves | 3e-05 |  |
| [[ST7L]] | -0.63 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[BAZ2B]] | -0.63 | -0.70 / -0.36 | both halves | 1e-04 |  |
| [[SERTAD4]] | -0.62 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[AMIGO2]] | -0.62 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[SENP1]] | -0.62 | -0.54 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-1.4, 0.7); signed map (-35.3, 19.7). **Vector** length 119, 31.6% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.4 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.3 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +0.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.9 | +2.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.5 | +2.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.3 | +3.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.2 | -11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.6 | -25.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.2 | -12.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -5.3 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.1 — chrX:129,803,288-129,843,909 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF379, CGI-89, ZNF380, DHHC9; previously ZDHHC10, CXorf11 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Reactome | 10 pathways, smallest: RAS processing; Maturation of spike protein_9694548; Translation of Structural Proteins_9694635 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y397](https://www.uniprot.org/uniprotkb/Q9Y397) (Palmitoyltransferase ZDHHC9):

> Palmitoyltransferase that catalyzes the addition of palmitate onto various protein substrates, such as ADRB2, GSDMD, HRAS, NRAS and CGAS. The ZDHHC9-GOLGA7 complex is a palmitoyltransferase specific for HRAS and NRAS. May have a palmitoyltransferase activity toward the beta-2 adrenergic receptor/ADRB2 and therefore regulate G protein-coupled receptor signaling. Acts as a regulator of innate immunity by catalyzing palmitoylation of CGAS, thereby promoting CGAS homodimerization and cyclic GMP-AMP …

**Summary**, from NCBI Gene [51114](https://www.ncbi.nlm.nih.gov/gene/51114):

> This gene encodes an integral membrane protein that is a member of the zinc finger DHHC domain-containing protein family. The encoded protein forms a complex with golgin subfamily A member 7 and functions as a palmitoyltransferase. This protein specifically palmitoylates HRAS and NRAS. Mutations in this gene are associated with X-linked cognitive disability. Alternate splicing results in multiple transcript variants that encode the same protein.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:18475](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18475) · Entrez [51114](https://www.ncbi.nlm.nih.gov/gene/51114) · UniProt [Q9Y397](https://www.uniprot.org/uniprotkb/Q9Y397) · Ensembl [ENSG00000188706](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188706)

## Data

Gene col 12041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12041); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12041]; `tensor/DDL_lfc|DDL_z.npy` [12041]; `embed/gene_vectors.npy` [12041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12041 or target_col == 12041). Every well: [[ZDHHC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
