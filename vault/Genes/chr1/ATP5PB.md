---
symbol: "ATP5PB"
type: "gene"
col: 3796
ensembl_id: "ENSG00000116459"
name: "ATP synthase peripheral stalk-membrane subunit b"
location: "1p13.2"
module: 28
arm: "+"
pooled_cpm: 39.88
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ATP5PB

*ATP synthase peripheral stalk-membrane subunit b* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.48× (z +16.6, q 0e+00, up in 45 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.26× (z +4.3, q 8e-04, up in 25 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[venetoclax (drug)]] 0.05 µM in 1 line (CHP-212 0.0610×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GUF1]] (+0.68, fdr 7e-06), [[TRUB1]] (+0.66, fdr 7e-06), [[MCCC2]] (+0.65, fdr 7e-06); moves opposite to [[CDC34]] (-0.64, fdr 1e-05), [[FRMD8]] (-0.61, fdr 1e-05), [[LGI4]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 13 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.48×** | +16.6 | 0e+00 | 45/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.35×** | +15.5 | 0e+00 | 36/39 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.74×** | +12.4 | 4e-33 | 39/43 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.62×** | +6.4 | 2e-08 | 36/48 (NCI-H1573, C32, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.46×** | +5.1 | 5e-05 | 27/47 (NCI-H23, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.41×** | +4.6 | 4e-04 | 29/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.43×** | +4.6 | 4e-04 | 31/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +4.5 | 4e-04 | 28/48 (NCI-H1573, PANC-1, …) | two highest doses | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.90×** | +4.5 | 5e-04 | 34/48 (A498, KATO III, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.3 | 8e-04 | 25/48 (A-172, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.7 | 0.010 | 25/46 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.64×** | +3.5 | 0.025 | 25/47 (SK-MEL-2, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.4 | 0.028 | 24/48 (NCI-H2347, C32, …) | top dose only | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.052 | 20/45 (MIA PaCa-2, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.094 | 21/48 (HS-578T, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3796.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[venetoclax (drug)]] 0.05 µM in 1 line (CHP-212 0.0610×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.849× | -3.1 | 0.72 | 14/48 (KATO III, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 27.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 38.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +14.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 28.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.80× (z +13.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 41.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 44.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 55.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +12.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 49.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +12.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +13.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 30.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +15.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 37.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +15.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 34.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 50.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +12.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 27.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.41× (z +11.3) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 32.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.43× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 24.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +11.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 61.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 51.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.4) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 39.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +11.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 38.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +10.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 44.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 27.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 37.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 84.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +11.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 42.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 50.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +12.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 1 | — | [[venetoclax (drug)]] 0.05 µM 0.0610× (z -8.6) |
| [[LS 180 (line)]] | wt | 56.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 43.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +9.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 41.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +9.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 48.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 31.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUF1]] | +0.68 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[TRUB1]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[MCCC2]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[MTMR2]] | +0.64 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[NCOA4]] | +0.63 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[AGL]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[SNX17]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[USP40]] | +0.61 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[FAM204A]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[MRPL30]] | +0.61 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[FUNDC1]] | +0.60 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[NDUFB5]] | +0.60 | +0.64 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 954 |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC34]] | -0.64 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[FRMD8]] | -0.61 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[LGI4]] | -0.60 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[CORO7]] | -0.60 | -0.68 / -0.41 | both halves | 4e-05 |  |
| [[RBM38]] | -0.59 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[PLIN3]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PHF1]] | -0.58 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[STK32C]] | -0.57 | -0.63 / -0.46 | both halves | 3e-05 | STRING 463 |
| [[LDLRAP1]] | -0.57 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[CSNK1E]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 | pathway: Organelle biogenesis and maintenance |
| [[ULK1]] | -0.56 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[TMEM184B]] | -0.55 | -0.49 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.4, 5.4); signed map (14.7, -34.0). **Vector** length 72.3, 17.1% of its response variance represented; |z| ≥ 3 in 661 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +3.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.4 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.4 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +16.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.5 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.2 | +0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase peripheral stalk-membrane subunit b |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:111,448,864-111,462,773 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ATP5F1 |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P24539](https://www.uniprot.org/uniprotkb/P24539) (ATP synthase peripheral stalk subunit b, mitochondrial):

> Subunit b, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain. ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and a stationary …

**Summary**, from NCBI Gene [515](https://www.ncbi.nlm.nih.gov/gene/515):

> This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic portion of mitochondrial ATP synthase consists of 5 different subunits (alpha, beta, gamma, …

**Accessions** — [HGNC:840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:840) · Entrez [515](https://www.ncbi.nlm.nih.gov/gene/515) · UniProt [P24539](https://www.uniprot.org/uniprotkb/P24539) · Ensembl [ENSG00000116459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116459)

## Data

Gene col 3796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3796); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3796]; `tensor/DDL_lfc|DDL_z.npy` [3796]; `embed/gene_vectors.npy` [3796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3796 or target_col == 3796). Every well: [[ATP5PB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5PB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
