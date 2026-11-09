---
symbol: "EPRS1"
type: "gene"
col: 5883
ensembl_id: "ENSG00000136628"
name: "glutamyl-prolyl-tRNA synthetase 1"
location: "1q41"
module: 63
arm: "+"
pooled_cpm: 218.94
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 23
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# EPRS1

*glutamyl-prolyl-tRNA synthetase 1* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.83× (z +11.5, q 9e-28, up in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Artesunate (drug)]] 5 µM: 1.32× (z +6.7, q 2e-09, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.406× (z -21.9, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCEA1]] (+0.86, fdr 7e-06), [[XPOT]] (+0.82, fdr 7e-06), [[PSAT1]] (+0.79, fdr 7e-06); moves opposite to [[PNRC2]] (-0.60, fdr 1e-05), [[POLR2L]] (-0.54, fdr 1e-05), [[NDUFA13]] (-0.53, fdr 5e-05, ⚠ NDUFA13 in the vector space only through flagged drug-doses), [[UNK]] (-0.53, fdr 4e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ANK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5883.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +11.5 | 9e-28 | 43/49 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +10.9 | 2e-25 | 41/44 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +7.1 | 2e-10 | 38/47 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.32×** | +6.7 | 2e-09 | 33/48 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.39×** | +6.2 | 5e-08 | 37/48 (Hs 766T, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.33×** | +5.5 | 5e-06 | 38/48 (SNU-1, SW48, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +5.2 | 2e-05 | 30/45 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +5.0 | 4e-05 | 30/48 (AsPC-1, SW 900, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.002 | 28/48 (Hs 766T, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.9 | 0.006 | 16/49 (NCI-H2030, SW 900, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.010 | 25/48 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.011 | 27/48 (HepG2/C3A, NCI-H1573, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.016 | 19/49 (SNU-1, NCI-H460, …) | top dose only |  |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.066 | 22/48 (NCI-H2030, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5883.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.406×** | -21.9 | 0e+00 | 46/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.429×** | -15.4 | 0e+00 | 47/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.490×** | -13.5 | 2e-39 | 47/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.519×** | -12.4 | 3e-33 | 38/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -11.4 | 6e-28 | 43/49 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.550×** | -11.3 | 1e-27 | 43/48 (A-172, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.578×** | -10.4 | 2e-23 | 43/48 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.595×** | -9.8 | 6e-21 | 42/48 (KATO III, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.667×** | -9.0 | 2e-17 | 45/48 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.641×** | -8.4 | 2e-15 | 36/48 (SNU-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -8.0 | 9e-14 | 34/47 (SW 900, H4, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.725×** | -6.1 | 6e-08 | 34/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -5.0 | 2e-05 | 30/48 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.814×** | -5.0 | 3e-05 | 21/48 (HS-578T, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.777×** | -4.8 | 7e-05 | 37/48 (AsPC-1, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.800×** | -3.9 | 0.003 | 27/47 (LoVo, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.831×** | -3.5 | 0.013 | 24/47 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.846× | -3.2 | 0.038 | 17/48 (NCI-H23, RKO, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.802×** | -3.0 | 0.071 | 16/48 (J82, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5883. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 391 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -33.8) |
| [[KATO III (line)]] | alt | 205 | 0 | 13 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.263× (z -17.9) |
| [[A498 (line)]] | wt | 428 | 2 (2 ⚠) | 10 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -23.6) |
| [[AsPC-1 (line)]] | alt | 199 | 2 (2 ⚠) | 9 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.53× (z +12.1) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -29.2) |
| [[HT-29 (line)]] | alt | 264 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -21.8) |
| [[NCI-H460 (line)]] | wt | 242 | 2 (2 ⚠) | 9 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -20.0) |
| [[SW480 (line)]] | alt | 180 | 2 (2 ⚠) | 9 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +11.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -14.0) |
| [[A-172 (line)]] | wt | 251 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -19.6) |
| [[H4 (line)]] | wt | 222 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -30.5) |
| [[HS-578T (line)]] | alt | 193 | 3 (3 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +14.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -15.6) |
| [[SW 900 (line)]] | alt | 312 | 0 | 10 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.290× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.407× (z -16.8) |
| [[SW1417 (line)]] | alt | 197 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -17.8) |
| [[NCI-H2347 (line)]] | alt | 241 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -16.6) |
| [[RKO (line)]] | wt | 313 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -21.6) |
| [[SNU-1 (line)]] | wt | 305 | 1 | 6 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.88× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -18.9) |
| [[BT-474 (line)]] | alt | 102 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -15.9) |
| [[HOP62 (line)]] | alt | 124 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 287 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -18.4) |
| [[A-427 (line)]] | wt | 281 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.475× (z -10.8) |
| [[COLO 205 (line)]] | alt | 147 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +10.3) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -13.7) |
| [[LS 180 (line)]] | wt | 251 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 130 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -14.5) |
| [[SNU-423 (line)]] | alt | 132 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -15.3) |
| [[SW48 (line)]] | wt | 359 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -15.2) |
| [[C32 (line)]] | wt | 148 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -15.2) |
| [[HepG2_C3A (line)]] | wt | 115 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +10.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.257× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.302× (z -11.4) |
| [[LoVo (line)]] | wt | 234 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -16.8) |
| [[RPMI-7951 (line)]] | alt | 171 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -17.4) |
| [[SK-MEL-2 (line)]] | alt | 112 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.190× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 152 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -10.5) |
| [[Hs 766T (line)]] | wt | 262 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.43× (z +10.4) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.424× (z -10.0) |
| [[J82 (line)]] | alt | 185 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -22.4) |
| [[NCI-H1792 (line)]] | alt | 158 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.61× (z +10.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.1) |
| [[A549 (line)]] | wt | 156 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +13.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 160 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +12.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.490× (z -8.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 128 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 127 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 189 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 201 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -13.2) |
| [[SHP-77 (line)]] | alt | 138 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +11.1) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.403× (z -9.6) |
| [[AN3 CA (line)]] | alt | 202 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.5) |
| [[HCT15 (line)]] | alt | 344 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.446× (z -9.0) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 123 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +9.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 198 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 194 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 363 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 155 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5883), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEA1]] | +0.86 | +0.87 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[XPOT]] | +0.82 | +0.83 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[PSAT1]] | +0.79 | +0.76 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 492 |
| [[AARS1]] | +0.79 | +0.78 / +0.80 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 976 |
| [[MTHFD2]] | +0.79 | +0.76 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 587 |
| [[SEC63]] | +0.78 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[NARS1]] | +0.78 | +0.74 / +0.80 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 998 |
| [[RSL24D1]] | +0.78 | +0.82 / +0.78 | both halves | 7e-06 | STRING 636 |
| [[TARS1]] | +0.78 | +0.81 / +0.82 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 928 |
| [[IARS1]] | +0.77 | +0.78 / +0.82 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[PHGDH]] | +0.77 | +0.73 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[ASNS]] | +0.77 | +0.72 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 671 |

