---
symbol: "ALDH1L1"
type: "gene"
col: 6945
ensembl_id: "ENSG00000144908"
name: "aldehyde dehydrogenase 1 family member L1"
location: "3q21.3"
module: 55
arm: "+"
pooled_cpm: 5.44
n_lines_expressing: 19
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# ALDH1L1

*aldehyde dehydrogenase 1 family member L1* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.34× (z +11.7, q 6e-29, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +5.8, q 8e-07, up in 2 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.606× (z -5.1, q 2e-04, down in 12 of 17 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC5A1]] (+0.71, fdr 1e-05), [[FAM83F]] (+0.70, fdr 1e-05), [[ABO]] (+0.68, fdr 1e-05); moves opposite to [[DNAAF9]] (-0.45, fdr 2e-04).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[VILL]] → it (grade B ⚠); 4 go from it, the strongest it → [[VILL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6945.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.34×** | +11.7 | 6e-29 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +10.8 | 8e-25 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +7.3 | 5e-11 | 1/6 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.8 | 8e-07 | 2/15 (LS 180, HCT15) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.03×** | +5.1 | 4e-05 | 1/13 (SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.94×** | +4.8 | 2e-04 | 0/11 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.7 | 2e-04 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +4.5 | 5e-04 | 1/4 (LoVo) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +3.6 | 0.017 | 2/9 (J82, Panc 03.27) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.4 | 0.034 | 1/11 (SW48) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.047 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.42×** | +3.3 | 0.050 | 0/13 | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.098 | 2/13 (J82, LoVo) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6945.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.606×** | -5.1 | 2e-04 | 12/17 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.635×** | -4.6 | 0.001 | 9/17 (KATO III, LS 180, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.668×** | -4.1 | 0.008 | 7/16 (H4, SW48, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.686×** | -3.8 | 0.019 | 8/17 (SK-MEL-2, LS 180, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.669×** | -3.8 | 0.019 | 2/17 (CFPAC-1, SNU-1) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.701×** | -3.6 | 0.030 | 5/17 (Panc 03.27, J82, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.715×** | -3.4 | 0.055 | 12/17 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.719×** | -3.3 | 0.058 | 7/17 (KATO III, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.727×** | -3.2 | 0.076 | 11/17 (KATO III, LS 180, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.730×** | -3.2 | 0.079 | 11/16 (SW48, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.733×** | -3.2 | 0.081 | 12/17 (KATO III, LS 180, …) | two highest doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.736×** | -3.1 | 0.088 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6945. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 75.9 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -14.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -13.5) |
| [[LoVo (line)]] | wt | 7.06 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0613× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0382× (z -16.2) |
| [[LS 180 (line)]] | wt | 47.3 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -11.1) |
| [[SW48 (line)]] | wt | 38.5 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -8.5) |
| [[J82 (line)]] | alt | 11.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0368× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0948× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 6.82 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0592× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.416 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.804 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.594 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.558 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.690 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6945), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC5A1]] | +0.71 | +0.67 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[FAM83F]] | +0.70 | +0.57 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[ABO]] | +0.68 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[TMEM125]] | +0.67 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MYO7B]] | +0.67 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[LYPD6B]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[EDAR]] | +0.62 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[LINC03040]] | +0.60 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[SKAP1]] | +0.60 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[ESRP1]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[SYK]] | +0.59 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PIP5K1B]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.45 | -0.38 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VILL]] | B | VILL activity raises ALDH1L1's level | lines that do not express VILL (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without VILL | 0.090 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[SLC6A20]] | C | SLC6A20 activity raises ALDH1L1's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 4.08× lower at baseline in the lines without SLC6A20 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH; co-absent with the target |
| [[BMP4]] | C | BMP4 activity raises ALDH1L1's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 2.98× lower at baseline in the lines without BMP4 | 0.070 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B; co-absent with the target |
| [[VWA2]] | C | VWA2 activity raises ALDH1L1's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 3.46× lower at baseline in the lines without VWA2 | 0.098 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VILL]] | B | ALDH1L1 activity raises VILL's level | lines that do not express ALDH1L1 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without ALDH1L1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SLC6A20, KLK7, BMP4 |
| [[LINC00923]] | C | ALDH1L1 activity raises LINC00923's level | lines that do not express ALDH1L1 (31) vs lines expressing it (19) | 2.73× lower at baseline in the lines without ALDH1L1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC6A20, KLK7, BMP4; co-absent with the target |
| [[BMP4]] | C | ALDH1L1 activity raises BMP4's level | lines that do not express ALDH1L1 (31) vs lines expressing it (19) | 3.92× lower at baseline in the lines without ALDH1L1 | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC6A20, KLK7, BMP4; co-absent with the target |
| [[TSPOAP1]] | C | ALDH1L1 activity raises TSPOAP1's level | lines that do not express ALDH1L1 (31) vs lines expressing it (19) | 1.75× lower at baseline in the lines without ALDH1L1 | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC6A20, KLK7, BMP4; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.4, 53.7); signed map (61.7, 9.0). **Vector** length 36.1, 7.37% of its response variance represented; |z| ≥ 3 in 455 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +1.6 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +5.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.7 | +0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.6 | +0.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.6 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.3 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.2 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -0.9 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.9 | +2.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.8 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -3.8 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.7 | -1.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -0.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 1 family member L1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:126,103,562-126,197,994 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 10-fTHF, FDH; previously FTHFD |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 3 pathways, smallest: Metabolism of folate and pterines; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [O75891](https://www.uniprot.org/uniprotkb/O75891) (Cytosolic 10-formyltetrahydrofolate dehydrogenase):

> Cytosolic 10-formyltetrahydrofolate dehydrogenase that catalyzes the NADP(+)-dependent conversion of 10-formyltetrahydrofolate to tetrahydrofolate and carbon dioxide. May also have an NADP(+)-dependent aldehyde dehydrogenase activity towards formaldehyde, acetaldehyde, propionaldehyde, and benzaldehyde (By similarity).

**Summary**, from NCBI Gene [10840](https://www.ncbi.nlm.nih.gov/gene/10840):

> The protein encoded by this gene catalyzes the conversion of 10-formyltetrahydrofolate, nicotinamide adenine dinucleotide phosphate (NADP+), and water to tetrahydrofolate, NADPH, and carbon dioxide. The encoded protein belongs to the aldehyde dehydrogenase family. Loss of function or expression of this gene is associated with decreased apoptosis, increased cell motility, and cancer progression. There is an antisense transcript that overlaps on the opposite strand with this gene locus. …

**Accessions** — [HGNC:3978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3978) · Entrez [10840](https://www.ncbi.nlm.nih.gov/gene/10840) · UniProt [O75891](https://www.uniprot.org/uniprotkb/O75891) · Ensembl [ENSG00000144908](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144908)

## Data

Gene col 6945: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6945); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6945, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6945]; `tensor/DDL_lfc|DDL_z.npy` [6945]; `embed/gene_vectors.npy` [6945]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6945 or target_col == 6945). Every well: [[ALDH1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
