---
symbol: "IL17RD"
type: "gene"
col: 6920
ensembl_id: "ENSG00000144730"
name: "interleukin 17 receptor D"
location: "3p14.3"
module: 30
arm: "+"
pooled_cpm: 11.68
n_lines_expressing: 46
n_dd_up: 18
n_dd_down: 24
n_dd_up_clean: 13
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# IL17RD

*interleukin 17 receptor D* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.16× (z +10.1, q 2e-21, up in 36 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.351× (z -19.4, q 0e+00, down in 36 of 43 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.408× (z -11.8, q 6e-30, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMSAP1]] (+0.64, fdr 1e-05), [[TMOD2]] (+0.63, fdr 1e-05), [[ABRAXAS1]] (+0.63, fdr 1e-05); moves opposite to [[RBM23]] (-0.60, fdr 1e-05), [[BMS1P4-1]] (-0.55, fdr 3e-05), [[MZF1-AS1]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SCN5A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[POMGNT2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6920.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.16×** | +10.1 | 2e-21 | 36/43 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +9.5 | 4e-19 | 31/43 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +8.4 | 9e-15 | 25/43 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.53×** | +7.9 | 3e-13 | 24/43 (LoVo, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +5.7 | 2e-06 | 22/44 (NCI-H460, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +5.6 | 2e-06 | 20/41 (SHP-77, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +5.3 | 9e-06 | 20/43 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.02×** | +4.8 | 1e-04 | 12/43 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.005 | 7/44 (HS-578T, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.34×** | +3.9 | 0.005 | 5/44 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +3.6 | 0.020 | 14/41 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.32×** | +3.4 | 0.028 | 6/44 (Hs 766T, HEC-1-A, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.60×** | +3.2 | 0.055 | 2/43 (C-33 A, A-427) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.39×** | +3.1 | 0.080 | 2/44 (SW480, NCI-H2347) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.080 | 8/42 (LS 180, NCI-H2030, …) | two highest doses | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.080 | 7/43 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.080 | 6/40 (SNU-423, SNU-1, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.096 | 4/44 (HCT15, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6920.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.351×** | -19.4 | 0e+00 | 36/43 (HEC-1-A, A549, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.316×** | -14.5 | 3e-45 | 38/43 (HEC-1-A, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.395×** | -12.2 | 6e-32 | 34/41 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.402×** | -12.0 | 9e-31 | 35/43 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.408×** | -11.8 | 6e-30 | 32/42 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.448×** | -10.5 | 6e-24 | 25/40 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.458×** | -10.2 | 1e-22 | 30/42 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.263×** | -9.1 | 4e-18 | 31/41 (Panc 03.27, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.503×** | -9.0 | 1e-17 | 26/42 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.518×** | -8.6 | 4e-16 | 26/43 (PANC-1, SK-MEL-2, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.568×** | -7.4 | 6e-12 | 28/43 (PANC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.611×** | -6.1 | 5e-08 | 24/41 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.624×** | -5.9 | 1e-07 | 20/37 (A-172, NCI-H23, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.422×** | -5.9 | 1e-07 | 21/39 (SNU-423, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.675×** | -5.1 | 1e-05 | 22/43 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.776×** | -4.7 | 1e-04 | 18/44 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.666×** | -3.8 | 0.004 | 10/44 (H4, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.739×** | -3.7 | 0.006 | 16/42 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.679×** | -3.6 | 0.008 | 14/41 (SW 900, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bergenin (drug)]] 0.5 µM |  | **0.795×** | -3.0 | 0.068 | 14/41 (C32, LS 180, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.735×** | -2.9 | 0.098 | 10/36 (NCI-H1792, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6920. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 25.2 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -23.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 18.4 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -16.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0409× (z -16.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.177× (z -8.7) |
| [[A-427 (line)]] | wt | 34.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -12.7) |
| [[PANC-1 (line)]] | alt | 8.11 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0607× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.219× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -13.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0575× (z -13.2) |
| [[AN3 CA (line)]] | alt | 82.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0559× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 6.10 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -8.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.148× (z -8.6) |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0312× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 23.6 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.176× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -15.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0344× (z -8.7) |
| [[SW480 (line)]] | alt | 26.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.291× (z -10.1) |
| [[A-172 (line)]] | wt | 7.56 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0705× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~37% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0878× (z -9.4) |
| [[A549 (line)]] | wt | 13.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0850× (z -19.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 10.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.204× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.239× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 33.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -13.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW48 (line)]] | wt | 25.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0837× (z -17.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0586× (z -13.7) |
| [[A498 (line)]] | wt | 6.14 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -9.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 6.17 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0936× (z -8.6) |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 4.85 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 18.9× (z +8.6) ⚠ unreliable plate only | — |
| [[CFPAC-1 (line)]] | alt | 7.75 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 9.24 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0615× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 5.67 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0671× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 9.95 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.129× (z -9.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.137× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[RPMI-7951 (line)]] | alt | 7.81 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -9.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 7.78 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -9.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6920), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMSAP1]] | +0.64 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TMOD2]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ABRAXAS1]] | +0.63 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[STX7]] | +0.63 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[LTA4H]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[MFSD10]] | +0.61 | +0.64 / +0.33 | both halves | 1e-04 |  |
| [[BMP8B]] | +0.61 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[SLC66A3]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RAB6B]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[LPCAT2]] | +0.59 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[IMPDH2]] | +0.59 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[SEMA4F]] | +0.59 | +0.40 / +0.52 | both halves | 5e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM23]] | -0.60 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[BMS1P4-1]] | -0.55 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[MZF1-AS1]] | -0.54 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ASH1L]] | -0.54 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[GTF2IRD2]] | -0.54 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[RBX1]] | -0.53 | -0.38 / -0.48 | both halves | 6e-05 | pathway: MAPK family signaling cascades |
| [[LSM1]] | -0.53 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SON]] | -0.52 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[ZFX]] | -0.52 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[LINC01252]] | -0.52 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[GTF2IRD2B]] | -0.50 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[EFCAB2]] | -0.50 | -0.41 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCN5A]] | B | SCN5A activity raises IL17RD's level | lines that do not express SCN5A (26) vs lines expressing it (24) | 2.09× lower at baseline in the lines without SCN5A | 0.020 | ⚠ within organs, on part of the lines; also absent: ANKRD20A11P, OLFML2A, SHISA9 |
| [[RIMS3]] | B | RIMS3 activity raises IL17RD's level | lines that do not express RIMS3 (9) vs lines expressing it (41) | 2.43× lower at baseline in the lines without RIMS3 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: STOX1, ZFP69B, LINC02456; maybe low, not absent |
| [[GJA3]] | B | GJA3 activity raises IL17RD's level | lines that do not express GJA3 (17) vs lines expressing it (33) | 2.10× lower at baseline in the lines without GJA3 | 0.054 | ⚠ within organs, on part of the lines; also absent: GBX1 |
| [[MTOR]] | B | MTOR activity lowers IL17RD's level | compounds that target MTOR: 4 of 8 raise it (AZD-8055, Bimiralisib, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 3.6% of all compounds | 0.058 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PNMA2]] | B | PNMA2 activity raises IL17RD's level | lines that do not express PNMA2 (16) vs lines expressing it (34) | 1.41× lower at baseline in the lines without PNMA2 | 0.098 | ⚠ within organs, on part of the lines; also absent: MCOLN3, CACNG6, SELENOM |
| [[GARNL3]] | C | GARNL3 activity raises IL17RD's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 2.40× lower at baseline in the lines without GARNL3 | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POMGNT2]] | C | IL17RD activity raises POMGNT2's level | lines that do not express IL17RD (4) vs lines expressing it (46) | 1.53× lower at baseline in the lines without IL17RD | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PRKAG2, ZNF391, FAM89A; its own permutation p |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.395). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-2.7, -4.0); signed map (-34.3, -12.8). **Vector** length 84.0, 17.6% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +4.4 | +7.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.0 | +8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +10.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +9.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.0 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.3 | -19.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.9 | -14.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | +0.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.4 | -1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 17 receptor D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:57,089,982-57,170,306 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEF, IL17RLM, FLJ35755, IL-17RD |
| Gene groups (HGNC) | Interleukin receptors; TIR domain containing |
| Reactome | 4 pathways, smallest: MAP2K and MAPK activation; RAF/MAP kinase cascade; MAPK1/MAPK3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFM7](https://www.uniprot.org/uniprotkb/Q8NFM7) (Interleukin-17 receptor D):

> Feedback inhibitor of fibroblast growth factor mediated Ras-MAPK signaling and ERK activation. Regulates the nuclear ERK signaling pathway by spatially blocking nuclear translocation of activated ERK without inhibiting cytoplasmic phosphorylation of ERK. Mediates JNK activation and may be involved in apoptosis (By similarity). May inhibit FGF-induced FGFR1 tyrosine phosphorylation (By similarity). Might have a role in the early stages of fate specification of GnRH-secreting neurons (By …

**Summary**, from NCBI Gene [54756](https://www.ncbi.nlm.nih.gov/gene/54756):

> This gene encodes a membrane protein belonging to the interleukin-17 receptor (IL-17R) protein family. The encoded protein is a component of the interleukin-17 receptor signaling complex, and the interaction between this protein and IL-17R does not require the interleukin. The gene product also affects fibroblast growth factor signaling, inhibiting or stimulating growth through MAPK/ERK signaling. Alternate splicing generates multiple transcript variants encoding distinct isoforms. [provided by …

**Accessions** — [HGNC:17616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17616) · Entrez [54756](https://www.ncbi.nlm.nih.gov/gene/54756) · UniProt [Q8NFM7](https://www.uniprot.org/uniprotkb/Q8NFM7) · Ensembl [ENSG00000144730](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144730)

## Data

Gene col 6920: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6920); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6920, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6920]; `tensor/DDL_lfc|DDL_z.npy` [6920]; `embed/gene_vectors.npy` [6920]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6920 or target_col == 6920). Every well: [[IL17RD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL17RD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
