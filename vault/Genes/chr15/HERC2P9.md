---
symbol: "HERC2P9"
type: "gene"
col: 13035
ensembl_id: "ENSG00000206149"
name: "HERC2 pseudogene 9"
location: "15q13.1"
module: 36
arm: "+"
pooled_cpm: 8.15
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# HERC2P9

*HERC2 pseudogene 9* — 15q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.14× (z +10.4, q 9e-23, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.678× (z -7.5, q 3e-11, down in 24 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HERC2P2]] (+0.94, fdr 7e-06), [[HERC2P3]] (+0.90, fdr 7e-06), [[HERC2]] (+0.85, fdr 7e-06); moves opposite to [[SGO1-AS1]] (-0.72, fdr 7e-06), [[FAM200B]] (-0.68, fdr 1e-05), [[TSPAN31]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13035.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.14×** | +10.4 | 9e-23 | 39/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.02×** | +9.7 | 1e-19 | 34/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +8.5 | 3e-15 | 36/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.93×** | +8.5 | 3e-15 | 31/44 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.77×** | +7.8 | 5e-13 | 28/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +7.4 | 1e-11 | 28/47 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 3e-04 | 17/43 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +4.0 | 0.005 | 9/47 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.62×** | +3.5 | 0.033 | 3/29 (PANC-1, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.25× | +3.0 | 0.13 | 2/47 (NCI-H460, HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13035.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -7.5 | 3e-11 | 24/42 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.686×** | -7.3 | 8e-11 | 22/44 (SK-MEL-2, J82, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -6.6 | 1e-08 | 20/32 (MIA PaCa-2, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.611×** | -6.5 | 1e-08 | 25/45 (NCI-H460, J82, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.662×** | -5.7 | 2e-06 | 17/47 (SW480, NCI-H460, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.663×** | -5.6 | 2e-06 | 18/47 (SW480, SW48, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.688×** | -5.1 | 2e-05 | 18/46 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.671×** | -5.1 | 3e-05 | 17/24 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.704×** | -4.8 | 1e-04 | 18/44 (HCT15, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.741×** | -4.1 | 0.002 | 20/44 (HS-578T, C32, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.745×** | -3.9 | 0.006 | 9/37 (A498, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.796× | -3.0 | 0.12 | 18/44 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13035. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.4 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.175× (z -11.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.215× (z -10.9) |
| [[SW480 (line)]] | alt | 9.83 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.282× (z -10.0) |
| [[J82 (line)]] | alt | 10.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.144× (z -10.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[MIA PaCa-2 (line)]] | alt | 8.40 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0946× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 8.66 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -12.4) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SW48 (line)]] | wt | 10.1 | 0 | 2 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0703× (z -9.5) |
| [[A498 (line)]] | wt | 8.76 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -8.5) |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.302× (z -9.3) ⚠ transcription drop; cell-cycle shift, explains ~77% of this change |
| [[SW1417 (line)]] | alt | 9.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13035), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P2]] | +0.94 | +0.89 / +0.92 | both halves | 7e-06 |  |
| [[HERC2P3]] | +0.90 | +0.84 / +0.82 | both halves | 7e-06 |  |
| [[HERC2]] | +0.85 | +0.84 / +0.79 | both halves | 7e-06 |  |
| [[EXOC2]] | +0.75 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[ZNF496]] | +0.75 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[ERI3]] | +0.72 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.72 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PACC1]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[HERC2P9-1]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[SPATA5]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[TYW1]] | +0.66 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[RNF216]] | +0.66 | +0.71 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGO1-AS1]] | -0.72 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[FAM200B]] | -0.68 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[TSPAN31]] | -0.67 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[FAM117A]] | -0.66 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[UPK2]] | -0.65 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[ATP23]] | -0.65 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[MALINC1]] | -0.64 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[SRGAP3]] | -0.64 | -0.58 / -0.37 | both halves | 7e-05 |  |
| [[CGGBP1]] | -0.63 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[NPHS1]] | -0.63 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[SSPN]] | -0.62 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[TSGA10]] | -0.62 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers HERC2P9's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers HERC2P9's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LGALS3]] | B | LGALS3 activity lowers HERC2P9's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.40× higher at baseline in the lines without LGALS3 | 0.092 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.851). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-7.0, -31.3); signed map (-16.0, -52.0). **Vector** length 72.3, 11.8% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +9.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.4 | +8.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +7.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.5 | +8.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +2.3 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.2 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -6.3 | -7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -7.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.7 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -4.4 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | HERC2 pseudogene 9 |
| Locus type | pseudogene |
| Location | 15q13.1 — chr15:28,590,189-28,674,027 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | FLJ59185 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:30495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30495) · Entrez [440248](https://www.ncbi.nlm.nih.gov/gene/440248) · Ensembl [ENSG00000206149](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206149)

## Data

Gene col 13035: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13035); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13035, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13035]; `tensor/DDL_lfc|DDL_z.npy` [13035]; `embed/gene_vectors.npy` [13035]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13035 or target_col == 13035). Every well: [[HERC2P9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERC2P9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
