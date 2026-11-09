---
symbol: "WDR7"
type: "gene"
col: 1657
ensembl_id: "ENSG00000091157"
name: "WD repeat domain 7"
location: "18q21.31"
module: 230
arm: "+"
pooled_cpm: 49.14
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 16
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/230"]
generated_by: "tahoemap"
---

# WDR7

*WD repeat domain 7* — 18q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.50× (z +18.3, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.500× (z -14.3, q 2e-43, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D19]] (+0.76, fdr 7e-06), [[WDR70]] (+0.67, fdr 7e-06), [[DIS3L2]] (+0.64, fdr 7e-06); moves opposite to [[BCL2L2-PABPN1]] (-0.63, fdr 3e-05), [[C14orf28]] (-0.61, fdr 5e-05), [[CCDC168]] (-0.61, fdr 3e-05).
> It is in [[Module 230]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 1 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1657.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.50×** | +18.3 | 0e+00 | 46/47 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.93×** | +15.7 | 0e+00 | 45/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.71×** | +14.6 | 1e-45 | 46/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +9.1 | 2e-17 | 34/47 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +7.6 | 2e-12 | 45/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +6.6 | 4e-09 | 34/47 (hTERT-HPNE, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.14×** | +5.8 | 5e-07 | 43/47 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +5.7 | 9e-07 | 30/48 (A-172, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +5.3 | 6e-06 | 24/47 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +5.0 | 3e-05 | 31/47 (SW 900, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.4 | 6e-04 | 33/47 (LS 180, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.064 | 20/46 (SW480, LS 180, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.064 | 22/47 (NCI-H460, SW48, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.065 | 19/47 (NCI-H2347, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.065 | 19/47 (A498, BT-474, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1657.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.500×** | -14.3 | 2e-43 | 44/47 (A498, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.475×** | -10.8 | 7e-25 | 43/47 (HEC-1-A, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.632×** | -6.7 | 5e-09 | 34/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.635×** | -6.3 | 3e-08 | 30/47 (C32, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.626×** | -6.2 | 6e-08 | 28/46 (SW 900, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.661×** | -6.0 | 2e-07 | 34/47 (HT-29, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.664×** | -6.0 | 2e-07 | 32/47 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.669×** | -5.8 | 4e-07 | 29/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.651×** | -5.8 | 5e-07 | 26/44 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.697×** | -5.1 | 2e-05 | 27/43 (HEC-1-A, C32, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **0.747×** | -4.2 | 0.001 | 28/47 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -4.2 | 0.001 | 26/47 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.741×** | -4.2 | 0.001 | 23/46 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.837× | -3.6 | 0.011 | 25/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.769×** | -3.5 | 0.021 | 19/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.810×** | -3.1 | 0.074 | 20/47 (COLO 205, AN3 CA, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1657. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 86.3 | 4 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.13× (z +11.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -16.1) |
| [[PANC-1 (line)]] | alt | 49.5 | 4 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -13.4) |
| [[A-427 (line)]] | wt | 82.2 | 4 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.09× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.304× (z -12.9) |
| [[C32 (line)]] | wt | 72.6 | 2 | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.28× (z +9.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -14.6) |
| [[LoVo (line)]] | wt | 51.9 | 3 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.46× (z +12.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -15.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.204× (z -15.4) |
| [[SW480 (line)]] | alt | 29.1 | 4 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.60× (z +12.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -11.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.377× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 69.2 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.70× (z +10.7) | [[Auranofin (drug)]] 5 µM 0.253× (z -14.8) |
| [[KATO III (line)]] | alt | 41.1 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.44× (z +11.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.264× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 57.7 | 5 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.75× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 57.5 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.84× (z +14.1) | [[Auranofin (drug)]] 5 µM 0.307× (z -10.5) |
| [[A498 (line)]] | wt | 42.8 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 44.0 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.44× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 61.7 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.50× (z +11.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -10.9) |
| [[HS-578T (line)]] | alt | 63.4 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.02× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -9.6) |
| [[HT-29 (line)]] | alt | 39.2 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -16.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -11.9) |
| [[J82 (line)]] | alt | 60.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.64× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -10.3) |
| [[LS 180 (line)]] | wt | 41.9 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 5.93× (z +12.2) | [[Digitoxin (drug)]] 0.5 µM 0.263× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 61.4 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.04× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.249× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 37.3 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -11.0) |
| [[RKO (line)]] | wt | 72.1 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.55× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -13.6) |
| [[SW1417 (line)]] | alt | 38.3 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.43× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.242× (z -11.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 57.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.82× (z +11.8) | — |
| [[C-33 A (line)]] | alt | 72.1 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.84× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.228× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.298× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 31.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 23.0 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.37× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -8.8) |
| [[Hs 766T (line)]] | wt | 33.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 46.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.69× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 68.2 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.14× (z +9.3) | [[Auranofin (drug)]] 5 µM 0.298× (z -9.8) |
| [[SNU-1 (line)]] | wt | 79.4 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.23× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.288× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.299× (z -9.0) |
| [[A-172 (line)]] | wt | 36.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 30.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.90× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.393× (z -9.3) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 48.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.7) |
| [[A549 (line)]] | wt | 49.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.52× (z +10.5) | — |
| [[CHP-212 (line)]] | wt | 58.9 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0454× (z -14.1) |
| [[H4 (line)]] | wt | 40.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.17× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 51.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.38× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 28.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 42.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.275× (z -10.8) |
| [[SW 900 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -12.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 57.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -9.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.77 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1657), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D19]] | +0.76 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[WDR70]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 | same gene group |
| [[DIS3L2]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CSTPP1]] | +0.63 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[COG2]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[NDUFA8]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[RAD54L2]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[VPS50]] | +0.60 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[STX8]] | +0.60 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[IFTAP]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[CEP162]] | +0.59 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[TTC26]] | +0.59 | +0.43 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L2-PABPN1]] | -0.63 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[C14orf28]] | -0.61 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[CCDC168]] | -0.61 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[MSL1]] | -0.60 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[PLD5P1]] | -0.60 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[CD27-AS1]] | -0.60 | -0.22 / -0.52 | both halves | 6e-04 |  |
| [[ZFC3H1]] | -0.60 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.60 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[TTC28-AS1]] | -0.59 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[C9orf153]] | -0.59 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ZNF460-AS1]] | -0.59 | -0.25 / -0.59 | both halves | 4e-04 |  |
| [[GNAS]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises WDR7's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TBC1D19]] | C | TBC1D19 activity raises WDR7's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without TBC1D19 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 230]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-27.7, -5.0); signed map (-18.9, -24.7). **Vector** length 110, 34.8% of its response variance represented; |z| ≥ 3 in 1,216 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.7 | +5.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +6.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +0.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.7 | +2.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.0 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -16.8 | -14.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -10.5 | -10.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -9.8 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.4 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.31 — chr18:56,651,343-57,029,811 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0541, TRAG |
| Gene groups (HGNC) | WD repeat domain containing; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4E6](https://www.uniprot.org/uniprotkb/Q9Y4E6) (WD repeat-containing protein 7):

> As part of the RAVE complex it may control the assembly of the proton-pumping V-ATPase complex and therefore regulate organelle acidification.

**Summary**, from NCBI Gene [23335](https://www.ncbi.nlm.nih.gov/gene/23335):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD) that may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. The encoded protein forms the beta subunit of rabconnectin-3 and binds directly …

**Accessions** — [HGNC:13490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13490) · Entrez [23335](https://www.ncbi.nlm.nih.gov/gene/23335) · UniProt [Q9Y4E6](https://www.uniprot.org/uniprotkb/Q9Y4E6) · Ensembl [ENSG00000091157](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091157)

## Data

Gene col 1657: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1657); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1657, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1657]; `tensor/DDL_lfc|DDL_z.npy` [1657]; `embed/gene_vectors.npy` [1657]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1657 or target_col == 1657). Every well: [[WDR7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
