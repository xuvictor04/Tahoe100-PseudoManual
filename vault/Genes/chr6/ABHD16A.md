---
symbol: "ABHD16A"
type: "gene"
col: 12871
ensembl_id: "ENSG00000204427"
name: "abhydrolase domain containing 16A, phospholipase"
location: "6p21.33"
module: 17
arm: "+"
pooled_cpm: 16.72
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ABHD16A

*abhydrolase domain containing 16A, phospholipase* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.35× (z +8.0, q 5e-13, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.687× (z -10.3, q 6e-22, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRCH4]] (+0.61, fdr 1e-05), [[PIP4P1]] (+0.59, fdr 3e-05), [[BAD]] (+0.57, fdr 3e-05); moves opposite to [[BEND3]] (-0.53, fdr 8e-05), [[SPOPL-DT]] (-0.52, fdr 7e-05), [[ABCA15P]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BCAM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12871.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +8.0 | 5e-13 | 27/47 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +6.6 | 1e-08 | 26/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +6.5 | 1e-08 | 24/48 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +6.3 | 4e-08 | 25/48 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +4.9 | 1e-04 | 14/48 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.4 | 9e-04 | 14/40 (HEC-1-A, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.012 | 8/44 (HS-578T, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.19× | +3.4 | 0.054 | 13/47 (J82, MIA PaCa-2, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.066 | 7/46 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.066 | 4/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | 1.18× | +3.2 | 0.066 | 10/46 (LoVo, RKO, …) | top dose only |  |
| [[Saquinavir (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.083 | 8/45 (Hs 766T, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.18× | +3.1 | 0.083 | 12/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.17× | +3.1 | 0.090 | 9/47 (A-172, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12871.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -10.3 | 6e-22 | 27/46 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.742×** | -5.8 | 2e-06 | 23/47 (C-33 A, AN3 CA, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.738×** | -5.7 | 2e-06 | 22/46 (LS 180, A-172, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.784×** | -4.7 | 3e-04 | 17/47 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.860× | -4.1 | 0.004 | 17/48 (MIA PaCa-2, Panc 03.27, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.667×** | -4.1 | 0.004 | 12/38 (SW48, A549, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.818×** | -3.9 | 0.008 | 14/47 (NCI-H23, MIA PaCa-2, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.818×** | -3.7 | 0.012 | 10/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.818×** | -3.7 | 0.012 | 15/47 (hTERT-HPNE, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.874× | -3.7 | 0.012 | 15/48 (RPMI-7951, AN3 CA, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.702×** | -3.6 | 0.019 | 7/48 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.829×** | -3.5 | 0.022 | 8/47 (NCI-H661, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.838× | -3.4 | 0.028 | 4/47 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.848× | -3.2 | 0.054 | 4/47 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.891× | -3.2 | 0.054 | 7/48 (PANC-1, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 39.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.117× (z -8.6) |
| [[Hs 766T (line)]] | wt | 14.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -8.6) |
| [[LoVo (line)]] | wt | 20.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -11.6) |
| [[A549 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[H4 (line)]] | wt | 12.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 24.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.131× (z -8.9) ⚠ toxic |
| [[RKO (line)]] | wt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.147× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~6% of this change |
| [[A-172 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRCH4]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PIP4P1]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[BAD]] | +0.57 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[YY1AP1]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ARAF]] | +0.56 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[NUDT14]] | +0.56 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[BCL3]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 | same gene group |
| [[MBD6]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ALAD]] | +0.53 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[C4orf33]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[NECAP1]] | +0.52 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[ROGDI]] | +0.52 | +0.43 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEND3]] | -0.53 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[SPOPL-DT]] | -0.52 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[ABCA15P]] | -0.52 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[PDK1-AS1]] | -0.52 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[CCT4]] | -0.51 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[BNC1]] | -0.51 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[RAP1GDS1]] | -0.51 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[HSPH1]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ADCY7]] | -0.49 | -0.46 / -0.41 | both halves | 4e-05 | same gene group |
| [[SLC4A10]] | -0.49 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[ARHGAP22]] | -0.49 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[SMG1P6]] | -0.48 | -0.51 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAM]] | B | BCAM activity raises ABHD16A's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without BCAM | 0.018 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[TM4SF19]] | B | TM4SF19 activity lowers ABHD16A's level | lines that do not express TM4SF19 (20) vs lines expressing it (30) | 1.28× higher at baseline in the lines without TM4SF19 | 0.051 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.434). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (0.9, -34.7); signed map (-6.9, 19.8). **Vector** length 74.8, 12.7% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~6% of this change | +2.8 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.7 | +6.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +4.4 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.1 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +3.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.9 | -5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -10.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 16A, phospholipase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,686,955-31,703,356 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NG26, D6S82E; previously BAT5 |
| Gene groups (HGNC) | Abhydrolase domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O95870](https://www.uniprot.org/uniprotkb/O95870) (Phosphatidylserine lipase ABHD16A):

> Phosphatidylserine (PS) lipase that mediates the hydrolysis of phosphatidylserine to generate lysophosphatidylserine (LPS) (By similarity). LPS constitutes a class of signaling lipids that regulates immunological and neurological processes (By similarity). Has no activity towards diacylglycerol, triacylglycerol or lysophosphatidylserine lipase. Also has monoacylglycerol lipase activity, with preference for 1-(9Z,12Z-octadecadienoyl)-glycerol (1-LG) and …

**Summary**, from NCBI Gene [7920](https://www.ncbi.nlm.nih.gov/gene/7920):

> A cluster of genes, BAT1-BAT5, has been localized in the vicinity of the genes for tumor necrosis factor alpha and tumor necrosis factor beta. These genes are all within the human major histocompatibility complex class III region. The protein encoded by this gene is thought to be involved in some aspects of immunity. Alternatively spliced transcript variants have been described. [provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:13921](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13921) · Entrez [7920](https://www.ncbi.nlm.nih.gov/gene/7920) · UniProt [O95870](https://www.uniprot.org/uniprotkb/O95870) · Ensembl [ENSG00000204427](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204427)

## Data

Gene col 12871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12871); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12871]; `tensor/DDL_lfc|DDL_z.npy` [12871]; `embed/gene_vectors.npy` [12871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12871 or target_col == 12871). Every well: [[ABHD16A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD16A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
