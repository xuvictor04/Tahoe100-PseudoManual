---
symbol: "CSDE1"
type: "gene"
col: 185
ensembl_id: "ENSG00000009307"
name: "cold shock domain containing E1"
location: "1p13.2"
module: 20
arm: "+"
pooled_cpm: 349.4
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CSDE1

*cold shock domain containing E1* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.05× (z +21.4, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.46× (z +7.3, q 4e-11, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.406× (z -17.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCBP2]] (+0.75, fdr 7e-06), [[PAPOLA]] (+0.70, fdr 7e-06), [[GHITM]] (+0.69, fdr 7e-06); moves opposite to [[ORAI1]] (-0.68, fdr 1e-05), [[DPF1]] (-0.62, fdr 3e-05), [[NTMT1]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CYBRD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 185.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.05×** | +21.4 | 0e+00 | 48/49 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +18.7 | 0e+00 | 44/44 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +14.1 | 7e-43 | 45/45 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +7.3 | 4e-11 | 43/48 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +7.0 | 2e-10 | 39/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +7.0 | 2e-10 | 0/50 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.40×** | +6.5 | 8e-09 | 38/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +6.1 | 6e-08 | 43/48 (HT-29, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +6.0 | 1e-07 | 43/49 (SNU-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.8 | 5e-07 | 32/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +4.7 | 1e-04 | 31/48 (SW48, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.7 | 2e-04 | 30/38 (HEC-1-A, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.27×** | +4.6 | 2e-04 | 31/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.55×** | +4.4 | 4e-04 | 43/47 (LoVo, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.3 | 6e-04 | 38/45 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.027 | 28/48 (LS 180, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.3 | 0.027 | 22/48 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.061 | 34/48 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.17× | +2.9 | 0.086 | 19/48 (HS-578T, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 185.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.406×** | -17.3 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.426×** | -16.4 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.489×** | -13.7 | 2e-40 | 48/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.582×** | -10.4 | 5e-23 | 46/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.726×** | -6.1 | 9e-08 | 41/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.545×** | -6.1 | 1e-07 | 46/49 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.785×** | -5.6 | 1e-06 | 32/48 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.752×** | -5.3 | 1e-05 | 31/48 (HT-29, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.826×** | -3.7 | 0.015 | 26/48 (CHP-212, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.847× | -3.2 | 0.078 | 20/48 (SW480, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -3.1 | 0.10 | 21/48 (HT-29, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 185. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 265 | 8 (8 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +17.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -17.7) |
| [[HT-29 (line)]] | alt | 448 | 5 (3 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.75× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.426× (z -14.4) |
| [[LoVo (line)]] | wt | 355 | 6 (6 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +21.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.372× (z -16.6) |
| [[LS 180 (line)]] | wt | 337 | 6 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.84× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.355× (z -15.7) |
| [[HEC-1-A (line)]] | alt | 377 | 4 (4 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +18.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -13.3) |
| [[KATO III (line)]] | alt | 284 | 4 (4 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +18.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.332× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 376 | 4 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +17.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.75× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.352× (z -16.3) |
| [[Panc 03.27 (line)]] | alt | 348 | 4 (4 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +24.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.397× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 554 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +21.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.433× (z -13.4) |
| [[A-172 (line)]] | wt | 268 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +19.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.476× (z -10.4) |
| [[A-427 (line)]] | wt | 269 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +19.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.416× (z -13.7) |
| [[A549 (line)]] | wt | 260 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +19.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 285 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +14.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.293× (z -17.5) |
| [[HepG2_C3A (line)]] | wt | 343 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -14.7) |
| [[HOP62 (line)]] | alt | 287 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +19.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.369× (z -13.1) |
| [[J82 (line)]] | alt | 347 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +19.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -17.3) |
| [[MIA PaCa-2 (line)]] | alt | 391 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +19.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 428 | 5 (5 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +12.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.480× (z -11.7) |
| [[PANC-1 (line)]] | alt | 309 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +20.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.77× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.406× (z -13.4) |
| [[SW 900 (line)]] | alt | 315 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +14.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.331× (z -16.5) |
| [[SW48 (line)]] | wt | 438 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +14.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.421× (z -12.0) |
| [[SW480 (line)]] | alt | 342 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +19.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.331× (z -19.0) |
| [[A498 (line)]] | wt | 331 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +17.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.406× (z -12.6) |
| [[C-33 A (line)]] | alt | 417 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +15.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.392× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 241 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +15.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.397× (z -13.5) |
| [[CHP-212 (line)]] | wt | 496 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.403× (z -10.7) |
| [[Hs 766T (line)]] | wt | 364 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +15.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.397× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 322 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +16.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -14.8) |
| [[NCI-H1792 (line)]] | alt | 380 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +18.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.465× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 332 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +13.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.399× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 892 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +16.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.435× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 363 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.84× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.463× (z -10.7) |
| [[SNU-423 (line)]] | alt | 380 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +17.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.458× (z -11.2) |
| [[SW1417 (line)]] | alt | 232 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +13.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.407× (z -13.5) |
| [[HCT15 (line)]] | alt | 512 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +13.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.388× (z -15.0) |
| [[hTERT-HPNE (line)]] | wt | 420 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +14.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.363× (z -14.2) |
| [[BT-474 (line)]] | alt | 332 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +10.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -12.8) |
| [[COLO 205 (line)]] | alt | 220 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +13.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.411× (z -11.2) |
| [[H4 (line)]] | wt | 291 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +13.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.296× (z -13.5) |
| [[RKO (line)]] | wt | 308 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +17.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.411× (z -13.2) |
| [[AN3 CA (line)]] | alt | 480 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.377× (z -11.3) |
| [[C32 (line)]] | wt | 261 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +15.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 477 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +16.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 262 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +17.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 409 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +11.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.494× (z -9.7) |
| [[NCI-H2122 (line)]] | alt | 307 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 483 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 394 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 298 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 185), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCBP2]] | +0.75 | +0.68 / +0.72 | both halves | 7e-06 | STRING 644 |
| [[PAPOLA]] | +0.70 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[GHITM]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[ST13]] | +0.66 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[RPL14]] | +0.65 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[EEF1A1]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[EEF1G]] | +0.62 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ALDH2]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[UFC1]] | +0.61 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[CANX]] | +0.60 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[EIF3F]] | +0.60 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[RPL4]] | +0.60 | +0.57 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORAI1]] | -0.68 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[DPF1]] | -0.62 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[NTMT1]] | -0.61 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[TXNDC17]] | -0.60 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[MAP1S]] | -0.58 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[ARF6]] | -0.57 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[MTMR9]] | -0.56 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[DUSP6]] | -0.56 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[POLR3K]] | -0.56 | -0.29 / -0.58 | both halves | 2e-04 |  |
| [[KRI1]] | -0.56 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[NANP]] | -0.56 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[MPHOSPH6]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYBRD1]] | B | CYBRD1 activity raises CSDE1's level | lines that do not express CYBRD1 (17) vs lines expressing it (33) | 1.19× lower at baseline in the lines without CYBRD1 | 0.035 | ⚠ within organs, on part of the lines; also absent: MME, BDNF, APOBEC3G |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CSDE1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CSDE1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.423). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.9, -23.8); signed map (-21.2, -32.3). **Vector** length 112, 47.4% of its response variance represented; |z| ≥ 3 in 1,291 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.0 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +14.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +18.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +7.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.6 | +2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.5 | +0.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +4.1 | -0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | -1.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -10.4 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.3 | -5.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.6 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.6 | -13.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -5.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.7 | +0.8 |
|  | [[vincristine (drug)]] 5 µM |  | -2.5 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | cold shock domain containing E1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:114,716,913-114,758,676 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D1S155E, UNR |
| Gene groups (HGNC) | Cold shock domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O75534](https://www.uniprot.org/uniprotkb/O75534) (Cold shock domain-containing protein E1):

> RNA-binding protein involved in translationally coupled mRNA turnover. Implicated with other RNA-binding proteins in the cytoplasmic deadenylation/translational and decay interplay of the FOS mRNA mediated by the major coding-region determinant of instability (mCRD) domain. Required for efficient formation of stress granules.; (Microbial infection) Required for internal initiation of translation of human rhinovirus RNA.

**Summary**, from NCBI Gene [7812](https://www.ncbi.nlm.nih.gov/gene/7812):

> Enables RISC complex binding activity; RNA stem-loop binding activity; and lncRNA binding activity. Involved in IRES-dependent viral translational initiation; regulation of gene expression; and stress granule assembly. Located in cytosol. Part of CRD-mediated mRNA stability complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29905) · Entrez [7812](https://www.ncbi.nlm.nih.gov/gene/7812) · UniProt [O75534](https://www.uniprot.org/uniprotkb/O75534) · Ensembl [ENSG00000009307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000009307)

## Data

Gene col 185: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 185); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 185, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 185]; `tensor/DDL_lfc|DDL_z.npy` [185]; `embed/gene_vectors.npy` [185]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 185 or target_col == 185). Every well: [[CSDE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSDE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
