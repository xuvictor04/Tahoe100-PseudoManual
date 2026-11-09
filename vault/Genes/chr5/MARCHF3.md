---
symbol: "MARCHF3"
type: "gene"
col: 10446
ensembl_id: "ENSG00000173926"
name: "membrane associated ring-CH-type finger 3"
location: "5q23.2"
module: 81
arm: "+"
pooled_cpm: 77.14
n_lines_expressing: 45
n_dd_up: 19
n_dd_down: 28
n_dd_up_clean: 15
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 23
direction_downstream: 13
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# MARCHF3

*membrane associated ring-CH-type finger 3* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.60× (z +16.4, q 0e+00, up in 37 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.499× (z -11.5, q 7e-28, down in 26 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.572× (z -9.6, q 1e-19, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STC1]] (+0.65, fdr 7e-06), [[CALM1]] (+0.65, fdr 1e-05), [[TIMP1]] (+0.63, fdr 8e-06); moves opposite to [[TMEM268]] (-0.56, fdr 3e-05), [[XPO1]] (-0.54, fdr 3e-05), [[PAIP1]] (-0.54, fdr 1e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[IL33]] → it (grade B ⚠); 13 go from it, the strongest it → [[ELL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10446.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.60×** | +16.4 | 0e+00 | 37/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.39×** | +15.0 | 0e+00 | 36/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.23×** | +13.8 | 5e-41 | 35/43 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +11.6 | 1e-28 | 32/43 (PANC-1, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.91×** | +11.1 | 1e-26 | 37/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +8.9 | 6e-17 | 31/42 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +7.1 | 1e-10 | 24/44 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +6.7 | 1e-09 | 22/42 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +5.8 | 3e-07 | 20/42 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.75×** | +5.0 | 3e-05 | 19/43 (PANC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.35×** | +5.0 | 3e-05 | 18/42 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +4.6 | 2e-04 | 18/44 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.64×** | +4.5 | 4e-04 | 20/43 (HOP62, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.18× | +4.1 | 0.001 | 12/43 (HS-578T, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.26×** | +4.0 | 0.002 | 16/43 (RKO, hTERT-HPNE, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.003 | 9/42 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.008 | 19/42 (RPMI-7951, SW 900, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10446.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.499×** | -11.5 | 7e-28 | 26/33 (HepG2/C3A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.571×** | -9.7 | 1e-19 | 28/41 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.572×** | -9.6 | 1e-19 | 31/43 (J82, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.560×** | -9.2 | 4e-18 | 28/36 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.614×** | -8.4 | 5e-15 | 24/42 (HOP62, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.622×** | -7.9 | 4e-13 | 29/42 (NCI-H1792, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.652×** | -7.4 | 1e-11 | 30/43 (LoVo, AsPC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.508×** | -6.1 | 8e-08 | 25/42 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.710×** | -5.5 | 3e-06 | 21/43 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.810×** | -5.1 | 2e-05 | 21/43 (HOP62, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.745×** | -5.1 | 2e-05 | 26/43 (HOP62, HS-578T, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.753×** | -4.9 | 5e-05 | 24/42 (SW48, RPMI-7951, …) | top dose only | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.819×** | -4.9 | 5e-05 | 23/43 (AsPC-1, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.761×** | -4.7 | 1e-04 | 24/43 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.604×** | -4.5 | 2e-04 | 14/31 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.765×** | -4.4 | 3e-04 | 20/43 (A549, CHP-212, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.768×** | -4.4 | 4e-04 | 19/42 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.782×** | -4.2 | 7e-04 | 20/43 (J82, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.783×** | -4.2 | 7e-04 | 22/43 (A549, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.648×** | -3.9 | 0.003 | 18/42 (AsPC-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.649×** | -3.9 | 0.003 | 18/42 (AsPC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.799×** | -3.7 | 0.005 | 18/42 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 186 | 0 | 17 (12 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.186× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 157 | 0 | 15 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -14.7) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.248× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 70.7 | 1 (1 ⚠) | 13 (7 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.287× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.315× (z -10.1) |
| [[SW480 (line)]] | alt | 33.2 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +20.6) | — |
| [[A549 (line)]] | wt | 112 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -17.4) |
| [[HS-578T (line)]] | alt | 143 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.260× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 285 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.341× (z -15.1) |
| [[A498 (line)]] | wt | 70.2 | 2 (1 ⚠) | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +8.9) | [[Triamcinolone (drug)]] 5 µM 0.379× (z -12.2) |
| [[J82 (line)]] | alt | 181 | 1 | 6 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.79× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.239× (z -15.4) |
| [[hTERT-HPNE (line)]] | wt | 166 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.283× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 50.7 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.32× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -8.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 29.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +16.2) | — |
| [[C32 (line)]] | wt | 31.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +12.6) | — |
| [[CFPAC-1 (line)]] | alt | 30.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +18.5) | — |
| [[SNU-423 (line)]] | alt | 162 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -12.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 43.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.240× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 44.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +13.7) | — |
| [[RPMI-7951 (line)]] | alt | 89.2 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.243× (z -11.7) ⚠ toxic |
| [[BT-474 (line)]] | alt | 27.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +8.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.101× (z -11.2) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 139 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0271× (z -25.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 134 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.182× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 74.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.44× (z +9.8) | — |
| [[RKO (line)]] | wt | 28.5 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.58× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +9.1) | — |
| [[H4 (line)]] | wt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -10.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 25.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 58.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.261× (z -8.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.255× (z -8.9) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 107 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.299× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H596 (line)]] | alt | 73.7 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.117× (z -14.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SHP-77 (line)]] | alt | 80.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -11.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 24.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +10.0) ⚠ cell-cycle shift, explains ~97% of this change | — |
| [[SW 1271 (line)]] | alt | 64.2 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0639× (z -8.7) |
| [[SW 900 (line)]] | alt | 70.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.286× (z -9.0) ⚠ toxic |
| [[SW48 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0533× (z -13.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STC1]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CALM1]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[TIMP1]] | +0.63 | +0.57 / +0.60 | both halves | 8e-06 |  |
| [[LRRC8C]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ABTB3]] | +0.62 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[AADACP1]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[MTSS1]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[IL1B]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[NLRP3]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[GFPT2]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM268]] | -0.56 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[XPO1]] | -0.54 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[PAIP1]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[RAD23B]] | -0.52 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[ZRANB2-DT]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[GTF2I]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[NAXD]] | -0.50 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[FBXO7]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[USP24]] | -0.50 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[COMT]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[CC2D2A]] | -0.48 | -0.41 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL33]] | B | IL33 activity weakens MARCHF3's drug response | lines that do not express IL33 (30) vs lines expressing it (14) | the lines without IL33 respond 1.28× as strongly (z diff -0.85); strongest at Panobinostat 5 µM: 2.86x vs 1.62x (z diff -3.6) | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411; target measured in part of the lines; artifact flags |
| [[IL33]] | B | IL33 activity raises MARCHF3's level | lines that do not express IL33 (35) vs lines expressing it (15) | 1.91× lower at baseline in the lines without IL33 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411 |
| [[IL1B]] | B | IL1B activity raises MARCHF3's level | lines that do not express IL1B (30) vs lines expressing it (20) | 2.50× lower at baseline in the lines without IL1B | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[SPOCK1]] | B | SPOCK1 activity raises MARCHF3's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 2.00× lower at baseline in the lines without SPOCK1 | 0.019 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[IL1B]] | B | IL1B activity weakens MARCHF3's drug response | lines that do not express IL1B (25) vs lines expressing it (19) | the lines without IL1B respond 0.90× as strongly (z diff +0.06); strongest at Panobinostat 5 µM: 3.02x vs 1.75x (z diff -2.5) | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA; target measured in part of the lines; both ways; artifact flags |
| [[NLRP3]] | B | NLRP3 activity raises MARCHF3's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 2.05× lower at baseline in the lines without NLRP3 | 0.025 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME |
| [[STC1]] | B | STC1 activity raises MARCHF3's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.90× lower at baseline in the lines without STC1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[F3]] | B | F3 activity raises MARCHF3's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.83× lower at baseline in the lines without F3 | 0.043 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[AADACP1]] | B | AADACP1 activity raises MARCHF3's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 1.77× lower at baseline in the lines without AADACP1 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1 |
| [[RGS2]] | B | RGS2 activity raises MARCHF3's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 1.63× lower at baseline in the lines without RGS2 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[TNS1]] | B | TNS1 activity raises MARCHF3's level | lines that do not express TNS1 (23) vs lines expressing it (27) | 1.85× lower at baseline in the lines without TNS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: C5orf46, LINC02970, ENSG00000223786 |
| [[TRIB1]] | B | TRIB1 activity raises MARCHF3's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.86× lower at baseline in the lines without TRIB1 | 0.048 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELL2]] | B | MARCHF3 activity raises ELL2's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 4.82× lower at baseline in the lines without MARCHF3 | 0.004 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[XPO1]] | B | MARCHF3 activity lowers XPO1's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 1.66× higher at baseline in the lines without MARCHF3 | 0.006 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[MCL1]] | B | MARCHF3 activity raises MCL1's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 1.79× lower at baseline in the lines without MARCHF3 | 0.016 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[EPAS1]] | B | MARCHF3 activity raises EPAS1's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 4.45× lower at baseline in the lines without MARCHF3 | 0.020 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[ST3GAL1]] | B | MARCHF3 activity raises ST3GAL1's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 4.46× lower at baseline in the lines without MARCHF3 | 0.036 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[CIB1]] | B | MARCHF3 activity raises CIB1's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 2.16× lower at baseline in the lines without MARCHF3 | 0.041 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[ITGA2]] | B | MARCHF3 activity raises ITGA2's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 4.17× lower at baseline in the lines without MARCHF3 | 0.048 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[SLC46A3]] | B | MARCHF3 activity raises SLC46A3's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 2.43× lower at baseline in the lines without MARCHF3 | 0.061 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[EFNA5]] | B | MARCHF3 activity raises EFNA5's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 2.76× lower at baseline in the lines without MARCHF3 | 0.064 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[STC1]] | B | MARCHF3 activity raises STC1's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 5.56× lower at baseline in the lines without MARCHF3 | 0.073 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[ANTXR2]] | B | MARCHF3 activity raises ANTXR2's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 3.26× lower at baseline in the lines without MARCHF3 | 0.085 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |
| [[ENTPD7]] | B | MARCHF3 activity raises ENTPD7's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 2.03× lower at baseline in the lines without MARCHF3 | 0.089 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.0, 3.0); signed map (2.8, 49.2). **Vector** length 133, 41.0% of its response variance represented; |z| ≥ 3 in 1,736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +7.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.9 | +4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | +11.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +16.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.4 | +1.6 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.6 | +2.2 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | +2.5 | +1.3 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -9.3 | -9.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.1 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.3 | -5.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.6 | -3.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -5.4 | -1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.2 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.0 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | membrane associated ring-CH-type finger 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.2 — chr5:126,867,714-127,030,558 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC48332, MARCH-III, RNF173; previously MARCH3 |
| Gene groups (HGNC) | Ring finger proteins; Membrane associated ring-CH-type fingers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UD3](https://www.uniprot.org/uniprotkb/Q86UD3) (E3 ubiquitin-protein ligase MARCHF3):

> E3 ubiquitin-protein ligase which may be involved in endosomal trafficking. E3 ubiquitin ligases accept ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfer the ubiquitin to targeted substrates.

**Summary**, from NCBI Gene [115123](https://www.ncbi.nlm.nih.gov/gene/115123):

> This gene encodes a member of the membrane-associated RING-CH (MARCH) family. The encoded protein is an E3 ubiquitin-protein ligase that may be involved in regulation of the endosomal transport pathway. [provided by RefSeq, Mar 2013]

**Accessions** — [HGNC:28728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28728) · Entrez [115123](https://www.ncbi.nlm.nih.gov/gene/115123) · UniProt [Q86UD3](https://www.uniprot.org/uniprotkb/Q86UD3) · Ensembl [ENSG00000173926](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173926)

## Data

Gene col 10446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10446); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10446]; `tensor/DDL_lfc|DDL_z.npy` [10446]; `embed/gene_vectors.npy` [10446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10446 or target_col == 10446). Every well: [[MARCHF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARCHF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
