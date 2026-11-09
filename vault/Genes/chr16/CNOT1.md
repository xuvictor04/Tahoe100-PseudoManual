---
symbol: "CNOT1"
type: "gene"
col: 4586
ensembl_id: "ENSG00000125107"
name: "CCR4-NOT transcription complex subunit 1"
location: "16q21"
module: 29
arm: "+"
pooled_cpm: 240.96
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CNOT1

*CCR4-NOT transcription complex subunit 1* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.07× (z +8.7, q 1e-15, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.672× (z -4.6, q 0.002, down in 44 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.700× (z -4.3, q 0.004, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAPOLA]] (+0.66, fdr 7e-06), [[SUMO3]] (+0.66, fdr 7e-06), [[MOB1A]] (+0.65, fdr 1e-05); moves opposite to [[ZNF611]] (-0.68, fdr 7e-06), [[PLIN3]] (-0.66, fdr 1e-05), [[EML2]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4586.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.07×** | +8.7 | 1e-15 | 47/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.83×** | +8.4 | 8e-15 | 47/49 (BT-474, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +7.2 | 8e-11 | 39/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.78×** | +6.4 | 2e-08 | 45/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +5.8 | 1e-06 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.4 | 7e-06 | 38/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +4.5 | 5e-04 | 37/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.008 | 34/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.7 | 0.013 | 0/50 | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.67×** | +3.2 | 0.072 | 40/49 (Panc 03.27, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.079 | 29/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4586.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.672×** | -4.6 | 0.002 | 44/47 (Panc 03.27, LS 180, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.700×** | -4.3 | 0.004 | 37/48 (CFPAC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.708×** | -4.2 | 0.005 | 42/48 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.801×** | -3.8 | 0.018 | 31/48 (H4, SK-MEL-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.734×** | -3.8 | 0.019 | 35/48 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -3.7 | 0.020 | 38/48 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.739×** | -3.4 | 0.055 | 25/45 (SW 900, KATO III, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4586. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 291 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.17× (z +18.0) | — |
| [[HEC-1-A (line)]] | alt | 259 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 257 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +14.6) | — |
| [[LOX-IMVI (line)]] | wt | 194 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 185 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.453× (z -8.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 182 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +13.0) | — |
| [[A549 (line)]] | wt | 241 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -9.1) ⚠ cell-cycle shift, explains ~10% of this change |
| [[COLO 205 (line)]] | alt | 243 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.15× (z +11.3) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 7.54× (z +10.9) | — |
| [[KATO III (line)]] | alt | 299 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 293 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 182 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +12.8) | — |
| [[RKO (line)]] | wt | 288 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 242 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -9.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 268 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +9.8) | — |
| [[A498 (line)]] | wt | 320 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.7) | — |
| [[BT-474 (line)]] | alt | 263 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.31× (z +11.8) | — |
| [[CHP-212 (line)]] | wt | 360 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 240 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 217 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 210 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.06× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 170 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 168 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.9) | — |
| [[J82 (line)]] | alt | 223 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 292 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 393 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.3) | — |
| [[SW48 (line)]] | wt | 309 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +10.0) | — |
| [[A-172 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 218 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 277 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 264 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 241 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 331 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 356 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 260 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 272 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4586), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPOLA]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SUMO3]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.65 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[EIF4H]] | +0.64 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[PRPF8]] | +0.64 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[TMEM123]] | +0.64 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[ATRAID]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ZMYM3]] | +0.63 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[CDK16]] | +0.63 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[ADI1]] | +0.61 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[PNPO]] | +0.61 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[CBX5]] | +0.61 | +0.47 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF611]] | -0.68 | -0.62 / -0.71 | both halves | 7e-06 |  |
| [[PLIN3]] | -0.66 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[EML2]] | -0.61 | -0.42 / -0.69 | both halves | 4e-05 |  |
| [[GGT7]] | -0.59 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[C19orf25]] | -0.58 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[NOP10]] ⚠ | -0.58 | -0.43 / -0.66 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF593]] | -0.58 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[SIRT6]] | -0.58 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[LRRC8E]] | -0.57 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[IER5]] | -0.56 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[ARID3B]] | -0.56 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[RPL36AL]] ⚠ | -0.56 | -0.45 / -0.62 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CROCCP2-1]] | -0.56 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[SYP]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CNOT1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CNOT1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF611]] | C | ZNF611 activity lowers CNOT1's level | lines that do not express ZNF611 (3) vs lines expressing it (47) | 1.25× higher at baseline in the lines without ZNF611 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF468, ZNF845, ZNF14; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-27.2, -20.8); signed map (-20.8, -39.1). **Vector** length 101, 43.2% of its response variance represented; |z| ≥ 3 in 858 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +8.7 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.2 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | -3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.8 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.6 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | -0.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.3 | -0.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.0 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.3 | +3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | CCR4-NOT transcription complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:58,519,951-58,629,885 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDC39, NOT1H, KIAA1007, AD-005; previously NOT1 |
| Gene groups (HGNC) | CCR4-NOT transcription complex; Armadillo like helical domain containing; Small nucleolar RNA protein coding host genes; MIF4G domain containing proteins |
| Reactome | 8 pathways, smallest: TP53 regulates transcription of additional cell cycle genes whose exact role in the p53 pathway remain uncertain; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [A5YKK6](https://www.uniprot.org/uniprotkb/A5YKK6) (CCR4-NOT transcription complex subunit 1):

> Scaffolding component of the CCR4-NOT complex which is one of the major cellular mRNA deadenylases and is linked to various cellular processes including bulk mRNA degradation, miRNA-mediated repression, translational repression during translational initiation and general transcription regulation. Additional complex functions may be a consequence of its influence on mRNA expression. Its scaffolding function implies its interaction with the catalytic complex module and diverse RNA-binding …

**Summary**, from NCBI Gene [23019](https://www.ncbi.nlm.nih.gov/gene/23019):

> Enables armadillo repeat domain binding activity; molecular adaptor activity; and nuclear receptor binding activity. Contributes to poly(A)-specific ribonuclease activity. Involved in several processes, including negative regulation of intracellular signal transduction; positive regulation of cytoplasmic mRNA processing body assembly; and regulation of gene expression. Located in P-body. Part of CCR4-NOT complex. Implicated in Vissers-Bodmer syndrome and holoprosencephaly 12. [provided by …

**Accessions** — [HGNC:7877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7877) · Entrez [23019](https://www.ncbi.nlm.nih.gov/gene/23019) · UniProt [A5YKK6](https://www.uniprot.org/uniprotkb/A5YKK6) · Ensembl [ENSG00000125107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125107)

## Data

Gene col 4586: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4586); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4586, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4586]; `tensor/DDL_lfc|DDL_z.npy` [4586]; `embed/gene_vectors.npy` [4586]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4586 or target_col == 4586). Every well: [[CNOT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNOT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
