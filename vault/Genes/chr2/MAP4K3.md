---
symbol: "MAP4K3"
type: "gene"
col: 247
ensembl_id: "ENSG00000011566"
name: "mitogen-activated protein kinase kinase kinase kinase 3"
location: "2p22.1"
module: 48
arm: "+"
pooled_cpm: 218.56
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# MAP4K3

*mitogen-activated protein kinase kinase kinase kinase 3* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.80× (z +13.8, q 2e-40, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.329× (z -25.1, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.647× (z -14.5, q 3e-45, down in 42 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (A549 0.338×, A-172 0.417×, NCI-H2347 0.326×, SW 900 0.430×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (A-172 0.175×, NCI-H23 0.176×, SHP-77 0.155×, SW480 0.221×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A498 0.212×, NCI-H1573 0.194×, SNU-1 0.170×, A-427 0.270×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (LoVo 0.416×, A-172 0.438×, SW 900 0.400×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.534×).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 30 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C4orf48]] (+0.55, fdr 1e-04), [[MRPS36]] (+0.53, fdr 2e-04, ⚠ MRPS36 in the vector space only through flagged drug-doses), [[POLR2J]] (+0.53, fdr 4e-05, ⚠ POLR2J in the vector space only through flagged drug-doses), [[ZNF609]] (+0.52, fdr 4e-05), [[SNX6]] (+0.51, fdr 4e-05); moves opposite to [[MAT2A]] (-0.49, fdr 4e-04), [[DPY19L3-DT]] (-0.48, fdr 5e-05), [[ZNF256]] (-0.48, fdr 9e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 247.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +13.8 | 2e-40 | 45/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +9.8 | 2e-20 | 44/48 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +9.2 | 1e-17 | 37/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +8.9 | 6e-17 | 41/48 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +8.4 | 6e-15 | 42/48 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +6.4 | 2e-08 | 37/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +5.4 | 4e-06 | 25/48 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +5.2 | 1e-05 | 25/47 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.22×** | +4.3 | 9e-04 | 24/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.2 | 0.002 | 21/48 (AsPC-1, PANC-1, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.002 | 23/47 (H4, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.003 | 21/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.008 | 21/48 (BT-474, H4, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.011 | 18/49 (A-427, J82, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.1 | 0.073 | 18/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 247.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 11 lines (A549 0.338×, A-172 0.417×, NCI-H2347 0.326×, SW 900 0.430×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (A-172 0.175×, NCI-H23 0.176×, SHP-77 0.155×, SW480 0.221×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A498 0.212×, NCI-H1573 0.194×, SNU-1 0.170×, A-427 0.270×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (LoVo 0.416×, A-172 0.438×, SW 900 0.400×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.534×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.329×** | -25.1 | 0e+00 | 43/44 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.368×** | -23.5 | 0e+00 | 49/49 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.416×** | -19.0 | 0e+00 | 43/45 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -14.5 | 3e-45 | 42/49 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.629×** | -10.0 | 3e-21 | 42/48 (SW 900, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.657×** | -9.8 | 7e-21 | 40/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.677×** | -9.2 | 5e-18 | 35/48 (LoVo, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.686×** | -8.5 | 1e-15 | 37/47 (RKO, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.722×** | -7.6 | 1e-12 | 36/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.782×** | -5.6 | 1e-06 | 29/50 (A-172, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.795×** | -5.4 | 4e-06 | 27/48 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -5.1 | 1e-05 | 20/48 (A-172, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.813×** | -4.7 | 1e-04 | 25/48 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.839× | -4.1 | 0.001 | 22/48 (A549, NCI-H2347, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.888× | -4.0 | 0.003 | 2/48 (SW48, COLO 205) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.872× | -3.1 | 0.065 | 10/49 (A-172, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 213 | 6 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -11.3) |
| [[SW 900 (line)]] | alt | 393 | 0 | 11 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -14.9) |
| [[A-172 (line)]] | wt | 174 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -26.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -19.7) |
| [[A549 (line)]] | wt | 317 | 2 | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -24.6) |
| [[NCI-H2347 (line)]] | alt | 289 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -18.9) |
| [[SNU-423 (line)]] | alt | 201 | 3 (1 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -11.7) |
| [[HT-29 (line)]] | alt | 171 | 3 (2 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -13.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 273 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -11.1) |
| [[A498 (line)]] | wt | 285 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -23.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -13.4) |
| [[HOP62 (line)]] | alt | 244 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -9.2) |
| [[SW480 (line)]] | alt | 220 | 1 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.83× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.519× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 315 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -11.2) |
| [[Hs 766T (line)]] | wt | 159 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -14.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 316 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 142 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.23× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.373× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.490× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 237 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.285× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 183 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +21.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -13.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 148 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.72× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +12.1) | — |
| [[C32 (line)]] | wt | 193 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -15.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 171 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.84× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -16.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 169 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -12.7) |
| [[KATO III (line)]] | alt | 178 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.97× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 311 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 113 | 2 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.56× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -9.2) |
| [[H4 (line)]] | wt | 186 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.472× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 418 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -18.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 186 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -17.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 170 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.416× (z -14.4) |
| [[LS 180 (line)]] | wt | 218 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 228 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -26.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 245 | 0 | 4 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0749× (z -18.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -9.6) |
| [[RKO (line)]] | wt | 199 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.193× (z -21.3) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 237 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -11.1) |
| [[SNU-1 (line)]] | wt | 155 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -9.7) |
| [[A-427 (line)]] | wt | 248 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -20.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 235 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.30× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -10.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 132 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 192 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -18.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 163 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.06× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -24.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 189 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -19.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 164 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -20.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 179 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -18.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 182 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -11.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 235 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 187 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 19 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C4orf48]] | +0.55 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[MRPS36]] ⚠ | +0.53 | +0.46 / +0.32 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[POLR2J]] ⚠ | +0.53 | +0.44 / +0.41 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UQCR10]] ⚠ | +0.52 | +0.45 / +0.30 | both halves | 2e-04 | pathway: HALLMARK_ADIPOGENESIS; ⚠ in the vector space only through flagged drug-doses |
| [[ZNF609]] | +0.52 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[SNX6]] | +0.51 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[UQCR11]] | +0.50 | +0.47 / +0.32 | both halves | 2e-04 | pathway: HALLMARK_ADIPOGENESIS |
| [[ATP5F1D]] ⚠ | +0.50 | +0.27 / +0.46 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL36]] | +0.50 | +0.26 / +0.36 | both halves | 3e-04 |  |
| [[NDUFB1]] | +0.50 | +0.37 / +0.36 | both halves | 1e-04 |  |
| [[COPS9]] | +0.50 | +0.44 / +0.31 | both halves | 2e-04 |  |
| [[DLG1]] | +0.49 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[TAOK3]] | +0.49 | +0.46 / +0.36 | both halves | 9e-05 |  |
| [[RABEP1]] | +0.49 | +0.25 / +0.48 | both halves | 4e-04 |  |
| [[EMC6]] | +0.48 | +0.34 / +0.31 | both halves | 2e-04 |  |
| [[TOMM7]] | +0.48 | +0.54 / +0.27 | both halves | 3e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAT2A]] | -0.49 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[DPY19L3-DT]] | -0.48 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[ZNF256]] | -0.48 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[PMPCA]] | -0.47 | -0.14 / -0.59 | ⚠ one half (not replicated) | 0.002 |  |
| [[U2AF2]] | -0.46 | -0.51 / -0.26 | both halves | 3e-04 |  |
| [[LINC03009]] | -0.46 | -0.08 / -0.42 | ⚠ not reproduced | 0.003 |  |
| [[PTPN18]] | -0.45 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[LY6G5B]] | -0.45 | -0.28 / -0.36 | both halves | 3e-04 |  |
| [[EEF1AKMT3]] | -0.44 | -0.13 / -0.49 | ⚠ not reproduced | 0.002 |  |
| [[PLXNB3]] | -0.44 | -0.11 / -0.42 | ⚠ not reproduced | 0.002 |  |
| [[CCAR2]] | -0.43 | -0.25 / -0.26 | both halves | 4e-04 |  |
| [[NRAS]] | -0.43 | -0.41 / -0.24 | both halves | 5e-04 |  |
| [[SORBS3]] | -0.43 | -0.41 / -0.25 | both halves | 4e-04 |  |
| [[RPSA]] | -0.43 | -0.33 / -0.29 | both halves | 3e-04 |  |
| [[SRSF1]] | -0.43 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[EIF4H]] | -0.42 | -0.33 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MAP4K3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.465). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-44.9, -18.8); signed map (-32.6, 7.8). **Vector** length 74.5, 23.0% of its response variance represented; |z| ≥ 3 in 1,319 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.0 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +9.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.3 | +5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.8 | +13.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +0.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.6 | +0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.2 | -9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.1 | -19.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.0 | -2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.8 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | +0.6 |
|  | [[Roxadustat (drug)]] 5 µM |  | -1.6 | +1.3 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.6 | +1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.1 — chr2:39,249,266-39,437,301 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GLK, MAPKKKK3; previously RAB8IPL1 |
| Gene groups (HGNC) | MAP4K family (GCK-I subfamily) |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVH8](https://www.uniprot.org/uniprotkb/Q8IVH8) (Mitogen-activated protein kinase kinase kinase kinase 3):

> Serine/threonine kinase that plays a role in the response to environmental stress. Appears to act upstream of the JUN N-terminal pathway. Activator of the Hippo signaling pathway which plays a pivotal role in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. MAP4Ks act in parallel to and are partially redundant with STK3/MST2 and STK4/MST2 in the phosphorylation and activation of LATS1/2, and establish MAP4Ks as components of the expanded Hippo …

**Summary**, from NCBI Gene [8491](https://www.ncbi.nlm.nih.gov/gene/8491):

> This gene encodes a member of the mitogen-activated protein kinase kinase kinase kinase family. The encoded protein activates key effectors in cell signalling, among them c-Jun. Alternatively spliced transcripts encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:6865](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6865) · Entrez [8491](https://www.ncbi.nlm.nih.gov/gene/8491) · UniProt [Q8IVH8](https://www.uniprot.org/uniprotkb/Q8IVH8) · Ensembl [ENSG00000011566](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011566)

## Data

Gene col 247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 247); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 247]; `tensor/DDL_lfc|DDL_z.npy` [247]; `embed/gene_vectors.npy` [247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 247 or target_col == 247). Every well: [[MAP4K3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP4K3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
