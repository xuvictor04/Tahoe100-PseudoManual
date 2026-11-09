---
symbol: "PMEPA1"
type: "gene"
col: 4507
ensembl_id: "ENSG00000124225"
name: "prostate transmembrane protein, androgen induced 1"
location: "20q13.31"
module: 141
arm: "+"
pooled_cpm: 200.56
n_lines_expressing: 44
n_dd_up: 20
n_dd_down: 38
n_dd_up_clean: 11
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 14
direction_downstream: 14
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# PMEPA1

*prostate transmembrane protein, androgen induced 1* — 20q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Rapamycin (drug)]] 5 µM: 1.41× (z +8.2, q 2e-13, up in 35 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.443× (z -19.4, q 0e+00, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP2K3]] (+0.66, fdr 7e-06), [[JAG1]] (+0.64, fdr 7e-06), [[SVIL]] (+0.63, fdr 7e-06); moves opposite to [[CIAO2A]] (-0.56, fdr 2e-05), [[MIGA1]] (-0.55, fdr 1e-05), [[STBD1]] (-0.53, fdr 3e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[WNT7B]] → it (grade B ⚠); 14 go from it, the strongest it → [[MBP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4507.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rapamycin (drug)]] 5 µM |  | **1.41×** | +8.2 | 2e-13 | 35/42 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.57×** | +7.3 | 8e-11 | 26/42 (KATO III, COLO 205, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +6.9 | 1e-09 | 24/42 (BT-474, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.3 | 6e-08 | 28/41 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.44×** | +5.9 | 3e-07 | 28/42 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.42×** | +5.9 | 4e-07 | 25/42 (NCI-H460, SW480, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.41×** | +5.9 | 4e-07 | 31/42 (C32, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +5.5 | 2e-06 | 24/42 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +5.5 | 2e-06 | 24/42 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Larotrectinib sulfate (drug)]] 5 µM | ⚠ unreliable plate only | **1.34×** | +5.0 | 3e-05 | 25/42 (C32, J82, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.34×** | +4.9 | 6e-05 | 25/42 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.31×** | +4.6 | 2e-04 | 25/43 (SW1417, NCI-H2347, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +4.6 | 2e-04 | 23/43 (SW1417, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.30×** | +4.4 | 4e-04 | 23/42 (SW480, NCI-H460, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.29×** | +4.3 | 6e-04 | 23/42 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.17× | +3.8 | 0.005 | 15/43 (C32, PANC-1, …) | all doses, flat |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.074 | 9/42 (A549, Panc 03.27, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +2.9 | 0.079 | 13/43 (A549, RPMI-7951, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.20×** | +2.9 | 0.079 | 13/42 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +2.9 | 0.079 | 21/42 (Hs 766T, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.05 µM |  | 1.19× | +2.9 | 0.089 | 16/43 (C32, J82, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4507.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.443×** | -19.4 | 0e+00 | 35/43 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.631×** | -7.8 | 2e-12 | 28/42 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -7.5 | 2e-11 | 28/42 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.652×** | -7.2 | 8e-11 | 29/42 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.642×** | -7.2 | 8e-11 | 31/41 (SW480, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.714×** | -6.2 | 4e-08 | 31/44 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.708×** | -6.2 | 4e-08 | 28/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.687×** | -6.0 | 2e-07 | 29/42 (NCI-H1792, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.759×** | -5.9 | 2e-07 | 27/42 (SW480, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.736×** | -5.9 | 2e-07 | 28/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.528×** | -5.6 | 1e-06 | 25/41 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.698×** | -5.6 | 1e-06 | 31/42 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.721×** | -5.5 | 2e-06 | 32/43 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -5.5 | 2e-06 | 1/44 (NCI-H1792) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.726×** | -5.4 | 3e-06 | 29/42 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.752×** | -4.6 | 1e-04 | 28/42 (SW480, SW 1088, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4507. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 203 | 1 (1 ⚠) | 18 | [[Harringtonine (drug)]] 5 µM 3.05× (z +10.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -11.9) |
| [[SW480 (line)]] | alt | 141 | 4 (3 ⚠) | 13 | [[Digitoxin (drug)]] 0.5 µM 2.61× (z +11.6) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.40× (z +10.6) | [[Binimetinib (drug)]] 0.5 µM 0.341× (z -15.9) |
| [[HEC-1-A (line)]] | alt | 376 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -23.5) |
| [[KATO III (line)]] | alt | 289 | 7 (5 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +27.9) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.34× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 160 | 8 (6 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +12.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.75× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -11.2) |
| [[SW1417 (line)]] | alt | 863 | 1 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.32× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -28.5) |
| [[A549 (line)]] | wt | 426 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -14.9) |
| [[A498 (line)]] | wt | 160 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +16.8) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[BT-474 (line)]] | alt | 699 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +13.9) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.62× (z +11.5) | — |
| [[A-172 (line)]] | wt | 87.5 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.38× (z +10.6) | — |
| [[COLO 205 (line)]] | alt | 155 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +16.9) ⚠ cell-cycle shift, explains ~91% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -10.6) |
| [[HOP62 (line)]] | alt | 239 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.39× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -17.2) |
| [[MIA PaCa-2 (line)]] | alt | 171 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -20.0) |
| [[NCI-H1792 (line)]] | alt | 426 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -21.7) |
| [[SW48 (line)]] | wt | 101 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.44× (z +10.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 4.30× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 237 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 82.4 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 1.98× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -9.5) |
| [[PANC-1 (line)]] | alt | 230 | 1 | 2 | [[Rapamycin (drug)]] 5 µM 1.64× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -20.0) |
| [[C32 (line)]] | wt | 54.5 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.19× (z +9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Rapamycin (drug)]] 5 µM 2.65× (z +8.8) | — |
| [[J82 (line)]] | alt | 60.1 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.99× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 279 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -18.4) |
| [[SK-MEL-2 (line)]] | alt | 141 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -10.8) |
| [[SW 1271 (line)]] | alt | 382 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -15.2) |
| [[A-427 (line)]] | wt | 50.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -19.5) ⚠ cell-cycle shift, explains ~91% of this change |
| [[AN3 CA (line)]] | alt | 56.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +8.7) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[AsPC-1 (line)]] | alt | 246 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.5) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[C-33 A (line)]] | alt | 67.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.68× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 278 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -16.8) |
| [[Hs 766T (line)]] | wt | 229 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.33× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 75.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -8.6) |
| [[LoVo (line)]] | wt | 128 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.9) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[LOX-IMVI (line)]] | wt | 73.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.210× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 279 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 263 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -17.7) |
| [[RPMI-7951 (line)]] | alt | 275 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -12.8) |
| [[SNU-423 (line)]] | alt | 202 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -8.6) |
| [[SW 900 (line)]] | alt | 188 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -11.2) |
| [[CHP-212 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 46.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 82.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 198 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4507), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP2K3]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[JAG1]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SVIL]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[IER2]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[DUSP4]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NR4A1]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ARHGAP26]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[DUSP5]] | +0.59 | +0.58 / +0.58 | both halves | 8e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SMOX]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SLC20A1]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_TGF_BETA_SIGNALING |
| [[SMAD3]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_TGF_BETA_SIGNALING; STRING 882 |
| [[DCBLD2]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO2A]] | -0.56 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[MIGA1]] | -0.55 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[STBD1]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[LNPK]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[FHIP2A]] | -0.52 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[VPS37A]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[TCEANC2]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ZNF343]] | -0.48 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[SOS1]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ZNF675]] | -0.48 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[TMED8]] | -0.48 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[DERL1]] | -0.47 | -0.38 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT7B]] | B | WNT7B activity raises PMEPA1's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.63× lower at baseline in the lines without WNT7B | 0.004 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[GOLT1A]] | B | GOLT1A activity raises PMEPA1's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.16× lower at baseline in the lines without GOLT1A | 0.015 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[ITGA3]] | B | ITGA3 activity raises PMEPA1's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 3.15× lower at baseline in the lines without ITGA3 | 0.016 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[SMAD3]] | B | SMAD3 activity raises PMEPA1's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 2.79× lower at baseline in the lines without SMAD3 | 0.017 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[BCAN-AS1]] | B | BCAN-AS1 activity raises PMEPA1's level | lines that do not express BCAN-AS1 (11) vs lines expressing it (39) | 1.90× lower at baseline in the lines without BCAN-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000272405, BCAN-AS2, ETV7; maybe low, not absent |
| [[IER3]] | B | IER3 activity raises PMEPA1's level | lines that do not express IER3 (5) vs lines expressing it (45) | 4.48× lower at baseline in the lines without IER3 | 0.022 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[VDR]] | B | VDR activity raises PMEPA1's level | lines that do not express VDR (8) vs lines expressing it (42) | 2.57× lower at baseline in the lines without VDR | 0.024 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[CD22]] | B | CD22 activity raises PMEPA1's level | lines that do not express CD22 (21) vs lines expressing it (29) | 2.30× lower at baseline in the lines without CD22 | 0.027 | ⚠ within organs, on part of the lines; also absent: CX3CL1, SHROOM4, CFB; maybe low, not absent |
| [[TRIB1]] | B | TRIB1 activity raises PMEPA1's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 2.80× lower at baseline in the lines without TRIB1 | 0.045 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[DUSP4]] | B | DUSP4 activity raises PMEPA1's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.13× lower at baseline in the lines without DUSP4 | 0.051 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[SHB]] | B | SHB activity raises PMEPA1's level | lines that do not express SHB (5) vs lines expressing it (45) | 3.58× lower at baseline in the lines without SHB | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC2A1, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[SMOX]] | B | SMOX activity raises PMEPA1's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.40× lower at baseline in the lines without SMOX | 0.087 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MBP]] | B | PMEPA1 activity raises MBP's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.26× lower at baseline in the lines without PMEPA1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[ITGA6]] | B | PMEPA1 activity raises ITGA6's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.69× lower at baseline in the lines without PMEPA1 | 0.037 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[ZMIZ2]] | B | PMEPA1 activity raises ZMIZ2's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without PMEPA1 | 0.046 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[CAB39]] | B | PMEPA1 activity raises CAB39's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without PMEPA1 | 0.047 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[WNT7B]] | B | PMEPA1 activity raises WNT7B's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 3.15× lower at baseline in the lines without PMEPA1 | 0.055 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[SMAD3]] | B | PMEPA1 activity raises SMAD3's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.94× lower at baseline in the lines without PMEPA1 | 0.069 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[LAMC2]] | B | PMEPA1 activity raises LAMC2's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 3.12× lower at baseline in the lines without PMEPA1 | 0.070 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[EGR1]] | B | PMEPA1 activity raises EGR1's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.74× lower at baseline in the lines without PMEPA1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[ARHGAP26]] | B | PMEPA1 activity raises ARHGAP26's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.87× lower at baseline in the lines without PMEPA1 | 0.083 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[MYO15B]] | B | PMEPA1 activity raises MYO15B's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without PMEPA1 | 0.084 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[RIN2]] | B | PMEPA1 activity raises RIN2's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 2.27× lower at baseline in the lines without PMEPA1 | 0.087 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |
| [[HES1]] | B | PMEPA1 activity raises HES1's level | lines that do not express PMEPA1 (6) vs lines expressing it (44) | 1.50× lower at baseline in the lines without PMEPA1 | 0.087 | ⚠ within organs, on part of the lines; also absent: SOX4, SLC2A1-DT, ENSG00000285253 |

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.3, 3.2); signed map (5.4, 43.2). **Vector** length 141, 43.6% of its response variance represented; |z| ≥ 3 in 1,732 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.2 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +1.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.5 | +6.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +4.4 | +4.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +4.1 | +8.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -19.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.2 | -6.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.8 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.7 | -7.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.9 | -7.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.9 | -5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.8 | -5.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.5 | -6.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.5 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | prostate transmembrane protein, androgen induced 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.31 — chr20:57,648,392-57,711,536 (-) |
| Ensembl biotype | protein_coding |
| Also known as | STAG1; previously TMEPAI |
| Hallmark sets | TGF_BETA_SIGNALING, ANDROGEN_RESPONSE, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: Downregulation of TGF-beta receptor signaling; TGF-beta receptor signaling activates SMADs; Signaling by TGF-beta Receptor Complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969W9](https://www.uniprot.org/uniprotkb/Q969W9) (Protein TMEPAI):

> Functions as a negative regulator of TGF-beta signaling and thereby probably plays a role in cell proliferation, differentiation, apoptosis, motility, extracellular matrix production and immunosuppression. In the canonical TGF-beta pathway, ZFYVE9/SARA recruits the intracellular signal transducer and transcriptional modulators SMAD2 and SMAD3 to the TGF-beta receptor. Phosphorylated by the receptor, SMAD2 and SMAD3 then form a heteromeric complex with SMAD4 that translocates to the nucleus to …

**Summary**, from NCBI Gene [56937](https://www.ncbi.nlm.nih.gov/gene/56937):

> This gene encodes a transmembrane protein that contains a Smad interacting motif (SIM). Expression of this gene is induced by androgens and transforming growth factor beta, and the encoded protein suppresses the androgen receptor and transforming growth factor beta signaling pathways though interactions with Smad proteins. Overexpression of this gene may play a role in multiple types of cancer. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this …

**Accessions** — [HGNC:14107](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14107) · Entrez [56937](https://www.ncbi.nlm.nih.gov/gene/56937) · UniProt [Q969W9](https://www.uniprot.org/uniprotkb/Q969W9) · Ensembl [ENSG00000124225](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124225)

## Data

Gene col 4507: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4507); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4507, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4507]; `tensor/DDL_lfc|DDL_z.npy` [4507]; `embed/gene_vectors.npy` [4507]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4507 or target_col == 4507). Every well: [[PMEPA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMEPA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
