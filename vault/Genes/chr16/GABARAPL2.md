---
symbol: "GABARAPL2"
type: "gene"
col: 425
ensembl_id: "ENSG00000034713"
name: "GABA type A receptor associated protein like 2"
location: "16q23.1"
module: 24
arm: "+"
pooled_cpm: 64.71
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# GABARAPL2

*GABA type A receptor associated protein like 2* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.29× (z +5.8, q 3e-06, up in 45 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.74× (z +3.9, q 0.015, up in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 4.41×, HOP62 3.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 3.57×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.303× (z -4.4, q 0.007, down in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.173×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX17]] (+0.78, fdr 7e-06), [[LAMTOR5]] (+0.77, fdr 7e-06), [[COX4I1]] (+0.77, fdr 7e-06, ⚠ COX4I1 in the vector space only through flagged drug-doses), [[COMMD6]] (+0.76, fdr 7e-06); moves opposite to [[CCT7]] (-0.72, fdr 7e-06), [[NUP155]] (-0.72, fdr 7e-06), [[DARS2]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 425.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 4.41×, HOP62 3.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 3.57×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.29×** | +5.8 | 3e-06 | 45/49 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.99×** | +4.6 | 1e-03 | 37/42 (SHP-77, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.75×** | +3.9 | 0.015 | 38/48 (KATO III, NCI-H1573, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +3.9 | 0.015 | 40/48 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +3.7 | 0.029 | 38/48 (C-33 A, HOP62, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.65×** | +3.5 | 0.040 | 30/48 (NCI-H1792, SW480, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | 1.64× | +3.2 | 0.11 | 29/45 (HOP62, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.59× | +3.1 | 0.12 | 34/47 (HepG2/C3A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 425.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.173×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.303×** | -4.4 | 0.007 | 42/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.608× | -3.5 | 0.10 | 43/48 (NCI-H2347, A498, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.610× | -3.5 | 0.10 | 34/48 (AsPC-1, SW48, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.719× | -3.3 | 0.15 | 39/48 (RKO, Hs 766T, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.618× | -3.2 | 0.17 | 29/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.734× | -3.1 | 0.20 | 36/48 (CFPAC-1, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 425. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 99.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 62.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[PANC-1 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[RKO (line)]] | wt | 91.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 83.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 86.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 88.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 78.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 87.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 425), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 16 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX17]] | +0.78 | +0.68 / +0.83 | both halves | 7e-06 |  |
| [[LAMTOR5]] | +0.77 | +0.63 / +0.78 | both halves | 7e-06 | pathway: Autophagy |
| [[COX4I1]] ⚠ | +0.77 | +0.67 / +0.78 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[COMMD6]] | +0.76 | +0.63 / +0.80 | both halves | 7e-06 |  |
| [[UQCRB]] ⚠ | +0.75 | +0.69 / +0.80 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MIEN1]] | +0.74 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[UBE2B]] | +0.73 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[TOMM7]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 | pathway: Autophagy |
| [[ATP5MK]] | +0.72 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.72 | +0.66 / +0.73 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MJ]] | +0.72 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[EIF1B]] | +0.72 | +0.56 / +0.81 | both halves | 1e-05 |  |
| [[RPL36]] | +0.71 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[RPL35A]] | +0.71 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[MRPL33]] | +0.70 | +0.63 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT7]] | -0.72 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[NUP155]] | -0.72 | -0.66 / -0.79 | both halves | 7e-06 |  |
| [[DARS2]] | -0.71 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[EIF2S1]] | -0.71 | -0.60 / -0.80 | both halves | 7e-06 | STRING 421 |
| [[ATIC]] | -0.71 | -0.65 / -0.72 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.70 | -0.58 / -0.71 | both halves | 8e-06 |  |
| [[SF3B3]] | -0.70 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[PSME3]] | -0.70 | -0.54 / -0.77 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.69 | -0.59 / -0.72 | both halves | 7e-06 |  |
| [[MTHFD1]] | -0.69 | -0.65 / -0.80 | both halves | 7e-06 |  |
| [[SF3B4]] | -0.67 | -0.53 / -0.71 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.67 | -0.48 / -0.75 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers GABARAPL2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.714). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-44.5, -24.0); signed map (-16.3, 5.6). **Vector** length 89.1, 36.2% of its response variance represented; |z| ≥ 3 in 529 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +3.5 | +3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +2.9 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | -0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -4.6 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -4.5 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -3.9 | +5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | GABA type A receptor associated protein like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:75,566,375-75,577,881 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GEF2, ATG8, GATE16, GATE-16, ATG8C |
| Gene groups (HGNC) | Autophagy related; GABA type A receptor-associated protein family |
| Hallmark sets | MYOGENESIS |
| Reactome | 6 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Macroautophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [P60520](https://www.uniprot.org/uniprotkb/P60520) (Gamma-aminobutyric acid receptor-associated protein-like 2):

> Ubiquitin-like modifier involved in intra-Golgi traffic (By similarity). Modulates intra-Golgi transport through coupling between NSF activity and SNAREs activation (By similarity). It first stimulates the ATPase activity of NSF which in turn stimulates the association with GOSR1 (By similarity). Involved in autophagy. Plays a role in mitophagy which contributes to regulate mitochondrial quantity and quality by eliminating the mitochondria to a basal level to fulfill cellular energy …

**Summary**, from NCBI Gene [11345](https://www.ncbi.nlm.nih.gov/gene/11345):

> Enables phosphatidylethanolamine binding activity and ubiquitin protein ligase binding activity. Involved in autophagosome assembly; negative regulation of proteasomal protein catabolic process; and protein localization to endoplasmic reticulum. Located in Golgi membrane and autophagosome membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13291) · Entrez [11345](https://www.ncbi.nlm.nih.gov/gene/11345) · UniProt [P60520](https://www.uniprot.org/uniprotkb/P60520) · Ensembl [ENSG00000034713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000034713)

## Data

Gene col 425: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 425); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 425, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 425]; `tensor/DDL_lfc|DDL_z.npy` [425]; `embed/gene_vectors.npy` [425]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 425 or target_col == 425). Every well: [[GABARAPL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABARAPL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
