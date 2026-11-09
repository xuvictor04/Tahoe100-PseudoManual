---
symbol: "RNF5"
type: "gene"
col: 12848
ensembl_id: "ENSG00000204308"
name: "ring finger protein 5"
location: "6p21.32"
module: 69
arm: "+"
pooled_cpm: 14.59
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# RNF5

*ring finger protein 5* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.00× (z +6.8, q 6e-09, up in 27 of 37 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 4.90×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.474× (z -7.3, q 1e-10, down in 43 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.747× (z -4.1, q 0.007, down in 23 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 0.258×, SW480 0.408×); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.192×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.110×; ⚠ toxic; cell-cycle shift, explains ~63% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (AN3 CA 0.0921×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.230×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCTN3]] (+0.63, fdr 2e-05), [[ARID4A]] (+0.62, fdr 4e-05), [[CTDSP2]] (+0.58, fdr 1e-05); moves opposite to [[USP45]] (-0.55, fdr 4e-05), [[DDX21]] (-0.54, fdr 3e-05), [[CPNE2]] (-0.53, fdr 3e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TPR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12848.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 4.90×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +6.8 | 6e-09 | 27/37 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +4.5 | 0.002 | 19/27 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.1 | 0.007 | 1/48 (MIA PaCa-2) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.51×** | +4.1 | 0.007 | 20/42 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12848.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 0.258×, SW480 0.408×); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.192×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.110×; ⚠ toxic; cell-cycle shift, explains ~63% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (AN3 CA 0.0921×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.230×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.474×** | -7.3 | 1e-10 | 43/47 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.611×** | -4.8 | 4e-04 | 29/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.618×** | -4.5 | 0.002 | 28/47 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.747×** | -4.1 | 0.007 | 23/46 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.802× | -3.1 | 0.22 | 14/48 (SW1417, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 20.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.90× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -8.6) |
| [[AN3 CA (line)]] | alt | 40.2 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0921× (z -8.9) |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.110× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~63% of this change |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.252× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -9.3) ⚠ cell-cycle shift, explains ~82% of this change |
| [[SW480 (line)]] | alt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.1) |
| [[A498 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN3]] | +0.63 | +0.48 / +0.69 | both halves | 2e-05 | pathway: Asparagine N-linked glycosylation |
| [[ARID4A]] | +0.62 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[CTDSP2]] | +0.58 | +0.52 / +0.61 | both halves | 1e-05 | same gene group |
| [[CIR1]] | +0.57 | +0.39 / +0.71 | both halves | 6e-05 |  |
| [[GABARAP]] ⚠ | +0.56 | +0.50 / +0.61 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DCAF11]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[PEX13]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[CXXC5]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[NUDT16L1]] | +0.54 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[RNASE4]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TNRC6B]] | +0.54 | +0.31 / +0.57 | both halves | 2e-04 | pathway: Co-inhibition by PD-1 |
| [[COX14]] | +0.53 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[CCNG2]] | +0.53 | +0.44 / +0.65 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP45]] | -0.55 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[DDX21]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[CPNE2]] | -0.53 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[TANGO6]] | -0.53 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[MDFI]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[GALNT14]] | -0.52 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[SLFNL1-AS1]] | -0.51 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[PUS7]] | -0.51 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[LINC01322]] | -0.51 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[PCOLCE2]] | -0.51 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CAPN2]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ADCY7]] | -0.50 | -0.51 / -0.36 | both halves | 1e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises RNF5's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPR]] | C | RNF5's natural level weakens TPR's drug response | RNF5's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.32; direction not clear | 0.023 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.2, -43.8); signed map (-12.5, 8.0). **Vector** length 64.2, 12.7% of its response variance represented; |z| ≥ 3 in 541 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | +1.8 | +4.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +1.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.0 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,178,405-32,180,793 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NG2, G16, RING5, RMA1 |
| Gene groups (HGNC) | Ring finger proteins; MicroRNA protein coding host genes; RING finger E3 ubiquitin protein ligases |
| Reactome | 15 pathways, smallest: ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle; N-glycan trimming in the ER and Calnexin/Calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99942](https://www.uniprot.org/uniprotkb/Q99942) (E3 ubiquitin-protein ligase RNF5):

> Membrane-bound E3 ubiquitin-protein ligase that mediates ubiquitination of target proteins. May function together with E2 ubiquitin-conjugating enzymes UBE2D1/UBCH5A and UBE2D2/UBC4. Mediates ubiquitination of PXN/paxillin,thereby regulating cell motility and localization of PXN/paxillin. Catalyzes ubiquitination of Salmonella type III secreted protein sopA. Mediates the 'Lys-63'-linked polyubiquitination of JKAMP thereby regulating JKAMP function by decreasing its association with components …

**Summary**, from NCBI Gene [6048](https://www.ncbi.nlm.nih.gov/gene/6048):

> The protein encoded by this gene contains a RING finger, which is a motif known to be involved in protein-protein interactions. This protein is a membrane-bound ubiquitin ligase. It can regulate cell motility by targeting paxillin ubiquitination and altering the distribution and localization of paxillin in cytoplasm and cell focal adhesions. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10068) · Entrez [6048](https://www.ncbi.nlm.nih.gov/gene/6048) · UniProt [Q99942](https://www.uniprot.org/uniprotkb/Q99942) · Ensembl [ENSG00000204308](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204308)

## Data

Gene col 12848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12848); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12848]; `tensor/DDL_lfc|DDL_z.npy` [12848]; `embed/gene_vectors.npy` [12848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12848 or target_col == 12848). Every well: [[RNF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
