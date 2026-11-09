---
symbol: "PHACTR4"
type: "gene"
col: 12818
ensembl_id: "ENSG00000204138"
name: "phosphatase and actin regulator 4"
location: "1p35.3"
module: 20
arm: "-"
pooled_cpm: 165.59
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PHACTR4

*phosphatase and actin regulator 4* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.61× (z +18.0, q 0e+00, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.642× (z -11.0, q 3e-25, down in 35 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.696× (z -9.7, q 7e-20, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 14 lines (NCI-H23 0.348×, C-33 A 0.366×, MIA PaCa-2 0.362×, HEC-1-A 0.461×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.176×, SNU-1 0.172×, NCI-H23 0.339×, C-33 A 0.374×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.225×, PANC-1 0.481×; ⚠ toxic; transcription drop); [[Fluvoxamine (drug)]] 5 µM in 1 line (SW 1088 0.0842×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ING3]] (+0.62, fdr 7e-06), [[ZNFX1]] (+0.60, fdr 1e-05), [[HELZ2]] (+0.59, fdr 1e-05); moves opposite to [[LINC03009]] (-0.58, fdr 1e-05), [[ANKRD30BL]] (-0.57, fdr 4e-05), [[RPL10]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TXNIP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12818.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +18.0 | 0e+00 | 38/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +13.1 | 2e-36 | 30/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +12.2 | 7e-32 | 35/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +9.0 | 3e-17 | 31/48 (A-427, PANC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +8.8 | 1e-16 | 38/48 (NCI-H1573, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +5.5 | 3e-06 | 34/48 (A-172, HS-578T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +5.5 | 3e-06 | 14/49 (CFPAC-1, HCT15, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.23×** | +5.3 | 7e-06 | 26/47 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.20×** | +4.9 | 5e-05 | 25/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +4.8 | 1e-04 | 18/49 (CFPAC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +4.8 | 1e-04 | 9/48 (CFPAC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.17× | +4.2 | 1e-03 | 20/48 (J82, A-172, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.2 | 1e-03 | 18/50 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +4.1 | 0.002 | 13/48 (A-172, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.9 | 0.003 | 19/47 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.12× | +3.8 | 0.005 | 13/48 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.014 | 12/48 (NCI-H23, A549, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.034 | 9/49 (NCI-H23, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.09× | +3.2 | 0.046 | 11/48 (A498, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12818.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 14 lines (NCI-H23 0.348×, C-33 A 0.366×, MIA PaCa-2 0.362×, HEC-1-A 0.461×, …); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.176×, SNU-1 0.172×, NCI-H23 0.339×, C-33 A 0.374×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.225×, PANC-1 0.481×; ⚠ toxic; transcription drop); [[Fluvoxamine (drug)]] 5 µM in 1 line (SW 1088 0.0842×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.642×** | -11.0 | 3e-25 | 35/45 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.637×** | -10.5 | 3e-23 | 40/49 (RKO, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.696×** | -9.7 | 7e-20 | 38/48 (NCI-H23, C-33 A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.703×** | -9.1 | 2e-17 | 32/44 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -6.9 | 6e-10 | 25/49 (HEC-1-A, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.796×** | -5.9 | 4e-07 | 26/47 (C-33 A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.833×** | -4.9 | 7e-05 | 24/48 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.824×** | -4.9 | 7e-05 | 24/48 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.717×** | -4.6 | 2e-04 | 23/38 (HOP62, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.862× | -3.8 | 0.008 | 16/47 (SW 900, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.763×** | -3.8 | 0.008 | 20/45 (C-33 A, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.875× | -3.4 | 0.027 | 9/49 (A549, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.882× | -3.4 | 0.034 | 17/48 (LS 180, RKO, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.05 µM |  | 0.889× | -3.2 | 0.063 | 10/48 (HCT15, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.891× | -3.1 | 0.071 | 17/48 (C-33 A, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 126 | 5 (2 ⚠) | 6 (6 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +18.3) | [[Digitoxin (drug)]] 0.05 µM 0.528× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 249 | 4 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +18.9) | [[Auranofin (drug)]] 5 µM 0.348× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 172 | 5 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.5) | [[Auranofin (drug)]] 5 µM 0.362× (z -14.7) |
| [[A-427 (line)]] | wt | 248 | 6 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +15.9) | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -20.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 164 | 5 (4 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +12.3) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.474× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 166 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +23.4) | [[Dinaciclib (drug)]] 5 µM 0.507× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 112 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +23.8) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -16.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 209 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.99× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.481× (z -14.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 214 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.65× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.557× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.634× (z -10.2) |
| [[C-33 A (line)]] | alt | 346 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.366× (z -16.8) |
| [[C32 (line)]] | wt | 173 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +21.3) | [[Ponatinib (drug)]] 5 µM 0.550× (z -8.7) |
| [[HOP62 (line)]] | alt | 164 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +23.4) | [[Lonafarnib (drug)]] 5 µM 0.191× (z -14.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.518× (z -10.6) |
| [[HS-578T (line)]] | alt | 149 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +16.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 197 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.461× (z -13.9) |
| [[NCI-H2030 (line)]] | alt | 184 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.576× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 207 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +15.8) | — |
| [[A498 (line)]] | wt | 181 | 1 (1 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.516× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 67.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.34× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 182 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.6) | [[Auranofin (drug)]] 5 µM 0.382× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 93.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -10.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 176 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +14.4) | — |
| [[RKO (line)]] | wt | 219 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.421× (z -12.3) |
| [[SNU-1 (line)]] | wt | 175 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -16.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 165 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.09× (z +10.8) | [[Auranofin (drug)]] 5 µM 0.540× (z -9.0) |
| [[H4 (line)]] | wt | 146 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.18× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 205 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.499× (z -9.0) |
| [[Hs 766T (line)]] | wt | 149 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.13× (z +10.5) | — |
| [[KATO III (line)]] | alt | 129 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.548× (z -9.6) |
| [[LS 180 (line)]] | wt | 140 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.498× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -13.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 112 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.2) | [[Auranofin (drug)]] 5 µM 0.368× (z -11.1) |
| [[SNU-423 (line)]] | alt | 151 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.467× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 79.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.16× (z +8.8) | — |
| [[A549 (line)]] | wt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 156 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.6) | — |
| [[NCI-H2347 (line)]] | alt | 144 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.60× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 142 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.396× (z -10.7) |
| [[SHP-77 (line)]] | alt | 141 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.528× (z -8.6) |
| [[SW 1088 (line)]] | alt | 144 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0842× (z -10.8) |
| [[SW 1271 (line)]] | alt | 155 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.213× (z -8.5) |
| [[SW 900 (line)]] | alt | 113 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.2) | — |
| [[SW48 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 183 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 218 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 137 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 226 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ING3]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ZNFX1]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[HELZ2]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[FAM193A]] | +0.58 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[TMEM265]] | +0.58 | +0.43 / +0.64 | both halves | 4e-05 |  |
| [[EPC1]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[RELB]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[PIGBOS1]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[INO80]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[RBM10]] | +0.55 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[SRSF4]] | +0.54 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[MRPS18B]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03009]] | -0.58 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ANKRD30BL]] | -0.57 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[RPL10]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[TIMM10B]] | -0.56 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[RPS18]] | -0.55 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.54 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[ABHD17A]] | -0.53 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[UBFD1]] | -0.53 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[NAPB]] | -0.53 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[MSL3]] | -0.52 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[SDHAP4]] | -0.52 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[NSUN5P1]] | -0.52 | -0.47 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TXNIP]] | B | TXNIP activity lowers PHACTR4's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.40× higher at baseline in the lines without TXNIP | 0.014 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[IFI16]] | B | IFI16 activity lowers PHACTR4's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 1.37× higher at baseline in the lines without IFI16 | 0.036 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[GBP1]] | B | GBP1 activity lowers PHACTR4's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.37× higher at baseline in the lines without GBP1 | 0.064 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[HDAC6]] | B | HDAC6 activity lowers PHACTR4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PHACTR4's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM199X]] | C | FAM199X's natural level strengthens PHACTR4's drug response | FAM199X's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.15; direction not clear | 0.058 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.523). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (32.1, -37.0); signed map (5.9, -12.3). **Vector** length 128, 38.8% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +18.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +7.0 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.4 | +3.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.9 | +5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +3.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.4 | +2.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.0 | -9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.2 | -6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.4 | -11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.5 | -9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.2 | -10.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -4.1 | -3.8 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[Pemetrexed (drug)]] 0.5 µM |  | -2.7 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | phosphatase and actin regulator 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:28,369,582-28,500,364 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13171, PPP1R124 |
| Gene groups (HGNC) | Phosphatase and actin regulators; Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZ21](https://www.uniprot.org/uniprotkb/Q8IZ21) (Phosphatase and actin regulator 4):

> Regulator of protein phosphatase 1 (PP1) required for neural tube and optic fissure closure, and enteric neural crest cell (ENCCs) migration during development. Acts as an activator of PP1 by interacting with PPP1CA and preventing phosphorylation of PPP1CA at 'Thr-320'. During neural tube closure, localizes to the ventral neural tube and activates PP1, leading to down-regulate cell proliferation within cranial neural tissue and the neural retina. Also acts as a regulator of migration of enteric …

**Summary**, from NCBI Gene [65979](https://www.ncbi.nlm.nih.gov/gene/65979):

> This gene encodes a member of the phosphatase and actin regulator (PHACTR) family. Other PHACTR family members have been shown to inhibit protein phosphatase 1 (PP1) activity, and the homolog of this gene in the mouse has been shown to interact with actin and PP1. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:25793](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25793) · Entrez [65979](https://www.ncbi.nlm.nih.gov/gene/65979) · UniProt [Q8IZ21](https://www.uniprot.org/uniprotkb/Q8IZ21) · Ensembl [ENSG00000204138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204138)

## Data

Gene col 12818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12818); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12818]; `tensor/DDL_lfc|DDL_z.npy` [12818]; `embed/gene_vectors.npy` [12818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12818 or target_col == 12818). Every well: [[PHACTR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHACTR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
