---
symbol: "ACADVL"
type: "gene"
col: 1029
ensembl_id: "ENSG00000072778"
name: "acyl-CoA dehydrogenase very long chain"
location: "17p13.1"
module: 50
arm: "+"
pooled_cpm: 56.78
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# ACADVL

*acyl-CoA dehydrogenase very long chain* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.26× (z +12.7, q 3e-34, up in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.46× (z +6.0, q 4e-07, up in 29 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.340×); [[Lonafarnib (drug)]] 5 µM in 1 line (HT-29 0.133×; ⚠ toxic); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.334×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBA1]] (+0.69, fdr 1e-05), [[FLNA]] (+0.69, fdr 8e-06), [[LIN7C]] (+0.67, fdr 3e-05); moves opposite to [[NCBP2AS2]] (-0.70, fdr 7e-06), [[SMIM26]] (-0.61, fdr 4e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[RPL36AL]] (-0.61, fdr 6e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[ADPRS]] (-0.61, fdr 3e-05), [[SF3B6]] (-0.59, fdr 2e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PGGHG]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1029.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +12.7 | 3e-34 | 46/49 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +10.8 | 1e-24 | 40/42 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +10.4 | 4e-23 | 40/45 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +6.0 | 4e-07 | 29/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +5.3 | 1e-05 | 32/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +4.9 | 1e-04 | 24/48 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 0.001 | 29/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +4.1 | 0.002 | 28/48 (H4, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.3 | 0.056 | 21/48 (AsPC-1, Panc 03.27, …) | top dose only | low cells (technical?) |
| [[Mifepristone (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.096 | 20/48 (SW1417, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1029.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.340×); [[Lonafarnib (drug)]] 5 µM in 1 line (HT-29 0.133×; ⚠ toxic); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.334×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | 0.779× | -3.6 | 0.11 | 23/47 (BT-474, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.797× | -3.5 | 0.11 | 19/48 (NCI-H2347, CHP-212, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.807× | -3.3 | 0.11 | 22/48 (SW480, AN3 CA, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -3.3 | 0.11 | 20/49 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | 0.808× | -3.3 | 0.11 | 20/48 (LS 180, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.9 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.0) | — |
| [[KATO III (line)]] | alt | 55.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 61.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 61.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 119 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.04× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 51.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +11.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 58.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.6) | [[Verteporfin (drug)]] 5 µM 0.334× (z -8.5) |
| [[LS 180 (line)]] | wt | 92.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 84.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +10.6) | — |
| [[A-172 (line)]] | wt | 59.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.72× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 57.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 70.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +9.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 33.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.133× (z -9.1) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +12.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 28.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 69.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 93.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -11.9) |
| [[SNU-423 (line)]] | alt | 34.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.5) | — |
| [[A549 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 76.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 78.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 83.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA1]] | +0.69 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[FLNA]] | +0.69 | +0.58 / +0.71 | both halves | 8e-06 |  |
| [[LIN7C]] | +0.67 | +0.46 / +0.71 | both halves | 3e-05 |  |
| [[CDK16]] | +0.67 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[NCSTN]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[BAG6]] | +0.65 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[RAB1B]] | +0.64 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[DCTN1]] | +0.62 | +0.41 / +0.70 | both halves | 4e-05 | pathway: IRE1alpha activates chaperones |
| [[ZBED6]] | +0.61 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[AP2M1]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PIGT]] | +0.61 | +0.39 / +0.68 | both halves | 6e-05 |  |
| [[TPP1]] | +0.61 | +0.41 / +0.67 | both halves | 4e-05 | pathway: IRE1alpha activates chaperones |

## Genes that move opposite

*30 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCBP2AS2]] | -0.70 | -0.59 / -0.70 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.61 | -0.41 / -0.67 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | -0.61 | -0.39 / -0.68 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ADPRS]] | -0.61 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[SF3B6]] | -0.59 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[SELENOH]] | -0.59 | -0.37 / -0.64 | both halves | 7e-05 |  |
| [[MRPL36]] | -0.58 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[C15orf61]] ⚠ | -0.57 | -0.47 / -0.66 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF593]] | -0.57 | -0.26 / -0.67 | both halves | 3e-04 |  |
| [[SF3B5]] ⚠ | -0.57 | -0.37 / -0.64 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FBXO45]] | -0.57 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[EMC6]] | -0.57 | -0.27 / -0.64 | both halves | 3e-04 |  |
| [[CEBPZ]] | -0.56 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[C16orf91]] | -0.56 | -0.28 / -0.64 | both halves | 3e-04 |  |
| [[CHCHD1]] | -0.56 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[PRPF38B]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGGHG]] | C | PGGHG activity lowers ACADVL's level | lines that do not express PGGHG (4) vs lines expressing it (46) | 1.68× higher at baseline in the lines without PGGHG | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GARIN1B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.2, -20.2); signed map (-16.0, -34.1). **Vector** length 115, 29.5% of its response variance represented; |z| ≥ 3 in 806 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.1 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.4 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +10.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.7 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +4.3 |
|  | [[Folic acid (drug)]] 5 µM |  | +2.6 | +0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +1.5 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.3 | -1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -3.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.5 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.5 | -3.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA dehydrogenase very long chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,217,125-7,225,266 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VLCAD, LCACD, ACAD6 |
| Gene groups (HGNC) | Acyl-CoA dehydrogenase family; Flavoproteins |
| Hallmark sets | FATTY_ACID_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 10 pathways, smallest: Beta oxidation of palmitoyl-CoA to myristoyl-CoA; mitochondrial fatty acid beta-oxidation of saturated fatty acids; Mitochondrial Fatty Acid Beta-Oxidation |
| Matched by | ensembl_id |

**Function**, from UniProt [P49748](https://www.uniprot.org/uniprotkb/P49748) (Very long-chain acyl-CoA dehydrogenase, mitochondrial):

> Catalyzes the first of the four reactions of the mitochondrial fatty acid beta-oxidation (FAO) pathway, which consists in the proR-proR stereospecific alpha, beta-dehydrogenation of fatty acyl-CoA thioesters using the electron transfer flavoprotein (ETF) as their physiologic electron acceptor, resulting in the formation of trans-2-enoyl-CoA ((2E)-enoyl-CoA). The mitochondrial FAO pathway is the major energy-producing process in tissues and is performed through cycles of four consecutive …

**Summary**, from NCBI Gene [37](https://www.ncbi.nlm.nih.gov/gene/37):

> The protein encoded by this gene is targeted to the inner mitochondrial membrane where it catalyzes the first step of the mitochondrial fatty acid beta-oxidation pathway. This acyl-Coenzyme A dehydrogenase is specific to long-chain and very-long-chain fatty acids. A deficiency in this gene product reduces myocardial fatty acid beta-oxidation and is associated with cardiomyopathy. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul …

**Accessions** — [HGNC:92](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:92) · Entrez [37](https://www.ncbi.nlm.nih.gov/gene/37) · UniProt [P49748](https://www.uniprot.org/uniprotkb/P49748) · Ensembl [ENSG00000072778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072778)

## Data

Gene col 1029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1029); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1029]; `tensor/DDL_lfc|DDL_z.npy` [1029]; `embed/gene_vectors.npy` [1029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1029 or target_col == 1029). Every well: [[ACADVL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACADVL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
