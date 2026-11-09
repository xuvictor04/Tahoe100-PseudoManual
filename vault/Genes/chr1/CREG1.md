---
symbol: "CREG1"
type: "gene"
col: 6688
ensembl_id: "ENSG00000143162"
name: "cellular repressor of E1A stimulated genes 1"
location: "1q24.2"
module: 29
arm: "+"
pooled_cpm: 27.51
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CREG1

*cellular repressor of E1A stimulated genes 1* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.77× (z +19.1, q 0e+00, up in 39 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.48× (z +17.0, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.805× (z -3.9, q 0.046, down in 16 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (LoVo 0.322×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.257×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMP2]] (+0.69, fdr 7e-06), [[FAM210B]] (+0.68, fdr 7e-06), [[PPT1]] (+0.66, fdr 1e-05); moves opposite to [[MTG2]] (-0.65, fdr 1e-05), [[UBE2J2]] (-0.65, fdr 7e-06), [[CCDC137]] (-0.64, fdr 4e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6688.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +19.1 | 0e+00 | 39/41 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +18.3 | 0e+00 | 29/32 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.48×** | +17.0 | 0e+00 | 42/46 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +16.7 | 0e+00 | 44/46 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.32×** | +15.7 | 0e+00 | 42/45 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +11.2 | 6e-27 | 30/36 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +10.7 | 5e-25 | 29/45 (A498, HT-29, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +10.6 | 2e-24 | 36/46 (HOP62, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +10.5 | 7e-24 | 34/46 (SW 900, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +9.0 | 8e-18 | 36/46 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +7.5 | 4e-12 | 28/45 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.38×** | +5.8 | 2e-07 | 22/45 (HEC-1-A, HOP62, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +5.7 | 5e-07 | 24/43 (AsPC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.35×** | +5.4 | 2e-06 | 17/40 (MIA PaCa-2, J82, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +5.3 | 4e-06 | 21/46 (PANC-1, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 4e-05 | 17/46 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.026 | 7/42 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.026 | 11/45 (A498, SNU-423, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.073 | 10/46 (HepG2/C3A, KATO III, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | 1.16× | +2.9 | 0.073 | 6/47 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +2.9 | 0.078 | 7/46 (KATO III, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6688.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 1 line (LoVo 0.322×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.257×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.805×** | -3.9 | 0.046 | 16/45 (NCI-H460, H4, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.818×** | -3.8 | 0.046 | 13/45 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 0.832× | -3.4 | 0.11 | 13/44 (SHP-77, NCI-H23, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.833× | -3.2 | 0.18 | 14/45 (SW480, LS 180, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.732× | -3.1 | 0.26 | 7/44 (A-427, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6688. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 20.8 | 6 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.85× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 79.7 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +16.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 9.91 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.79× (z +13.6) | — |
| [[A498 (line)]] | wt | 50.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.4) | — |
| [[J82 (line)]] | alt | 34.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +11.7) | — |
| [[HEC-1-A (line)]] | alt | 41.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +10.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 25.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +11.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.322× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 25.4 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 3.94× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 26.6 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.42× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 26.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.28× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 23.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.32× (z +8.7) | — |
| [[SW480 (line)]] | alt | 35.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +12.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 28.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +9.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 43.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +8.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 31.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 40.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +8.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 18.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6688), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMP2]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[FAM210B]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[PPT1]] | +0.66 | +0.56 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[ITM2C]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[SCARB2]] | +0.64 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[CLSTN1]] | +0.64 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ERMP1]] | +0.63 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TWSG1]] | +0.62 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[CRTAP]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[GNS]] | +0.61 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[LTA4H]] | +0.61 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[ABRAXAS1]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTG2]] | -0.65 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[UBE2J2]] | -0.65 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[CCDC137]] | -0.64 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[UBE2CP5]] | -0.60 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[MEF2B]] | -0.60 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[WAPL]] | -0.59 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[ZNF75A]] | -0.58 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[CLCF1]] | -0.58 | -0.49 / -0.60 | both halves | 2e-05 |  |
| [[MRPL45P2]] | -0.58 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[KCNJ14]] | -0.57 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[BMS1P4-1]] | -0.57 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[AFG3L1P]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-20.5, -19.5); signed map (-28.7, -37.3). **Vector** length 86.0, 18.4% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +19.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.7 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +18.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | +0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | cellular repressor of E1A stimulated genes 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:167,529,117-167,553,805 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CREG |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O75629](https://www.uniprot.org/uniprotkb/O75629) (Protein CREG1):

> May contribute to the transcriptional control of cell growth and differentiation. Antagonizes transcriptional activation and cellular transformation by the adenovirus E1A protein. The transcriptional control activity of cell growth requires interaction with IGF2R.

**Summary**, from NCBI Gene [8804](https://www.ncbi.nlm.nih.gov/gene/8804):

> The adenovirus E1A protein both activates and represses gene expression to promote cellular proliferation and inhibit differentiation. The protein encoded by this gene antagonizes transcriptional activation and cellular transformation by E1A. This protein shares limited sequence similarity with E1A and binds both the general transcription factor TBP and the tumor suppressor pRb in vitro. This gene may contribute to the transcriptional control of cell growth and differentiation. [provided by …

**Accessions** — [HGNC:2351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2351) · Entrez [8804](https://www.ncbi.nlm.nih.gov/gene/8804) · UniProt [O75629](https://www.uniprot.org/uniprotkb/O75629) · Ensembl [ENSG00000143162](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143162)

## Data

Gene col 6688: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6688); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6688, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6688]; `tensor/DDL_lfc|DDL_z.npy` [6688]; `embed/gene_vectors.npy` [6688]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6688 or target_col == 6688). Every well: [[CREG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CREG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
