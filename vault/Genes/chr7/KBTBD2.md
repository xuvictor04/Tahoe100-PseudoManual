---
symbol: "KBTBD2"
type: "gene"
col: 10011
ensembl_id: "ENSG00000170852"
name: "kelch repeat and BTB domain containing 2"
location: "7p14.3"
module: 109
arm: "+"
pooled_cpm: 81.81
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 32
n_dd_up_clean: 7
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# KBTBD2

*kelch repeat and BTB domain containing 2* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.59× (z +11.5, q 5e-28, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.399× (z -16.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHF19]] (+0.64, fdr 1e-05), [[PLEKHG2]] (+0.63, fdr 9e-06), [[EXTL2]] (+0.60, fdr 2e-05); moves opposite to [[HTT]] (-0.58, fdr 3e-05), [[EPS15L1]] (-0.57, fdr 2e-05), [[EXOC6B]] (-0.57, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10011.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +11.5 | 5e-28 | 39/48 (SK-MEL-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.13×** | +9.2 | 1e-17 | 43/49 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +8.5 | 4e-15 | 41/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +6.7 | 4e-09 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +5.5 | 5e-06 | 27/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +4.9 | 1e-04 | 28/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +4.7 | 2e-04 | 30/48 (HEC-1-A, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.29×** | +4.3 | 0.001 | 25/48 (NCI-H460, SK-MEL-2, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.016 | 21/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.093 | 5/48 (Hs 766T, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10011.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.399×** | -16.2 | 0e+00 | 48/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.408×** | -15.8 | 0e+00 | 47/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.419×** | -15.3 | 0e+00 | 46/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.536×** | -11.0 | 7e-26 | 41/49 (SW48, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.528×** | -10.8 | 4e-25 | 39/44 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.639×** | -7.9 | 3e-13 | 38/48 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.748×** | -7.2 | 5e-11 | 32/49 (A549, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -6.9 | 3e-10 | 37/50 (SK-MEL-2, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.679×** | -6.8 | 7e-10 | 41/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.684×** | -6.7 | 1e-09 | 42/48 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.670×** | -6.7 | 1e-09 | 38/48 (A549, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.698×** | -6.1 | 6e-08 | 33/48 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.742×** | -5.4 | 3e-06 | 32/48 (SW480, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.514×** | -5.4 | 3e-06 | 38/48 (A-427, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.527×** | -5.2 | 9e-06 | 34/48 (HEC-1-A, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.747×** | -5.1 | 1e-05 | 36/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.748×** | -4.9 | 3e-05 | 28/48 (NCI-H1573, A-427, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.789×** | -4.8 | 4e-05 | 26/50 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.767×** | -4.6 | 9e-05 | 33/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.797×** | -4.5 | 2e-04 | 25/49 (NCI-H1573, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.780×** | -4.4 | 3e-04 | 28/49 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 70.9 | 11 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.26× (z +17.4) | — |
| [[SW480 (line)]] | alt | 110 | 2 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.309× (z -15.3) |
| [[A-427 (line)]] | wt | 80.7 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 65.3 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.318× (z -14.2) |
| [[PANC-1 (line)]] | alt | 99.2 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.447× (z -9.6) |
| [[A549 (line)]] | wt | 90.5 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.336× (z -11.2) |
| [[KATO III (line)]] | alt | 74.9 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.389× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 41.7 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 94.9 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.0) |
| [[SNU-423 (line)]] | alt | 85.0 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.292× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 105 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.266× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 63.1 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +17.9) | [[Panobinostat (drug)]] 0.5 µM 0.357× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 104 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.246× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 86.0 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.457× (z -9.8) |
| [[HOP62 (line)]] | alt | 72.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -11.9) |
| [[HT-29 (line)]] | alt | 98.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -20.1) |
| [[MIA PaCa-2 (line)]] | alt | 111 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +8.8) ⚠ cell-cycle shift, explains ~79% of this change | [[Panobinostat (drug)]] 5 µM 0.355× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 60.3 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -12.6) |
| [[SHP-77 (line)]] | alt | 153 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.262× (z -12.1) |
| [[A-172 (line)]] | wt | 98.2 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -9.9) |
| [[C32 (line)]] | wt | 106 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.278× (z -11.0) |
| [[COLO 205 (line)]] | alt | 58.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 69.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.356× (z -9.7) |
| [[SW1417 (line)]] | alt | 91.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.331× (z -12.9) |
| [[A498 (line)]] | wt | 76.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -10.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 55.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.315× (z -11.6) |
| [[HCT15 (line)]] | alt | 85.9 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0911× (z -9.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.352× (z -8.7) |
| [[Hs 766T (line)]] | wt | 97.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 69.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.368× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.396× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 64.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.411× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 120 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.362× (z -9.1) |
| [[SW 1271 (line)]] | alt | 80.6 | 0 | 2 | — | [[Mifepristone (drug)]] 0.05 µM 0.0765× (z -10.0) |
| [[SW 900 (line)]] | alt | 73.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +12.6) | [[Belinostat (drug)]] 5 µM 0.392× (z -9.3) |
| [[BT-474 (line)]] | alt | 76.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 65.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 58.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -9.2) |
| [[J82 (line)]] | alt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.409× (z -8.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 69.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.474× (z -8.5) |
| [[LS 180 (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0966× (z -21.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM 0.0795× (z -9.6) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 57.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0737× (z -19.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 75.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 73.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF19]] | +0.64 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[PLEKHG2]] | +0.63 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[EXTL2]] | +0.60 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[CHAMP1]] | +0.60 | +0.37 / +0.57 | both halves | 9e-05 |  |
| [[JUNB]] | +0.60 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[SPRY2]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[EGR3]] | +0.59 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[TADA3]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[IFNGR2]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PNRC2]] | +0.58 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[SKIL]] | +0.58 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[EGR2]] | +0.57 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HTT]] | -0.58 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[EPS15L1]] | -0.57 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[EXOC6B]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[MAP4]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ANO10]] | -0.55 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[ANKRD39]] | -0.55 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SNX29]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ERC1]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[CRYAB]] | -0.54 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[ATP2C1]] | -0.54 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[PHKB]] | -0.54 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[INTS10]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises KBTBD2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.2% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds |
| [[RPL39L]] | B | RPL39L activity lowers KBTBD2's level | lines that do not express RPL39L (16) vs lines expressing it (34) | 1.07× higher at baseline in the lines without RPL39L | 0.048 | ⚠ within organs, on part of the lines; also absent: ANKRD6, RNF150, EVL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.1, 0.7); signed map (5.3, 28.7). **Vector** length 97.6, 31.5% of its response variance represented; |z| ≥ 3 in 1,359 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +11.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +5.4 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~80% of this change | +4.4 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +0.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | -3.7 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.2 | +0.1 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.2 | -0.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -9.7 | -6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -9.2 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.5 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.8 | -6.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.3 | -5.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.6 | -5.4 |
|  | [[EX229 (drug)]] 5 µM |  | -4.5 | -3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.0 | -1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | kelch repeat and BTB domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:32,868,172-32,894,131 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP566C134; previously BKLHD1 |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY47](https://www.uniprot.org/uniprotkb/Q8IY47) (Kelch repeat and BTB domain-containing protein 2):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex that acts as a regulator of the insulin signaling pathway, modulating insulin sensitivity by limiting PIK3R1/p85alpha abundance in adipocytes. Targets PIK3R1, the regulatory subunit of phosphatidylinositol 3-kinase (PI3K), for 'Lys-48'-linked polyubiquitination and proteasome-mediated degradation.

**Summary**, from NCBI Gene [25948](https://www.ncbi.nlm.nih.gov/gene/25948):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in protein K48-linked ubiquitination and regulation of cellular response to insulin stimulus. Acts upstream of or within with a positive effect on protein polyubiquitination. Located in nucleus. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21751) · Entrez [25948](https://www.ncbi.nlm.nih.gov/gene/25948) · UniProt [Q8IY47](https://www.uniprot.org/uniprotkb/Q8IY47) · Ensembl [ENSG00000170852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170852)

## Data

Gene col 10011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10011); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10011]; `tensor/DDL_lfc|DDL_z.npy` [10011]; `embed/gene_vectors.npy` [10011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10011 or target_col == 10011). Every well: [[KBTBD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KBTBD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
