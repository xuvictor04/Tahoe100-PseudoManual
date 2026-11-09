---
symbol: "GRK4"
type: "gene"
col: 4610
ensembl_id: "ENSG00000125388"
name: "G protein-coupled receptor kinase 4"
location: "4p16.3"
module: 26
arm: "+"
pooled_cpm: 6.78
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# GRK4

*G protein-coupled receptor kinase 4* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.71× (z +26.1, q 0e+00, up in 41 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.719× (z -3.9, q 0.050, down in 16 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.713× (z -3.5, q 0.077, down in 14 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAVIN4]] (+0.74, fdr 7e-06), [[DNAH10]] (+0.74, fdr 7e-06), [[RNF32]] (+0.72, fdr 1e-05); moves opposite to [[L2HGDH]] (-0.62, fdr 2e-04), [[DPY30]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4610.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.71×** | +26.1 | 0e+00 | 41/41 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.49×** | +15.4 | 0e+00 | 35/43 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.72×** | +11.9 | 2e-30 | 34/42 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +11.0 | 4e-26 | 11/15 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.52×** | +11.0 | 5e-26 | 19/28 (SW 900, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +10.1 | 8e-22 | 32/40 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +9.7 | 4e-20 | 39/47 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.22×** | +9.5 | 2e-19 | 39/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.75×** | +9.4 | 2e-19 | 31/47 (HOP62, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.18×** | +9.3 | 1e-18 | 31/45 (HOP62, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.17×** | +8.1 | 3e-14 | 29/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +6.8 | 4e-10 | 25/47 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +6.2 | 2e-08 | 24/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +5.9 | 2e-07 | 12/34 (CFPAC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.72×** | +5.6 | 6e-07 | 21/42 (KATO III, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.5 | 1e-06 | 22/43 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +4.2 | 7e-04 | 10/44 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.002 | 13/46 (NCI-H1573, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4610.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.719×** | -3.9 | 0.050 | 16/41 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.713×** | -3.5 | 0.077 | 14/46 (NCI-H23, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.571×** | -3.5 | 0.077 | 12/39 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.718×** | -3.5 | 0.077 | 16/45 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.757× | -3.3 | 0.10 | 11/47 (A-172, SHP-77, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.759× | -3.3 | 0.10 | 12/46 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 7.65 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +19.2) | — |
| [[NCI-H1573 (line)]] | alt | 3.79 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 7.82 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +10.3) | [[Docetaxel (drug)]] 0.05 µM 0.0897× (z -10.9) ⚠ transcription drop |
| [[NCI-H460 (line)]] | wt | 5.92 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.12× (z +14.7) | — |
| [[A498 (line)]] | wt | 6.94 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +16.4) | — |
| [[CFPAC-1 (line)]] | alt | 5.60 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +14.8) | — |
| [[HEC-1-A (line)]] | alt | 13.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -9.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 5.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +11.7) | — |
| [[LOX-IMVI (line)]] | wt | 2.79 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.0× (z +12.4) | — |
| [[A-172 (line)]] | wt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +13.2) | — |
| [[A549 (line)]] | wt | 2.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 9.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.22× (z +12.1) | — |
| [[C-33 A (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +8.6) | — |
| [[C32 (line)]] | wt | 3.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.30× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 4.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 5.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.73× (z +8.5) | — |
| [[J82 (line)]] | alt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 4.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.31× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 6.96 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.50× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 4.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +11.5) | — |
| [[RKO (line)]] | wt | 8.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.67× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 6.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.04× (z +12.4) | — |
| [[SW 900 (line)]] | alt | 4.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.32× (z +8.6) | — |
| [[SW480 (line)]] | alt | 5.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.41× (z +12.6) | — |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAVIN4]] | +0.74 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[DNAH10]] | +0.74 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[RNF32]] | +0.72 | +0.79 / +0.50 | both halves | 1e-05 |  |
| [[HCG17]] | +0.72 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[PKD1L1]] | +0.71 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[GPR137]] | +0.71 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[NEB]] | +0.71 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[MZF1-AS1]] | +0.70 | +0.81 / +0.46 | both halves | 2e-05 |  |
| [[SAXO1]] | +0.70 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[LINC01135]] | +0.70 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[NUP210L]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[LINC02646]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L2HGDH]] | -0.62 | -0.64 / -0.30 | both halves | 2e-04 |  |
| [[DPY30]] | -0.60 | -0.61 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GRK4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DDR2]] | B | DDR2 activity raises GRK4's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.66× lower at baseline in the lines without DDR2 | 0.017 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[RIMS2]] | B | RIMS2 activity raises GRK4's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 1.26× lower at baseline in the lines without RIMS2 | 0.048 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[LINC00667]] | B | LINC00667 activity lowers GRK4's level | lines that do not express LINC00667 (6) vs lines expressing it (44) | 2.46× higher at baseline in the lines without LINC00667 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with ZFHX3; also absent: PTPRH, SOCS3; its own permutation p |
| [[LINC00907]] | C | LINC00907 activity raises GRK4's level | lines that do not express LINC00907 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without LINC00907 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAH6, ABHD12B, ESRRB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (30.8, -8.3); signed map (23.2, 8.5). **Vector** length 66.1, 10.7% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +26.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +11.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +9.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +6.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.8 | +1.9 |
| fall | [[NG25 (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.0 | +9.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:2,963,571-3,040,760 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GPRK4; previously GPRK2L |
| Gene groups (HGNC) | G protein-coupled receptor kinase family |
| Reactome | 4 pathways, smallest: Inactivation, recovery and regulation of the phototransduction cascade; The phototransduction cascade; Visual phototransduction |
| Matched by | ensembl_id |

**Function**, from UniProt [P32298](https://www.uniprot.org/uniprotkb/P32298) (G protein-coupled receptor kinase 4):

> Specifically phosphorylates the activated forms of G protein-coupled receptors, such as ADRB2, DRD1 and DRD3. Such receptor phosphorylation initiates beta-arrestin-mediated receptor internalization, and signaling events leading to their desensitization. Mediates phosphorylation of DRD1 in the absence of dopamine activation, resulting in constitutive desensitization.; [Isoform 1]: Phosphorylates rhodopsin and its activity is inhibited by calmodulin.; [Isoform 2]: In contrast to isoform 1, does …

**Summary**, from NCBI Gene [2868](https://www.ncbi.nlm.nih.gov/gene/2868):

> This gene encodes a member of the guanine nucleotide-binding protein (G protein)-coupled receptor kinase subfamily of the Ser/Thr protein kinase family. The protein phosphorylates the activated forms of G protein-coupled receptors thus initiating its deactivation. This gene has been linked to both genetic and acquired hypertension. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:4543](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4543) · Entrez [2868](https://www.ncbi.nlm.nih.gov/gene/2868) · UniProt [P32298](https://www.uniprot.org/uniprotkb/P32298) · Ensembl [ENSG00000125388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125388)

## Data

Gene col 4610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4610); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4610]; `tensor/DDL_lfc|DDL_z.npy` [4610]; `embed/gene_vectors.npy` [4610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4610 or target_col == 4610). Every well: [[GRK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
