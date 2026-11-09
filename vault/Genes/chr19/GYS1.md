---
symbol: "GYS1"
type: "gene"
col: 2500
ensembl_id: "ENSG00000104812"
name: "glycogen synthase 1"
location: "19q13.33"
module: 103
arm: "+"
pooled_cpm: 97.79
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# GYS1

*glycogen synthase 1* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.33× (z +4.8, q 0.001, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.303× (z -20.0, q 0e+00, down in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.323× (z -19.7, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPFIA4]] (+0.72, fdr 7e-06), [[PFKFB4]] (+0.71, fdr 7e-06), [[BNIP3]] (+0.68, fdr 7e-06); moves opposite to [[SLC12A2-DT]] (-0.57, fdr 4e-05), [[ADGRA3]] (-0.57, fdr 1e-05), [[ARAP2]] (-0.54, fdr 4e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPR155]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +4.8 | 0.001 | 29/47 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.64×** | +4.6 | 0.001 | 34/48 (SNU-423, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Roxadustat (drug)]] 5 µM |  | **1.29×** | +4.3 | 0.004 | 28/48 (HOP62, BT-474, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.011 | 23/48 (Panc 03.27, SW 900, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.16× | +3.8 | 0.015 | 15/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.015 | 20/47 (SK-MEL-2, RKO, …) | two highest doses | low cells (technical?) |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.025 | 24/48 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.16× | +3.3 | 0.069 | 14/50 (HOP62, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.12 | 19/48 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2500.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.303×** | -20.0 | 0e+00 | 38/44 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.323×** | -19.7 | 0e+00 | 46/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.353×** | -18.2 | 0e+00 | 44/49 (C-33 A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.493×** | -17.4 | 0e+00 | 37/48 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.387×** | -15.9 | 0e+00 | 44/47 (SNU-423, HCT15, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.377×** | -15.7 | 0e+00 | 40/45 (A549, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.494×** | -11.8 | 3e-30 | 39/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -10.9 | 9e-26 | 41/48 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.539×** | -10.8 | 3e-25 | 36/48 (C32, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.556×** | -10.2 | 1e-22 | 44/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -8.5 | 1e-15 | 31/49 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.604×** | -8.4 | 2e-15 | 37/47 (SNU-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.672×** | -6.9 | 2e-10 | 36/48 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.674×** | -6.9 | 3e-10 | 38/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.686×** | -6.5 | 2e-09 | 29/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.793×** | -5.7 | 5e-07 | 25/48 (SNU-423, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.734×** | -5.4 | 3e-06 | 35/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -5.2 | 6e-06 | 27/48 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.742×** | -5.0 | 2e-05 | 25/50 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.844× | -4.1 | 9e-04 | 24/48 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.804×** | -3.8 | 0.004 | 23/48 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 146 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -27.9) |
| [[NCI-H460 (line)]] | wt | 85.9 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -21.2) |
| [[SNU-423 (line)]] | alt | 149 | 0 | 12 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0734× (z -25.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.294× (z -17.3) |
| [[RPMI-7951 (line)]] | alt | 256 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.334× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 104 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -15.6) |
| [[SW 900 (line)]] | alt | 108 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 212 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -21.6) |
| [[NCI-H1573 (line)]] | alt | 62.9 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -20.3) |
| [[C-33 A (line)]] | alt | 301 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0139× (z -36.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.372× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 247 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -25.8) |
| [[CFPAC-1 (line)]] | alt | 178 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.298× (z -17.2) |
| [[H4 (line)]] | wt | 228 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -20.2) |
| [[HCT15 (line)]] | alt | 175 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -21.4) |
| [[HOP62 (line)]] | alt | 123 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -16.4) |
| [[NCI-H2030 (line)]] | alt | 69.5 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.289× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 100 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -20.9) |
| [[A-427 (line)]] | wt | 69.4 | 1 | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.77× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.7) |
| [[Hs 766T (line)]] | wt | 70.3 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -10.8) |
| [[HS-578T (line)]] | alt | 174 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -11.6) |
| [[J82 (line)]] | alt | 144 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.490× (z -12.0) |
| [[PANC-1 (line)]] | alt | 41.0 | 2 (2 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.13× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.417× (z -10.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.440× (z -9.8) |
| [[SNU-1 (line)]] | wt | 150 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -13.8) |
| [[AN3 CA (line)]] | alt | 160 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0776× (z -18.1) |
| [[hTERT-HPNE (line)]] | wt | 161 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 101 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -28.4) |
| [[A549 (line)]] | wt | 90.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.361× (z -15.9) |
| [[KATO III (line)]] | alt | 52.0 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -11.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 54.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.193× (z -8.9) |
| [[SW480 (line)]] | alt | 46.3 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.96× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.481× (z -8.6) |
| [[A-172 (line)]] | wt | 71.1 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.225× (z -14.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -13.6) |
| [[BT-474 (line)]] | alt | 78.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -11.6) |
| [[COLO 205 (line)]] | alt | 48.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 152 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -17.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 75.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 79.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -12.2) |
| [[SW 1088 (line)]] | alt | 171 | 0 | 2 | — | [[Cabozantinib (S-malate) (drug)]] 0.05 µM 0.126× (z -8.8) |
| [[SW1417 (line)]] | alt | 74.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.402× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -10.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0982× (z -12.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 44.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -9.4) ⚠ toxic |
| [[LoVo (line)]] | wt | 54.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.408× (z -9.9) |
| [[LS 180 (line)]] | wt | 76.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -11.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 65.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 96.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -9.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2500), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPFIA4]] | +0.72 | +0.78 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[PFKFB4]] | +0.71 | +0.70 / +0.61 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[BNIP3]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ZNF395]] | +0.66 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[YEATS2]] | +0.66 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[PLEKHA2]] | +0.65 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[DPCD]] | +0.64 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[TBC1D9B]] | +0.63 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[CABIN1]] | +0.63 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[GPR155]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ENO2]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC12A2-DT]] | -0.57 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ADGRA3]] | -0.57 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ARAP2]] | -0.54 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[PCBD2]] | -0.54 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[SH3D19]] | -0.53 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[CYP4V2]] | -0.53 | -0.54 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR155]] | B | GPR155 activity raises GYS1's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 2.09× lower at baseline in the lines without GPR155 | 0.064 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises GYS1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.9, -16.8); signed map (-37.4, 25.3). **Vector** length 138, 50.0% of its response variance represented; |z| ≥ 3 in 1,415 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.0 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.2 | +2.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +7.2 | +2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.1 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.9 | +4.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.7 | +1.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +0.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.5 | -15.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.3 | -19.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.7 | -15.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -20.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.6 | -10.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.6 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | glycogen synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,968,130-48,993,310 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GSY; previously GYS |
| Gene groups (HGNC) | Glycosyl transferases group 1 domain containing |
| Hallmark sets | GLYCOLYSIS, HYPOXIA |
| Reactome | 7 pathways, smallest: Myoclonic epilepsy of Lafora; Glycogen synthesis; Glycogen storage diseases |
| Matched by | ensembl_id |

**Function**, from UniProt [P13807](https://www.uniprot.org/uniprotkb/P13807) (Glycogen):

> Glycogen synthase participates in the glycogen biosynthetic process along with glycogenin and glycogen branching enzyme. Extends the primer composed of a few glucose units formed by glycogenin by adding new glucose units to it. In this context, glycogen synthase transfers the glycosyl residue from UDP-Glc to the non-reducing end of alpha-1,4-glucan.

**Summary**, from NCBI Gene [2997](https://www.ncbi.nlm.nih.gov/gene/2997):

> The protein encoded by this gene catalyzes the addition of glucose monomers to the growing glycogen molecule through the formation of alpha-1,4-glycoside linkages. Mutations in this gene are associated with muscle glycogen storage disease. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:4706](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4706) · Entrez [2997](https://www.ncbi.nlm.nih.gov/gene/2997) · UniProt [P13807](https://www.uniprot.org/uniprotkb/P13807) · Ensembl [ENSG00000104812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104812)

## Data

Gene col 2500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2500); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2500, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2500]; `tensor/DDL_lfc|DDL_z.npy` [2500]; `embed/gene_vectors.npy` [2500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2500 or target_col == 2500). Every well: [[GYS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GYS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
