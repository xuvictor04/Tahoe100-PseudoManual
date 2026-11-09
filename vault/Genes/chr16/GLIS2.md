---
symbol: "GLIS2"
type: "gene"
col: 4749
ensembl_id: "ENSG00000126603"
name: "GLIS family zinc finger 2"
location: "16p13.3"
module: 4
arm: "-"
pooled_cpm: 14.43
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# GLIS2

*GLIS family zinc finger 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.35× (z +14.1, q 2e-42, up in 31 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.650× (z -5.1, q 2e-04, down in 25 of 45 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 0.504× (z -4.2, q 0.005, down in 22 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.168×, Panc 03.27 0.194×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.0992×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (HT-29 0.216×); [[Alpelisib (drug)]] 0.05 µM in 1 line (SNU-1 0.0860×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SHP-77 0.101×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIM3]] (+0.71, fdr 7e-06), [[CBX4]] (+0.68, fdr 7e-06), [[ZIC2]] (+0.68, fdr 9e-06); moves opposite to [[ZNF731P]] (-0.67, fdr 7e-06), [[XRCC5]] (-0.62, fdr 7e-06), [[NUP155]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NUAK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.35×** | +14.1 | 2e-42 | 31/44 (KATO III, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +6.5 | 2e-08 | 25/43 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.69×** | +6.1 | 2e-07 | 23/42 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 0.006 | 20/44 (HEC-1-A, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.8 | 0.013 | 16/40 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.013 | 22/43 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.36×** | +3.6 | 0.026 | 16/41 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.30× | +3.0 | 0.17 | 11/45 (SW480, HEC-1-A, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4749.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.168×, Panc 03.27 0.194×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (KATO III 0.0992×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Auranofin (drug)]] 5 µM in 1 line (HT-29 0.216×); [[Alpelisib (drug)]] 0.05 µM in 1 line (SNU-1 0.0860×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SHP-77 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.650×** | -5.1 | 2e-04 | 25/45 (LoVo, SW1417, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.697×** | -4.3 | 0.005 | 23/45 (A498, NCI-H1573, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.504×** | -4.2 | 0.005 | 22/43 (CFPAC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.719×** | -3.9 | 0.014 | 22/45 (MIA PaCa-2, NCI-H23, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.730×** | -3.7 | 0.023 | 17/45 (A498, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.733×** | -3.5 | 0.039 | 16/43 (SNU-1, RKO, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.731×** | -3.5 | 0.039 | 16/44 (HT-29, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.766× | -3.2 | 0.11 | 16/44 (J82, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | 0.833× | -3.1 | 0.14 | 10/46 (SHP-77, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.611× | -3.0 | 0.14 | 12/42 (Hs 766T, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 17.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0992× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 31.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +14.6) | — |
| [[AsPC-1 (line)]] | alt | 22.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +14.1) | — |
| [[NCI-H460 (line)]] | wt | 12.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 20.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.0) | — |
| [[A549 (line)]] | wt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 8.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 21.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +15.2) | — |
| [[HOP62 (line)]] | alt | 8.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 19.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.216× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 7.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 8.34 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.101× (z -9.0) |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0860× (z -9.1) |
| [[SW1417 (line)]] | alt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +8.6) | — |
| [[A-172 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIM3]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[CBX4]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[ZIC2]] | +0.68 | +0.75 / +0.57 | both halves | 9e-06 | same gene group |
| [[MAP3K2-DT]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ERF]] | +0.65 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[BCOR]] | +0.64 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[RARG]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TUBB2B]] | +0.61 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[KREMEN2]] | +0.60 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[BBC3]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[DLX2]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[NFIX]] | +0.59 | +0.67 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF731P]] | -0.67 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[XRCC5]] | -0.62 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[NUP155]] | -0.60 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[DROSHA]] | -0.60 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[PRIM2]] | -0.59 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[TMX3]] | -0.58 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[MRPS27]] | -0.57 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[HERC2P9-1]] | -0.57 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[ANAPC10]] | -0.56 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[EIPR1]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.55 | -0.44 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUAK1]] | B | NUAK1 activity raises GLIS2's level | lines that do not express NUAK1 (5) vs lines expressing it (45) | 2.85× lower at baseline in the lines without NUAK1 | 0.060 | ⚠ within organs, on part of the lines; also absent: TGFB1, DBN1, CAVIN1; its own permutation p |
| [[PSMB5]] | B | PSMB5 activity raises GLIS2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (22.3, -3.5); signed map (-3.6, 13.1). **Vector** length 91.9, 20.0% of its response variance represented; |z| ≥ 3 in 780 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +14.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.1 | +6.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.9 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +2.9 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +2.8 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.0 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.9 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.1 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.1 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | GLIS family zinc finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,314,761-4,339,597 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NPHP7 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZE0](https://www.uniprot.org/uniprotkb/Q9BZE0) (Zinc finger protein GLIS2):

> Can act either as a transcriptional repressor or as a transcriptional activator, depending on the cell context. Acts as a repressor of the Hedgehog signaling pathway (By similarity). Represses the Hedgehog-dependent expression of Wnt4 (By similarity). Necessary to maintain the differentiated epithelial phenotype in renal cells through the inhibition of SNAI1, which itself induces the epithelial-to-mesenchymal transition (By similarity). Represses transcriptional activation mediated by CTNNB1 in …

**Summary**, from NCBI Gene [84662](https://www.ncbi.nlm.nih.gov/gene/84662):

> This gene is a member of the GLI-similar zinc finger protein family and encodes a nuclear transcription factor with five C2H2-type zinc finger domains. The protein encoded by this gene is widely expressed at low levels in the neural tube and peripheral nervous system and likely promotes neuronal differentiation. It is abundantly expressed in the kidney and may have a role in the regulation of kidney morphogenesis. p120 regulates the expression level of this protein and induces the cleavage of …

**Accessions** — [HGNC:29450](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29450) · Entrez [84662](https://www.ncbi.nlm.nih.gov/gene/84662) · UniProt [Q9BZE0](https://www.uniprot.org/uniprotkb/Q9BZE0) · Ensembl [ENSG00000126603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126603)

## Data

Gene col 4749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4749); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4749]; `tensor/DDL_lfc|DDL_z.npy` [4749]; `embed/gene_vectors.npy` [4749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4749 or target_col == 4749). Every well: [[GLIS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLIS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
