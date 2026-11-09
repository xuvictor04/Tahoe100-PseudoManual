---
symbol: "ACTR6"
type: "gene"
col: 1099
ensembl_id: "ENSG00000075089"
name: "actin related protein 6"
location: "12q23.1"
module: 3
arm: "+"
pooled_cpm: 36.36
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ACTR6

*actin related protein 6* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.87× (z +10.7, q 5e-24, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.661× (z -7.0, q 1e-09, down in 37 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.664× (z -3.6, q 0.078, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.159×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.241×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.280×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCD4]] (+0.64, fdr 1e-05), [[MED31]] (+0.63, fdr 1e-05), [[RNF181]] (+0.62, fdr 1e-05); moves opposite to [[ADCK1]] (-0.63, fdr 3e-05), [[TMEM147-AS1]] (-0.60, fdr 3e-05), [[CYP4V2]] (-0.56, fdr 9e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SUGP1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1099.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +10.7 | 5e-24 | 44/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +10.4 | 5e-23 | 44/48 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +10.3 | 1e-22 | 43/48 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +8.2 | 3e-14 | 37/48 (NCI-H1573, LOX-IMVI, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +7.4 | 1e-11 | 36/48 (NCI-H1573, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +7.2 | 7e-11 | 34/48 (NCI-H1573, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +4.9 | 1e-04 | 29/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +4.7 | 2e-04 | 26/46 (HT-29, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.20×** | +4.5 | 5e-04 | 18/48 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.001 | 17/48 (A549, BT-474, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.004 | 25/48 (NCI-H2030, SHP-77, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **1.25×** | +3.9 | 0.005 | 18/47 (SW48, SW480, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.24×** | +3.7 | 0.008 | 19/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.2 | 0.047 | 14/43 (NCI-H1792, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1099.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.159×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.241×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 0.280×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.661×** | -7.0 | 1e-09 | 37/48 (A498, CFPAC-1, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.664×** | -3.6 | 0.078 | 22/48 (Hs 766T, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.812×** | -3.5 | 0.078 | 22/46 (SW48, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.827× | -3.2 | 0.16 | 15/48 (SNU-423, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.822× | -3.2 | 0.16 | 21/47 (HepG2/C3A, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.879× | -3.1 | 0.18 | 3/48 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.1 | 0.18 | 14/48 (NCI-H460, NCI-H2347, …) | rises with dose | composition shift |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.828× | -3.0 | 0.18 | 7/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1099. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 32.5 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.59× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 32.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.24× (z +10.3) | — |
| [[A-427 (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[HCT15 (line)]] | alt | 44.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.241× (z -9.9) |
| [[SW 900 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 40.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1099), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCD4]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[MED31]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[RNF181]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ECI2]] | +0.62 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[INTS4]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[EMC4]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ZNHIT3]] | +0.61 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[HACL1]] | +0.61 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[VRK3]] | +0.60 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[DPY30]] | +0.60 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[ZCCHC17]] | +0.60 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[KIAA1143]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCK1]] | -0.63 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[TMEM147-AS1]] | -0.60 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[CYP4V2]] | -0.56 | -0.49 / -0.37 | both halves | 9e-05 |  |
| [[PTP4A3]] | -0.56 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RAP2C-AS1]] | -0.55 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[SRSF1]] | -0.55 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[EME2]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[MTA2]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PIEZO1]] | -0.54 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[HNRNPK]] | -0.53 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[TRIM28]] | -0.52 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[PSPC1]] | -0.52 | -0.46 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUGP1]] | C | SUGP1's natural level weakens ACTR6's drug response | SUGP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.05; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.516). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-21.9, -47.9); signed map (-24.2, 9.0). **Vector** length 90.8, 20.7% of its response variance represented; |z| ≥ 3 in 753 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.9 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +8.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.5 | +3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.4 | +2.4 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.6 | +1.4 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | +1.6 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -7.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.7 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:100,199,122-100,241,865 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARP6, FLJ13433 |
| Gene groups (HGNC) | SRCAP complex subunits; Actin related proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZN1](https://www.uniprot.org/uniprotkb/Q9GZN1) (Actin-related protein 6):

> Required for formation and/or maintenance of proper nucleolar structure and function. Plays a dual role in the regulation of ribosomal DNA (rDNA) transcription (By similarity). In the presence of high glucose, maintains active rDNA transcription through H2A.Z deposition and under glucose starvation, is required for the repression of rDNA transcription, and this function may be independent of H2A.Z (By similarity).

**Summary**, from NCBI Gene [64431](https://www.ncbi.nlm.nih.gov/gene/64431):

> Predicted to enable nucleosome binding activity. Involved in nucleolus organization. Located in nucleolus. Part of Swr1 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24025](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24025) · Entrez [64431](https://www.ncbi.nlm.nih.gov/gene/64431) · UniProt [Q9GZN1](https://www.uniprot.org/uniprotkb/Q9GZN1) · Ensembl [ENSG00000075089](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075089)

## Data

Gene col 1099: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1099); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1099, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1099]; `tensor/DDL_lfc|DDL_z.npy` [1099]; `embed/gene_vectors.npy` [1099]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1099 or target_col == 1099). Every well: [[ACTR6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTR6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
