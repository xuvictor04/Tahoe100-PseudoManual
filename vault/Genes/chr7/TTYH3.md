---
symbol: "TTYH3"
type: "gene"
col: 5853
ensembl_id: "ENSG00000136295"
name: "tweety family member 3"
location: "7p22.3"
module: 2
arm: "+"
pooled_cpm: 36.38
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TTYH3

*tweety family member 3* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.32× (z +4.4, q 0.006, up in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 2.15×, NCI-H1792 2.21×; ⚠ cell-cycle shift, explains ~84% of this change); [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (NCI-H2122 0.947×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 3.23×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.559× (z -9.1, q 3e-17, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGRN]] (+0.64, fdr 8e-06), [[ZFPM1]] (+0.61, fdr 1e-05), [[SEMA3F]] (+0.58, fdr 1e-05); moves opposite to [[SLC22A15]] (-0.46, fdr 1e-04), [[RSL1D1]] (-0.46, fdr 4e-05), [[ZFYVE9]] (-0.45, fdr 9e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LFNG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5853.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 2.15×, NCI-H1792 2.21×; ⚠ cell-cycle shift, explains ~84% of this change); [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (NCI-H2122 0.947×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 3.23×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +4.4 | 0.006 | 23/47 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.089 | 17/47 (SW480, A-172, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.23× | +3.3 | 0.15 | 15/46 (SK-MEL-2, AsPC-1, …) | rises with dose | low cells (technical?) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.23× | +3.3 | 0.15 | 5/47 (J82, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5853.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.559×** | -9.1 | 3e-17 | 33/45 (KATO III, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.578×** | -8.6 | 2e-15 | 33/47 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.609×** | -7.8 | 1e-12 | 34/47 (KATO III, HepG2/C3A, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.675×** | -5.8 | 7e-07 | 28/47 (HOP62, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.695×** | -5.5 | 4e-06 | 25/47 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.745×** | -4.6 | 4e-04 | 23/47 (COLO 205, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.599×** | -4.2 | 0.002 | 17/47 (SW480, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.768×** | -4.1 | 0.002 | 19/47 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.769×** | -4.1 | 0.002 | 21/47 (MIA PaCa-2, AN3 CA, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.769×** | -4.1 | 0.002 | 18/47 (KATO III, SW 900, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | **0.832×** | -4.1 | 0.002 | 12/47 (hTERT-HPNE, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.777×** | -3.8 | 0.007 | 18/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.662×** | -3.4 | 0.030 | 19/46 (LoVo, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.801×** | -3.3 | 0.034 | 20/45 (LS 180, COLO 205, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.039 | 15/47 (SW 1088, RPMI-7951, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.821×** | -3.1 | 0.071 | 16/47 (HOP62, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5853. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 109 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0863× (z -19.0) |
| [[COLO 205 (line)]] | alt | 65.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -13.3) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -11.7) |
| [[A498 (line)]] | wt | 62.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +11.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 25.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -11.2) |
| [[A549 (line)]] | wt | 22.2 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 64.9 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.250× (z -9.2) |
| [[HT-29 (line)]] | alt | 38.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -9.6) |
| [[A-427 (line)]] | wt | 12.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.168× (z -10.3) |
| [[BT-474 (line)]] | alt | 55.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -11.9) |
| [[CHP-212 (line)]] | wt | 65.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.276× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 36.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 9.57 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.160× (z -9.8) |
| [[HOP62 (line)]] | alt | 52.5 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.344× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 32.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 48.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.5) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[NCI-H460 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.4) ⚠ cell-cycle shift, explains ~84% of this change |
| [[RKO (line)]] | wt | 31.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -12.8) ⚠ cell-cycle shift, explains ~84% of this change |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -11.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5853), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGRN]] | +0.64 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[ZFPM1]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SEMA3F]] | +0.58 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[RPS6KA1]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[PRKACA]] | +0.56 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[FGFRL1]] | +0.54 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[NOTCH1]] | +0.54 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[TMEM63B]] | +0.53 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SLC35B2]] | +0.53 | +0.62 / +0.30 | both halves | 2e-04 |  |
| [[FGFR3]] | +0.52 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[ADCY6]] | +0.52 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[BCAM]] | +0.51 | +0.59 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC22A15]] | -0.46 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[RSL1D1]] | -0.46 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ZFYVE9]] | -0.45 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[SMARCAL1]] | -0.45 | -0.42 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LFNG]] | B | LFNG activity raises TTYH3's level | lines that do not express LFNG (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without LFNG | 0.078 | ⚠ within organs, on part of the lines; also absent: TNFSF10, EPHA4, CXXC5; maybe low, not absent |
| [[COL9A3]] | B | COL9A3 activity raises TTYH3's level | lines that do not express COL9A3 (28) vs lines expressing it (22) | 1.41× lower at baseline in the lines without COL9A3 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000259639, AK4P3, LINC01169 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.446). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (16.5, -5.6); signed map (-15.9, 34.3). **Vector** length 107, 25.6% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.6 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +3.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.7 | +2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +2.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.9 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.8 | +2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.5 | +1.8 |
|  | [[Saquinavir (drug)]] 0.5 µM |  | +2.4 | +3.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -7.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.1 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | tweety family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:2,631,961-2,664,802 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1691 |
| Gene groups (HGNC) | Tweety family |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0H2](https://www.uniprot.org/uniprotkb/Q9C0H2) (Protein tweety homolog 3):

> Calcium-independent, swelling-dependent volume-regulated anion channel (VRAC-swell) which plays a pivotal role in the process of regulatory volume decrease (RVD) in the brain through the efflux of anions like chloride and organic osmolytes like glutamate (By similarity). Probable large-conductance Ca(2+)-activated chloride channel.

**Summary**, from NCBI Gene [80727](https://www.ncbi.nlm.nih.gov/gene/80727):

> This gene encodes a member of the tweety family of proteins. Members of this family function as chloride anion channels. The encoded protein functions as a calcium(2+)-activated large conductance chloride(-) channel. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:22222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22222) · Entrez [80727](https://www.ncbi.nlm.nih.gov/gene/80727) · UniProt [Q9C0H2](https://www.uniprot.org/uniprotkb/Q9C0H2) · Ensembl [ENSG00000136295](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136295)

## Data

Gene col 5853: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5853); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5853, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5853]; `tensor/DDL_lfc|DDL_z.npy` [5853]; `embed/gene_vectors.npy` [5853]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5853 or target_col == 5853). Every well: [[TTYH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTYH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
