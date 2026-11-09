---
symbol: "RPRD2"
type: "gene"
col: 8637
ensembl_id: "ENSG00000163125"
name: "regulation of nuclear pre-mRNA domain containing 2"
location: "1q21.2"
module: 184
arm: "-"
pooled_cpm: 137.4
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# RPRD2

*regulation of nuclear pre-mRNA domain containing 2* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.72× (z +15.5, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.336× (z -26.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAF1]] (+0.68, fdr 1e-05), [[MAIP1]] (+0.67, fdr 1e-05), [[KDM3B]] (+0.66, fdr 1e-05); moves opposite to [[EHD4]] (-0.68, fdr 1e-05), [[SEPTIN10]] (-0.66, fdr 1e-05), [[MICAL2]] (-0.63, fdr 3e-05).
> It sits in the **-** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KCTD3]] → it (grade C ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8637.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.72×** | +15.5 | 0e+00 | 47/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +14.6 | 0e+00 | 37/48 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.48×** | +10.7 | 2e-24 | 46/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +9.6 | 1e-19 | 40/48 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +8.5 | 3e-15 | 33/48 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +6.9 | 4e-10 | 32/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +6.0 | 1e-07 | 27/48 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +5.6 | 1e-06 | 26/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +5.4 | 5e-06 | 25/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +4.6 | 3e-04 | 24/47 (SW48, A-172, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.20×** | +4.2 | 0.001 | 24/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +4.0 | 0.002 | 16/49 (A498, SHP-77, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.18× | +3.9 | 0.004 | 18/48 (HOP62, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.9 | 0.004 | 19/48 (C32, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.12× | +3.8 | 0.006 | 14/48 (J82, HT-29, …) | rises with dose | low cells (technical?) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.006 | 23/49 (SW48, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.086 | 15/48 (LS 180, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8637.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.336×** | -26.7 | 0e+00 | 48/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.382×** | -23.6 | 0e+00 | 48/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.471×** | -18.5 | 0e+00 | 47/48 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.480×** | -18.0 | 0e+00 | 38/49 (RKO, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.498×** | -16.4 | 0e+00 | 33/44 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.603×** | -11.5 | 2e-28 | 36/45 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.734×** | -10.7 | 7e-25 | 37/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.677×** | -9.6 | 9e-20 | 41/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.743×** | -7.3 | 2e-11 | 30/49 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **0.774×** | -6.3 | 2e-08 | 35/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.772×** | -6.1 | 5e-08 | 29/50 (A-427, NCI-H2347, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.824×** | -4.8 | 9e-05 | 25/47 (SW 900, CFPAC-1, …) | two highest doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.852× | -3.9 | 0.004 | 17/48 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.848× | -3.9 | 0.004 | 19/48 (hTERT-HPNE, NCI-H2347, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.856× | -3.8 | 0.005 | 16/48 (NCI-H460, NCI-H1792, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.773×** | -3.8 | 0.005 | 21/48 (KATO III, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.853× | -3.8 | 0.005 | 16/47 (NCI-H460, SW 900, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.861× | -3.7 | 0.007 | 16/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.868× | -3.5 | 0.014 | 9/48 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.745×** | -3.5 | 0.014 | 17/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.872× | -3.4 | 0.020 | 20/48 (A-427, HEC-1-A, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.873× | -3.4 | 0.020 | 7/49 (NCI-H2122, SW 900, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.910× | -3.3 | 0.024 | 1/48 (NCI-H1792) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.873× | -3.2 | 0.030 | 18/48 (NCI-H2347, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 169 | 1 | 12 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.237× (z -20.9) |
| [[SW480 (line)]] | alt | 156 | 6 (1 ⚠) | 7 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.02× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.270× (z -22.5) |
| [[LS 180 (line)]] | wt | 165 | 4 (1 ⚠) | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +17.2) | [[Panobinostat (drug)]] 0.5 µM 0.291× (z -17.1) |
| [[LoVo (line)]] | wt | 114 | 6 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +17.3) | [[Panobinostat (drug)]] 0.5 µM 0.441× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 144 | 2 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.299× (z -16.7) |
| [[NCI-H460 (line)]] | wt | 166 | 3 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -28.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.361× (z -17.0) |
| [[A-427 (line)]] | wt | 183 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.339× (z -14.7) |
| [[BT-474 (line)]] | alt | 250 | 5 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.362× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 166 | 3 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.293× (z -18.7) |
| [[KATO III (line)]] | alt | 106 | 3 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -15.0) |
| [[SHP-77 (line)]] | alt | 306 | 2 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.52× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.264× (z -19.6) |
| [[SW1417 (line)]] | alt | 146 | 3 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -16.2) |
| [[CHP-212 (line)]] | wt | 224 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Capmatinib (drug)]] 5 µM 0.0726× (z -9.9) |
| [[PANC-1 (line)]] | alt | 127 | 1 | 6 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.12× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.385× (z -15.4) |
| [[RKO (line)]] | wt | 170 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.37× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.321× (z -14.6) |
| [[C-33 A (line)]] | alt | 189 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.99× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.348× (z -13.0) |
| [[HT-29 (line)]] | alt | 114 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.303× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 116 | 2 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.82× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 106 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.391× (z -11.7) |
| [[COLO 205 (line)]] | alt | 198 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.76× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -13.5) |
| [[HCT15 (line)]] | alt | 194 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.390× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 132 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.275× (z -13.3) |
| [[HOP62 (line)]] | alt | 103 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.326× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 161 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.368× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 152 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.431× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 105 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.51× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -15.4) |
| [[SNU-423 (line)]] | alt | 91.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.331× (z -12.7) |
| [[SW48 (line)]] | wt | 160 | 2 | 3 | [[TAK-901 (drug)]] 0.05 µM 3.89× (z +13.8) | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 120 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.337× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 120 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.444× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 96.2 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 4.89× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -14.0) |
| [[SNU-1 (line)]] | wt | 184 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.20× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.0772× (z -29.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.384× (z -11.3) |
| [[SW 900 (line)]] | alt | 228 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.263× (z -16.8) |
| [[A549 (line)]] | wt | 95.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +20.2) | [[Panobinostat (drug)]] 5 µM 0.482× (z -9.0) |
| [[Hs 766T (line)]] | wt | 110 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -14.6) |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -11.2) |
| [[J82 (line)]] | alt | 82.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.0) | [[Panobinostat (drug)]] 0.5 µM 0.500× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 125 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.481× (z -10.0) |
| [[A-172 (line)]] | wt | 116 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.8) | — |
| [[A498 (line)]] | wt | 96.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.453× (z -11.7) |
| [[HS-578T (line)]] | alt | 66.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 88.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.2) | — |
| [[C32 (line)]] | wt | 121 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 9.23× (z +11.4) | — |
| [[H4 (line)]] | wt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.7) | — |
| [[NCI-H661 (line)]] | alt | 128 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -8.5) |
| [[SW 1088 (line)]] | alt | 94.6 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.117× (z -8.9) ⚠ transcription drop |
| [[AN3 CA (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAF1]] | +0.68 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MAIP1]] | +0.67 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[KDM3B]] | +0.66 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CREB3L4]] | +0.65 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[NDUFS3]] | +0.64 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ATP6V0D1-DT]] | +0.62 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[CLPX]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[SMAD1]] | +0.61 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[HOXA3]] | +0.61 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ZNF428]] | +0.61 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[HFE]] | +0.60 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[PRRT1]] | +0.59 | +0.56 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD4]] | -0.68 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[SEPTIN10]] | -0.66 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[MICAL2]] | -0.63 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[C3orf52]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[CAP1]] | -0.62 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[R3HDM4]] | -0.61 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[CORO1C]] | -0.60 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[UCHL3]] | -0.59 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[FLNB]] | -0.59 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[ELOVL1]] | -0.58 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[RELL1]] | -0.58 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[LRRFIP1]] | -0.57 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCTD3]] | C | KCTD3's natural level strengthens RPRD2's drug response | KCTD3's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.37; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | RPRD2's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | RPRD2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.390 over the table, 0.043 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **-** arm (projection on the module's main direction -0.755). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-1.4, 16.2); signed map (22.4, -17.4). **Vector** length 111, 36.2% of its response variance represented; |z| ≥ 3 in 1,341 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +14.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.4 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +7.4 | +3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.9 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | +5.6 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +10.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +4.5 | +1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +4.4 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.8 | -10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.5 | -26.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.9 | -23.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.2 | -18.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -5.1 | -3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.2 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | regulation of nuclear pre-mRNA domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:150,363,091-150,476,566 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32145, HSPC099; previously KIAA0460 |
| Gene groups (HGNC) | CTD interacting domain containing; Regulation of nuclear pre-mRNA domain containing |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

UniProt [Q5VT52](https://www.uniprot.org/uniprotkb/Q5VT52) carries no function annotation.

**Summary**, from NCBI Gene [23248](https://www.ncbi.nlm.nih.gov/gene/23248):

> Predicted to enable RNA polymerase II complex binding activity. Predicted to be involved in mRNA 3'-end processing. Part of transcription preinitiation complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29039](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29039) · Entrez [23248](https://www.ncbi.nlm.nih.gov/gene/23248) · UniProt [Q5VT52](https://www.uniprot.org/uniprotkb/Q5VT52) · Ensembl [ENSG00000163125](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163125)

## Data

Gene col 8637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8637); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8637]; `tensor/DDL_lfc|DDL_z.npy` [8637]; `embed/gene_vectors.npy` [8637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8637 or target_col == 8637). Every well: [[RPRD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPRD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
