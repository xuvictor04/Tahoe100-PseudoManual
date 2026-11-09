---
symbol: "PCNX1"
type: "gene"
col: 2016
ensembl_id: "ENSG00000100731"
name: "pecanex 1"
location: "14q24.2"
module: 18
arm: "+"
pooled_cpm: 216.5
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PCNX1

*pecanex 1* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.85× (z +12.7, q 3e-34, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.431× (z -16.3, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.690× (z -7.7, q 2e-12, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 0.188×, SW 1271 0.0453×, C-33 A 0.206×, NCI-H2030 0.297×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 0.109×, NCI-H23 0.166×, CHP-212 0.0867×, NCI-H1792 0.199×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C-33 A 0.201×, NCI-H2030 0.314×, SW48 0.217×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A549 0.492×, SW480 0.559×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STXBP5]] (+0.62, fdr 1e-05), [[MEMO1]] (+0.57, fdr 5e-05), [[ARHGEF11]] (+0.57, fdr 5e-05); moves opposite to [[ZNF17]] (-0.47, fdr 9e-05), [[ZNF417]] (-0.46, fdr 1e-04), [[TRIM52]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SOBP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2016.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +12.7 | 3e-34 | 46/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +9.8 | 2e-20 | 34/48 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +8.7 | 7e-16 | 41/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +8.3 | 2e-14 | 42/48 (NCI-H23, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.1 | 9e-14 | 41/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +4.5 | 8e-04 | 27/48 (NCI-H460, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.004 | 24/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.22×** | +4.0 | 0.004 | 24/49 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +4.0 | 0.004 | 25/47 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +3.8 | 0.007 | 22/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.7 | 0.010 | 13/48 (COLO 205, A-172, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +3.6 | 0.014 | 22/47 (LoVo, J82, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.022 | 24/48 (C32, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.1 | 0.068 | 18/45 (J82, C32, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2016.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 0.188×, SW 1271 0.0453×, C-33 A 0.206×, NCI-H2030 0.297×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 0.109×, NCI-H23 0.166×, CHP-212 0.0867×, NCI-H1792 0.199×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (C-33 A 0.201×, NCI-H2030 0.314×, SW48 0.217×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A549 0.492×, SW480 0.559×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.431×** | -16.3 | 0e+00 | 47/49 (NCI-H23, SW 1271, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.475×** | -14.2 | 1e-43 | 41/45 (C-33 A, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.500×** | -13.8 | 4e-41 | 44/44 (C-33 A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.615×** | -9.7 | 5e-20 | 43/47 (NCI-H2030, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.690×** | -7.7 | 2e-12 | 33/48 (A549, SW480, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.719×** | -6.8 | 8e-10 | 33/48 (A549, C-33 A, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.784×** | -5.0 | 4e-05 | 36/48 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.831×** | -3.8 | 0.009 | 23/48 (LS 180, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.879× | -3.7 | 0.013 | 6/48 (A-427, BT-474, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.841× | -3.4 | 0.045 | 18/48 (MIA PaCa-2, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.856× | -3.2 | 0.066 | 22/48 (SW 900, SNU-423, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.706×** | -3.2 | 0.072 | 24/45 (HCT15, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.847× | -3.1 | 0.088 | 11/48 (C-33 A, NCI-H2030, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.852× | -3.1 | 0.088 | 14/48 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.901× | -3.0 | 0.091 | 18/49 (A549, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 230 | 5 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +17.2) | [[Dinaciclib (drug)]] 0.05 µM 0.474× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.559× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 225 | 6 | 1 (1 ⚠) | [[Dexamethasone (drug)]] 5 µM 2.29× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.421× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 376 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -23.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 266 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -15.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.492× (z -10.5) |
| [[SW 900 (line)]] | alt | 256 | 3 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -12.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 164 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.436× (z -9.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 230 | 4 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -12.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 228 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -12.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 274 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -13.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 202 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -13.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 218 | 1 (1 ⚠) | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +10.0) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.418× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 359 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -16.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 127 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.455× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 353 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 351 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -18.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 226 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -10.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 154 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -10.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 241 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.390× (z -13.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 319 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -25.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 343 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0867× (z -20.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 210 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -10.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 200 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.268× (z -13.6) ⚠ toxic |
| [[J82 (line)]] | alt | 151 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 248 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -16.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 293 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -11.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 353 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -15.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 246 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -13.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 181 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.475× (z -8.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.7) | — |
| [[Hs 766T (line)]] | wt | 133 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 205 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -14.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 250 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -14.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 327 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -13.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 187 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.475× (z -9.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 271 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -15.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -12.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 231 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.466× (z -10.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 276 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -12.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -11.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 143 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 178 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -9.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -12.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -11.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 254 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0453× (z -18.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 194 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STXBP5]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[MEMO1]] | +0.57 | +0.65 / +0.39 | both halves | 5e-05 |  |
| [[ARHGEF11]] | +0.57 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[ATXN2]] | +0.54 | +0.58 / +0.40 | both halves | 4e-05 |  |
| [[RDX]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[FDX1]] | +0.53 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CHD7]] | +0.52 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[GYG1]] | +0.52 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[MED13L]] | +0.52 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[SPECC1L]] | +0.51 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[DTNB]] | +0.51 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ARMC8]] | +0.51 | +0.49 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF17]] | -0.47 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[ZNF417]] | -0.46 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[TRIM52]] | -0.45 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[ADAMTS16]] | -0.45 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[RNF121]] | -0.45 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[ZNF526]] | -0.44 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[WDR37]] | -0.44 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[DDX49]] | -0.44 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[RABGEF1P3]] | -0.43 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SLC25A14]] | -0.43 | -0.36 / -0.36 | both halves | 9e-05 |  |
| [[RNF139-DT]] | -0.43 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[FOXRED1]] | -0.43 | -0.39 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOBP]] | B | SOBP activity raises PCNX1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.48× lower at baseline in the lines without SOBP | 0.049 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[PTPRG]] | B | PTPRG activity raises PCNX1's level | lines that do not express PTPRG (8) vs lines expressing it (42) | 1.21× lower at baseline in the lines without PTPRG | 0.0995 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.324). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (0.4, -26.4); signed map (8.3, -3.3). **Vector** length 91.9, 31.7% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +5.8 | +4.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.0 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +3.4 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.3 | +0.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +2.8 | +1.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.7 | +0.9 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | -7.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.3 | -6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.8 | -9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.4 | -0.9 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.4 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | pecanex 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:70,907,405-71,115,382 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0995, KIAA0805, pecanex; previously PCNXL1, PCNX |
| Gene groups (HGNC) | Pecanex family |
| Matched by | ensembl_id |

UniProt [Q96RV3](https://www.uniprot.org/uniprotkb/Q96RV3) carries no function annotation.

**Summary**, from NCBI Gene [22990](https://www.ncbi.nlm.nih.gov/gene/22990):

> This gene encodes an evolutionarily conserved transmembrane protein similar to the pecanex protein in Drosophila. The fly protein is a component of the Notch signaling pathway, which functions in several developmental processes. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:19740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19740) · Entrez [22990](https://www.ncbi.nlm.nih.gov/gene/22990) · UniProt [Q96RV3](https://www.uniprot.org/uniprotkb/Q96RV3) · Ensembl [ENSG00000100731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100731)

## Data

Gene col 2016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2016); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2016]; `tensor/DDL_lfc|DDL_z.npy` [2016]; `embed/gene_vectors.npy` [2016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2016 or target_col == 2016). Every well: [[PCNX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCNX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
