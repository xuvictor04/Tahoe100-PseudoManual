---
symbol: "TM4SF19-DYNLT2B"
type: "gene"
col: 15779
ensembl_id: "ENSG00000273331"
name: "TM4SF19-DYNLT2B readthrough (NMD candidate)"
location: "3q29"
module: 229
arm: "+"
pooled_cpm: 4.14
n_lines_expressing: 30
n_dd_up: 13
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 16
tags: ["gene", "module/229"]
generated_by: "tahoemap"
---

# TM4SF19-DYNLT2B

*TM4SF19-DYNLT2B readthrough (NMD candidate)* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.76× (z +8.9, q 3e-16, up in 26 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.359× (z -9.7, q 2e-19, down in 20 of 24 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TM4SF19]] (+0.92, fdr 7e-06, ⚠ same locus), [[DYNLT2B]] (+0.76, fdr 7e-06, ⚠ same locus), [[LAT]] (+0.64, fdr 1e-05), [[ZNF83]] (+0.63, fdr 1e-05), [[SHANK1]] (+0.63, fdr 9e-06); moves opposite to [[CAND1]] (-0.56, fdr 4e-05), [[PCIF1]] (-0.56, fdr 5e-05), [[ATRAID]] (-0.55, fdr 3e-05).
> It is in [[Module 229]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02934]] → it (grade B ⚠); 16 go from it, the strongest it → [[LUCAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15779.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.76×** | +8.9 | 3e-16 | 26/26 (SHP-77, HEC-1-A, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +4.8 | 3e-04 | 10/21 (NCI-H1573, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +4.8 | 3e-04 | 1/8 (NCI-H1792) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.71×** | +3.6 | 0.034 | 12/26 (J82, A-172, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.6 | 0.034 | 4/21 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **2.09×** | +3.5 | 0.034 | 10/24 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.07×** | +3.5 | 0.034 | 5/20 (A-172, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.71×** | +3.5 | 0.034 | 9/25 (NCI-H2030, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **2.62×** | +3.4 | 0.045 | 4/18 (A-172, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 5 µM |  | **2.49×** | +3.2 | 0.077 | 7/20 (NCI-H1573, A-172, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +3.1 | 0.085 | 8/26 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.40×** | +3.1 | 0.098 | 9/22 (A-172, HOP62, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.099 | 6/25 (A-172, NCI-H460, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15779.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.359×** | -9.7 | 2e-19 | 20/24 (NCI-H1573, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.337×** | -7.3 | 9e-11 | 20/26 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.776×** | -6.0 | 3e-07 | 19/28 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.420×** | -5.8 | 1e-06 | 18/26 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.459×** | -5.4 | 9e-06 | 15/27 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.455×** | -5.3 | 1e-05 | 16/26 (HEC-1-A, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.460×** | -5.0 | 5e-05 | 13/25 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.461×** | -4.9 | 8e-05 | 13/24 (HCT15, SW480, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.578×** | -4.1 | 0.003 | 16/27 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.604×** | -4.0 | 0.004 | 12/26 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.533×** | -3.9 | 0.005 | 15/26 (NCI-H2347, HepG2/C3A, …) | all doses, flat | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.353×** | -3.6 | 0.013 | 12/24 (LOX-IMVI, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.589×** | -3.5 | 0.018 | 15/26 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.705×** | -3.3 | 0.041 | 2/28 (SHP-77, A-172) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.617×** | -3.2 | 0.049 | 10/26 (CFPAC-1, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.679×** | -3.2 | 0.054 | 14/26 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | **0.717×** | -3.1 | 0.058 | 6/26 (LOX-IMVI, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15779. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 6.06 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0245× (z -13.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0264× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 21.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -12.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.164× (z -9.8) |
| [[A-172 (line)]] | wt | 34.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0914× (z -12.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.130× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 2.99 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0319× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 1.50 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.310× (z -8.6) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 7.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 6.44 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 6.91 | 0 | 1 | — | [[Trametinib (drug)]] 0.05 µM 0.152× (z -8.8) |
| [[SNU-423 (line)]] | alt | 4.54 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -8.6) |
| [[A-427 (line)]] | wt | 0.281 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.798 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.371 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15779), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM4SF19]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[DYNLT2B]] | +0.76 | +0.63 / +0.76 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LAT]] | +0.64 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[ZNF83]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.63 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[ARHGAP22]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[LINC01705]] | +0.57 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[CRYM]] | +0.55 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[GSTO1]] | +0.55 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[AP1S2]] | +0.54 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[LUCAT1]] | +0.54 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ATP6V0D2]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SH2D2A]] | +0.53 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[GPATCH2L]] | +0.53 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAND1]] | -0.56 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[PCIF1]] | -0.56 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[ATRAID]] | -0.55 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[CNOT1]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[TMEM123]] | -0.54 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ADI1]] | -0.52 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[ZMYM3]] | -0.51 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[IL13RA1]] | -0.49 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[PRPF8]] | -0.49 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[TNS3]] | -0.48 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[ZNF608]] | -0.48 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[CDK16]] | -0.47 | -0.28 / -0.47 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02934]] | B | LINC02934 activity lowers TM4SF19-DYNLT2B's level | lines that do not express LINC02934 (8) vs lines expressing it (42) | 2.18× higher at baseline in the lines without LINC02934 | 0.025 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ARAP3]] | B | ARAP3 activity raises TM4SF19-DYNLT2B's level | lines that do not express ARAP3 (9) vs lines expressing it (41) | 2.53× lower at baseline in the lines without ARAP3 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: HRH1, TGFB1I1, ENSG00000230479 |
| [[ZFPM2-AS1]] | C | ZFPM2-AS1 activity raises TM4SF19-DYNLT2B's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 2.13× lower at baseline in the lines without ZFPM2-AS1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6; co-absent with the target |
| [[CLDN14-AS1]] | C | CLDN14-AS1 activity raises TM4SF19-DYNLT2B's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 2.48× lower at baseline in the lines without CLDN14-AS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 13, C 3. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LUCAT1]] | B | [[TM4SF19]], TM4SF19-DYNLT2B activity raises LUCAT1's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 3.79× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[MAP2K1]] | B | [[TM4SF19]], TM4SF19-DYNLT2B activity raises MAP2K1's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 1.52× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.002 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[GPATCH2L]] | B | [[TM4SF19]], TM4SF19-DYNLT2B activity raises GPATCH2L's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 1.32× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.014 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[ATP5F1B]] | B | TM4SF19-DYNLT2B activity lowers ATP5F1B's level | lines that do not express TM4SF19-DYNLT2B (20) vs lines expressing it (30) | 1.38× higher at baseline in the lines without TM4SF19-DYNLT2B | 0.018 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[ZBTB43]] | B | TM4SF19-DYNLT2B activity raises ZBTB43's level | lines that do not express TM4SF19-DYNLT2B (20) vs lines expressing it (30) | 1.47× lower at baseline in the lines without TM4SF19-DYNLT2B | 0.028 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[SPOCD1]] | B | [[TM4SF19]], TM4SF19-DYNLT2B activity raises SPOCD1's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 3.26× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.035 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[SHC3]] | B | [[TM4SF19]], TM4SF19-DYNLT2B activity raises SHC3's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 2.13× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.039 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[ADGRL1-AS1]] | B | TM4SF19-DYNLT2B activity raises ADGRL1-AS1's level | lines that do not express TM4SF19-DYNLT2B (20) vs lines expressing it (30) | 1.28× lower at baseline in the lines without TM4SF19-DYNLT2B | 0.046 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[RABGEF1P3]] | B | [[TM4SF19]], TM4SF19-DYNLT2B activity raises RABGEF1P3's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 1.70× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.046 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[DYNLT2B]] | B | [[TM4SF19]], TM4SF19-DYNLT2B activity raises DYNLT2B's level | lines that do not express TM4SF19, TM4SF19-DYNLT2B (20) vs lines expressing them (30) | 1.45× lower at baseline in the lines without TM4SF19, TM4SF19-DYNLT2B | 0.056 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; co-absent genes |
| [[HOXC4]] | B | TM4SF19-DYNLT2B activity lowers HOXC4's level | lines that do not express TM4SF19-DYNLT2B (20) vs lines expressing it (30) | 2.15× higher at baseline in the lines without TM4SF19-DYNLT2B | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[CORO2B]] | B | [[TM4SF19]], TM4SF19-DYNLT2B activity strengthens CORO2B's drug response | lines that do not express TM4SF19, TM4SF19-DYNLT2B (11) vs lines expressing them (23) | the lines without TM4SF19, TM4SF19-DYNLT2B respond 0.55× as strongly (z diff +1.63); strongest at Homoharringtonine 5 µM: 0.72x vs 0.37x (z diff +3.6) | 0.071 | ⚠ within organs, on part of the lines; also absent: ADAMTS9, KYNU, PAK3; target measured in part of the lines; artifact flags; co-absent genes |

