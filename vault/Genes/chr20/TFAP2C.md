---
symbol: "TFAP2C"
type: "gene"
col: 1510
ensembl_id: "ENSG00000087510"
name: "transcription factor AP-2 gamma"
location: "20q13.31"
module: 97
arm: "+"
pooled_cpm: 16.13
n_lines_expressing: 32
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# TFAP2C

*transcription factor AP-2 gamma* — 20q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +12.9, q 3e-35, up in 18 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.603× (z -7.7, q 9e-12, down in 16 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.446× (z -6.4, q 4e-08, down in 18 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BDNF]] (+0.57, fdr 1e-05), [[GATA3]] (+0.55, fdr 2e-05), [[FZD7]] (+0.55, fdr 1e-05); moves opposite to [[ZDHHC6]] (-0.51, fdr 1e-04), [[BTAF1]] (-0.50, fdr 6e-05), [[OPA1]] (-0.49, fdr 1e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RHOV]] → it (grade B ⚠); 2 go from it, the strongest it → [[NR2F1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1510.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +12.9 | 3e-35 | 18/28 (CFPAC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +12.6 | 4e-34 | 18/30 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +8.7 | 7e-16 | 16/30 (SNU-423, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +8.1 | 7e-14 | 14/30 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +8.0 | 2e-13 | 20/30 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +5.8 | 5e-07 | 15/30 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +4.8 | 1e-04 | 9/30 (SNU-423, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.3 | 0.002 | 4/30 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.013 | 3/25 (SW480, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.041 | 3/29 (SK-MEL-2, A-172, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.062 | 7/29 (SNU-423, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.23×** | +3.1 | 0.081 | 4/24 (SNU-423, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Afatinib (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.11 | 2/30 (BT-474, SK-MEL-2) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1510.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.603×** | -7.7 | 9e-12 | 16/23 (SW1417, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -6.4 | 4e-08 | 18/30 (NCI-H2030, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.642×** | -6.2 | 1e-07 | 14/19 (NCI-H2030, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -5.9 | 4e-07 | 17/30 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.689×** | -5.7 | 2e-06 | 13/30 (SW1417, NCI-H23, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.537×** | -4.9 | 8e-05 | 14/28 (SW1417, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.602×** | -4.0 | 0.005 | 11/28 (NCI-H23, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.859× | -3.3 | 0.073 | 5/30 (CHP-212, BT-474, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.807×** | -3.2 | 0.073 | 8/29 (Hs 766T, SW48, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.673×** | -3.1 | 0.096 | 7/27 (SW1417, C32, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.805× | -3.1 | 0.10 | 13/28 (NCI-H23, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1510. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 79.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -21.0) |
| [[A498 (line)]] | wt | 17.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +21.6) | — |
| [[NCI-H23 (line)]] | alt | 51.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -18.5) |
| [[SW1417 (line)]] | alt | 80.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -19.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 8.17 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 20.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -13.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 39.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 6.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +10.1) | — |
| [[NCI-H661 (line)]] | alt | 80.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0719× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 13.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.275× (z -8.7) |
| [[A-172 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1510), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BDNF]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[GATA3]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 | STRING 858 |
| [[FZD7]] | +0.55 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[FOXC1]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[RHOV]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[TCF7L2]] | +0.51 | +0.38 / +0.51 | both halves | 6e-05 | pathway: Gastrulation |
| [[IRF2BPL]] | +0.51 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[LATS2]] | +0.50 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[SIX5]] | +0.49 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[DEPDC7]] | +0.49 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[PTGER4]] | +0.49 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[PELI2]] | +0.49 | +0.40 / +0.42 | both halves | 5e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC6]] | -0.51 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[BTAF1]] | -0.50 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[OPA1]] | -0.49 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[NDUFA10]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[TMPRSS5]] | -0.47 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[RPN1]] | -0.46 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ATPAF1]] | -0.46 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[RBM44]] | -0.46 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[LONP2]] | -0.45 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[PCYT1A]] | -0.45 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[EIF2A]] | -0.45 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[TMED7]] | -0.45 | -0.36 / -0.42 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOV]] | B | RHOV activity raises TFAP2C's level | lines that do not express RHOV (23) vs lines expressing it (27) | 2.04× lower at baseline in the lines without RHOV | 0.061 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR2F1]] | B | TFAP2C activity lowers NR2F1's level | lines that do not express TFAP2C (18) vs lines expressing it (32) | 1.98× higher at baseline in the lines without TFAP2C | 0.063 | ⚠ within organs, on part of the lines; also absent: LYPD1, SETBP1, SAA1 |
| [[PLPP3]] | B | TFAP2C activity raises PLPP3's level | lines that do not express TFAP2C (18) vs lines expressing it (32) | 1.30× lower at baseline in the lines without TFAP2C | 0.086 | ⚠ within organs, on part of the lines; also absent: LYPD1, SETBP1, SAA1 |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.194). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.9, -4.4); signed map (13.8, -6.9). **Vector** length 66.8, 14.2% of its response variance represented; |z| ≥ 3 in 674 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.4 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +8.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.9 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +4.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.1 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.5 | -6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.5 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -5.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor AP-2 gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.31 — chr20:56,629,306-56,639,283 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AP2-GAMMA, ERF1, TFAP2G, hAP-2g |
| Gene groups (HGNC) | Transcription factor AP-2 family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 13 pathways, smallest: TFAP2 (AP-2) family regulates transcription of other transcription factors; TFAP2 (AP-2) family regulates transcription of cell cycle factors; Activation of the TFAP2 (AP-2) family of transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92754](https://www.uniprot.org/uniprotkb/Q92754) (Transcription factor AP-2 gamma):

> Sequence-specific DNA-binding transcription factor that interacts with cellular enhancer elements to regulate transcription of selected genes, and which plays a key role in early embryonic development. AP-2 factors bind to the consensus sequence 5'-GCCNNNGGC-3' and activate genes involved in a large spectrum of important biological functions. TFAP2C plays a key role in early embryonic development by regulating both inner cell mass (ICM) and trophectoderm differentiation (By similarity). At the …

**Summary**, from NCBI Gene [7022](https://www.ncbi.nlm.nih.gov/gene/7022):

> The protein encoded by this gene is a sequence-specific DNA-binding transcription factor involved in the activation of several developmental genes. The encoded protein can act as either a homodimer or heterodimer with other family members and is induced during retinoic acid-mediated differentiation. It plays a role in the development of the eyes, face, body wall, limbs, and neural tube. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11744) · Entrez [7022](https://www.ncbi.nlm.nih.gov/gene/7022) · UniProt [Q92754](https://www.uniprot.org/uniprotkb/Q92754) · Ensembl [ENSG00000087510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087510)

## Data

Gene col 1510: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1510); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1510, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1510]; `tensor/DDL_lfc|DDL_z.npy` [1510]; `embed/gene_vectors.npy` [1510]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1510 or target_col == 1510). Every well: [[TFAP2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFAP2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
