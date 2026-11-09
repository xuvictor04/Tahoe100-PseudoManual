---
symbol: "EIF3B"
type: "gene"
col: 2736
ensembl_id: "ENSG00000106263"
name: "eukaryotic translation initiation factor 3 subunit B"
location: "7p22.3"
module: 33
arm: "+"
pooled_cpm: 128.53
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# EIF3B

*eukaryotic translation initiation factor 3 subunit B* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.47× (z +12.5, q 4e-33, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.806× (z -5.9, q 3e-06, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[URB1]] (+0.77, fdr 7e-06), [[DDX54]] (+0.77, fdr 7e-06), [[WDR3]] (+0.73, fdr 7e-06); moves opposite to [[BTN2A2]] (-0.61, fdr 9e-06), [[RO60]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2736.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.47×** | +12.5 | 4e-33 | 47/49 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.19×** | +11.6 | 7e-29 | 44/48 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.76×** | +10.8 | 6e-25 | 41/48 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.72×** | +10.5 | 2e-23 | 41/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +8.3 | 9e-15 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.22×** | +8.0 | 1e-13 | 29/38 (LoVo, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +7.1 | 8e-11 | 38/48 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.40×** | +6.5 | 6e-09 | 34/48 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.40×** | +6.3 | 2e-08 | 36/47 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +5.7 | 6e-07 | 33/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +5.5 | 2e-06 | 27/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.58×** | +4.6 | 2e-04 | 33/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.002 | 30/48 (NCI-H460, CFPAC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.003 | 24/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.9 | 0.004 | 23/47 (HT-29, Hs 766T, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.006 | 26/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.6 | 0.010 | 17/49 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.019 | 18/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 1.18× | +3.1 | 0.047 | 13/48 (MIA PaCa-2, C-33 A, …) | top dose only | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.34×** | +2.9 | 0.082 | 14/48 (PANC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +2.9 | 0.082 | 19/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2736.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.806×** | -5.9 | 3e-06 | 29/48 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.772×** | -4.8 | 5e-04 | 29/47 (AsPC-1, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.789×** | -4.6 | 8e-04 | 28/49 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.790×** | -4.5 | 8e-04 | 25/48 (LoVo, KATO III, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.814×** | -4.0 | 0.008 | 24/47 (LoVo, C32, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.825×** | -3.7 | 0.021 | 19/47 (LS 180, SW48, …) | two highest doses | low cells (technical?) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.829×** | -3.6 | 0.026 | 21/49 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.840× | -3.2 | 0.090 | 18/48 (LoVo, LOX-IMVI, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.848× | -3.2 | 0.095 | 17/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.846× | -3.1 | 0.11 | 15/47 (HepG2/C3A, LoVo, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 117 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +14.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.13× (z +11.2) | — |
| [[SW480 (line)]] | alt | 163 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +13.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.28× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 166 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +15.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.64× (z +14.0) | — |
| [[NCI-H460 (line)]] | wt | 116 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.36× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.70× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 85.3 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.80× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 6.41× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 99.9 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.90× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 189 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.34× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 36.3 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.18× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 284 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 171 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +12.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.94× (z +9.1) | — |
| [[A-172 (line)]] | wt | 68.6 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.67× (z +9.2) | [[Harringtonine (drug)]] 5 µM 0.366× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 60.1 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.1) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[KATO III (line)]] | alt | 148 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.56× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 94.6 | 2 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 5.57× (z +9.0) | — |
| [[A-427 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 209 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 124 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.76× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 70.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.5× (z +9.7) | — |
| [[H4 (line)]] | wt | 247 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.13× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 109 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.20× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.26× (z +8.7) ⚠ unreliable plate only | — |
| [[NCI-H23 (line)]] | alt | 158 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 1.99× (z +8.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 147 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.06× (z +11.3) | — |
| [[SNU-1 (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 161 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.15× (z +8.6) | — |
| [[SW48 (line)]] | wt | 218 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 5.06× (z +15.8) | — |
| [[A498 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 96.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 120 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 107 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 81.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 125 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 118 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[URB1]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 | same gene group |
| [[DDX54]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 | STRING 459 |
| [[WDR3]] | +0.73 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[NSUN2]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[RNPS1]] | +0.71 | +0.76 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1 |
| [[TOMM40]] | +0.70 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[DHX33]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[MDN1]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[POLR3H]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[PDCD11]] | +0.68 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[KLHDC4]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN2A2]] | -0.61 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[RO60]] | -0.56 | -0.56 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.3, -38.3); signed map (-5.9, -51.0). **Vector** length 98.4, 32.2% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.53 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.53 to 10); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.61 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +6.4 | +11.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +7.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +12.5 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.9 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | +0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -2.9 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | +3.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:2,354,086-2,380,745 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRT1; previously EIF3S9 |
| Gene groups (HGNC) | RNA binding motif containing; Eukaryotic translation initiation factor 3 complex subunits; Armadillo like helical domain containing |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P55884](https://www.uniprot.org/uniprotkb/P55884) (Eukaryotic translation initiation factor 3 subunit B):

> RNA-binding component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG recognition. The eIF-3 complex is also required for …

**Summary**, from NCBI Gene [8662](https://www.ncbi.nlm.nih.gov/gene/8662):

> Enables RNA binding activity. Contributes to translation initiation factor activity. Involved in several processes, including IRES-dependent viral translational initiation; translational initiation; and viral translational termination-reinitiation. Located in cytoplasmic stress granule and cytosol. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3280) · Entrez [8662](https://www.ncbi.nlm.nih.gov/gene/8662) · UniProt [P55884](https://www.uniprot.org/uniprotkb/P55884) · Ensembl [ENSG00000106263](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106263)

## Data

Gene col 2736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2736); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2736]; `tensor/DDL_lfc|DDL_z.npy` [2736]; `embed/gene_vectors.npy` [2736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2736 or target_col == 2736). Every well: [[EIF3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
