---
symbol: "TSN"
type: "gene"
col: 13065
ensembl_id: "ENSG00000211460"
name: "translin"
location: "2q14.3"
module: 20
arm: "+"
pooled_cpm: 40.75
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# TSN

*translin* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.98× (z +13.9, q 6e-41, up in 39 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 3.47× (z +13.2, q 1e-37, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.714× (z -9.8, q 8e-20, down in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.314×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.474×; ⚠ cell-cycle shift, would explain all of this change); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (CHP-212 0.104×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STT3A]] (+0.76, fdr 7e-06), [[EIF3F]] (+0.68, fdr 7e-06), [[VTI1B]] (+0.68, fdr 7e-06); moves opposite to [[IER5]] (-0.64, fdr 7e-06), [[BAIAP2L1]] (-0.60, fdr 2e-05), [[RNF223]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13065.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +13.9 | 6e-41 | 39/46 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.47×** | +13.2 | 1e-37 | 43/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.47×** | +13.2 | 1e-37 | 47/48 (LoVo, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +11.0 | 5e-26 | 30/39 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +8.7 | 3e-16 | 38/48 (LoVo, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +8.0 | 8e-14 | 28/42 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +8.0 | 1e-13 | 35/47 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +6.1 | 9e-08 | 24/48 (HEC-1-A, NCI-H1792, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +5.3 | 9e-06 | 21/48 (J82, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +5.1 | 2e-05 | 25/47 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[NG25 (drug)]] 5 µM |  | **1.53×** | +4.5 | 3e-04 | 20/47 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.3 | 7e-04 | 15/35 (A-172, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.22×** | +4.1 | 0.002 | 19/47 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.22×** | +4.0 | 0.002 | 19/47 (HT-29, C32, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.8 | 0.005 | 17/48 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.022 | 11/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.18× | +3.2 | 0.046 | 8/48 (AsPC-1, NCI-H460, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.061 | 8/48 (LoVo, NCI-H2030, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.082 | 5/48 (A-427, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +2.9 | 0.093 | 15/47 (HEC-1-A, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13065.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.314×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 0.474×; ⚠ cell-cycle shift, would explain all of this change); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (CHP-212 0.104×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.714×** | -9.8 | 8e-20 | 37/48 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.675×** | -8.0 | 2e-13 | 37/48 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.848× | -3.4 | 0.11 | 10/48 (SNU-1, SW480, …) | all doses, stronger at high dose |  |
| [[Quinestrol (drug)]] 5 µM |  | 0.891× | -3.4 | 0.11 | 7/48 (HEC-1-A, COLO 205, …) | rises with dose |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.848× | -3.3 | 0.12 | 7/48 (AsPC-1, SW48, …) | top dose only | plate-row cell shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.811× | -3.1 | 0.21 | 13/47 (SW480, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 44.4 | 3 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 6.88× (z +11.4) | — |
| [[SW480 (line)]] | alt | 49.5 | 3 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 4.93× (z +10.7) | — |
| [[A549 (line)]] | wt | 28.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +11.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 37.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.12× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -11.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 34.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 58.7 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 6.07× (z +10.3) | — |
| [[A-172 (line)]] | wt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +11.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 32.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.104× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 32.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.31× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 42.0 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 8.71× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +9.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 48.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.16× (z +9.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 38.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 40.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 88.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3A]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[EIF3F]] | +0.68 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[VTI1B]] | +0.68 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[SNRPC]] | +0.68 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[MAGOH]] | +0.67 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[PRPF8]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[DERL1]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ZMPSTE24]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[RPN1]] | +0.62 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[SUPV3L1]] | +0.61 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PMS2]] | +0.61 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[DDOST]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER5]] | -0.64 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[BAIAP2L1]] | -0.60 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[RNF223]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[PPP1R13B]] | -0.55 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[MIDN]] | -0.55 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[NBPF14]] | -0.54 | -0.34 / -0.65 | both halves | 1e-04 |  |
| [[EIF1B]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ORAI1]] | -0.54 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[SLC25A37]] | -0.54 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[ZSWIM4]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[METTL23]] | -0.53 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[HES4]] | -0.53 | -0.38 / -0.59 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-20.9, -15.6); signed map (-32.6, -26.7). **Vector** length 98.2, 23.4% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.3 | +13.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.2 | +13.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +11.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +8.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.2 | +0.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.8 | -9.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -8.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | translin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:121,737,103-121,767,853 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRSLN, BCLF-1, REHF-1 |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 2 pathways, smallest: Small interfering RNA (siRNA) biogenesis; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15631](https://www.uniprot.org/uniprotkb/Q15631) (Translin):

> DNA-binding protein that specifically recognizes consensus sequences at the breakpoint junctions in chromosomal translocations, mostly involving immunoglobulin (Ig)/T-cell receptor gene segments. Seems to recognize single-stranded DNA ends generated by staggered breaks occurring at recombination hot spots.; As part of the Translin-TRAX complex, participates in the activation of the RNA-induced silencing complex (RISC) by degrading siRNA passenger strand cleavage products. Within the complex, …

**Summary**, from NCBI Gene [7247](https://www.ncbi.nlm.nih.gov/gene/7247):

> This gene encodes a DNA-binding protein which specifically recognizes conserved target sequences at the breakpoint junction of chromosomal translocations. Translin polypeptides form a multimeric structure that is responsible for its DNA-binding activity. Recombination-associated motifs and translin-binding sites are present at recombination hotspots and may serve as indicators of breakpoints in genes which are fused by translocations. These binding activities may play a crucial role in …

**Accessions** — [HGNC:12379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12379) · Entrez [7247](https://www.ncbi.nlm.nih.gov/gene/7247) · UniProt [Q15631](https://www.uniprot.org/uniprotkb/Q15631) · Ensembl [ENSG00000211460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000211460)

## Data

Gene col 13065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13065); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13065]; `tensor/DDL_lfc|DDL_z.npy` [13065]; `embed/gene_vectors.npy` [13065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13065 or target_col == 13065). Every well: [[TSN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
