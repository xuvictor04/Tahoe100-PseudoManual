---
symbol: "NALCN"
type: "gene"
col: 2249
ensembl_id: "ENSG00000102452"
name: "sodium leak channel, non-selective"
location: "13q32.3-q33.1"
module: 121
arm: "+"
pooled_cpm: 25.52
n_lines_expressing: 28
n_dd_up: 7
n_dd_down: 31
n_dd_up_clean: 7
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 10
direction_downstream: 16
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# NALCN

*sodium leak channel, non-selective* — 13q32.3-q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +12.3, q 3e-32, up in 17 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.447× (z -10.5, q 7e-23, down in 18 of 25 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.524× (z -8.4, q 7e-15, down in 18 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGBL1]] (+0.64, fdr 1e-05, ⚠ same locus), [[NRG1]] (+0.60, fdr 3e-05), [[LINC01776]] (+0.58, fdr 1e-05), [[TLR6]] (+0.57, fdr 1e-05); moves opposite to [[TMPRSS5]] (-0.52, fdr 5e-05), [[ZCCHC17]] (-0.50, fdr 4e-05), [[SNHG30]] (-0.49, fdr 4e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ZC3H12C]] → it (grade B ⚠); 16 go from it, the strongest it → [[ZC3H12C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +12.3 | 3e-32 | 17/26 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +5.7 | 4e-06 | 12/25 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +5.5 | 5e-06 | 14/25 (RPMI-7951, C32, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.8 | 2e-04 | 12/26 (RPMI-7951, C32, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.7 | 2e-04 | 10/25 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.049 | 12/26 (A549, HOP62, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.059 | 9/26 (C32, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.28× | +3.1 | 0.15 | 3/18 (NCI-H2347, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2249.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.447×** | -10.5 | 7e-23 | 18/25 (Panc 03.27, A549, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.515×** | -8.6 | 2e-15 | 18/25 (Panc 03.27, A549, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.524×** | -8.4 | 7e-15 | 18/25 (Panc 03.27, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.525×** | -8.4 | 7e-15 | 18/25 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.526×** | -8.4 | 8e-15 | 18/25 (Panc 03.27, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.566×** | -7.4 | 1e-11 | 17/25 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.594×** | -6.8 | 9e-10 | 16/25 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.601×** | -6.6 | 2e-09 | 16/25 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.604×** | -6.6 | 3e-09 | 14/25 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.629×** | -6.0 | 9e-08 | 16/25 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.684×** | -4.8 | 1e-04 | 14/25 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.498×** | -4.7 | 1e-04 | 15/24 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.511×** | -4.6 | 2e-04 | 13/25 (Panc 03.27, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.791×** | -4.3 | 6e-04 | 15/26 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.724×** | -4.2 | 9e-04 | 13/25 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.720×** | -4.0 | 0.002 | 14/26 (NCI-H1573, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.577×** | -3.7 | 0.005 | 13/25 (HS-578T, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.585×** | -3.7 | 0.007 | 9/25 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.757×** | -3.5 | 0.012 | 10/25 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.833×** | -3.4 | 0.017 | 5/26 (Panc 03.27, A-427, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.631×** | -3.1 | 0.038 | 8/25 (PANC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.845× | -3.1 | 0.039 | 7/26 (CFPAC-1, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.0 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -18.9) |
| [[PANC-1 (line)]] | alt | 98.1 | 1 | 10 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.4) | [[Ixazomib citrate (drug)]] 5 µM 0.310× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 136 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0450× (z -28.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.183× (z -16.0) |
| [[NCI-H1573 (line)]] | alt | 40.4 | 0 | 7 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.202× (z -10.5) |
| [[A549 (line)]] | wt | 58.3 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -12.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 27.3 | 0 | 3 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.266× (z -13.4) |
| [[SW 1271 (line)]] | alt | 241 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -11.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.109× (z -9.8) |
| [[Hs 766T (line)]] | wt | 15.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 91.2 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.356× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 66.9 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -10.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[NCI-H2347 (line)]] | alt | 27.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +13.6) | — |
| [[SW 900 (line)]] | alt | 52.1 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0833× (z -18.0) ⚠ toxic; cell-cycle shift, explains ~61% of this change |
| [[NCI-H1792 (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -12.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 9.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +8.8) | — |
| [[A-172 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.20 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.97 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGBL1]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 | ⚠ same locus (36.1 kb: neighbours can correlate without regulation) |
| [[NRG1]] | +0.60 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[LINC01776]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TLR6]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[KLHL5]] | +0.56 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CPED1]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[CAVIN2-AS1]] | +0.56 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[PIEZO2]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PDE1C]] | +0.55 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[FAT4]] | +0.54 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[SERTAD4]] | +0.54 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[MPDZ]] | +0.53 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SYT14]] | +0.53 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMPRSS5]] | -0.52 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[ZCCHC17]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[SNHG30]] | -0.49 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ZDHHC9]] | -0.49 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[ADPGK]] | -0.49 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[RAB6A]] | -0.48 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[RNF121]] | -0.48 | -0.47 / -0.32 | both halves | 1e-04 |  |
| [[CERS5]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[FBXO34]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[SDHAP1]] | -0.46 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[QPCTL]] | -0.46 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[PIK3C2A]] | -0.45 | -0.42 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3H12C]] | B | ZC3H12C activity raises NALCN's level | lines that do not express ZC3H12C (7) vs lines expressing it (43) | 4.10× lower at baseline in the lines without ZC3H12C | 0.037 | ⚠ within organs, on part of the lines; also absent: TMOD2, KLF12, DPF1 |
| [[JAK1]], [[JAK3]] | B | JAK1, JAK3 activity lowers NALCN's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[SYNPO]] | C | SYNPO activity raises NALCN's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 4.12× lower at baseline in the lines without SYNPO | 0.012 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent; co-absent with the target |
| [[SERTAD4]] | C | SERTAD4 activity raises NALCN's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 3.11× lower at baseline in the lines without SERTAD4 | 0.032 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC; co-absent with the target |
| [[PRICKLE1]] | C | PRICKLE1 activity raises NALCN's level | lines that do not express PRICKLE1 (26) vs lines expressing it (24) | 3.48× lower at baseline in the lines without PRICKLE1 | 0.036 | ⚠ within organs, on part of the lines; also absent: COL4A2, NR0B1, THBD; co-absent with the target |
| [[TLR1]] | C | TLR1 activity raises NALCN's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 3.27× lower at baseline in the lines without TLR1 | 0.054 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158; co-absent with the target |
| [[P3H2]] | C | P3H2 activity raises NALCN's level | lines that do not express P3H2 (28) vs lines expressing it (22) | 2.92× lower at baseline in the lines without P3H2 | 0.056 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1; co-absent with the target |
| [[FAT4]] | C | FAT4 activity raises NALCN's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 5.36× lower at baseline in the lines without FAT4 | 0.079 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[VEGFC]] | C | VEGFC activity raises NALCN's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 4.59× lower at baseline in the lines without VEGFC | 0.091 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1; co-absent with the target |
| [[TLR6]] | C | TLR6 activity raises NALCN's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 3.52× lower at baseline in the lines without TLR6 | 0.094 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 7, C 9. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3H12C]] | B | NALCN activity raises ZC3H12C's level | lines that do not express NALCN (22) vs lines expressing it (28) | 2.69× lower at baseline in the lines without NALCN | 0.018 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229 |
| [[CDH7]] | B | NALCN activity lowers CDH7's level | lines that do not express NALCN (22) vs lines expressing it (28) | 1.25× higher at baseline in the lines without NALCN | 0.037 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229 |
| [[KLHL5]] | B | NALCN activity raises KLHL5's level | lines that do not express NALCN (22) vs lines expressing it (28) | 2.85× lower at baseline in the lines without NALCN | 0.045 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229 |
| [[BHLHE41]] | B | NALCN activity raises BHLHE41's level | lines that do not express NALCN (22) vs lines expressing it (28) | 2.66× lower at baseline in the lines without NALCN | 0.060 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229 |
| [[NHS]] | B | NALCN activity raises NHS's level | lines that do not express NALCN (22) vs lines expressing it (28) | 3.12× lower at baseline in the lines without NALCN | 0.072 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229 |
| [[NEPRO-AS1]] | B | NALCN activity raises NEPRO-AS1's level | lines that do not express NALCN (22) vs lines expressing it (28) | 1.38× lower at baseline in the lines without NALCN | 0.086 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229 |
| cells under [[Cobimetinib (drug)]] 0.5 µM | B | NALCN activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express NALCN (22) vs lines expressing it (26) | the lines without NALCN: 1.30× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229 |
| [[MYLK]] | C | NALCN activity raises MYLK's level | lines that do not express NALCN (22) vs lines expressing it (28) | 4.10× lower at baseline in the lines without NALCN | 0.027 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229; co-absent with the target |
| [[SPANXA2-OT1]] | C | NALCN activity raises SPANXA2-OT1's level | lines that do not express NALCN (22) vs lines expressing it (28) | 4.12× lower at baseline in the lines without NALCN | 0.036 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229; co-absent with the target |
| [[ITGBL1]] | C | NALCN activity raises ITGBL1's level | lines that do not express NALCN (22) vs lines expressing it (28) | 5.29× lower at baseline in the lines without NALCN | 0.037 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229; co-absent with the target |
| [[P3H2]] | C | NALCN activity raises P3H2's level | lines that do not express NALCN (22) vs lines expressing it (28) | 3.34× lower at baseline in the lines without NALCN | 0.039 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229; co-absent with the target |
| [[SYNPO]] | C | NALCN activity raises SYNPO's level | lines that do not express NALCN (22) vs lines expressing it (28) | 3.19× lower at baseline in the lines without NALCN | 0.063 | ⚠ within organs, on part of the lines; also absent: STAC, EDIL3-DT, ZNF229; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.3, 27.0); signed map (41.6, 28.6). **Vector** length 81.6, 23.5% of its response variance represented; |z| ≥ 3 in 725 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +12.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +4.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | -8.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.7 | -8.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -6.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | sodium leak channel, non-selective |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.3-q33.1 — chr13:101,053,776-101,416,508 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA430M15.1, CanIon; previously VGCNL1 |
| Gene groups (HGNC) | Sodium leak channels, non selective; NALCN channel complex subunits |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZF0](https://www.uniprot.org/uniprotkb/Q8IZF0) (Sodium leak channel NALCN):

> Voltage-sensing, pore-forming subunit of the NALCN channelosome complex, which regulates the resting membrane potential by depolarizing sodium leak currents. The NALCN channelosome complex is a voltage-gated ion channel responsible for the resting Na(+) permeability that controls neuronal excitability. The NALCN channelosome is constitutively active and conducts monovalent cations but is blocked by physiological concentrations of extracellular divalent cations. In addition to its role in …

**Summary**, from NCBI Gene [259232](https://www.ncbi.nlm.nih.gov/gene/259232):

> This gene encodes a voltage-independent, nonselective cation channel which belongs to a family of voltage-gated sodium and calcium channels that regulates the resting membrane potential and excitability of neurons. This family is expressed throughout the nervous system and conducts a persistent sodium leak current that contributes to tonic neuronal excitability. The encoded protein forms a channelosome complex that includes G-protein-coupled receptors, UNC-79, UNC-80, NCA localization factor-1, …

**Accessions** — [HGNC:19082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19082) · Entrez [259232](https://www.ncbi.nlm.nih.gov/gene/259232) · UniProt [Q8IZF0](https://www.uniprot.org/uniprotkb/Q8IZF0) · Ensembl [ENSG00000102452](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102452)

## Data

Gene col 2249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2249); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2249]; `tensor/DDL_lfc|DDL_z.npy` [2249]; `embed/gene_vectors.npy` [2249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2249 or target_col == 2249). Every well: [[NALCN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NALCN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
