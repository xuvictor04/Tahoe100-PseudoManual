---
symbol: "MED19"
type: "gene"
col: 8000
ensembl_id: "ENSG00000156603"
name: "mediator complex subunit 19"
location: "11q12.1"
module: 12
arm: "+"
pooled_cpm: 16.47
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MED19

*mediator complex subunit 19* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.32× (z +10.8, q 1e-24, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.57× (z +8.6, q 2e-15, up in 41 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.0849×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SNU-1 0.0745×); [[Dinaciclib (drug)]] 5 µM in 1 line (BT-474 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKAP]] (+0.80, fdr 7e-06), [[CCDC174]] (+0.77, fdr 7e-06), [[KRTCAP2]] (+0.75, fdr 1e-05); moves opposite to [[HNRNPA3]] (-0.76, fdr 7e-06), [[IPO5]] (-0.71, fdr 1e-05), [[MAPK9]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.32×** | +10.8 | 1e-24 | 41/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.57×** | +8.6 | 2e-15 | 41/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.54×** | +8.2 | 5e-14 | 38/47 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.6 | 5e-12 | 38/46 (Hs 766T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.09×** | +6.8 | 2e-09 | 42/48 (LoVo, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.05×** | +6.6 | 5e-09 | 37/48 (LoVo, SW480, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +6.4 | 2e-08 | 34/42 (NCI-H2030, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.82×** | +5.5 | 3e-06 | 35/47 (LoVo, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.85×** | +4.9 | 6e-05 | 33/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | **1.45×** | +3.4 | 0.035 | 22/44 (C32, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 1.39× | +3.0 | 0.12 | 20/46 (BT-474, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8000.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (COLO 205 0.0849×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SNU-1 0.0745×); [[Dinaciclib (drug)]] 5 µM in 1 line (BT-474 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.696× | -3.3 | 0.55 | 21/48 (Panc 03.27, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 11.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +10.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.48× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +11.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.22× (z +8.6) | — |
| [[A549 (line)]] | wt | 18.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +10.5) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 12.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +8.7) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.0) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0849× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +9.1) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[HepG2_C3A (line)]] | wt | 8.75 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0667× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.6) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[KATO III (line)]] | alt | 24.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +8.6) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[LoVo (line)]] | wt | 13.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.7) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +11.8) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[PANC-1 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.7) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0745× (z -9.4) |
| [[A-172 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAP]] | +0.80 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.77 | +0.84 / +0.71 | both halves | 7e-06 |  |
| [[KRTCAP2]] | +0.75 | +0.57 / +0.80 | both halves | 1e-05 |  |
| [[SCAND1]] | +0.75 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.73 | +0.59 / +0.73 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[DNAL4]] | +0.71 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[ING2]] | +0.71 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[NRBF2]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[R3HCC1]] | +0.71 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.71 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[TCEAL8]] | +0.70 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[RNF113A]] | +0.70 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[LENG1]] | +0.70 | +0.75 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA3]] | -0.76 | -0.67 / -0.75 | both halves | 7e-06 |  |
| [[IPO5]] | -0.71 | -0.57 / -0.74 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.70 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[MAT2A]] | -0.70 | -0.62 / -0.70 | both halves | 7e-06 |  |
| [[DHFR]] | -0.69 | -0.51 / -0.72 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.69 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[APP]] | -0.69 | -0.63 / -0.71 | both halves | 7e-06 |  |
| [[RPSA]] | -0.68 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[TMX3]] | -0.68 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[CTSZ]] | -0.67 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[PABIR2]] | -0.67 | -0.66 / -0.69 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.67 | -0.45 / -0.72 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MED19's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MARCKS]] | B | MARCKS activity raises MED19's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 1.23× lower at baseline in the lines without MARCKS | 0.097 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.774). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-39.7, -12.4); signed map (-12.3, -2.6). **Vector** length 76.2, 19.0% of its response variance represented; |z| ≥ 3 in 634 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA Splicing - Major Pathway* (reactome, mean cos +0.50 to 17); *mRNA Splicing* (reactome, mean cos +0.50 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.3 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +8.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.3 | +8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +4.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.4 | +1.5 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.2 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.1 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.6 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.3 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | -0.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | +1.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | +1.3 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.5 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:57,703,710-57,712,221 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LCMR1 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [A0JLT2](https://www.uniprot.org/uniprotkb/A0JLT2) (Mediator of RNA polymerase II transcription subunit 19):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [219541](https://www.ncbi.nlm.nih.gov/gene/219541):

> The protein encoded by this gene is a subunit of the Mediator complex, which binds to gene-specific regulatory factors and provides support for the basal RNA polymerase II transcription machinery. This gene has been implicated in the growth of several types of cancer, and inhibition of its expression inhibits the growth and spread of these cancers. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:29600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29600) · Entrez [219541](https://www.ncbi.nlm.nih.gov/gene/219541) · UniProt [A0JLT2](https://www.uniprot.org/uniprotkb/A0JLT2) · Ensembl [ENSG00000156603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156603)

## Data

Gene col 8000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8000); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8000]; `tensor/DDL_lfc|DDL_z.npy` [8000]; `embed/gene_vectors.npy` [8000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8000 or target_col == 8000). Every well: [[MED19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
