---
symbol: "HIF1A-AS3"
type: "gene"
col: 15128
ensembl_id: "ENSG00000258667"
name: "HIF1A antisense RNA 1"
location: "14q23.2"
module: 99
arm: "+"
pooled_cpm: 131.49
n_lines_expressing: 37
n_dd_up: 24
n_dd_down: 16
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# HIF1A-AS3

*HIF1A antisense RNA 1* — 14q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.40× (z +18.8, q 0e+00, up in 31 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.599× (z -11.1, q 1e-25, down in 28 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB3P1]] (+0.59, fdr 1e-05), [[HLA-V-1]] (+0.54, fdr 3e-05), [[PLOD2]] (+0.54, fdr 1e-05); moves opposite to [[RAD1]] (-0.46, fdr 4e-05), [[POMT2]] (-0.43, fdr 6e-05), [[INTS15]] (-0.42, fdr 1e-04).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C4orf47]] → it (grade C ⚠); 1 goes from it, the strongest it → [[LINC02940]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.40×** | +18.8 | 0e+00 | 31/35 (Panc 03.27, SW 900, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.76×** | +8.1 | 1e-13 | 22/36 (Hs 766T, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.69×** | +8.1 | 1e-13 | 24/35 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +7.4 | 2e-11 | 24/35 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.5 | 9e-09 | 21/35 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.24×** | +6.5 | 9e-09 | 17/26 (HOP62, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +6.2 | 5e-08 | 24/34 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +6.1 | 7e-08 | 25/35 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.06×** | +5.8 | 4e-07 | 26/35 (HT-29, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 4e-05 | 16/35 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.38×** | +4.8 | 1e-04 | 20/35 (NCI-H2030, A-427, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +4.5 | 3e-04 | 17/36 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +4.1 | 0.002 | 15/32 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.009 | 18/34 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.009 | 21/34 (NCI-H2030, A549, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.009 | 17/36 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.029 | 11/34 (A549, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15128.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -11.1 | 1e-25 | 28/36 (COLO 205, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.474×** | -11.0 | 1e-25 | 30/34 (COLO 205, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.617×** | -7.4 | 3e-11 | 23/35 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.638×** | -6.9 | 9e-10 | 21/35 (SW480, J82, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.686×** | -5.6 | 3e-06 | 19/30 (CFPAC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.694×** | -5.4 | 7e-06 | 21/35 (COLO 205, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.708×** | -5.3 | 1e-05 | 21/36 (NCI-H2030, CFPAC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.716×** | -5.1 | 2e-05 | 21/35 (NCI-H2030, LOX-IMVI, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.741×** | -4.6 | 3e-04 | 19/35 (HOP62, Panc 03.27, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.575×** | -4.4 | 6e-04 | 21/36 (J82, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.769×** | -4.0 | 0.003 | 15/35 (RKO, KATO III, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **0.780×** | -3.8 | 0.007 | 18/35 (BT-474, J82, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 0.837× | -3.6 | 0.013 | 15/35 (KATO III, HT-29, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **0.787×** | -3.5 | 0.018 | 17/34 (J82, SW 1271, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.805×** | -3.3 | 0.035 | 18/34 (KATO III, COLO 205, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.797×** | -3.2 | 0.046 | 12/34 (J82, SW480, …) | all doses, flat |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.870× | -3.0 | 0.082 | 11/36 (COLO 205, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 228 | 10 (4 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.59× (z +18.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.0) |
| [[Hs 766T (line)]] | wt | 173 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +35.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 9.48× (z +18.4) | — |
| [[J82 (line)]] | alt | 219 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -10.5) |
| [[PANC-1 (line)]] | alt | 87.5 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.42× (z +15.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.72× (z +15.5) | — |
| [[KATO III (line)]] | alt | 142 | 3 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.62× (z +12.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -12.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -10.8) |
| [[SW48 (line)]] | wt | 223 | 1 | 6 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.36× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -17.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.163× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 471 | 3 (1 ⚠) | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.88× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[HCT15 (line)]] | alt | 199 | 1 | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.60× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -21.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -10.0) |
| [[LoVo (line)]] | wt | 147 | 1 | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.94× (z +14.9) | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -26.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.340× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 286 | 1 | 5 (4 ⚠) | [[Auranofin (drug)]] 5 µM 4.00× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 392 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +17.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.40× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[SW 900 (line)]] | alt | 270 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.63× (z +23.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 14.1× (z +21.7) | — |
| [[SW480 (line)]] | alt | 144 | 3 (1 ⚠) | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.39× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -12.2) |
| [[COLO 205 (line)]] | alt | 212 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -23.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.156× (z -16.3) |
| [[HT-29 (line)]] | alt | 88.2 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.71× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -16.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.232× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 322 | 1 | 4 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.75× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -17.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 97.8 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.24× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -20.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.250× (z -12.7) |
| [[HOP62 (line)]] | alt | 112 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.0× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 1271 (line)]] | alt | 198 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 8.32× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0733× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 111 | 2 | 1 | [[Auranofin (drug)]] 5 µM 3.40× (z +10.0) | [[Harringtonine (drug)]] 5 µM 0.325× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 160 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.81× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[RKO (line)]] | wt | 219 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.2× (z +14.5) | — |
| [[A-427 (line)]] | wt | 33.8 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.37× (z +16.1) | — |
| [[A549 (line)]] | wt | 150 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 7.30× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -9.3) |
| [[BT-474 (line)]] | alt | 138 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 120 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.90× (z +12.0) | — |
| [[NCI-H2347 (line)]] | alt | 67.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.70× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 246 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 11.2× (z +22.0) | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 104 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.52× (z +12.9) | — |
| [[A498 (line)]] | wt | 49.4 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.52× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 62.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.33× (z +10.6) | — |
| [[A-172 (line)]] | wt | 19.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 27.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 30.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 23.6 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 19.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 23.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 23.0 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 28.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 37.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB3P1]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[HLA-V-1]] | +0.54 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[PLOD2]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[KCTD11]] | +0.52 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[SNAPC1]] | +0.50 | +0.52 / +0.40 | both halves | 5e-05 | ⚠ same locus (11.3 kb: neighbours can correlate without regulation) |
| [[SLC2A1-DT]] | +0.50 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[MMP24OS]] | +0.49 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[POT1-AS1]] | +0.49 | +0.35 / +0.54 | both halves | 1e-04 | same gene group |
| [[MFSD4B]] | +0.47 | +0.33 / +0.44 | both halves | 1e-04 |  |
| [[C11orf65]] | +0.46 | +0.46 / +0.33 | both halves | 1e-04 |  |
| [[GBE1]] | +0.46 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[FAM162A]] | +0.46 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[LINC02940]] | +0.46 | +0.35 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD1]] | -0.46 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[POMT2]] | -0.43 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[INTS15]] | -0.42 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[NHSL1]] | -0.42 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[UBP1]] | -0.41 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[MAP3K6]] | -0.41 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[NAPG]] | -0.41 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[PATZ1]] | -0.40 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[ABCC5]] | -0.40 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[SLF1]] | -0.39 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[ARHGEF19]] | -0.39 | -0.42 / -0.32 | both halves | 1e-04 |  |
| [[PXYLP1]] | -0.38 | -0.33 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C4orf47]] | C | C4orf47 activity raises HIF1A-AS3's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 2.46× lower at baseline in the lines without C4orf47 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02940]] | B | HIF1A-AS3 activity lowers LINC02940's level | lines that do not express HIF1A-AS3 (13) vs lines expressing it (37) | 1.94× higher at baseline in the lines without HIF1A-AS3 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, TNFRSF1B, CTSZ; maybe low, not absent |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.389). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.8, -16.2); signed map (-0.4, 13.7). **Vector** length 126, 34.9% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.4 | +18.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.0 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +4.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.8 | +4.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.4 | -11.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.6 | -7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.7 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | -1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | HIF1A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q23.2 — chr14:61,680,723-61,751,163 (-) |
| Ensembl biotype | lncRNA |
| Also known as | HIFAL, 5'aHIF-1A; previously HIF1A-AS3 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | prev_symbol |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43014) · Entrez [100750246](https://www.ncbi.nlm.nih.gov/gene/100750246) · Ensembl [ENSG00000258667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258667)

## Data

Gene col 15128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15128); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15128]; `tensor/DDL_lfc|DDL_z.npy` [15128]; `embed/gene_vectors.npy` [15128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15128 or target_col == 15128). Every well: [[HIF1A-AS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIF1A-AS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
