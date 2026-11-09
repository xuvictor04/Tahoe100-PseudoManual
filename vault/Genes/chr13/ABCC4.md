---
symbol: "ABCC4"
type: "gene"
col: 4598
ensembl_id: "ENSG00000125257"
name: "ATP binding cassette subfamily C member 4 (PEL blood group)"
location: "13q32.1"
module: 18
arm: "+"
pooled_cpm: 87.24
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 20
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ABCC4

*ATP binding cassette subfamily C member 4 (PEL blood group)* — 13q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.86× (z +11.5, q 5e-28, up in 41 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.25× (z +5.9, q 4e-07, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -16.6, q 0e+00, down in 36 of 46 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.432× (z -15.1, q 0e+00, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UCK2]] (+0.70, fdr 7e-06), [[NLN]] (+0.67, fdr 7e-06), [[LETM1]] (+0.67, fdr 7e-06); moves opposite to [[NOSIP]] (-0.57, fdr 1e-05), [[ZFYVE1]] (-0.54, fdr 2e-05), [[ADAM8]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADAM8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.86×** | +11.5 | 5e-28 | 41/46 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +7.5 | 2e-11 | 25/42 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.9 | 8e-10 | 26/45 (NCI-H1573, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.8 | 1e-09 | 25/47 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +5.9 | 4e-07 | 23/46 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +5.1 | 3e-05 | 25/46 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **1.67×** | +5.0 | 6e-05 | 23/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.63×** | +4.7 | 2e-04 | 23/46 (NCI-H460, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +3.9 | 0.006 | 20/44 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.22×** | +3.8 | 0.009 | 18/46 (LS 180, LoVo, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.009 | 17/46 (NCI-H460, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.22×** | +3.7 | 0.010 | 19/46 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.012 | 17/46 (HEC-1-A, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.015 | 17/46 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.018 | 15/47 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.032 | 14/46 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +3.2 | 0.042 | 16/46 (HOP62, A498, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.042 | 9/46 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.042 | 16/46 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.1 | 0.056 | 19/45 (MIA PaCa-2, A549, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.18× | +3.1 | 0.056 | 16/46 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.070 | 13/46 (A549, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4598.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.534×** | -16.6 | 0e+00 | 36/46 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.432×** | -15.1 | 0e+00 | 38/46 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.589×** | -9.9 | 1e-20 | 30/46 (RKO, A498, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.608×** | -9.3 | 2e-18 | 29/46 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.614×** | -9.1 | 8e-18 | 30/46 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.617×** | -9.0 | 2e-17 | 30/46 (RKO, A-172, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.630×** | -8.3 | 8e-15 | 33/45 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.435×** | -8.1 | 3e-14 | 37/47 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.744×** | -5.5 | 2e-06 | 24/46 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.814×** | -5.4 | 3e-06 | 26/46 (LS 180, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.754×** | -5.3 | 7e-06 | 25/46 (RKO, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.782×** | -4.6 | 2e-04 | 24/46 (NCI-H460, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.784×** | -4.5 | 2e-04 | 21/46 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -4.2 | 9e-04 | 19/46 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.810×** | -3.9 | 0.003 | 17/46 (A549, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.819×** | -3.7 | 0.006 | 18/46 (LOX-IMVI, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.831×** | -3.5 | 0.016 | 20/46 (A-172, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.821×** | -3.4 | 0.018 | 13/45 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.842× | -3.2 | 0.034 | 12/46 (HT-29, CHP-212, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.893× | -3.0 | 0.063 | 7/47 (Panc 03.27, RKO, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.803×** | -2.9 | 0.081 | 13/46 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 27.6 | 17 (3 ⚠) | 0 | [[Budesonide (drug)]] 5 µM 4.73× (z +12.2) | — |
| [[RKO (line)]] | wt | 163 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -28.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0896× (z -24.5) |
| [[A-172 (line)]] | wt | 257 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -19.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.140× (z -17.1) |
| [[A498 (line)]] | wt | 236 | 2 | 11 (5 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 2.16× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -17.4) |
| [[PANC-1 (line)]] | alt | 159 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -34.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.199× (z -23.0) |
| [[SNU-1 (line)]] | wt | 128 | 1 (1 ⚠) | 8 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.00× (z +9.3) ⚠ unreliable plate only | [[Harringtonine (drug)]] 5 µM 0.111× (z -18.1) |
| [[MIA PaCa-2 (line)]] | alt | 65.3 | 3 (1 ⚠) | 5 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.81× (z +9.8) ⚠ unreliable plate only · without an alert: [[Cobimetinib (drug)]] 5 µM 2.78× (z +9.3) | [[Harringtonine (drug)]] 5 µM 0.242× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 60.0 | 1 (1 ⚠) | 7 (6 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.57× (z +13.9) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -19.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.200× (z -16.9) |
| [[SW48 (line)]] | wt | 109 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -15.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.166× (z -14.7) |
| [[A549 (line)]] | wt | 96.9 | 2 | 5 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.49× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.289× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 160 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -14.8) |
| [[LS 180 (line)]] | wt | 49.7 | 1 | 6 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.68× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -17.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.275× (z -10.9) |
| [[LoVo (line)]] | wt | 62.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -18.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.169× (z -18.0) |
| [[LOX-IMVI (line)]] | wt | 154 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.402× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 161 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -15.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.350× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 96.3 | 1 (1 ⚠) | 3 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.56× (z +9.9) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -16.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.200× (z -16.2) |
| [[SW480 (line)]] | alt | 116 | 1 (1 ⚠) | 3 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.65× (z +10.9) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -11.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.432× (z -9.0) |
| [[C-33 A (line)]] | alt | 69.6 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.274× (z -9.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.321× (z -8.5) |
| [[HT-29 (line)]] | alt | 72.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -14.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 137 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 40.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.00× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.36× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 33.5 | 3 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 3.88× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 30.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -14.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.326× (z -8.8) |
| [[BT-474 (line)]] | alt | 29.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0876× (z -10.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 105 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.08× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -11.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 43.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -14.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Hs 766T (line)]] | wt | 35.4 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.27× (z +9.9) ⚠ unreliable plate only | [[Harringtonine (drug)]] 5 µM 0.249× (z -9.1) |
| [[HS-578T (line)]] | alt | 31.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 90.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.444× (z -8.8) |
| [[AN3 CA (line)]] | alt | 77.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -10.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 99.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -14.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 32.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +9.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 43.7 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.04× (z +9.9) ⚠ unreliable plate only | — |
| [[Panc 03.27 (line)]] | alt | 42.1 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.13× (z +8.8) ⚠ unreliable plate only | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.172× (z -8.6) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.03× (z +8.7) ⚠ toxic | — |
| [[SW 900 (line)]] | alt | 64.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.326× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 7.89 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UCK2]] | +0.70 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[NLN]] | +0.67 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[LETM1]] | +0.67 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[DKC1]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[MAN2A1]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[LARP1]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ADCY3]] | +0.64 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[AGPAT3]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[GART]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.64 | +0.68 / +0.57 | both halves | 8e-06 |  |
| [[MDN1]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[NUDT3]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOSIP]] | -0.57 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[ZFYVE1]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[ADAM8]] | -0.54 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[SLU7]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[BTG1]] | -0.53 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[CCS]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[MXD1]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM8]] | B | ADAM8 activity lowers ABCC4's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.53× higher at baseline in the lines without ADAM8 | 0.078 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[SLC16A6]] | B | SLC16A6 activity lowers ABCC4's level | lines that do not express SLC16A6 (27) vs lines expressing it (23) | 1.51× higher at baseline in the lines without SLC16A6 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENPP2, TMEM47, IGFBP7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.740). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.0, -35.6); signed map (-4.1, -53.2). **Vector** length 136, 42.3% of its response variance represented; |z| ≥ 3 in 1,549 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +11.0 | +11.5 |
|  | [[EX229 (drug)]] 5 µM |  | +6.4 | +5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.4 | +6.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.5 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +5.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.8 | +3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.8 | +3.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -15.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.6 | -8.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.1 | -5.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.6 | -8.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | -4.2 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.4 | -2.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily C member 4 (PEL blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.1 — chr13:95,019,835-95,301,475 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRP4, EST170205, MOAT-B, MOATB |
| Gene groups (HGNC) | Blood group antigens; ATP binding cassette subfamily C |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 9 pathways, smallest: Paracetamol ADME; Azathioprine ADME; Drug ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [O15439](https://www.uniprot.org/uniprotkb/O15439) (ATP-binding cassette sub-family C member 4):

> ATP-dependent transporter of the ATP-binding cassette (ABC) family that actively extrudes physiological compounds and xenobiotics from cells. Transports a range of endogenous molecules that have a key role in cellular communication and signaling, including cyclic nucleotides such as cyclic AMP (cAMP) and cyclic GMP (cGMP), bile acids, steroid conjugates, urate, and prostaglandins. Mediates the ATP-dependent efflux of glutathione conjugates such as leukotriene C4 (LTC4) and leukotriene B4 (LTB4) …

**Summary**, from NCBI Gene [10257](https://www.ncbi.nlm.nih.gov/gene/10257):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MRP subfamily which is involved in multi-drug resistance. This family member plays a role in cellular detoxification as a pump for its substrate, organic anions. It may also …

**Accessions** — [HGNC:55](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55) · Entrez [10257](https://www.ncbi.nlm.nih.gov/gene/10257) · UniProt [O15439](https://www.uniprot.org/uniprotkb/O15439) · Ensembl [ENSG00000125257](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125257)

## Data

Gene col 4598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4598); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4598]; `tensor/DDL_lfc|DDL_z.npy` [4598]; `embed/gene_vectors.npy` [4598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4598 or target_col == 4598). Every well: [[ABCC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
