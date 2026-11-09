---
symbol: "PDIA6"
type: "gene"
col: 6817
ensembl_id: "ENSG00000143870"
name: "protein disulfide isomerase family A member 6"
location: "2p25.1"
module: 42
arm: "+"
pooled_cpm: 283.23
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# PDIA6

*protein disulfide isomerase family A member 6* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.75× (z +14.3, q 2e-43, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.64× (z +3.6, q 0.015, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A-427 5.48×, SW480 4.07×, A549 4.26×, PANC-1 3.77×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 4.24×, SHP-77 3.24×, SW480 3.45×, PANC-1 3.34×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 4.08×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.307× (z -23.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDIA3]] (+0.93, fdr 7e-06), [[PDIA4]] (+0.88, fdr 7e-06), [[HSP90B1]] (+0.82, fdr 7e-06); moves opposite to [[ZNF480]] (-0.68, fdr 7e-06), [[MRFAP1L1]] (-0.64, fdr 7e-06), [[TRIM47]] (-0.63, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6817.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A-427 5.48×, SW480 4.07×, A549 4.26×, PANC-1 3.77×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (A-427 4.24×, SHP-77 3.24×, SW480 3.45×, PANC-1 3.34×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 4.08×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.75×** | +14.3 | 2e-43 | 48/49 (A-427, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +12.9 | 2e-35 | 43/44 (A-427, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +10.0 | 2e-21 | 44/45 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.42×** | +5.0 | 8e-05 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.28×** | +5.0 | 8e-05 | 30/49 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.41×** | +4.8 | 1e-04 | 34/48 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.33×** | +3.9 | 0.009 | 27/47 (SHP-77, A-427, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.8 | 0.009 | 28/38 (Panc 03.27, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.31×** | +3.8 | 0.010 | 30/48 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +3.6 | 0.015 | 32/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.31×** | +3.6 | 0.015 | 28/50 (A-427, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6817.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.307×** | -23.6 | 0e+00 | 48/48 (KATO III, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.436×** | -11.7 | 3e-29 | 45/48 (RPMI-7951, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.504×** | -9.3 | 2e-18 | 46/48 (KATO III, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.704×** | -7.0 | 3e-10 | 43/48 (NCI-H2030, RPMI-7951, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.642×** | -6.3 | 4e-08 | 46/48 (RKO, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.668×** | -5.7 | 1e-06 | 37/48 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.728×** | -4.5 | 6e-04 | 33/48 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | **0.799×** | -4.5 | 6e-04 | 35/48 (C32, RPMI-7951, …) | rises with dose | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.550×** | -4.4 | 7e-04 | 40/49 (KATO III, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.756×** | -3.9 | 0.005 | 32/48 (KATO III, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.741×** | -3.9 | 0.005 | 40/47 (A-172, CHP-212, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.621×** | -3.5 | 0.021 | 37/50 (J82, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.787×** | -3.4 | 0.031 | 31/48 (Hs 766T, SW 1088, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.786×** | -3.3 | 0.044 | 27/47 (NCI-H2030, RKO, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.797×** | -3.2 | 0.052 | 29/49 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 571 | 2 (2 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -35.6) |
| [[A-172 (line)]] | wt | 326 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -19.4) |
| [[NCI-H2030 (line)]] | alt | 459 | 4 (4 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -28.8) |
| [[A-427 (line)]] | wt | 340 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -19.3) |
| [[J82 (line)]] | alt | 203 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -29.0) |
| [[LOX-IMVI (line)]] | wt | 160 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 363 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -25.4) |
| [[Panc 03.27 (line)]] | alt | 196 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -15.2) |
| [[RPMI-7951 (line)]] | alt | 371 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.24× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -34.7) |
| [[A498 (line)]] | wt | 345 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -14.3) |
| [[H4 (line)]] | wt | 338 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -27.7) |
| [[NCI-H2347 (line)]] | alt | 266 | 1 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.6) ⚠ cell-cycle shift, explains ~13% of this change | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -19.6) |
| [[PANC-1 (line)]] | alt | 272 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -15.0) |
| [[RKO (line)]] | wt | 269 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -28.5) |
| [[SHP-77 (line)]] | alt | 416 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +14.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -20.7) |
| [[SK-MEL-2 (line)]] | alt | 229 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -19.7) |
| [[SNU-423 (line)]] | alt | 209 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -12.6) |
| [[SW480 (line)]] | alt | 143 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -16.8) |
| [[A549 (line)]] | wt | 232 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -11.4) |
| [[C-33 A (line)]] | alt | 199 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -14.1) |
| [[HOP62 (line)]] | alt | 410 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -22.3) |
| [[HT-29 (line)]] | alt | 270 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -23.4) |
| [[hTERT-HPNE (line)]] | wt | 302 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 291 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -20.9) |
| [[NCI-H1792 (line)]] | alt | 236 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 324 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -22.1) |
| [[SNU-1 (line)]] | wt | 240 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -20.8) |
| [[AN3 CA (line)]] | alt | 282 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 153 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 367 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -19.7) |
| [[HepG2_C3A (line)]] | wt | 310 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -17.6) |
| [[Hs 766T (line)]] | wt | 194 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -14.3) |
| [[HS-578T (line)]] | alt | 423 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -21.1) |
| [[LoVo (line)]] | wt | 205 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -16.6) |
| [[LS 180 (line)]] | wt | 316 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -21.3) |
| [[SW 900 (line)]] | alt | 257 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -14.4) |
| [[SW48 (line)]] | wt | 268 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -17.4) |
| [[C32 (line)]] | wt | 176 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -13.6) |
| [[HCT15 (line)]] | alt | 265 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 257 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.582× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 326 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -13.1) |
| [[SW 1088 (line)]] | alt | 523 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -18.0) |
| [[SW1417 (line)]] | alt | 222 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -10.6) |
| [[SW 1271 (line)]] | alt | 185 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.9) |
| [[BT-474 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 181 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 386 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA3]] | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; STRING 916 |
| [[PDIA4]] | +0.88 | +0.90 / +0.86 | both halves | 7e-06 | same gene group; STRING 893 |
| [[HSP90B1]] | +0.82 | +0.83 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 990 |
| [[DDOST]] | +0.80 | +0.81 / +0.81 | both halves | 7e-06 | STRING 902 |
| [[CALR]] | +0.79 | +0.80 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 937 |
| [[MLEC]] | +0.78 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[HYOU1]] | +0.76 | +0.72 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 943 |
| [[DNAJB11]] | +0.75 | +0.78 / +0.71 | both halves | 7e-06 | pathway: IRE1alpha activates chaperones; STRING 959 |
| [[TMED10]] | +0.75 | +0.78 / +0.73 | both halves | 7e-06 | STRING 642 |
| [[RPN2]] | +0.74 | +0.74 / +0.74 | both halves | 7e-06 | STRING 842 |
| [[TM9SF2]] | +0.73 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[HSPA5]] | +0.73 | +0.81 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 995 |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF480]] | -0.68 | -0.70 / -0.62 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | -0.64 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[TRIM47]] | -0.63 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[PDRG1]] | -0.63 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[MRPL58]] | -0.62 | -0.62 / -0.67 | both halves | 7e-06 |  |
| [[RPL7L1]] | -0.62 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[CCDC137]] | -0.61 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[CMTR2]] | -0.61 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[ZC3HC1]] | -0.61 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[ERCC4]] | -0.61 | -0.63 / -0.57 | both halves | 9e-06 |  |
| [[THG1L]] | -0.60 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[EID2]] | -0.60 | -0.62 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises PDIA6's level | compounds that target MTOR: 4 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Temsirolimus) | 50% of the class's compounds vs 2.8% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds |
| [[CKAP4]] | C | CKAP4 activity raises PDIA6's level | lines that do not express CKAP4 (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without CKAP4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CAMKK1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, -30.3); signed map (-55.0, 6.5). **Vector** length 133, 55.4% of its response variance represented; |z| ≥ 3 in 1,257 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.51 to 23); *Maturation of DENV proteins* (reactome, mean cos +0.72 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.70 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +9.5 | +5.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +7.1 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | -1.4 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.8 | +0.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -12.0 | -9.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.4 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.2 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.6 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -23.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.4 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.3 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.8 | -0.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.5 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | protein disulfide isomerase family A member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:10,783,391-10,837,977 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P5, ERp5; previously TXNDC7 |
| Gene groups (HGNC) | Protein disulfide isomerases; Thioredoxin domain containing |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 7 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Post-translational protein phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15084](https://www.uniprot.org/uniprotkb/Q15084) (Protein disulfide-isomerase A6):

> May function as a chaperone that inhibits aggregation of misfolded proteins. Negatively regulates the unfolded protein response (UPR) through binding to UPR sensors such as ERN1, which in turn inactivates ERN1 signaling. May also regulate the UPR via the EIF2AK3 UPR sensor. Plays a role in platelet aggregation and activation by agonists such as convulxin, collagen and thrombin.

**Summary**, from NCBI Gene [10130](https://www.ncbi.nlm.nih.gov/gene/10130):

> This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, two catalytically active thioredoxin (TRX) domains, a TRX-like domain, and a C-terminal ER-retention sequence. This protein inhibits the aggregation of misfolded proteins and exhibits both isomerase and chaperone activity. Alternative splicing results in …

**Accessions** — [HGNC:30168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30168) · Entrez [10130](https://www.ncbi.nlm.nih.gov/gene/10130) · UniProt [Q15084](https://www.uniprot.org/uniprotkb/Q15084) · Ensembl [ENSG00000143870](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143870)

## Data

Gene col 6817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6817); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6817]; `tensor/DDL_lfc|DDL_z.npy` [6817]; `embed/gene_vectors.npy` [6817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6817 or target_col == 6817). Every well: [[PDIA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDIA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
