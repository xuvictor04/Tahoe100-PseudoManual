---
symbol: "TBC1D19"
type: "gene"
col: 3071
ensembl_id: "ENSG00000109680"
name: "TBC1 domain family member 19"
location: "4p15.2"
module: 17
arm: "+"
pooled_cpm: 50.75
n_lines_expressing: 46
n_dd_up: 20
n_dd_down: 18
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 10
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# TBC1D19

*TBC1 domain family member 19* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.92× (z +9.3, q 1e-17, up in 33 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.328× (z -22.3, q 0e+00, down in 44 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR7]] (+0.76, fdr 7e-06), [[BBS5]] (+0.69, fdr 1e-05), [[IFTAP]] (+0.68, fdr 1e-05); moves opposite to [[CCDC168]] (-0.60, fdr 2e-05), [[TPTEP2-CSNK1E]] (-0.59, fdr 1e-05), [[ZFYVE27]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PKIG]] → it (grade B ⚠); 10 go from it, the strongest it → [[WDR7]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3071.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +9.3 | 1e-17 | 33/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +9.1 | 2e-17 | 34/44 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +7.5 | 1e-11 | 33/44 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +6.1 | 2e-07 | 28/44 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +5.1 | 4e-05 | 26/44 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.44×** | +4.9 | 1e-04 | 24/44 (C32, LoVo, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.6 | 3e-04 | 28/44 (hTERT-HPNE, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +4.4 | 6e-04 | 24/44 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +4.4 | 8e-04 | 27/44 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.24×** | +4.3 | 9e-04 | 21/44 (LS 180, H4, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +4.3 | 0.001 | 21/43 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.33×** | +4.0 | 0.003 | 22/44 (SNU-1, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.30×** | +3.6 | 0.015 | 16/43 (SW48, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.018 | 18/44 (LoVo, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.019 | 20/43 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.021 | 18/44 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +3.1 | 0.052 | 21/45 (SNU-423, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.079 | 14/43 (SW480, RKO, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.081 | 16/44 (LS 180, SW48, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3071.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.328×** | -22.3 | 0e+00 | 44/44 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.363×** | -13.8 | 9e-41 | 39/44 (A-172, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.460×** | -11.0 | 8e-26 | 39/44 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.494×** | -10.0 | 2e-21 | 37/43 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.505×** | -9.7 | 4e-20 | 33/44 (SW480, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.510×** | -9.2 | 4e-18 | 37/44 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.526×** | -9.1 | 7e-18 | 34/44 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.561×** | -7.9 | 3e-13 | 35/43 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.594×** | -7.4 | 1e-11 | 33/44 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.634×** | -6.4 | 7e-09 | 29/44 (NCI-H1573, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.636×** | -5.9 | 2e-07 | 25/40 (RPMI-7951, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.690×** | -5.0 | 2e-05 | 23/38 (LOX-IMVI, NCI-H1792, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.744×** | -4.2 | 0.001 | 25/44 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **0.756×** | -4.0 | 0.003 | 21/42 (HCT15, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.761×** | -3.9 | 0.004 | 22/43 (MIA PaCa-2, NCI-H2030, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.853× | -3.2 | 0.052 | 17/44 (HOP62, SNU-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.859× | -3.0 | 0.069 | 18/44 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3071. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 78.6 | 4 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +34.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0872× (z -21.4) |
| [[SW480 (line)]] | alt | 44.1 | 0 | 11 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -18.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -16.7) |
| [[HOP62 (line)]] | alt | 49.9 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -18.8) |
| [[LoVo (line)]] | wt | 35.7 | 4 | 5 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.48× (z +13.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -13.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.258× (z -12.5) |
| [[PANC-1 (line)]] | alt | 18.7 | 3 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.88× (z +10.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -12.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 33.2 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0594× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -15.9) |
| [[LS 180 (line)]] | wt | 37.8 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.69× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -11.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.274× (z -9.5) |
| [[HCT15 (line)]] | alt | 68.0 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -15.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 71.4 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -17.7) |
| [[J82 (line)]] | alt | 41.1 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -17.2) |
| [[Panc 03.27 (line)]] | alt | 40.4 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -19.4) |
| [[RPMI-7951 (line)]] | alt | 64.4 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -16.4) |
| [[SNU-423 (line)]] | alt | 127 | 2 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +17.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -15.3) |
| [[H4 (line)]] | wt | 98.6 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -10.6) |
| [[HT-29 (line)]] | alt | 30.3 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -15.0) |
| [[hTERT-HPNE (line)]] | wt | 54.3 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 9.81× (z +20.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 145 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.165× (z -12.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 133 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -19.0) |
| [[AN3 CA (line)]] | alt | 63.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -17.2) |
| [[NCI-H1573 (line)]] | alt | 48.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 40.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 59.7 | 1 (1 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 3.82× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -14.7) |
| [[A-427 (line)]] | wt | 36.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[A498 (line)]] | wt | 52.3 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.53× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -16.3) |
| [[A549 (line)]] | wt | 35.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -10.8) |
| [[C32 (line)]] | wt | 67.6 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -14.1) |
| [[CFPAC-1 (line)]] | alt | 72.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -18.0) |
| [[Hs 766T (line)]] | wt | 21.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 41.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 26.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -9.7) |
| [[RKO (line)]] | wt | 42.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -10.9) |
| [[SHP-77 (line)]] | alt | 32.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -10.5) |
| [[SW1417 (line)]] | alt | 20.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -11.5) |
| [[CHP-212 (line)]] | wt | 126 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -14.6) |
| [[HS-578T (line)]] | alt | 58.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -11.0) |
| [[SW 900 (line)]] | alt | 72.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -15.5) |
| [[AsPC-1 (line)]] | alt | 9.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3071), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR7]] | +0.76 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[BBS5]] | +0.69 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[IFTAP]] | +0.68 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[TTC26]] | +0.68 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[NDUFA8]] | +0.67 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[NPHP1]] | +0.67 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ZSCAN26]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[TTC5]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[DNAAF4]] | +0.65 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[NUDT12]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ESD]] | +0.63 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[TTBK2]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 | STRING 493 |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC168]] | -0.60 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.59 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[ZFYVE27]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | -0.58 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[BCL2L2-PABPN1]] | -0.57 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[MSL1]] | -0.56 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[WDR20]] | -0.56 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[ZNF460-AS1]] | -0.55 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[SIAH2-AS1]] | -0.54 | -0.23 / -0.46 | both halves | 5e-04 |  |
| [[PRDM10]] | -0.54 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[CDK2AP1]] | -0.53 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[PTGR3]] | -0.53 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKIG]] | B | PKIG activity raises TBC1D19's level | lines that do not express PKIG (6) vs lines expressing it (44) | 2.80× lower at baseline in the lines without PKIG | 0.069 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[MAP9]] | B | MAP9 activity raises TBC1D19's level | lines that do not express MAP9 (17) vs lines expressing it (33) | 2.22× lower at baseline in the lines without MAP9 | 0.095 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, RNF150, BVES |
| [[DYNC2H1]] | C | DYNC2H1 activity raises TBC1D19's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 2.85× lower at baseline in the lines without DYNC2H1 | 0.074 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR7]] | C | TBC1D19 activity raises WDR7's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without TBC1D19 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |
| [[SAAL1]] | C | TBC1D19 activity raises SAAL1's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 2.11× lower at baseline in the lines without TBC1D19 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |
| [[PKIG]] | C | TBC1D19 activity raises PKIG's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 3.83× lower at baseline in the lines without TBC1D19 | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent |
| [[DYNC2H1]] | C | TBC1D19 activity raises DYNC2H1's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 6.48× lower at baseline in the lines without TBC1D19 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[AGK]] | C | TBC1D19 activity raises AGK's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 4.02× lower at baseline in the lines without TBC1D19 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |
| [[IRAK1BP1]] | C | TBC1D19 activity raises IRAK1BP1's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 2.89× lower at baseline in the lines without TBC1D19 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[TTC26]] | C | TBC1D19 activity raises TTC26's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 2.33× lower at baseline in the lines without TBC1D19 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |
| [[ZFP1]] | C | TBC1D19 activity raises ZFP1's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without TBC1D19 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |
| [[WDR70]] | C | TBC1D19 activity raises WDR70's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without TBC1D19 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |
| [[TTC1]] | C | TBC1D19 activity raises TTC1's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 1.30× lower at baseline in the lines without TBC1D19 | 0.0996 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.656). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.0, -0.5); signed map (-21.4, -17.7). **Vector** length 101, 28.0% of its response variance represented; |z| ≥ 3 in 1,292 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Assembly of the 9+0 primary cilium* (reactome, mean cos +0.54 to 11); *Intraflagellar transport* (reactome, mean cos +0.52 to 6); *Cilium Assembly* (reactome, mean cos +0.54 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.0 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | +5.6 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +4.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.8 | -22.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -9.7 | -13.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.7 | -11.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | -9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:26,576,437-26,756,223 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11082 |
| Gene groups (HGNC) | Tubulin polyglutamylase complex subunits; TBC1 domain family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5T2](https://www.uniprot.org/uniprotkb/Q8N5T2) (TBC1 domain family member 19):

> May act as a GTPase-activating protein for Rab family protein(s).

**Summary**, from NCBI Gene [55296](https://www.ncbi.nlm.nih.gov/gene/55296):

> Predicted to enable GTPase activator activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25624](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25624) · Entrez [55296](https://www.ncbi.nlm.nih.gov/gene/55296) · UniProt [Q8N5T2](https://www.uniprot.org/uniprotkb/Q8N5T2) · Ensembl [ENSG00000109680](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109680)

## Data

Gene col 3071: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3071); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3071, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3071]; `tensor/DDL_lfc|DDL_z.npy` [3071]; `embed/gene_vectors.npy` [3071]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3071 or target_col == 3071). Every well: [[TBC1D19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
