---
symbol: "CALD1"
type: "gene"
col: 4377
ensembl_id: "ENSG00000122786"
name: "caldesmon 1"
location: "7q33"
module: 66
arm: "+"
pooled_cpm: 230.92
n_lines_expressing: 36
n_dd_up: 10
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# CALD1

*caldesmon 1* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.28× (z +16.8, q 0e+00, up in 31 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.20× (z +5.3, q 2e-05, up in 16 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.517× (z -18.8, q 0e+00, down in 27 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL12A1]] (+0.63, fdr 1e-05), [[GLIPR1]] (+0.62, fdr 1e-05), [[ALPK2]] (+0.59, fdr 1e-05); moves opposite to [[RAD9A]] (-0.53, fdr 2e-05), [[CCT6P3-1]] (-0.48, fdr 5e-05), [[SMG1P5]] (-0.48, fdr 4e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CCDC80]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4377.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +16.8 | 0e+00 | 31/35 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +12.4 | 9e-33 | 31/32 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +11.5 | 3e-28 | 25/33 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +5.3 | 2e-05 | 16/34 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +5.2 | 3e-05 | 19/35 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.7 | 2e-04 | 19/33 (HepG2/C3A, hTERT-HPNE, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 8e-04 | 20/34 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 9e-04 | 17/34 (HepG2/C3A, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.0 | 0.003 | 14/34 (NCI-H23, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.006 | 15/34 (A549, NCI-H2347, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.19× | +3.8 | 0.007 | 15/35 (HepG2/C3A, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.17× | +3.5 | 0.026 | 14/36 (HepG2/C3A, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 1.18× | +3.4 | 0.029 | 11/33 (hTERT-HPNE, SW480, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.042 | 10/35 (hTERT-HPNE, HS-578T, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.051 | 12/33 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.18× | +3.2 | 0.053 | 13/33 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.17× | +3.2 | 0.053 | 13/34 (NCI-H23, C32, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.077 | 6/34 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.077 | 13/34 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.077 | 11/34 (NCI-H23, A-427, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.517×** | -18.8 | 0e+00 | 27/35 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.447×** | -16.4 | 0e+00 | 29/34 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.508×** | -13.8 | 8e-41 | 29/34 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.598×** | -10.5 | 2e-23 | 26/34 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -10.1 | 8e-22 | 30/34 (SHP-77, H4, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.614×** | -9.9 | 4e-21 | 31/34 (H4, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -9.5 | 1e-19 | 27/34 (H4, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.559×** | -9.4 | 3e-19 | 31/34 (H4, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.629×** | -9.4 | 3e-19 | 28/34 (H4, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.644×** | -8.9 | 2e-17 | 29/34 (C32, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.650×** | -8.8 | 9e-17 | 28/33 (H4, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.660×** | -8.5 | 1e-15 | 30/34 (H4, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -8.0 | 4e-14 | 25/34 (H4, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.732×** | -6.3 | 9e-09 | 28/34 (H4, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.748×** | -5.9 | 1e-07 | 21/34 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.767×** | -5.4 | 3e-06 | 20/34 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 870 | 0 | 19 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -19.4) |
| [[RKO (line)]] | wt | 402 | 0 | 18 (6 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0498× (z -23.6) |
| [[LOX-IMVI (line)]] | wt | 895 | 0 | 14 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -24.0) |
| [[NCI-H23 (line)]] | alt | 243 | 8 (4 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 2.87× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -16.7) |
| [[NCI-H460 (line)]] | wt | 184 | 2 (2 ⚠) | 11 (6 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -24.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.322× (z -15.5) |
| [[SW480 (line)]] | alt | 178 | 1 (1 ⚠) | 11 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +11.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.220× (z -21.7) |
| [[C32 (line)]] | wt | 884 | 3 (3 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +12.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -21.6) |
| [[MIA PaCa-2 (line)]] | alt | 259 | 0 | 11 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 217 | 2 (2 ⚠) | 9 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -18.3) |
| [[SHP-77 (line)]] | alt | 185 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -26.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -16.6) |
| [[HOP62 (line)]] | alt | 275 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -16.7) |
| [[A-172 (line)]] | wt | 301 | 5 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.518× (z -9.8) |
| [[A549 (line)]] | wt | 236 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.366× (z -11.6) |
| [[CHP-212 (line)]] | wt | 445 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.293× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 243 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +11.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.359× (z -12.8) |
| [[HepG2_C3A (line)]] | wt | 249 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 498 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +11.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -17.0) |
| [[LS 180 (line)]] | wt | 93.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.99× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 176 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.03× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -13.8) |
| [[SNU-423 (line)]] | alt | 343 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +13.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.417× (z -9.7) |
| [[A498 (line)]] | wt | 603 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +18.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 528 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.95× (z +13.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 263 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +14.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 108 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +13.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 412 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.457× (z -11.9) |
| [[A-427 (line)]] | wt | 123 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 411 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -8.8) |
| [[Hs 766T (line)]] | wt | 196 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +9.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -15.9) |
| [[NCI-H2347 (line)]] | alt | 112 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.92× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 245 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.425× (z -8.8) |
| [[SW 1088 (line)]] | alt | 989 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -12.6) |
| [[SW 900 (line)]] | alt | 127 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 62.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.78× (z +9.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 20.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 51.9 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 18.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 765 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 54.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.7 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 27.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 32.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 54.8 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 25.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL12A1]] | +0.63 | +0.52 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[GLIPR1]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[ALPK2]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[FILIP1L]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CAV1]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[RBMS3]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TRIM55]] | +0.56 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[CCDC80]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[CLCN4]] | +0.56 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[THBS1]] | +0.55 | +0.42 / +0.54 | both halves | 4e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[LINC00702]] | +0.54 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[TENM2]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD9A]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[CCT6P3-1]] | -0.48 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[SMG1P5]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CAPN10]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[SAP130]] | -0.46 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[TNPO3]] | -0.46 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[TMEM53]] | -0.44 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[ZNF487]] | -0.44 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[ZMYND19]] | -0.44 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ASB16-AS1]] | -0.44 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[GID4]] | -0.42 | -0.40 / -0.37 | both halves | 7e-05 |  |
| [[TAF4]] | -0.42 | -0.44 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC80]] | B | CCDC80 activity raises CALD1's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 3.66× lower at baseline in the lines without CCDC80 | 0.008 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[PHACTR1]] | B | PHACTR1 activity raises CALD1's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 4.36× lower at baseline in the lines without PHACTR1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L |
| [[ALPK2]] | B | ALPK2 activity raises CALD1's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 5.24× lower at baseline in the lines without ALPK2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4 |
| [[ZNF883]] | B | ZNF883 activity raises CALD1's level | lines that do not express ZNF883 (22) vs lines expressing it (28) | 4.05× lower at baseline in the lines without ZNF883 | 0.037 | ⚠ within organs, on part of the lines; also absent: AK5, SOX5, GAP43 |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises CALD1's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 4.41× lower at baseline in the lines without PDCD1LG2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.8, 18.0); signed map (44.8, 19.9). **Vector** length 120, 36.8% of its response variance represented; |z| ≥ 3 in 1,390 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.8 | +11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.8 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.7 | +16.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +12.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.8 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +3.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -4.5 | -8.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.3 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.5 | -3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -8.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | caldesmon 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:134,744,252-134,970,729 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDM, H-CAD, L-CAD, h-CD |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 2 pathways, smallest: Smooth Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05682](https://www.uniprot.org/uniprotkb/Q05682) (Caldesmon):

> Actin- and myosin-binding protein implicated in the regulation of actomyosin interactions in smooth muscle and nonmuscle cells (could act as a bridge between myosin and actin filaments). Stimulates actin binding of tropomyosin which increases the stabilization of actin filament structure. In muscle tissues, inhibits the actomyosin ATPase by binding to F-actin. This inhibition is attenuated by calcium-calmodulin and is potentiated by tropomyosin. Interacts with actin, myosin, two molecules of …

**Summary**, from NCBI Gene [800](https://www.ncbi.nlm.nih.gov/gene/800):

> This gene encodes a calmodulin- and actin-binding protein that plays an essential role in the regulation of smooth muscle and nonmuscle contraction. The conserved domain of this protein possesses the binding activities to Ca(2+)-calmodulin, actin, tropomyosin, myosin, and phospholipids. This protein is a potent inhibitor of the actin-tropomyosin activated myosin MgATPase, and serves as a mediating factor for Ca(2+)-dependent inhibition of smooth muscle contraction. Alternative splicing of this …

**Accessions** — [HGNC:1441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1441) · Entrez [800](https://www.ncbi.nlm.nih.gov/gene/800) · UniProt [Q05682](https://www.uniprot.org/uniprotkb/Q05682) · Ensembl [ENSG00000122786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122786)

## Data

Gene col 4377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4377); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4377]; `tensor/DDL_lfc|DDL_z.npy` [4377]; `embed/gene_vectors.npy` [4377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4377 or target_col == 4377). Every well: [[CALD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
