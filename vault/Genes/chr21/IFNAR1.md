---
symbol: "IFNAR1"
type: "gene"
col: 6599
ensembl_id: "ENSG00000142166"
name: "interferon alpha and beta receptor subunit 1"
location: "21q22.11"
module: 68
arm: "+"
pooled_cpm: 76.17
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# IFNAR1

*interferon alpha and beta receptor subunit 1* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.35× (z +5.7, q 7e-06, up in 26 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-172 2.73×, A498 2.39×, PANC-1 2.19×, J82 2.40×, …; ⚠ cell-cycle shift, explains ~82% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A-172 2.58×, A498 2.30×; ⚠ cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 2.82×, A498 2.57×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.607× (z -9.8, q 6e-20, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STXBP3]] (+0.66, fdr 1e-05), [[PAXIP1-AS2]] (+0.66, fdr 1e-05), [[XRN1]] (+0.63, fdr 1e-05); moves opposite to [[BRF1]] (-0.66, fdr 1e-05), [[ATAD3B]] (-0.63, fdr 1e-05), [[DPH7]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6599.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (A-172 2.73×, A498 2.39×, PANC-1 2.19×, J82 2.40×, …; ⚠ cell-cycle shift, explains ~82% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A-172 2.58×, A498 2.30×; ⚠ cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 2.82×, A498 2.57×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.35×** | +5.7 | 7e-06 | 26/48 (A-172, A498, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | 1.19× | +4.8 | 4e-04 | 21/48 (A-172, A498, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.7 | 4e-04 | 23/43 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Amsacrine (drug)]] 5 µM |  | 1.13× | +3.4 | 0.082 | 6/48 (A498, LS 180, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.082 | 14/48 (A498, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6599.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.607×** | -9.8 | 6e-20 | 38/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.619×** | -8.4 | 9e-15 | 41/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.656×** | -8.3 | 2e-14 | 39/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.681×** | -7.6 | 6e-12 | 38/48 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.780×** | -4.9 | 1e-04 | 26/48 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.634×** | -4.7 | 3e-04 | 25/48 (NCI-H460, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -4.2 | 0.002 | 0/50 | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.820×** | -3.9 | 0.007 | 24/48 (SW 1088, hTERT-HPNE, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.700×** | -3.7 | 0.016 | 24/48 (HEC-1-A, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.705×** | -3.6 | 0.019 | 22/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.709×** | -3.5 | 0.021 | 24/48 (C32, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.732×** | -3.2 | 0.064 | 18/45 (LoVo, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.847× | -3.1 | 0.074 | 16/47 (LS 180, COLO 205, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.826×** | -3.1 | 0.074 | 20/48 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6599. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 107 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +18.6) ⚠ cell-cycle shift, explains ~82% of this change | — |
| [[A498 (line)]] | wt | 92.4 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +16.4) ⚠ cell-cycle shift, explains ~82% of this change | — |
| [[CFPAC-1 (line)]] | alt | 116 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.444× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 63.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 76.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.42× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 85.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.464× (z -8.7) |
| [[AN3 CA (line)]] | alt | 59.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0757× (z -13.4) |
| [[BT-474 (line)]] | alt | 51.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.3) ⚠ cell-cycle shift, explains ~82% of this change | — |
| [[HCT15 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -10.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.5) ⚠ cell-cycle shift, explains ~82% of this change | — |
| [[HOP62 (line)]] | alt | 80.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.510× (z -9.0) |
| [[J82 (line)]] | alt | 42.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.9) ⚠ cell-cycle shift, explains ~82% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.459× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 73.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.531× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 51.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.389× (z -10.3) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 45.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.9) ⚠ cell-cycle shift, explains ~82% of this change | — |
| [[AsPC-1 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 93.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 97.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 81.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6599), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STXBP3]] | +0.66 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[PAXIP1-AS2]] | +0.66 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[XRN1]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BAZ2B]] | +0.62 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[ZMAT2]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[LINC02605]] | +0.58 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[TAPBPL]] | +0.58 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[C11orf58]] | +0.58 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SLU7]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CGGBP1]] | +0.57 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CTSS]] | +0.57 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[BTN2A2]] | +0.57 | +0.60 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRF1]] | -0.66 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[ATAD3B]] | -0.63 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[DPH7]] | -0.63 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[PEMT]] | -0.62 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[TRABD]] | -0.61 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[ZNF692]] | -0.61 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[POLRMT]] | -0.61 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[GNB1L]] | -0.59 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[ACTR5]] | -0.59 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[MSTO2P]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[NTAQ1]] | -0.59 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[CPSF1]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-3.9, -27.4); signed map (20.2, -14.7). **Vector** length 111, 29.9% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +7.9 | +4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +6.7 | +5.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.8 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +2.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.7 | -8.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -2.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.6 | -9.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.3 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.2 | -4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.1 | -3.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | interferon alpha and beta receptor subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:33,324,387-33,359,864 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IFRC; previously IFNAR |
| Gene groups (HGNC) | Interferon receptors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INFLAMMATORY_RESPONSE |
| Reactome | 13 pathways, smallest: Regulation of IFNA/IFNB signaling; Evasion by RSV of host interferon responses; Interferon alpha/beta signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P17181](https://www.uniprot.org/uniprotkb/P17181) (Interferon alpha/beta receptor 1):

> Together with IFNAR2, forms the heterodimeric receptor for type I interferons (including interferons alpha, beta, epsilon, omega and kappa). Type I interferon binding activates the JAK-STAT signaling cascade, resulting in transcriptional activation or repression of interferon-regulated genes that encode the effectors of the interferon response. Mechanistically, type I interferon-binding brings the IFNAR1 and IFNAR2 subunits into close proximity with one another, driving their associated Janus …

**Summary**, from NCBI Gene [3454](https://www.ncbi.nlm.nih.gov/gene/3454):

> The protein encoded by this gene is a type I membrane protein that forms one of the two chains of a receptor for interferons alpha and beta. Binding and activation of the receptor stimulates Janus protein kinases, which in turn phosphorylate several proteins, including STAT1 and STAT2. The protein belongs to the type II cytokine receptor family and functions as an antiviral factor. [provided by RefSeq, Jul 2020]

**Accessions** — [HGNC:5432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5432) · Entrez [3454](https://www.ncbi.nlm.nih.gov/gene/3454) · UniProt [P17181](https://www.uniprot.org/uniprotkb/P17181) · Ensembl [ENSG00000142166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142166)

## Data

Gene col 6599: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6599); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6599, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6599]; `tensor/DDL_lfc|DDL_z.npy` [6599]; `embed/gene_vectors.npy` [6599]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6599 or target_col == 6599). Every well: [[IFNAR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFNAR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
