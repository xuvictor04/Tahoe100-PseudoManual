---
symbol: "TYSND1"
type: "gene"
col: 7994
ensembl_id: "ENSG00000156521"
name: "trypsin like peroxisomal matrix peptidase 1"
location: "10q22.1"
module: 10
arm: "+"
pooled_cpm: 7.37
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TYSND1

*trypsin like peroxisomal matrix peptidase 1* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.66× (z +15.4, q 0e+00, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.437× (z -9.3, q 9e-18, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (60 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 40 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRM1]] (+0.70, fdr 1e-05), [[SIAH2-AS1]] (+0.69, fdr 3e-04), [[CTBP1-DT]] (+0.67, fdr 1e-04); moves opposite to [[F11R]] (-0.60, fdr 1e-04), [[PIGH]] (-0.59, fdr 0.002, ⚠ not reproduced), [[STAM2]] (-0.58, fdr 3e-05), [[SERAC1]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +15.4 | 0e+00 | 39/42 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.81×** | +9.3 | 3e-18 | 30/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +8.8 | 4e-16 | 26/38 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +8.0 | 3e-13 | 29/41 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +6.7 | 2e-09 | 20/47 (HOP62, SW1417, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.79×** | +6.5 | 9e-09 | 28/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.50×** | +4.5 | 5e-04 | 12/43 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +4.5 | 5e-04 | 5/13 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.001 | 12/47 (C-33 A, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.2 | 0.002 | 12/34 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.004 | 9/47 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.007 | 9/45 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.6 | 0.012 | 5/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.023 | 14/44 (SW480, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.038 | 5/44 (A549, SW480, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.041 | 6/46 (SW1417, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.043 | 4/47 (NCI-H460, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7994.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.437×** | -9.3 | 9e-18 | 34/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.496×** | -7.9 | 9e-13 | 29/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.589×** | -6.0 | 5e-07 | 24/46 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.642×** | -5.0 | 9e-05 | 21/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.667×** | -4.6 | 6e-04 | 20/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.681×** | -4.3 | 0.001 | 14/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.712×** | -3.8 | 0.011 | 9/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.725×** | -3.6 | 0.020 | 15/47 (KATO III, LOX-IMVI, …) | top dose only |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.741×** | -3.4 | 0.045 | 9/47 (SW1417, SNU-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.747×** | -3.3 | 0.056 | 7/47 (A549, NCI-H2347, …) | two highest doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.756× | -3.0 | 0.11 | 5/47 (C-33 A, hTERT-HPNE, …) | top dose only | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.828× | -3.0 | 0.11 | 9/45 (H4, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.1 | 1 | 5 (3 ⚠) | [[Selinexor (drug)]] 5 µM 2.51× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -14.5) |
| [[SW480 (line)]] | alt | 8.20 | 1 | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -13.0) |
| [[SW48 (line)]] | wt | 21.6 | 0 | 2 | — | [[Decitabine (drug)]] 0.05 µM 0.0984× (z -9.6) |
| [[BT-474 (line)]] | alt | 8.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0827× (z -9.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 3.05 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0583× (z -9.4) |
| [[HOP62 (line)]] | alt | 7.75 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[J82 (line)]] | alt | 5.02 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0634× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 11.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 36 of them with an alert (⚠; 36 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRM1]] | +0.70 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SIAH2-AS1]] | +0.69 | +0.66 / +0.28 | both halves | 3e-04 |  |
| [[CTBP1-DT]] | +0.67 | +0.63 / +0.34 | both halves | 1e-04 |  |
| [[PLBD1-AS1]] | +0.67 | +0.65 / +0.37 | both halves | 9e-05 |  |
| [[DHRS4-AS1]] | +0.65 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[CDNF]] | +0.65 | +0.66 / +0.31 | both halves | 2e-04 |  |
| [[ZNF747]] | +0.65 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[ADCK1]] | +0.64 | +0.69 / +0.20 | both halves | 7e-04 |  |
| [[MYLK4]] | +0.63 | +0.54 / +0.24 | both halves | 4e-04 |  |
| [[PIGW]] | +0.62 | +0.48 / +0.31 | both halves | 2e-04 |  |
| [[NEK8]] | +0.62 | +0.61 / +0.30 | both halves | 2e-04 |  |
| [[KICS2]] | +0.61 | +0.68 / +0.29 | both halves | 3e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[F11R]] | -0.60 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[PIGH]] | -0.59 | -0.48 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[STAM2]] | -0.58 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SERAC1]] | -0.58 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[TPMT]] | -0.58 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[CEP131]] | -0.57 | -0.43 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[GNAI2]] | -0.57 | -0.46 / -0.04 | ⚠ not reproduced | 0.005 |  |
| [[CLTCL1]] | -0.56 | -0.41 / -0.16 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TYSND1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.1, 13.7); signed map (26.9, -14.6). **Vector** length 64.5, 9.88% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.7 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +15.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -0.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | trypsin like peroxisomal matrix peptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:70,137,981-70,146,700 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC34695, NET41 |
| Reactome | 3 pathways, smallest: TYSND1 cleaves peroxisomal proteins; Peroxisomal protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2T9J0](https://www.uniprot.org/uniprotkb/Q2T9J0) (Peroxisomal leader peptide-processing protease):

> Peroxisomal protease that mediates both the removal of the leader peptide from proteins containing a PTS2 target sequence and processes several PTS1-containing proteins. Catalyzes the processing of PTS1-proteins involved in the peroxisomal beta-oxidation of fatty acids.

**Summary**, from NCBI Gene [219743](https://www.ncbi.nlm.nih.gov/gene/219743):

> This gene encodes a protease that removes the N-terminal peroxisomal targeting signal (PTS2) from proteins produced in the cytosol, thereby facilitating their import into the peroxisome. The encoded protein is also capable of removing the C-terminal peroxisomal targeting signal (PTS1) from proteins in the peroxisomal matrix. The full-length protein undergoes self-cleavage to produce shorter, potentially inactive, peptides. Alternative splicing results in multiple transcript variants for this …

**Accessions** — [HGNC:28531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28531) · Entrez [219743](https://www.ncbi.nlm.nih.gov/gene/219743) · UniProt [Q2T9J0](https://www.uniprot.org/uniprotkb/Q2T9J0) · Ensembl [ENSG00000156521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156521)

## Data

Gene col 7994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7994); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7994]; `tensor/DDL_lfc|DDL_z.npy` [7994]; `embed/gene_vectors.npy` [7994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7994 or target_col == 7994). Every well: [[TYSND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TYSND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
