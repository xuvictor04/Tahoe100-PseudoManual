---
symbol: "SLC37A4"
type: "gene"
col: 6051
ensembl_id: "ENSG00000137700"
name: "solute carrier family 37 member 4"
location: "11q23.3"
module: 58
arm: "+"
pooled_cpm: 4.23
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# SLC37A4

*solute carrier family 37 member 4* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.50× (z +9.1, q 5e-17, up in 12 of 19 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.95× (z +4.1, q 0.003, up in 3 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.381× (z -9.6, q 5e-19, down in 37 of 43 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THYN1]] (+0.66, fdr 1e-05), [[MFSD3]] (+0.61, fdr 1e-05), [[PCYOX1L]] (+0.61, fdr 1e-05); moves opposite to [[ACYP2]] (-0.50, fdr 7e-04), [[C11orf58]] (-0.48, fdr 3e-04), [[TBCE-1]] (-0.48, fdr 3e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[YBX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6051.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.50×** | +9.1 | 5e-17 | 12/19 (LS 180, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.36×** | +8.2 | 7e-14 | 6/7 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.00×** | +6.4 | 3e-08 | 4/11 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.68×** | +5.1 | 4e-05 | 15/47 (SW 900, Hs 766T, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.8 | 2e-04 | 10/22 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.1 | 0.003 | 5/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.95×** | +4.1 | 0.003 | 3/30 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.48×** | +3.9 | 0.007 | 13/45 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.47×** | +3.8 | 0.009 | 9/46 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.29×** | +3.6 | 0.021 | 7/36 (RKO, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.027 | 9/46 (NCI-H1573, BT-474, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +3.3 | 0.045 | 0/13 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6051.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.381×** | -9.6 | 5e-19 | 37/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.393×** | -9.3 | 4e-18 | 25/34 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.404×** | -9.0 | 4e-17 | 32/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.544×** | -8.5 | 2e-15 | 27/37 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.453×** | -7.9 | 4e-13 | 24/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.558×** | -5.8 | 6e-07 | 22/46 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.562×** | -5.7 | 8e-07 | 18/36 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.581×** | -5.4 | 5e-06 | 18/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.634×** | -4.5 | 4e-04 | 11/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.635×** | -4.3 | 0.001 | 19/40 (CFPAC-1, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.657×** | -4.2 | 0.002 | 16/42 (HEC-1-A, SW48, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.398×** | -4.1 | 0.002 | 13/33 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.712×** | -3.1 | 0.080 | 9/46 (NCI-H661, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6051. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.92 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.153× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 4.64 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0637× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 7.01 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.117× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 4.63 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0547× (z -10.2) |
| [[LoVo (line)]] | wt | 3.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0615× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 5.30 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0607× (z -11.4) |
| [[A-172 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6051), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THYN1]] | +0.66 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MFSD3]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PCYOX1L]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[LRRC45]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[THEM6]] | +0.60 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SCRN2]] | +0.59 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[MLST8]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[JMJD8]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TKFC]] | +0.57 | +0.63 / +0.50 | both halves | 1e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[HAUS4]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PPM1M]] | +0.56 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[NUDT8]] | +0.56 | +0.46 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACYP2]] | -0.50 | -0.21 / -0.49 | both halves | 7e-04 |  |
| [[C11orf58]] | -0.48 | -0.26 / -0.40 | both halves | 3e-04 |  |
| [[TBCE-1]] | -0.48 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[CREM]] | -0.47 | -0.40 / -0.24 | both halves | 5e-04 |  |
| [[MAFG]] | -0.47 | -0.33 / -0.32 | both halves | 2e-04 |  |
| [[RUFY3]] | -0.47 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[ATP6V1G1]] | -0.47 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[FBXO30]] | -0.47 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[TBCA]] | -0.46 | -0.34 / -0.32 | both halves | 1e-04 |  |
| [[ZNF529-AS1]] | -0.46 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[CAB39L]] | -0.46 | -0.26 / -0.39 | both halves | 3e-04 |  |
| [[LINC01772]] | -0.46 | -0.31 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YBX2]] | B | YBX2 activity raises SLC37A4's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 1.42× lower at baseline in the lines without YBX2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9 |
| [[ARHGEF16]] | B | ARHGEF16 activity raises SLC37A4's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 1.49× lower at baseline in the lines without ARHGEF16 | 0.066 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[PSMB5]] | B | PSMB5 activity raises SLC37A4's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.450). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-27.2, -43.6); signed map (-34.0, -38.3). **Vector** length 42.7, 4.89% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.0 | +1.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.9 | +4.8 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +1.8 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +1.6 | +5.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.1 | +0.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.0 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.9 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 37 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,023,751-119,030,906 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GSD1b, GSD1c, GSD1d, G6PT, SPX4; previously G6PT1, G6PT2, G6PT3 |
| Gene groups (HGNC) | Solute carrier family 37 |
| Hallmark sets | GLYCOLYSIS, HYPOXIA, MTORC1_SIGNALING |
| Reactome | 6 pathways, smallest: Glycogen storage diseases; Gluconeogenesis; Diseases of carbohydrate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O43826](https://www.uniprot.org/uniprotkb/O43826) (Glucose-6-phosphate exchanger SLC37A4):

> Inorganic phosphate and glucose-6-phosphate antiporter of the endoplasmic reticulum. Transports cytoplasmic glucose-6-phosphate into the lumen of the endoplasmic reticulum and translocates inorganic phosphate into the opposite direction. Responsible for glucose production through glycogenolysis and gluconeogenesis and plays a central role in homeostatic regulation of blood glucose levels.

**Summary**, from NCBI Gene [2542](https://www.ncbi.nlm.nih.gov/gene/2542):

> This gene regulates glucose-6-phosphate transport from the cytoplasm to the lumen of the endoplasmic reticulum, in order to maintain glucose homeostasis. It also plays a role in ATP-mediated calcium sequestration in the lumen of the endoplasmic reticulum. Mutations in this gene have been associated with various forms of glycogen storage disease. Alternative splicing in this gene results in multiple transcript variants.[provided by RefSeq, Aug 2009]

**Accessions** — [HGNC:4061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4061) · Entrez [2542](https://www.ncbi.nlm.nih.gov/gene/2542) · UniProt [O43826](https://www.uniprot.org/uniprotkb/O43826) · Ensembl [ENSG00000137700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137700)

## Data

Gene col 6051: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6051); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6051, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6051]; `tensor/DDL_lfc|DDL_z.npy` [6051]; `embed/gene_vectors.npy` [6051]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6051 or target_col == 6051). Every well: [[SLC37A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC37A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
