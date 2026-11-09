---
symbol: "KIF1B"
type: "gene"
col: 610
ensembl_id: "ENSG00000054523"
name: "kinesin family member 1B"
location: "1p36.22"
module: 60
arm: "+"
pooled_cpm: 199.3
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# KIF1B

*kinesin family member 1B* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.75× (z +24.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.557× (z -14.4, q 5e-44, down in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 0.834× (z -4.1, q 0.004, down in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (C-33 A 0.338×, A-172 0.372×, HEC-1-A 0.408×, AsPC-1 0.399×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H2347 0.371×, C-33 A 0.317×, HEC-1-A 0.373×, A-427 0.381×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 0.0398×, AN3 CA 0.233×, NCI-H1792 0.396×, HT-29 0.424×; ⚠ toxic; transcription drop); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.307×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX29]] (+0.63, fdr 7e-06), [[EXOC6B]] (+0.62, fdr 7e-06), [[MAP4]] (+0.62, fdr 7e-06); moves opposite to [[DGUOK]] (-0.55, fdr 1e-05), [[SRSF1]] (-0.51, fdr 5e-05), [[STAMBPL1]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STAMBPL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 610.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.75×** | +24.8 | 0e+00 | 48/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.41×** | +21.6 | 0e+00 | 48/48 (HT-29, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.58×** | +19.7 | 0e+00 | 48/48 (PANC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +17.8 | 0e+00 | 40/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.74×** | +9.7 | 4e-20 | 46/49 (COLO 205, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +8.9 | 8e-17 | 34/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +7.1 | 1e-10 | 34/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +6.8 | 8e-10 | 32/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +6.3 | 2e-08 | 30/48 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +6.1 | 7e-08 | 35/49 (MIA PaCa-2, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +5.9 | 2e-07 | 27/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.18× | +5.7 | 5e-07 | 24/49 (LS 180, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +5.7 | 6e-07 | 26/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +5.0 | 2e-05 | 32/48 (SW48, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +4.6 | 2e-04 | 23/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.21×** | +4.4 | 4e-04 | 24/47 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.5 | 0.013 | 9/49 (CFPAC-1, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 610.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (C-33 A 0.338×, A-172 0.372×, HEC-1-A 0.408×, AsPC-1 0.399×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H2347 0.371×, C-33 A 0.317×, HEC-1-A 0.373×, A-427 0.381×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 0.0398×, AN3 CA 0.233×, NCI-H1792 0.396×, HT-29 0.424×; ⚠ toxic; transcription drop); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.307×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.557×** | -14.4 | 5e-44 | 44/49 (C-33 A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.601×** | -11.5 | 2e-28 | 35/45 (NCI-H2347, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.655×** | -10.0 | 4e-21 | 38/44 (C-33 A, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -7.9 | 5e-13 | 35/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -5.4 | 9e-06 | 0/50 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.834× | -4.1 | 0.004 | 22/47 (NCI-H460, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.898× | -3.7 | 0.016 | 3/48 (NCI-H1792, SNU-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.816×** | -3.5 | 0.029 | 21/47 (SW 900, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.875× | -3.3 | 0.069 | 10/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | 0.876× | -3.2 | 0.069 | 19/48 (CFPAC-1, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 171 | 12 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.28× (z +23.6) | [[Dinaciclib (drug)]] 0.05 µM 0.492× (z -13.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 221 | 6 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.51× (z +13.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.428× (z -11.9) ⚠ toxic |
| [[LS 180 (line)]] | wt | 190 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.26× (z +22.0) | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 149 | 9 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.03× (z +20.6) | — |
| [[HT-29 (line)]] | alt | 170 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.25× (z +26.1) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -13.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 164 | 6 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.37× (z +22.6) | [[Dinaciclib (drug)]] 0.5 µM 0.594× (z -9.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 118 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -9.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 256 | 4 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.20× (z +18.2) | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -14.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 187 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -10.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 308 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 247 | 4 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.46× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 184 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +15.7) | — |
| [[SNU-423 (line)]] | alt | 218 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +17.7) | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 216 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -14.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 362 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -12.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 114 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.40× (z +22.4) | [[Dinaciclib (drug)]] 5 µM 0.496× (z -10.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 176 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.56× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.531× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 174 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 125 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.96× (z +19.9) | — |
| [[NCI-H2347 (line)]] | alt | 190 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.10× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -15.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 260 | 5 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.70× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -11.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 175 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.10× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -14.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 184 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.28× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.478× (z -9.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 119 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.07× (z +22.9) | — |
| [[H4 (line)]] | wt | 202 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 6.00× (z +20.6) | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -9.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 236 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +23.0) | [[Dinaciclib (drug)]] 0.5 µM 0.518× (z -9.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 127 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.13× (z +20.0) | — |
| [[NCI-H2030 (line)]] | alt | 270 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.21× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -11.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 184 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 160 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.74× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 145 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +15.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.473× (z -10.2) ⚠ toxic |
| [[A549 (line)]] | wt | 183 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.24× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.562× (z -8.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 196 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -13.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 214 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.25× (z +12.1) | — |
| [[C-33 A (line)]] | alt | 309 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.0398× (z -43.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 125 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.28× (z +15.4) | — |
| [[SHP-77 (line)]] | alt | 182 | 4 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.66× (z +12.1) | — |
| [[AN3 CA (line)]] | alt | 352 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -13.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 232 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.19× (z +16.3) | — |
| [[HepG2_C3A (line)]] | wt | 490 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.47× (z +10.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.393× (z -10.1) ⚠ toxic |
| [[SW 900 (line)]] | alt | 171 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.10× (z +14.2) | — |
| [[J82 (line)]] | alt | 239 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.458× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 196 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.47× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 199 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.307× (z -8.7) |
| [[RKO (line)]] | wt | 270 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +14.0) | — |
| [[CHP-212 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 191 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX29]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[EXOC6B]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[MAP4]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[HECTD4]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 | same gene group |
| [[MACO1]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[WDR44]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 | same gene group |
| [[HSPB1]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TTLL7]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[SANBR]] | +0.60 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CCSER2]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ERC1]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[LRRFIP2]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGUOK]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[SRSF1]] | -0.51 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[STAMBPL1]] | -0.49 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[KBTBD2]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[VMA21]] | -0.47 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[RFT1]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[UMPS]] | -0.46 | -0.35 / -0.47 | both halves | 1e-04 | same gene group |
| [[PFAS]] | -0.46 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[TIGD1]] | -0.46 | -0.32 / -0.45 | both halves | 2e-04 | same gene group |
| [[MIR30DHG]] | -0.45 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[TMEM147-AS1]] | -0.45 | -0.39 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAMBPL1]] | B | STAMBPL1 activity lowers KIF1B's level | lines that do not express STAMBPL1 (6) vs lines expressing it (44) | 1.68× higher at baseline in the lines without STAMBPL1 | 0.070 | ⚠ within organs, on part of the lines; also absent: CFAP45, PMAIP1, OCIAD2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.3, -0.4); signed map (-13.1, 18.7). **Vector** length 102, 34.2% of its response variance represented; |z| ≥ 3 in 1,322 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.3 | +24.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.0 | +21.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.0 | +19.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.8 | +3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.7 | +9.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.2 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | +3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.7 | -7.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.0 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | +5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:10,210,570-10,381,603 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0591, KLP, HMSNII; previously CMT2A, CMT2 |
| Gene groups (HGNC) | Kinesins; Pleckstrin homology domain containing; MicroRNA protein coding host genes |
| Hallmark sets | PROTEIN_SECRETION, INFLAMMATORY_RESPONSE, MITOTIC_SPINDLE |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O60333](https://www.uniprot.org/uniprotkb/O60333) (Kinesin-like protein KIF1B):

> Has a plus-end-directed microtubule motor activity and functions as a motor for transport of vesicles and organelles along microtubules.; [Isoform 2]: Has a plus-end-directed microtubule motor activity and functions as a motor for anterograde synaptic vesicle transport along axonal microtubules from the cell body to the presynapse in neuronal cells (By similarity). Functions as a downstream effector in a developmental apoptotic pathway that is activated when nerve growth factor (NGF) becomes …

**Summary**, from NCBI Gene [23095](https://www.ncbi.nlm.nih.gov/gene/23095):

> Enables plus-end-directed microtubule motor activity. Involved in apoptotic process involved in development and mitochondrion transport along microtubule. Is active in mitochondrion. Implicated in Charcot-Marie-Tooth disease type 2A1; hepatocellular carcinoma; multiple sclerosis; neuroblastoma; and ovary epithelial cancer. Biomarker of hepatocellular carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16636](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16636) · Entrez [23095](https://www.ncbi.nlm.nih.gov/gene/23095) · UniProt [O60333](https://www.uniprot.org/uniprotkb/O60333) · Ensembl [ENSG00000054523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054523)

## Data

Gene col 610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 610); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 610]; `tensor/DDL_lfc|DDL_z.npy` [610]; `embed/gene_vectors.npy` [610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 610 or target_col == 610). Every well: [[KIF1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
