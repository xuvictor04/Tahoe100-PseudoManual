---
symbol: "RNASEK"
type: "gene"
col: 13295
ensembl_id: "ENSG00000219200"
name: "ribonuclease K"
location: "17p13.1"
module: 24
arm: "+"
pooled_cpm: 37.53
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# RNASEK

*ribonuclease K* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +8.9, q 5e-16, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ralimetinib dimesylate (drug)]] 0.05 µM: 0.617× (z -4.1, q 0.025, down in 41 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Budesonide (drug)]] 5 µM: 0.634× (z -3.9, q 0.033, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.109×; ⚠ cell-cycle shift, explains ~47% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (NCI-H661 0.0769×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUTA]] (+0.71, fdr 7e-06), [[ATP6V0B]] (+0.68, fdr 7e-06), [[CD63]] (+0.67, fdr 8e-06); moves opposite to [[TCOF1]] (-0.65, fdr 7e-06), [[PPP5C]] (-0.62, fdr 1e-05), [[TUBGCP3]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13295.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +8.9 | 5e-16 | 43/48 (NCI-H2347, J82, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.71×** | +8.2 | 8e-14 | 44/46 (NCI-H460, C32, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.29×** | +6.6 | 7e-09 | 34/37 (A549, NCI-H1792, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +5.9 | 5e-07 | 38/42 (NCI-H23, J82, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.96×** | +5.7 | 2e-06 | 40/47 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.87×** | +5.3 | 1e-05 | 36/46 (Panc 03.27, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +4.2 | 0.002 | 28/48 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +3.8 | 0.010 | 31/47 (SNU-423, SW480, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.59×** | +3.7 | 0.012 | 32/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.7 | 0.012 | 27/46 (NCI-H2347, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.012 | 29/48 (RKO, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.43× | +3.0 | 0.10 | 26/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.43× | +3.0 | 0.10 | 26/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | 1.43× | +3.0 | 0.11 | 23/47 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13295.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.109×; ⚠ cell-cycle shift, explains ~47% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (NCI-H661 0.0769×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.617×** | -4.1 | 0.025 | 41/48 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.634×** | -3.9 | 0.033 | 31/48 (Hs 766T, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.765× | -3.2 | 0.26 | 27/48 (H4, HS-578T, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.696× | -3.1 | 0.31 | 26/48 (Hs 766T, SW 900, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 42.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 52.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.109× (z -9.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[AsPC-1 (line)]] | alt | 34.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +8.9) | — |
| [[C32 (line)]] | wt | 42.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 25.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 42.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.9) | — |
| [[J82 (line)]] | alt | 37.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.8) | — |
| [[KATO III (line)]] | alt | 41.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 25.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H661 (line)]] | alt | 41.8 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0769× (z -8.7) |
| [[A-172 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUTA]] | +0.71 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[ATP6V0B]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 | STRING 997 |
| [[CD63]] | +0.67 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[ATP6V1F]] | +0.67 | +0.66 / +0.69 | both halves | 7e-06 | STRING 996 |
| [[MICU1]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SYNRG]] | +0.62 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[NPC2]] | +0.62 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[ATP6V1G1]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 | STRING 987 |
| [[GABARAP]] ⚠ | +0.61 | +0.70 / +0.64 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[HLA-A]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[BMPR2]] | +0.58 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[HSD17B14]] | +0.58 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[NEU1]] | +0.58 | +0.64 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCOF1]] | -0.65 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[PPP5C]] | -0.62 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[TUBGCP3]] | -0.60 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[SSRP1]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[AGK]] | -0.59 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[LAS1L]] | -0.58 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[PRPF19]] | -0.58 | -0.40 / -0.66 | both halves | 5e-05 |  |
| [[POLR3B]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[NBEAL2]] | -0.57 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[CSTF2]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[MRPL3]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[EXOSC2]] | -0.56 | -0.48 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RNASEK's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.422). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-9.4, -45.7); signed map (-10.3, 6.8). **Vector** length 73.4, 21.9% of its response variance represented; |z| ≥ 3 in 619 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +8.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +3.3 | +3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +3.1 | +5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.0 | +3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.8 | +0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.4 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.6 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -2.6 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | +0.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,012,417-7,014,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC71993 |
| Reactome | 3 pathways, smallest: Dengue Virus Attachment and Entry; Dengue Virus Infection; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P5S7](https://www.uniprot.org/uniprotkb/Q6P5S7) (Ribonuclease kappa):

> Endoribonuclease which preferentially cleaves ApU and ApG phosphodiester bonds and hydrolyzes UpU bonds at a lower rate. Degrades circular RNAs (circRNAs), preferentially over their cognate linear transcripts, and limits their age-associated accumulation. Acts synergistically with the lysosome in circRNA turnover, degrading circRNAs outside the organelle while lysosome-resident RNASE1 degrades circRNAs within the lysosomal lumen. Contributes to the decrease in global circRNA levels induced by …

**Summary**, from NCBI Gene [440400](https://www.ncbi.nlm.nih.gov/gene/440400):

> Enables RNA endonuclease activity. Involved in endosomal lumen acidification; proton transmembrane transport; and receptor-mediated endocytosis of virus by host cell. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33911) · Entrez [440400](https://www.ncbi.nlm.nih.gov/gene/440400) · UniProt [Q6P5S7](https://www.uniprot.org/uniprotkb/Q6P5S7) · Ensembl [ENSG00000219200](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000219200)

## Data

Gene col 13295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13295); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13295]; `tensor/DDL_lfc|DDL_z.npy` [13295]; `embed/gene_vectors.npy` [13295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13295 or target_col == 13295). Every well: [[RNASEK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNASEK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
