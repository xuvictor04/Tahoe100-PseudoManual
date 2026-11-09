---
symbol: "GNB2"
type: "gene"
col: 10245
ensembl_id: "ENSG00000172354"
name: "G protein subunit beta 2"
location: "7q22.1"
module: 3
arm: "+"
pooled_cpm: 71.45
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# GNB2

*G protein subunit beta 2* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.17× (z +9.0, q 2e-16, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 4.29×, NCI-H23 4.91×, MIA PaCa-2 5.40×, C32 4.12×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 4.27×, J82 3.04×, NCI-H1573 3.86×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.355× (z -13.1, q 2e-36, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBFA2T2]] (+0.75, fdr 7e-06), [[COX6A1]] (+0.73, fdr 7e-06), [[TRAPPC1]] (+0.73, fdr 7e-06); moves opposite to [[KICS2]] (-0.72, fdr 1e-05), [[TRMT13]] (-0.71, fdr 7e-06), [[ZNF620]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10245.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (PANC-1 4.29×, NCI-H23 4.91×, MIA PaCa-2 5.40×, C32 4.12×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 4.27×, J82 3.04×, NCI-H1573 3.86×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.17×** | +9.0 | 2e-16 | 47/49 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.57×** | +8.1 | 2e-13 | 41/42 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.77×** | +5.1 | 6e-05 | 41/47 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.78×** | +4.8 | 3e-04 | 36/45 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.43× | +3.1 | 0.21 | 29/47 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.41× | +3.1 | 0.21 | 28/48 (SNU-423, RKO, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10245.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.355×** | -13.1 | 2e-36 | 48/48 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.406×** | -8.1 | 2e-13 | 44/48 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.468×** | -6.5 | 1e-08 | 43/48 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.404×** | -4.2 | 0.003 | 41/48 (Panc 03.27, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.425×** | -4.0 | 0.007 | 38/49 (Panc 03.27, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.636×** | -3.5 | 0.039 | 28/48 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 124 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -13.1) |
| [[HS-578T (line)]] | alt | 80.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -15.7) |
| [[hTERT-HPNE (line)]] | wt | 69.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 92.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -23.7) |
| [[Panc 03.27 (line)]] | alt | 80.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -15.3) |
| [[RKO (line)]] | wt | 110 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -23.1) |
| [[A-172 (line)]] | wt | 107 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -11.5) |
| [[HOP62 (line)]] | alt | 56.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -16.2) |
| [[J82 (line)]] | alt | 72.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 66.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 66.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 61.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.3) |
| [[PANC-1 (line)]] | alt | 50.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW48 (line)]] | wt | 91.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -11.9) |
| [[A-427 (line)]] | wt | 64.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.272× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 89.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -10.4) |
| [[BT-474 (line)]] | alt | 66.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 83.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -16.4) |
| [[H4 (line)]] | wt | 64.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -11.8) |
| [[HCT15 (line)]] | alt | 69.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -12.4) |
| [[Hs 766T (line)]] | wt | 92.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -9.6) |
| [[HT-29 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.5) |
| [[KATO III (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 53.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 66.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.3) |
| [[NCI-H661 (line)]] | alt | 85.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 54.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 54.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -14.7) |
| [[SNU-423 (line)]] | alt | 57.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW 900 (line)]] | alt | 69.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.8) |
| [[SW1417 (line)]] | alt | 85.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.9) |
| [[SW480 (line)]] | alt | 71.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -8.8) |
| [[A498 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 69.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | +0.75 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[COX6A1]] | +0.73 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[TRAPPC1]] | +0.73 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.72 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[CD81]] | +0.70 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[IGSF8]] | +0.70 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[UBL5]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[HEBP1]] | +0.69 | +0.64 / +0.51 | both halves | 1e-05 | pathway: G alpha (i) signalling events |
| [[TMED4]] | +0.68 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[KDELR1]] | +0.68 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[NENF]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[KLHL7]] | +0.67 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KICS2]] | -0.72 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[TRMT13]] | -0.71 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[ZNF620]] | -0.70 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[NEPRO-AS1]] | -0.70 | -0.69 / -0.46 | both halves | 3e-05 |  |
| [[GPATCH4]] | -0.69 | -0.70 / -0.55 | both halves | 1e-05 |  |
| [[POGLUT1]] | -0.69 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[PYM1]] | -0.68 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[MTHFSD]] | -0.68 | -0.66 / -0.40 | both halves | 4e-05 |  |
| [[RBM26-AS1]] | -0.67 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[GABPB2]] | -0.67 | -0.68 / -0.38 | both halves | 6e-05 |  |
| [[ST7L]] | -0.67 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.66 | -0.68 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.7, -14.3); signed map (-35.8, 13.5). **Vector** length 79.9, 29.8% of its response variance represented; |z| ≥ 3 in 582 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.8 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.3 | +1.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +1.2 | -1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.9 | -8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -13.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,673,567-100,679,174 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | WD repeat domain containing; G protein subunits beta |
| Hallmark sets | COAGULATION, COMPLEMENT |
| Reactome | 66 pathways, smallest: G beta:gamma signalling through BTK; Prostacyclin signalling through prostacyclin receptor; G beta:gamma signalling through PLC beta |
| Matched by | ensembl_id |

**Function**, from UniProt [P62879](https://www.uniprot.org/uniprotkb/P62879) (Guanine nucleotide-binding protein G(I)/G(S)/G(T) subunit beta-2):

> Guanine nucleotide-binding proteins (G proteins) are involved as a modulator or transducer in various transmembrane signaling systems. The beta and gamma chains are required for the GTPase activity, for replacement of GDP by GTP, and for G protein-effector interaction.

**Summary**, from NCBI Gene [2783](https://www.ncbi.nlm.nih.gov/gene/2783):

> Heterotrimeric guanine nucleotide-binding proteins (G proteins), which integrate signals between receptors and effector proteins, are composed of an alpha, a beta, and a gamma subunit. These subunits are encoded by families of related genes. This gene encodes a beta subunit. Beta subunits are important regulators of alpha subunits, as well as of certain signal transduction receptors and effectors. This gene contains a trinucleotide (CCG) repeat length polymorphism in its 5' UTR. [provided by …

**Accessions** — [HGNC:4398](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4398) · Entrez [2783](https://www.ncbi.nlm.nih.gov/gene/2783) · UniProt [P62879](https://www.uniprot.org/uniprotkb/P62879) · Ensembl [ENSG00000172354](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172354)

## Data

Gene col 10245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10245); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10245]; `tensor/DDL_lfc|DDL_z.npy` [10245]; `embed/gene_vectors.npy` [10245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10245 or target_col == 10245). Every well: [[GNB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
