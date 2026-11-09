---
symbol: "SLC20A2"
type: "gene"
col: 9672
ensembl_id: "ENSG00000168575"
name: "solute carrier family 20 member 2"
location: "8p11.21"
module: 30
arm: "-"
pooled_cpm: 128.94
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# SLC20A2

*solute carrier family 20 member 2* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +8.8, q 9e-16, up in 30 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.692× (z -7.4, q 1e-10, down in 35 of 47 measured lines) ⚠ transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.720× (z -6.6, q 1e-08, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRNT1]] (+0.63, fdr 1e-05), [[SLFNL1-AS1]] (+0.61, fdr 1e-05), [[ZNF124]] (+0.59, fdr 3e-05); moves opposite to [[TMEM185A]] (-0.68, fdr 7e-06), [[PRKAB2]] (-0.63, fdr 1e-05), [[CAT]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HOOK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9672.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +8.8 | 9e-16 | 30/49 (Hs 766T, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +7.5 | 2e-11 | 34/48 (AsPC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +6.8 | 2e-09 | 36/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +4.9 | 1e-04 | 25/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | 1.37× | +3.3 | 0.11 | 17/48 (RKO, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +3.3 | 0.11 | 19/48 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.17× | +3.0 | 0.19 | 15/47 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.16× | +3.0 | 0.19 | 19/48 (NCI-H1573, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9672.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.692×** | -7.4 | 1e-10 | 35/47 (SW1417, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.720×** | -6.6 | 1e-08 | 25/48 (SW1417, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.746×** | -5.9 | 8e-07 | 28/48 (HT-29, SW1417, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.815×** | -5.8 | 9e-07 | 28/48 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.757×** | -5.6 | 3e-06 | 29/48 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[NG25 (drug)]] 5 µM |  | **0.590×** | -5.5 | 3e-06 | 41/47 (RKO, C32, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.782×** | -4.9 | 7e-05 | 28/48 (BT-474, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | **0.778×** | -4.8 | 9e-05 | 24/44 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.813×** | -4.2 | 0.002 | 23/48 (C32, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **0.809×** | -4.1 | 0.002 | 23/47 (SHP-77, SNU-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.812×** | -4.0 | 0.003 | 24/48 (AN3 CA, A-427, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.829×** | -3.8 | 0.008 | 23/48 (HT-29, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | 0.837× | -3.6 | 0.015 | 24/49 (RKO, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | 0.839× | -3.3 | 0.043 | 20/45 (SW48, KATO III, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9672. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 134 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +23.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 170 | 5 (2 ⚠) | 1 (1 ⚠) | [[Daptomycin (drug)]] 5 µM 3.68× (z +13.2) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 2.32× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 148 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +11.9) | [[Adagrasib (drug)]] 0.05 µM 0.665× (z -16.7) ⚠ position not correctable · without an alert: [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.460× (z -8.6) |
| [[SW1417 (line)]] | alt | 367 | 0 | 4 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.383× (z -9.9) ⚠ transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.411× (z -9.2) |
| [[HT-29 (line)]] | alt | 212 | 0 | 3 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.339× (z -9.1) ⚠ transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.345× (z -8.9) |
| [[A-172 (line)]] | wt | 78.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.14× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 123 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +14.4) | — |
| [[Hs 766T (line)]] | wt | 68.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +15.5) | — |
| [[NCI-H2030 (line)]] | alt | 78.9 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.39× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[NCI-H460 (line)]] | wt | 73.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +13.8) | — |
| [[SHP-77 (line)]] | alt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.477× (z -9.2) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A498 (line)]] | wt | 65.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 95.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0851× (z -15.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[C32 (line)]] | wt | 62.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 269 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 311 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.431× (z -8.6) ⚠ transcription drop |
| [[LS 180 (line)]] | wt | 183 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[NCI-H1792 (line)]] | alt | 90.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +12.3) | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0512× (z -14.0) |
| [[RKO (line)]] | wt | 230 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0586× (z -36.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 98.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 95.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[SNU-1 (line)]] | wt | 96.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.341× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[SNU-423 (line)]] | alt | 54.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.9) | — |
| [[SW48 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[A549 (line)]] | wt | 95.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 154 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 93.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 184 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 107 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 94.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 150 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 199 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9672), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRNT1]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ZNF124]] | +0.59 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[KCNJ14]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CRK]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[MIRLET7A1HG]] | +0.57 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[TEAD4]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[PKP4]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[HCG18]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[TLNRD1]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SUSD1]] | +0.56 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[WDR4]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185A]] | -0.68 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[PRKAB2]] | -0.63 | -0.72 / -0.51 | both halves | 1e-05 |  |
| [[CAT]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[GALT]] | -0.59 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[ZNF14]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[ANKMY2]] | -0.59 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[SKIC3]] | -0.58 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[FBXO7]] | -0.58 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[USP30]] | -0.58 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[NPHP1]] | -0.57 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[ORC4]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PJA2]] | -0.57 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOOK1]] | B | HOOK1 activity raises SLC20A2's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 1.57× lower at baseline in the lines without HOOK1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[CASC19]] | B | CASC19 activity raises SLC20A2's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 1.60× lower at baseline in the lines without CASC19 | 0.060 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[ABL1]] | B | ABL1 activity raises SLC20A2's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 2.5% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **-** arm (projection on the module's main direction -0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (3.3, -8.9); signed map (14.9, -0.1). **Vector** length 133, 39.4% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.1 | +6.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.0 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +3.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.4 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +2.1 |
| fall | [[NG25 (drug)]] 5 µM |  | -5.1 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.1 | -4.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -5.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 20 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:42,416,475-42,541,926 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PiT-2, Glvr-2, Ram-1, PIT2; previously MLVAR, GLVR2 |
| Gene groups (HGNC) | Solute carrier family 20 |
| Reactome | 6 pathways, smallest: Sodium-coupled phosphate cotransporters; SLC-mediated transport of inorganic anions; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08357](https://www.uniprot.org/uniprotkb/Q08357) (Sodium-dependent phosphate transporter 2):

> Sodium-phosphate symporter which preferentially transports the monovalent form of phosphate with a stoichiometry of two sodium ions per phosphate ion. Plays a critical role in the determination of bone quality and strength by providing phosphate for bone mineralization (By similarity). Required to maintain normal cerebrospinal fluid phosphate levels (By similarity). Mediates phosphate-induced calcification of vascular smooth muscle cells (VCMCs) and can functionally compensate for loss of …

**Summary**, from NCBI Gene [6575](https://www.ncbi.nlm.nih.gov/gene/6575):

> This gene encodes a member of the inorganic phosphate transporter family. The encoded protein is a type 3 sodium-dependent phosphate symporter that plays an important role in phosphate homeostasis by mediating cellular phosphate uptake. The encoded protein also confers susceptibility to viral infection as a gamma-retroviral receptor. Mutations in this gene may play a role in familial idiopathic basal ganglia calcification. Alternatively spliced transcript variants encoding multiple isoforms …

**Accessions** — [HGNC:10947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10947) · Entrez [6575](https://www.ncbi.nlm.nih.gov/gene/6575) · UniProt [Q08357](https://www.uniprot.org/uniprotkb/Q08357) · Ensembl [ENSG00000168575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168575)

## Data

Gene col 9672: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9672); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9672, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9672]; `tensor/DDL_lfc|DDL_z.npy` [9672]; `embed/gene_vectors.npy` [9672]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9672 or target_col == 9672). Every well: [[SLC20A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC20A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
