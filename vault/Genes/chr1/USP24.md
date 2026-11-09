---
symbol: "USP24"
type: "gene"
col: 8509
ensembl_id: "ENSG00000162402"
name: "ubiquitin specific peptidase 24"
location: "1p32.3"
module: 1
arm: "+"
pooled_cpm: 177.08
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# USP24

*ubiquitin specific peptidase 24* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.77× (z +9.9, q 2e-20, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.284× (z -21.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTPAP]] (+0.69, fdr 3e-05), [[ZZZ3]] (+0.68, fdr 7e-06), [[SCAF8]] (+0.67, fdr 1e-05); moves opposite to [[SEC22B]] (-0.67, fdr 3e-05), [[TMEM184B]] (-0.65, fdr 6e-05), [[TMED9]] (-0.64, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TMEM92-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +9.9 | 2e-20 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +9.7 | 1e-19 | 35/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +7.4 | 3e-11 | 43/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.36×** | +7.0 | 4e-10 | 44/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +6.9 | 7e-10 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +6.5 | 1e-08 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.16×** | +6.2 | 4e-08 | 40/48 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.9 | 8e-05 | 33/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.26×** | +4.0 | 0.004 | 27/48 (A498, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.007 | 26/48 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.012 | 27/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.017 | 26/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.017 | 24/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.21×** | +3.1 | 0.070 | 23/48 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.084 | 22/48 (SW480, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8509.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.284×** | -21.9 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.289×** | -21.6 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.360×** | -17.8 | 0e+00 | 48/48 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.465×** | -13.3 | 3e-38 | 47/49 (HCT15, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.531×** | -10.6 | 3e-24 | 40/44 (A549, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.566×** | -9.9 | 4e-21 | 46/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.580×** | -8.8 | 1e-16 | 36/45 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.618×** | -8.4 | 4e-15 | 46/48 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.629×** | -7.8 | 5e-13 | 46/47 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.734×** | -7.6 | 2e-12 | 34/49 (RKO, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.659×** | -7.3 | 2e-11 | 45/48 (BT-474, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -6.0 | 9e-08 | 35/48 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.763×** | -4.7 | 1e-04 | 38/49 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.781×** | -4.3 | 7e-04 | 27/48 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.800×** | -3.7 | 0.007 | 30/50 (H4, HOP62, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.636×** | -3.7 | 0.009 | 25/49 (SK-MEL-2, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 143 | 10 (2 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +14.7) | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -17.3) |
| [[SW480 (line)]] | alt | 207 | 5 (1 ⚠) | 9 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.214× (z -23.7) |
| [[A-172 (line)]] | wt | 126 | 2 | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -18.3) |
| [[HEC-1-A (line)]] | alt | 238 | 1 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.210× (z -19.5) |
| [[LoVo (line)]] | wt | 165 | 3 (2 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.270× (z -18.2) |
| [[PANC-1 (line)]] | alt | 225 | 6 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +23.6) | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -17.5) |
| [[HS-578T (line)]] | alt | 200 | 2 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.237× (z -18.7) |
| [[SNU-423 (line)]] | alt | 144 | 1 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -19.1) |
| [[MIA PaCa-2 (line)]] | alt | 248 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -21.6) |
| [[RKO (line)]] | wt | 241 | 1 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -16.9) |
| [[SW48 (line)]] | wt | 256 | 1 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.210× (z -15.5) |
| [[A498 (line)]] | wt | 126 | 3 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +18.2) | [[Panobinostat (drug)]] 5 µM 0.283× (z -16.0) |
| [[A549 (line)]] | wt | 138 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.218× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.238× (z -17.2) |
| [[C-33 A (line)]] | alt | 225 | 1 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.277× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 218 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -18.3) |
| [[NCI-H2347 (line)]] | alt | 157 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +16.6) | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -16.2) |
| [[SK-MEL-2 (line)]] | alt | 164 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.310× (z -15.1) |
| [[BT-474 (line)]] | alt | 135 | 2 | 4 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.11× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -15.7) |
| [[C32 (line)]] | wt | 162 | 0 | 6 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.327× (z -13.7) |
| [[CFPAC-1 (line)]] | alt | 161 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.373× (z -11.9) |
| [[H4 (line)]] | wt | 231 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -14.5) |
| [[HepG2_C3A (line)]] | wt | 152 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -11.3) |
| [[HOP62 (line)]] | alt | 169 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -18.3) |
| [[Hs 766T (line)]] | wt | 185 | 1 | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.242× (z -16.6) |
| [[HT-29 (line)]] | alt | 154 | 2 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -14.3) |
| [[KATO III (line)]] | alt | 122 | 3 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.283× (z -14.3) |
| [[LS 180 (line)]] | wt | 188 | 2 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.230× (z -18.3) |
| [[NCI-H2030 (line)]] | alt | 200 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.385× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 144 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 146 | 2 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.435× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 207 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.257× (z -16.8) |
| [[RPMI-7951 (line)]] | alt | 167 | 1 | 4 | [[Harringtonine (drug)]] 5 µM 2.29× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -13.4) |
| [[SNU-1 (line)]] | wt | 285 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.290× (z -13.4) |
| [[SW 900 (line)]] | alt | 131 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -12.0) |
| [[SW1417 (line)]] | alt | 231 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -19.9) |
| [[A-427 (line)]] | wt | 183 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -16.5) |
| [[AsPC-1 (line)]] | alt | 123 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -13.1) |
| [[HCT15 (line)]] | alt | 190 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.277× (z -13.8) |
| [[J82 (line)]] | alt | 142 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -16.8) |
| [[Panc 03.27 (line)]] | alt | 174 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -17.4) |
| [[SHP-77 (line)]] | alt | 202 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.292× (z -14.3) |
| [[CHP-212 (line)]] | wt | 110 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -10.1) |
| [[COLO 205 (line)]] | alt | 121 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 172 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.356× (z -13.2) |
| [[AN3 CA (line)]] | alt | 208 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -10.0) |
| [[NCI-H661 (line)]] | alt | 191 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0312× (z -10.0) |
| [[NCI-H2122 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTPAP]] | +0.69 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[ZZZ3]] | +0.68 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[SCAF8]] | +0.67 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[MCCC2]] | +0.67 | +0.41 / +0.68 | both halves | 4e-05 |  |
| [[SENP6]] | +0.67 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[TLK1]] | +0.66 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[DIS3L]] | +0.66 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[RBM26]] | +0.66 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[PAIP1]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[UTP20]] | +0.64 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[CC2D2A]] | +0.63 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[GTF3C6]] | +0.63 | +0.41 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC22B]] | -0.67 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[TMEM184B]] | -0.65 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[TMED9]] | -0.64 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[ARID3B]] | -0.64 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[SRA1]] | -0.63 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[ATG101]] | -0.62 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[GP6-AS1]] | -0.62 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[RABGEF1]] | -0.62 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[TMEM104]] | -0.61 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[BET1L]] | -0.61 | -0.39 / -0.61 | both halves | 6e-05 |  |
| [[WIPI1]] | -0.61 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[P4HB]] | -0.60 | -0.32 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity lowers USP24's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.40× higher at baseline in the lines without TMEM92-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[TMCC3]] | B | TMCC3 activity lowers USP24's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 1.18× higher at baseline in the lines without TMCC3 | 0.065 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[TOP2A]] | B | TOP2A activity raises USP24's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.9, 4.1); signed map (11.4, -34.4). **Vector** length 86.2, 34.2% of its response variance represented; |z| ≥ 3 in 1,320 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +7.5 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +6.8 | -10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +6.1 | -13.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | -1.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.3 | -0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.3 | -8.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -7.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.5 | -9.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.2 | -0.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.8 | -17.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.0 | +0.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:55,066,359-55,215,378 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1057 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPU5](https://www.uniprot.org/uniprotkb/Q9UPU5) (Ubiquitin carboxyl-terminal hydrolase 24):

> Ubiquitin-specific protease that regulates cell survival in various contexts through modulating the protein stability of some of its substrates including DDB2, MCL1 or TP53. Plays a positive role on ferritinophagy where ferritin is degraded in lysosomes and releases free iron.

**Summary**, from NCBI Gene [23358](https://www.ncbi.nlm.nih.gov/gene/23358):

> Modification of cellular proteins by ubiquitin is an essential regulatory mechanism controlled by the coordinated action of multiple ubiquitin-conjugating and deubiquitinating enzymes. USP24 belongs to a large family of cysteine proteases that function as deubiquitinating enzymes (Quesada et al., 2004 [PubMed 14715245]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:12623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12623) · Entrez [23358](https://www.ncbi.nlm.nih.gov/gene/23358) · UniProt [Q9UPU5](https://www.uniprot.org/uniprotkb/Q9UPU5) · Ensembl [ENSG00000162402](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162402)

## Data

Gene col 8509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8509); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8509]; `tensor/DDL_lfc|DDL_z.npy` [8509]; `embed/gene_vectors.npy` [8509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8509 or target_col == 8509). Every well: [[USP24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
