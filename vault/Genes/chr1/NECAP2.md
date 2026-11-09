---
symbol: "NECAP2"
type: "gene"
col: 8049
ensembl_id: "ENSG00000157191"
name: "NECAP endocytosis associated 2"
location: "1p36.13"
module: 11
arm: "+"
pooled_cpm: 23.59
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# NECAP2

*NECAP endocytosis associated 2* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +18.2, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.748× (z -5.3, q 8e-05, down in 16 of 32 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (RPMI-7951 0.103×, SW480 0.302×, LoVo 0.225×, HT-29 0.227×, …; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.140×, NCI-H23 0.239×, SK-MEL-2 0.280×; ⚠ cell-cycle shift, explains ~41% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.111×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Futibatinib (drug)]] 5 µM in 1 line (Hs 766T 0.0750×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FNTA]] (+0.73, fdr 7e-06), [[CIDECP1]] (+0.69, fdr 7e-06), [[TSG101]] (+0.68, fdr 7e-06); moves opposite to [[STT3B]] (-0.62, fdr 7e-06), [[LDHB]] (-0.62, fdr 1e-05), [[GMPS]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8049.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +18.2 | 0e+00 | 42/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.19×** | +14.2 | 2e-43 | 40/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +12.0 | 8e-31 | 38/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +10.3 | 1e-22 | 38/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +7.6 | 3e-12 | 31/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +6.4 | 1e-08 | 25/48 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +5.9 | 3e-07 | 24/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +5.7 | 7e-07 | 24/47 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +5.3 | 6e-06 | 21/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 3e-04 | 16/48 (HOP62, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 6e-04 | 19/47 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 8e-04 | 12/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 9e-04 | 16/48 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.2 | 1e-03 | 16/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.24×** | +4.0 | 0.002 | 13/47 (SW1417, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.0 | 0.003 | 13/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.009 | 9/47 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.030 | 15/48 (HEC-1-A, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8049.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (RPMI-7951 0.103×, SW480 0.302×, LoVo 0.225×, HT-29 0.227×, …; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.140×, NCI-H23 0.239×, SK-MEL-2 0.280×; ⚠ cell-cycle shift, explains ~41% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.111×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Futibatinib (drug)]] 5 µM in 1 line (Hs 766T 0.0750×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.748×** | -5.3 | 8e-05 | 16/32 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.786×** | -4.6 | 0.002 | 18/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.830×** | -3.5 | 0.059 | 16/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.878× | -3.5 | 0.059 | 13/48 (CFPAC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -3.4 | 0.059 | 1/48 (SW 1088) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.834× | -3.4 | 0.059 | 12/47 (SNU-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.05 µM |  | 0.841× | -3.0 | 0.21 | 8/47 (NCI-H661, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +19.6) | — |
| [[NCI-H460 (line)]] | wt | 15.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 29.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 21.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 17.1 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.64× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -10.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 21.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -12.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -10.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A549 (line)]] | wt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 41.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.111× (z -14.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 40.0 | 0 | 1 | — | [[Futibatinib (drug)]] 5 µM 0.0750× (z -11.5) |
| [[HS-578T (line)]] | alt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 29.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -12.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[J82 (line)]] | alt | 35.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -11.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2347 (line)]] | alt | 24.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -14.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -9.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNTA]] | +0.73 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[CIDECP1]] | +0.69 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[TSG101]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[SLC31A2]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[MED18]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[THAP1]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[DPF2]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ZFP90]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[DNAL4]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[TJAP1]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | +0.60 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[ZNF197]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3B]] | -0.62 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[LDHB]] | -0.62 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[GMPS]] | -0.59 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[PAICS]] | -0.58 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[LAPTM4B]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[GPC4]] | -0.57 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[NDC1]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[PTDSS1]] | -0.56 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[TMTC4]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[PMS1]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[TTC13]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ADAM15]] | -0.55 | -0.53 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.6, -0.2); signed map (1.4, -13.0). **Vector** length 86.7, 17.1% of its response variance represented; |z| ≥ 3 in 839 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.8 | +18.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +12.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +14.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +5.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | -2.4 | -3.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | NECAP endocytosis associated 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:16,440,721-16,460,078 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10420 |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVZ3](https://www.uniprot.org/uniprotkb/Q9NVZ3) (Adaptin ear-binding coat-associated protein 2):

> Involved in endocytosis.

**Summary**, from NCBI Gene [55707](https://www.ncbi.nlm.nih.gov/gene/55707):

> This gene likely encodes a member of the adaptin-ear-binding coat-associated protein family. Studies of a similar protein in rat suggest a role in clathrin-mediated endocytosis. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:25528](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25528) · Entrez [55707](https://www.ncbi.nlm.nih.gov/gene/55707) · UniProt [Q9NVZ3](https://www.uniprot.org/uniprotkb/Q9NVZ3) · Ensembl [ENSG00000157191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157191)

## Data

Gene col 8049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8049); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8049]; `tensor/DDL_lfc|DDL_z.npy` [8049]; `embed/gene_vectors.npy` [8049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8049 or target_col == 8049). Every well: [[NECAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NECAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
