---
symbol: "UBAP2"
type: "gene"
col: 5962
ensembl_id: "ENSG00000137073"
name: "ubiquitin associated protein 2"
location: "9p13.3"
module: 93
arm: "+"
pooled_cpm: 188.59
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# UBAP2

*ubiquitin associated protein 2* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +20.7, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.656× (z -8.7, q 1e-15, down in 33 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 0.447×, KATO III 0.439×, MIA PaCa-2 0.404×, C-33 A 0.431×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RKO 0.305×, A-427 0.373×, KATO III 0.431×, PANC-1 0.512×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 2 lines (Panc 03.27 0.0576×, HEC-1-A 0.243×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.449×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.175×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRPV1]] (+0.53, fdr 3e-05), [[ARIH1]] (+0.51, fdr 3e-05), [[OGDH]] (+0.51, fdr 2e-05); moves opposite to [[ABHD13]] (-0.59, fdr 2e-05), [[TSEN15]] (-0.52, fdr 4e-05), [[NEPRO]] (-0.51, fdr 2e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5962.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +20.7 | 0e+00 | 43/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.18×** | +16.6 | 0e+00 | 48/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +13.8 | 9e-41 | 44/50 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.86×** | +13.3 | 6e-38 | 47/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +12.9 | 4e-36 | 42/48 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +11.8 | 6e-30 | 47/48 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +10.4 | 3e-23 | 38/49 (Hs 766T, AsPC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +6.9 | 3e-10 | 29/48 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +6.7 | 1e-09 | 41/48 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +6.2 | 3e-08 | 28/48 (NCI-H1573, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.9 | 2e-07 | 30/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +5.2 | 1e-05 | 32/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.24×** | +4.6 | 2e-04 | 23/48 (J82, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.002 | 23/48 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.14× | +4.0 | 0.003 | 18/48 (Hs 766T, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.005 | 27/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.062 | 17/48 (CFPAC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +2.9 | 0.096 | 8/48 (C-33 A, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5962.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 0.447×, KATO III 0.439×, MIA PaCa-2 0.404×, C-33 A 0.431×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (RKO 0.305×, A-427 0.373×, KATO III 0.431×, PANC-1 0.512×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 2 lines (Panc 03.27 0.0576×, HEC-1-A 0.243×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.449×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.175×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.656×** | -8.7 | 1e-15 | 33/44 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.646×** | -8.7 | 1e-15 | 32/45 (RKO, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.673×** | -8.5 | 4e-15 | 35/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **0.798×** | -4.8 | 2e-04 | 27/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -4.0 | 0.008 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.835× | -3.9 | 0.009 | 23/48 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.889× | -3.6 | 0.027 | 9/48 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.854× | -3.4 | 0.047 | 14/48 (SW 1088, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.856× | -3.1 | 0.12 | 18/47 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5962. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 142 | 10 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +26.5) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -9.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 239 | 8 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.587× (z -9.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 236 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.500× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 181 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +18.9) | — |
| [[KATO III (line)]] | alt | 215 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.439× (z -12.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 240 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +18.0) | [[Lonafarnib (drug)]] 5 µM 0.0576× (z -19.5) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 188 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +11.7) | [[Lonafarnib (drug)]] 5 µM 0.243× (z -11.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 138 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +18.9) | — |
| [[Hs 766T (line)]] | wt | 180 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +19.2) | — |
| [[J82 (line)]] | alt | 254 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.8) | [[Dinaciclib (drug)]] 0.05 µM 0.440× (z -10.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 174 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +20.1) | [[Dinaciclib (drug)]] 0.05 µM 0.493× (z -8.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 244 | 3 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 106 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +24.9) | — |
| [[NCI-H23 (line)]] | alt | 143 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.39× (z +12.1) | — |
| [[RKO (line)]] | wt | 171 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -13.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 248 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.8) | — |
| [[LS 180 (line)]] | wt | 180 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +15.7) | — |
| [[SK-MEL-2 (line)]] | alt | 164 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +21.0) | — |
| [[SW 900 (line)]] | alt | 156 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +13.9) | [[Docetaxel (drug)]] 0.05 µM 0.460× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~22% of this change |
| [[A-172 (line)]] | wt | 132 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +11.4) | — |
| [[A498 (line)]] | wt | 265 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.543× (z -8.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 54.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +16.7) | — |
| [[HepG2_C3A (line)]] | wt | 126 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 142 | 4 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +15.2) | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 357 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.447× (z -13.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 174 | 3 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.458× (z -9.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 264 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +12.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.526× (z -9.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 167 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.449× (z -11.8) |
| [[A549 (line)]] | wt | 163 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +13.8) | — |
| [[NCI-H1792 (line)]] | alt | 110 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +20.9) | — |
| [[RPMI-7951 (line)]] | alt | 106 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 272 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.431× (z -11.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 121 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +21.6) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -11.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 227 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +16.5) | — |
| [[HCT15 (line)]] | alt | 245 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.96× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.486× (z -9.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 90.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +11.3) | — |
| [[SW48 (line)]] | wt | 240 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +12.2) | — |
| [[NCI-H2030 (line)]] | alt | 133 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +14.2) | — |
| [[SNU-1 (line)]] | wt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.383× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 154 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.175× (z -9.0) |
| [[AN3 CA (line)]] | alt | 198 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 180 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 229 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 190 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5962), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRPV1]] | +0.53 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[ARIH1]] | +0.51 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[OGDH]] | +0.51 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[TXLNG]] | +0.50 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[TOB2]] | +0.50 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[RAPGEF6]] | +0.49 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[SLC9A1]] | +0.47 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[FUS]] | +0.47 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[DEPDC5]] | +0.47 | +0.28 / +0.52 | both halves | 3e-04 |  |
| [[PSEN1]] | +0.46 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[SHPK]] | +0.46 | +0.47 / +0.38 | both halves | 7e-05 |  |
| [[POLG]] | +0.46 | +0.40 / +0.44 | both halves | 5e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD13]] | -0.59 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[TSEN15]] | -0.52 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[NEPRO]] | -0.51 | -0.54 / -0.49 | both halves | 2e-05 |  |
| [[ZNF484]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[RNF2]] | -0.49 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[ZNF221]] | -0.48 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[RAD23B]] | -0.47 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[ZKSCAN8]] | -0.47 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[PSMD6]] | -0.46 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[DLD]] | -0.46 | -0.47 / -0.33 | both halves | 1e-04 | STRING 448 |
| [[NAA16]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[LYPLAL1]] | -0.46 | -0.39 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.429). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-21.6, -6.2); signed map (5.1, 17.7). **Vector** length 104, 33.8% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +13.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +12.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +6.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.7 | +2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.5 | +0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.3 | +0.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.0 | -8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.1 | -8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.4 | -8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.3 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.1 | -2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.1 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:33,921,693-34,049,388 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1491, bA176F3.5, FLJ22435 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T6F2](https://www.uniprot.org/uniprotkb/Q5T6F2) (Ubiquitin-associated protein 2):

> Recruits the ubiquitination machinery to RNA polymerase II for polyubiquitination, removal and degradation, when the transcription-coupled nucleotide excision repair (TC-NER) machinery fails to resolve DNA damage. May promote the degradation of ANXA2.

**Summary**, from NCBI Gene [55833](https://www.ncbi.nlm.nih.gov/gene/55833):

> The protein encoded by this gene contains a UBA (ubiquitin associated) domain, which is characteristic of proteins that function in the ubiquitination pathway. This gene may show increased expression in the adrenal gland and lymphatic tissues. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:14185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14185) · Entrez [55833](https://www.ncbi.nlm.nih.gov/gene/55833) · UniProt [Q5T6F2](https://www.uniprot.org/uniprotkb/Q5T6F2) · Ensembl [ENSG00000137073](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137073)

## Data

Gene col 5962: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5962); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5962, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5962]; `tensor/DDL_lfc|DDL_z.npy` [5962]; `embed/gene_vectors.npy` [5962]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5962 or target_col == 5962). Every well: [[UBAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
