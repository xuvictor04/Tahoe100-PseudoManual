---
symbol: "BMP7"
type: "gene"
col: 2077
ensembl_id: "ENSG00000101144"
name: "bone morphogenetic protein 7"
location: "20q13.31"
module: 27
arm: "+"
pooled_cpm: 19.82
n_lines_expressing: 27
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# BMP7

*bone morphogenetic protein 7* — 20q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.96× (z +9.3, q 6e-18, up in 5 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +7.0, q 3e-10, up in 5 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.614× (z -6.5, q 4e-08, down in 17 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KSR2]] (+0.60, fdr 1e-05), [[SEMA4G]] (+0.59, fdr 1e-05), [[TTPA]] (+0.57, fdr 3e-05); moves opposite to [[TFPI]] (-0.55, fdr 1e-05), [[OSMR]] (-0.50, fdr 3e-05), [[CC2D1B]] (-0.48, fdr 4e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02253]] → it (grade C ⚠); 8 go from it, the strongest it → [[NEK5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2077.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +9.3 | 6e-18 | 5/21 (BT-474, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +7.1 | 3e-10 | 4/14 (PANC-1, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.0 | 3e-10 | 5/25 (BT-474, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.7 | 2e-06 | 9/25 (SNU-423, NCI-H2030, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **1.27×** | +4.7 | 3e-04 | 6/25 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.54×** | +4.3 | 0.002 | 3/23 (H4, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.006 | 7/24 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.027 | 6/25 (SW480, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.027 | 4/23 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.042 | 3/23 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.042 | 5/25 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.042 | 9/25 (AsPC-1, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2077.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.614×** | -6.5 | 4e-08 | 17/23 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.634×** | -6.3 | 7e-08 | 17/24 (NCI-H1573, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.649×** | -6.0 | 3e-07 | 17/24 (LS 180, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.748×** | -5.7 | 2e-06 | 17/24 (NCI-H1573, SW48, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.673×** | -5.5 | 4e-06 | 13/24 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.683×** | -5.3 | 1e-05 | 14/24 (NCI-H23, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.704×** | -4.9 | 9e-05 | 13/25 (LS 180, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.730×** | -4.4 | 9e-04 | 12/24 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.567×** | -4.1 | 0.002 | 12/24 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.779×** | -3.5 | 0.030 | 11/24 (LoVo, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.628×** | -3.4 | 0.038 | 4/25 (NCI-H1573, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.790×** | -3.3 | 0.049 | 6/25 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2077. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 150 | 0 | 28 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0605× (z -30.6) |
| [[LS 180 (line)]] | wt | 104 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -14.6) |
| [[LoVo (line)]] | wt | 24.9 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -19.0) |
| [[COLO 205 (line)]] | alt | 77.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -16.3) |
| [[SW480 (line)]] | alt | 74.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -13.6) |
| [[SW48 (line)]] | wt | 31.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0679× (z -19.1) |
| [[A-427 (line)]] | wt | 43.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.210× (z -13.9) |
| [[BT-474 (line)]] | alt | 56.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -9.2) |
| [[PANC-1 (line)]] | alt | 7.36 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.5) |
| [[SW1417 (line)]] | alt | 49.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -13.6) |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM 0.175× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 5.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.16× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 21.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -8.6) |
| [[NCI-H661 (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0906× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~23% of this change |
| [[A-172 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2077), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KSR2]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[SEMA4G]] | +0.59 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[TTPA]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[PIK3C2B]] | +0.57 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[HUNK]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[AXIN2]] | +0.56 | +0.49 / +0.46 | both halves | 3e-05 | STRING 437 |
| [[RNF43]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CHDH]] | +0.56 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[BMP4]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 | same gene group; pathway: Elastic fibre formation; STRING 978 |
| [[LRP4]] | +0.54 | +0.56 / +0.41 | both halves | 4e-05 | pathway: Extracellular matrix organization |
| [[HOXB8]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[IQGAP2]] | +0.53 | +0.48 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFPI]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[OSMR]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[CC2D1B]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02253]] | C | LINC02253 activity raises BMP7's level | lines that do not express LINC02253 (35) vs lines expressing it (15) | 4.18× lower at baseline in the lines without LINC02253 | 0.029 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02058, ENSG00000289349; co-absent with the target |
| [[YBX2]] | C | YBX2 activity raises BMP7's level | lines that do not express YBX2 (28) vs lines expressing it (22) | 3.51× lower at baseline in the lines without YBX2 | 0.067 | ⚠ within organs, on part of the lines; also absent: CKMT1A, PRR15L, FGF9; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEK5]] | B | BMP7 activity raises NEK5's level | lines that do not express BMP7 (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without BMP7 | 0.058 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A |
| [[NEK5]] | B | BMP7 activity weakens NEK5's drug response | lines that do not express BMP7 (22) vs lines expressing it (24) | the lines without BMP7 respond 1.07× as strongly (z diff -0.08); strongest at Dinaciclib 5 µM: 1.11x vs 0.44x (z diff -4.1) | 0.070 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A; target measured in part of the lines; both ways; artifact flags |
| [[TTPA]] | B | BMP7 activity raises TTPA's level | lines that do not express BMP7 (23) vs lines expressing it (27) | 1.69× lower at baseline in the lines without BMP7 | 0.079 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A |
| [[STRBP]] | B | BMP7 activity weakens STRBP's drug response | lines that do not express BMP7 (23) vs lines expressing it (25) | the lines without BMP7 respond 1.35× as strongly (z diff -1.28); strongest at Homoharringtonine 5 µM: 1.52x vs 1.35x (z diff -2.3) | 0.081 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A; target measured in part of the lines; artifact flags |
| [[ENTREP2]] | B | BMP7 activity raises ENTREP2's level | lines that do not express BMP7 (23) vs lines expressing it (27) | 2.02× lower at baseline in the lines without BMP7 | 0.087 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A |
| [[HUNK]] | B | BMP7 activity raises HUNK's level | lines that do not express BMP7 (23) vs lines expressing it (27) | 2.06× lower at baseline in the lines without BMP7 | 0.097 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A |
| [[UGT8]] | B | BMP7 activity lowers UGT8's level | lines that do not express BMP7 (23) vs lines expressing it (27) | 1.69× higher at baseline in the lines without BMP7 | 0.098 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A |
| [[CDX2]] | C | BMP7 activity raises CDX2's level | lines that do not express BMP7 (23) vs lines expressing it (27) | 1.72× lower at baseline in the lines without BMP7 | 0.073 | ⚠ within organs, on part of the lines; also absent: NFASC, ENSG00000291189, KIF1A; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.447). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.6, 45.6); signed map (61.2, 13.4). **Vector** length 68.9, 16.8% of its response variance represented; |z| ≥ 3 in 628 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.7 | +4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -5.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -4.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | bone morphogenetic protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.31 — chr20:57,168,753-57,266,641 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OP-1 |
| Gene groups (HGNC) | Bone morphogenetic proteins |
| Reactome | 6 pathways, smallest: Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2; Molecules associated with elastic fibres |
| Matched by | ensembl_id |

**Function**, from UniProt [P18075](https://www.uniprot.org/uniprotkb/P18075) (Bone morphogenetic protein 7):

> Growth factor of the TGF-beta superfamily that plays important role in various biological processes, including embryogenesis, hematopoiesis, neurogenesis and skeletal morphogenesis. Initiates the canonical BMP signaling cascade by associating with type I receptor ACVR1 and type II receptor ACVR2A. Once all three components are bound together in a complex at the cell surface, ACVR2A phosphorylates and activates ACVR1. In turn, ACVR1 propagates signal by phosphorylating SMAD1/5/8 that travel to …

**Summary**, from NCBI Gene [655](https://www.ncbi.nlm.nih.gov/gene/655):

> This gene encodes a secreted ligand of the TGF-beta (transforming growth factor-beta) superfamily of proteins. Ligands of this family bind various TGF-beta receptors leading to recruitment and activation of SMAD family transcription factors that regulate gene expression. The encoded preproprotein is proteolytically processed to generate each subunit of the disulfide-linked homodimer, which plays a role in bone, kidney and brown adipose tissue development. Additionally, this protein induces …

**Accessions** — [HGNC:1074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1074) · Entrez [655](https://www.ncbi.nlm.nih.gov/gene/655) · UniProt [P18075](https://www.uniprot.org/uniprotkb/P18075) · Ensembl [ENSG00000101144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101144)

## Data

Gene col 2077: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2077); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2077, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2077]; `tensor/DDL_lfc|DDL_z.npy` [2077]; `embed/gene_vectors.npy` [2077]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2077 or target_col == 2077). Every well: [[BMP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
