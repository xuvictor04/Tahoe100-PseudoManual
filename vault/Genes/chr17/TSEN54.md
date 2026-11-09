---
symbol: "TSEN54"
type: "gene"
col: 11252
ensembl_id: "ENSG00000182173"
name: "tRNA splicing endonuclease subunit 54"
location: "17q25.1"
module: 77
arm: "+"
pooled_cpm: 10.95
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# TSEN54

*tRNA splicing endonuclease subunit 54* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.61× (z +18.4, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.552× (z -12.1, q 9e-31, down in 34 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM120B]] (+0.73, fdr 7e-06), [[LPCAT4]] (+0.72, fdr 7e-06), [[ANKRD27]] (+0.71, fdr 1e-05); moves opposite to [[TIA1]] (-0.69, fdr 1e-05), [[RIPK2-DT]] (-0.69, fdr 1e-05), [[ZNF655]] (-0.67, fdr 2e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TLR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11252.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.61×** | +18.4 | 0e+00 | 46/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.47×** | +17.8 | 0e+00 | 47/47 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.43×** | +17.7 | 0e+00 | 45/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.23×** | +11.5 | 3e-28 | 39/45 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.01×** | +10.0 | 2e-21 | 39/47 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +9.8 | 8e-21 | 29/45 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +6.5 | 8e-09 | 18/37 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.16×** | +5.8 | 6e-07 | 20/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +4.7 | 2e-04 | 14/38 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.33×** | +3.9 | 0.006 | 17/40 (HS-578T, SW480, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.011 | 5/41 (NCI-H23, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.061 | 9/46 (H4, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11252.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.552×** | -12.1 | 9e-31 | 34/44 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.689×** | -5.4 | 2e-05 | 20/45 (SW1417, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.723×** | -4.7 | 6e-04 | 20/47 (KATO III, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.775×** | -3.5 | 0.057 | 17/45 (RKO, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11252. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.0 | 3 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 3.70× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.0) |
| [[A498 (line)]] | wt | 9.25 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.09× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 15.0 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.39× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 6.62 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.25× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 6.07 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.03× (z +8.9) | — |
| [[SW480 (line)]] | alt | 19.1 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.93× (z +9.5) | — |
| [[A-172 (line)]] | wt | 7.83 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.47× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 8.97 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 9.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0720× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 6.62 | 0 | 1 | — | [[Paclitaxel (drug)]] 0.05 µM 0.0464× (z -9.1) |
| [[Hs 766T (line)]] | wt | 4.52 | 0 | 1 | — | [[Tubulin inhibitor 6 (drug)]] 0.05 µM 0.0558× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 5.98 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0651× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 9.80 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 9.12 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0679× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 5.90 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0639× (z -9.5) |
| [[A-427 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11252), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM120B]] | +0.73 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[LPCAT4]] | +0.72 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ANKRD27]] | +0.71 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[BRAT1]] | +0.69 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[FOXK2]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[C20orf27]] | +0.66 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[MTMR12]] | +0.66 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ANKRD13B]] | +0.66 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[TAF5L]] | +0.66 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[GFOD2]] | +0.66 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[MPST]] | +0.65 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SSBP4]] | +0.65 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.69 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.69 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.67 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[TSGA10]] | -0.67 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[OCIAD1]] | -0.66 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[PRKAR1A]] | -0.65 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[LPXN]] | -0.65 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[DDX6]] | -0.65 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[SUCLG2-DT]] | -0.65 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[AKT1S1]] | -0.65 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[PCNX4-DT]] | -0.65 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[SDCBP2-AS1]] | -0.64 | -0.54 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLR1]] | B | TLR1 activity lowers TSEN54's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 1.72× higher at baseline in the lines without TLR1 | 0.016 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.818). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-1.7, -0.6); signed map (-42.2, -3.9). **Vector** length 83.5, 16.4% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.4 | +17.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.3 | +11.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +18.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +17.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +10.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.3 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -12.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | -0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +0.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.9 | -0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | tRNA splicing endonuclease subunit 54 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,515,944-75,524,735 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SEN54, SEN54L |
| Gene groups (HGNC) | tRNA-splicing endonuclease subunits |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6J9](https://www.uniprot.org/uniprotkb/Q7Z6J9) (tRNA-splicing endonuclease subunit Sen54):

> Non-catalytic subunit of the tRNA-splicing endonuclease complex, a complex responsible for identification and cleavage of the splice sites in pre-tRNA. It cleaves pre-tRNA at the 5' and 3' splice sites to release the intron. The products are an intron and two tRNA half-molecules bearing 2',3' cyclic phosphate and 5'-OH termini. There are no conserved sequences at the splice sites, but the intron is invariably located at the same site in the gene, placing the splice sites an invariant distance …

**Summary**, from NCBI Gene [283989](https://www.ncbi.nlm.nih.gov/gene/283989):

> This gene encodes a subunit of the tRNA splicing endonuclease complex, which catalyzes the removal of introns from precursor tRNAs. The complex is also implicated in pre-mRNA 3-prime end processing. Mutations in this gene result in pontocerebellar hypoplasia type 2.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:27561](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27561) · Entrez [283989](https://www.ncbi.nlm.nih.gov/gene/283989) · UniProt [Q7Z6J9](https://www.uniprot.org/uniprotkb/Q7Z6J9) · Ensembl [ENSG00000182173](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182173)

## Data

Gene col 11252: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11252); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11252, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11252]; `tensor/DDL_lfc|DDL_z.npy` [11252]; `embed/gene_vectors.npy` [11252]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11252 or target_col == 11252). Every well: [[TSEN54 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSEN54.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
