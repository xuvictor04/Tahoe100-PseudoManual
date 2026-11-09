---
symbol: "SEC16B"
type: "gene"
col: 4180
ensembl_id: "ENSG00000120341"
name: "SEC16 homolog B, endoplasmic reticulum export factor"
location: "1q25.2"
module: 8
arm: "+"
pooled_cpm: 4.42
n_lines_expressing: 37
n_dd_up: 11
n_dd_down: 37
n_dd_up_clean: 8
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 28
direction_downstream: 16
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SEC16B

*SEC16 homolog B, endoplasmic reticulum export factor* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.96× (z +5.9, q 2e-06, up in 17 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.254× (z -17.6, q 0e+00, down in 28 of 30 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.237× (z -12.5, q 1e-33, down in 28 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYZL2P]] (+0.76, fdr 7e-06, ⚠ same locus), [[ARSL]] (+0.70, fdr 7e-06), [[LY75]] (+0.66, fdr 7e-06), [[UBA7]] (+0.60, fdr 8e-06); moves opposite to [[RASSF8]] (-0.45, fdr 4e-05), [[ORMDL2]] (-0.44, fdr 1e-04), [[ZXDC]] (-0.43, fdr 8e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[APOL1]] → it (grade B ⚠); 16 go from it, the strongest it → [[PLA2R1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.96×** | +5.9 | 2e-06 | 17/31 (LoVo, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.36×** | +3.9 | 0.017 | 10/34 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.35×** | +3.9 | 0.017 | 5/34 (LS 180, KATO III, …) | all doses, flat | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.017 | 8/35 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.017 | 10/34 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.077 | 5/35 (COLO 205, HEC-1-A, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.077 | 10/33 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +3.3 | 0.077 | 8/34 (A498, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.34×** | +3.2 | 0.094 | 9/34 (LoVo, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.40×** | +3.1 | 0.094 | 6/35 (LS 180, PANC-1, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.40×** | +3.1 | 0.094 | 6/34 (HS-578T, COLO 205, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.26× | +3.1 | 0.10 | 4/34 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.39× | +3.0 | 0.11 | 3/32 (AsPC-1, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4180.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.254×** | -17.6 | 0e+00 | 28/30 (COLO 205, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.237×** | -12.5 | 1e-33 | 28/32 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.252×** | -12.5 | 2e-33 | 32/34 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.274×** | -11.7 | 1e-29 | 23/30 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.282×** | -11.5 | 2e-28 | 32/34 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.467×** | -9.7 | 2e-20 | 21/30 (COLO 205, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.369×** | -9.0 | 2e-17 | 24/33 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.374×** | -8.9 | 4e-17 | 21/30 (COLO 205, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.433×** | -7.6 | 2e-12 | 24/34 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.465×** | -6.9 | 3e-10 | 20/33 (SW1417, NCI-H2347, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.468×** | -6.9 | 4e-10 | 19/30 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.292×** | -5.8 | 3e-07 | 16/31 (COLO 205, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.635×** | -5.8 | 3e-07 | 18/34 (HT-29, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.540×** | -5.6 | 1e-06 | 18/34 (PANC-1, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.550×** | -5.4 | 3e-06 | 18/30 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.558×** | -5.3 | 5e-06 | 18/34 (NCI-H2030, KATO III, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.534×** | -5.1 | 1e-05 | 16/33 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 46.8 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0405× (z -24.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0372× (z -18.0) |
| [[PANC-1 (line)]] | alt | 5.45 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0589× (z -20.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0562× (z -14.7) |
| [[HT-29 (line)]] | alt | 7.58 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0355× (z -18.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0996× (z -9.2) |
| [[SNU-423 (line)]] | alt | 5.92 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0275× (z -12.4) |
| [[A498 (line)]] | wt | 11.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0656× (z -20.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0317× (z -18.6) |
| [[HEC-1-A (line)]] | alt | 6.73 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -13.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.126× (z -9.5) |
| [[KATO III (line)]] | alt | 7.15 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -12.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0594× (z -11.2) |
| [[SW1417 (line)]] | alt | 4.88 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0578× (z -10.5) |
| [[A-172 (line)]] | wt | 4.09 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0447× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 3.65 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0376× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0852× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 8.59 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0658× (z -16.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -9.2) |
| [[A549 (line)]] | wt | 4.66 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0817× (z -10.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 2.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0736× (z -8.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SK-MEL-2 (line)]] | alt | 8.25 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0584× (z -10.2) |
| [[A-427 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.725 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYZL2P]] | +0.76 | +0.81 / +0.66 | both halves | 7e-06 | ⚠ same locus (23.8 kb, same strand: neighbours can correlate without regulation) |
| [[ARSL]] | +0.70 | +0.66 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LY75]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[UBA7]] | +0.60 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[MMP7]] | +0.60 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[PROM2]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[PLAAT4]] | +0.58 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[ABCC6]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[PLSCR4]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[APOL1]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SLC40A1]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[TM4SF4]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[BCL2L15]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASSF8]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[ORMDL2]] | -0.44 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[ZXDC]] | -0.43 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[HGSNAT]] | -0.43 | -0.40 / -0.55 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 26, C 2. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOL1]] | B | APOL1 activity raises SEC16B's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.29× lower at baseline in the lines without APOL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[LGALS9]] | B | LGALS9 activity raises SEC16B's level | lines that do not express LGALS9 (13) vs lines expressing it (37) | 2.33× lower at baseline in the lines without LGALS9 | 0.008 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ATP8B1, CTSS; maybe low, not absent |
| [[ITIH2]] | B | ITIH2 activity raises SEC16B's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.24× lower at baseline in the lines without ITIH2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH |
| [[MMP7]] | B | MMP7 activity raises SEC16B's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 2.21× lower at baseline in the lines without MMP7 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[CD74]] | B | CD74 activity raises SEC16B's level | lines that do not express CD74 (31) vs lines expressing it (19) | 2.01× lower at baseline in the lines without CD74 | 0.026 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[MAP2K6]] | B | MAP2K6 activity raises SEC16B's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 1.54× lower at baseline in the lines without MAP2K6 | 0.032 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[RNF128]] | B | RNF128 activity raises SEC16B's level | lines that do not express RNF128 (23) vs lines expressing it (27) | 1.89× lower at baseline in the lines without RNF128 | 0.037 | ⚠ within organs, on part of the lines; also absent: AZGP1, RNF43, PROM1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SEC16B's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[HLA-DRA]] | B | HLA-DRA activity raises SEC16B's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 1.99× lower at baseline in the lines without HLA-DRA | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530 |
| [[HNF1B]] | B | HNF1B activity raises SEC16B's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 1.98× lower at baseline in the lines without HNF1B | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[TCN1]] | B | TCN1 activity raises SEC16B's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 1.99× lower at baseline in the lines without TCN1 | 0.044 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B |
| [[PROM1]] | B | PROM1 activity raises SEC16B's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 2.00× lower at baseline in the lines without PROM1 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLA2R1]] | B | SEC16B activity raises PLA2R1's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.95× lower at baseline in the lines without SEC16B | 0.005 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[USH1C]] | B | SEC16B activity raises USH1C's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.93× lower at baseline in the lines without SEC16B | 0.031 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[LY75]] | B | SEC16B activity raises LY75's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.88× lower at baseline in the lines without SEC16B | 0.034 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[PACS1]] | B | SEC16B activity lowers PACS1's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 1.39× higher at baseline in the lines without SEC16B | 0.035 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[GALM]] | B | SEC16B activity raises GALM's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.25× lower at baseline in the lines without SEC16B | 0.038 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[RNF128]] | B | SEC16B activity raises RNF128's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 3.61× lower at baseline in the lines without SEC16B | 0.042 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[DPP4]] | B | SEC16B activity raises DPP4's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 3.76× lower at baseline in the lines without SEC16B | 0.044 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[MYOM3]] | B | SEC16B activity raises MYOM3's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.11× lower at baseline in the lines without SEC16B | 0.050 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[APOL1]] | B | SEC16B activity raises APOL1's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.87× lower at baseline in the lines without SEC16B | 0.064 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[VILL]] | B | SEC16B activity raises VILL's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without SEC16B | 0.081 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[SULT1C2]] | B | SEC16B activity raises SULT1C2's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.06× lower at baseline in the lines without SEC16B | 0.082 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[HNMT]] | B | SEC16B activity raises HNMT's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.58× lower at baseline in the lines without SEC16B | 0.088 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.3, 53.2); signed map (61.7, -0.3). **Vector** length 64.5, 12.4% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.0 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.5 | +0.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +3.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.0 | -6.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -12.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -5.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -11.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.3 | -3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.6 | -4.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | SEC16 homolog B, endoplasmic reticulum export factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.2 — chr1:177,923,956-177,984,303 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RGPR-p117, RGPR, Sec16S; previously LZTR2 |
| Gene groups (HGNC) | SEC16 endoplasmic reticulum export factor family |
| Reactome | 6 pathways, smallest: COPII-mediated vesicle transport; ER to Golgi Anterograde Transport; Transport to the Golgi and subsequent modification |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JE7](https://www.uniprot.org/uniprotkb/Q96JE7) (Protein transport protein Sec16B):

> Plays a role in the organization of the endoplasmic reticulum exit sites (ERES), also known as transitional endoplasmic reticulum (tER). Required for secretory cargo traffic from the endoplasmic reticulum to the Golgi apparatus. Involved in peroxisome biogenesis. Regulates the transport of peroxisomal biogenesis factors PEX3 and PEX16 from the ER to peroxisomes.

**Summary**, from NCBI Gene [89866](https://www.ncbi.nlm.nih.gov/gene/89866):

> SEC16B is a mammalian homolog of S. cerevisiae Sec16 that is required for organization of transitional endoplasmic reticulum (ER) sites and protein export (Bhattacharyya and Glick, 2007 [PubMed 17192411]).[supplied by OMIM, Jun 2009]

**Accessions** — [HGNC:30301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30301) · Entrez [89866](https://www.ncbi.nlm.nih.gov/gene/89866) · UniProt [Q96JE7](https://www.uniprot.org/uniprotkb/Q96JE7) · Ensembl [ENSG00000120341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120341)

## Data

Gene col 4180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4180); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4180]; `tensor/DDL_lfc|DDL_z.npy` [4180]; `embed/gene_vectors.npy` [4180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4180 or target_col == 4180). Every well: [[SEC16B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC16B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
