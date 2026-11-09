---
symbol: "TOE1"
type: "gene"
col: 5369
ensembl_id: "ENSG00000132773"
name: "target of EGR1, exonuclease"
location: "1p34.1"
module: 7
arm: "+"
pooled_cpm: 5.8
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TOE1

*target of EGR1, exonuclease* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.48× (z +5.5, q 2e-05, up in 25 of 42 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.63× (z +4.8, q 4e-04, up in 19 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 5.48×; ⚠ cell-cycle shift, explains ~51% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.399× (z -9.1, q 6e-17, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF689]] (+0.71, fdr 7e-06), [[DDX28]] (+0.70, fdr 7e-06), [[YTHDF2]] (+0.69, fdr 7e-06); moves opposite to [[IDS]] (-0.64, fdr 1e-05), [[SEPTIN2]] (-0.61, fdr 1e-05), [[AP3S1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5369.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 5.48×; ⚠ cell-cycle shift, explains ~51% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.48×** | +5.5 | 2e-05 | 25/42 (AsPC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +4.8 | 4e-04 | 19/38 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.015 | 14/46 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.50×** | +3.9 | 0.015 | 14/45 (AsPC-1, A498, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.4 | 0.084 | 15/32 (A-427, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.35× | +3.0 | 0.24 | 9/44 (HOP62, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5369.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.399×** | -9.1 | 6e-17 | 38/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.425×** | -8.4 | 8e-15 | 32/46 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.433×** | -8.3 | 3e-14 | 35/47 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.674×** | -5.5 | 5e-06 | 26/45 (SW480, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.622×** | -4.7 | 3e-04 | 17/47 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.694×** | -3.6 | 0.031 | 17/27 (HT-29, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.505×** | -3.5 | 0.034 | 12/45 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.707×** | -3.4 | 0.045 | 13/44 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.717× | -3.1 | 0.10 | 14/40 (RKO, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.736× | -3.0 | 0.15 | 4/46 (SNU-1, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5369. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 8.94 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0667× (z -9.6) |
| [[SW480 (line)]] | alt | 8.05 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 4.92 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +9.1) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[HOP62 (line)]] | alt | 5.78 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -9.7) |
| [[LoVo (line)]] | wt | 6.36 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -8.8) ⚠ cell-cycle shift, explains ~8% of this change |
| [[RKO (line)]] | wt | 8.05 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0667× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 5.40 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0523× (z -9.1) |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.148× (z -8.6) |
| [[A-172 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5369), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF689]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[DDX28]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 | STRING 475 |
| [[YTHDF2]] | +0.69 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.66 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[FIZ1]] | +0.64 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[ZNF282]] | +0.64 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[MTHFS]] | +0.64 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[ZNF75A]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ZCCHC3]] | +0.63 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[MTG2]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[CCDC137]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MRM2]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDS]] | -0.64 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[SEPTIN2]] | -0.61 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[AP3S1]] | -0.60 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[LTA4H]] | -0.57 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[NPTN]] | -0.56 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[HK2]] | -0.56 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[SPAG9]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[CAST]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PSAP]] | -0.55 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[GM2A]] | -0.54 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[ATP6AP2]] | -0.54 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[STX7]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TOE1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises TOE1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-39.8, 8.9); signed map (-3.5, -25.6). **Vector** length 71.9, 12.8% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.9 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.0 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.3 | +0.5 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +1.2 | +0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.1 | +1.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.1 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -5.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.0 | -9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.8 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | target of EGR1, exonuclease |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,340,052-45,343,973 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hCaf1z, TOE-1 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; PARN exonuclease family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GM8](https://www.uniprot.org/uniprotkb/Q96GM8) (Target of EGR1 protein 1):

> Inhibits cell growth rate and cell cycle. Induces CDKN1A expression as well as TGF-beta expression. Mediates the inhibitory growth effect of EGR1. Involved in the maturation of snRNAs and snRNA 3'-tail processing.

**Summary**, from NCBI Gene [114034](https://www.ncbi.nlm.nih.gov/gene/114034):

> Enables poly(A)-specific ribonuclease activity and snRNA binding activity. Involved in snRNA 3'-end processing. Located in Cajal body and cytoplasm. Implicated in pontocerebellar hypoplasia type 7. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15954) · Entrez [114034](https://www.ncbi.nlm.nih.gov/gene/114034) · UniProt [Q96GM8](https://www.uniprot.org/uniprotkb/Q96GM8) · Ensembl [ENSG00000132773](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132773)

## Data

Gene col 5369: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5369); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5369, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5369]; `tensor/DDL_lfc|DDL_z.npy` [5369]; `embed/gene_vectors.npy` [5369]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5369 or target_col == 5369). Every well: [[TOE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
