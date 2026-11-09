---
symbol: "FBL"
type: "gene"
col: 2560
ensembl_id: "ENSG00000105202"
name: "fibrillarin rRNA 2'-O-methyltransferase"
location: "19q13.2"
module: 134
arm: "+"
pooled_cpm: 204.79
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# FBL

*fibrillarin rRNA 2'-O-methyltransferase* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.33× (z +6.0, q 1e-06, up in 42 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 1.99× (z +3.7, q 0.014, up in 40 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 3.66×, A498 3.30×, HT-29 3.02×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 2.88×, A-172 2.16×; ⚠ cell-cycle shift, explains ~20% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 3.27×, NCI-H1792 3.25×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.378×, C-33 A 0.422×); [[Selinexor (drug)]] 5 µM in 2 lines (LS 180 0.438×, A498 0.451×; ⚠ cell-cycle shift, would explain all of this change); [[Vilanterol (drug)]] 0.05 µM in 1 line (SW 1271 0.0561×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDK1]] (+0.65, fdr 2e-05), [[AK2]] (+0.62, fdr 1e-05), [[HDHD5]] (+0.62, fdr 1e-05); moves opposite to [[UBE2A]] (-0.52, fdr 5e-05), [[LARP7]] (-0.52, fdr 5e-05), [[MOB3C]] (-0.50, fdr 5e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 12 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2560.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 3.66×, A498 3.30×, HT-29 3.02×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 2.88×, A-172 2.16×; ⚠ cell-cycle shift, explains ~20% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H460 3.27×, NCI-H1792 3.25×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.33×** | +6.0 | 1e-06 | 42/47 (LoVo, HT-29, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.77×** | +5.7 | 4e-06 | 34/43 (SW480, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.78×** | +5.2 | 3e-05 | 35/44 (RKO, Panc 03.27, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.66×** | +5.2 | 3e-05 | 40/46 (BT-474, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.56×** | +4.4 | 0.001 | 33/48 (NCI-H2347, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.52×** | +4.3 | 0.002 | 35/46 (NCI-H460, NCI-H1792, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +3.9 | 0.006 | 34/46 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.30×** | +3.8 | 0.012 | 29/47 (NCI-H2347, A-172, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.99×** | +3.7 | 0.014 | 40/46 (CFPAC-1, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +3.4 | 0.044 | 26/46 (NCI-H460, PANC-1, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.40×** | +3.3 | 0.051 | 28/46 (A-427, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.2 | 0.076 | 25/45 (HepG2/C3A, RKO, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.53× | +3.0 | 0.11 | 24/46 (NCI-H1792, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2560.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.378×, C-33 A 0.422×); [[Selinexor (drug)]] 5 µM in 2 lines (LS 180 0.438×, A498 0.451×; ⚠ cell-cycle shift, would explain all of this change); [[Vilanterol (drug)]] 0.05 µM in 1 line (SW 1271 0.0561×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.786× | -3.5 | 0.29 | 29/46 (LS 180, A498, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.802× | -3.2 | 0.41 | 26/46 (SNU-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | 0.567× | -3.0 | 0.45 | 31/47 (SK-MEL-2, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 65.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.30× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | [[Selinexor (drug)]] 5 µM 0.451× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 184 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 89.2 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.30× (z +9.5) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[A-172 (line)]] | wt | 92.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.7) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[AN3 CA (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 109 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[LS 180 (line)]] | wt | 87.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.438× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.25× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[NCI-H2347 (line)]] | alt | 74.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +13.3) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[RKO (line)]] | wt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.01× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SNU-1 (line)]] | wt | 137 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -10.3) |
| [[SW 1271 (line)]] | alt | 72.6 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0561× (z -10.7) |
| [[SW480 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[A-427 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 249 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.4 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 90.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 143 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 80.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 94.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 145 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.0 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 323 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1,877 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 166 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDK1]] | +0.65 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[AK2]] | +0.62 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[HDHD5]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[USP37]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[NDC1]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[FAM210A]] | +0.60 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[PDXP]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[WDR45B]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[CABIN1]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[POM121]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[TENT4A]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[YEATS2]] | +0.58 | +0.57 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2A]] | -0.52 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[LARP7]] | -0.52 | -0.52 / -0.40 | both halves | 5e-05 | STRING 705 |
| [[MOB3C]] | -0.50 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[PMF1]] | -0.50 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[UBQLN2]] | -0.49 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[C11orf58]] | -0.49 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[NFU1]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[DCTN6]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[BRPF3]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 | STRING 420 |
| [[UBXN4]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ZNF776]] | -0.47 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ZNF24]] | -0.46 | -0.41 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FBL's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.0, -18.2); signed map (-39.0, 23.6). **Vector** length 76.2, 27.4% of its response variance represented; |z| ≥ 3 in 666 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +3.1 | +3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.7 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.6 | +4.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.0 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.2 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +0.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | +0.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.1 | +0.9 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | fibrillarin rRNA 2'-O-methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,834,458-39,846,379 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNU3IP1, FLRN, FIB, Nop1 |
| Gene groups (HGNC) | U3 small nucleolar ribonucleoprotein; 7BS 2'O-ribose DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [P22087](https://www.uniprot.org/uniprotkb/P22087) (rRNA 2'-O-methyltransferase fibrillarin):

> S-adenosyl-L-methionine-dependent methyltransferase that has the ability to methylate both RNAs and proteins. Involved in pre-rRNA processing by catalyzing the site-specific 2'-hydroxyl methylation of ribose moieties in pre-ribosomal RNA. Site specificity is provided by a guide RNA that base pairs with the substrate (By similarity). Methylation occurs at a characteristic distance from the sequence involved in base pairing with the guide RNA (By similarity). Probably catalyzes 2'-O-methylation …

**Summary**, from NCBI Gene [2091](https://www.ncbi.nlm.nih.gov/gene/2091):

> This gene product is a component of a nucleolar small nuclear ribonucleoprotein (snRNP) particle thought to participate in the first step in processing preribosomal RNA. It is associated with the U3, U8, and U13 small nuclear RNAs and is located in the dense fibrillar component (DFC) of the nucleolus. The encoded protein contains an N-terminal repetitive domain that is rich in glycine and arginine residues, like fibrillarins in other species. Its central region resembles an RNA-binding domain …

**Accessions** — [HGNC:3599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3599) · Entrez [2091](https://www.ncbi.nlm.nih.gov/gene/2091) · UniProt [P22087](https://www.uniprot.org/uniprotkb/P22087) · Ensembl [ENSG00000105202](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105202)

## Data

Gene col 2560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2560); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2560]; `tensor/DDL_lfc|DDL_z.npy` [2560]; `embed/gene_vectors.npy` [2560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2560 or target_col == 2560). Every well: [[FBL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
