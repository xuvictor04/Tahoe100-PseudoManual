---
symbol: "ZBTB43"
type: "gene"
col: 9762
ensembl_id: "ENSG00000169155"
name: "zinc finger and BTB domain containing 43"
location: "9q33.3"
module: 34
arm: "+"
pooled_cpm: 111.2
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 12
n_dd_up_clean: 32
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# ZBTB43

*zinc finger and BTB domain containing 43* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.21× (z +14.5, q 4e-45, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.655× (z -7.0, q 1e-09, down in 28 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.796× (z -5.5, q 8e-06, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSTB]] (+0.64, fdr 7e-06), [[PLEKHM1]] (+0.62, fdr 7e-06), [[ATP6V1D]] (+0.59, fdr 1e-05); moves opposite to [[ATP5F1A]] (-0.64, fdr 7e-06), [[NFIA]] (-0.64, fdr 7e-06), [[TMPO]] (-0.63, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TM4SF19-DYNLT2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9762.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.21×** | +14.5 | 4e-45 | 48/49 (LoVo, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +13.8 | 1e-40 | 42/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.08×** | +12.3 | 1e-32 | 45/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.04×** | +12.3 | 1e-32 | 46/48 (BT-474, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +11.9 | 2e-30 | 43/48 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +11.4 | 3e-28 | 41/48 (LoVo, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +11.3 | 9e-28 | 41/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.87×** | +10.5 | 6e-24 | 44/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.86×** | +10.4 | 1e-23 | 44/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +9.0 | 1e-17 | 41/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +8.7 | 2e-16 | 39/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +6.8 | 6e-10 | 33/48 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +6.4 | 7e-09 | 31/48 (LOX-IMVI, LoVo, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +6.2 | 3e-08 | 32/48 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +6.0 | 7e-08 | 31/49 (HT-29, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.35×** | +4.9 | 3e-05 | 28/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9762.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.655×** | -7.0 | 1e-09 | 28/49 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -6.5 | 3e-08 | 26/43 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -5.5 | 8e-06 | 31/48 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.760×** | -4.5 | 0.001 | 28/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.798×** | -3.8 | 0.013 | 24/49 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -3.8 | 0.013 | 16/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.801×** | -3.8 | 0.013 | 28/48 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.793×** | -3.6 | 0.019 | 21/45 (A549, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -3.5 | 0.028 | 0/50 | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **0.813×** | -3.5 | 0.030 | 18/48 (LoVo, SK-MEL-2, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.821×** | -3.3 | 0.042 | 19/48 (NCI-H460, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 5 µM |  | 0.872× | -3.3 | 0.045 | 12/49 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~3% of this change | **0.826×** | -3.2 | 0.053 | 19/48 (NCI-H2347, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Larotrectinib (drug)]] 5 µM |  | 0.877× | -3.2 | 0.064 | 11/48 (Hs 766T, CHP-212, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.832×** | -3.1 | 0.065 | 22/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.832×** | -3.1 | 0.065 | 15/49 (NCI-H460, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 0.881× | -3.0 | 0.076 | 8/48 (SK-MEL-2, SW 1088, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.837× | -3.0 | 0.079 | 15/48 (HOP62, SW480, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.839× | -3.0 | 0.087 | 18/47 (LS 180, J82, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.838× | -2.9 | 0.091 | 18/47 (AsPC-1, BT-474, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.886× | -2.9 | 0.094 | 11/49 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9762. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 264 | 10 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.62× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 88.1 | 8 | 2 | [[TAK-901 (drug)]] 5 µM 11.4× (z +15.5) | [[Tucidinostat (drug)]] 5 µM 0.529× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 133 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 194 | 7 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.31× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -10.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 49.8 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +16.1) | — |
| [[KATO III (line)]] | alt | 89.9 | 8 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.88× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 95.9 | 7 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.22× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 54.2 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +16.4) | — |
| [[SNU-1 (line)]] | wt | 92.7 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.40× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 55.0 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +11.9) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.75× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 143 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.418× (z -8.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 196 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 48.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +16.8) | — |
| [[A498 (line)]] | wt | 167 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -12.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 153 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -15.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 65.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.32× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 150 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -16.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 98.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +10.8) | — |
| [[A-172 (line)]] | wt | 208 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.30× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -15.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 147 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -11.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 110 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.363× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.511× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 94.4 | 2 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.82× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 159 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -12.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 106 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.70× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -10.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 91.9 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.59× (z +11.4) | — |
| [[A-427 (line)]] | wt | 36.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.8) | — |
| [[AsPC-1 (line)]] | alt | 121 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.1) | — |
| [[COLO 205 (line)]] | alt | 210 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 107 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.24× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 100 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 8.70× (z +10.3) | [[Tucidinostat (drug)]] 5 µM 0.492× (z -9.2) |
| [[SHP-77 (line)]] | alt | 89.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.78× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 117 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.73× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -11.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 127 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.431× (z -8.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 72.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.28× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 75.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.4) | — |
| [[SW 1088 (line)]] | alt | 85.7 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.0794× (z -8.5) |
| [[SW48 (line)]] | wt | 69.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 95.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 167 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9762), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSTB]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[PLEKHM1]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ATP6V1D]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ZNF611]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 | same gene group |
| [[RABGEF1]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[NOXRED1]] | +0.56 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[ZFYVE1]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[ZNF432]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[RRAGC]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ZNF430]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 | same gene group |
| [[C19orf25]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[FBXL12]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1A]] | -0.64 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[NFIA]] | -0.64 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[TMPO]] | -0.63 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[HNRNPR]] | -0.59 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[GMPS]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[LMNB1]] | -0.57 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[CAPRIN1]] | -0.56 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[PRKDC]] | -0.56 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[CSE1L]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[TOP2B]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[HADH]] | -0.55 | -0.60 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TM4SF19-DYNLT2B]] | B | TM4SF19-DYNLT2B activity raises ZBTB43's level | lines that do not express TM4SF19-DYNLT2B (20) vs lines expressing it (30) | 1.47× lower at baseline in the lines without TM4SF19-DYNLT2B | 0.028 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[WFDC3]] | B | WFDC3 activity raises ZBTB43's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.44× lower at baseline in the lines without WFDC3 | 0.046 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[WFDC10B]] | B | WFDC10B activity raises ZBTB43's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 1.39× lower at baseline in the lines without WFDC10B | 0.078 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[CRYM]] | B | CRYM activity raises ZBTB43's level | lines that do not express CRYM (12) vs lines expressing it (38) | 1.44× lower at baseline in the lines without CRYM | 0.080 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.307). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.7, -38.3); signed map (7.3, 17.6). **Vector** length 106, 38.8% of its response variance represented; |z| ≥ 3 in 1,464 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.0 | +11.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +5.8 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.2 | +4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.1 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | +4.8 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.7 | +6.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.6 | +4.1 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.7 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -5.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | +6.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.3 | -0.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:126,805,006-126,838,210 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0414, ZNF-X, FLJ22470, ZBTB22B; previously ZNF297B |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O43298](https://www.uniprot.org/uniprotkb/O43298) (Zinc finger and BTB domain-containing protein 43):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [23099](https://www.ncbi.nlm.nih.gov/gene/23099):

> Enables RNA polymerase III general transcription initiation factor binding activity and sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in chromatin. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17908) · Entrez [23099](https://www.ncbi.nlm.nih.gov/gene/23099) · UniProt [O43298](https://www.uniprot.org/uniprotkb/O43298) · Ensembl [ENSG00000169155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169155)

## Data

Gene col 9762: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9762); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9762, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9762]; `tensor/DDL_lfc|DDL_z.npy` [9762]; `embed/gene_vectors.npy` [9762]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9762 or target_col == 9762). Every well: [[ZBTB43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
