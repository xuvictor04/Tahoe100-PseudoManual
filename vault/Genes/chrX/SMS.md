---
symbol: "SMS"
type: "gene"
col: 2221
ensembl_id: "ENSG00000102172"
name: "spermine synthase"
location: "Xp22.11"
module: 154
arm: "+"
pooled_cpm: 188.06
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 25
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# SMS

*spermine synthase* — Xp22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.20× (z +12.3, q 5e-32, up in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.36× (z +6.8, q 2e-09, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.635× (z -10.0, q 8e-21, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMIP]] (+0.64, fdr 1e-05), [[FLNB]] (+0.63, fdr 1e-05), [[GDPD5]] (+0.62, fdr 8e-05); moves opposite to [[PPP4R3A]] (-0.56, fdr 3e-05), [[DHRS4]] (-0.54, fdr 3e-04), [[LUC7L2]] (-0.53, fdr 4e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CAVIN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2221.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +12.3 | 5e-32 | 42/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +9.0 | 9e-17 | 39/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.36×** | +6.8 | 2e-09 | 36/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.48×** | +5.9 | 7e-07 | 40/46 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +5.8 | 1e-06 | 31/45 (LS 180, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.39×** | +5.2 | 2e-05 | 34/46 (SW480, AN3 CA, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.80×** | +4.8 | 1e-04 | 36/45 (KATO III, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.36×** | +4.8 | 1e-04 | 36/47 (AN3 CA, LS 180, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.63×** | +4.3 | 9e-04 | 35/47 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~73% of this change | **1.32×** | +4.3 | 9e-04 | 32/47 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 0.001 | 27/47 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.004 | 29/46 (SW480, AN3 CA, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.9 | 0.004 | 17/47 (RKO, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.2 | 0.049 | 17/47 (RKO, NCI-H460, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.15× | +3.1 | 0.075 | 9/48 (MIA PaCa-2, SHP-77, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2221.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -10.0 | 8e-21 | 36/48 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.599×** | -8.0 | 4e-13 | 38/47 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.614×** | -7.6 | 5e-12 | 36/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.614×** | -7.3 | 4e-11 | 35/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.767×** | -5.9 | 6e-07 | 32/47 (RKO, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.713×** | -5.3 | 1e-05 | 33/47 (MIA PaCa-2, HOP62, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.720×** | -5.1 | 3e-05 | 30/47 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.734×** | -4.8 | 1e-04 | 30/47 (H4, NCI-H460, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.564×** | -4.7 | 2e-04 | 38/48 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.753×** | -4.4 | 6e-04 | 27/47 (A549, BT-474, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.757×** | -4.3 | 7e-04 | 28/47 (H4, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.761×** | -4.3 | 1e-03 | 29/48 (A549, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.762×** | -4.2 | 1e-03 | 29/47 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~67% of this change | **0.759×** | -4.1 | 0.001 | 29/46 (NCI-H460, hTERT-HPNE, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.837× | -3.9 | 0.003 | 25/47 (A549, A-427, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.778×** | -3.9 | 0.003 | 29/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.850× | -3.6 | 0.011 | 18/47 (A549, A498, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.796×** | -3.6 | 0.011 | 23/47 (A549, HOP62, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.800×** | -3.5 | 0.013 | 27/47 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.788×** | -3.4 | 0.015 | 22/47 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.809×** | -3.3 | 0.024 | 23/47 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Encorafenib (drug)]] 5 µM |  | **0.683×** | -3.1 | 0.044 | 24/47 (AsPC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.824×** | -3.0 | 0.057 | 24/47 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2221. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 939 | 1 | 4 (3 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.86× (z +9.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -8.6) |
| [[PANC-1 (line)]] | alt | 189 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +13.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.397× (z -11.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 136 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -12.4) |
| [[J82 (line)]] | alt | 238 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -10.6) |
| [[HT-29 (line)]] | alt | 82.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.96× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 137 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.266× (z -12.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 266 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -12.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -11.7) |
| [[RKO (line)]] | wt | 186 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.94× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -16.3) |
| [[A-427 (line)]] | wt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 87.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +11.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 125 | 1 | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.01× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 207 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.519× (z -9.2) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.1) |
| [[H4 (line)]] | wt | 240 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -9.3) |
| [[HCT15 (line)]] | alt | 89.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 232 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 240 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -9.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 253 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -13.0) |
| [[LoVo (line)]] | wt | 87.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +13.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 102 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 189 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 144 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 65.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 347 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 74.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 147 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +15.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 347 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -11.6) |
| [[A549 (line)]] | wt | 212 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -13.2) |
| [[AN3 CA (line)]] | alt | 172 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 171 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -9.0) |
| [[BT-474 (line)]] | alt | 211 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 86.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 202 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.402× (z -9.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 88.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 118 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.18× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.9) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 82.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 198 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 476 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 90.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2221), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMIP]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[FLNB]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[GDPD5]] | +0.62 | +0.64 / +0.37 | both halves | 8e-05 |  |
| [[ADAMTS16]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[DRAP1]] | +0.61 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[PTPRF]] | +0.60 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[DTNA]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[MEAK7]] | +0.60 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[PIK3CD]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[CORO1C]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[LRRFIP1]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[EFL1]] | +0.57 | +0.58 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP4R3A]] | -0.56 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[DHRS4]] | -0.54 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[LUC7L2]] | -0.53 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[RPRD1B]] | -0.53 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[NCOA2]] | -0.53 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[DDX59]] | -0.52 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[MFSD14A]] | -0.52 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[EFCAB2]] | -0.52 | -0.56 / -0.22 | both halves | 6e-04 |  |
| [[CREBBP]] | -0.51 | -0.49 / -0.21 | both halves | 6e-04 |  |
| [[RAF1]] | -0.50 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[RNF146]] | -0.50 | -0.47 / -0.25 | both halves | 4e-04 |  |
| [[CASD1]] | -0.49 | -0.46 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAVIN1]] | B | CAVIN1 activity raises SMS's level | lines that do not express CAVIN1 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without CAVIN1 | 0.087 | ⚠ within organs, on part of the lines; also absent: NUAK1, SLC25A43, BLVRA |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.5, -2.2); signed map (-3.0, 44.0). **Vector** length 116, 40.8% of its response variance represented; |z| ≥ 3 in 1,457 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.7 | +2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.6 | +0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.6 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.5 | +6.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.7 | +5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.9 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | -1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~67% of this change | -6.5 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -5.1 | -5.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -5.0 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.3 | -5.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.9 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.7 | -4.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -3.4 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | spermine synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.11 — chrX:21,940,709-21,994,837 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPMSY, SpS, MRSR; previously SRS |
| Gene groups (HGNC) | 7BS non-methyltransferases |
| Hallmark sets | ANDROGEN_RESPONSE, FATTY_ACID_METABOLISM |
| Reactome | 2 pathways, smallest: Metabolism of polyamines; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P52788](https://www.uniprot.org/uniprotkb/P52788) (Spermine synthase):

> Catalyzes the production of spermine from spermidine and decarboxylated S-adenosylmethionine (dcSAM).

**Summary**, from NCBI Gene [6611](https://www.ncbi.nlm.nih.gov/gene/6611):

> This gene encodes a protein belonging to the spermidine/spermin synthase family and catalyzes the production of spermine from spermidine. Pseudogenes of this gene are located on chromosomes 1, 5, 6 and X. Mutations in this gene cause an X-linked intellectual disability called Snyder-Robinson Syndrome (SRS). Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:11123](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11123) · Entrez [6611](https://www.ncbi.nlm.nih.gov/gene/6611) · UniProt [P52788](https://www.uniprot.org/uniprotkb/P52788) · Ensembl [ENSG00000102172](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102172)

## Data

Gene col 2221: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2221); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2221, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2221]; `tensor/DDL_lfc|DDL_z.npy` [2221]; `embed/gene_vectors.npy` [2221]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2221 or target_col == 2221). Every well: [[SMS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
