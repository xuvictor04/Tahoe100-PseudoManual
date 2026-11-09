---
symbol: "NBEAL2"
type: "gene"
col: 8383
ensembl_id: "ENSG00000160796"
name: "neurobeachin like 2"
location: "3p21.31"
module: 2
arm: "+"
pooled_cpm: 14.67
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# NBEAL2

*neurobeachin like 2* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.55× (z +5.2, q 1e-04, up in 12 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Budesonide (drug)]] 5 µM: 1.32× (z +3.6, q 0.040, up in 17 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.512× (z -12.6, q 1e-33, down in 35 of 45 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.468× (z -9.5, q 7e-19, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSMF]] (+0.70, fdr 7e-06), [[KLHL17]] (+0.69, fdr 7e-06), [[ZDHHC8]] (+0.68, fdr 7e-06); moves opposite to [[XRN1]] (-0.62, fdr 8e-06), [[RNASEK]] (-0.57, fdr 1e-05), [[ASH1L]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ARHGAP8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +5.2 | 1e-04 | 12/24 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +4.1 | 0.011 | 17/46 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.9 | 0.022 | 8/36 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.040 | 17/46 (A549, Panc 03.27, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 1.32× | +3.3 | 0.13 | 14/44 (HOP62, SW48, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.17 | 8/46 (A549, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.1 | 0.18 | 9/47 (AsPC-1, A498, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.31× | +3.0 | 0.19 | 8/45 (LS 180, SNU-423, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8383.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.512×** | -12.6 | 1e-33 | 35/45 (HEC-1-A, RKO, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.468×** | -9.5 | 7e-19 | 31/43 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -8.7 | 7e-16 | 26/44 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.486×** | -8.7 | 7e-16 | 33/45 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.551×** | -7.9 | 3e-13 | 28/45 (HS-578T, A-172, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.372×** | -6.9 | 6e-10 | 27/44 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.456×** | -5.5 | 4e-06 | 24/41 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.649×** | -4.9 | 8e-05 | 24/45 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.731×** | -4.2 | 0.002 | 17/44 (SW480, A-172, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.739×** | -4.0 | 0.003 | 15/46 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.592×** | -3.7 | 0.013 | 17/30 (LS 180, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.748×** | -3.3 | 0.050 | 9/46 (A549, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -3.2 | 0.059 | 16/45 (J82, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.778×** | -3.2 | 0.065 | 6/47 (CHP-212, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 41.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 37.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -13.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.265× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A549 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0861× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0402× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 7.79 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.119× (z -8.9) |
| [[HT-29 (line)]] | alt | 22.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -10.6) |
| [[KATO III (line)]] | alt | 26.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -8.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -12.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 8.15 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0665× (z -8.5) |
| [[SNU-423 (line)]] | alt | 5.12 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -10.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSMF]] | +0.70 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[KLHL17]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ZDHHC8]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[GNAZ]] | +0.68 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SH3GLB2]] | +0.67 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[TRABD]] | +0.66 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[SDC3]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TCF3]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[JMJD7]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[GPAT4]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[GLB1L2]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRN1]] | -0.62 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[RNASEK]] | -0.57 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ASH1L]] | -0.57 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[DCP1A]] | -0.56 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[NIPBL]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 | same gene group |
| [[SLU7]] | -0.56 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ARID4B]] | -0.55 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PAXIP1-AS2]] | -0.55 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[CIR1]] | -0.55 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[C3orf38]] | -0.54 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[NBR1]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP8]] | B | ARHGAP8 activity raises NBEAL2's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without ARHGAP8 | 0.005 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[GLB1L2]] | B | GLB1L2 activity raises NBEAL2's level | lines that do not express GLB1L2 (16) vs lines expressing it (34) | 1.76× lower at baseline in the lines without GLB1L2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CHDH, PLS1, ASTL |
| [[SLC29A2]] | B | SLC29A2 activity raises NBEAL2's level | lines that do not express SLC29A2 (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without SLC29A2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC27A2, EPHA10, OCLN; its own permutation p |
| [[LAMA5]] | B | LAMA5 activity raises NBEAL2's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.59× lower at baseline in the lines without LAMA5 | 0.097 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.9, -24.6); signed map (-44.4, -10.0). **Vector** length 86.7, 18.0% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +0.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.0 | +2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.5 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -8.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.3 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.3 | -12.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.5 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | neurobeachin like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:46,979,666-47,009,704 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0540 |
| Gene groups (HGNC) | WD repeat domain containing; BEACH domain containing ; Armadillo like helical domain containing |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZNJ1](https://www.uniprot.org/uniprotkb/Q6ZNJ1) (Neurobeachin-like protein 2):

> Probably involved in thrombopoiesis. Plays a role in the development or secretion of alpha-granules, that contain several growth factors important for platelet biogenesis.

**Summary**, from NCBI Gene [23218](https://www.ncbi.nlm.nih.gov/gene/23218):

> The protein encoded by this gene contains a beige and Chediak-Higashi (BEACH) domain and multiple WD40 domains, and may play a role in megakaryocyte alpha-granule biogenesis. Mutations in this gene are a cause of gray platelet syndrome. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:31928](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31928) · Entrez [23218](https://www.ncbi.nlm.nih.gov/gene/23218) · UniProt [Q6ZNJ1](https://www.uniprot.org/uniprotkb/Q6ZNJ1) · Ensembl [ENSG00000160796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160796)

## Data

Gene col 8383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8383); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8383]; `tensor/DDL_lfc|DDL_z.npy` [8383]; `embed/gene_vectors.npy` [8383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8383 or target_col == 8383). Every well: [[NBEAL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBEAL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
