---
symbol: "GLRX2"
type: "gene"
col: 347
ensembl_id: "ENSG00000023572"
name: "glutaredoxin 2"
location: "1q31.2"
module: 11
arm: "+"
pooled_cpm: 10.45
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# GLRX2

*glutaredoxin 2* — 1q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.62× (z +18.3, q 0e+00, up in 40 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Berbamine (dihydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0570×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.109×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0763×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 5 µM in 1 line (C-33 A 0.174×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL58]] (+0.72, fdr 7e-06), [[THAP5]] (+0.64, fdr 7e-06), [[SLC35A4]] (+0.64, fdr 7e-06); moves opposite to [[RCN2]] (-0.69, fdr 7e-06), [[MLEC]] (-0.69, fdr 7e-06), [[SUMF2]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 347.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.62×** | +18.3 | 0e+00 | 40/45 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.11×** | +14.6 | 0e+00 | 44/45 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.97×** | +14.6 | 0e+00 | 39/43 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.48×** | +12.2 | 4e-32 | 43/46 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.22×** | +10.7 | 1e-24 | 39/46 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.95×** | +9.0 | 2e-17 | 24/32 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +8.5 | 2e-15 | 26/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.91×** | +8.3 | 5e-15 | 16/20 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.83×** | +8.1 | 4e-14 | 32/47 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.80×** | +7.9 | 2e-13 | 30/47 (NCI-H460, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +7.4 | 8e-12 | 31/47 (PANC-1, HOP62, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.72×** | +7.3 | 1e-11 | 33/47 (NCI-H460, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.67×** | +6.9 | 3e-10 | 34/47 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +6.8 | 6e-10 | 30/47 (PANC-1, COLO 205, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +5.7 | 4e-07 | 28/45 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +5.5 | 1e-06 | 18/47 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +5.0 | 2e-05 | 19/46 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +4.2 | 6e-04 | 14/47 (NCI-H2347, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.003 | 14/48 (C32, RPMI-7951, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.003 | 11/48 (PANC-1, C32, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.036 | 9/44 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 347.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Berbamine (dihydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0570×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.109×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0763×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 5 µM in 1 line (C-33 A 0.174×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.595× | -3.7 | 0.11 | 11/46 (HT-29, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.769× | -3.6 | 0.11 | 16/47 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Rifaximin (drug)]] 5 µM |  | 0.782× | -3.2 | 0.26 | 9/46 (AsPC-1, A498, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.643× | -3.1 | 0.27 | 7/44 (A-172, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 347. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 19.5 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H460 (line)]] | wt | 16.2 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.69× (z +9.4) | — |
| [[A498 (line)]] | wt | 18.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 10.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +11.9) | — |
| [[A-172 (line)]] | wt | 17.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 6.10 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 8.23 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +11.8) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.109× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 9.04 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 5 µM 0.174× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 7.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 6.91 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0670× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 1 | — | [[Berbamine (dihydrochloride) (drug)]] 0.05 µM 0.0570× (z -9.9) |
| [[HOP62 (line)]] | alt | 7.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 8.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +9.2) | — |
| [[J82 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 4.60 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0763× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +9.6) | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 347), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL58]] | +0.72 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[THAP5]] | +0.64 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[SLC35A4]] | +0.64 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[RPF1]] | +0.64 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[NSUN5]] | +0.64 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[ASNSD1]] | +0.64 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[NME6]] | +0.63 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[TRIM47]] | +0.63 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[METTL18]] | +0.62 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[EIF6]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[THG1L]] | +0.62 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[NSRP1]] | +0.62 | +0.67 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCN2]] | -0.69 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[MLEC]] | -0.69 | -0.71 / -0.64 | both halves | 7e-06 |  |
| [[SUMF2]] | -0.65 | -0.72 / -0.44 | both halves | 3e-05 |  |
| [[TMED4]] | -0.63 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[SMARCD2]] | -0.61 | -0.73 / -0.38 | both halves | 7e-05 |  |
| [[PIGS]] | -0.60 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[CALM3]] | -0.59 | -0.69 / -0.40 | both halves | 4e-05 |  |
| [[GANAB]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[CEP43]] | -0.58 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[PDIA6]] | -0.58 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[SBNO1]] | -0.58 | -0.72 / -0.45 | both halves | 3e-05 |  |
| [[SELENON]] | -0.58 | -0.57 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-31.6, 4.9); signed map (2.0, -21.9). **Vector** length 72.2, 13.1% of its response variance represented; |z| ≥ 3 in 1,006 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +14.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.5 | +14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +18.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +12.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +5.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[Rifaximin (drug)]] 5 µM |  | -0.8 | -3.2 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -0.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | glutaredoxin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.2 — chr1:193,090,866-193,106,114 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRX2, bA101E13.1 |
| Gene groups (HGNC) | Glutaredoxin domain containing |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS18](https://www.uniprot.org/uniprotkb/Q9NS18) (Glutaredoxin-2, mitochondrial):

> Glutathione-dependent oxidoreductase that facilitates the maintenance of mitochondrial redox homeostasis upon induction of apoptosis by oxidative stress. Involved in response to hydrogen peroxide and regulation of apoptosis caused by oxidative stress. Acts as a very efficient catalyst of monothiol reactions because of its high affinity for protein glutathione-mixed disulfides. Can receive electrons not only from glutathione (GSH), but also from thioredoxin reductase supporting both monothiol …

**Summary**, from NCBI Gene [51022](https://www.ncbi.nlm.nih.gov/gene/51022):

> The protein encoded by this gene is a member of the glutaredoxin family of proteins, which maintain cellular thiol homeostasis. These proteins are thiol-disulfide oxidoreductases that use a glutathione-binding site and one or two active cysteines in their active site. This gene undergoes alternative splicing to produce multiple isoforms, one of which is ubiquitously expressed and localizes to mitochondria, where it functions in mitochondrial redox homeostasis and is important for the protection …

**Accessions** — [HGNC:16065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16065) · Entrez [51022](https://www.ncbi.nlm.nih.gov/gene/51022) · UniProt [Q9NS18](https://www.uniprot.org/uniprotkb/Q9NS18) · Ensembl [ENSG00000023572](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023572)

## Data

Gene col 347: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 347); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 347, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 347]; `tensor/DDL_lfc|DDL_z.npy` [347]; `embed/gene_vectors.npy` [347]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 347 or target_col == 347). Every well: [[GLRX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLRX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
