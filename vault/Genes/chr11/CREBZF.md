---
symbol: "CREBZF"
type: "gene"
col: 6028
ensembl_id: "ENSG00000137504"
name: "CREB/ATF bZIP transcription factor"
location: "11q14.1"
module: 96
arm: "+"
pooled_cpm: 52.33
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# CREBZF

*CREB/ATF bZIP transcription factor* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.51× (z +13.9, q 3e-41, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.825× (z -4.6, q 0.003, down in 21 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.202×, NCI-H1792 0.373×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.312×; ⚠ cell-cycle shift, explains ~41% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW 1271 0.0826×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRRM2]] (+0.62, fdr 3e-05), [[CNOT3]] (+0.61, fdr 2e-05), [[PAF1]] (+0.58, fdr 2e-05); moves opposite to [[LYPLA1]] (-0.59, fdr 3e-05), [[RASA2]] (-0.50, fdr 1e-04), [[PIGF]] (-0.50, fdr 2e-04).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6028.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +13.9 | 3e-41 | 41/48 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +9.2 | 6e-18 | 31/47 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +7.6 | 4e-12 | 33/49 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +6.4 | 2e-08 | 34/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +6.3 | 4e-08 | 30/48 (RKO, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +5.3 | 1e-05 | 25/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +5.2 | 2e-05 | 25/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +5.1 | 3e-05 | 23/48 (A-427, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +4.9 | 5e-05 | 24/48 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.0 | 0.003 | 20/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.6 | 0.016 | 19/48 (A-427, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.029 | 22/48 (J82, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.037 | 16/48 (SW480, PANC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.059 | 5/48 (HT-29, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.059 | 13/47 (KATO III, NCI-H2347, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.097 | 11/48 (Hs 766T, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6028.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.202×, NCI-H1792 0.373×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.312×; ⚠ cell-cycle shift, explains ~41% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW 1271 0.0826×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.825×** | -4.6 | 0.003 | 21/48 (NCI-H23, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.852× | -3.8 | 0.038 | 13/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.867× | -3.4 | 0.13 | 19/48 (C32, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.871× | -3.3 | 0.15 | 16/48 (HEC-1-A, PANC-1, …) | rises with dose | position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.874× | -3.0 | 0.24 | 13/47 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Aliskiren (drug)]] 0.5 µM |  | 0.881× | -3.0 | 0.24 | 8/48 (SHP-77, NCI-H661, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6028. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 48.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.5) | — |
| [[RKO (line)]] | wt | 53.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +10.5) | — |
| [[A-172 (line)]] | wt | 51.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.2) | — |
| [[A498 (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.450× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 43.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.4) | — |
| [[H4 (line)]] | wt | 55.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -12.2) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HCT15 (line)]] | alt | 60.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.7) | — |
| [[J82 (line)]] | alt | 66.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.7) | — |
| [[KATO III (line)]] | alt | 73.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 51.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[NCI-H23 (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[Panc 03.27 (line)]] | alt | 57.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 83.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 53.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 83.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0826× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 75.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.5) | — |
| [[A-427 (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 71.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6028), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRRM2]] | +0.62 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[CNOT3]] | +0.61 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[PAF1]] | +0.58 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[RXRB]] | +0.58 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[DCAF8]] | +0.56 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[ACIN1]] | +0.56 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[ZNF764]] | +0.56 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[SCAF1]] | +0.56 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[DXO]] | +0.55 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[EIF2B5]] | +0.55 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[RBM4]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[GIGYF1]] | +0.54 | +0.49 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPLA1]] | -0.59 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[RASA2]] | -0.50 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[PIGF]] | -0.50 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[DNAJC5]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[UBA6]] | -0.50 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[ILRUN]] | -0.49 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[STRN]] | -0.48 | -0.51 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[PLEKHB2]] | -0.48 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[GRB2]] | -0.48 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[GGCT]] | -0.48 | -0.48 / -0.22 | both halves | 6e-04 |  |
| [[WDFY2]] | -0.47 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[MYO9B]] | -0.47 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[COG5]] | -0.47 | -0.40 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-11.0, 4.5); signed map (15.3, -22.5). **Vector** length 75.8, 13.5% of its response variance represented; |z| ≥ 3 in 813 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +13.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.5 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.4 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.6 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +5.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +5.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.4 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.2 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.3 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -0.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | CREB/ATF bZIP transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:85,657,742-85,682,908 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZF, SMILE |
| Gene groups (HGNC) | Basic leucine zipper proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS37](https://www.uniprot.org/uniprotkb/Q9NS37) (CREB/ATF bZIP transcription factor):

> Strongly activates transcription when bound to HCFC1. Suppresses the expression of HSV proteins in cells infected with the virus in a HCFC1-dependent manner. Also suppresses the HCFC1-dependent transcriptional activation by CREB3 and reduces the amount of CREB3 in the cell. Able to down-regulate expression of some cellular genes in CREBZF-expressing cells.

**Summary**, from NCBI Gene [58487](https://www.ncbi.nlm.nih.gov/gene/58487):

> Enables identical protein binding activity. Involved in regulation of gene expression and response to virus. Located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24905) · Entrez [58487](https://www.ncbi.nlm.nih.gov/gene/58487) · UniProt [Q9NS37](https://www.uniprot.org/uniprotkb/Q9NS37) · Ensembl [ENSG00000137504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137504)

## Data

Gene col 6028: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6028); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6028, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6028]; `tensor/DDL_lfc|DDL_z.npy` [6028]; `embed/gene_vectors.npy` [6028]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6028 or target_col == 6028). Every well: [[CREBZF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CREBZF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
