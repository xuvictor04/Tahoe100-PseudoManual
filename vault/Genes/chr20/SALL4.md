---
symbol: "SALL4"
type: "gene"
col: 2072
ensembl_id: "ENSG00000101115"
name: "spalt like transcription factor 4"
location: "20q13.2"
module: 19
arm: "+"
pooled_cpm: 6.9
n_lines_expressing: 29
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SALL4

*spalt like transcription factor 4* — 20q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +9.9, q 3e-20, up in 12 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.459× (z -11.0, q 3e-25, down in 21 of 26 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE4B]] (+0.58, fdr 1e-05), [[QPCT]] (+0.56, fdr 2e-04), [[RHOH]] (+0.54, fdr 2e-05); moves opposite to [[SLC35A3]] (-0.42, fdr 6e-04), [[CLTCL1]] (-0.41, fdr 4e-04), [[ZYG11B]] (-0.41, fdr 7e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MMRN1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[QPCT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2072.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +9.9 | 3e-20 | 12/26 (Hs 766T, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +8.5 | 4e-15 | 3/10 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +7.4 | 2e-11 | 11/26 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +7.2 | 6e-11 | 2/13 (NCI-H2030, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +6.1 | 9e-08 | 12/26 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +4.6 | 3e-04 | 6/26 (J82, Hs 766T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +4.5 | 5e-04 | 5/26 (COLO 205, RPMI-7951, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.5 | 5e-04 | 1/20 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.3 | 0.001 | 4/27 (NCI-H23, SW 900, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +3.8 | 0.010 | 1/11 (NCI-H2347) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.022 | 3/25 (Hs 766T, NCI-H2030, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +3.5 | 0.022 | 9/26 (A-427, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.032 | 0/25 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.038 | 4/26 (BT-474, Hs 766T, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2072.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.459×** | -11.0 | 3e-25 | 21/26 (C-33 A, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.510×** | -9.5 | 6e-19 | 17/26 (C-33 A, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.605×** | -7.1 | 2e-10 | 17/26 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.637×** | -6.4 | 3e-08 | 17/26 (BT-474, C-33 A, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.713×** | -4.8 | 2e-04 | 13/26 (C-33 A, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.716×** | -4.7 | 2e-04 | 10/25 (C-33 A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.563×** | -4.2 | 0.002 | 12/24 (Hs 766T, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.775×** | -3.6 | 0.023 | 8/26 (C-33 A, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.772×** | -3.5 | 0.033 | 12/26 (A-427, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.627×** | -3.4 | 0.033 | 6/26 (C-33 A, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **0.789×** | -3.3 | 0.042 | 7/25 (CFPAC-1, A549, …) | top dose only |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.799× | -3.1 | 0.11 | 3/26 (NCI-H2030, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2072. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 191 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0691× (z -24.5) |
| [[SW 900 (line)]] | alt | 24.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 30.4 | 0 | 1 | — | [[GSK1059615 (drug)]] 5 µM 0.0421× (z -11.5) |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0814× (z -8.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM 0.0737× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 7.22 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.109× (z -9.7) |
| [[NCI-H661 (line)]] | alt | 150 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -8.8) |
| [[A-172 (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.741 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.889 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.780 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.807 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.734 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.955 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2072), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE4B]] | +0.58 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[QPCT]] | +0.56 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[RHOH]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[MIR1915HG]] | +0.53 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[HHAT]] | +0.51 | +0.39 / +0.37 | both halves | 9e-05 |  |
| [[TMEM52B]] | +0.50 | +0.45 / +0.31 | both halves | 2e-04 |  |
| [[ATP8B4]] | +0.50 | +0.25 / +0.39 | both halves | 4e-04 |  |
| [[CLDN16]] | +0.50 | +0.29 / +0.41 | both halves | 2e-04 |  |
| [[MMRN1]] | +0.50 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[HORMAD1]] | +0.50 | +0.37 / +0.33 | both halves | 1e-04 |  |
| [[NOVA1]] | +0.50 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[CSGALNACT1]] | +0.50 | +0.54 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A3]] | -0.42 | -0.27 / -0.22 | both halves | 6e-04 |  |
| [[CLTCL1]] | -0.41 | -0.30 / -0.25 | both halves | 4e-04 |  |
| [[ZYG11B]] | -0.41 | -0.21 / -0.35 | both halves | 7e-04 |  |
| [[SPTLC2]] | -0.40 | -0.24 / -0.25 | both halves | 5e-04 |  |
| [[TARS3]] | -0.40 | -0.33 / -0.28 | both halves | 3e-04 |  |
| [[HAUS3]] | -0.40 | -0.24 / -0.33 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMRN1]] | B | MMRN1 activity raises SALL4's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 6.60× lower at baseline in the lines without MMRN1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5 |
| [[SUGCT]] | C | SUGCT activity raises SALL4's level | lines that do not express SUGCT (4) vs lines expressing it (46) | 1.00× lower at baseline in the lines without SUGCT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, CABYR, HHAT; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[QPCT]] | B | SALL4 activity raises QPCT's level | lines that do not express SALL4 (21) vs lines expressing it (29) | 1.95× lower at baseline in the lines without SALL4 | 0.085 | ⚠ within organs, on part of the lines; also absent: CHST8, PAX7, SLC6A11 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.470). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.9, 27.1); signed map (42.7, 16.8). **Vector** length 46.6, 8.30% of its response variance represented; |z| ≥ 3 in 571 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +0.4 |
| fall | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.2 | -11.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | +0.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | +0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | spalt like transcription factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.2 — chr20:51,782,331-51,802,521 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1112F19.1, ZNF797 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Reactome | 6 pathways, smallest: POU5F1 (OCT4), SOX2, NANOG activate genes related to proliferation; Transcriptional regulation of pluripotent stem cells; Regulation of PTEN gene transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJQ4](https://www.uniprot.org/uniprotkb/Q9UJQ4) (Sal-like protein 4):

> Transcription factor with a key role in the maintenance and self-renewal of embryonic and hematopoietic stem cells.

**Summary**, from NCBI Gene [57167](https://www.ncbi.nlm.nih.gov/gene/57167):

> This gene encodes a zinc finger transcription factor thought to play a role in the development of abducens motor neurons. Defects in this gene are a cause of Duane-radial ray syndrome (DRRS). Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:15924](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15924) · Entrez [57167](https://www.ncbi.nlm.nih.gov/gene/57167) · UniProt [Q9UJQ4](https://www.uniprot.org/uniprotkb/Q9UJQ4) · Ensembl [ENSG00000101115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101115)

## Data

Gene col 2072: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2072); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2072, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2072]; `tensor/DDL_lfc|DDL_z.npy` [2072]; `embed/gene_vectors.npy` [2072]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2072 or target_col == 2072). Every well: [[SALL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SALL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
