---
symbol: "INTS11"
type: "gene"
col: 4785
ensembl_id: "ENSG00000127054"
name: "integrator complex subunit 11"
location: "1p36.33"
module: 2
arm: "+"
pooled_cpm: 20.33
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# INTS11

*integrator complex subunit 11* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.55× (z +16.5, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.797× (z -5.4, q 4e-05, down in 23 of 47 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.208×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.147×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.278×; ⚠ cell-cycle shift, explains ~57% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABHD17A]] (+0.78, fdr 7e-06), [[ZDHHC8]] (+0.77, fdr 7e-06), [[CPSF1]] (+0.75, fdr 7e-06); moves opposite to [[BAZ2B]] (-0.65, fdr 2e-05), [[LINC02307]] (-0.65, fdr 2e-05), [[PBDC1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4785.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.55×** | +16.5 | 0e+00 | 45/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.40×** | +15.4 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.27×** | +14.4 | 2e-44 | 44/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +7.3 | 4e-11 | 30/44 (NCI-H1573, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +6.8 | 2e-09 | 23/39 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.5 | 8e-09 | 24/43 (NCI-H23, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.92×** | +6.0 | 2e-07 | 24/48 (LS 180, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +5.9 | 2e-07 | 28/48 (PANC-1, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.86×** | +5.7 | 8e-07 | 21/46 (KATO III, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +5.5 | 2e-06 | 25/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +5.1 | 2e-05 | 16/28 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +5.0 | 3e-05 | 18/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 3e-05 | 15/46 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.32×** | +4.8 | 5e-05 | 21/48 (J82, LS 180, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.31×** | +4.4 | 4e-04 | 18/47 (HEC-1-A, SW48, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 4e-04 | 19/46 (NCI-H23, AsPC-1, …) | two highest doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.009 | 7/48 (NCI-H2030, CFPAC-1, …) | two highest doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.010 | 12/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.013 | 13/48 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.020 | 6/45 (HT-29, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.025 | 12/46 (SK-MEL-2, HOP62, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.036 | 7/47 (HT-29, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4785.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.208×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.147×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.278×; ⚠ cell-cycle shift, explains ~57% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.797×** | -5.4 | 4e-05 | 23/47 (SK-MEL-2, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.802×** | -3.8 | 0.049 | 14/48 (NCI-H2347, NCI-H23, …) | rises with dose | composition shift; position effect removed |
| [[Verapamil (drug)]] 5 µM |  | 0.838× | -3.0 | 0.45 | 9/47 (C32, SW 1271, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 19.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.10× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[SW480 (line)]] | alt | 24.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +14.1) | — |
| [[A-427 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -9.3) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HEC-1-A (line)]] | alt | 29.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 21.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 23.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.46× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.127× (z -8.5) ⚠ toxic |
| [[SW48 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD17A]] | +0.78 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[ZDHHC8]] | +0.77 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[CPSF1]] | +0.75 | +0.69 / +0.67 | both halves | 7e-06 | same gene group; STRING 808 |
| [[SBF1]] | +0.74 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[WDR5]] | +0.73 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[ABCA2]] | +0.73 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[STK25]] | +0.72 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | +0.70 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[KLHL17]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[NOMO2]] | +0.69 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[SH3GLB2]] | +0.68 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[FBXW2]] | +0.68 | +0.69 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.65 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[LINC02307]] | -0.65 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[PBDC1]] | -0.65 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[ANKRD26]] | -0.63 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[SCAF11]] | -0.62 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[MICOS10]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.61 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PATL2]] | -0.61 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[TRIP11]] | -0.61 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[NIPBL]] | -0.60 | -0.44 / -0.53 | both halves | 3e-05 | STRING 752 |
| [[TMEM35B]] | -0.60 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[TCEAL4]] | -0.59 | -0.54 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.789). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.7, -23.4); signed map (-45.1, -10.5). **Vector** length 80.8, 15.2% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | +5.3 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +6.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +5.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +4.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +0.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.9 | -3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.9 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -4.4 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -0.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,311,585-1,324,687 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20542, RC-68, CPSF73L, INT11; previously CPSF3L |
| Gene groups (HGNC) | Integrator complex; MBL fold containing DNA/RNA interacting subfamily; MicroRNA protein coding host genes |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TA45](https://www.uniprot.org/uniprotkb/Q5TA45) (Integrator complex subunit 11):

> RNA endonuclease component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol …

**Summary**, from NCBI Gene [54973](https://www.ncbi.nlm.nih.gov/gene/54973):

> The Integrator complex contains at least 12 subunits and associates with the C-terminal domain of RNA polymerase II large subunit (POLR2A; MIM 180660) and mediates the 3-prime end processing of small nuclear RNAs U1 (RNU1; MIM 180680) and U2 (RNU2; MIM 180690). INTS11, or CPSF3L, is the catalytic subunit of the Integrator complex (Baillat et al., 2005 [PubMed 16239144]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26052) · Entrez [54973](https://www.ncbi.nlm.nih.gov/gene/54973) · UniProt [Q5TA45](https://www.uniprot.org/uniprotkb/Q5TA45) · Ensembl [ENSG00000127054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127054)

## Data

Gene col 4785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4785); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4785]; `tensor/DDL_lfc|DDL_z.npy` [4785]; `embed/gene_vectors.npy` [4785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4785 or target_col == 4785). Every well: [[INTS11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
