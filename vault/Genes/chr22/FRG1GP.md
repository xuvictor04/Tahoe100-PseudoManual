---
symbol: "FRG1GP"
type: "gene"
col: 16002
ensembl_id: "ENSG00000283023"
name: "FSHD region gene 1 family member G, pseudogene"
location: "22p11.2"
module: 183
arm: "+"
pooled_cpm: 2.13
n_lines_expressing: 22
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# FRG1GP

*FSHD region gene 1 family member G, pseudogene* — 22p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.68× (z +11.8, q 2e-29, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.90× (z +7.2, q 1e-10, up in 5 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRG1DP]] (+0.80, fdr 7e-06), [[FRG1FP]] (+0.65, fdr 1e-04), [[FRG1BP]] (+0.62, fdr 1e-05); moves opposite to [[PKP4]] (-0.54, fdr 1e-04), [[SCHIP1]] (-0.51, fdr 5e-05), [[TEAD1]] (-0.50, fdr 1e-04).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01518]] → it (grade C ⚠); 3 go from it, the strongest it → [[SPIN2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16002.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.68×** | +11.8 | 2e-29 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.77×** | +7.5 | 2e-11 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.90×** | +7.2 | 1e-10 | 5/17 (SNU-423, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +7.0 | 3e-10 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.00×** | +6.2 | 5e-08 | 1/6 (SNU-423) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +5.3 | 1e-05 | 7/13 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +4.7 | 2e-04 | 2/7 (HS-578T, H4) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +4.6 | 3e-04 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.74×** | +4.4 | 7e-04 | 4/11 (HS-578T, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.12×** | +4.3 | 0.001 | 1/8 (SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +3.9 | 0.005 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.6 | 0.014 | 3/8 (HS-578T, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.017 | 3/11 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.018 | 2/16 (SHP-77, SK-MEL-2) | rises with dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.54×** | +3.2 | 0.053 | 1/9 (HepG2/C3A) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.70×** | +3.0 | 0.081 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +2.9 | 0.087 | 1/13 (H4) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pemigatinib (drug)]] 0.05 µM |  | **1.48×** | +2.9 | 0.087 | 3/12 (HS-578T, HepG2/C3A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16002.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | 0.609× | -3.6 | 0.16 | 2/17 (RPMI-7951, A-427) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.675× | -3.1 | 0.52 | 7/16 (A-172, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.987 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.539 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.594 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.899 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.850 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.720 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.234 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.418 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.540 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.614 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.421 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRG1DP]] | +0.80 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[FRG1FP]] | +0.65 | +0.33 / +0.69 | both halves | 1e-04 |  |
| [[FRG1BP]] | +0.62 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[FRG1JP]] | +0.58 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[SPIN2B]] | +0.57 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[LINC01518]] | +0.57 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[RTCA]] | +0.57 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[ZNF383]] | +0.57 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[MINDY3]] | +0.55 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[PRPF39]] | +0.54 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[CGRRF1]] | +0.54 | +0.43 / +0.37 | both halves | 9e-05 |  |
| [[RRAGD]] | +0.54 | +0.34 / +0.50 | both halves | 1e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKP4]] | -0.54 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[SCHIP1]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[TEAD1]] | -0.50 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[KPNA4]] | -0.48 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[SLC4A7]] | -0.48 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[C2CD3]] | -0.47 | -0.42 / -0.22 | both halves | 6e-04 |  |
| [[SATB2]] | -0.47 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[PSPC1]] | -0.47 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[SNRPB]] | -0.47 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[UBASH3B]] | -0.47 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[CYCS]] | -0.47 | -0.18 / -0.40 | ⚠ not reproduced | 9e-04 |  |
| [[SLC20A2]] | -0.47 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[EHBP1]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01518]] | C | LINC01518 activity raises FRG1GP's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 2.53× lower at baseline in the lines without LINC01518 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |
| [[FRG1FP]] | C | FRG1FP activity raises FRG1GP's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 2.44× lower at baseline in the lines without FRG1FP | 0.096 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPIN2B]] | B | FRG1GP activity raises SPIN2B's level | lines that do not express FRG1GP (28) vs lines expressing it (22) | 1.15× lower at baseline in the lines without FRG1GP | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: BAGE2, TPTE, CCDC144NL-AS1; maybe low, not absent |
| [[FRG1FP]] | C | FRG1GP activity raises FRG1FP's level | lines that do not express FRG1GP (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without FRG1GP | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: BAGE2, TPTE, CCDC144NL-AS1; maybe low, not absent; co-absent with the target |
| [[LINC01518]] | C | FRG1GP activity raises LINC01518's level | lines that do not express FRG1GP (28) vs lines expressing it (22) | 3.38× lower at baseline in the lines without FRG1GP | 0.065 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: BAGE2, TPTE, CCDC144NL-AS1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.0, 30.8); signed map (-23.9, -10.9). **Vector** length 16.1, 1.74% of its response variance represented; |z| ≥ 3 in 374 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +1.2 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.1 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.9 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.9 | +11.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.7 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.5 | +3.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.5 | +1.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.5 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | +0.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.4 | +1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.4 | -1.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.4 | -1.0 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.4 | -0.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.4 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | FSHD region gene 1 family member G, pseudogene |
| Locus type | pseudogene |
| Location | 22p11.2 — chr22:12,602,466-12,626,642 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51766) · Entrez [101930531](https://www.ncbi.nlm.nih.gov/gene/101930531) · Ensembl [ENSG00000283023](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000283023)

## Data

Gene col 16002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16002); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16002]; `tensor/DDL_lfc|DDL_z.npy` [16002]; `embed/gene_vectors.npy` [16002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16002 or target_col == 16002). Every well: [[FRG1GP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRG1GP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
