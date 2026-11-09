---
symbol: "RADIL"
type: "gene"
col: 8116
ensembl_id: "ENSG00000157927"
name: "Rap associating with DIL domain"
location: "7p22.1"
module: 19
arm: "+"
pooled_cpm: 4.22
n_lines_expressing: 29
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 4
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# RADIL

*Rap associating with DIL domain* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.16× (z +18.4, q 0e+00, up in 24 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.604× (z -5.7, q 9e-06, down in 15 of 25 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCUBE1]] (+0.65, fdr 1e-05), [[COL4A4]] (+0.64, fdr 1e-05), [[GALNT16]] (+0.62, fdr 3e-05); moves opposite to [[TSGA10]] (-0.60, fdr 3e-04), [[DNAI4]] (-0.56, fdr 1e-04), [[METTL6]] (-0.56, fdr 6e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EPB41L3]] → it (grade B ⚠); 4 go from it, the strongest it → [[COL4A4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8116.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.16×** | +18.4 | 0e+00 | 24/25 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.95×** | +15.4 | 0e+00 | 23/24 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +11.1 | 2e-26 | 7/23 (BT-474, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +10.0 | 3e-21 | 17/24 (NCI-H2347, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.49×** | +9.9 | 7e-21 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.29×** | +9.3 | 1e-18 | 21/24 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.17×** | +8.7 | 3e-16 | 24/25 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +7.0 | 2e-10 | 2/16 (HS-578T, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +6.5 | 4e-09 | 5/24 (SW480, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +6.2 | 4e-08 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +4.9 | 4e-05 | 2/23 (HS-578T, HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.5 | 3e-04 | 6/23 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.51×** | +4.5 | 3e-04 | 2/15 (AN3 CA, HEC-1-A) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +3.7 | 0.009 | 12/23 (NCI-H2347, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.6 | 0.013 | 0/7 | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.5 | 0.016 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.034 | 2/18 (A549, NCI-H1792) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.043 | 7/23 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8116.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.604×** | -5.7 | 9e-06 | 15/25 (NCI-H460, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.705×** | -3.8 | 0.036 | 13/25 (NCI-H460, A-427, …) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[crizotinib (drug)]] 5 µM |  | **0.707×** | -3.7 | 0.036 | 6/23 (A549, BT-474, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.720×** | -3.5 | 0.072 | 3/23 (SW 900, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8116. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0343× (z -20.4) |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0414× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 7.24 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.61 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0681× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.723 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.650 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.849 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.510 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.563 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8116), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCUBE1]] | +0.65 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[COL4A4]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[GALNT16]] | +0.62 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[CEP72]] | +0.61 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[KIF26A]] | +0.61 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[SLITRK4]] | +0.61 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[DNMT3B]] | +0.60 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[FAM124A]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CBX2]] | +0.59 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[ATP2A3]] | +0.59 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[CNTN1]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[DDIT4L]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSGA10]] | -0.60 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[DNAI4]] | -0.56 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[METTL6]] | -0.56 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[GGPS1]] | -0.55 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[TIMMDC1]] | -0.55 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[PKN2-AS1]] | -0.55 | -0.46 / -0.29 | both halves | 3e-04 |  |
| [[THAP2]] | -0.54 | -0.40 / -0.29 | both halves | 3e-04 |  |
| [[MCTS1]] | -0.54 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[BCDIN3D]] | -0.54 | -0.36 / -0.36 | both halves | 9e-05 |  |
| [[AEBP2]] | -0.53 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[KRCC1]] | -0.53 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[CCDC90B-AS1]] | -0.53 | -0.39 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L3]] | B | EPB41L3 activity raises RADIL's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 1.78× lower at baseline in the lines without EPB41L3 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R |
| [[RUNX2]] | B | RUNX2 activity lowers RADIL's level | lines that do not express RUNX2 (8) vs lines expressing it (42) | 2.61× higher at baseline in the lines without RUNX2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SATB1, ITGA3, TCEAL3; maybe low, not absent; its own permutation p |
| [[FAM124A]] | C | FAM124A activity raises RADIL's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 2.58× lower at baseline in the lines without FAM124A | 0.018 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1; co-absent with the target |
| [[MMP17]] | C | MMP17 activity raises RADIL's level | lines that do not express MMP17 (17) vs lines expressing it (33) | 2.39× lower at baseline in the lines without MMP17 | 0.086 | ⚠ within organs, on part of the lines; also absent: NOVA2, TUB, RIMKLB; co-absent with the target |
| [[CNKSR2]] | C | CNKSR2 activity raises RADIL's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 2.54× lower at baseline in the lines without CNKSR2 | 0.087 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL4A4]] | C | RADIL activity raises COL4A4's level | lines that do not express RADIL (21) vs lines expressing it (29) | 2.95× lower at baseline in the lines without RADIL | 0.008 | ⚠ within organs, on part of the lines; also absent: ZYG11A, OLFM1, JAKMIP1; maybe low, not absent; co-absent with the target |
| [[FAM124A]] | C | RADIL activity raises FAM124A's level | lines that do not express RADIL (21) vs lines expressing it (29) | 2.21× lower at baseline in the lines without RADIL | 0.010 | ⚠ within organs, on part of the lines; also absent: ZYG11A, OLFM1, JAKMIP1; maybe low, not absent; co-absent with the target |
| [[COL4A3]] | C | RADIL activity raises COL4A3's level | lines that do not express RADIL (21) vs lines expressing it (29) | 3.10× lower at baseline in the lines without RADIL | 0.012 | ⚠ within organs, on part of the lines; also absent: ZYG11A, OLFM1, JAKMIP1; maybe low, not absent; co-absent with the target |
| [[MMP17]] | C | RADIL activity raises MMP17's level | lines that do not express RADIL (21) vs lines expressing it (29) | 2.05× lower at baseline in the lines without RADIL | 0.090 | ⚠ within organs, on part of the lines; also absent: ZYG11A, OLFM1, JAKMIP1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.513). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.4, 39.9); signed map (40.3, 47.9). **Vector** length 48.5, 9.12% of its response variance represented; |z| ≥ 3 in 652 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +6.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +3.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.4 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | Rap associating with DIL domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:4,797,055-4,883,716 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10324, KIAA1849, RASIP2 |
| Gene groups (HGNC) | PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JH8](https://www.uniprot.org/uniprotkb/Q96JH8) (Ras-associating and dilute domain-containing protein):

> Downstream effector of Rap required for cell adhesion and migration of neural crest precursors during development.

**Summary**, from NCBI Gene [55698](https://www.ncbi.nlm.nih.gov/gene/55698):

> Predicted to enable GTPase binding activity. Acts upstream of or within substrate adhesion-dependent cell spreading. Located in microtubule. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22226) · Entrez [55698](https://www.ncbi.nlm.nih.gov/gene/55698) · UniProt [Q96JH8](https://www.uniprot.org/uniprotkb/Q96JH8) · Ensembl [ENSG00000157927](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157927)

## Data

Gene col 8116: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8116); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8116, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8116]; `tensor/DDL_lfc|DDL_z.npy` [8116]; `embed/gene_vectors.npy` [8116]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8116 or target_col == 8116). Every well: [[RADIL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RADIL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
