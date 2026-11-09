---
symbol: "SNX27"
type: "gene"
col: 6729
ensembl_id: "ENSG00000143376"
name: "sorting nexin 27"
location: "1q21.3"
module: 65
arm: "+"
pooled_cpm: 97.45
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# SNX27

*sorting nexin 27* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.15× (z +5.0, q 3e-04, up in 17 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1792 3.77×, HOP62 2.17×, LoVo 1.69×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 2.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 1.63×; ⚠ cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.711× (z -7.8, q 3e-12, down in 29 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 0.765× (z -4.2, q 0.004, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM1A]] (+0.62, fdr 1e-05), [[LTA4H]] (+0.61, fdr 7e-06), [[MTX2]] (+0.59, fdr 9e-06); moves opposite to [[ZNF274]] (-0.55, fdr 1e-05), [[CLCF1]] (-0.55, fdr 3e-05), [[RASAL2]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6729.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1792 3.77×, HOP62 2.17×, LoVo 1.69×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 2.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 1.63×; ⚠ cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.15× | +5.0 | 3e-04 | 17/48 (NCI-H1573, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +4.6 | 0.001 | 22/48 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.26 | 6/48 (NCI-H460, SW 1088, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.26 | 18/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.13× | +3.1 | 0.26 | 11/48 (AsPC-1, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6729.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.711×** | -7.8 | 3e-12 | 29/45 (C-33 A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.777×** | -6.0 | 5e-07 | 27/48 (NCI-H460, RKO, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.805×** | -5.2 | 4e-05 | 22/44 (SK-MEL-2, SW 900, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.819×** | -5.0 | 1e-04 | 24/49 (SHP-77, A-172, …) | all doses, flat | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.765×** | -4.2 | 0.004 | 26/47 (NCI-H23, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~4% of this change | 0.852× | -3.8 | 0.014 | 20/47 (MIA PaCa-2, SW 900, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.756×** | -3.6 | 0.022 | 22/49 (RKO, NCI-H1792, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.865× | -3.6 | 0.022 | 18/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 5 µM |  | **0.758×** | -3.6 | 0.022 | 18/46 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.869× | -3.5 | 0.029 | 12/48 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.872× | -3.4 | 0.035 | 16/48 (SW1417, AN3 CA, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.804×** | -3.4 | 0.035 | 21/48 (SNU-1, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.874× | -3.3 | 0.037 | 17/48 (SHP-77, AsPC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.963× | -3.3 | 0.042 | 0/50 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.784×** | -3.1 | 0.063 | 18/48 (LOX-IMVI, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.915× | -3.1 | 0.067 | 6/48 (SW 900, RPMI-7951, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **0.824×** | -3.0 | 0.081 | 14/48 (NCI-H661, SW 900, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6729. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 96.5 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -13.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 114 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.421× (z -13.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 103 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.355× (z -12.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.497× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.401× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HOP62 (line)]] | alt | 80.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +15.6) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.526× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[LOX-IMVI (line)]] | wt | 92.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.423× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.280× (z -8.8) |
| [[SHP-77 (line)]] | alt | 135 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[C-33 A (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.410× (z -9.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 84.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.06× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LoVo (line)]] | wt | 64.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +24.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 88.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.179× (z -11.1) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 85.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW 1088 (line)]] | alt | 95.1 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0740× (z -10.0) |
| [[SW 900 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW48 (line)]] | wt | 88.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[SW480 (line)]] | alt | 81.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.552× (z -9.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 113 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 95.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 89.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6729), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM1A]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[LTA4H]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[MTX2]] | +0.59 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[IARS2]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[USP3]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[TSNAX]] | +0.56 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[ANAPC4]] | +0.55 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[FZD3]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[SLC25A30]] | +0.55 | +0.32 / +0.63 | both halves | 2e-04 |  |
| [[CIAO2A]] | +0.54 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[NAPB]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[BBS2]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF274]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[CLCF1]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[RASAL2]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[AGAP6]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[SETX]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[C11orf91]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[CYTH2]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[SMURF1]] | -0.50 | -0.24 / -0.59 | both halves | 5e-04 |  |
| [[ZNF75A]] | -0.50 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[EXOC8]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[CRK]] | -0.49 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[SAP30BP]] | -0.49 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-5.7, -8.9); signed map (-32.6, -14.5). **Vector** length 92.8, 20.2% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.3 | +5.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +1.1 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -6.3 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.6 | -6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.9 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -2.8 | -3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,612,006-151,699,091 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MY014, KIAA0488, MGC20471 |
| Gene groups (HGNC) | Sorting nexins; PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96L92](https://www.uniprot.org/uniprotkb/Q96L92) (Sorting nexin-27):

> Involved in the retrograde transport from endosome to plasma membrane, a trafficking pathway that promotes the recycling of internalized transmembrane proteins. Following internalization, endocytosed transmembrane proteins are delivered to early endosomes and recycled to the plasma membrane instead of being degraded in lysosomes. SNX27 specifically binds and directs sorting of a subset of transmembrane proteins containing a PDZ-binding motif at the C-terminus: following interaction with target …

**Summary**, from NCBI Gene [81609](https://www.ncbi.nlm.nih.gov/gene/81609):

> This gene encodes a member of the sorting nexin family, a diverse group of cytoplasmic and membrane-associated proteins involved in endocytosis of plasma membrane receptors and protein trafficking through these compartments. All members of this protein family contain a phosphoinositide binding domain (PX domain). A highly similar protein in mouse is responsible for the specific recruitment of an isoform of serotonin 5-hydroxytryptamine 4 receptor into early endosomes, suggesting the analogous …

**Accessions** — [HGNC:20073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20073) · Entrez [81609](https://www.ncbi.nlm.nih.gov/gene/81609) · UniProt [Q96L92](https://www.uniprot.org/uniprotkb/Q96L92) · Ensembl [ENSG00000143376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143376)

## Data

Gene col 6729: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6729); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6729, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6729]; `tensor/DDL_lfc|DDL_z.npy` [6729]; `embed/gene_vectors.npy` [6729]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6729 or target_col == 6729). Every well: [[SNX27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
