---
symbol: "RANBP10"
type: "gene"
col: 6488
ensembl_id: "ENSG00000141084"
name: "RAN binding protein 10"
location: "16q22"
module: 3
arm: "+"
pooled_cpm: 72.74
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# RANBP10

*RAN binding protein 10* — 16q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.07× (z +20.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.430× (z -14.2, q 1e-42, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.626× (z -8.7, q 4e-16, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUGP1]] (+0.70, fdr 7e-06), [[CRY2]] (+0.69, fdr 7e-06), [[HEATR5B]] (+0.68, fdr 7e-06); moves opposite to [[NCR3LG1]] (-0.66, fdr 1e-05), [[SLC39A10]] (-0.64, fdr 1e-05), [[BTBD1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6488.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.07×** | +20.8 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +17.4 | 0e+00 | 43/48 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.36×** | +15.9 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.25×** | +15.1 | 0e+00 | 46/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +10.9 | 1e-25 | 45/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.70×** | +9.3 | 1e-18 | 43/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +8.9 | 5e-17 | 37/48 (A-427, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +7.9 | 3e-13 | 36/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +7.6 | 3e-12 | 32/48 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +6.6 | 2e-09 | 34/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.5 | 3e-06 | 24/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 3e-04 | 24/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +4.4 | 4e-04 | 25/48 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.41×** | +4.4 | 4e-04 | 28/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.22×** | +3.5 | 0.015 | 19/48 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.018 | 22/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.018 | 23/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6488.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.430×** | -14.2 | 1e-42 | 46/49 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.512×** | -12.0 | 2e-30 | 39/43 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.576×** | -9.5 | 5e-19 | 36/45 (NCI-H2030, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.626×** | -8.7 | 4e-16 | 39/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.770×** | -4.9 | 1e-04 | 27/49 (COLO 205, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.795×** | -4.1 | 0.004 | 22/48 (SW480, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -3.8 | 0.011 | 16/48 (RPMI-7951, C32, …) | two highest doses |  |
| [[Busulfan (drug)]] 5 µM |  | 0.889× | -3.1 | 0.13 | 8/49 (SW 1271, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 98.4 | 5 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +14.8) | [[Auranofin (drug)]] 5 µM 0.315× (z -14.7) |
| [[PANC-1 (line)]] | alt | 43.1 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -9.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 121 | 7 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.43× (z +22.8) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -16.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 65.3 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.61× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0814× (z -24.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 44.2 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.27× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 97.5 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -21.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 97.4 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.28× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -10.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 85.7 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -10.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 47.8 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -9.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 51.5 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.94× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -9.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 80.0 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -10.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 79.3 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +12.5) | [[Auranofin (drug)]] 5 µM 0.296× (z -14.0) |
| [[HT-29 (line)]] | alt | 54.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +15.2) | — |
| [[KATO III (line)]] | alt | 64.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.82× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 62.8 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.23× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -9.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 55.2 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 3.55× (z +12.5) | [[Auranofin (drug)]] 5 µM 0.367× (z -9.8) |
| [[A549 (line)]] | wt | 59.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.25× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -17.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 70.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -11.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 66.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +13.1) | — |
| [[LS 180 (line)]] | wt | 59.7 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.49× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 35.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 47.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.56× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 60.5 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.73× (z +10.7) | [[Auranofin (drug)]] 5 µM 0.323× (z -12.1) |
| [[SW 900 (line)]] | alt | 74.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -13.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 90.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.1) | — |
| [[A498 (line)]] | wt | 78.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -9.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 52.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 177 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 71.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -10.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 68.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 58.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -12.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 78.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -10.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 93.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +16.4) | — |
| [[COLO 205 (line)]] | alt | 57.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 57.3 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.75× (z +8.9) | [[Tucidinostat (drug)]] 5 µM 0.491× (z -8.8) |
| [[SNU-1 (line)]] | wt | 55.5 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.86× (z +9.2) | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.265× (z -9.1) |
| [[AN3 CA (line)]] | alt | 82.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -12.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 70.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +8.5) | — |
| [[C32 (line)]] | wt | 63.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -11.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 116 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.195× (z -10.5) |
| [[H4 (line)]] | wt | 66.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -8.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.104× (z -9.6) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 55.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 84.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.4) | — |
| [[SW 1088 (line)]] | alt | 78.9 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0680× (z -8.9) |
| [[SW 1271 (line)]] | alt | 74.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.109× (z -9.2) |
| [[HCT15 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGP1]] | +0.70 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CRY2]] | +0.69 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[HEATR5B]] | +0.68 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.67 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.66 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CCS]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[WASF2]] | +0.66 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[LAMTOR5]] | +0.65 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[ALKBH7]] | +0.65 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PMM1]] | +0.65 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[CRYZL1]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[RNF181]] | +0.64 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCR3LG1]] | -0.66 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SLC39A10]] | -0.64 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[BTBD1]] | -0.63 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[REEP3]] | -0.61 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[TUG1]] | -0.59 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[EIF4G1]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[PURB]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.58 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[SEPTIN11]] | -0.58 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[SOCS4]] | -0.58 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[TRIM44]] | -0.57 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ZNF121]] | -0.57 | -0.43 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.7, -17.1); signed map (-27.3, 10.5). **Vector** length 95.4, 28.5% of its response variance represented; |z| ≥ 3 in 1,123 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.4 | +20.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +15.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +10.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.1 | +2.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +15.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +8.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +4.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.2 | -8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.1 | -9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | RAN binding protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22 — chr16:67,723,070-67,806,560 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1464 |
| Gene groups (HGNC) | CTLH complex subunits |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 3 pathways, smallest: MET activates RAS signaling; Signaling by MET; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6VN20](https://www.uniprot.org/uniprotkb/Q6VN20) (Ran-binding protein 10):

> May act as an adapter protein to couple membrane receptors to intracellular signaling pathways (Probable). Core component of the CTLH E3 ubiquitin-protein ligase complex that selectively accepts ubiquitin from UBE2H and mediates ubiquitination and subsequent proteasomal degradation of the transcription factor HBP1. Enhances dihydrotestosterone-induced transactivation activity of AR, as well as dexamethasone-induced transactivation activity of NR3C1, but does not affect estrogen-induced …

**Summary**, from NCBI Gene [57610](https://www.ncbi.nlm.nih.gov/gene/57610):

> RAN is a small GTPase involved in the assembly of microtubules to form mitotic spindles. The protein encoded by this gene is a cytoplasmic guanine nucleotide exchange factor (GEF) that binds beta-tubulin and has GEF activity toward RAN. The encoded protein plays a role in the formation of noncentrosomal microtubules. In addition, this protein may be involved in the regulation of D(1) receptor signaling by protein kinase C delta and protein kinase C gamma. Several transcript variants encoding …

**Accessions** — [HGNC:29285](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29285) · Entrez [57610](https://www.ncbi.nlm.nih.gov/gene/57610) · UniProt [Q6VN20](https://www.uniprot.org/uniprotkb/Q6VN20) · Ensembl [ENSG00000141084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141084)

## Data

Gene col 6488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6488); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6488]; `tensor/DDL_lfc|DDL_z.npy` [6488]; `embed/gene_vectors.npy` [6488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6488 or target_col == 6488). Every well: [[RANBP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RANBP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
