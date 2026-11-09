---
symbol: "LNPK"
type: "gene"
col: 6864
ensembl_id: "ENSG00000144320"
name: "lunapark, ER junction formation factor"
location: "2q31.1"
module: 164
arm: "+"
pooled_cpm: 107.1
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# LNPK

*lunapark, ER junction formation factor* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +11.7, q 1e-28, up in 40 of 50 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.439× (z -24.9, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX3]] (+0.74, fdr 7e-06), [[HELZ]] (+0.71, fdr 7e-06), [[VDAC3]] (+0.69, fdr 7e-06); moves opposite to [[SKIL]] (-0.56, fdr 3e-05), [[C22orf46]] (-0.54, fdr 1e-05), [[IER2]] (-0.54, fdr 1e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[VPS37A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +11.7 | 1e-28 | 40/50 (LS 180, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +11.2 | 8e-27 | 42/48 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.29×** | +7.6 | 5e-12 | 29/49 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +5.7 | 2e-06 | 25/48 (A-427, COLO 205, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +5.3 | 2e-05 | 28/48 (A498, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.27×** | +5.2 | 2e-05 | 28/48 (COLO 205, A-427, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.26×** | +4.9 | 7e-05 | 26/48 (SW48, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.25×** | +4.8 | 1e-04 | 24/48 (PANC-1, A-427, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.24×** | +4.6 | 3e-04 | 23/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.001 | 24/49 (PANC-1, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.002 | 22/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.003 | 20/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.7 | 0.011 | 11/48 (LoVo, PANC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.063 | 14/49 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.081 | 13/48 (MIA PaCa-2, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.093 | 7/48 (NCI-H2030, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6864.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.439×** | -24.9 | 0e+00 | 40/48 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.535×** | -13.4 | 3e-38 | 40/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.540×** | -12.7 | 1e-34 | 43/47 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.601×** | -10.5 | 2e-23 | 37/48 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.725×** | -6.9 | 7e-10 | 33/48 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.740×** | -6.4 | 1e-08 | 31/48 (C32, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.746×** | -6.0 | 1e-07 | 30/47 (HepG2/C3A, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.738×** | -6.0 | 1e-07 | 27/45 (HCT15, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.781×** | -5.3 | 8e-06 | 31/48 (NCI-H460, SNU-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -5.0 | 3e-05 | 23/48 (HOP62, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.804×** | -4.6 | 2e-04 | 24/48 (SW 900, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.805×** | -4.6 | 2e-04 | 29/49 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.864× | -4.4 | 4e-04 | 14/48 (A-172, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.828×** | -4.0 | 0.002 | 23/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.839× | -3.6 | 0.011 | 19/44 (SK-MEL-2, HCT15, …) | inconsistent across doses | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | 0.839× | -3.6 | 0.011 | 20/47 (HT-29, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **0.799×** | -3.4 | 0.020 | 22/48 (C32, HT-29, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.737×** | -3.4 | 0.020 | 20/49 (HCT15, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.848× | -3.4 | 0.020 | 17/48 (C32, J82, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.896× | -3.3 | 0.023 | 8/48 (HS-578T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.856× | -3.3 | 0.023 | 17/47 (MIA PaCa-2, NCI-H23, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 306 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -39.2) |
| [[NCI-H460 (line)]] | wt | 143 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -26.0) |
| [[SK-MEL-2 (line)]] | alt | 126 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -28.4) |
| [[J82 (line)]] | alt | 151 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -21.6) |
| [[PANC-1 (line)]] | alt | 57.3 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +15.0) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.7) | — |
| [[A-427 (line)]] | wt | 56.1 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +11.8) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +9.6) | — |
| [[A498 (line)]] | wt | 108 | 1 | 4 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.06× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -22.9) |
| [[HCT15 (line)]] | alt | 158 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -22.1) |
| [[HEC-1-A (line)]] | alt | 171 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -26.3) |
| [[NCI-H23 (line)]] | alt | 68.2 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +12.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.7) | — |
| [[A-172 (line)]] | wt | 191 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -29.0) |
| [[AsPC-1 (line)]] | alt | 56.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -12.7) |
| [[HOP62 (line)]] | alt | 138 | 1 | 3 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -24.0) |
| [[HS-578T (line)]] | alt | 120 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -24.6) |
| [[LOX-IMVI (line)]] | wt | 101 | 3 (1 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -16.0) |
| [[LS 180 (line)]] | wt | 87.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.386× (z -10.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 126 | 1 | 3 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -20.2) |
| [[NCI-H1792 (line)]] | alt | 123 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -19.5) |
| [[NCI-H2030 (line)]] | alt | 95.7 | 3 (1 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -10.1) |
| [[SW 900 (line)]] | alt | 144 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -13.2) |
| [[AN3 CA (line)]] | alt | 199 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0667× (z -19.8) |
| [[HepG2_C3A (line)]] | wt | 134 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.222× (z -14.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.418× (z -12.0) |
| [[Hs 766T (line)]] | wt | 110 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -15.2) |
| [[LoVo (line)]] | wt | 54.5 | 2 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +11.3) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 50.2 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +11.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[RPMI-7951 (line)]] | alt | 167 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -29.7) |
| [[SW48 (line)]] | wt | 78.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 50.4 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +10.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[H4 (line)]] | wt | 120 | 1 | 1 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -17.6) |
| [[NCI-H2347 (line)]] | alt | 93.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -14.7) |
| [[Panc 03.27 (line)]] | alt | 81.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -9.6) |
| [[RKO (line)]] | wt | 113 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -13.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 127 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -31.0) |
| [[C-33 A (line)]] | alt | 86.8 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -13.4) |
| [[CHP-212 (line)]] | wt | 138 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.7) |
| [[HT-29 (line)]] | alt | 81.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.462× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.1) |
| [[SHP-77 (line)]] | alt | 90.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.7) |
| [[SNU-1 (line)]] | wt | 122 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.351× (z -8.9) |
| [[SW 1088 (line)]] | alt | 143 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -9.0) |
| [[SW 1271 (line)]] | alt | 135 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -8.5) |
| [[SW1417 (line)]] | alt | 84.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW480 (line)]] | alt | 86.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.476× (z -10.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 72.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX3]] | +0.74 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[HELZ]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[VDAC3]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[PLEKHA8]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[HERC3]] | +0.66 | +0.69 / +0.57 | both halves | 9e-06 |  |
| [[PLEKHA2]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[PDK1]] | +0.65 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[USP37]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[CABIN1]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[IARS2]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SMAP2]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ECI2]] | +0.63 | +0.69 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKIL]] | -0.56 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[C22orf46]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[IER2]] | -0.54 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[CHTOP]] | -0.53 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[SFPQ]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ZNF274]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[SRGAP1]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[NANOS3]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[PMEPA1]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[PPP1R10]] | -0.52 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[NOP56]] | -0.52 | -0.55 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LNPK's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VPS37A]] | C | LNPK's natural level weakens VPS37A's drug response | LNPK's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.11; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.727). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.5, -17.8); signed map (-37.6, 22.9). **Vector** length 151, 50.3% of its response variance represented; |z| ≥ 3 in 1,305 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +11.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +11.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.0 | +5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.2 | +3.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +4.0 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.6 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.4 | -24.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.0 | -6.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.0 | -12.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.8 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -13.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.3 | -5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.8 | -2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | lunapark, ER junction formation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:175,923,882-176,002,839 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ul, LNP1, LNP; previously KIAA1715 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0E8](https://www.uniprot.org/uniprotkb/Q9C0E8) (Endoplasmic reticulum junction formation protein lunapark):

> Endoplasmic reticulum (ER)-shaping membrane protein that plays a role in determining ER morphology. Involved in the stabilization of nascent three-way ER tubular junctions within the ER network. May also play a role as a curvature-stabilizing protein within the three-way ER tubular junction network. May be involved in limb development (By similarity). Is involved in central nervous system development.

**Summary**, from NCBI Gene [80856](https://www.ncbi.nlm.nih.gov/gene/80856):

> Enables identical protein binding activity. Involved in endoplasmic reticulum tubular network maintenance and positive regulation of endoplasmic reticulum tubular network organization. Located in endoplasmic reticulum tubular network membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21610](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21610) · Entrez [80856](https://www.ncbi.nlm.nih.gov/gene/80856) · UniProt [Q9C0E8](https://www.uniprot.org/uniprotkb/Q9C0E8) · Ensembl [ENSG00000144320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144320)

## Data

Gene col 6864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6864); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6864]; `tensor/DDL_lfc|DDL_z.npy` [6864]; `embed/gene_vectors.npy` [6864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6864 or target_col == 6864). Every well: [[LNPK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LNPK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