## Where it sits

- **Module**: [[Module 229]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.6, -4.0); signed map (14.3, 52.1). **Vector** length 64.2, 16.2% of its response variance represented; |z| ≥ 3 in 629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.7 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | -0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.7 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -5.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.6 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.4 | -9.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | TM4SF19-DYNLT2B readthrough (NMD candidate) |
| Locus type | readthrough (other) |
| Location | 3q29 — chr3:196,316,082-196,338,373 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TM4SF19-TCTEX1D2 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100534611](https://www.ncbi.nlm.nih.gov/gene/100534611):

> This locus represents naturally occurring read-through transcription between the neighboring transmembrane 4 L six family member 19 (TM4SF19) and Tctex1 domain containing 2 (TCTEX1D2) genes on chromosome 3. The read-through transcript is a candidate for nonsense-mediated mRNA decay (NMD), and is thus not expected to produce a protein product. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:49190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49190) · Entrez [100534611](https://www.ncbi.nlm.nih.gov/gene/100534611) · Ensembl [ENSG00000273331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273331)

## Data

Gene col 15779: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15779); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15779, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15779]; `tensor/DDL_lfc|DDL_z.npy` [15779]; `embed/gene_vectors.npy` [15779]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15779 or target_col == 15779). Every well: [[TM4SF19-DYNLT2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM4SF19-DYNLT2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
