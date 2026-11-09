---
symbol: "EXPH5"
type: "gene"
col: 3163
ensembl_id: "ENSG00000110723"
name: "exophilin 5"
location: "11q22.3"
module: 8
arm: "+"
pooled_cpm: 59.7
n_lines_expressing: 30
n_dd_up: 22
n_dd_down: 12
n_dd_up_clean: 19
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 46
direction_downstream: 31
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# EXPH5

*exophilin 5* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.73× (z +13.3, q 2e-37, up in 17 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.707× (z -5.9, q 1e-06, down in 16 of 28 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.542× (z -5.5, q 9e-06, down in 19 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MACC1]] (+0.63, fdr 7e-06), [[TOX3]] (+0.62, fdr 1e-05), [[ARHGEF38]] (+0.61, fdr 1e-05); moves opposite to [[SEC14L2]] (-0.51, fdr 1e-05), [[PANK2]] (-0.49, fdr 4e-05), [[BMS1P23]] (-0.47, fdr 5e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 46 arrows point to it, the strongest [[RASEF]] → it (grade B ⚠); 31 go from it, the strongest it → [[SAMD12]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3163.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.73×** | +13.3 | 2e-37 | 17/28 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.15×** | +13.1 | 1e-36 | 14/28 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +11.4 | 5e-28 | 10/28 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.84×** | +10.4 | 4e-23 | 20/28 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +8.6 | 1e-15 | 12/28 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +7.7 | 2e-12 | 15/28 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.35×** | +7.2 | 4e-11 | 11/28 (LoVo, SNU-423, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.00×** | +6.2 | 4e-08 | 11/28 (NCI-H2030, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.33×** | +4.9 | 6e-05 | 15/28 (SW480, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +4.6 | 2e-04 | 16/28 (SW480, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +4.6 | 2e-04 | 8/28 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 5e-04 | 12/28 (NCI-H1573, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.002 | 16/29 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.003 | 13/28 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.005 | 12/28 (KATO III, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.009 | 7/28 (NCI-H1573, RKO, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3163.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.707×** | -5.9 | 1e-06 | 16/28 (KATO III, SW48, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.783×** | -5.9 | 1e-06 | 17/28 (SW 900, RKO, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.542×** | -5.5 | 9e-06 | 19/29 (KATO III, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.573×** | -5.0 | 1e-04 | 18/28 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.589×** | -4.7 | 3e-04 | 14/20 (SW480, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.772×** | -4.4 | 1e-03 | 17/28 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.786×** | -4.1 | 0.003 | 10/28 (SW 900, NCI-H2030, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.636×** | -4.0 | 0.004 | 14/28 (KATO III, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.799×** | -3.8 | 0.008 | 14/28 (SW480, SW 900, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.805×** | -3.5 | 0.028 | 6/28 (Panc 03.27, LS 180, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.754×** | -3.4 | 0.030 | 13/28 (KATO III, SW 1271, …) | two highest doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.828×** | -3.2 | 0.062 | 15/28 (LoVo, SW48, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.839× | -3.0 | 0.12 | 16/28 (LS 180, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 246 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 182 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.408× (z -8.9) |
| [[LoVo (line)]] | wt | 76.7 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +15.6) ⚠ cell-cycle shift, explains ~40% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.472× (z -8.9) |
| [[SW48 (line)]] | wt | 122 | 0 | 4 (3 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0820× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 55.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -15.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW480 (line)]] | alt | 181 | 0 | 3 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.441× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 145 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.379× (z -9.0) |
| [[RKO (line)]] | wt | 35.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -17.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[BT-474 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[Panc 03.27 (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +11.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SW 900 (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.395× (z -9.9) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SW1417 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.96 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.40 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.37 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.86 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.23 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 366 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.78 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.86 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.68 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.13 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.18 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.28 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.92 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 65.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACC1]] | +0.63 | +0.70 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[TOX3]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[ARHGEF38]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TMC5]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[POF1B]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PIP5K1B]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CLIC5]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[CLDN3]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TMEM45B]] | +0.56 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[RASSF6]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[RASEF]] | +0.55 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ADGRF1]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC14L2]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[PANK2]] | -0.49 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[BMS1P23]] | -0.47 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[ANPEP]] | -0.45 | -0.48 / -0.37 | both halves | 7e-05 |  |
| [[LINC00941]] | -0.43 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[KCTD10]] | -0.43 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[PLCG1]] | -0.43 | -0.36 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 13, C 33. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASEF]] | B | RASEF activity raises EXPH5's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.74× lower at baseline in the lines without RASEF | 0.005 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[ANK3]] | B | ANK3 activity raises EXPH5's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 3.82× lower at baseline in the lines without ANK3 | 0.006 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[SAMD12]] | B | SAMD12 activity raises EXPH5's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 3.83× lower at baseline in the lines without SAMD12 | 0.008 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[KLF4]] | B | KLF4 activity raises EXPH5's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 2.58× lower at baseline in the lines without KLF4 | 0.014 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[DAPP1]] | B | DAPP1 activity raises EXPH5's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 3.53× lower at baseline in the lines without DAPP1 | 0.017 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises EXPH5's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.22× lower at baseline in the lines without ELF3-AS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[HNF4G]] | B | HNF4G activity raises EXPH5's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.10× lower at baseline in the lines without HNF4G | 0.032 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[PTPRK]] | B | PTPRK activity raises EXPH5's level | lines that do not express PTPRK (6) vs lines expressing it (44) | 3.32× lower at baseline in the lines without PTPRK | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000246225, EPS8, ASPH |
| [[RBM47]] | B | RBM47 activity raises EXPH5's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 3.22× lower at baseline in the lines without RBM47 | 0.076 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[ANXA3]] | B | ANXA3 activity raises EXPH5's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 3.17× lower at baseline in the lines without ANXA3 | 0.077 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[TMC4]] | B | TMC4 activity raises EXPH5's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 3.27× lower at baseline in the lines without TMC4 | 0.087 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[RASEF]] | B | RASEF activity weakens EXPH5's drug response | lines that do not express RASEF (9) vs lines expressing it (19) | the lines without RASEF respond 2.51× as strongly (z diff -1.81); strongest at Panobinostat 0.5 µM: 1.69x vs 0.87x (z diff -4.2) | 0.093 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D; target measured in part of the lines; artifact flags |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 11, C 20. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD12]] | B | EXPH5 activity raises SAMD12's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 3.46× lower at baseline in the lines without EXPH5 | 0.016 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[DAPP1]] | B | EXPH5 activity raises DAPP1's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 2.77× lower at baseline in the lines without EXPH5 | 0.058 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[HNF4G]] | B | EXPH5 activity raises HNF4G's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 3.06× lower at baseline in the lines without EXPH5 | 0.060 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[ELF3-AS1]] | B | EXPH5 activity raises ELF3-AS1's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 2.60× lower at baseline in the lines without EXPH5 | 0.060 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[TMC4]] | B | EXPH5 activity raises TMC4's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 3.26× lower at baseline in the lines without EXPH5 | 0.071 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[ANK3]] | B | EXPH5 activity raises ANK3's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 2.98× lower at baseline in the lines without EXPH5 | 0.073 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[KLF4]] | B | EXPH5 activity raises KLF4's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 1.84× lower at baseline in the lines without EXPH5 | 0.074 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[RAPGEF5]] | B | EXPH5 activity raises RAPGEF5's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 2.80× lower at baseline in the lines without EXPH5 | 0.086 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[RBM47]] | B | EXPH5 activity raises RBM47's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 3.75× lower at baseline in the lines without EXPH5 | 0.095 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | EXPH5 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express EXPH5 (20) vs lines expressing it (28) | the lines without EXPH5: 0.82× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[TMPRSS3]] | B | EXPH5 activity raises TMPRSS3's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 1.90× lower at baseline in the lines without EXPH5 | 0.097 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A |
| [[FAAH2]] | C | EXPH5 activity raises FAAH2's level | lines that do not express EXPH5 (20) vs lines expressing it (30) | 4.08× lower at baseline in the lines without EXPH5 | 0.021 | ⚠ within organs, on part of the lines; also absent: GALNT3, ENSG00000243004, GOLT1A; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.532). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.4, 50.8); signed map (58.6, 4.2). **Vector** length 87.9, 24.2% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +13.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.3 | +7.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +2.5 | +2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +4.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -2.5 | -5.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -2.4 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -4.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -3.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | exophilin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:108,505,435-108,593,768 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLAC2-B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEV8](https://www.uniprot.org/uniprotkb/Q8NEV8) (Exophilin-5):

> May act as Rab effector protein and play a role in vesicle trafficking.

**Summary**, from NCBI Gene [23086](https://www.ncbi.nlm.nih.gov/gene/23086):

> The protein encoded by this gene is a member of the synaptotagmin-like protein (Slp) family lacking a C2 domain. It contains an N-terminal synaptotagmin-like homology domain (SHD), and is a ras-related protein Rab-27B effector protein. This protein is thought to be involved in exosome secretion and intracellular vesicle trafficking. Reduced expression of this gene results in keratin filament defects. Mutations in this gene have been associated with some cases of epidermolysis bullosa, an …

**Accessions** — [HGNC:30578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30578) · Entrez [23086](https://www.ncbi.nlm.nih.gov/gene/23086) · UniProt [Q8NEV8](https://www.uniprot.org/uniprotkb/Q8NEV8) · Ensembl [ENSG00000110723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110723)

## Data

Gene col 3163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3163); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3163]; `tensor/DDL_lfc|DDL_z.npy` [3163]; `embed/gene_vectors.npy` [3163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3163 or target_col == 3163). Every well: [[EXPH5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXPH5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
