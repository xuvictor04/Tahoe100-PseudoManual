---
symbol: "SEPTIN11"
type: "gene"
col: 6227
ensembl_id: "ENSG00000138758"
name: "septin 11"
location: "4q21.1"
module: 54
arm: "-"
pooled_cpm: 154.01
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# SEPTIN11

*septin 11* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.58× (z +24.9, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.58× (z +17.0, q 0e+00, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.621× (z -12.5, q 4e-33, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OXCT1]] (+0.70, fdr 7e-06), [[NID1]] (+0.64, fdr 1e-05), [[HNRNPK]] (+0.63, fdr 1e-05); moves opposite to [[MRPL55]] (-0.70, fdr 1e-05), [[RBIS]] (-0.69, fdr 1e-05), [[ATP5MJ]] (-0.67, fdr 1e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SPECC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +24.9 | 0e+00 | 47/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +24.7 | 0e+00 | 42/44 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +17.0 | 0e+00 | 30/48 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +16.4 | 0e+00 | 41/45 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +11.0 | 7e-26 | 33/49 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +10.1 | 7e-22 | 34/48 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +5.2 | 2e-05 | 24/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.23×** | +5.1 | 2e-05 | 23/47 (C32, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.20× | +4.8 | 1e-04 | 21/48 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.20× | +4.5 | 4e-04 | 23/50 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.14× | +3.5 | 0.025 | 18/48 (HOP62, KATO III, …) | top dose only | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.15× | +3.5 | 0.025 | 22/48 (SW480, SNU-423, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.13× | +3.1 | 0.072 | 18/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.072 | 9/48 (HS-578T, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.088 | 6/49 (hTERT-HPNE, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6227.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.621×** | -12.5 | 4e-33 | 37/48 (Hs 766T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.622×** | -12.4 | 4e-33 | 39/48 (Hs 766T, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.703×** | -9.3 | 4e-18 | 31/48 (Hs 766T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.775×** | -6.3 | 4e-08 | 29/48 (NCI-H2347, A498, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.805×** | -5.5 | 5e-06 | 24/47 (SNU-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.815×** | -5.4 | 7e-06 | 23/48 (LoVo, Hs 766T, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.798×** | -4.2 | 0.002 | 24/48 (BT-474, HEC-1-A, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.819×** | -3.7 | 0.013 | 20/48 (RKO, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.881× | -3.3 | 0.053 | 19/48 (LoVo, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.886× | -3.1 | 0.11 | 13/47 (AsPC-1, A-172, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | 0.800× | -3.1 | 0.11 | 17/46 (A-172, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.922× | -3.0 | 0.12 | 2/48 (HCT15, NCI-H661) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 191 | 6 (3 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +15.5) | [[Panobinostat (drug)]] 5 µM 0.477× (z -13.2) |
| [[SW480 (line)]] | alt | 111 | 6 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +21.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +18.8) | [[Panobinostat (drug)]] 5 µM 0.519× (z -11.7) |
| [[A-172 (line)]] | wt | 233 | 4 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.336× (z -16.9) |
| [[NCI-H1792 (line)]] | alt | 120 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 85.3 | 7 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.529× (z -10.1) |
| [[A-427 (line)]] | wt | 135 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.08× (z +16.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -16.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.499× (z -15.3) |
| [[AN3 CA (line)]] | alt | 838 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 135 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +24.6) | — |
| [[J82 (line)]] | alt | 172 | 4 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +18.0) | [[Panobinostat (drug)]] 5 µM 0.430× (z -12.4) |
| [[PANC-1 (line)]] | alt | 151 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +18.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.502× (z -12.0) |
| [[SNU-423 (line)]] | alt | 68.9 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +19.7) | — |
| [[A549 (line)]] | wt | 111 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +14.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -14.5) |
| [[HT-29 (line)]] | alt | 143 | 4 (2 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.514× (z -8.9) |
| [[LoVo (line)]] | wt | 146 | 3 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.79× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +10.0) | [[Ixazomib citrate (drug)]] 5 µM 0.519× (z -9.6) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.518× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 195 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +11.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.415× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 334 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +14.0) | [[Bortezomib (drug)]] 0.05 µM 0.522× (z -9.2) ⚠ cell-cycle shift, explains ~23% of this change |
| [[RPMI-7951 (line)]] | alt | 157 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.8) | — |
| [[A498 (line)]] | wt | 175 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +19.5) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.578× (z -9.0) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.612× (z -8.6) |
| [[HOP62 (line)]] | alt | 118 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +20.2) | — |
| [[KATO III (line)]] | alt | 105 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 80.7 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +18.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.471× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 196 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.454× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 55.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.57× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.54× (z +12.1) | — |
| [[C32 (line)]] | wt | 162 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +16.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 285 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.257× (z -17.7) |
| [[LS 180 (line)]] | wt | 150 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +13.2) | — |
| [[RKO (line)]] | wt | 205 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +13.6) | [[Panobinostat (drug)]] 0.5 µM 0.499× (z -11.0) |
| [[SHP-77 (line)]] | alt | 145 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +12.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.494× (z -10.1) |
| [[SW 900 (line)]] | alt | 122 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.6) | — |
| [[H4 (line)]] | wt | 121 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 125 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +14.6) | — |
| [[HS-578T (line)]] | alt | 117 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +16.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 72.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +18.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 142 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +15.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 130 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 81.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +18.5) | — |
| [[BT-474 (line)]] | alt | 321 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +16.3) | — |
| [[C-33 A (line)]] | alt | 222 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.59× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 83.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +15.1) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 294 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.181× (z -19.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.463× (z -8.9) |
| [[SW48 (line)]] | wt | 217 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.436× (z -10.3) |
| [[CHP-212 (line)]] | wt | 144 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 49.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 81.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 358 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OXCT1]] | +0.70 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[NID1]] | +0.64 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[HNRNPK]] | +0.63 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SEPTIN8]] | +0.63 | +0.61 / +0.49 | both halves | 1e-05 | same gene group; STRING 953 |
| [[GNG12]] | +0.63 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[EPB41L2]] | +0.62 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[SLC39A10]] | +0.61 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CDK6]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[STK26]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[FGD5-AS1]] | +0.60 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[USP13]] | +0.60 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[GALNT7]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL55]] | -0.70 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[RBIS]] | -0.69 | -0.53 / -0.72 | both halves | 1e-05 |  |
| [[ATP5MJ]] | -0.67 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.67 | -0.48 / -0.73 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MED10]] | -0.66 | -0.53 / -0.74 | both halves | 1e-05 |  |
| [[ATG4B]] | -0.66 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[TMEM208]] | -0.66 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[MED31]] | -0.65 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[CCDC127]] | -0.65 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[LAMTOR5]] | -0.64 | -0.46 / -0.68 | both halves | 3e-05 |  |
| [[ACAD10]] | -0.64 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[GOLPH3L]] | -0.64 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[VRK3]] | -0.63 | -0.61 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPECC1]] | B | SPECC1 activity lowers SEPTIN11's level | lines that do not express SPECC1 (6) vs lines expressing it (44) | 1.62× higher at baseline in the lines without SPECC1 | 0.064 | ⚠ within organs, on part of the lines; also absent: BMP8B, FARP1, KIAA1522 |
| [[FMNL3]] | B | FMNL3 activity raises SEPTIN11's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without FMNL3 | 0.091 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |
| [[STK26]] | B | STK26 activity lowers SEPTIN11's level | lines that do not express STK26 (5) vs lines expressing it (45) | 1.99× higher at baseline in the lines without STK26 | 0.094 | ⚠ across organs; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises SEPTIN11's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises SEPTIN11's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FLOT2]] | C | FLOT2's natural level strengthens SEPTIN11's drug response | FLOT2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.71, reverse -0.04; direction clear | 0.007 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |
| [[CDK6]] | C | CDK6 activity lowers SEPTIN11's level | lines that do not express CDK6 (4) vs lines expressing it (46) | 2.09× higher at baseline in the lines without CDK6 | 0.080 | ⚠ few lines (4 vs 46); across organs; also absent: FCHSD1, CDK6-AS1, PLS3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.678). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.8, -14.4); signed map (21.0, -34.7). **Vector** length 138, 42.0% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +24.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +17.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +24.7 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.3 | +1.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +3.0 | +1.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.4 | -12.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.9 | -12.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.9 | -6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.6 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.1 | -3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -5.0 | -4.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.6 | -2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.2 | -3.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | septin 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:76,949,751-77,040,384 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10849, Septin-11; previously SEPT11 |
| Gene groups (HGNC) | Septins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVA2](https://www.uniprot.org/uniprotkb/Q9NVA2) (Septin-11):

> Filament-forming cytoskeletal GTPase. May play a role in cytokinesis (Potential). May play a role in the cytoarchitecture of neurons, including dendritic arborization and dendritic spines, and in GABAergic synaptic connectivity (By similarity). During Listeria monocytogenes infection, not required for the bacterial entry process, but restricts its efficacy.

**Summary**, from NCBI Gene [55752](https://www.ncbi.nlm.nih.gov/gene/55752):

> SEPT11 belongs to the conserved septin family of filament-forming cytoskeletal GTPases that are involved in a variety of cellular functions including cytokinesis and vesicle trafficking (Hanai et al., 2004 [PubMed 15196925]; Nagata et al., 2004 [PubMed 15485874]).[supplied by OMIM, Jul 2009]

**Accessions** — [HGNC:25589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25589) · Entrez [55752](https://www.ncbi.nlm.nih.gov/gene/55752) · UniProt [Q9NVA2](https://www.uniprot.org/uniprotkb/Q9NVA2) · Ensembl [ENSG00000138758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138758)

## Data

Gene col 6227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6227); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6227]; `tensor/DDL_lfc|DDL_z.npy` [6227]; `embed/gene_vectors.npy` [6227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6227 or target_col == 6227). Every well: [[SEPTIN11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
