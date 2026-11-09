---
symbol: "CUL9"
type: "gene"
col: 3391
ensembl_id: "ENSG00000112659"
name: "cullin 9"
location: "6p21.1"
module: 127
arm: "+"
pooled_cpm: 21.09
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# CUL9

*cullin 9* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.62× (z +7.2, q 3e-10, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.427× (z -12.8, q 1e-34, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCRIB]] (+0.67, fdr 7e-06), [[PCNX3]] (+0.63, fdr 1e-05), [[ACSF3]] (+0.62, fdr 3e-05); moves opposite to [[PCF11-AS1]] (-0.51, fdr 2e-04), [[CERT1]] (-0.48, fdr 7e-05), [[LEPR]] (-0.48, fdr 1e-04).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3391.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +7.2 | 3e-10 | 31/48 (LOX-IMVI, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.6 | 7e-06 | 1/48 (NCI-H1573) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.39×** | +4.9 | 1e-04 | 22/48 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.25× | +3.2 | 0.23 | 13/47 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3391.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.427×** | -12.8 | 1e-34 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.549×** | -12.7 | 1e-34 | 44/47 (Panc 03.27, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.431×** | -12.6 | 3e-34 | 43/47 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.552×** | -8.9 | 7e-17 | 32/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.579×** | -8.2 | 2e-14 | 33/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.613×** | -5.0 | 6e-05 | 24/48 (PANC-1, NCI-H23, …) | rises with dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -4.3 | 0.001 | 25/47 (C32, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.752×** | -4.3 | 0.001 | 23/48 (NCI-H460, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.659×** | -4.2 | 0.001 | 21/48 (HOP62, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.759×** | -4.1 | 0.002 | 19/47 (SW 1271, SK-MEL-2, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.767×** | -4.0 | 0.004 | 19/47 (RKO, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.766×** | -3.9 | 0.004 | 21/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.685×** | -3.9 | 0.005 | 18/46 (J82, NCI-H23, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.834× | -3.9 | 0.005 | 19/48 (CHP-212, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.791×** | -3.5 | 0.017 | 16/47 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sonidegib (drug)]] 0.5 µM |  | **0.755×** | -3.0 | 0.094 | 9/47 (LOX-IMVI, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3391. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 35.1 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -13.8) |
| [[SW480 (line)]] | alt | 18.5 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -12.9) |
| [[LOX-IMVI (line)]] | wt | 23.5 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.264× (z -10.1) |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -12.1) |
| [[J82 (line)]] | alt | 19.6 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0472× (z -13.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 42.8 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.135× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 17.7 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.260× (z -10.7) |
| [[RKO (line)]] | wt | 21.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -10.7) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -10.3) |
| [[LoVo (line)]] | wt | 18.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.301× (z -8.6) |
| [[C-33 A (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -9.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0623× (z -11.4) |
| [[H4 (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.318× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 19.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -11.1) |
| [[LS 180 (line)]] | wt | 18.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 21.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 17.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.193× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.256× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 36.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -11.4) |
| [[SNU-423 (line)]] | alt | 21.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -8.8) |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -11.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3391), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCRIB]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PCNX3]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ACSF3]] | +0.62 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[PRPF31]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[RNF123]] | +0.60 | +0.42 / +0.63 | both halves | 4e-05 | same gene group |
| [[LAS1L]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ABCF3]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[BAP1]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PIP4K2B]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[EP400]] | +0.57 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[DNAJC14]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PIGO]] | +0.55 | +0.44 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCF11-AS1]] | -0.51 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[CERT1]] | -0.48 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[LEPR]] | -0.48 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[NKIRAS1]] | -0.47 | -0.31 / -0.30 | both halves | 2e-04 |  |
| [[RNASEK]] | -0.47 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[OXR1]] | -0.46 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ZNF821]] | -0.46 | -0.22 / -0.44 | both halves | 6e-04 |  |
| [[OXR1-AS1]] | -0.46 | -0.17 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[NDUFC1]] | -0.45 | -0.20 / -0.44 | both halves | 7e-04 |  |
| [[TBPL1]] | -0.45 | -0.26 / -0.39 | both halves | 4e-04 |  |
| [[SMIM27]] | -0.45 | -0.11 / -0.48 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CUL9's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.1, -26.3); signed map (-13.3, -30.6). **Vector** length 81.5, 16.6% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +0.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.7 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.6 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +3.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +0.1 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.6 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.3 | -12.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -4.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -12.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -0.7 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | -1.9 | -2.5 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | cullin 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,182,184-43,224,587 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H7AP1, KIAA0708, PARC |
| Gene groups (HGNC) | Ring finger proteins; Cullins; RBR E3 ubiquitin ligases; Armadillo like helical domain containing |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWT3](https://www.uniprot.org/uniprotkb/Q8IWT3) (Cullin-9):

> Core component of a Cul9-RING ubiquitin-protein ligase complex composed of CUL9 and RBX1. The CUL9-RBX1 complex mediates ubiquitination and subsequent degradation of BIRC5 and is required to maintain microtubule dynamics and genome integrity. Acts downstream of the 3M complex, which inhibits the ubiquitination of BIRC5. The CUL9-RBX1 complex also mediates mono-ubiquitination of p53/TP53. Acts as a cytoplasmic anchor protein in p53/TP53-associated protein complex. Regulates the subcellular …

**Summary**, from NCBI Gene [23113](https://www.ncbi.nlm.nih.gov/gene/23113):

> Predicted to enable ubiquitin ligase complex scaffold activity. Involved in microtubule cytoskeleton organization; protein ubiquitination; and regulation of mitotic nuclear division. Part of cullin-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15982) · Entrez [23113](https://www.ncbi.nlm.nih.gov/gene/23113) · UniProt [Q8IWT3](https://www.uniprot.org/uniprotkb/Q8IWT3) · Ensembl [ENSG00000112659](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112659)

## Data

Gene col 3391: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3391); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3391, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3391]; `tensor/DDL_lfc|DDL_z.npy` [3391]; `embed/gene_vectors.npy` [3391]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3391 or target_col == 3391). Every well: [[CUL9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUL9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
