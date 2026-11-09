---
symbol: "TET2"
type: "gene"
col: 9694
ensembl_id: "ENSG00000168769"
name: "tet methylcytosine dioxygenase 2"
location: "4q24"
module: 95
arm: "+"
pooled_cpm: 114.02
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# TET2

*tet methylcytosine dioxygenase 2* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.51× (z +12.6, q 2e-33, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.287× (z -25.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF827]] (+0.73, fdr 1e-05), [[HFE]] (+0.66, fdr 3e-05), [[BAZ2B]] (+0.64, fdr 4e-05); moves opposite to [[LYPLA1]] (-0.66, fdr 1e-05), [[TPD52L2]] (-0.61, fdr 3e-05), [[VKORC1L1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CA11]] → it (grade B ⚠); 4 go from it, the strongest it → cells under [[Almonertinib (mesylate) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9694.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.51×** | +12.6 | 2e-33 | 47/49 (NCI-H1573, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +8.8 | 4e-16 | 38/48 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +8.2 | 4e-14 | 28/48 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +5.8 | 9e-07 | 32/48 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +5.5 | 4e-06 | 33/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +5.2 | 2e-05 | 26/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.16× | +4.4 | 8e-04 | 20/48 (A498, LS 180, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.008 | 24/48 (NCI-H1573, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.017 | 15/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.20× | +3.6 | 0.017 | 20/47 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.041 | 17/47 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.041 | 13/48 (NCI-H2347, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[Tadalafil (drug)]] 5 µM |  | 1.18× | +3.3 | 0.043 | 15/48 (hTERT-HPNE, NCI-H661, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.18× | +3.2 | 0.047 | 19/50 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.17× | +3.2 | 0.056 | 18/48 (A498, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9694.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.287×** | -25.9 | 0e+00 | 48/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.307×** | -24.5 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.393×** | -19.4 | 0e+00 | 47/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.456×** | -16.3 | 0e+00 | 47/49 (NCI-H1792, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.461×** | -15.5 | 0e+00 | 39/44 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.496×** | -13.5 | 2e-39 | 42/45 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.570×** | -11.2 | 3e-27 | 44/47 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.615×** | -10.1 | 4e-22 | 42/48 (hTERT-HPNE, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.770×** | -7.7 | 9e-13 | 31/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.691×** | -7.7 | 9e-13 | 34/48 (C32, H4, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.757×** | -5.5 | 1e-06 | 29/47 (CFPAC-1, NCI-H2030, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.763×** | -5.4 | 3e-06 | 30/50 (hTERT-HPNE, H4, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.710×** | -5.0 | 3e-05 | 36/48 (CHP-212, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.792×** | -4.8 | 5e-05 | 29/48 (AN3 CA, SW48, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.795×** | -4.7 | 8e-05 | 28/48 (hTERT-HPNE, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.744×** | -4.3 | 6e-04 | 30/48 (hTERT-HPNE, C-33 A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.833× | -3.8 | 0.005 | 23/48 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.686×** | -3.8 | 0.005 | 23/46 (NCI-H460, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.829×** | -3.7 | 0.005 | 22/48 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.704×** | -3.5 | 0.011 | 21/49 (hTERT-HPNE, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.846× | -3.5 | 0.013 | 20/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.847× | -3.3 | 0.022 | 21/48 (COLO 205, BT-474, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.897× | -3.2 | 0.032 | 12/49 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9694. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 220 | 4 (1 ⚠) | 8 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -19.4) |
| [[HOP62 (line)]] | alt | 133 | 1 | 9 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.08× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.183× (z -21.5) |
| [[LS 180 (line)]] | wt | 172 | 4 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.42× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.250× (z -18.0) |
| [[NCI-H460 (line)]] | wt | 129 | 3 (1 ⚠) | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.89× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.317× (z -15.7) |
| [[C32 (line)]] | wt | 158 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -16.5) |
| [[NCI-H1792 (line)]] | alt | 220 | 1 | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.13× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -23.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.197× (z -21.4) |
| [[CFPAC-1 (line)]] | alt | 187 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.274× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 171 | 3 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.73× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.252× (z -21.2) |
| [[hTERT-HPNE (line)]] | wt | 169 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -19.0) |
| [[BT-474 (line)]] | alt | 123 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -15.0) |
| [[LOX-IMVI (line)]] | wt | 123 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.284× (z -13.9) |
| [[A498 (line)]] | wt | 72.0 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -15.8) |
| [[AN3 CA (line)]] | alt | 276 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.265× (z -10.8) |
| [[HCT15 (line)]] | alt | 202 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.354× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 134 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.291× (z -14.7) |
| [[RPMI-7951 (line)]] | alt | 163 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -19.7) |
| [[SW480 (line)]] | alt | 59.5 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.46× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.204× (z -21.4) |
| [[A549 (line)]] | wt | 70.9 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.223× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 80.3 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.352× (z -10.8) |
| [[CHP-212 (line)]] | wt | 282 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.200× (z -13.1) |
| [[H4 (line)]] | wt | 144 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -20.2) |
| [[Hs 766T (line)]] | wt | 83.3 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -16.0) |
| [[MIA PaCa-2 (line)]] | alt | 86.3 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.39× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.374× (z -10.2) |
| [[SW1417 (line)]] | alt | 82.7 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.232× (z -18.3) |
| [[SW48 (line)]] | wt | 102 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -11.8) |
| [[A-172 (line)]] | wt | 102 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.420× (z -10.2) |
| [[A-427 (line)]] | wt | 98.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C-33 A (line)]] | alt | 276 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.340× (z -10.5) |
| [[COLO 205 (line)]] | alt | 137 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 7.04× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.179× (z -16.1) |
| [[HT-29 (line)]] | alt | 77.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -12.9) |
| [[LoVo (line)]] | wt | 83.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 110 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -16.1) |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -14.2) |
| [[SNU-1 (line)]] | wt | 162 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 73.7 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.61× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -15.2) |
| [[SW 900 (line)]] | alt | 123 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -15.0) |
| [[HepG2_C3A (line)]] | wt | 137 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.362× (z -9.2) |
| [[HS-578T (line)]] | alt | 75.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -15.3) |
| [[KATO III (line)]] | alt | 84.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.189× (z -18.6) |
| [[NCI-H2030 (line)]] | alt | 84.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.32× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 65.4 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.368× (z -9.7) |
| [[RKO (line)]] | wt | 125 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.386× (z -10.0) |
| [[SHP-77 (line)]] | alt | 113 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -13.8) |
| [[J82 (line)]] | alt | 78.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -12.8) |
| [[PANC-1 (line)]] | alt | 50.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.445× (z -10.2) |
| [[SW 1271 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Decitabine (drug)]] 0.05 µM 0.0950× (z -9.5) |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 124 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9694), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF827]] | +0.73 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[HFE]] | +0.66 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[BAZ2B]] | +0.64 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[TAPBPL]] | +0.62 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[MEIS2]] | +0.62 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[TCEAL1]] | +0.61 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[EMSY-DT]] | +0.61 | +0.42 / +0.38 | both halves | 6e-05 |  |
| [[ZNF436]] | +0.61 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[HMG20A]] | +0.61 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[CDKN1B]] | +0.60 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[RBKS]] | +0.60 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[ZFX]] | +0.60 | +0.41 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPLA1]] | -0.66 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[TPD52L2]] | -0.61 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[VKORC1L1]] | -0.60 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[PBX4]] | -0.60 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[WRN]] | -0.60 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[TRABD]] | -0.60 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ANKS6]] | -0.60 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[NTAQ1]] | -0.59 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[LPCAT1]] | -0.59 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[GNB1L]] | -0.58 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[TMEM241]] | -0.57 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[ST6GALNAC6]] | -0.57 | -0.39 / -0.50 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA11]] | B | CA11 activity lowers TET2's level | lines that do not express CA11 (6) vs lines expressing it (44) | 1.38× higher at baseline in the lines without CA11 | 0.027 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Almonertinib (mesylate) (drug)]] 5 µM | C | TET2's natural level lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | TET2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.78 | 0.120 over the table, 3e-04 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Adagrasib (drug)]] 0.5 µM | C | TET2's natural level raises the cells' numbers under Adagrasib 0.5 µM (protects the cells) | TET2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63 | 0.406 over the table, 0.072 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | TET2's natural level raises the cells' numbers under Fluvoxamine 0.5 µM (protects the cells) | TET2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.476 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | TET2's natural level raises the cells' numbers under Bendamustine 0.5 µM (protects the cells) | TET2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.478 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (13.3, 4.0); signed map (23.1, -16.9). **Vector** length 114, 39.8% of its response variance represented; |z| ≥ 3 in 1,385 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chromatin organization* (reactome, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +9.8 | +0.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +8.2 | +4.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.6 | +12.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.5 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +8.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.4 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +2.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +4.1 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.9 | +2.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -11.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -5.1 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.8 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.3 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -25.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -7.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | tet methylcytosine dioxygenase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:105,145,875-105,279,816 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20032; previously KIAA1546 |
| Gene groups (HGNC) | Tet methylcytosine dioxygenase family |
| Reactome | 6 pathways, smallest: TET1,2,3 and TDG demethylate DNA; Specification of primordial germ cells; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6N021](https://www.uniprot.org/uniprotkb/Q6N021) (Methylcytosine dioxygenase TET2):

> Dioxygenase that catalyzes the conversion of the modified genomic base 5-methylcytosine (5mC) into 5-hydroxymethylcytosine (5hmC) and plays a key role in active DNA demethylation. Has a preference for 5-hydroxymethylcytosine in CpG motifs. Also mediates subsequent conversion of 5hmC into 5-formylcytosine (5fC), and conversion of 5fC to 5-carboxylcytosine (5caC). Conversion of 5mC into 5hmC, 5fC and 5caC probably constitutes the first step in cytosine demethylation. Methylation at the C5 …

**Summary**, from NCBI Gene [54790](https://www.ncbi.nlm.nih.gov/gene/54790):

> The protein encoded by this gene is a methylcytosine dioxygenase that catalyzes the conversion of methylcytosine to 5-hydroxymethylcytosine. The encoded protein is involved in myelopoiesis, and defects in this gene have been associated with several myeloproliferative disorders. Two variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:25941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25941) · Entrez [54790](https://www.ncbi.nlm.nih.gov/gene/54790) · UniProt [Q6N021](https://www.uniprot.org/uniprotkb/Q6N021) · Ensembl [ENSG00000168769](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168769)

## Data

Gene col 9694: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9694); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9694, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9694]; `tensor/DDL_lfc|DDL_z.npy` [9694]; `embed/gene_vectors.npy` [9694]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9694 or target_col == 9694). Every well: [[TET2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TET2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
