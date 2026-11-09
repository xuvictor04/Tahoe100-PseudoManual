---
symbol: "CCNL1"
type: "gene"
col: 8747
ensembl_id: "ENSG00000163660"
name: "cyclin L1"
location: "3q25.31"
module: 14
arm: "+"
pooled_cpm: 277.63
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CCNL1

*cyclin L1* — 3q25.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.05× (z +27.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.408× (z -12.2, q 2e-31, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.685× (z -5.3, q 2e-05, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRF1]] (+0.69, fdr 7e-06), [[NFKB1]] (+0.61, fdr 7e-06), [[NAMPT]] (+0.59, fdr 2e-05); moves opposite to [[EXOC2]] (-0.54, fdr 1e-05), [[PSMF1]] (-0.52, fdr 3e-05), [[TRIP4]] (-0.50, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RHOV]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8747.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.05×** | +27.9 | 0e+00 | 48/48 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.15×** | +16.2 | 0e+00 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **8.22×** | +15.5 | 0e+00 | 49/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +13.6 | 4e-40 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.44×** | +12.6 | 3e-34 | 44/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **5.42×** | +12.5 | 1e-33 | 47/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.44×** | +12.1 | 1e-31 | 43/48 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.29×** | +11.7 | 1e-29 | 45/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.09×** | +10.4 | 1e-23 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.9 | 1e-13 | 35/49 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +7.0 | 1e-10 | 41/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.46×** | +5.3 | 6e-06 | 35/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.2 | 0.001 | 29/38 (SK-MEL-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.010 | 26/50 (RKO, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.015 | 26/48 (SK-MEL-2, A-427, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.059 | 21/48 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Hexylresorcinol (drug)]] 5 µM |  | 1.16× | +3.0 | 0.076 | 9/49 (KATO III, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8747.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.408×** | -12.2 | 2e-31 | 41/44 (NCI-H23, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.585×** | -7.6 | 9e-12 | 41/49 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.685×** | -5.3 | 2e-05 | 38/48 (NCI-H23, KATO III, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -4.6 | 6e-04 | 37/48 (NCI-H23, Panc 03.27, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.807×** | -4.3 | 0.002 | 31/49 (HT-29, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.770×** | -3.7 | 0.021 | 29/48 (NCI-H23, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.847× | -3.3 | 0.069 | 23/49 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -3.1 | 0.15 | 15/48 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 0.807× | -3.0 | 0.15 | 23/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8747. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 163 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +26.5) | — |
| [[LoVo (line)]] | wt | 245 | 10 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +31.0) | [[Dinaciclib (drug)]] 5 µM 0.480× (z -11.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 209 | 10 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -9.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 191 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +28.9) | — |
| [[J82 (line)]] | alt | 396 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +24.4) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -10.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 285 | 9 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +27.4) | [[Ponatinib (drug)]] 5 µM 0.487× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 227 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 432 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 428 | 5 (1 ⚠) | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.66× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.148× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.408× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 315 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +32.8) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -8.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 225 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +24.3) | — |
| [[PANC-1 (line)]] | alt | 235 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +26.7) | — |
| [[RKO (line)]] | wt | 232 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 326 | 6 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.485× (z -8.6) |
| [[SW480 (line)]] | alt | 232 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 135 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.18× (z +30.1) | — |
| [[A-427 (line)]] | wt | 375 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 338 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +23.9) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -10.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 525 | 5 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.483× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 341 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 261 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -9.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 394 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -13.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 239 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +24.0) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 238 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +22.5) | — |
| [[HT-29 (line)]] | alt | 310 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -12.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 225 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +27.7) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -9.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 248 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -12.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 326 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +16.7) | — |
| [[hTERT-HPNE (line)]] | wt | 197 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.19× (z +25.6) | — |
| [[NCI-H1792 (line)]] | alt | 205 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -11.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 305 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -10.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 243 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +14.8) | — |
| [[CFPAC-1 (line)]] | alt | 439 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 423 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -16.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 218 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.8) | — |
| [[Hs 766T (line)]] | wt | 185 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +21.6) | — |
| [[A498 (line)]] | wt | 228 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +21.0) | — |
| [[C-33 A (line)]] | alt | 167 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 319 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -10.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 258 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +19.8) | — |
| [[COLO 205 (line)]] | alt | 455 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +12.7) | — |
| [[HCT15 (line)]] | alt | 210 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 219 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +14.7) | — |
| [[CHP-212 (line)]] | wt | 244 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 189 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.28× (z +9.0) | — |
| [[SW 1088 (line)]] | alt | 173 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +12.3) | — |
| [[SW 1271 (line)]] | alt | 235 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +12.4) | — |
| [[NCI-H2122 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8747), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRF1]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NFKB1]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NAMPT]] | +0.59 | +0.47 / +0.65 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[YBX3]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[REL]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[WTAP]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[CTNNB1]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RBM39]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[EFNA1]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[BCL3]] | +0.55 | +0.44 / +0.60 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SOCS3-DT]] | +0.54 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[NFKBIA]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC2]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[PSMF1]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[TRIP4]] | -0.50 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[GFM2]] | -0.50 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[LIMK1]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[CSNK2A2]] | -0.49 | -0.46 / -0.40 | both halves | 4e-05 | STRING 476 |
| [[LSP1P4]] | -0.49 | -0.37 / -0.52 | both halves | 7e-05 |  |
| [[ZDHHC18]] | -0.47 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TRAK2]] | -0.47 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[NUDC]] | -0.46 | -0.25 / -0.50 | both halves | 4e-04 |  |
| [[TTC4]] | -0.46 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[AP2A2]] | -0.46 | -0.30 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOV]] | B | RHOV activity raises CCNL1's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.25× lower at baseline in the lines without RHOV | 0.027 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[CXCL2]] | B | CXCL2 activity raises CCNL1's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without CXCL2 | 0.036 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[TOP2A]] | B | TOP2A activity lowers CCNL1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.455). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.5, 6.5); signed map (41.9, 6.0). **Vector** length 109, 47.3% of its response variance represented; |z| ≥ 3 in 1,369 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.4 | +1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | -0.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.5 | -0.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.5 | -0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.5 | -4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.5 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.6 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.0 | -0.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cyclin L1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.31 — chr3:157,146,508-157,160,760 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ania-6a |
| Gene groups (HGNC) | Cyclins |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK58](https://www.uniprot.org/uniprotkb/Q9UK58) (Cyclin-L1):

> Regulatory component of the cyclin-L-CDK11 complex that regulates transcription and pre-mRNA splicing. Inhibited by the CDK-specific inhibitor CDKN1A/p21. May be a candidate proto-oncogene in head and neck squamous cell carcinomas (HNSCC).

**Summary**, from NCBI Gene [57018](https://www.ncbi.nlm.nih.gov/gene/57018):

> Enables cyclin-dependent protein serine/threonine kinase regulator activity. Involved in regulation of mRNA splicing, via spliceosome. Located in nuclear body. Part of cyclin L-CDK11 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20569) · Entrez [57018](https://www.ncbi.nlm.nih.gov/gene/57018) · UniProt [Q9UK58](https://www.uniprot.org/uniprotkb/Q9UK58) · Ensembl [ENSG00000163660](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163660)

## Data

Gene col 8747: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8747); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8747, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8747]; `tensor/DDL_lfc|DDL_z.npy` [8747]; `embed/gene_vectors.npy` [8747]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8747 or target_col == 8747). Every well: [[CCNL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
