---
symbol: "PDAP1"
type: "gene"
col: 2731
ensembl_id: "ENSG00000106244"
name: "PDGFA associated protein 1"
location: "7q22.1"
module: 215
arm: "+"
pooled_cpm: 69.77
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/215"]
generated_by: "tahoemap"
---

# PDAP1

*PDGFA associated protein 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.86× (z +25.3, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.55× (z +7.1, q 2e-10, up in 41 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (SHP-77 0.130×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.116×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (SHP-77 0.165×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPN11]] (+0.77, fdr 7e-06), [[PSMC3]] (+0.76, fdr 7e-06), [[CCT7]] (+0.72, fdr 7e-06); moves opposite to [[SNHG19]] (-0.75, fdr 7e-06), [[SNHG25]] (-0.74, fdr 7e-06), [[CSKMT]] (-0.73, fdr 7e-06).
> It is in [[Module 215]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2731.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.86×** | +25.3 | 0e+00 | 49/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.39×** | +22.8 | 0e+00 | 43/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.44×** | +18.3 | 0e+00 | 45/45 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +7.1 | 2e-10 | 41/48 (NCI-H460, NCI-H1573, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +6.7 | 3e-09 | 39/48 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +6.6 | 4e-09 | 38/48 (MIA PaCa-2, BT-474, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.51×** | +6.4 | 2e-08 | 35/48 (NCI-H1792, A498, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +5.7 | 7e-07 | 35/48 (C32, RKO, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.42×** | +5.6 | 1e-06 | 35/48 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.45×** | +5.5 | 3e-06 | 32/47 (NCI-H460, C32, …) | all doses, flat | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +4.9 | 4e-05 | 35/48 (NCI-H1573, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.36×** | +4.7 | 1e-04 | 29/47 (NCI-H1792, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.31×** | +4.3 | 6e-04 | 24/48 (A498, RKO, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 0.001 | 29/48 (NCI-H460, HT-29, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **1.29×** | +3.9 | 0.004 | 27/47 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Busulfan (drug)]] 5 µM |  | 1.17× | +3.6 | 0.013 | 14/49 (NCI-H460, H4, …) | inconsistent across doses | position effect removed |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.017 | 25/48 (SK-MEL-2, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 5 µM |  | 1.16× | +3.4 | 0.018 | 12/48 (SW48, C-33 A, …) | top dose only | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.022 | 20/48 (PANC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.029 | 21/47 (NCI-H460, HT-29, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.038 | 18/47 (NCI-H460, HT-29, …) | all doses, flat |  |
| [[Allantoin (drug)]] 5 µM |  | 1.14× | +3.0 | 0.066 | 8/48 (A-427, NCI-H460, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.20× | +2.9 | 0.074 | 20/48 (H4, KATO III, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2731.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (SHP-77 0.130×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.116×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (SHP-77 0.165×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.736× | -3.5 | 0.13 | 24/48 (SHP-77, NCI-H661, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.808× | -3.4 | 0.13 | 20/48 (SW1417, Panc 03.27, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.812× | -3.3 | 0.13 | 20/48 (SW48, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.804× | -3.3 | 0.13 | 22/48 (A498, SHP-77, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.816× | -3.2 | 0.13 | 20/48 (SHP-77, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2731. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 72.2 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.20× (z +19.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 69.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +16.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 52.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +14.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 72.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +16.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 38.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +12.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 47.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.79× (z +15.0) ⚠ toxic; transcription drop | [[Thymol (drug)]] 0.5 µM 0.130× (z -16.6) |
| [[A-427 (line)]] | wt | 74.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +16.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 87.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +18.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 53.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +17.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 103 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.02× (z +16.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 64.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +16.3) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 40.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +11.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 49.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.78× (z +16.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 64.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +13.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 95.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +16.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 82.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +12.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 99.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +17.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 80.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +14.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 51.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.29× (z +17.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 63.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +17.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 65.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +14.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 47.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.01× (z +18.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 46.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +13.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 79.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.97× (z +18.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 62.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.38× (z +20.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 59.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +14.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 86.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.85× (z +18.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 73.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 54.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +16.1) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 55.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +14.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 93.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +14.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 88.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.13× (z +22.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 52.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.3) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 79.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +11.3) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 62.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.02× (z +9.6) ⚠ toxic; transcription drop | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.116× (z -10.7) |
| [[H4 (line)]] | wt | 67.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +13.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 65.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +12.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 60.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 73.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 58.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 87.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +12.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 42.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.67× (z +13.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 127 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +12.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 64.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2731), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN11]] | +0.77 | +0.79 / +0.75 | both halves | 7e-06 |  |
| [[PSMC3]] | +0.76 | +0.77 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[CCT7]] | +0.72 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[HUWE1]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[CCT5]] | +0.70 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[ZNF460]] | +0.68 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[LIN7C]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[HSPB8]] | +0.67 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[EIF4H]] | +0.66 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[EIF4G1]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[PSME3IP1]] | +0.66 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[PUS7L]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*63 of its nearest partners move opposite, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG19]] | -0.75 | -0.60 / -0.79 | both halves | 7e-06 |  |
| [[SNHG25]] | -0.74 | -0.64 / -0.75 | both halves | 7e-06 |  |
| [[CSKMT]] | -0.73 | -0.62 / -0.78 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | -0.71 | -0.57 / -0.77 | both halves | 1e-05 |  |
| [[COMMD6]] | -0.69 | -0.61 / -0.71 | both halves | 7e-06 |  |
| [[MZT2B]] | -0.69 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[BRI3]] | -0.67 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[SNHG9]] | -0.67 | -0.44 / -0.71 | both halves | 3e-05 |  |
| [[NDUFA2]] | -0.67 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[RPS29]] | -0.66 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[TOMM7]] | -0.66 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[RPLP2]] | -0.66 | -0.62 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 215]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.866). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.1, -20.7); signed map (-6.5, -36.9). **Vector** length 99.0, 27.9% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +7.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.9 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +3.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.2 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.8 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.1 | -2.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.8 | +0.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.7 | -2.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | PDGFA associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,392,048-99,408,597 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAP1, PAP, HASPP28 |
| Hallmark sets | UV_RESPONSE_UP, MTORC1_SIGNALING |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13442](https://www.uniprot.org/uniprotkb/Q13442) (28 kDa heat- and acid-stable phosphoprotein):

> Enhances PDGFA-stimulated cell growth in fibroblasts, but inhibits the mitogenic effect of PDGFB.

**Summary**, from NCBI Gene [11333](https://www.ncbi.nlm.nih.gov/gene/11333):

> The protein encoded by this gene is a phosphoprotein that may upregulate the PDGFA-stimulated growth of fibroblasts and also downregulate the mitogenicity of PDGFB. The encoded protein in rodents has been shown to bind PDGFA with a low affinity. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:14634](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14634) · Entrez [11333](https://www.ncbi.nlm.nih.gov/gene/11333) · UniProt [Q13442](https://www.uniprot.org/uniprotkb/Q13442) · Ensembl [ENSG00000106244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106244)

## Data

Gene col 2731: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2731); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2731, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2731]; `tensor/DDL_lfc|DDL_z.npy` [2731]; `embed/gene_vectors.npy` [2731]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2731 or target_col == 2731). Every well: [[PDAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
