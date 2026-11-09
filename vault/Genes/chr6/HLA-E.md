---
symbol: "HLA-E"
type: "gene"
col: 12896
ensembl_id: "ENSG00000204592"
name: "major histocompatibility complex, class I, E"
location: "6p22.1"
module: 70
arm: "+"
pooled_cpm: 213.44
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 22
n_dd_up_clean: 22
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 22
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# HLA-E

*major histocompatibility complex, class I, E* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.65× (z +20.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.277× (z -9.9, q 2e-20, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-B]] (+0.83, fdr 7e-06), [[HLA-A]] (+0.80, fdr 7e-06), [[HLA-F]] (+0.78, fdr 7e-06); moves opposite to [[XPO7]] (-0.60, fdr 1e-05), [[TUBGCP3]] (-0.59, fdr 1e-05), [[CHCHD6]] (-0.58, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[OASL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.65×** | +20.4 | 0e+00 | 47/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +9.1 | 2e-17 | 41/47 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +8.9 | 9e-17 | 42/49 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +8.2 | 4e-14 | 31/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.69×** | +7.7 | 1e-12 | 43/47 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +7.2 | 5e-11 | 13/49 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.0 | 2e-10 | 34/47 (HOP62, SW1417, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.55×** | +4.6 | 2e-04 | 41/47 (LS 180, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.6 | 2e-04 | 28/47 (HT-29, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +4.6 | 3e-04 | 28/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +4.4 | 5e-04 | 32/47 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.002 | 28/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.005 | 29/47 (RKO, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.005 | 25/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.011 | 28/47 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.011 | 28/47 (AsPC-1, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.017 | 28/46 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12896.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.277×** | -9.9 | 2e-20 | 44/47 (SK-MEL-2, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.525×** | -9.0 | 8e-17 | 38/46 (A-172, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.334×** | -8.5 | 5e-15 | 45/48 (LOX-IMVI, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.631×** | -6.5 | 9e-09 | 39/48 (SNU-423, HepG2/C3A, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.736×** | -6.4 | 2e-08 | 33/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.703×** | -5.2 | 2e-05 | 41/47 (LoVo, BT-474, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.714×** | -5.0 | 6e-05 | 31/47 (COLO 205, A498, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.747×** | -4.3 | 0.001 | 28/47 (AsPC-1, A498, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.748×** | -4.3 | 0.001 | 37/47 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.577×** | -4.2 | 0.001 | 26/37 (SNU-1, A549, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.757×** | -4.1 | 0.002 | 27/48 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.757×** | -4.1 | 0.002 | 30/47 (MIA PaCa-2, LoVo, …) | two highest doses | position effect removed |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **0.603×** | -3.9 | 0.004 | 28/48 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.780×** | -3.6 | 0.011 | 32/47 (KATO III, NCI-H2030, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.787×** | -3.5 | 0.016 | 25/47 (NCI-H1792, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.787×** | -3.5 | 0.016 | 27/47 (COLO 205, A-172, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.851× | -3.3 | 0.028 | 22/48 (MIA PaCa-2, LoVo, …) | two highest doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.658×** | -3.2 | 0.040 | 26/47 (AsPC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 171 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +20.2) | — |
| [[HOP62 (line)]] | alt | 156 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +22.7) | — |
| [[J82 (line)]] | alt | 450 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +17.2) | — |
| [[C32 (line)]] | wt | 226 | 5 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.41× (z +21.5) | [[TAK-901 (drug)]] 0.05 µM 0.319× (z -11.0) |
| [[HS-578T (line)]] | alt | 236 | 5 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +14.7) | [[TAK-901 (drug)]] 0.05 µM 0.346× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 189 | 3 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +15.0) | [[Tofacitinib (drug)]] 5 µM 0.438× (z -11.1) |
| [[COLO 205 (line)]] | alt | 450 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.273× (z -12.5) |
| [[LoVo (line)]] | wt | 213 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +15.0) | [[Tofacitinib (drug)]] 5 µM 0.466× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 141 | 4 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +16.8) | [[PH-797804 (drug)]] 5 µM 0.229× (z -8.7) |
| [[A-172 (line)]] | wt | 305 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +10.0) | [[TAK-901 (drug)]] 0.05 µM 0.255× (z -15.0) |
| [[BT-474 (line)]] | alt | 122 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +10.8) | [[TAK-901 (drug)]] 0.05 µM 0.146× (z -14.0) |
| [[HT-29 (line)]] | alt | 159 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +16.8) | — |
| [[hTERT-HPNE (line)]] | wt | 387 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.5) | [[TAK-901 (drug)]] 0.05 µM 0.264× (z -14.6) |
| [[LOX-IMVI (line)]] | wt | 188 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +15.8) | [[TAK-901 (drug)]] 0.05 µM 0.266× (z -14.0) |
| [[NCI-H2347 (line)]] | alt | 238 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +10.8) | [[TAK-901 (drug)]] 0.05 µM 0.303× (z -12.6) |
| [[SNU-1 (line)]] | wt | 133 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.3) | [[Lonafarnib (drug)]] 5 µM 0.105× (z -9.2) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 601 | 0 | 4 | — | [[TAK-901 (drug)]] 0.05 µM 0.347× (z -10.9) |
| [[SW 900 (line)]] | alt | 167 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +15.3) | — |
| [[SW480 (line)]] | alt | 77.5 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +21.5) | [[TAK-901 (drug)]] 0.05 µM 0.388× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 271 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +18.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.430× (z -9.9) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 367 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +16.6) | [[PH-797804 (drug)]] 5 µM 0.218× (z -9.6) |
| [[LS 180 (line)]] | wt | 125 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +13.0) | [[TAK-901 (drug)]] 0.05 µM 0.378× (z -9.2) |
| [[SW1417 (line)]] | alt | 171 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +14.7) | [[TAK-901 (drug)]] 0.05 µM 0.344× (z -11.9) |
| [[SW48 (line)]] | wt | 134 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +15.2) | [[TAK-901 (drug)]] 0.05 µM 0.328× (z -9.4) |
| [[A498 (line)]] | wt | 244 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.2) | [[TAK-901 (drug)]] 5 µM 0.208× (z -10.3) |
| [[A549 (line)]] | wt | 178 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +11.1) | [[PH-797804 (drug)]] 5 µM 0.168× (z -9.6) |
| [[C-33 A (line)]] | alt | 113 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 166 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +17.4) | [[Verteporfin (drug)]] 5 µM 0.423× (z -8.5) |
| [[Hs 766T (line)]] | wt | 449 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 132 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 162 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.5) | [[TAK-901 (drug)]] 5 µM 0.112× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 353 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +12.3) | [[TAK-901 (drug)]] 0.05 µM 0.325× (z -11.7) |
| [[RKO (line)]] | wt | 151 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +13.0) | [[PH-797804 (drug)]] 5 µM 0.168× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 292 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.8) | [[TAK-901 (drug)]] 0.05 µM 0.426× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 222 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +14.8) | [[PH-797804 (drug)]] 5 µM 0.177× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 458 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.6) | — |
| [[H4 (line)]] | wt | 157 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +15.4) | — |
| [[HCT15 (line)]] | alt | 149 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 62.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 183 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +15.7) | — |
| [[NCI-H2030 (line)]] | alt | 237 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +14.8) | — |
| [[NCI-H596 (line)]] | alt | 170 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.141× (z -11.8) |
| [[SW 1271 (line)]] | alt | 148 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +10.1) | — |
| [[A-427 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 125 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 114 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-B]] | +0.83 | +0.75 / +0.82 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 994 |
| [[HLA-A]] | +0.80 | +0.72 / +0.80 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 989 |
| [[HLA-F]] | +0.78 | +0.70 / +0.80 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 997 |
| [[TAP1]] | +0.75 | +0.70 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 764 |
| [[B2M]] | +0.75 | +0.67 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 999 |
| [[IRF7]] | +0.73 | +0.70 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[CTSS]] | +0.70 | +0.63 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[GBP4]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[TRIM5]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[PPM1K]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[HLA-C]] | +0.68 | +0.52 / +0.70 | both halves | 1e-05 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 989 |
| [[IFI27]] | +0.68 | +0.54 / +0.71 | both halves | 1e-05 | pathway: Interferon Signaling |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPO7]] | -0.60 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[TUBGCP3]] | -0.59 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[CHCHD6]] | -0.58 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[HEATR3]] | -0.58 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[NUP155]] | -0.58 | -0.54 / -0.62 | both halves | 1e-05 | pathway: Interferon Signaling |
| [[COA1]] | -0.57 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[MRPL3]] | -0.57 | -0.60 / -0.56 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[AGPS]] | -0.57 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CSTF2]] | -0.57 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[SNRPD1]] | -0.57 | -0.62 / -0.45 | both halves | 3e-05 | pathway: SARS-CoV-2 Infection |
| [[PGAM5]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[NOL10]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 20, C 2. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OASL]] | B | OASL activity raises HLA-E's level | lines that do not express OASL (10) vs lines expressing it (40) | 2.06× lower at baseline in the lines without OASL | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[HLA-F]] | B | HLA-F activity raises HLA-E's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 2.38× lower at baseline in the lines without HLA-F | 0.002 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[HLA-B]] | B | HLA-B activity raises HLA-E's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 2.53× lower at baseline in the lines without HLA-B | 0.004 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[PTGES]] | B | PTGES activity raises HLA-E's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.74× lower at baseline in the lines without PTGES | 0.004 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[CTSS]] | B | CTSS activity raises HLA-E's level | lines that do not express CTSS (15) vs lines expressing it (35) | 1.71× lower at baseline in the lines without CTSS | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[C15orf48]] | B | C15orf48 activity raises HLA-E's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 1.74× lower at baseline in the lines without C15orf48 | 0.006 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[IFI16]] | B | IFI16 activity raises HLA-E's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 1.89× lower at baseline in the lines without IFI16 | 0.009 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[MAF]] | B | MAF activity raises HLA-E's level | lines that do not express MAF (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without MAF | 0.011 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[GBP1]] | B | GBP1 activity raises HLA-E's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.98× lower at baseline in the lines without GBP1 | 0.022 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[TOP2A]] | B | TOP2A activity lowers HLA-E's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IFIT3]] | B | IFIT3 activity raises HLA-E's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 2.08× lower at baseline in the lines without IFIT3 | 0.025 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises HLA-E's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.97× lower at baseline in the lines without GBP4 | 0.030 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.5, 50.0); signed map (64.1, 27.5). **Vector** length 160, 58.4% of its response variance represented; |z| ≥ 3 in 1,514 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.57 to 25); *interferon alpha response* (hallmark, mean cos +0.58 to 19); *Non-canonical inflammasome activation* (reactome, mean cos +0.57 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +20.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +7.6 | +7.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +7.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.0 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.7 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +4.2 | +3.0 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -9.8 | -9.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -9.7 | -8.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -7.8 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.7 | -5.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.3 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.0 | -2.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.9 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | major histocompatibility complex, class I, E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:30,489,509-30,494,194 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Histocompatibility complex; C1-set domain containing |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 19 pathways, smallest: Endosomal/Vacuolar pathway; DAP12 signaling; DAP12 interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P13747](https://www.uniprot.org/uniprotkb/P13747) (HLA class I histocompatibility antigen, alpha chain E):

> Non-classical major histocompatibility class Ib molecule involved in immune self-nonself discrimination. In complex with B2M/beta-2-microglobulin binds nonamer self-peptides derived from the signal sequence of classical MHC class Ia molecules (VL9 peptides - VMAPRT[V/L][L/V/I/F]L). Peptide-bound HLA-E-B2M heterotrimeric complex primarily functions as a ligand for natural killer (NK) cell inhibitory receptor KLRD1-KLRC1, enabling NK cells to monitor the expression of other MHC class I molecules …

**Summary**, from NCBI Gene [3133](https://www.ncbi.nlm.nih.gov/gene/3133):

> HLA-E belongs to the HLA class I heavy chain paralogues. This class I molecule is a heterodimer consisting of a heavy chain and a light chain (beta-2 microglobulin). The heavy chain is anchored in the membrane. HLA-E binds a restricted subset of peptides derived from the leader peptides of other class I molecules. The heavy chain is approximately 45 kDa and its gene contains 8 exons. Exon one encodes the leader peptide, exons 2 and 3 encode the alpha1 and alpha2 domains, which both bind the …

**Accessions** — [HGNC:4962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4962) · Entrez [3133](https://www.ncbi.nlm.nih.gov/gene/3133) · UniProt [P13747](https://www.uniprot.org/uniprotkb/P13747) · Ensembl [ENSG00000204592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204592)

## Data

Gene col 12896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12896); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12896]; `tensor/DDL_lfc|DDL_z.npy` [12896]; `embed/gene_vectors.npy` [12896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12896 or target_col == 12896). Every well: [[HLA-E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLA-E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
