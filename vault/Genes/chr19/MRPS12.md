---
symbol: "MRPS12"
type: "gene"
col: 4906
ensembl_id: "ENSG00000128626"
name: "mitochondrial ribosomal protein S12"
location: "19q13.2"
module: 54
arm: "+"
pooled_cpm: 9.63
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# MRPS12

*mitochondrial ribosomal protein S12* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.22× (z +6.8, q 6e-09, up in 34 of 37 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.17× (z +6.6, q 1e-08, up in 37 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 5.19×).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.554× (z -5.1, q 2e-04, down in 32 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 0.182×, A498 0.268×, BT-474 0.128×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.0851×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (75 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 31 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C16orf91]] (+0.78, fdr 4e-05), [[EMC6]] (+0.78, fdr 4e-05), [[EXOSC4]] (+0.77, fdr 1e-05); moves opposite to [[HP1BP3]] (-0.66, fdr 1e-04), [[CBX5]] (-0.61, fdr 3e-04), [[CCDC50]] (-0.59, fdr 3e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4906.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 5.19×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.22×** | +6.8 | 6e-09 | 34/37 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +6.6 | 1e-08 | 37/43 (A549, KATO III, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **2.58×** | +5.7 | 2e-06 | 20/31 (A498, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **2.52×** | +5.4 | 1e-05 | 8/15 (NCI-H2030, SW480, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **2.26×** | +4.9 | 1e-04 | 26/35 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.96×** | +4.1 | 0.005 | 25/46 (A549, HOP62, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.8 | 0.010 | 19/47 (SNU-423, SW1417, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.75×** | +3.4 | 0.050 | 20/47 (A549, HOP62, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.69×** | +3.2 | 0.098 | 18/46 (A549, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4906.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2030 0.182×, A498 0.268×, BT-474 0.128×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.0851×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.554×** | -5.1 | 2e-04 | 32/43 (NCI-H2030, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.328× | -3.5 | 0.11 | 19/43 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.600× | -3.1 | 0.35 | 17/46 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.1) |
| [[A549 (line)]] | wt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 6.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -9.1) |
| [[KATO III (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[NCI-H2030 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 8.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0851× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 25 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C16orf91]] | +0.78 | +0.42 / +0.81 | both halves | 4e-05 |  |
| [[EMC6]] | +0.78 | +0.42 / +0.85 | both halves | 4e-05 | **novel candidate** |
| [[EXOSC4]] | +0.77 | +0.53 / +0.79 | both halves | 1e-05 | STRING 567 |
| [[POP7]] | +0.77 | +0.52 / +0.80 | both halves | 1e-05 |  |
| [[NCBP2AS2]] | +0.73 | +0.35 / +0.81 | both halves | 1e-04 |  |
| [[SF3B5]] ⚠ | +0.72 | +0.39 / +0.79 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF593]] | +0.71 | +0.45 / +0.79 | both halves | 3e-05 |  |
| [[CHCHD1]] | +0.71 | +0.24 / +0.81 | both halves | 5e-04 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 982 |
| [[MRPL36]] | +0.70 | +0.36 / +0.76 | both halves | 1e-04 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 999 |
| [[GEMIN6]] | +0.70 | +0.43 / +0.76 | both halves | 3e-05 |  |
| [[AURKAIP1]] | +0.69 | +0.52 / +0.70 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 979 |
| [[NR2C2AP]] | +0.68 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[MRPS26]] | +0.68 | +0.52 / +0.73 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 988 |

## Genes that move opposite

*12 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HP1BP3]] | -0.66 | -0.35 / -0.68 | both halves | 1e-04 |  |
| [[CBX5]] | -0.61 | -0.27 / -0.64 | both halves | 3e-04 |  |
| [[CCDC50]] | -0.59 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[MYBL1]] | -0.56 | -0.36 / -0.50 | both halves | 9e-05 | STRING 400 |
| [[YWHAE]] | -0.56 | -0.10 / -0.62 | ⚠ one half (not replicated) | 0.003 |  |
| [[DHFR]] | -0.55 | -0.07 / -0.70 | ⚠ one half (not replicated) | 0.004 |  |
| [[RAB1B]] | -0.55 | -0.12 / -0.54 | ⚠ one half (not replicated) | 0.002 |  |
| [[ACADM]] | -0.55 | -0.18 / -0.57 | ⚠ one half (not replicated) | 9e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[ITGAV]] | -0.55 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[CDC42]] | -0.55 | -0.10 / -0.66 | ⚠ one half (not replicated) | 0.003 |  |
| [[SRP9]] | -0.54 | -0.10 / -0.62 | ⚠ one half (not replicated) | 0.003 |  |
| [[PRKAR1A]] | -0.54 | -0.28 / -0.60 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MRPS12's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-44.2, -11.2); signed map (-12.1, -8.0). **Vector** length 58.4, 12.6% of its response variance represented; |z| ≥ 3 in 573 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +6.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.5 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | -3.4 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | -3.1 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,930,944-38,933,168 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPS12, RPSM12, uS12m; previously RPMS12 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [O15235](https://www.uniprot.org/uniprotkb/O15235) carries no function annotation.

**Summary**, from NCBI Gene [6183](https://www.ncbi.nlm.nih.gov/gene/6183):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:10380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10380) · Entrez [6183](https://www.ncbi.nlm.nih.gov/gene/6183) · UniProt [O15235](https://www.uniprot.org/uniprotkb/O15235) · Ensembl [ENSG00000128626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128626)

## Data

Gene col 4906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4906); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4906]; `tensor/DDL_lfc|DDL_z.npy` [4906]; `embed/gene_vectors.npy` [4906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4906 or target_col == 4906). Every well: [[MRPS12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
