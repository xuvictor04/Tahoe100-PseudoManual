---
symbol: "RPN2"
type: "gene"
col: 4014
ensembl_id: "ENSG00000118705"
name: "ribophorin II"
location: "20q11.23"
module: 42
arm: "+"
pooled_cpm: 129.66
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# RPN2

*ribophorin II* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.30× (z +14.3, q 8e-44, up in 45 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.05× (z +9.6, q 1e-19, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.696× (z -8.8, q 5e-16, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDIA3]] (+0.76, fdr 7e-06), [[DDOST]] (+0.75, fdr 7e-06), [[PDIA6]] (+0.74, fdr 7e-06); moves opposite to [[ZNF286B]] (-0.59, fdr 1e-05), [[TNIP2]] (-0.58, fdr 1e-05), [[FNTA]] (-0.57, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4014.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.30×** | +14.3 | 8e-44 | 45/49 (KATO III, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.07×** | +12.0 | 8e-31 | 35/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.05×** | +9.6 | 1e-19 | 47/49 (RKO, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.83×** | +9.6 | 1e-19 | 43/45 (KATO III, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.34×** | +7.1 | 2e-10 | 33/49 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.18×** | +6.7 | 2e-09 | 35/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.45×** | +6.4 | 1e-08 | 35/48 (LS 180, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.45×** | +6.4 | 1e-08 | 38/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.39×** | +5.5 | 3e-06 | 34/50 (A-427, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.34×** | +4.8 | 1e-04 | 26/48 (SNU-423, RKO, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.25×** | +3.8 | 0.007 | 25/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.25×** | +3.8 | 0.008 | 24/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.017 | 23/48 (HT-29, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~88% of this change | **1.22×** | +3.3 | 0.039 | 24/47 (COLO 205, Panc 03.27, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.3 | 0.039 | 21/37 (Panc 03.27, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.039 | 22/48 (CFPAC-1, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4014.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.696×** | -8.8 | 5e-16 | 34/48 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.719×** | -5.7 | 3e-06 | 31/48 (HS-578T, SW 1088, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.724×** | -5.2 | 5e-05 | 35/47 (HS-578T, A-172, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.746×** | -5.1 | 6e-05 | 25/48 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.761×** | -4.5 | 6e-04 | 32/49 (HepG2/C3A, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.778×** | -4.3 | 0.001 | 23/48 (A-172, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.649×** | -3.7 | 0.014 | 30/50 (HS-578T, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.669×** | -3.5 | 0.034 | 28/49 (J82, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.830×** | -3.2 | 0.063 | 19/48 (KATO III, CFPAC-1, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.690×** | -3.2 | 0.063 | 20/48 (J82, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.878× | -3.2 | 0.063 | 14/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.826×** | -3.2 | 0.063 | 21/47 (SW480, C32, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **0.832×** | -3.2 | 0.063 | 21/48 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.835× | -3.1 | 0.074 | 22/48 (C32, RKO, …) | two highest doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.701×** | -3.1 | 0.078 | 20/49 (J82, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.884× | -3.0 | 0.084 | 8/48 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.841× | -3.0 | 0.087 | 18/48 (SNU-423, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4014. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 133 | 6 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.62× (z +12.2) | — |
| [[A-172 (line)]] | wt | 109 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -13.7) |
| [[HOP62 (line)]] | alt | 95.8 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -9.4) |
| [[J82 (line)]] | alt | 183 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -13.3) |
| [[HS-578T (line)]] | alt | 165 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -14.9) |
| [[KATO III (line)]] | alt | 219 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 185 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 134 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -9.8) |
| [[RKO (line)]] | wt | 156 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 7.03× (z +12.5) | — |
| [[A-427 (line)]] | wt | 130 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 78.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.86× (z +8.8) | — |
| [[C32 (line)]] | wt | 114 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 113 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.25× (z +8.7) | — |
| [[H4 (line)]] | wt | 127 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 90.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.19× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 106 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 112 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 166 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -14.0) |
| [[SK-MEL-2 (line)]] | alt | 145 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -8.7) |
| [[SNU-423 (line)]] | alt | 117 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW 900 (line)]] | alt | 140 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.41× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -9.6) |
| [[A498 (line)]] | wt | 129 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[A549 (line)]] | wt | 81.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[C-33 A (line)]] | alt | 92.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[LS 180 (line)]] | wt | 147 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.51× (z +13.7) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[NCI-H23 (line)]] | alt | 162 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 117 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HepG2_C3A (line)]] | wt | 192 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.440× (z -8.9) |
| [[Hs 766T (line)]] | wt | 208 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.328× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 185 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +14.3) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[Panc 03.27 (line)]] | alt | 84.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SHP-77 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -8.5) |
| [[SW 1088 (line)]] | alt | 191 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.133× (z -10.3) |
| [[SW1417 (line)]] | alt | 206 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.2) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[SW48 (line)]] | wt | 91.3 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.09× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 103 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 94.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4014), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA3]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 671 |
| [[DDOST]] | +0.75 | +0.77 / +0.75 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 999 |
| [[PDIA6]] | +0.74 | +0.74 / +0.74 | both halves | 7e-06 | STRING 842 |
| [[MLEC]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 991 |
| [[GANAB]] | +0.67 | +0.68 / +0.64 | both halves | 7e-06 | pathway: Adherens junctions interactions; STRING 662 |
| [[PDIA4]] | +0.66 | +0.70 / +0.64 | both halves | 7e-06 | STRING 524 |
| [[SPARC]] | +0.65 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[TMED10]] | +0.63 | +0.64 / +0.63 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 633 |
| [[LMAN2]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 407 |
| [[CALR]] | +0.61 | +0.67 / +0.60 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 681 |
| [[TMED4]] | +0.60 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[PIGS]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF286B]] | -0.59 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[TNIP2]] | -0.58 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[FNTA]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[DAXX]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[CPEB1]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[GLRX2]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ZNF197]] | -0.54 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[TIPRL]] | -0.54 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ZNF354A]] | -0.54 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[ZNF525]] | -0.51 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[TRAPPC3]] | -0.51 | -0.42 / -0.57 | both halves | 4e-05 | pathway: Asparagine N-linked glycosylation |
| [[NECAP2]] | -0.51 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RPN2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.9, -21.8); signed map (-55.5, 6.2). **Vector** length 118, 40.9% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.56 to 11); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.56 to 9); *IRE1alpha activates chaperones* (reactome, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.6 | +9.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.4 | +6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.4 | +5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.9 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +4.0 | +9.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.6 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.3 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.2 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.8 | -8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.7 | -5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.0 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | ribophorin II |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:37,178,410-37,241,619 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SWP1, RPNII, RIBIIR, RPN-II |
| Gene groups (HGNC) | Oligosaccharyltransferase complex subunits |
| Reactome | 26 pathways, smallest: PD-L1(CD274) glycosylation and translocation to plasma membrane; Regulation of CDH1 posttranslational processing and trafficking to plasma membrane; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [P04844](https://www.uniprot.org/uniprotkb/P04844) (Dolichyl-diphosphooligosaccharide--protein glycosyltransferase subunit 2):

> Subunit of the oligosaccharyl transferase (OST) complex that catalyzes the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2) in eukaryotes) from the lipid carrier dolichol-pyrophosphate to an asparagine residue within an Asn-Xaa-Ser/Thr consensus motif in nascent polypeptide chains, the first step in protein N-glycosylation. N-glycosylation occurs cotranslationally and the complex associates with the Sec61 complex at the channel-forming translocon complex that mediates protein …

**Summary**, from NCBI Gene [6185](https://www.ncbi.nlm.nih.gov/gene/6185):

> This gene encodes a type I integral membrane protein found only in the rough endoplasmic reticulum. The encoded protein is part of an N-oligosaccharyl transferase complex that links high mannose oligosaccharides to asparagine residues found in the Asn-X-Ser/Thr consensus motif of nascent polypeptide chains. This protein is similar in sequence to the yeast oligosaccharyl transferase subunit SWP1. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:10382](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10382) · Entrez [6185](https://www.ncbi.nlm.nih.gov/gene/6185) · UniProt [P04844](https://www.uniprot.org/uniprotkb/P04844) · Ensembl [ENSG00000118705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118705)

## Data

Gene col 4014: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4014); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4014, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4014]; `tensor/DDL_lfc|DDL_z.npy` [4014]; `embed/gene_vectors.npy` [4014]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4014 or target_col == 4014). Every well: [[RPN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
