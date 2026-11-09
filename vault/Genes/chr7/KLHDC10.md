---
symbol: "KLHDC10"
type: "gene"
col: 4904
ensembl_id: "ENSG00000128607"
name: "kelch domain containing 10"
location: "7q32.2"
module: 30
arm: "+"
pooled_cpm: 128.98
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# KLHDC10

*kelch domain containing 10* — 7q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.94× (z +10.2, q 1e-21, up in 37 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.421× (z -24.5, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.691× (z -15.4, q 0e+00, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASB7]] (+0.81, fdr 7e-06), [[CRYZL1]] (+0.78, fdr 7e-06), [[MED23]] (+0.75, fdr 7e-06); moves opposite to [[THOC6]] (-0.69, fdr 7e-06), [[SKIL]] (-0.67, fdr 7e-06), [[HNRNPK]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SNHG18]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4904.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.94×** | +10.2 | 1e-21 | 37/49 (KATO III, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +8.5 | 8e-15 | 33/48 (C-33 A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +8.3 | 2e-14 | 33/48 (C32, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +8.2 | 3e-14 | 37/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.26×** | +6.8 | 1e-09 | 26/48 (PANC-1, C32, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +6.2 | 5e-08 | 27/48 (C32, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.16× | +6.2 | 6e-08 | 18/48 (Panc 03.27, RKO, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | **1.21×** | +5.3 | 6e-06 | 24/47 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +5.2 | 1e-05 | 22/48 (C32, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.1 | 2e-05 | 23/48 (C-33 A, C32, …) | all doses, flat | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.18× | +4.9 | 4e-05 | 18/48 (RKO, SHP-77, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.33×** | +4.4 | 6e-04 | 19/49 (C32, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.005 | 14/49 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.10× | +3.7 | 0.007 | 4/48 (HT-29, RKO, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.09× | +3.5 | 0.020 | 1/48 (MIA PaCa-2) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.058 | 16/47 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.08× | +3.0 | 0.063 | 3/48 (HT-29, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4904.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.421×** | -24.5 | 0e+00 | 41/44 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.448×** | -23.6 | 0e+00 | 48/49 (AN3 CA, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.691×** | -15.4 | 0e+00 | 33/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.612×** | -13.4 | 2e-38 | 34/45 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.690×** | -10.5 | 9e-24 | 33/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.716×** | -9.8 | 8e-21 | 34/48 (AsPC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.744×** | -8.7 | 2e-16 | 38/48 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.832×** | -7.7 | 1e-12 | 23/48 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **0.773×** | -7.6 | 2e-12 | 29/48 (SW 900, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.807×** | -5.9 | 3e-07 | 26/47 (RKO, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.821×** | -5.8 | 3e-07 | 25/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.823×** | -5.7 | 4e-07 | 26/49 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.825×** | -5.7 | 6e-07 | 24/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~9% of this change | 0.840× | -4.9 | 3e-05 | 23/47 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.867× | -4.2 | 9e-04 | 12/48 (J82, LS 180, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.867× | -4.1 | 0.002 | 18/48 (J82, C32, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.867× | -4.0 | 0.002 | 16/47 (SW 1271, A498, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.898× | -3.2 | 0.042 | 6/48 (LS 180, SW 1088, …) | top dose only |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.894× | -3.1 | 0.049 | 6/48 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.933× | -2.9 | 0.093 | 2/48 (C-33 A, CHP-212) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4904. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 102 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -26.0) |
| [[A498 (line)]] | wt | 293 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.572× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 151 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -30.2) |
| [[C32 (line)]] | wt | 274 | 2 | 6 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 3.37× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -24.0) |
| [[PANC-1 (line)]] | alt | 103 | 5 (4 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.13× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.30× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -13.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 111 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -17.0) |
| [[HOP62 (line)]] | alt | 102 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -17.1) |
| [[HS-578T (line)]] | alt | 207 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -21.7) |
| [[hTERT-HPNE (line)]] | wt | 85.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -15.5) |
| [[SW480 (line)]] | alt | 130 | 3 (2 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.60× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.36× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.573× (z -10.5) |
| [[SNU-423 (line)]] | alt | 102 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -22.5) |
| [[AN3 CA (line)]] | alt | 363 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0927× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.259× (z -17.6) |
| [[Hs 766T (line)]] | wt | 148 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -14.4) |
| [[J82 (line)]] | alt | 110 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -18.8) |
| [[KATO III (line)]] | alt | 142 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.70× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -16.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 102 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -17.5) |
| [[NCI-H2347 (line)]] | alt | 118 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 128 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 137 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.482× (z -11.2) |
| [[SW 900 (line)]] | alt | 160 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.548× (z -10.7) |
| [[C-33 A (line)]] | alt | 122 | 1 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.25× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -12.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 102 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.56× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 130 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -28.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.359× (z -19.5) |
| [[RKO (line)]] | wt | 121 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.96× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.494× (z -8.8) |
| [[SW1417 (line)]] | alt | 194 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -21.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 142 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.5) |
| [[HCT15 (line)]] | alt | 154 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -11.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 107 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.447× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.620× (z -9.5) |
| [[LS 180 (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -12.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -18.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 251 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.3) |
| [[A-427 (line)]] | wt | 80.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -26.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -26.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 90.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 97.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -10.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 66.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 89.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.420× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 179 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.573× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 98.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -12.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.411× (z -11.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 94.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4904), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB7]] | +0.81 | +0.80 / +0.81 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.78 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[MED23]] | +0.75 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[KLHL7]] | +0.74 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[TENT2]] | +0.72 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[CCZ1B]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[FAM174A]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[NUP54]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[CCZ1]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[CWC15]] | +0.71 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[ZFP14]] | +0.70 | +0.69 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | -0.69 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[SKIL]] | -0.67 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.66 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[HNRNPA2B1]] | -0.64 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.64 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.63 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[PHF19]] | -0.62 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[PIEZO1]] | -0.62 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[ELK4]] | -0.61 | -0.54 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG18]] | B | SNHG18 activity raises KLHDC10's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.27× lower at baseline in the lines without SNHG18 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.727). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-1.7, -13.0); signed map (-33.4, -4.7). **Vector** length 141, 45.0% of its response variance represented; |z| ≥ 3 in 1,260 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +8.0 | +8.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +10.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.6 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.0 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +4.9 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.2 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +6.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +3.4 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -12.0 | -15.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -11.7 | -24.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -10.7 | -23.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -10.0 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.6 | -9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.4 | -5.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | kelch domain containing 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.2 — chr7:130,070,534-130,135,705 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0265, slim |
| Reactome | 3 pathways, smallest: Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide; Ribosome-associated quality control; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PID8](https://www.uniprot.org/uniprotkb/Q6PID8) (Kelch domain-containing protein 10):

> Substrate-recognition component of a Cul2-RING (CRL2) E3 ubiquitin-protein ligase complex of the DesCEND (destruction via C-end degrons) pathway, which recognizes a C-degron located at the extreme C-terminus of target proteins, leading to their ubiquitination and degradation. The C-degron recognized by the DesCEND pathway is usually a motif of less than ten residues and can be present in full-length proteins, truncated proteins or proteolytically cleaved forms. The CRL2(KLHDC10) complex …

**Summary**, from NCBI Gene [23008](https://www.ncbi.nlm.nih.gov/gene/23008):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in rescue of stalled cytosolic ribosome and ubiquitin-dependent protein catabolic process via the C-end degron rule pathway. Is active in Cul2-RING ubiquitin ligase complex and cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22194](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22194) · Entrez [23008](https://www.ncbi.nlm.nih.gov/gene/23008) · UniProt [Q6PID8](https://www.uniprot.org/uniprotkb/Q6PID8) · Ensembl [ENSG00000128607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128607)

## Data

Gene col 4904: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4904); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4904, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4904]; `tensor/DDL_lfc|DDL_z.npy` [4904]; `embed/gene_vectors.npy` [4904]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4904 or target_col == 4904). Every well: [[KLHDC10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHDC10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
