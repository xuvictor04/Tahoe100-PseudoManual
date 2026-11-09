---
symbol: "GABPB1-AS1"
type: "gene"
col: 14417
ensembl_id: "ENSG00000244879"
name: "GABPB1 antisense RNA 1"
location: "15q21.2"
module: 124
arm: "+"
pooled_cpm: 66.0
n_lines_expressing: 48
n_dd_up: 28
n_dd_down: 23
n_dd_up_clean: 20
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# GABPB1-AS1

*GABPB1 antisense RNA 1* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +17.3, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.465× (z -11.6, q 2e-28, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPM2A]] (+0.77, fdr 1e-05), [[ZNF337-AS1]] (+0.74, fdr 1e-05), [[ADCK1]] (+0.74, fdr 4e-05); moves opposite to [[GNAI2]] (-0.72, fdr 3e-04), [[RAB3A]] (-0.67, fdr 2e-04), [[YIF1B]] (-0.67, fdr 0.001, ⚠ one half only (not replicated)), [[ARL3]] (-0.65, fdr 1e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FTCDNL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14417.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +17.3 | 0e+00 | 41/47 (HOP62, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +9.0 | 5e-17 | 40/46 (HOP62, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +8.5 | 3e-15 | 33/46 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +8.1 | 1e-13 | 34/46 (HOP62, HS-578T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.58×** | +6.9 | 6e-10 | 38/46 (RPMI-7951, NCI-H1573, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +5.8 | 6e-07 | 28/43 (NCI-H1792, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +5.6 | 2e-06 | 29/46 (LoVo, H4, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.5 | 3e-06 | 22/41 (AsPC-1, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +4.6 | 2e-04 | 26/46 (COLO 205, KATO III, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.3 | 8e-04 | 25/48 (HOP62, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.001 | 23/46 (LS 180, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.001 | 23/46 (NCI-H1792, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.30×** | +4.0 | 0.003 | 21/46 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.004 | 19/47 (NCI-H460, COLO 205, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.20× | +3.9 | 0.004 | 11/46 (NCI-H1792, A498, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.006 | 25/46 (RPMI-7951, A498, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.013 | 17/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.023 | 13/46 (LS 180, J82, …) | inconsistent across doses |  |
| [[Meloxicam (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.023 | 15/46 (J82, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14417.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.465×** | -11.6 | 2e-28 | 35/46 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.483×** | -11.0 | 1e-25 | 38/46 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.486×** | -10.9 | 2e-25 | 40/46 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.329×** | -8.8 | 2e-16 | 37/47 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.564×** | -8.7 | 5e-16 | 36/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.349×** | -8.3 | 8e-15 | 33/46 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.688×** | -8.0 | 9e-14 | 29/46 (SW480, RKO, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.598×** | -7.5 | 5e-12 | 30/46 (LS 180, NCI-H460, …) | top dose only | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.617×** | -7.3 | 2e-11 | 33/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.683×** | -5.5 | 3e-06 | 28/46 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.698×** | -5.5 | 3e-06 | 29/46 (PANC-1, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.699×** | -5.4 | 4e-06 | 28/46 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.708×** | -5.2 | 7e-06 | 27/46 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.714×** | -5.1 | 1e-05 | 26/46 (PANC-1, SW480, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.534×** | -5.0 | 3e-05 | 30/45 (LoVo, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.757×** | -4.2 | 9e-04 | 24/46 (AN3 CA, SW1417, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.650×** | -3.4 | 0.019 | 17/47 (SW480, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 5 µM |  | **0.809×** | -3.2 | 0.037 | 11/46 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.673×** | -3.1 | 0.044 | 17/45 (Hs 766T, COLO 205, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.820×** | -2.9 | 0.097 | 11/46 (NCI-H460, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 102 | 0 | 14 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -18.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.294× (z -12.7) |
| [[SW480 (line)]] | alt | 156 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -16.4) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.225× (z -16.3) |
| [[LoVo (line)]] | wt | 113 | 2 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +12.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -15.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.331× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 167 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.354× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 43.2 | 1 | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.2) | [[Harringtonine (drug)]] 5 µM 0.183× (z -13.8) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.286× (z -10.5) |
| [[RKO (line)]] | wt | 63.1 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -15.9) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.212× (z -11.8) |
| [[HOP62 (line)]] | alt | 24.5 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.26× (z +18.2) | — |
| [[LS 180 (line)]] | wt | 74.3 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.156× (z -14.2) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.321× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -11.7) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.118× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 18.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 61.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +10.7) | [[Belinostat (drug)]] 5 µM 0.353× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 82.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +13.0) | [[Bortezomib (drug)]] 5 µM 0.124× (z -8.9) ⚠ toxic |
| [[SW1417 (line)]] | alt | 63.6 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -13.5) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.361× (z -8.5) |
| [[A-172 (line)]] | wt | 36.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +14.2) | — |
| [[A549 (line)]] | wt | 78.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.0) ⚠ cell-cycle shift, explains ~84% of this change |
| [[BT-474 (line)]] | alt | 91.2 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.276× (z -10.4) |
| [[C-33 A (line)]] | alt | 203 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -11.1) |
| [[HT-29 (line)]] | alt | 67.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +12.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.305× (z -10.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LOX-IMVI (line)]] | wt | 45.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +11.8) | [[Harringtonine (drug)]] 5 µM 0.313× (z -9.0) ⚠ cell-cycle shift, explains ~49% of this change |
| [[NCI-H1573 (line)]] | alt | 82.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.55× (z +9.4) ⚠ toxic; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -12.7) ⚠ cell-cycle shift, explains ~84% of this change |
| [[SNU-1 (line)]] | wt | 77.9 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.150× (z -10.6) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.224× (z -8.7) |
| [[SNU-423 (line)]] | alt | 24.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.20× (z +13.1) | — |
| [[SW 900 (line)]] | alt | 35.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.4) | — |
| [[A-427 (line)]] | wt | 49.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.333× (z -10.2) |
| [[A498 (line)]] | wt | 54.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -10.1) ⚠ cell-cycle shift, explains ~84% of this change |
| [[AN3 CA (line)]] | alt | 84.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -10.6) ⚠ cell-cycle shift, explains ~84% of this change |
| [[C32 (line)]] | wt | 36.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +11.1) | — |
| [[HCT15 (line)]] | alt | 57.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 47.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +13.7) | — |
| [[HS-578T (line)]] | alt | 22.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 64.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +9.3) | — |
| [[J82 (line)]] | alt | 30.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.2) | — |
| [[KATO III (line)]] | alt | 36.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +13.3) | — |
| [[Panc 03.27 (line)]] | alt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.09× (z +16.8) | — |
| [[RPMI-7951 (line)]] | alt | 149 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 10 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPM2A]] | +0.77 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[ZNF337-AS1]] | +0.74 | +0.71 / +0.49 | both halves | 1e-05 | same gene group |
| [[ADCK1]] | +0.74 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[DPH5-DT]] | +0.72 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[RXYLT1]] | +0.71 | +0.74 / +0.28 | both halves | 3e-04 |  |
| [[SLC16A1-AS1]] | +0.70 | +0.69 / +0.50 | both halves | 1e-05 | same gene group |
| [[PCBP1-AS1]] | +0.69 | +0.54 / +0.49 | both halves | 1e-05 | same gene group |
| [[P2RY11]] | +0.68 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[HEXIM2-AS1]] | +0.67 | +0.57 / +0.43 | both halves | 3e-05 | same gene group |
| [[MSANTD2]] | +0.67 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[RFX3-DT]] | +0.67 | +0.63 / +0.34 | both halves | 1e-04 |  |
| [[SPOPL-DT]] | +0.67 | +0.68 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI2]] | -0.72 | -0.70 / -0.26 | both halves | 3e-04 |  |
| [[RAB3A]] | -0.67 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[YIF1B]] | -0.67 | -0.61 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[ARL3]] | -0.65 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[ALAD]] | -0.62 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[FOXO6]] | -0.60 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[METTL26]] | -0.60 | -0.57 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[CEP131]] | -0.60 | -0.55 / -0.20 | both halves | 7e-04 |  |
| [[RRAS]] | -0.60 | -0.55 / -0.20 | ⚠ one half (not replicated) | 7e-04 |  |
| [[PCMT1]] | -0.60 | -0.54 / -0.18 | ⚠ one half (not replicated) | 0.001 |  |
| [[MAD2L2]] | -0.59 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[ARRB2]] | -0.59 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[GPATCH11]] | -0.59 | -0.38 / -0.28 | both halves | 3e-04 |  |
| [[PLPPR2]] | -0.58 | -0.51 / -0.20 | both halves | 7e-04 |  |
| [[PLA2G15]] | -0.58 | -0.52 / -0.23 | both halves | 5e-04 |  |
| [[DOK4]] | -0.58 | -0.54 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FTCDNL1]] | B | FTCDNL1 activity raises GABPB1-AS1's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.80× lower at baseline in the lines without FTCDNL1 | 0.010 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers GABPB1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01088]] | B | LINC01088 activity raises GABPB1-AS1's level | lines that do not express LINC01088 (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without LINC01088 | 0.074 | ⚠ within organs, on part of the lines; also absent: PPP4R4, GPR155, PKIG; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.842). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-2.2, 8.6); signed map (25.3, -28.6). **Vector** length 126, 41.2% of its response variance represented; |z| ≥ 3 in 1,295 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +17.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.1 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +5.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.2 | +6.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +2.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -8.9 | -10.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -8.4 | -11.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.3 | -11.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.7 | -5.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -2.7 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.7 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -5.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | GABPB1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q21.2 — chr15:50,354,944-50,372,202 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44157) · Entrez [100129387](https://www.ncbi.nlm.nih.gov/gene/100129387) · Ensembl [ENSG00000244879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244879)

## Data

Gene col 14417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14417); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14417]; `tensor/DDL_lfc|DDL_z.npy` [14417]; `embed/gene_vectors.npy` [14417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14417 or target_col == 14417). Every well: [[GABPB1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABPB1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
