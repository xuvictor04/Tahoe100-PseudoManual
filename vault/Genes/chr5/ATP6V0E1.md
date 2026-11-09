---
symbol: "ATP6V0E1"
type: "gene"
col: 3496
ensembl_id: "ENSG00000113732"
name: "ATPase H+ transporting V0 subunit e1"
location: "5q35.1"
module: 24
arm: "+"
pooled_cpm: 83.34
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ATP6V0E1

*ATPase H+ transporting V0 subunit e1* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.58× (z +11.6, q 2e-28, up in 46 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0708×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.281×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.389×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLN3]] (+0.65, fdr 7e-06), [[NPC2]] (+0.65, fdr 7e-06), [[ATG14]] (+0.64, fdr 1e-05); moves opposite to [[ZWILCH]] (-0.57, fdr 1e-05), [[DNMT1]] (-0.56, fdr 1e-05), [[NOLC1]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF737]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.58×** | +11.6 | 2e-28 | 46/49 (RKO, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.06×** | +10.6 | 1e-23 | 46/48 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +10.3 | 1e-22 | 46/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.01×** | +10.2 | 2e-22 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.86×** | +9.0 | 2e-17 | 45/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.91×** | +8.9 | 4e-17 | 44/48 (HEC-1-A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.69×** | +7.6 | 2e-12 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +7.5 | 3e-12 | 40/48 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.68×** | +7.5 | 3e-12 | 36/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +5.5 | 2e-06 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +5.2 | 8e-06 | 34/48 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.2 | 1e-05 | 30/47 (Hs 766T, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.34×** | +4.2 | 1e-03 | 34/48 (HEC-1-A, H4, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.2 | 0.001 | 27/47 (A-427, HT-29, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.003 | 29/48 (HEC-1-A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.020 | 24/47 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.061 | 20/49 (A498, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.079 | 13/49 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (AN3 CA 0.0708×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.281×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.389×; ⚠ cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 71.7 | 11 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.93× (z +17.4) | — |
| [[SW480 (line)]] | alt | 70.8 | 6 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.48× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 79.9 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.73× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.01× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 119 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.07× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 73.1 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +10.7) | — |
| [[KATO III (line)]] | alt | 79.8 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +13.0) | — |
| [[LoVo (line)]] | wt | 87.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.57× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[HEC-1-A (line)]] | alt | 84.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.79× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 82.9 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.21× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 43.7 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.57× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 72.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +14.3) | — |
| [[HOP62 (line)]] | alt | 56.7 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.43× (z +10.5) | — |
| [[J82 (line)]] | alt | 88.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 168 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +9.3) | — |
| [[A-427 (line)]] | wt | 60.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.42× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0708× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 90.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.94× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 45.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.41× (z +9.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 92.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.69× (z +8.8) | — |
| [[RKO (line)]] | wt | 98.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.27× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 120 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.02× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 125 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.3) | — |
| [[A-172 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 78.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLN3]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[NPC2]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[ATG14]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[CCDC142]] | +0.62 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[ZNF358]] | +0.62 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CWC15]] | +0.61 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[SPNS1]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[UXT]] | +0.60 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ATP6V1H]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 997 |
| [[HEXA]] | +0.59 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[EMC3]] | +0.59 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[BLVRB]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZWILCH]] | -0.57 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[DNMT1]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[NOLC1]] | -0.56 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[ELK4]] | -0.56 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[CYCS]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[ARHGAP4]] | -0.53 | -0.30 / -0.65 | both halves | 2e-04 |  |
| [[NUP188]] | -0.53 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[CCDC18]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[SLC4A7]] | -0.52 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[DNAJC10]] | -0.52 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[C18orf54]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[SYNCRIP]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF737]] | B | ZNF737 activity raises ATP6V0E1's level | lines that do not express ZNF737 (18) vs lines expressing it (32) | 1.35× lower at baseline in the lines without ZNF737 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZNF85, ZNF66, ZNF90 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.525). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-16.2, -15.2); signed map (-18.5, 6.0). **Vector** length 117, 38.7% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.0 | +7.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +11.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.0 | +8.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.4 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.4 | +10.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +9.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.2 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +7.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.9 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -0.4 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V0 subunit e1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:172,983,771-173,035,445 (+) |
| Ensembl biotype | protein_coding |
| Also known as | M9.2; previously ATP6H, ATP6V0E |
| Gene groups (HGNC) | V-type ATPase subunits; Small nucleolar RNA protein coding host genes |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 16 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Insulin receptor recycling; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [O15342](https://www.uniprot.org/uniprotkb/O15342) (V-type proton ATPase subunit e 1):

> Subunit of the V0 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it promotes acidification of the extracellular environment (By similarity). The V-ATPase complex also acts as an activator for mTORC1 on …

**Summary**, from NCBI Gene [8992](https://www.ncbi.nlm.nih.gov/gene/8992):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 domain and a transmembrane V0 domain. The V1 domain consists of three A and three B subunits, two G …

**Accessions** — [HGNC:863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:863) · Entrez [8992](https://www.ncbi.nlm.nih.gov/gene/8992) · UniProt [O15342](https://www.uniprot.org/uniprotkb/O15342) · Ensembl [ENSG00000113732](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113732)

## Data

Gene col 3496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3496); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3496]; `tensor/DDL_lfc|DDL_z.npy` [3496]; `embed/gene_vectors.npy` [3496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3496 or target_col == 3496). Every well: [[ATP6V0E1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V0E1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
