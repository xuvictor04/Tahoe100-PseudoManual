---
symbol: "MICAL1"
type: "gene"
col: 5726
ensembl_id: "ENSG00000135596"
name: "microtubule associated monooxygenase, calponin and LIM domain containing 1"
location: "6q21"
module: 2
arm: "+"
pooled_cpm: 15.2
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MICAL1

*microtubule associated monooxygenase, calponin and LIM domain containing 1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.45× (z +5.0, q 3e-04, up in 21 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.477× (z -15.2, q 0e+00, down in 33 of 45 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.457× (z -5.9, q 6e-07, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC39A13]] (+0.62, fdr 1e-05), [[CEP170B]] (+0.61, fdr 7e-06), [[ADAMTSL5]] (+0.59, fdr 9e-06); moves opposite to [[CNOT2]] (-0.51, fdr 4e-04), [[ZNF33A]] (-0.51, fdr 4e-05), [[DLEU1]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MEIS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5726.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 3e-04 | 21/46 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.42×** | +4.9 | 3e-04 | 16/45 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.8 | 4e-04 | 6/21 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.8 | 0.020 | 8/34 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 1.26× | +3.3 | 0.11 | 8/44 (C32, HOP62, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.1 | 0.14 | 12/47 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.14 | 10/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.24× | +3.1 | 0.14 | 9/47 (AsPC-1, Hs 766T, …) | rises with dose | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 1.16× | +3.0 | 0.17 | 8/47 (A-172, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5726.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.477×** | -15.2 | 0e+00 | 33/45 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.601×** | -7.4 | 4e-11 | 27/44 (SHP-77, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.457×** | -5.9 | 6e-07 | 26/45 (PANC-1, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.687×** | -5.5 | 7e-06 | 21/44 (SW48, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.695×** | -5.3 | 1e-05 | 20/47 (HS-578T, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.763×** | -3.9 | 0.008 | 15/47 (A-172, A549, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.756×** | -3.9 | 0.008 | 18/46 (HEC-1-A, NCI-H1792, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.769×** | -3.8 | 0.009 | 18/47 (SK-MEL-2, A-427, …) | rises with dose | position effect removed |
| [[Sulfatinib (drug)]] 5 µM |  | **0.767×** | -3.7 | 0.013 | 13/45 (KATO III, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.776×** | -3.7 | 0.013 | 15/46 (A-172, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.782×** | -3.6 | 0.018 | 17/46 (HS-578T, SW48, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.640×** | -3.4 | 0.033 | 10/42 (Hs 766T, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.793×** | -3.4 | 0.033 | 13/47 (KATO III, hTERT-HPNE, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.796×** | -3.3 | 0.037 | 11/46 (HT-29, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.856× | -3.2 | 0.050 | 21/44 (HS-578T, PANC-1, …) | top dose only | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.801×** | -3.1 | 0.063 | 11/45 (SNU-423, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5726. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 7.85 | 0 | 2 | — | [[Busulfan (drug)]] 0.5 µM 0.0634× (z -10.6) |
| [[J82 (line)]] | alt | 9.74 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 18.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.291× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 9.99 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0704× (z -10.6) |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -9.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 28.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -14.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -10.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -20.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -10.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 900 (line)]] | alt | 6.92 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0753× (z -9.5) |
| [[SW1417 (line)]] | alt | 5.23 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0704× (z -9.7) |
| [[SW48 (line)]] | wt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0793× (z -9.6) |
| [[A-172 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5726), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A13]] | +0.62 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[CEP170B]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ADAMTSL5]] | +0.59 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[KLF13]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[GDI1]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NBEAL2]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[PGGHG]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CDR2L]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PITPNM1]] | +0.57 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[MAPK11]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TESK1]] | +0.57 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[CDYL2]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNOT2]] | -0.51 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[ZNF33A]] | -0.51 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[DLEU1]] | -0.51 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ZNF292]] | -0.50 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[CTDSPL2]] | -0.49 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[RPRD2]] | -0.49 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[TET2]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[MTUS1]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[HNMT]] | -0.48 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[PRELID2]] | -0.47 | -0.33 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEIS3]] | B | MEIS3 activity raises MICAL1's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 2.18× lower at baseline in the lines without MEIS3 | 0.032 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-9.6, -25.5); signed map (-8.9, 29.9). **Vector** length 79.1, 14.4% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.4 | -15.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -2.4 | -3.9 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.4 | -3.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated monooxygenase, calponin and LIM domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:109,444,062-109,465,968 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MICAL, FLJ11937, DKFZp434B1517, FLJ21739; previously NICAL |
| Gene groups (HGNC) | LIM domain containing; Bivalent Mical/EHBP Rab binding domain containing; Flavoproteins; MICAL oxygenase family |
| Reactome | 2 pathways, smallest: Factors involved in megakaryocyte development and platelet production; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDZ2](https://www.uniprot.org/uniprotkb/Q8TDZ2) ([F-actin]-monooxygenase MICAL1):

> Monooxygenase that promotes depolymerization of F-actin by mediating oxidation of specific methionine residues on actin to form methionine-sulfoxide, resulting in actin filament disassembly and preventing repolymerization. In the absence of actin, it also functions as a NADPH oxidase producing H(2)O(2). Acts as a cytoskeletal regulator that connects NEDD9 to intermediate filaments. Also acts as a negative regulator of apoptosis via its interaction with STK38 and STK38L; acts by antagonizing …

**Summary**, from NCBI Gene [64780](https://www.ncbi.nlm.nih.gov/gene/64780):

> This gene encodes an enzyme that oxidizes methionine residues on actin, thereby promoting depolymerization of actin filaments. This protein interacts with and regulates signalling by NEDD9/CAS-L (neural precursor cell expressed, developmentally down-regulated 9). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:20619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20619) · Entrez [64780](https://www.ncbi.nlm.nih.gov/gene/64780) · UniProt [Q8TDZ2](https://www.uniprot.org/uniprotkb/Q8TDZ2) · Ensembl [ENSG00000135596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135596)

## Data

Gene col 5726: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5726); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5726, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5726]; `tensor/DDL_lfc|DDL_z.npy` [5726]; `embed/gene_vectors.npy` [5726]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5726 or target_col == 5726). Every well: [[MICAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MICAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
