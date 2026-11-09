---
symbol: "MFSD12"
type: "gene"
col: 8417
ensembl_id: "ENSG00000161091"
name: "major facilitator superfamily domain containing 12"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 42.06
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MFSD12

*major facilitator superfamily domain containing 12* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.92× (z +15.9, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.768× (z -5.5, q 2e-05, down in 27 of 46 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.387× (z -5.2, q 5e-05, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAFK]] (+0.69, fdr 7e-06), [[GDI1]] (+0.61, fdr 1e-05), [[DVL1]] (+0.60, fdr 1e-04); moves opposite to [[NNT]] (-0.56, fdr 3e-05), [[PRIMPOL]] (-0.56, fdr 3e-05), [[PGAP4]] (-0.56, fdr 3e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8417.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.92×** | +15.9 | 0e+00 | 41/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.59×** | +14.1 | 1e-42 | 41/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +13.6 | 7e-40 | 37/43 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.35×** | +12.6 | 3e-34 | 39/46 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +12.6 | 4e-34 | 31/35 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +9.9 | 5e-21 | 29/39 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.2 | 2e-05 | 26/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.1 | 2e-05 | 26/46 (SW480, Hs 766T, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +5.0 | 3e-05 | 33/44 (HCT15, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.55×** | +4.6 | 2e-04 | 21/46 (RPMI-7951, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.36×** | +4.6 | 2e-04 | 24/45 (NCI-H460, C32, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.001 | 20/46 (SW480, KATO III, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.003 | 18/46 (NCI-H460, LOX-IMVI, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.30×** | +3.9 | 0.005 | 20/44 (Panc 03.27, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.007 | 19/45 (HEC-1-A, H4, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.014 | 14/46 (RKO, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.018 | 14/45 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.021 | 16/45 (SHP-77, SW 1271, …) | two highest doses | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.056 | 11/46 (RPMI-7951, C32, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.071 | 4/46 (KATO III, LOX-IMVI, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8417.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.768×** | -5.5 | 2e-05 | 27/46 (SK-MEL-2, A-172, …) | rises with dose | low cells (technical?); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.387×** | -5.2 | 5e-05 | 23/45 (NCI-H460, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -4.1 | 0.009 | 19/46 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.485×** | -4.0 | 0.009 | 22/47 (A-427, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -3.7 | 0.025 | 19/45 (NCI-H23, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.791×** | -3.5 | 0.050 | 13/46 (NCI-H460, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.798×** | -3.3 | 0.069 | 13/46 (AsPC-1, LS 180, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.801× | -3.1 | 0.12 | 15/45 (NCI-H23, A-172, …) | top dose only |  |
| [[Valdecoxib (drug)]] 0.05 µM |  | 0.813× | -3.1 | 0.14 | 13/45 (SNU-423, CHP-212, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8417. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.3 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.02× (z +19.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 4.39× (z +13.8) | — |
| [[HOP62 (line)]] | alt | 21.0 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.15× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 208 | 3 (3 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +11.6) ⚠ cell-cycle shift, explains ~82% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 25.3 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.14× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 19.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.95× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -8.5) ⚠ cell-cycle shift, explains ~58% of this change |
| [[SHP-77 (line)]] | alt | 30.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.3× (z +17.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 22.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.05× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 35.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.23× (z +8.7) | — |
| [[KATO III (line)]] | alt | 25.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 33.8 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.27× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 22.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.84× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 19.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.08× (z +10.3) | — |
| [[RKO (line)]] | wt | 30.0 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.68× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -8.8) |
| [[SW1417 (line)]] | alt | 22.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.09× (z +9.7) | — |
| [[A-172 (line)]] | wt | 73.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -10.9) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A-427 (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -13.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[C32 (line)]] | wt | 199 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.97× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 14.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.24× (z +8.8) | — |
| [[LoVo (line)]] | wt | 19.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.20× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.5) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[NCI-H23 (line)]] | alt | 40.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.6) ⚠ cell-cycle shift, explains ~58% of this change |
| [[SW 900 (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.40× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.31 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.81 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8417), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAFK]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[GDI1]] | +0.61 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[DVL1]] | +0.60 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[GALNS]] | +0.60 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[PPP1R12C]] | +0.59 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[RMC1]] | +0.59 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[DLGAP4]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.59 | +0.37 / +0.38 | both halves | 8e-05 |  |
| [[PEDS1]] | +0.58 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[CADM4]] | +0.57 | +0.32 / +0.44 | both halves | 2e-04 |  |
| [[AMDHD2]] | +0.57 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[FBRSL1]] | +0.57 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NNT]] | -0.56 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PRIMPOL]] | -0.56 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[PGAP4]] | -0.56 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[TCEANC2]] | -0.56 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[TMEM68]] | -0.54 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[ATP5PB]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ANGEL2]] | -0.54 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[VBP1]] | -0.53 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[TDRD3]] | -0.53 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[RWDD2B]] | -0.53 | -0.27 / -0.27 | both halves | 3e-04 |  |
| [[ITPKB]] | -0.53 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[FAS]] | -0.52 | -0.34 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.531). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (13.2, -2.7); signed map (-20.1, 25.2). **Vector** length 102, 25.5% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.9 | +15.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.3 | +14.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.5 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +13.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.8 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.4 | -5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -3.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | +1.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | major facilitator superfamily domain containing 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,538,261-3,574,290 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC20700, PP3501, SLC59B1; previously C19orf28 |
| Gene groups (HGNC) | Solute carrier family 59 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NUT3](https://www.uniprot.org/uniprotkb/Q6NUT3) (Major facilitator superfamily domain-containing protein 12):

> Transporter that mediates the import of cysteine into melanosomes, thereby regulating skin pigmentation. In melanosomes, cysteine import is required both for normal levels of cystine, the oxidized dimer of cysteine, and provide cysteine for the production of the cysteinyldopas used in pheomelanin synthesis, thereby regulating skin pigmentation. Also catalyzes import of cysteine into lysosomes in non-pigmented cells, regulating lysosomal cystine and cysteine storage, which is essential for redox …

**Summary**, from NCBI Gene [126321](https://www.ncbi.nlm.nih.gov/gene/126321):

> Enables cysteine transmembrane transporter activity. Involved in cysteine transmembrane transport; pigment metabolic process involved in pigmentation; and regulation of melanin biosynthetic process. Located in lysosome and melanosome. Part of late endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28299) · Entrez [126321](https://www.ncbi.nlm.nih.gov/gene/126321) · UniProt [Q6NUT3](https://www.uniprot.org/uniprotkb/Q6NUT3) · Ensembl [ENSG00000161091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161091)

## Data

Gene col 8417: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8417); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8417, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8417]; `tensor/DDL_lfc|DDL_z.npy` [8417]; `embed/gene_vectors.npy` [8417]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8417 or target_col == 8417). Every well: [[MFSD12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
