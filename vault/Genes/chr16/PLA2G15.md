---
symbol: "PLA2G15"
type: "gene"
col: 2316
ensembl_id: "ENSG00000103066"
name: "phospholipase A2 group XV"
location: "16q22.1"
module: 85
arm: "+"
pooled_cpm: 8.48
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# PLA2G15

*phospholipase A2 group XV* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.56× (z +30.1, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.237×; ⚠ cell-cycle shift, explains ~73% of this change); [[Isocorydine (drug)]] 0.5 µM in 1 line (Hs 766T 0.0943×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW1417 0.119×); [[Gallic acid (drug)]] 0.05 µM in 1 line (H4 0.0769×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOSPD3]] (+0.71, fdr 1e-05), [[CARD19]] (+0.71, fdr 1e-05), [[GNAI2]] (+0.71, fdr 3e-05); moves opposite to [[POGLUT1]] (-0.67, fdr 1e-05), [[ST7L]] (-0.65, fdr 3e-05), [[FUBP1]] (-0.64, fdr 5e-05).
> It sits in the **+** arm of [[Module 085]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2316.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.56×** | +30.1 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.55×** | +27.5 | 0e+00 | 47/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.24×** | +23.2 | 0e+00 | 47/47 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +12.9 | 3e-36 | 29/43 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +9.2 | 3e-18 | 25/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +7.0 | 2e-10 | 26/42 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.37×** | +5.1 | 3e-05 | 15/43 (SW480, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +5.1 | 3e-05 | 12/47 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.69×** | +4.4 | 7e-04 | 5/47 (NCI-H2030, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +4.4 | 7e-04 | 11/46 (SW480, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.0 | 0.003 | 7/48 (SW480, SW1417, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.61×** | +4.0 | 0.003 | 5/42 (SW480, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.005 | 9/48 (H4, A498, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.036 | 10/46 (NCI-H460, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.063 | 9/47 (SW48, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2316.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.237×; ⚠ cell-cycle shift, explains ~73% of this change); [[Isocorydine (drug)]] 0.5 µM in 1 line (Hs 766T 0.0943×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW1417 0.119×); [[Gallic acid (drug)]] 0.05 µM in 1 line (H4 0.0769×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -4.7 | 0.002 | 7/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.811× | -3.4 | 0.22 | 6/47 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.815× | -3.1 | 0.32 | 8/45 (HOP62, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.0 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 11.7× (z +20.2) | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 7.84× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 6.67 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 10.4× (z +13.8) | — |
| [[SW1417 (line)]] | alt | 7.67 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 10.5× (z +11.2) | [[Pyridoxine (drug)]] 0.5 µM 0.119× (z -10.1) |
| [[A498 (line)]] | wt | 8.77 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.60× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 18.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.32× (z +13.4) | — |
| [[J82 (line)]] | alt | 11.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.45× (z +11.4) | — |
| [[KATO III (line)]] | alt | 6.76 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 11.1× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 4.40 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.79× (z +10.7) | — |
| [[A549 (line)]] | wt | 4.89 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 12.6× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 3.50 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 13.7× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 9.61 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.95× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 9.72 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 12.3× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 8.30 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 7.13× (z +8.8) | [[Isocorydine (drug)]] 0.5 µM 0.0943× (z -10.5) |
| [[LoVo (line)]] | wt | 3.78 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 6.79 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.63× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 4.62 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.5× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.28× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 9.64 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.13× (z +9.7) | — |
| [[A-172 (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.1) ⚠ cell-cycle shift, explains ~73% of this change |
| [[H4 (line)]] | wt | 9.75 | 0 | 1 | — | [[Gallic acid (drug)]] 0.05 µM 0.0769× (z -9.2) |
| [[HCT15 (line)]] | alt | 10.0 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0982× (z -8.9) |
| [[HS-578T (line)]] | alt | 12.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 4.63 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.37× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 5.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 4.80 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.150× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 13.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.212× (z -8.9) |
| [[A-427 (line)]] | wt | 9.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSPD3]] | +0.71 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[CARD19]] | +0.71 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.71 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[IGSF8]] | +0.70 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SH2B2]] | +0.69 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.68 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[AGPAT2]] | +0.68 | +0.62 / +0.47 | both halves | 2e-05 | pathway: Glycerophospholipid biosynthesis |
| [[SLC27A1]] | +0.68 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.68 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SNAPC2]] | +0.68 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[RRAS]] | +0.67 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TRAPPC1]] | +0.65 | +0.41 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT1]] | -0.67 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ST7L]] | -0.65 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[FUBP1]] | -0.64 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[GCFC2]] | -0.63 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[TIA1]] | -0.62 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[TXNRD2]] | -0.61 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ZNF337-AS1]] | -0.61 | -0.53 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[PSME3IP1]] | -0.61 | -0.57 / -0.37 | both halves | 9e-05 |  |
| [[EWSR1]] | -0.60 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[RGS5]] | -0.60 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[FZD6]] | -0.60 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[MTHFSD]] | -0.60 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[NEK9]] | -0.60 | -0.44 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.717). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.2, -0.8); signed map (-29.4, 17.2). **Vector** length 72.8, 12.4% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +30.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.4 | +27.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +23.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.0 | +9.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +1.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase A2 group XV |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:68,245,304-68,261,058 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LLPL, GXVPLA2; previously LYPLA3 |
| Gene groups (HGNC) | Phospholipases; Acyltransferases |
| Reactome | 4 pathways, smallest: Hydrolysis of LPC; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCC3](https://www.uniprot.org/uniprotkb/Q8NCC3) (Lysosomal phospholipase A and acyltransferase):

> Has dual calcium-independent phospholipase and O-acyltransferase activities with a potential role in glycerophospholipid homeostasis and remodeling of acyl groups of lipophilic alcohols present in acidic cellular compartments. Catalyzes hydrolysis of the ester bond of the fatty acyl group attached at sn-1 or sn-2 position of phospholipids (phospholipase A1 or A2 activity) and transfer it to the hydroxyl group at the first carbon of lipophilic alcohols (O-acyltransferase activity). Among …

**Summary**, from NCBI Gene [23659](https://www.ncbi.nlm.nih.gov/gene/23659):

> Lysophospholipases are enzymes that act on biological membranes to regulate the multifunctional lysophospholipids. The protein encoded by this gene hydrolyzes lysophosphatidylcholine to glycerophosphorylcholine and a free fatty acid. This enzyme is present in the plasma and thought to be associated with high-density lipoprotein. A later paper contradicts the function of this gene. It demonstrates that this gene encodes a lysosomal enzyme instead of a lysophospholipase and has both …

**Accessions** — [HGNC:17163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17163) · Entrez [23659](https://www.ncbi.nlm.nih.gov/gene/23659) · UniProt [Q8NCC3](https://www.uniprot.org/uniprotkb/Q8NCC3) · Ensembl [ENSG00000103066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103066)

## Data

Gene col 2316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2316); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2316]; `tensor/DDL_lfc|DDL_z.npy` [2316]; `embed/gene_vectors.npy` [2316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2316 or target_col == 2316). Every well: [[PLA2G15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLA2G15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