## Genes that move opposite

*4 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNRC2]] | -0.60 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[POLR2L]] | -0.54 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[NDUFA13]] ⚠ | -0.53 | -0.62 / -0.40 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UNK]] | -0.53 | -0.51 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANK2]] | B | ANK2 activity raises EPRS1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.25× lower at baseline in the lines without ANK2 | 0.030 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[PSAT1]] | B | PSAT1 activity raises EPRS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without PSAT1 | 0.053 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[GPX8]] | B | GPX8 activity raises EPRS1's level | lines that do not express GPX8 (8) vs lines expressing it (42) | 1.17× lower at baseline in the lines without GPX8 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000232295, EMP3, LGALS1 |
| [[TOP2A]] | B | TOP2A activity raises EPRS1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KIFC3]] | C | KIFC3 activity lowers EPRS1's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 1.41× higher at baseline in the lines without KIFC3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.814). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.9, 47.4); signed map (-14.3, 24.2). **Vector** length 155, 62.2% of its response variance represented; |z| ≥ 3 in 1,438 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.66 to 16); *unfolded protein response* (hallmark, mean cos +0.69 to 11); *Response of EIF2AK1 (HRI) to heme deficiency* (reactome, mean cos +0.59 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +7.4 | +6.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +6.6 | +5.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.5 | +7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.2 | +3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.8 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.7 | +3.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +4.5 | +4.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.7 | -13.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -9.6 | -9.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.0 | -8.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.0 | -15.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.1 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -6.5 | -3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.9 | -2.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -4.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | glutamyl-prolyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:219,968,600-220,046,530 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EARS, PARS, GLUPRORS; previously QPRS, QARS, EPRS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I; Aminoacyl tRNA synthetases, Class II |
| Hallmark sets | MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 10 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; tRNA modification in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [P07814](https://www.uniprot.org/uniprotkb/P07814) (Bifunctional glutamate/proline--tRNA ligase):

> Multifunctional protein which primarily functions within the aminoacyl-tRNA synthetase multienzyme complex, also known as multisynthetase complex. Within the complex it catalyzes the attachment of both L-glutamate and L-proline to their cognate tRNAs in a two-step reaction where the amino acid is first activated by ATP to form a covalent intermediate with AMP. Subsequently, the activated amino acid is transferred to the acceptor end of the cognate tRNA to form L-glutamyl-tRNA(Glu) and …

**Summary**, from NCBI Gene [2058](https://www.ncbi.nlm.nih.gov/gene/2058):

> Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is a multifunctional aminoacyl-tRNA synthetase that catalyzes the aminoacylation of glutamic acid and proline tRNA species. Alternative splicing has been observed for this gene, but the full-length nature and biological validity of the variant have not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3418](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3418) · Entrez [2058](https://www.ncbi.nlm.nih.gov/gene/2058) · UniProt [P07814](https://www.uniprot.org/uniprotkb/P07814) · Ensembl [ENSG00000136628](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136628)

## Data

Gene col 5883: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5883); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5883, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5883]; `tensor/DDL_lfc|DDL_z.npy` [5883]; `embed/gene_vectors.npy` [5883]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5883 or target_col == 5883). Every well: [[EPRS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPRS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
