---
symbol: "ARHGAP10"
type: "gene"
col: 979
ensembl_id: "ENSG00000071205"
name: "Rho GTPase activating protein 10"
location: "4q31.23"
module: 210
arm: "+"
pooled_cpm: 87.72
n_lines_expressing: 47
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/210"]
generated_by: "tahoemap"
---

# ARHGAP10

*Rho GTPase activating protein 10* — 4q31.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 1.28× (z +4.7, q 1e-03, up in 29 of 46 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.20× (z +3.6, q 0.047, up in 20 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H460 2.67×, LS 180 1.79×, C32 2.42×; ⚠ cell-cycle shift, explains ~5% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (CFPAC-1 2.76×, BT-474 2.07×; ⚠ cell-cycle shift, explains ~96% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H23 3.50×, BT-474 2.79×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (BT-474 3.57×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (A-172 2.48×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.482× (z -14.0, q 5e-42, down in 42 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.681× (z -7.4, q 2e-11, down in 31 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 6 lines (A498 0.380×, SNU-423 0.377×, LOX-IMVI 0.400×, hTERT-HPNE 0.350×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW 900 0.0432×, SNU-1 0.132×, HCT15 0.180×, LoVo 0.308×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.0946×, hTERT-HPNE 0.171×, AsPC-1 0.313×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (RKO 0.339×, HCT15 0.365×, SNU-423 0.456×); [[Ferulic acid (drug)]] 0.05 µM in 1 line (SW 1271 0.0638×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUT8]] (+0.53, fdr 2e-05), [[UST]] (+0.53, fdr 3e-05), [[SPECC1]] (+0.53, fdr 5e-05); moves opposite to [[PPP1CB-DT]] (-0.42, fdr 7e-05), [[PDCD6P1]] (-0.40, fdr 1e-04), [[TSFM]] (-0.40, fdr 2e-04).
> It is in [[Module 210]], a single-armed module (tRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAMLD1]] → it (grade B ⚠); 2 go from it, the strongest it → [[UBOX5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 979.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H460 2.67×, LS 180 1.79×, C32 2.42×; ⚠ cell-cycle shift, explains ~5% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (CFPAC-1 2.76×, BT-474 2.07×; ⚠ cell-cycle shift, explains ~96% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H23 3.50×, BT-474 2.79×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (BT-474 3.57×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (A-172 2.48×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.28×** | +4.7 | 1e-03 | 29/46 (LS 180, NCI-H1792, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.6 | 1e-03 | 22/45 (NCI-H460, SW48, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.23×** | +3.9 | 0.018 | 21/45 (A-427, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.047 | 20/45 (BT-474, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.047 | 16/44 (NCI-H1573, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 1.20× | +3.4 | 0.055 | 18/45 (LS 180, A498, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | 1.12× | +3.1 | 0.15 | 18/45 (NCI-H1792, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Irinotecan (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.16 | 9/45 (PANC-1, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 979.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 6 lines (A498 0.380×, SNU-423 0.377×, LOX-IMVI 0.400×, hTERT-HPNE 0.350×, …); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW 900 0.0432×, SNU-1 0.132×, HCT15 0.180×, LoVo 0.308×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.0946×, hTERT-HPNE 0.171×, AsPC-1 0.313×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (RKO 0.339×, HCT15 0.365×, SNU-423 0.456×); [[Ferulic acid (drug)]] 0.05 µM in 1 line (SW 1271 0.0638×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.482×** | -14.0 | 5e-42 | 42/46 (RKO, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -12.1 | 2e-31 | 34/41 (SW 900, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.495×** | -12.0 | 5e-31 | 32/43 (A-172, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.680×** | -7.4 | 2e-11 | 36/45 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.681×** | -7.4 | 2e-11 | 31/45 (A498, SNU-423, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -7.0 | 2e-10 | 27/45 (RKO, HCT15, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.714×** | -6.2 | 4e-08 | 29/44 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.782×** | -4.7 | 2e-04 | 24/45 (SNU-423, A498, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | 0.844× | -4.6 | 2e-04 | 23/45 (AN3 CA, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.861× | -4.1 | 0.003 | 20/46 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.831×** | -3.4 | 0.033 | 18/47 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.854× | -3.0 | 0.12 | 14/45 (HOP62, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 107 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.377× (z -10.9) |
| [[BT-474 (line)]] | alt | 117 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.57× (z +11.6) | — |
| [[A-172 (line)]] | wt | 86.2 | 2 (1 ⚠) | 3 (3 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.48× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -14.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 106 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.380× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 235 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.350× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 111 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.289× (z -13.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.400× (z -10.1) |
| [[LS 180 (line)]] | wt | 105 | 2 (2 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.4) ⚠ cell-cycle shift, explains ~5% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 167 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -12.9) ⚠ cell-cycle shift, explains ~5% of this change |
| [[AsPC-1 (line)]] | alt | 168 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -17.3) ⚠ cell-cycle shift, explains ~5% of this change |
| [[CFPAC-1 (line)]] | alt | 75.3 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +16.2) ⚠ cell-cycle shift, explains ~96% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.293× (z -13.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 113 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -13.3) ⚠ cell-cycle shift, explains ~96% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.272× (z -8.9) |
| [[Hs 766T (line)]] | wt | 108 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.7) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.352× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 30.7 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.50× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -11.0) ⚠ cell-cycle shift, explains ~14% of this change |
| [[NCI-H460 (line)]] | wt | 47.5 | 3 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +16.1) ⚠ cell-cycle shift, explains ~5% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.402× (z -9.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 119 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0946× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -11.0) |
| [[HCT15 (line)]] | alt | 130 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.365× (z -9.9) |
| [[LoVo (line)]] | wt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 127 | 1 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.87× (z +11.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -11.9) ⚠ cell-cycle shift, explains ~96% of this change |
| [[NCI-H1792 (line)]] | alt | 125 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 68.3 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.234× (z -14.0) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 126 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.416× (z -8.7) |
| [[PANC-1 (line)]] | alt | 71.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.426× (z -11.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 88.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0432× (z -30.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -18.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 62.7 | 0 | 2 | — | [[Ferulic acid (drug)]] 0.05 µM 0.0638× (z -9.4) |
| [[SW48 (line)]] | wt | 138 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -10.0) ⚠ cell-cycle shift, explains ~96% of this change |
| [[SW480 (line)]] | alt | 53.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 74.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -10.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -14.5) ⚠ cell-cycle shift, explains ~96% of this change |
| [[C-33 A (line)]] | alt | 77.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -10.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 43.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.2) ⚠ cell-cycle shift, explains ~5% of this change | — |
| [[H4 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -10.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 63.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.427× (z -9.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 96.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -10.0) ⚠ cell-cycle shift, explains ~5% of this change |
| [[J82 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.440× (z -9.2) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -9.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.95 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUT8]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 | same gene group |
| [[UST]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[SPECC1]] | +0.53 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[FAM110B]] | +0.50 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[MCC]] | +0.49 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[SLCO3A1]] | +0.49 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[NTN1]] | +0.49 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[PLEKHA5]] | +0.48 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[KALRN]] | +0.47 | +0.44 / +0.44 | both halves | 3e-05 | same gene group; pathway: RAC1 GTPase cycle |
| [[CACHD1]] | +0.46 | +0.37 / +0.41 | both halves | 7e-05 | same gene group |
| [[SSH2]] | +0.46 | +0.34 / +0.48 | both halves | 1e-04 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[CACNA1C]] | +0.44 | +0.45 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1CB-DT]] | -0.42 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[PDCD6P1]] | -0.40 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[TSFM]] | -0.40 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[SNED1-AS1]] | -0.40 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[VCPKMT]] | -0.39 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[UBOX5]] | -0.39 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[RAB11B-AS1]] | -0.38 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[MTERF4]] | -0.38 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[ADAM20P1]] | -0.38 | -0.24 / -0.41 | both halves | 4e-04 |  |
| [[RUSF1]] | -0.37 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[SLC28A2-AS1]] | -0.37 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[KHDC4]] | -0.37 | -0.36 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAMLD1]] | B | MAMLD1 activity raises ARHGAP10's level | lines that do not express MAMLD1 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without MAMLD1 | 0.016 | ⚠ within organs, on part of the lines; also absent: FHOD3, PGM5P2-1, CAV1 |
| [[CHRNA7]] | B | CHRNA7 activity weakens ARHGAP10's drug response | lines that do not express CHRNA7 (16) vs lines expressing it (30) | the lines without CHRNA7 respond 1.97× as strongly (z diff -2.27); strongest at Panobinostat 5 µM: 0.59x vs 0.93x (z diff -4.8) | 0.047 | ⚠ within organs, on part of the lines; also absent: LRRC4B, NKD2, IGFL4; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[UST]] | B | UST activity raises ARHGAP10's level | lines that do not express UST (12) vs lines expressing it (38) | 2.08× lower at baseline in the lines without UST | 0.086 | ⚠ within organs, on part of the lines; also absent: SLC1A1, SH3GL3 |
| [[MECOM]] | B | MECOM activity strengthens ARHGAP10's drug response | lines that do not express MECOM (16) vs lines expressing it (30) | the lines without MECOM respond 0.67× as strongly (z diff +1.42); strongest at Auranofin 5 µM: 0.86x vs 0.63x (z diff +2.9) | 0.098 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBOX5]] | C | ARHGAP10 activity lowers UBOX5's level | lines that do not express ARHGAP10 (3) vs lines expressing it (47) | 1.63× higher at baseline in the lines without ARHGAP10 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2; its own permutation p |
| [[MAMLD1]] | C | ARHGAP10 activity raises MAMLD1's level | lines that do not express ARHGAP10 (3) vs lines expressing it (47) | 7.37× lower at baseline in the lines without ARHGAP10 | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2 |

## Where it sits

- **Module**: [[Module 210]] — tRNA processing; 13 genes; every member is in the + arm (projection on the module's main direction -0.392). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.3, 39.4); signed map (41.8, -16.9). **Vector** length 105, 28.8% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | +4.1 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +1.6 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.1 | -12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -7.0 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.9 | -0.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.23 — chr4:147,732,063-148,072,776 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20896, FLJ41791, GRAF2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; AH/BAR family Rho GTPase activating proteins; SH3 domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 9 pathways, smallest: Regulation of Apoptosis; RHOA GTPase cycle; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [A1A4S6](https://www.uniprot.org/uniprotkb/A1A4S6) (Rho GTPase-activating protein 10):

> GTPase-activating protein that catalyzes the conversion of active GTP-bound Rho GTPases to their inactive GDP-bound form, thus suppressing various Rho GTPase-mediated cellular processes. Also converts Cdc42 to an inactive GDP-bound state. Essential for PTKB2 regulation of cytoskeletal organization via Rho family GTPases. Inhibits PAK2 proteolytic fragment PAK-2p34 kinase activity and changes its localization from the nucleus to the perinuclear region. Stabilizes PAK-2p34 thereby increasing …

**Summary**, from NCBI Gene [79658](https://www.ncbi.nlm.nih.gov/gene/79658):

> Predicted to enable GTPase activator activity. Predicted to be involved in cytoskeleton organization and negative regulation of apoptotic process. Located in cytosol and endosome membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26099](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26099) · Entrez [79658](https://www.ncbi.nlm.nih.gov/gene/79658) · UniProt [A1A4S6](https://www.uniprot.org/uniprotkb/A1A4S6) · Ensembl [ENSG00000071205](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071205)

## Data

Gene col 979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 979); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 979]; `tensor/DDL_lfc|DDL_z.npy` [979]; `embed/gene_vectors.npy` [979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 979 or target_col == 979). Every well: [[ARHGAP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
