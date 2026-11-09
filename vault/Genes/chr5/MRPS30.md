---
symbol: "MRPS30"
type: "gene"
col: 3425
ensembl_id: "ENSG00000112996"
name: "mitochondrial ribosomal protein S30"
location: "5p12"
module: 33
arm: "+"
pooled_cpm: 37.89
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# MRPS30

*mitochondrial ribosomal protein S30* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.60× (z +8.1, q 4e-13, up in 34 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.248×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (HCT15 0.126×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS35]] (+0.76, fdr 7e-06), [[EIF3E]] (+0.66, fdr 7e-06), [[QTRT2]] (+0.65, fdr 7e-06); moves opposite to [[CCNYL1]] (-0.55, fdr 1e-05), [[DMPK]] (-0.49, fdr 3e-05), [[PDLIM7]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Lapatinib ditosylate (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3425.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +8.1 | 4e-13 | 34/48 (NCI-H23, HT-29, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +7.8 | 2e-12 | 32/47 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +7.2 | 9e-11 | 36/48 (SW480, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.09×** | +6.6 | 6e-09 | 29/48 (LS 180, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.44×** | +6.3 | 4e-08 | 31/47 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +6.2 | 7e-08 | 28/48 (A-172, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.43×** | +5.9 | 3e-07 | 24/40 (MIA PaCa-2, A549, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.7 | 7e-07 | 31/48 (SW480, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +5.4 | 3e-06 | 29/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.41×** | +5.4 | 3e-06 | 22/42 (A549, H4, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 3e-04 | 29/48 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.30×** | +4.5 | 4e-04 | 24/48 (LS 180, COLO 205, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.4 | 6e-04 | 21/48 (SW 900, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +4.3 | 7e-04 | 25/48 (PANC-1, LoVo, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +4.3 | 8e-04 | 19/46 (J82, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.001 | 21/48 (NCI-H1573, LoVo, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.57×** | +4.0 | 0.002 | 19/48 (NCI-H460, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.003 | 19/48 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.006 | 18/48 (SW480, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.007 | 12/48 (NCI-H460, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.007 | 14/48 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3425.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.248×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (HCT15 0.126×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.850× | -4.0 | 0.043 | 18/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.692× | -3.3 | 0.21 | 20/48 (Hs 766T, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.822× | -3.3 | 0.21 | 9/48 (HEC-1-A, hTERT-HPNE, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3425. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 42.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A549 (line)]] | wt | 23.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[COLO 205 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[HCT15 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.126× (z -9.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 41.2 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.59× (z +9.3) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 50.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H23 (line)]] | alt | 95.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.15× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 37.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 424 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 52.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3425), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS35]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 972 |
| [[EIF3E]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[QTRT2]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[SUPV3L1]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[APEX1]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.61 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PAIP1]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SLC25A38]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[NOB1]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[NUFIP1]] | +0.60 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[RPP30]] | +0.59 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ZNF343]] | +0.59 | +0.64 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNYL1]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[DMPK]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PDLIM7]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SLC12A4]] | -0.48 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[ZSWIM4]] | -0.48 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[ADGRL1-AS1]] | -0.48 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[RELT]] | -0.48 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[CALM1]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[SMTN]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SEPTIN10]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | MRPS30's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | MRPS30's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.024 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.485). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.8, -12.7); signed map (-32.8, -20.8). **Vector** length 77.0, 15.9% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.3 | +6.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.8 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.0 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -2.2 | +4.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p12 — chr5:44,808,947-44,820,428 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAP, mL65; previously PDCD9 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9NP92](https://www.uniprot.org/uniprotkb/Q9NP92) carries no function annotation.

**Summary**, from NCBI Gene [10884](https://www.ncbi.nlm.nih.gov/gene/10884):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:8769](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8769) · Entrez [10884](https://www.ncbi.nlm.nih.gov/gene/10884) · UniProt [Q9NP92](https://www.uniprot.org/uniprotkb/Q9NP92) · Ensembl [ENSG00000112996](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112996)

## Data

Gene col 3425: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3425); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3425, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3425]; `tensor/DDL_lfc|DDL_z.npy` [3425]; `embed/gene_vectors.npy` [3425]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3425 or target_col == 3425). Every well: [[MRPS30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
