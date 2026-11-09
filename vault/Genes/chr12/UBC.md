---
symbol: "UBC"
type: "gene"
col: 7473
ensembl_id: "ENSG00000150991"
name: "ubiquitin C"
location: "12q24.3"
module: 12
arm: "+"
pooled_cpm: 357.38
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# UBC

*ubiquitin C* — 12q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 6.44× (z +18.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.535× (z -8.6, q 5e-15, down in 49 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 14 lines (AsPC-1 0.312×, A-172 0.263×, NCI-H2347 0.396×, HS-578T 0.366×, …); [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H2347 0.238×, NCI-H661 0.0826×, BT-474 0.227×, A-172 0.185×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 0.178×; ⚠ toxic; transcription drop); [[Verteporfin (drug)]] 5 µM in 1 line (SW 1088 0.198×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRF2]] (+0.66, fdr 7e-06), [[DNAJB1]] (+0.65, fdr 7e-06), [[ADRM1]] (+0.63, fdr 7e-06); moves opposite to [[CEP43]] (-0.53, fdr 3e-05), [[ARGLU1]] (-0.52, fdr 3e-05), [[TMA7]] (-0.52, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7473.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **6.44×** | +18.0 | 0e+00 | 48/48 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **5.15×** | +15.9 | 0e+00 | 48/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **5.50×** | +15.6 | 0e+00 | 48/48 (HEC-1-A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.25×** | +11.1 | 3e-26 | 43/48 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.37×** | +10.5 | 1e-23 | 49/50 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **7.44×** | +10.2 | 3e-22 | 45/45 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.81×** | +10.0 | 1e-21 | 46/48 (A-427, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **3.58×** | +8.8 | 9e-17 | 48/49 (HEC-1-A, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.35×** | +7.9 | 1e-13 | 45/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.07×** | +7.0 | 1e-10 | 42/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +4.5 | 3e-04 | 37/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.80×** | +4.1 | 0.002 | 42/47 (SW 1271, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.057 | 40/49 (Panc 03.27, Hs 766T, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.38×** | +3.1 | 0.081 | 29/48 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7473.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 14 lines (AsPC-1 0.312×, A-172 0.263×, NCI-H2347 0.396×, HS-578T 0.366×, …); [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H2347 0.238×, NCI-H661 0.0826×, BT-474 0.227×, A-172 0.185×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 0.178×; ⚠ toxic; transcription drop); [[Verteporfin (drug)]] 5 µM in 1 line (SW 1088 0.198×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.535×** | -8.6 | 5e-15 | 49/49 (AsPC-1, A-172, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.422×** | -8.1 | 2e-13 | 41/44 (NCI-H2347, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.565×** | -5.3 | 2e-05 | 43/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.726×** | -4.4 | 0.001 | 39/48 (COLO 205, SW48, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.652×** | -4.2 | 0.003 | 27/49 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.655×** | -4.0 | 0.007 | 37/50 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **0.696×** | -3.4 | 0.054 | 35/47 (RKO, AsPC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.723× | -3.2 | 0.11 | 34/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7473. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 368 | 13 (8 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 9.91× (z +17.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.9) |
| [[A-172 (line)]] | wt | 487 | 6 (1 ⚠) | 5 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 9.42× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -14.2) |
| [[A-427 (line)]] | wt | 259 | 9 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.44× (z +20.2) | — |
| [[C32 (line)]] | wt | 285 | 9 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.96× (z +15.2) | — |
| [[HEC-1-A (line)]] | alt | 223 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 11.4× (z +22.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 406 | 6 (2 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.09× (z +11.3) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -8.9) |
| [[PANC-1 (line)]] | alt | 388 | 7 (4 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.97× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -9.3) |
| [[SW1417 (line)]] | alt | 345 | 7 (2 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 7.22× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -9.3) |
| [[A549 (line)]] | wt | 483 | 7 (3 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 5.65× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 687 | 5 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +16.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.76× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -15.2) |
| [[HOP62 (line)]] | alt | 306 | 6 (2 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 7.53× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -10.2) |
| [[KATO III (line)]] | alt | 251 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 8.72× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.338× (z -10.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 308 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +19.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 6.68× (z +18.0) | — |
| [[LS 180 (line)]] | wt | 276 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.67× (z +16.5) | — |
| [[NCI-H1573 (line)]] | alt | 463 | 7 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +15.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 4.58× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 699 | 5 (1 ⚠) | 3 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 5.68× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -12.7) |
| [[SW 900 (line)]] | alt | 306 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 8.85× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -8.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 222 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 8.10× (z +17.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -8.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 315 | 5 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 6.95× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -9.0) |
| [[H4 (line)]] | wt | 277 | 7 (3 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 10.8× (z +16.7) | — |
| [[HT-29 (line)]] | alt | 320 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 8.37× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -8.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 282 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.21× (z +16.4) | — |
| [[NCI-H2030 (line)]] | alt | 297 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +15.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 7.63× (z +15.3) | — |
| [[RPMI-7951 (line)]] | alt | 307 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 7.90× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 284 | 7 (3 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 6.65× (z +14.1) | — |
| [[SNU-423 (line)]] | alt | 372 | 5 (2 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 6.54× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -9.6) |
| [[HS-578T (line)]] | alt | 449 | 4 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 9.70× (z +16.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 255 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.56× (z +15.4) | — |
| [[SW48 (line)]] | wt | 316 | 4 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 7.51× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -9.0) |
| [[A498 (line)]] | wt | 432 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 10.1× (z +16.8) | — |
| [[J82 (line)]] | alt | 297 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 6.57× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 291 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.70× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 359 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +12.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.89× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 335 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 6.41× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -10.1) |
| [[RKO (line)]] | wt | 269 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.54× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.228× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~57% of this change |
| [[SHP-77 (line)]] | alt | 118 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.61× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 293 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.60× (z +15.8) | — |
| [[AN3 CA (line)]] | alt | 218 | 4 | 0 | [[Auranofin (drug)]] 5 µM 6.88× (z +12.2) | — |
| [[C-33 A (line)]] | alt | 268 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.78× (z +13.3) | — |
| [[CFPAC-1 (line)]] | alt | 717 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.36× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -8.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 418 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +14.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.46× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 289 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.41× (z +16.2) | — |
| [[HepG2_C3A (line)]] | wt | 347 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.45× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -9.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 307 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.66× (z +13.6) | — |
| [[SW 1271 (line)]] | alt | 288 | 4 | 0 | [[Auranofin (drug)]] 5 µM 6.76× (z +10.2) | — |
| [[CHP-212 (line)]] | wt | 206 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.51× (z +14.1) | — |
| [[SW 1088 (line)]] | alt | 618 | 2 | 1 | [[Bortezomib (drug)]] 0.05 µM 5.32× (z +9.0) | [[Verteporfin (drug)]] 5 µM 0.198× (z -8.9) |
| [[NCI-H661 (line)]] | alt | 256 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0826× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 419 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 314 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7473), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRF2]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[DNAJB1]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 | pathway: MAPK family signaling cascades |
| [[ADRM1]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 | pathway: ABC transporter disorders; STRING 993 |
| [[BAG3]] | +0.60 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[MYG1]] | +0.59 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[MRPL10]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ZNF426]] | +0.58 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ZFAND5]] | +0.56 | +0.49 / +0.59 | both halves | 1e-05 | STRING 657 |
| [[DNAJB2]] | +0.55 | +0.60 / +0.45 | both halves | 3e-05 | STRING 506 |
| [[MSRB1]] | +0.55 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[CYB5R1]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[UBB]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 998 |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP43]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 | pathway: G2/M Transition |
| [[ARGLU1]] | -0.52 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[TMA7]] | -0.52 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[PAXBP1]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[QSOX2]] | -0.50 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[SNRPG]] | -0.50 | -0.35 / -0.54 | both halves | 1e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[RPL41]] | -0.49 | -0.43 / -0.43 | both halves | 4e-05 | pathway: Protein localization |
| [[PAXIP1]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 | pathway: Affinity selection of immunoglobulins |
| [[RBBP4]] | -0.49 | -0.45 / -0.39 | both halves | 6e-05 | pathway: Adherens junctions interactions; STRING 484 |
| [[CCNL2]] | -0.47 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[PTMS]] | -0.47 | -0.51 / -0.29 | both halves | 3e-04 |  |
| [[CPSF6]] | -0.46 | -0.47 / -0.43 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises UBC's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.421). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-42.9, -5.1); signed map (-22.6, -26.4). **Vector** length 156, 62.3% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +13.3 | +15.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +12.7 | +15.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +11.2 | +18.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.4 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +9.5 | +11.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.3 | +8.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +4.7 | +2.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +4.4 | +1.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.6 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.7 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.2 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -8.1 | -5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -7.9 | -4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -1.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -4.3 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.0 | -2.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.3 — chr12:124,911,604-124,917,368 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ubiquitins |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 415 pathways, smallest: Maturation of protein E_9683683; Maturation of protein E_9694493; FLT3 signaling by CBL mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P0CG48](https://www.uniprot.org/uniprotkb/P0CG48) (Polyubiquitin-C):

> [Ubiquitin]: Exists either covalently attached to another protein, or free (unanchored). When covalently bound, it is conjugated to target proteins via an isopeptide bond either as a monomer (monoubiquitin), a polymer linked via different Lys residues of the ubiquitin (polyubiquitin chains) or a linear polymer linked via the initiator Met of the ubiquitin (linear polyubiquitin chains). Polyubiquitin chains, when attached to a target protein, have different functions depending on the Lys residue …

**Summary**, from NCBI Gene [7316](https://www.ncbi.nlm.nih.gov/gene/7316):

> This gene represents a ubiquitin gene, ubiquitin C. The encoded protein is a polyubiquitin precursor. Conjugation of ubiquitin monomers or polymers can lead to various effects within a cell, depending on the residues to which ubiquitin is conjugated. Ubiquitination has been associated with protein degradation, DNA repair, cell cycle regulation, kinase modification, endocytosis, and regulation of other cell signaling pathways. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:12468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12468) · Entrez [7316](https://www.ncbi.nlm.nih.gov/gene/7316) · UniProt [P0CG48](https://www.uniprot.org/uniprotkb/P0CG48) · Ensembl [ENSG00000150991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150991)

## Data

Gene col 7473: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7473); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7473, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7473]; `tensor/DDL_lfc|DDL_z.npy` [7473]; `embed/gene_vectors.npy` [7473]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7473 or target_col == 7473). Every well: [[UBC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
