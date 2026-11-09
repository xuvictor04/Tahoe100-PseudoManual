---
symbol: "MYNN"
type: "gene"
col: 1420
ensembl_id: "ENSG00000085274"
name: "myoneurin"
location: "3q26.2"
module: 41
arm: "+"
pooled_cpm: 45.83
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# MYNN

*myoneurin* — 3q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.88× (z +15.5, q 0e+00, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.415× (z -15.9, q 0e+00, down in 43 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.738× (z -5.5, q 6e-06, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIL4]] (+0.67, fdr 9e-06), [[SPTY2D1]] (+0.67, fdr 7e-06), [[UFL1]] (+0.67, fdr 1e-05); moves opposite to [[TTL]] (-0.62, fdr 1e-05), [[APP]] (-0.57, fdr 1e-05), [[PTK2]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOXA11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +15.5 | 0e+00 | 39/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +10.7 | 4e-24 | 41/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +10.3 | 8e-23 | 40/49 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +9.5 | 4e-19 | 39/47 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +6.6 | 4e-09 | 31/48 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +5.9 | 4e-07 | 29/48 (NCI-H460, BT-474, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +5.8 | 7e-07 | 28/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.4 | 6e-06 | 29/47 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.4 | 7e-04 | 22/48 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.041 | 16/48 (NCI-H2030, SNU-423, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.18× | +3.0 | 0.12 | 16/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1420.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.415×** | -15.9 | 0e+00 | 43/46 (C-33 A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.412×** | -15.4 | 0e+00 | 36/40 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.613×** | -8.2 | 6e-14 | 28/44 (SK-MEL-2, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.738×** | -5.5 | 6e-06 | 28/48 (SW1417, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -5.1 | 5e-05 | 31/48 (hTERT-HPNE, H4, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -4.7 | 3e-04 | 24/48 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.779×** | -4.5 | 6e-04 | 23/48 (SW1417, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.790×** | -4.1 | 0.003 | 21/48 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.845× | -4.0 | 0.004 | 23/48 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.802×** | -4.0 | 0.004 | 22/48 (A498, HT-29, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.818×** | -3.6 | 0.015 | 19/47 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.819×** | -3.6 | 0.015 | 18/48 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.822×** | -3.5 | 0.017 | 19/48 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.059 | 15/48 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.788×** | -3.1 | 0.080 | 15/48 (CHP-212, A549, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.844× | -3.1 | 0.080 | 13/48 (PANC-1, AN3 CA, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 51.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.5) | — |
| [[NCI-H460 (line)]] | wt | 26.6 | 5 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.54× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.0824× (z -24.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 55.2 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -10.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 44.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +11.5) | — |
| [[KATO III (line)]] | alt | 55.2 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -14.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 45.3 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.15× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.0741× (z -20.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 61.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -11.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 44.9 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -11.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 40.0 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -14.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 68.3 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -9.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 76.3 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0469× (z -21.7) ⚠ toxic; cell-cycle shift, explains ~75% of this change |
| [[HEC-1-A (line)]] | alt | 46.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 48.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -24.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 52.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -11.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 47.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -11.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 41.2 | 0 | 2 (2 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.122× (z -9.7) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 44.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -16.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 41.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -9.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 64.3 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0854× (z -12.7) ⚠ toxic |
| [[J82 (line)]] | alt | 55.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 42.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 40.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -17.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 47.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 58.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -12.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 40.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -16.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 57.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -12.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 58.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -11.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -13.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -12.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 49.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -9.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 53.1 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.158× (z -8.9) |
| [[HCT15 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0849× (z -14.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 34.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 48.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.2) | — |
| [[LoVo (line)]] | wt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -12.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -11.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 45.1 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.5 µM 0.0764× (z -8.5) |
| [[COLO 205 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIL4]] | +0.67 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[SPTY2D1]] | +0.67 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[UFL1]] | +0.67 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[LYSMD3]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[KBTBD7]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 | same gene group |
| [[SPOP]] | +0.64 | +0.58 / +0.57 | both halves | 8e-06 | same gene group |
| [[GOSR1]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TCEAL8]] | +0.61 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[BNIP1]] | +0.61 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[VIRMA]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[YIPF5]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[COG1]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTL]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[APP]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[PTK2]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.57 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[DIAPH1]] | -0.56 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[MFSD14B]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[LRP8]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[HACD3]] | -0.54 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[NCK2]] | -0.54 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[HIGD1A]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[TSPAN17]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[MAST2]] | -0.52 | -0.56 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA11]] | B | HOXA11 activity lowers MYNN's level | lines that do not express HOXA11 (29) vs lines expressing it (21) | 1.12× higher at baseline in the lines without HOXA11 | 0.038 | ⚠ within organs, on part of the lines; also absent: HOXA9, IL20RA, PRSS3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.712). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.4, -38.6); signed map (-51.9, 15.7). **Vector** length 77.5, 17.7% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.52 to 8); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | -0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.2 | -0.1 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.2 | +0.2 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.2 | -0.2 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | +1.1 | +1.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~75% of this change | -3.5 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | +0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -0.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -15.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | myoneurin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.2 — chr3:169,773,396-169,789,716 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SBBIZ1, ZBTB31, ZNF902 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

UniProt [Q9NPC7](https://www.uniprot.org/uniprotkb/Q9NPC7) carries no function annotation.

**Summary**, from NCBI Gene [55892](https://www.ncbi.nlm.nih.gov/gene/55892):

> This gene encodes a member of the BTB/POZ and zinc finger domain-containing protein family that are involved in the control of gene expression. Alternative splicing results in multiple transcript variants and a pseudogene has been identified on chromosome 14. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:14955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14955) · Entrez [55892](https://www.ncbi.nlm.nih.gov/gene/55892) · UniProt [Q9NPC7](https://www.uniprot.org/uniprotkb/Q9NPC7) · Ensembl [ENSG00000085274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085274)

## Data

Gene col 1420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1420); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1420]; `tensor/DDL_lfc|DDL_z.npy` [1420]; `embed/gene_vectors.npy` [1420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1420 or target_col == 1420). Every well: [[MYNN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYNN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
