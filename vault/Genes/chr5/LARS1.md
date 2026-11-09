---
symbol: "LARS1"
type: "gene"
col: 5468
ensembl_id: "ENSG00000133706"
name: "leucyl-tRNA synthetase 1"
location: "5q32"
module: 1
arm: "+"
pooled_cpm: 177.65
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 13
n_dd_up_clean: 17
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# LARS1

*leucyl-tRNA synthetase 1* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.43× (z +21.2, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 1.40× (z +8.0, q 1e-13, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.718× (z -11.3, q 1e-26, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NARS1]] (+0.73, fdr 7e-06), [[YARS1]] (+0.70, fdr 7e-06), [[TARS1]] (+0.70, fdr 7e-06); moves opposite to [[UBL5]] (-0.59, fdr 1e-05), [[NDUFA2]] (-0.59, fdr 2e-05), [[GABARAPL2]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GABRE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5468.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +21.2 | 0e+00 | 49/49 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +18.1 | 0e+00 | 42/44 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +14.3 | 3e-44 | 35/45 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +11.5 | 3e-28 | 39/48 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.40×** | +8.0 | 1e-13 | 35/48 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +7.6 | 3e-12 | 30/48 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.23×** | +7.0 | 2e-10 | 27/48 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +6.3 | 2e-08 | 38/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.59×** | +5.8 | 5e-07 | 35/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +5.5 | 2e-06 | 29/48 (NCI-H1573, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +5.4 | 3e-06 | 19/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **1.25×** | +5.2 | 1e-05 | 27/47 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +5.1 | 1e-05 | 27/48 (Panc 03.27, A-172, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.50×** | +5.1 | 2e-05 | 31/48 (LOX-IMVI, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.9 | 4e-05 | 17/49 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.25×** | +4.9 | 4e-05 | 32/48 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +4.7 | 7e-05 | 26/48 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.22×** | +4.7 | 7e-05 | 26/47 (NCI-H2030, HEC-1-A, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.22×** | +4.7 | 8e-05 | 26/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 3e-04 | 24/48 (SW480, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5468.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -11.3 | 1e-26 | 34/49 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.635×** | -10.9 | 2e-25 | 39/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.643×** | -10.6 | 4e-24 | 37/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.691×** | -8.9 | 9e-17 | 38/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.711×** | -8.2 | 2e-14 | 34/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.748×** | -7.0 | 2e-10 | 27/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.766×** | -6.4 | 9e-09 | 30/48 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.766×** | -6.4 | 1e-08 | 33/48 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.857× | -5.3 | 9e-06 | 23/48 (J82, LS 180, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.808×** | -5.2 | 1e-05 | 24/48 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.748×** | -5.0 | 3e-05 | 29/48 (SNU-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.829×** | -4.5 | 3e-04 | 22/48 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.859× | -3.7 | 0.009 | 18/47 (LOX-IMVI, CFPAC-1, …) | two highest doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | 0.857× | -3.5 | 0.021 | 16/48 (HCT15, CHP-212, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.773×** | -3.3 | 0.042 | 21/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.910× | -3.2 | 0.042 | 8/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.780×** | -3.1 | 0.057 | 14/48 (RKO, COLO 205, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 349 | 0 | 10 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.382× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 160 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 252 | 0 | 9 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -16.5) |
| [[SW480 (line)]] | alt | 213 | 3 (3 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +14.1) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -23.6) |
| [[LS 180 (line)]] | wt | 142 | 3 (3 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +15.3) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.479× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 195 | 3 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.83× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.558× (z -9.1) |
| [[SNU-1 (line)]] | wt | 262 | 1 | 7 (2 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.90× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.346× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.486× (z -11.6) |
| [[HT-29 (line)]] | alt | 178 | 4 (4 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +14.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.364× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.488× (z -11.2) |
| [[J82 (line)]] | alt | 175 | 3 (3 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +12.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.420× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.526× (z -9.2) |
| [[LoVo (line)]] | wt | 178 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.43× (z +13.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.387× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.440× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 111 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.20× (z +18.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.38× (z +15.4) | — |
| [[RKO (line)]] | wt | 299 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -20.5) |
| [[KATO III (line)]] | alt | 192 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +11.9) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.450× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 287 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.31× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -18.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.647× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 105 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.79× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 125 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +10.7) | [[Belinostat (drug)]] 5 µM 0.515× (z -9.4) |
| [[A498 (line)]] | wt | 170 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +13.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 124 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.25× (z +12.2) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.330× (z -12.0) |
| [[HOP62 (line)]] | alt | 80.9 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +17.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.520× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 184 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +16.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -12.4) |
| [[SW48 (line)]] | wt | 203 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.289× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -11.3) |
| [[BT-474 (line)]] | alt | 136 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -13.7) |
| [[C-33 A (line)]] | alt | 258 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +10.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.490× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 96.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.56× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 181 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 117 | 4 (4 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.60× (z +12.7) ⚠ unreliable plate only | — |
| [[SHP-77 (line)]] | alt | 245 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.91× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.661× (z -9.0) |
| [[SNU-423 (line)]] | alt | 111 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +17.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 93.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +13.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 181 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +14.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 264 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.86× (z +10.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -11.2) |
| [[A549 (line)]] | wt | 125 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +15.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 82.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +15.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 92.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +13.9) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 92.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.37× (z +16.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 206 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +13.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 174 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +16.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 145 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 254 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +11.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -9.3) |
| [[AN3 CA (line)]] | alt | 248 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -8.9) |
| [[CHP-212 (line)]] | wt | 181 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.481× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 205 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -8.9) |
| [[HCT15 (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +9.1) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 96.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H596 (line)]] | alt | 156 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.114× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 160 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NARS1]] | +0.73 | +0.78 / +0.66 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 954 |
| [[YARS1]] | +0.70 | +0.64 / +0.72 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 980 |
| [[TARS1]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 980 |
| [[IMPACT]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[GTF2H3]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ATIC]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 | STRING 471 |
| [[GUF1]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 | STRING 439 |
| [[CFAP97]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[DNAJA3]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[MTIF2]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 | STRING 550 |
| [[SRP72]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBL5]] | -0.59 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[NDUFA2]] | -0.59 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[GABARAPL2]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SDF2]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[COX7A2]] ⚠ | -0.54 | -0.48 / -0.50 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RBM38]] | -0.54 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[TMEM50A]] | -0.54 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[NDUFB11]] ⚠ | -0.53 | -0.57 / -0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[C1QL1]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[FGFR3]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABRE]] | B | GABRE activity lowers LARS1's level | lines that do not express GABRE (20) vs lines expressing it (30) | 1.44× higher at baseline in the lines without GABRE | 0.026 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3 |
| [[ANK2]] | B | ANK2 activity raises LARS1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.38× lower at baseline in the lines without ANK2 | 0.052 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[PSAT1]] | B | PSAT1 activity raises LARS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without PSAT1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[ABHD17C]] | B | ABHD17C activity lowers LARS1's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 1.32× higher at baseline in the lines without ABHD17C | 0.067 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[C1QL1]] | B | C1QL1 activity raises LARS1's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.26× lower at baseline in the lines without C1QL1 | 0.084 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.623). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-31.0, -16.1); signed map (-0.7, -37.7). **Vector** length 155, 55.5% of its response variance represented; |z| ≥ 3 in 1,663 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.9 | +11.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +7.5 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.5 | +7.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.5 | +8.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.6 | +5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +6.4 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +6.2 | +5.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +5.7 | +5.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.7 | -10.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -7.5 | -8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -11.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.8 | -10.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.6 | -8.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.7 | -5.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -4.2 | -2.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | -4.2 | -3.5 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -4.0 | -2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | leucyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:146,110,566-146,182,696 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC192, FLJ10595, FLJ21788, LEUS, RNTLS; previously LARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Reactome | 7 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Transcriptional and post-translational regulation of MITF-M expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2J5](https://www.uniprot.org/uniprotkb/Q9P2J5) (Leucine--tRNA ligase, cytoplasmic):

> Aminoacyl-tRNA synthetase that catalyzes the specific attachment of leucine to its cognate tRNA (tRNA(Leu)). It performs tRNA aminoacylation in a two-step reaction: Leu is initially activated by ATP to form a leucyl-adenylate (Leu-AMP) intermediate; then the leucyl moiety is transferred to the acceptor 3' end of the tRNA to yield leucyl-tRNA. To improve the fidelity of catalytic reactions, it is also able to hydrolyze misactivated aminoacyl-adenylate intermediates (pre-transfer editing) and …

**Summary**, from NCBI Gene [51520](https://www.ncbi.nlm.nih.gov/gene/51520):

> This gene encodes a cytosolic leucine-tRNA synthetase, a member of the class I aminoacyl-tRNA synthetase family. The encoded enzyme catalyzes the ATP-dependent ligation of L-leucine to tRNA(Leu). It is found in the cytoplasm as part of a multisynthetase complex and interacts with the arginine tRNA synthetase through its C-terminal domain. A mutation in this gene was found in affected individuals with infantile liver failure syndrome 1. Alternatively spliced transcript variants of this gene have …

**Accessions** — [HGNC:6512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6512) · Entrez [51520](https://www.ncbi.nlm.nih.gov/gene/51520) · UniProt [Q9P2J5](https://www.uniprot.org/uniprotkb/Q9P2J5) · Ensembl [ENSG00000133706](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133706)

## Data

Gene col 5468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5468); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5468]; `tensor/DDL_lfc|DDL_z.npy` [5468]; `embed/gene_vectors.npy` [5468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5468 or target_col == 5468). Every well: [[LARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
