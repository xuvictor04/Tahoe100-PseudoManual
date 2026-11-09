---
symbol: "EPHX4"
type: "gene"
col: 10201
ensembl_id: "ENSG00000172031"
name: "epoxide hydrolase 4"
location: "1p22.1"
module: 27
arm: "+"
pooled_cpm: 2.66
n_lines_expressing: 34
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# EPHX4

*epoxide hydrolase 4* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.91× (z +8.3, q 4e-14, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.45× (z +4.3, q 0.002, up in 5 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.484× (z -5.9, q 2e-06, down in 16 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01357]] (+0.62, fdr 3e-05), [[EMID1]] (+0.58, fdr 1e-05), [[KCTD14]] (+0.58, fdr 2e-05); moves opposite to [[CDKL5]] (-0.49, fdr 4e-05), [[MYO9A]] (-0.46, fdr 9e-05), [[FNDC3B]] (-0.45, fdr 4e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC01357]] → it (grade B ⚠); 3 go from it, the strongest it → [[FBLIM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10201.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +8.3 | 4e-14 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +5.5 | 1e-05 | 3/16 (J82, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +4.4 | 0.002 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +4.3 | 0.002 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +4.3 | 0.002 | 5/30 (LS 180, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.69×** | +4.2 | 0.003 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +4.1 | 0.003 | 7/27 (COLO 205, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.1 | 0.003 | 1/11 (HCT15) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.007 | 6/29 (CFPAC-1, SW48, …) | rises with dose | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.59×** | +3.8 | 0.009 | 2/16 (LoVo, SHP-77) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +3.7 | 0.010 | 0/7 | rises with dose | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.86×** | +3.6 | 0.014 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.014 | 2/23 (RKO, J82) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +3.4 | 0.023 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~6% here); noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.041 | 1/19 (NCI-H1792) | top dose only | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.72×** | +3.1 | 0.060 | 1/17 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.70×** | +3.1 | 0.067 | 1/16 (MIA PaCa-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +3.0 | 0.082 | 1/12 (LS 180) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.66×** | +2.9 | 0.100 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10201.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.484×** | -5.9 | 2e-06 | 16/28 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.557×** | -4.8 | 5e-04 | 18/30 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.564×** | -4.5 | 0.001 | 12/28 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.632×** | -3.8 | 0.025 | 13/23 (SW480, SW48, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.682× | -3.1 | 0.20 | 17/29 (SW480, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10201. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.4 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -16.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.101× (z -14.5) |
| [[LoVo (line)]] | wt | 6.18 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0831× (z -11.4) |
| [[LS 180 (line)]] | wt | 5.71 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0986× (z -8.9) |
| [[RKO (line)]] | wt | 12.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -9.7) |
| [[SW48 (line)]] | wt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0746× (z -9.1) |
| [[A-172 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.670 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.620 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.723 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.972 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.938 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.882 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.671 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10201), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01357]] | +0.62 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[EMID1]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[KCTD14]] | +0.58 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[HUNK]] | +0.57 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[IL20RA]] | +0.55 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[LINC02058]] | +0.54 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[BLACAT1]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[LARGE2]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[NMNAT3]] | +0.53 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[FGD3]] | +0.52 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[TTPA]] | +0.52 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[CRACD]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL5]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[MYO9A]] | -0.46 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[FNDC3B]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[CCDC7]] | -0.43 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[RB1]] | -0.42 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[TAOK1]] | -0.42 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[SPDYA]] | -0.41 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01357]] | B | LINC01357 activity raises EPHX4's level | lines that do not express LINC01357 (24) vs lines expressing it (26) | 1.85× lower at baseline in the lines without LINC01357 | 0.099 | ⚠ within organs, on part of the lines; also absent: PLBD1-AS1, PLBD1, SYN2 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBLIM1]] | B | EPHX4 activity raises FBLIM1's level | lines that do not express EPHX4 (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without EPHX4 | 0.019 | ⚠ within organs, on part of the lines; also absent: GALNT6, NOD2 |
| [[HUNK]] | B | EPHX4 activity raises HUNK's level | lines that do not express EPHX4 (16) vs lines expressing it (34) | 1.92× lower at baseline in the lines without EPHX4 | 0.061 | ⚠ within organs, on part of the lines; also absent: GALNT6, NOD2 |
| [[PSD4]] | B | EPHX4 activity raises PSD4's level | lines that do not express EPHX4 (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without EPHX4 | 0.084 | ⚠ within organs, on part of the lines; also absent: GALNT6, NOD2 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.452). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.7, 45.2); signed map (60.0, 13.0). **Vector** length 44.9, 8.14% of its response variance represented; |z| ≥ 3 in 576 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.0 | +0.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | epoxide hydrolase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:92,029,985-92,063,538 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EPHXRP, FLJ90341, EH4; previously ABHD7 |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Matched by | ensembl_id |

UniProt [Q8IUS5](https://www.uniprot.org/uniprotkb/Q8IUS5) carries no function annotation.

**Summary**, from NCBI Gene [253152](https://www.ncbi.nlm.nih.gov/gene/253152):

> Predicted to enable hydrolase activity. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23758) · Entrez [253152](https://www.ncbi.nlm.nih.gov/gene/253152) · UniProt [Q8IUS5](https://www.uniprot.org/uniprotkb/Q8IUS5) · Ensembl [ENSG00000172031](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172031)

## Data

Gene col 10201: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10201); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10201, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10201]; `tensor/DDL_lfc|DDL_z.npy` [10201]; `embed/gene_vectors.npy` [10201]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10201 or target_col == 10201). Every well: [[EPHX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
