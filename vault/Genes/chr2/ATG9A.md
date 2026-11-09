---
symbol: "ATG9A"
type: "gene"
col: 12741
ensembl_id: "ENSG00000198925"
name: "autophagy related 9A"
location: "2q35"
module: 2
arm: "+"
pooled_cpm: 21.03
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ATG9A

*autophagy related 9A* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +15.9, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.727× (z -5.1, q 2e-04, down in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.122×, C32 0.240×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.140×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C32 0.216×; ⚠ toxic; cell-cycle shift, explains ~71% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.0879×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TESK1]] (+0.65, fdr 1e-05), [[PRAF2]] (+0.62, fdr 1e-05), [[ANKZF1]] (+0.61, fdr 7e-06, ⚠ same locus), [[GUCD1]] (+0.58, fdr 1e-05); moves opposite to [[BRIX1]] (-0.56, fdr 1e-05), [[UTP14A]] (-0.55, fdr 1e-05), [[AGK]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12741.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +15.9 | 0e+00 | 42/47 (NCI-H2030, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +7.3 | 8e-11 | 31/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +7.1 | 2e-10 | 32/48 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.46×** | +6.2 | 6e-08 | 28/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +5.5 | 5e-06 | 28/48 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +5.1 | 3e-05 | 25/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.36×** | +5.0 | 5e-05 | 24/45 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.34×** | +4.8 | 1e-04 | 23/47 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.6 | 2e-04 | 21/47 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +4.4 | 5e-04 | 22/47 (CFPAC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.3 | 1e-03 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.29×** | +4.1 | 0.002 | 17/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.26×** | +3.8 | 0.007 | 15/47 (NCI-H460, LoVo, …) | rises with dose | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.5 | 0.020 | 8/37 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.062 | 11/44 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.089 | 12/46 (Panc 03.27, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12741.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.122×, C32 0.240×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.140×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C32 0.216×; ⚠ toxic; cell-cycle shift, explains ~71% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.0879×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.727×** | -5.1 | 2e-04 | 25/47 (PANC-1, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.783×** | -4.1 | 0.012 | 20/46 (MIA PaCa-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12741. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 34.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.216× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 24.2 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +12.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 21.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 16.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 15.4 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +10.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[C-33 A (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.197× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~9% of this change |
| [[H4 (line)]] | wt | 21.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0879× (z -11.3) |
| [[Hs 766T (line)]] | wt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +8.8) | — |
| [[LoVo (line)]] | wt | 17.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 18.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 35.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12741), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TESK1]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[PRAF2]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[ANKZF1]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[RETREG2]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 | ⚠ same locus (33.9 kb: neighbours can correlate without regulation) |
| [[ABCB6]] | +0.58 | +0.54 / +0.54 | both halves | 1e-05 | ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[GUCD1]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[RAB5B]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[NLGN2]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[BCL2L2]] | +0.57 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[CRAT]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[NARF]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[TP53I13]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[SBF1]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[RELL2]] | +0.55 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRIX1]] | -0.56 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[UTP14A]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[AGK]] | -0.54 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[RRP15]] | -0.54 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[CEP83]] | -0.53 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[ZNHIT6]] | -0.53 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[RIOK1]] | -0.52 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[PAK1IP1]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TCERG1]] | -0.51 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[WDR35]] | -0.50 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[RBM28]] | -0.50 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[NBN]] | -0.50 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.422). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (4.0, -37.2); signed map (-22.4, 9.4). **Vector** length 86.8, 17.5% of its response variance represented; |z| ≥ 3 in 785 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +15.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | +3.9 | +5.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +7.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.0 | +3.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.3 | +1.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +0.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 9A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,219,380-219,229,717 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22169; previously APG9L1 |
| Gene groups (HGNC) | Autophagy related |
| Reactome | 5 pathways, smallest: PINK1-PRKN Mediated Mitophagy; Mitophagy; Selective autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3C6](https://www.uniprot.org/uniprotkb/Q7Z3C6) (Autophagy-related protein 9A):

> Phospholipid scramblase involved in autophagy by mediating autophagosomal membrane expansion. Cycles between the preautophagosomal structure/phagophore assembly site (PAS) and the cytoplasmic vesicle pool and supplies membrane for the growing autophagosome. Lipid scramblase activity plays a key role in preautophagosomal structure/phagophore assembly by distributing the phospholipids that arrive through ATG2 (ATG2A or ATG2B) from the cytoplasmic to the luminal leaflet of the bilayer, thereby …

**Summary**, from NCBI Gene [79065](https://www.ncbi.nlm.nih.gov/gene/79065):

> Enables phospholipid scramblase activity. Involved in autophagosome assembly. Located in several cellular components, including Golgi apparatus; endosome; and phagophore assembly site. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22408) · Entrez [79065](https://www.ncbi.nlm.nih.gov/gene/79065) · UniProt [Q7Z3C6](https://www.uniprot.org/uniprotkb/Q7Z3C6) · Ensembl [ENSG00000198925](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198925)

## Data

Gene col 12741: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12741); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12741, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12741]; `tensor/DDL_lfc|DDL_z.npy` [12741]; `embed/gene_vectors.npy` [12741]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12741 or target_col == 12741). Every well: [[ATG9A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG9A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
