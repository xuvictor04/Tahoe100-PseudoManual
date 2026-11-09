---
symbol: "SENP6"
type: "gene"
col: 3398
ensembl_id: "ENSG00000112701"
name: "SUMO specific peptidase 6"
location: "6q14.1"
module: 51
arm: "+"
pooled_cpm: 259.01
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# SENP6

*SUMO specific peptidase 6* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.71× (z +22.3, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.175× (z -50.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAF8]] (+0.76, fdr 7e-06), [[CPLANE1]] (+0.70, fdr 7e-06), [[ZNF644]] (+0.70, fdr 7e-06); moves opposite to [[QSOX1]] (-0.60, fdr 2e-05), [[DNAJC5]] (-0.59, fdr 2e-05), [[LPCAT1]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DHFR2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +22.3 | 0e+00 | 42/48 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +17.2 | 0e+00 | 44/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +15.5 | 0e+00 | 44/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.27×** | +11.8 | 6e-30 | 46/49 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +10.8 | 5e-25 | 39/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +10.4 | 2e-23 | 32/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +10.0 | 2e-21 | 43/48 (RKO, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +9.2 | 2e-18 | 35/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +8.5 | 9e-16 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +5.1 | 2e-05 | 24/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.19× | +4.9 | 5e-05 | 22/47 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.6 | 2e-04 | 21/48 (NCI-H460, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.11× | +4.4 | 4e-04 | 12/48 (A-427, A498, …) | rises with dose | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.7 | 0.009 | 19/38 (NCI-H1573, H4, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.4 | 0.027 | 9/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3398.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.175×** | -50.8 | 0e+00 | 48/48 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.179×** | -50.1 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.209×** | -45.7 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.420×** | -25.3 | 0e+00 | 48/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.532×** | -18.4 | 0e+00 | 48/48 (SW48, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.674×** | -16.3 | 0e+00 | 44/48 (SW480, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -15.0 | 0e+00 | 37/49 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.659×** | -12.2 | 3e-32 | 40/48 (SNU-423, LoVo, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.479×** | -10.6 | 3e-24 | 47/49 (A498, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.711×** | -10.0 | 1e-21 | 33/49 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.712×** | -9.6 | 6e-20 | 30/44 (SNU-1, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.743×** | -8.3 | 4e-15 | 35/50 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.764×** | -7.9 | 2e-13 | 34/49 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.783×** | -6.9 | 2e-10 | 29/48 (NCI-H23, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~14% of this change | **0.803×** | -6.4 | 5e-09 | 29/48 (PANC-1, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.850× | -4.4 | 4e-04 | 18/47 (HepG2/C3A, RKO, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.879× | -3.8 | 0.005 | 7/48 (SW1417, A549, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.903× | -3.0 | 0.076 | 6/48 (SW 1271, AsPC-1, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 5 µM |  | **0.817×** | -2.9 | 0.086 | 18/46 (SW480, HT-29, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 272 | 9 (1 ⚠) | 10 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +17.4) | [[Panobinostat (drug)]] 5 µM 0.144× (z -42.3) |
| [[NCI-H460 (line)]] | wt | 242 | 10 (3 ⚠) | 7 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.153× (z -34.6) |
| [[Panc 03.27 (line)]] | alt | 562 | 5 | 11 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.90× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.101× (z -43.2) |
| [[LOX-IMVI (line)]] | wt | 312 | 6 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -33.8) |
| [[NCI-H23 (line)]] | alt | 520 | 4 | 10 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +21.4) | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -32.2) |
| [[HOP62 (line)]] | alt | 208 | 3 (1 ⚠) | 10 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.157× (z -32.5) |
| [[KATO III (line)]] | alt | 253 | 6 (1 ⚠) | 7 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.140× (z -35.2) |
| [[NCI-H1573 (line)]] | alt | 182 | 9 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +18.4) | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -19.8) |
| [[SW48 (line)]] | wt | 329 | 4 | 9 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.12× (z +14.5) | [[Belinostat (drug)]] 5 µM 0.141× (z -26.6) |
| [[HS-578T (line)]] | alt | 255 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -36.5) |
| [[LoVo (line)]] | wt | 288 | 6 | 6 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +18.1) | [[Panobinostat (drug)]] 5 µM 0.130× (z -42.4) |
| [[LS 180 (line)]] | wt | 287 | 6 (1 ⚠) | 6 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.111× (z -29.3) |
| [[MIA PaCa-2 (line)]] | alt | 348 | 4 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +17.0) | [[Panobinostat (drug)]] 5 µM 0.106× (z -41.3) |
| [[PANC-1 (line)]] | alt | 223 | 4 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +20.4) | [[Panobinostat (drug)]] 5 µM 0.217× (z -30.2) |
| [[RKO (line)]] | wt | 295 | 5 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.175× (z -31.8) |
| [[SK-MEL-2 (line)]] | alt | 272 | 4 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +14.3) | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -24.2) |
| [[SNU-423 (line)]] | alt | 321 | 1 | 11 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.62× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.110× (z -41.3) |
| [[SW 900 (line)]] | alt | 172 | 6 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -24.5) |
| [[NCI-H2030 (line)]] | alt | 340 | 3 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +17.3) | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -25.0) |
| [[NCI-H2347 (line)]] | alt | 339 | 1 | 10 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.62× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -36.8) |
| [[A498 (line)]] | wt | 156 | 2 | 8 | [[TAK-901 (drug)]] 5 µM 3.02× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -38.4) |
| [[C32 (line)]] | wt | 256 | 3 | 7 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.209× (z -22.2) |
| [[NCI-H1792 (line)]] | alt | 251 | 4 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 0.5 µM 1.81× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.110× (z -36.1) |
| [[SHP-77 (line)]] | alt | 243 | 3 (1 ⚠) | 7 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.185× (z -28.1) |
| [[A-172 (line)]] | wt | 243 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.158× (z -34.2) |
| [[BT-474 (line)]] | alt | 305 | 1 | 7 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -27.4) |
| [[H4 (line)]] | wt | 322 | 2 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.143× (z -27.6) |
| [[HEC-1-A (line)]] | alt | 336 | 3 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -27.0) |
| [[HT-29 (line)]] | alt | 179 | 2 | 6 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +20.7) | [[Panobinostat (drug)]] 5 µM 0.170× (z -29.5) |
| [[SW1417 (line)]] | alt | 186 | 2 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -26.3) |
| [[A-427 (line)]] | wt | 164 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +16.4) | [[Panobinostat (drug)]] 5 µM 0.226× (z -23.6) |
| [[A549 (line)]] | wt | 216 | 1 | 6 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.153× (z -29.3) |
| [[AsPC-1 (line)]] | alt | 176 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +20.1) | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -28.0) |
| [[C-33 A (line)]] | alt | 288 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.191× (z -27.8) |
| [[CHP-212 (line)]] | wt | 371 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -21.7) |
| [[COLO 205 (line)]] | alt | 106 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +15.5) | [[Panobinostat (drug)]] 5 µM 0.191× (z -18.4) |
| [[HCT15 (line)]] | alt | 289 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.260× (z -19.0) |
| [[HepG2_C3A (line)]] | wt | 224 | 2 | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -20.7) |
| [[hTERT-HPNE (line)]] | wt | 264 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -27.9) |
| [[SNU-1 (line)]] | wt | 404 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.202× (z -23.2) |
| [[AN3 CA (line)]] | alt | 425 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -16.6) |
| [[CFPAC-1 (line)]] | alt | 138 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.182× (z -24.4) |
| [[Hs 766T (line)]] | wt | 165 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.142× (z -27.2) |
| [[J82 (line)]] | alt | 183 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.241× (z -24.6) |
| [[RPMI-7951 (line)]] | alt | 240 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -20.5) |
| [[SW 1088 (line)]] | alt | 249 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -11.5) |
| [[SW 1271 (line)]] | alt | 263 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.169× (z -13.1) |
| [[NCI-H661 (line)]] | alt | 268 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -11.3) |
| [[NCI-H2122 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 261 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAF8]] | +0.76 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[CPLANE1]] | +0.70 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ZNF644]] | +0.70 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[WARS2]] | +0.69 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[GTF3C6]] | +0.68 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[UBE3A]] | +0.67 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[ZFX]] | +0.67 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[USP24]] | +0.67 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[NFYC]] | +0.67 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.67 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[GABPB2]] | +0.66 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[LATS1]] | +0.66 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QSOX1]] | -0.60 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[DNAJC5]] | -0.59 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[LPCAT1]] | -0.58 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[EXTL3]] | -0.58 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[GMCL1]] | -0.58 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[SIPA1]] | -0.58 | -0.38 / -0.53 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SENP6's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DHFR2]] | C | SENP6's natural level weakens DHFR2's drug response | SENP6's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.14; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.797). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.4, 12.5); signed map (12.0, -33.3). **Vector** length 114, 43.6% of its response variance represented; |z| ≥ 3 in 1,519 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.9 | +22.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.7 | +17.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +10.6 | -9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | +10.1 | -10.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +9.9 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.9 | +0.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.8 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | -0.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.7 | -0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.3 | -12.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.2 | -25.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.0 | -18.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -16.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.4 | -7.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.1 | -10.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.5 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SUMO specific peptidase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:75,601,509-75,718,281 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SUSP1, KIAA0797 |
| Gene groups (HGNC) | SUMO specific peptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZR1](https://www.uniprot.org/uniprotkb/Q9GZR1) (Sentrin-specific protease 6):

> Protease that deconjugates SUMO1, SUMO2 and SUMO3 from targeted proteins. Processes preferentially poly-SUMO2 and poly-SUMO3 chains, but does not efficiently process SUMO1, SUMO2 and SUMO3 precursors. Deconjugates SUMO1 from RXRA, leading to transcriptional activation. Involved in chromosome alignment and spindle assembly, by regulating the kinetochore CENPH-CENPI-CENPK complex. Desumoylates PML and CENPI, protecting them from degradation by the ubiquitin ligase RNF4, which targets …

**Summary**, from NCBI Gene [26054](https://www.ncbi.nlm.nih.gov/gene/26054):

> Ubiquitin-like molecules (UBLs), such as SUMO1 (UBL1; MIM 601912), are structurally related to ubiquitin (MIM 191339) and can be ligated to target proteins in a similar manner as ubiquitin. However, covalent attachment of UBLs does not result in degradation of the modified proteins. SUMO1 modification is implicated in the targeting of RANGAP1 (MIM 602362) to the nuclear pore complex, as well as in stabilization of I-kappa-B-alpha (NFKBIA; MIM 164008) from degradation by the 26S proteasome. Like …

**Accessions** — [HGNC:20944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20944) · Entrez [26054](https://www.ncbi.nlm.nih.gov/gene/26054) · UniProt [Q9GZR1](https://www.uniprot.org/uniprotkb/Q9GZR1) · Ensembl [ENSG00000112701](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112701)

## Data

Gene col 3398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3398); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3398]; `tensor/DDL_lfc|DDL_z.npy` [3398]; `embed/gene_vectors.npy` [3398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3398 or target_col == 3398). Every well: [[SENP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SENP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
