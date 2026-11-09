---
symbol: "DPCD"
type: "gene"
col: 9254
ensembl_id: "ENSG00000166171"
name: "deleted in primary ciliary dyskinesia homolog (mouse)"
location: "10q24.32"
module: 103
arm: "+"
pooled_cpm: 17.32
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# DPCD

*deleted in primary ciliary dyskinesia homolog (mouse)* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.43× (z +4.1, q 0.020, up in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.35× (z +3.5, q 0.095, up in 16 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 3.47×, Hs 766T 5.70×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.565× (z -6.3, q 2e-07, down in 30 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.680× (z -6.2, q 2e-07, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GYS1]] (+0.64, fdr 1e-05), [[PEX3]] (+0.63, fdr 1e-05), [[NDUFB8]] (+0.60, fdr 1e-05); moves opposite to [[REEP3]] (-0.52, fdr 9e-05), [[EPM2A]] (-0.52, fdr 2e-04), [[PCBD2]] (-0.51, fdr 1e-04).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NRN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9254.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 3.47×, Hs 766T 5.70×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.43×** | +4.1 | 0.020 | 25/48 (A498, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.39×** | +3.8 | 0.041 | 22/48 (PANC-1, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.095 | 16/45 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 1.32× | +3.2 | 0.21 | 18/47 (PANC-1, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | 1.32× | +3.0 | 0.23 | 13/32 (A-172, Hs 766T, …) | rises with dose | composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | 1.30× | +3.0 | 0.23 | 12/47 (LS 180, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9254.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.565×** | -6.3 | 2e-07 | 30/45 (RKO, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.680×** | -6.2 | 2e-07 | 34/48 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.620×** | -5.5 | 7e-06 | 30/47 (C32, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.624×** | -5.4 | 8e-06 | 25/46 (C32, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.629×** | -5.3 | 1e-05 | 31/47 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.740×** | -4.8 | 1e-04 | 25/47 (C32, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.666×** | -4.7 | 2e-04 | 26/47 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.676×** | -4.5 | 5e-04 | 22/46 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.725×** | -3.7 | 0.014 | 21/47 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.733×** | -3.6 | 0.021 | 22/48 (NCI-H460, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.738×** | -3.5 | 0.025 | 19/46 (H4, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9254. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 25.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -11.0) |
| [[A-172 (line)]] | wt | 24.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | — |
| [[A-427 (line)]] | wt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -9.7) |
| [[C-33 A (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.210× (z -9.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.101× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0966× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 25.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.8) |
| [[Hs 766T (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0868× (z -10.4) ⚠ toxic |
| [[RKO (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0498× (z -16.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -9.0) |
| [[SNU-423 (line)]] | alt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.5) |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.323× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9254), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GYS1]] | +0.64 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[PEX3]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[NDUFB8]] | +0.60 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[DDX41]] | +0.57 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[CABIN1]] | +0.56 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[CFAP36]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CETN2]] | +0.56 | +0.37 / +0.56 | both halves | 7e-05 |  |
| [[PFKFB4]] | +0.56 | +0.54 / +0.44 | both halves | 3e-05 | same gene group |
| [[WDR54]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[NPHP1]] | +0.56 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[TMEM67]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[SCAND2P]] | +0.55 | +0.68 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REEP3]] | -0.52 | -0.37 / -0.55 | both halves | 9e-05 |  |
| [[EPM2A]] | -0.52 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[PCBD2]] | -0.51 | -0.45 / -0.34 | both halves | 1e-04 | same gene group |
| [[B3GLCT]] | -0.50 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[ADSS2]] | -0.50 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[FGD5-AS1]] | -0.49 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[DPH5-DT]] | -0.48 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[SLC2A9]] | -0.48 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[AVEN]] | -0.48 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[JADE3]] | -0.47 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[OXCT1]] | -0.47 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[CFAP161]] | -0.47 | -0.46 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRN1]] | B | NRN1 activity raises DPCD's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.22× lower at baseline in the lines without NRN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[HDAC6]] | B | HDAC6 activity lowers DPCD's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.9, -18.3); signed map (-37.8, 23.2). **Vector** length 86.1, 21.6% of its response variance represented; |z| ≥ 3 in 620 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +1.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +3.4 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +0.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.5 | +1.2 |
|  | [[Ritonavir (drug)]] 0.5 µM |  | +1.5 | +2.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.1 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.4 | -5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | deleted in primary ciliary dyskinesia homolog (mouse) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:101,570,560-101,609,662 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP566F084, RP11-529I10.4 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVM2](https://www.uniprot.org/uniprotkb/Q9BVM2) (Protein DPCD):

> May play a role in the formation or function of ciliated cells.

**Summary**, from NCBI Gene [25911](https://www.ncbi.nlm.nih.gov/gene/25911):

> This gene in mouse encodes a protein that may be involved in the generation and maintenance of ciliated cells. In mouse, expression of this gene increases during ciliated cell differentiation, and disruption of this gene has been linked to primary ciliary dyskinesia. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:24542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24542) · Entrez [25911](https://www.ncbi.nlm.nih.gov/gene/25911) · UniProt [Q9BVM2](https://www.uniprot.org/uniprotkb/Q9BVM2) · Ensembl [ENSG00000166171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166171)

## Data

Gene col 9254: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9254); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9254, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9254]; `tensor/DDL_lfc|DDL_z.npy` [9254]; `embed/gene_vectors.npy` [9254]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9254 or target_col == 9254). Every well: [[DPCD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPCD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
