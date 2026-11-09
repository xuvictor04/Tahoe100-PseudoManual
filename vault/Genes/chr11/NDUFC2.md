---
symbol: "NDUFC2"
type: "gene"
col: 7513
ensembl_id: "ENSG00000151366"
name: "NADH:ubiquinone oxidoreductase subunit C2"
location: "11q14.1"
module: 48
arm: "+"
pooled_cpm: 32.81
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# NDUFC2

*NADH:ubiquinone oxidoreductase subunit C2* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.96× (z +8.7, q 2e-15, up in 39 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 1.68× (z +3.2, q 0.094, up in 34 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 5.73×, HS-578T 5.24×, A549 6.68×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.227×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 30 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCR10]] (+0.77, fdr 7e-06, ⚠ UQCR10 in the vector space only through flagged drug-doses), [[C4orf48]] (+0.76, fdr 1e-05), [[NDUFB11]] (+0.71, fdr 7e-06, ⚠ NDUFB11 in the vector space only through flagged drug-doses), [[ATP5MJ]] (+0.71, fdr 2e-05), [[ROMO1]] (+0.70, fdr 7e-06); moves opposite to [[TLN1]] (-0.57, fdr 3e-05), [[UBQLN4]] (-0.57, fdr 1e-04), [[EEF1A1]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MIR181A1HG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7513.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 5.73×, HS-578T 5.24×, A549 6.68×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.96×** | +8.7 | 2e-15 | 39/42 (PANC-1, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.58×** | +7.8 | 2e-12 | 34/36 (A549, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +5.1 | 6e-05 | 41/46 (LOX-IMVI, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.10×** | +4.7 | 3e-04 | 40/47 (SW480, PANC-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.15×** | +4.5 | 8e-04 | 35/41 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.84×** | +3.9 | 0.011 | 34/46 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.77×** | +3.6 | 0.024 | 33/48 (COLO 205, J82, …) | two highest doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.46×** | +3.4 | 0.048 | 36/48 (Hs 766T, PANC-1, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.68×** | +3.2 | 0.094 | 34/47 (HS-578T, SW 1271, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7513.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.227×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.369× | -3.3 | 0.42 | 36/48 (SW480, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.391× | -3.1 | 0.42 | 33/47 (A-427, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 51.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 20.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.68× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HS-578T (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[PANC-1 (line)]] | alt | 43.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A-172 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 41.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 30 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCR10]] ⚠ | +0.77 | +0.65 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 975; ⚠ in the vector space only through flagged drug-doses |
| [[C4orf48]] | +0.76 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[NDUFB11]] ⚠ | +0.71 | +0.71 / +0.71 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MJ]] | +0.71 | +0.47 / +0.74 | both halves | 2e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 542 |
| [[NDUFA11]] ⚠ | +0.71 | +0.62 / +0.63 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 998; ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | +0.70 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[CHCHD1]] | +0.70 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[UQCR11]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 987 |
| [[ATP5MF]] | +0.68 | +0.60 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 672 |
| [[UQCRQ]] ⚠ | +0.68 | +0.63 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 987; ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | +0.68 | +0.55 / +0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ELOB]] | +0.67 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[ATP5ME]] | +0.67 | +0.48 / +0.69 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 799 |
| [[TOMM7]] | +0.67 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[COX6C]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 913 |
| [[LAMTOR5]] | +0.67 | +0.39 / +0.67 | both halves | 6e-05 |  |
| [[MNAT1]] | +0.66 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLN1]] | -0.57 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[UBQLN4]] | -0.57 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[EEF1A1]] | -0.55 | -0.39 / -0.61 | both halves | 6e-05 |  |
| [[SMG1P6]] | -0.55 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[ATN1]] | -0.55 | -0.28 / -0.54 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR181A1HG]] | B | MIR181A1HG activity raises NDUFC2's level | lines that do not express MIR181A1HG (7) vs lines expressing it (43) | 1.39× lower at baseline in the lines without MIR181A1HG | 0.097 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[POLR2I]] | C | POLR2I's natural level strengthens NDUFC2's drug response | POLR2I's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse -0.04; direction not clear | 0.057 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.7, -19.9); signed map (-33.9, 8.0). **Vector** length 58.9, 19.9% of its response variance represented; |z| ≥ 3 in 422 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Complex IV assembly* (reactome, mean cos +0.53 to 11); *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.61 to 7); *Cytoprotection by HMOX1* (reactome, mean cos +0.56 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | +2.9 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | -0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -3.7 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -3.4 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -3.1 | +8.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit C2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:78,068,297-78,079,862 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B14.5b, HLC-1 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O95298](https://www.uniprot.org/uniprotkb/O95298) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis but required for the complex assembly. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4718](https://www.ncbi.nlm.nih.gov/gene/4718):

> Predicted to enable NADH dehydrogenase (ubiquinone) activity. Involved in mitochondrial respiratory chain complex I assembly. Located in mitochondrial inner membrane. Part of respiratory chain complex I. Implicated in nuclear type mitochondrial complex I deficiency and stroke. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7706](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7706) · Entrez [4718](https://www.ncbi.nlm.nih.gov/gene/4718) · UniProt [O95298](https://www.uniprot.org/uniprotkb/O95298) · Ensembl [ENSG00000151366](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151366)

## Data

Gene col 7513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7513); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7513]; `tensor/DDL_lfc|DDL_z.npy` [7513]; `embed/gene_vectors.npy` [7513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7513 or target_col == 7513). Every well: [[NDUFC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
