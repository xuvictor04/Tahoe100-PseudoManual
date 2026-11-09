---
symbol: "CLHC1"
type: "gene"
col: 8612
ensembl_id: "ENSG00000162994"
name: "clathrin heavy chain linker domain containing 1"
location: "2p16.1"
module: 88
arm: "+"
pooled_cpm: 17.58
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# CLHC1

*clathrin heavy chain linker domain containing 1* — 2p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +6.8, q 5e-09, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.310× (z -11.4, q 2e-27, down in 40 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.441× (z -8.0, q 3e-13, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB30-DT]] (+0.82, fdr 1e-05), [[ZC3H4]] (+0.78, fdr 1e-05), [[PPP3CB-AS1]] (+0.78, fdr 3e-05); moves opposite to [[FAM118A]] (-0.69, fdr 7e-04), [[TSPAN33]] (-0.69, fdr 3e-05), [[MAST3]] (-0.69, fdr 4e-04).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8612.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.8 | 5e-09 | 34/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.6 | 8e-06 | 34/48 (SW1417, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +5.2 | 4e-05 | 24/46 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +4.5 | 9e-04 | 27/45 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.1 | 0.006 | 6/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.008 | 21/48 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.46×** | +3.6 | 0.029 | 19/47 (LS 180, NCI-H1573, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.035 | 17/47 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.080 | 11/48 (AsPC-1, Panc 03.27, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +3.2 | 0.086 | 15/47 (A-172, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8612.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.310×** | -11.4 | 2e-27 | 40/46 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.376×** | -9.5 | 5e-19 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.441×** | -8.0 | 3e-13 | 37/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.472×** | -7.3 | 4e-11 | 35/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.520×** | -5.7 | 1e-06 | 29/43 (A-427, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.663×** | -3.9 | 0.010 | 23/48 (HepG2/C3A, A-427, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.483×** | -3.7 | 0.017 | 21/45 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.489×** | -3.6 | 0.019 | 18/48 (KATO III, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~72% of this change | **0.696×** | -3.5 | 0.026 | 21/44 (HS-578T, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.711×** | -3.3 | 0.050 | 20/47 (C-33 A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.709× | -3.0 | 0.12 | 18/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.6 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.177× (z -11.3) |
| [[A-427 (line)]] | wt | 32.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.141× (z -11.4) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0384× (z -15.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -12.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.215× (z -8.6) |
| [[KATO III (line)]] | alt | 32.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -13.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 9.53 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +11.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -10.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 9.58 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0759× (z -10.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0981× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 27.8 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.169× (z -8.7) |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0907× (z -10.3) ⚠ transcription drop; cell-cycle shift, explains ~72% of this change |
| [[hTERT-HPNE (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -11.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.232× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0960× (z -11.0) |
| [[LS 180 (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0846× (z -9.0) |
| [[A-172 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB30-DT]] | +0.82 | +0.86 / +0.56 | both halves | 1e-05 |  |
| [[ZC3H4]] | +0.78 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | +0.78 | +0.76 / +0.45 | both halves | 3e-05 |  |
| [[ST7L]] | +0.77 | +0.78 / +0.61 | both halves | 7e-06 |  |
| [[MCPH1]] | +0.76 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[GABPB2]] | +0.75 | +0.78 / +0.47 | both halves | 2e-05 |  |
| [[TASOR]] | +0.75 | +0.80 / +0.49 | both halves | 1e-05 |  |
| [[LEKR1]] | +0.75 | +0.80 / +0.44 | both halves | 3e-05 |  |
| [[METTL6]] | +0.74 | +0.76 / +0.42 | both halves | 4e-05 |  |
| [[ZNF655]] | +0.74 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | +0.74 | +0.80 / +0.31 | both halves | 2e-04 |  |
| [[PCBP1-AS1]] | +0.73 | +0.73 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.69 | -0.70 / -0.21 | both halves | 7e-04 |  |
| [[TSPAN33]] | -0.69 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[MAST3]] | -0.69 | -0.68 / -0.25 | both halves | 4e-04 |  |
| [[CBFA2T2]] | -0.69 | -0.74 / -0.39 | both halves | 5e-05 |  |
| [[GMCL1]] | -0.68 | -0.73 / -0.38 | both halves | 7e-05 |  |
| [[HEBP1]] | -0.67 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[CARHSP1]] | -0.67 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[YIF1B]] | -0.66 | -0.69 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[STK32C]] | -0.65 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[EFNA3]] | -0.65 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[SLC9A6]] | -0.65 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[SLC29A4]] | -0.65 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[DNAAF3]] | -0.65 | -0.44 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CLHC1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ALOX12P2-1]] | B | ALOX12P2-1 activity raises CLHC1's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.45× lower at baseline in the lines without ALOX12P2-1 | 0.074 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.850). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (4.5, 8.0); signed map (17.6, -25.6). **Vector** length 73.4, 15.2% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.6 | +1.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | +1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | +0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -3.9 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | clathrin heavy chain linker domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.1 — chr2:55,172,547-55,232,563 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31438; previously C2orf63 |
| Gene groups (HGNC) | TSNAXIP1 domain containing |
| Matched by | ensembl_id |

UniProt [Q8NHS4](https://www.uniprot.org/uniprotkb/Q8NHS4) carries no function annotation.

**Summary**, from NCBI Gene [130162](https://www.ncbi.nlm.nih.gov/gene/130162):

> Predicted to enable AP-1 adaptor complex binding activity and AP-3 adaptor complex binding activity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26453) · Entrez [130162](https://www.ncbi.nlm.nih.gov/gene/130162) · UniProt [Q8NHS4](https://www.uniprot.org/uniprotkb/Q8NHS4) · Ensembl [ENSG00000162994](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162994)

## Data

Gene col 8612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8612); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8612]; `tensor/DDL_lfc|DDL_z.npy` [8612]; `embed/gene_vectors.npy` [8612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8612 or target_col == 8612). Every well: [[CLHC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLHC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
