---
symbol: "PDK1"
type: "gene"
col: 7610
ensembl_id: "ENSG00000152256"
name: "pyruvate dehydrogenase kinase 1"
location: "2q31.1"
module: 99
arm: "+"
pooled_cpm: 220.44
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 30
n_dd_up_clean: 12
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# PDK1

*pyruvate dehydrogenase kinase 1* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.54× (z +7.6, q 2e-11, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.265× (z -21.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDK3]] (+0.82, fdr 7e-06), [[HERC3]] (+0.78, fdr 7e-06), [[INSIG2]] (+0.77, fdr 7e-06); moves opposite to [[ZNF274]] (-0.65, fdr 1e-05), [[ZNF140]] (-0.59, fdr 3e-05), [[RBMXL1]] (-0.58, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7610.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.54×** | +7.6 | 2e-11 | 46/49 (C32, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +6.0 | 4e-07 | 35/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **2.48×** | +5.4 | 1e-05 | 43/48 (HT-29, SW480, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.35×** | +5.1 | 5e-05 | 42/48 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.31×** | +5.0 | 6e-05 | 28/38 (NCI-H1573, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.009 | 32/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.8 | 0.012 | 30/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.027 | 37/48 (SHP-77, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.035 | 28/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.76×** | +3.4 | 0.043 | 36/48 (NCI-H2030, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.045 | 30/49 (PANC-1, HT-29, …) | top dose only | plate-row cell shift |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.058 | 32/48 (PANC-1, HepG2/C3A, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.072 | 31/49 (C-33 A, SHP-77, …) | top dose only |  |
| [[Lonafarnib (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.077 | 29/48 (SW48, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7610.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.265×** | -21.5 | 0e+00 | 48/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.328×** | -12.2 | 5e-32 | 43/44 (SK-MEL-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.370×** | -10.9 | 2e-25 | 40/48 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.389×** | -10.8 | 6e-25 | 48/49 (NCI-H23, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.397×** | -10.6 | 5e-24 | 40/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.467×** | -8.4 | 6e-15 | 45/47 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.476×** | -8.2 | 3e-14 | 45/47 (C-33 A, HT-29, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.502×** | -7.9 | 2e-13 | 46/48 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.505×** | -7.8 | 4e-13 | 45/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.675×** | -6.4 | 1e-08 | 46/48 (AN3 CA, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.680×** | -6.2 | 2e-08 | 37/49 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.702×** | -5.7 | 5e-07 | 39/48 (C32, HepG2/C3A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.651×** | -4.9 | 4e-05 | 44/48 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.661×** | -4.7 | 9e-05 | 41/48 (C32, RPMI-7951, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.676×** | -4.5 | 3e-04 | 41/48 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.684×** | -4.3 | 5e-04 | 36/48 (C32, HCT15, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.726×** | -3.7 | 0.009 | 38/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.735×** | -3.5 | 0.014 | 31/48 (hTERT-HPNE, A-172, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.737×** | -3.5 | 0.015 | 40/48 (NCI-H2347, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.747×** | -3.3 | 0.024 | 35/49 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.748×** | -3.3 | 0.024 | 32/49 (HT-29, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 448 | 2 | 11 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 7.44× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -25.4) |
| [[NCI-H460 (line)]] | wt | 408 | 4 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -31.2) |
| [[HEC-1-A (line)]] | alt | 188 | 1 | 7 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.96× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -18.1) |
| [[LOX-IMVI (line)]] | wt | 439 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0928× (z -27.2) |
| [[SW480 (line)]] | alt | 186 | 1 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -18.7) |
| [[KATO III (line)]] | alt | 148 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -19.8) |
| [[NCI-H1573 (line)]] | alt | 257 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.44× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -24.0) |
| [[NCI-H1792 (line)]] | alt | 232 | 4 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.35× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -10.6) |
| [[C-33 A (line)]] | alt | 259 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -15.6) |
| [[HT-29 (line)]] | alt | 177 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -21.1) |
| [[MIA PaCa-2 (line)]] | alt | 287 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0978× (z -29.0) |
| [[NCI-H23 (line)]] | alt | 216 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.52× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -18.8) |
| [[PANC-1 (line)]] | alt | 131 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 7.09× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -16.8) |
| [[RKO (line)]] | wt | 210 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -16.5) |
| [[RPMI-7951 (line)]] | alt | 418 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -20.7) |
| [[SNU-1 (line)]] | wt | 275 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -23.3) |
| [[AN3 CA (line)]] | alt | 375 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -18.5) |
| [[BT-474 (line)]] | alt | 132 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -17.4) |
| [[HepG2_C3A (line)]] | wt | 304 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -21.6) |
| [[LoVo (line)]] | wt | 186 | 2 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -19.6) |
| [[NCI-H2347 (line)]] | alt | 217 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.378× (z -13.0) |
| [[A-172 (line)]] | wt | 173 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.344× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 331 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.344× (z -9.0) |
| [[COLO 205 (line)]] | alt | 132 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.19× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.7) |
| [[HCT15 (line)]] | alt | 288 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -22.0) |
| [[Hs 766T (line)]] | wt | 253 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -15.8) |
| [[LS 180 (line)]] | wt | 215 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -13.6) |
| [[SK-MEL-2 (line)]] | alt | 179 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -18.7) |
| [[SW 900 (line)]] | alt | 227 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 155 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -19.9) |
| [[HS-578T (line)]] | alt | 229 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -14.1) |
| [[hTERT-HPNE (line)]] | wt | 232 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.3) |
| [[J82 (line)]] | alt | 198 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -9.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 248 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.5) |
| [[SW 1271 (line)]] | alt | 267 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -10.7) |
| [[SW48 (line)]] | wt | 206 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -15.1) |
| [[A-427 (line)]] | wt | 94.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -11.1) |
| [[A549 (line)]] | wt | 151 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -13.1) |
| [[CHP-212 (line)]] | wt | 222 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -13.4) |
| [[HOP62 (line)]] | alt | 273 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 187 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -20.1) |
| [[SHP-77 (line)]] | alt | 152 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -15.3) |
| [[A498 (line)]] | wt | 91.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 265 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDK3]] | +0.82 | +0.90 / +0.74 | both halves | 7e-06 | same gene group; pathway: HALLMARK_HYPOXIA; STRING 833 |
| [[HERC3]] | +0.78 | +0.86 / +0.64 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.77 | +0.85 / +0.67 | both halves | 7e-06 |  |
| [[EGLN1]] | +0.76 | +0.81 / +0.75 | both halves | 7e-06 | STRING 514 |
| [[ERO1A]] | +0.76 | +0.82 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[HDAC3]] | +0.75 | +0.86 / +0.64 | both halves | 7e-06 | pathway: Signaling by Nuclear Receptors |
| [[TPD52]] | +0.75 | +0.83 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[HK2]] | +0.73 | +0.84 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 753 |
| [[KDM3A]] | +0.73 | +0.81 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[FAM162A]] | +0.72 | +0.88 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[WDR45B]] | +0.72 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[FAM210A]] | +0.71 | +0.81 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF274]] | -0.65 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[ZNF140]] | -0.59 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[RBMXL1]] | -0.58 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[SLC35C2]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ZNF75A]] | -0.55 | -0.64 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.1, -17.1); signed map (-36.2, 24.0). **Vector** length 127, 54.9% of its response variance represented; |z| ≥ 3 in 1,426 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.3 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | -6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +0.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.0 | -4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.7 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.9 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.9 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | -1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.4 | -21.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.9 | -10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -10.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.3 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.0 | -0.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.0 | -4.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | pyruvate dehydrogenase kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:172,555,373-172,608,669 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pyruvate dehydrogenase kinase family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, HYPOXIA, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: Regulation of pyruvate dehydrogenase (PDH) complex; Regulation of pyruvate metabolism; Signaling by Retinoic Acid |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15118](https://www.uniprot.org/uniprotkb/Q15118) ([Pyruvate dehydrogenase (acetyl-transferring)] kinase isozyme 1, mitochondrial):

> Kinase that plays a key role in regulation of glucose and fatty acid metabolism and homeostasis via phosphorylation of the pyruvate dehydrogenase subunits PDHA1 and PDHA2. This inhibits pyruvate dehydrogenase activity, and thereby regulates metabolite flux through the tricarboxylic acid cycle, down-regulates aerobic respiration and inhibits the formation of acetyl-coenzyme A from pyruvate. Plays an important role in cellular responses to hypoxia and is important for cell proliferation under …

**Summary**, from NCBI Gene [5163](https://www.ncbi.nlm.nih.gov/gene/5163):

> Pyruvate dehydrogenase (PDH) is a mitochondrial multienzyme complex that catalyzes the oxidative decarboxylation of pyruvate and is one of the major enzymes responsible for the regulation of homeostasis of carbohydrate fuels in mammals. The enzymatic activity is regulated by a phosphorylation/dephosphorylation cycle. Phosphorylation of PDH by a specific pyruvate dehydrogenase kinase (PDK) results in inactivation. Multiple alternatively spliced transcript variants have been found for this gene. …

**Accessions** — [HGNC:8809](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8809) · Entrez [5163](https://www.ncbi.nlm.nih.gov/gene/5163) · UniProt [Q15118](https://www.uniprot.org/uniprotkb/Q15118) · Ensembl [ENSG00000152256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152256)

## Data

Gene col 7610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7610); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7610]; `tensor/DDL_lfc|DDL_z.npy` [7610]; `embed/gene_vectors.npy` [7610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7610 or target_col == 7610). Every well: [[PDK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
