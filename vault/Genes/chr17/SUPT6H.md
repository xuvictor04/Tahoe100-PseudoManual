---
symbol: "SUPT6H"
type: "gene"
col: 3030
ensembl_id: "ENSG00000109111"
name: "SPT6 homolog, histone chaperone and transcription elongation factor"
location: "17q11.2"
module: 11
arm: "+"
pooled_cpm: 159.14
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# SUPT6H

*SPT6 homolog, histone chaperone and transcription elongation factor* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.24× (z +27.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.822× (z -4.7, q 0.002, down in 22 of 49 measured lines) ⚠ cell-cycle shift, explains ~14% of this change. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 0.785× (z -4.1, q 0.010, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2F1]] (+0.69, fdr 7e-06), [[USP16]] (+0.62, fdr 7e-06), [[CDK12]] (+0.61, fdr 1e-05); moves opposite to [[METAP1]] (-0.56, fdr 1e-05), [[RYK]] (-0.56, fdr 1e-05), [[ZNF706]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3030.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.24×** | +27.0 | 0e+00 | 47/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.65×** | +21.4 | 0e+00 | 47/49 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +17.0 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +16.6 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.97×** | +16.0 | 0e+00 | 48/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.51×** | +15.5 | 0e+00 | 44/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +14.5 | 0e+00 | 44/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.89×** | +14.3 | 3e-44 | 47/48 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.79×** | +13.8 | 3e-41 | 47/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +12.3 | 5e-33 | 43/48 (HT-29, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +9.0 | 1e-17 | 36/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +8.2 | 1e-14 | 36/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.26×** | +7.7 | 5e-13 | 28/49 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +7.4 | 5e-12 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +7.0 | 1e-10 | 32/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +6.5 | 4e-09 | 40/49 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.3 | 0.027 | 15/48 (KATO III, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3030.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.822×** | -4.7 | 0.002 | 22/49 (SW480, hTERT-HPNE, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.785×** | -4.1 | 0.010 | 26/47 (SW48, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.844× | -4.0 | 0.010 | 21/49 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.844× | -3.9 | 0.015 | 19/47 (SW 900, HT-29, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.853× | -3.8 | 0.017 | 13/49 (SW480, HS-578T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.895× | -3.7 | 0.018 | 7/48 (A-172, H4, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.868× | -3.4 | 0.059 | 9/48 (C32, AN3 CA, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.834× | -3.1 | 0.14 | 14/48 (H4, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 0.880× | -3.1 | 0.14 | 12/48 (H4, HOP62, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.881× | -3.0 | 0.14 | 9/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 147 | 16 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +26.2) | — |
| [[NCI-H460 (line)]] | wt | 165 | 15 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +22.4) | — |
| [[SW480 (line)]] | alt | 160 | 14 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +20.4) | — |
| [[HEC-1-A (line)]] | alt | 171 | 12 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +17.3) | — |
| [[LoVo (line)]] | wt | 121 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +18.4) | — |
| [[A-172 (line)]] | wt | 204 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +22.3) | — |
| [[BT-474 (line)]] | alt | 148 | 10 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.35× (z +13.5) | — |
| [[HOP62 (line)]] | alt | 160 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +23.2) | — |
| [[LOX-IMVI (line)]] | wt | 164 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +20.8) | — |
| [[LS 180 (line)]] | wt | 124 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +17.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 183 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +17.7) | — |
| [[SNU-1 (line)]] | wt | 121 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 152 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +18.6) | — |
| [[KATO III (line)]] | alt | 201 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +15.1) | — |
| [[SW48 (line)]] | wt | 133 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 126 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +18.3) | — |
| [[Panc 03.27 (line)]] | alt | 193 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +16.0) | — |
| [[RKO (line)]] | wt | 168 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +16.1) | — |
| [[A-427 (line)]] | wt | 107 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.4) | — |
| [[COLO 205 (line)]] | alt | 186 | 7 | 0 | [[TAK-901 (drug)]] 5 µM 12.6× (z +14.9) | — |
| [[NCI-H1792 (line)]] | alt | 170 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +14.9) | — |
| [[NCI-H2347 (line)]] | alt | 148 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.5) | — |
| [[SW 900 (line)]] | alt | 138 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +15.2) | — |
| [[SW1417 (line)]] | alt | 153 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +14.1) | — |
| [[A549 (line)]] | wt | 205 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +21.6) | — |
| [[AsPC-1 (line)]] | alt | 124 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +18.2) | — |
| [[C32 (line)]] | wt | 121 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.6) | — |
| [[J82 (line)]] | alt | 141 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +18.0) | — |
| [[NCI-H1573 (line)]] | alt | 156 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +16.5) | — |
| [[HepG2_C3A (line)]] | wt | 128 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +14.1) | — |
| [[A498 (line)]] | wt | 211 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +16.3) | — |
| [[NCI-H2030 (line)]] | alt | 194 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 210 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +15.6) | — |
| [[RPMI-7951 (line)]] | alt | 176 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +14.2) | — |
| [[SK-MEL-2 (line)]] | alt | 140 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +15.5) | — |
| [[SNU-423 (line)]] | alt | 159 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +20.2) | — |
| [[CFPAC-1 (line)]] | alt | 143 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.7) | — |
| [[H4 (line)]] | wt | 188 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 183 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 112 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +18.5) | — |
| [[hTERT-HPNE (line)]] | wt | 157 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 143 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.81× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 151 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.4) | — |
| [[CHP-212 (line)]] | wt | 168 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 165 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2F1]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; STRING 414 |
| [[USP16]] | +0.62 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[CDK12]] | +0.61 | +0.65 / +0.50 | both halves | 1e-05 | STRING 882 |
| [[USP8]] | +0.61 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[CSNK1A1]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[DDX27]] | +0.60 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[DNAJC7]] | +0.60 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[TAF2]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[DHX38]] | +0.59 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[TOX4]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[DNAJB12]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[TRIM39]] | +0.59 | +0.58 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | -0.56 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[RYK]] | -0.56 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ZNF706]] | -0.55 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[USP3]] | -0.54 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[TMEM131L]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PALS2]] | -0.53 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[FDX1]] | -0.53 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[SYPL1]] | -0.53 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[BTBD3]] | -0.52 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[GCSH]] | -0.52 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[MTX2]] | -0.52 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ILKAP]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.317). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-21.5, 12.2); signed map (-3.0, -12.6). **Vector** length 109, 37.1% of its response variance represented; |z| ≥ 3 in 1,256 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.0 | +14.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.2 | +16.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +12.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +13.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +5.9 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +6.5 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | +3.4 | +1.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.1 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.6 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | SPT6 homolog, histone chaperone and transcription elongation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,662,198-28,702,679 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0162, SPT6H |
| Gene groups (HGNC) | SH2 domain containing |
| Reactome | 7 pathways, smallest: Formation of RNA Pol II elongation complex; RNA Polymerase II Transcription Elongation; RNA Polymerase II Pre-transcription Events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7KZ85](https://www.uniprot.org/uniprotkb/Q7KZ85) (Transcription elongation factor SPT6):

> Histone H3-H4 chaperone that plays a key role in the regulation of transcription elongation and mRNA processing. Enhances the transcription elongation by RNA polymerase II (RNAPII) and is also required for the efficient activation of transcriptional elongation by the HIV-1 nuclear transcriptional activator, Tat. Besides chaperoning histones in transcription, acts to transport and splice mRNA by forming a complex with IWS1 and the C-terminal domain (CTD) of the RNAPII subunit RPB1 (POLR2A). The …

**Summary**, from NCBI Gene [6830](https://www.ncbi.nlm.nih.gov/gene/6830):

> Enables histone binding activity. Involved in transcription elongation-coupled chromatin remodeling. Predicted to be located in nucleoplasm. Predicted to be part of transcription elongation factor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11470) · Entrez [6830](https://www.ncbi.nlm.nih.gov/gene/6830) · UniProt [Q7KZ85](https://www.uniprot.org/uniprotkb/Q7KZ85) · Ensembl [ENSG00000109111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109111)

## Data

Gene col 3030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3030); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3030]; `tensor/DDL_lfc|DDL_z.npy` [3030]; `embed/gene_vectors.npy` [3030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3030 or target_col == 3030). Every well: [[SUPT6H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUPT6H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
