---
symbol: "SLK"
type: "gene"
col: 797
ensembl_id: "ENSG00000065613"
name: "STE20 like kinase"
location: "10q24.33-q25.1"
module: 179
arm: "-"
pooled_cpm: 196.13
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# SLK

*STE20 like kinase* — 10q24.33-q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.90× (z +18.8, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.642× (z -19.0, q 0e+00, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP5]] (+0.58, fdr 1e-05), [[ROCK2]] (+0.56, fdr 1e-05), [[INPP1]] (+0.54, fdr 2e-05); moves opposite to [[KHDC4]] (-0.58, fdr 2e-05), [[MED26]] (-0.58, fdr 3e-05), [[UBOX5]] (-0.53, fdr 3e-05).
> It sits in the **-** arm of [[Module 179]] (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CYP3A5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.90×** | +18.8 | 0e+00 | 43/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +16.6 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.41×** | +14.8 | 0e+00 | 32/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +13.3 | 6e-38 | 38/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +11.9 | 1e-30 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +11.5 | 2e-28 | 42/47 (HepG2/C3A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +11.0 | 2e-26 | 37/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +10.9 | 1e-25 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +10.2 | 2e-22 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +9.4 | 3e-19 | 35/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +9.0 | 1e-17 | 29/44 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +8.8 | 7e-17 | 34/49 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +6.6 | 2e-09 | 29/48 (NCI-H1573, KATO III, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **1.22×** | +5.8 | 3e-07 | 24/47 (HT-29, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.18× | +5.1 | 1e-05 | 18/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.10× | +4.3 | 7e-04 | 0/48 | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +4.0 | 0.002 | 18/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.09× | +3.9 | 0.003 | 1/49 (CFPAC-1) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.07× | +3.0 | 0.061 | 5/49 (SHP-77, SW480, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.10× | +3.0 | 0.061 | 6/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.068 | 12/49 (A-172, HS-578T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 797.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -19.0 | 0e+00 | 37/49 (LoVo, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.735×** | -9.3 | 3e-18 | 35/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -9.1 | 2e-17 | 4/50 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.759×** | -8.4 | 8e-15 | 32/48 (AsPC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.789×** | -7.2 | 7e-11 | 31/48 (LoVo, LS 180, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **0.784×** | -6.3 | 2e-08 | 33/48 (HCT15, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.817×** | -5.9 | 3e-07 | 26/48 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -5.8 | 4e-07 | 16/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.774×** | -5.5 | 2e-06 | 29/48 (AsPC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.882× | -5.4 | 4e-06 | 13/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.821×** | -5.1 | 1e-05 | 27/49 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.853× | -4.8 | 7e-05 | 17/49 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 0.906× | -4.3 | 9e-04 | 11/48 (C32, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | 0.872× | -4.0 | 0.003 | 21/47 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.867× | -3.7 | 0.008 | 15/48 (NCI-H23, A-427, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.868× | -3.7 | 0.008 | 16/48 (SNU-1, SW1417, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.917× | -3.6 | 0.009 | 9/49 (LS 180, LoVo, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.808×** | -3.4 | 0.022 | 15/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | 0.890× | -3.3 | 0.030 | 7/47 (hTERT-HPNE, A-172, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 0.897× | -3.2 | 0.038 | 11/49 (LoVo, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Bergenin (drug)]] 0.5 µM |  | 0.885× | -3.2 | 0.038 | 9/48 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.932× | -3.0 | 0.064 | 1/48 (SW 1271) | top dose only |  |
| [[Roxadustat (drug)]] 0.05 µM |  | 0.899× | -3.0 | 0.064 | 6/47 (H4, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 261 | 10 (5 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -14.1) |
| [[PANC-1 (line)]] | alt | 191 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +25.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.89× (z +20.2) | — |
| [[SW480 (line)]] | alt | 146 | 5 (2 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.641× (z -10.7) |
| [[LoVo (line)]] | wt | 354 | 1 (1 ⚠) | 7 (5 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.82× (z +8.9) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -27.0) |
| [[HepG2_C3A (line)]] | wt | 180 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +14.2) | — |
| [[KATO III (line)]] | alt | 277 | 2 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -22.7) |
| [[RKO (line)]] | wt | 171 | 6 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 2.77× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -8.6) |
| [[A-172 (line)]] | wt | 171 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +17.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.14× (z +12.5) | — |
| [[A498 (line)]] | wt | 106 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +20.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.71× (z +14.6) | — |
| [[A549 (line)]] | wt | 154 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +20.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.36× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 444 | 1 | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -16.2) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 268 | 3 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -14.0) |
| [[H4 (line)]] | wt | 98.8 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 173 | 3 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +13.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.90× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -11.5) |
| [[LS 180 (line)]] | wt | 295 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -17.3) |
| [[MIA PaCa-2 (line)]] | alt | 427 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -24.8) |
| [[SNU-423 (line)]] | alt | 193 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +17.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.30× (z +13.1) | — |
| [[SW 900 (line)]] | alt | 168 | 4 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 2.66× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -13.4) |
| [[C32 (line)]] | wt | 182 | 0 | 4 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -12.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 126 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +17.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.45× (z +14.0) | — |
| [[Hs 766T (line)]] | wt | 484 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -21.1) |
| [[J82 (line)]] | alt | 89.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.31× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 140 | 3 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 2.81× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 118 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.56× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 163 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +14.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +13.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.576× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~62% of this change |
| [[HOP62 (line)]] | alt | 88.3 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 2.34× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 107 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.82× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 178 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +12.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.63× (z +8.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.555× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~62% of this change |
| [[RPMI-7951 (line)]] | alt | 147 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.49× (z +11.6) | — |
| [[A-427 (line)]] | wt | 128 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.08× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 254 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -14.4) |
| [[COLO 205 (line)]] | alt | 276 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -15.5) |
| [[HCT15 (line)]] | alt | 177 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 162 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.666× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 126 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.3) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[Panc 03.27 (line)]] | alt | 244 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.72× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -15.1) |
| [[SHP-77 (line)]] | alt | 111 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 97.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.64× (z +10.6) | — |
| [[SNU-1 (line)]] | wt | 153 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.19× (z +8.7) | — |
| [[SW48 (line)]] | wt | 228 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -9.6) |
| [[AN3 CA (line)]] | alt | 230 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.58× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 190 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -15.0) |
| [[hTERT-HPNE (line)]] | wt | 140 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +8.7) | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 1 | — | [[Silodosin (drug)]] 0.05 µM 0.0797× (z -10.4) |
| [[C-33 A (line)]] | alt | 186 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP5]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 | pathway: RHOA GTPase cycle |
| [[ROCK2]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 | pathway: RHOA GTPase cycle; STRING 514 |
| [[INPP1]] | +0.54 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[SKIL]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[NAB1]] | +0.51 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CYP3A5]] | +0.50 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[KIDINS220]] | +0.49 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[KTN1]] | +0.49 | +0.45 / +0.46 | both halves | 3e-05 | pathway: RHOA GTPase cycle |
| [[KLF3]] | +0.49 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[EZR]] | +0.49 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SMC3]] | +0.48 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[AHNAK2]] | +0.48 | +0.40 / +0.52 | both halves | 5e-05 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KHDC4]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[MED26]] | -0.58 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[UBOX5]] | -0.53 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[DERL1]] | -0.53 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[EEF1AKMT4]] | -0.53 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[SNHG21]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[RNF121]] | -0.52 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[QPCTL]] | -0.52 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[ISOC2]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[DPM1]] | -0.50 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[MGAT1]] | -0.50 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[THOC3]] | -0.49 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP3A5]] | B | CYP3A5 activity raises SLK's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 1.44× lower at baseline in the lines without CYP3A5 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[DSC2]] | B | DSC2 activity raises SLK's level | lines that do not express DSC2 (22) vs lines expressing it (28) | 1.31× lower at baseline in the lines without DSC2 | 0.074 | ⚠ within organs, on part of the lines; also absent: FAM110C, SPINT1-AS1, PRR15-DT |
| [[C2orf27A]] | B | C2orf27A activity lowers SLK's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 1.92× higher at baseline in the lines without C2orf27A | 0.085 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent |
| [[MAP9]] | B | MAP9 activity lowers SLK's level | lines that do not express MAP9 (17) vs lines expressing it (33) | 1.51× higher at baseline in the lines without MAP9 | 0.089 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, RNF150, BVES; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **-** arm (projection on the module's main direction -0.655). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (5.2, -20.4); signed map (10.9, -9.5). **Vector** length 130, 43.6% of its response variance represented; |z| ≥ 3 in 1,446 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +12.1 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +12.0 | +8.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.7 | +18.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.1 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.6 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.9 | +9.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.1 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +6.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.1 | +4.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.4 | +2.1 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -0.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -4.8 | -9.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -0.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.8 | -3.7 |
|  | [[Decitabine (drug)]] 0.05 µM |  | -2.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | STE20 like kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.33-q25.1 — chr10:103,967,140-104,029,233 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STK2, se20-9, KIAA0204 |
| Gene groups (HGNC) | SLK/STK10 kinase family |
| Reactome | 6 pathways, smallest: RHOB GTPase cycle; RHOC GTPase cycle; RHOA GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2G2](https://www.uniprot.org/uniprotkb/Q9H2G2) (STE20-like serine/threonine-protein kinase):

> Mediates apoptosis and actin stress fiber dissolution.

**Summary**, from NCBI Gene [9748](https://www.ncbi.nlm.nih.gov/gene/9748):

> Enables protein homodimerization activity and protein serine/threonine kinase activity. Involved in several processes, including cytoplasmic microtubule organization; protein autophosphorylation; and regulation of focal adhesion assembly. Located in perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11088) · Entrez [9748](https://www.ncbi.nlm.nih.gov/gene/9748) · UniProt [Q9H2G2](https://www.uniprot.org/uniprotkb/Q9H2G2) · Ensembl [ENSG00000065613](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065613)

## Data

Gene col 797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 797); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 797]; `tensor/DDL_lfc|DDL_z.npy` [797]; `embed/gene_vectors.npy` [797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 797 or target_col == 797). Every well: [[SLK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
