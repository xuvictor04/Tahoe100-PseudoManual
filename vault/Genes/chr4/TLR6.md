---
symbol: "TLR6"
type: "gene"
col: 10463
ensembl_id: "ENSG00000174130"
name: "toll like receptor 6"
location: "4p14"
module: 117
arm: "+"
pooled_cpm: 6.13
n_lines_expressing: 34
n_dd_up: 17
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 11
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# TLR6

*toll like receptor 6* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +10.4, q 1e-22, up in 19 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.559× (z -6.4, q 1e-07, down in 20 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLR1]] (+0.90, fdr 7e-06, ⚠ same locus), [[CAPS2]] (+0.70, fdr 7e-06), [[EGF]] (+0.67, fdr 7e-06), [[LINC02328]] (+0.67, fdr 7e-06); moves opposite to [[ZDHHC9]] (-0.64, fdr 7e-06), [[WDR5]] (-0.58, fdr 1e-05), [[FBXO31]] (-0.57, fdr 1e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NMRAL2P-1]] → it (grade B ⚠); 11 go from it, the strongest it → [[MOB3C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10463.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +10.4 | 1e-22 | 19/30 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +8.3 | 3e-14 | 6/10 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +8.0 | 3e-13 | 20/31 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +6.8 | 1e-09 | 18/30 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.83×** | +6.6 | 4e-09 | 16/31 (NCI-H1573, HEC-1-A, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +6.2 | 5e-08 | 8/32 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +6.1 | 9e-08 | 10/31 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +5.2 | 1e-05 | 11/31 (A-172, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +5.1 | 2e-05 | 3/14 (NCI-H2030, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +4.9 | 7e-05 | 6/31 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +4.4 | 5e-04 | 11/31 (LOX-IMVI, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.002 | 5/31 (NCI-H2347, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.002 | 12/31 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.0 | 0.002 | 4/20 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.003 | 10/31 (Hs 766T, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.033 | 5/31 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.75×** | +3.2 | 0.045 | 2/21 (CFPAC-1, PANC-1) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10463.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.559×** | -6.4 | 1e-07 | 20/31 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.633×** | -5.0 | 2e-04 | 15/31 (SNU-423, A-172, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.638×** | -4.9 | 2e-04 | 17/31 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **0.645×** | -4.8 | 2e-04 | 13/31 (SNU-423, hTERT-HPNE, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.655×** | -4.6 | 4e-04 | 13/31 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.666×** | -4.4 | 9e-04 | 10/31 (NCI-H2347, A498, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.671×** | -4.4 | 0.001 | 11/31 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.674×** | -4.3 | 0.001 | 15/31 (COLO 205, H4, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.681×** | -4.2 | 0.002 | 10/31 (A498, NCI-H2347, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.700×** | -3.9 | 0.006 | 11/31 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -3.5 | 0.023 | 12/28 (H4, COLO 205, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.804×** | -3.4 | 0.035 | 14/30 (A498, NCI-H460, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.736×** | -3.3 | 0.035 | 8/31 (SNU-423, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.561×** | -3.3 | 0.037 | 11/31 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.739×** | -3.3 | 0.037 | 8/31 (A498, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.759×** | -3.0 | 0.093 | 10/30 (SW 1271, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10463. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 12.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.48× (z +15.0) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -9.7) ⚠ cell-cycle shift, explains ~70% of this change |
| [[COLO 205 (line)]] | alt | 7.08 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0723× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 25.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 2.12 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 17.2 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -9.7) ⚠ cell-cycle shift, explains ~19% of this change |
| [[A-172 (line)]] | wt | 4.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.00× (z +10.9) | — |
| [[A498 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -10.5) ⚠ cell-cycle shift, explains ~19% of this change |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.118× (z -10.3) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 2.64 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0677× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 2.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 8.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +9.4) | — |
| [[A-427 (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.587 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10463), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLR1]] | +0.90 | +0.91 / +0.87 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 999; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CAPS2]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[EGF]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[LINC02328]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[DOCK10]] | +0.66 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[KIAA1217]] | +0.65 | +0.57 / +0.68 | both halves | 9e-06 |  |
| [[LRP1B]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ALOX12P2-1]] | +0.63 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[BTN2A2]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | +0.63 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[TRIM16L]] | +0.62 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[IGSF1]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ZSCAN31]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC9]] | -0.64 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[WDR5]] | -0.58 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[FBXO31]] | -0.57 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CD81]] | -0.56 | -0.53 / -0.46 | both halves | 2e-05 | same gene group |
| [[SPATA33]] | -0.56 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[SMARCD2]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[SRD5A1]] | -0.56 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[SDHAP1]] | -0.55 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[SLC19A2]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ZMYND19]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[PDPR2P]] | -0.54 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[SMG1P5]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity raises TLR6's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without NMRAL2P-1 | 0.046 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[RNASEL]] | B | RNASEL activity raises TLR6's level | lines that do not express RNASEL (5) vs lines expressing it (45) | 3.05× lower at baseline in the lines without RNASEL | 0.052 | ⚠ within organs, on part of the lines; also absent: SP140L, KIFC3, DDX60; maybe low, not absent |
| [[EBF1]] | B | EBF1 activity raises TLR6's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 2.49× lower at baseline in the lines without EBF1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4 |
| [[TLR1]] | C | TLR1 activity raises TLR6's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 3.89× lower at baseline in the lines without TLR1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MOB3C]] | B | TLR6 activity raises MOB3C's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 1.42× lower at baseline in the lines without TLR6 | 0.008 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[RIPK2-DT]] | B | TLR6 activity raises RIPK2-DT's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 1.76× lower at baseline in the lines without TLR6 | 0.017 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[CARD6]] | B | TLR6 activity raises CARD6's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 2.23× lower at baseline in the lines without TLR6 | 0.046 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[DGKI]] | B | TLR6 activity raises DGKI's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 2.78× lower at baseline in the lines without TLR6 | 0.048 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| cells under [[Cobimetinib (drug)]] 5 µM | B | TLR6 activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express TLR6 (16) vs lines expressing it (32) | the lines without TLR6: 1.23× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[RTN4RL1]] | B | TLR6 activity lowers RTN4RL1's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 1.63× higher at baseline in the lines without TLR6 | 0.073 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[DIO2]] | B | TLR6 activity raises DIO2's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 1.92× lower at baseline in the lines without TLR6 | 0.081 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[ASF1A]] | B | TLR6 activity lowers ASF1A's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 1.51× higher at baseline in the lines without TLR6 | 0.091 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| cells under [[Cobimetinib (drug)]] 0.5 µM | B | TLR6 activity lowers the cells' numbers under Cobimetinib 0.5 µM (makes them more sensitive) | lines that do not express TLR6 (16) vs lines expressing it (32) | the lines without TLR6: 1.28× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent |
| [[TLR1]] | C | TLR6 activity raises TLR1's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 4.28× lower at baseline in the lines without TLR6 | 1e-03 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent; co-absent with the target |
| [[NALCN]] | C | TLR6 activity raises NALCN's level | lines that do not express TLR6 (16) vs lines expressing it (34) | 3.52× lower at baseline in the lines without TLR6 | 0.094 | ⚠ within organs, on part of the lines; also absent: TLR1, ENSG00000289526, CYP27C1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.630). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.1, 48.1); signed map (50.0, -8.3). **Vector** length 72.7, 16.2% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +10.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +2.0 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -4.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.6 | -4.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.5 | -2.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.4 | -3.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.3 | -5.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | toll like receptor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:38,822,897-38,856,817 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD286 |
| Gene groups (HGNC) | CD molecules; Toll like receptors |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 19 pathways, smallest: MyD88 deficiency (TLR2/4); IRAK4 deficiency (TLR2/4); Regulation of TLR by endogenous ligand |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2C9](https://www.uniprot.org/uniprotkb/Q9Y2C9) (Toll-like receptor 6):

> Participates in the innate immune response to Gram-positive bacteria and fungi. Specifically recognizes diacylated and, to a lesser extent, triacylated lipopeptides. In response to diacylated lipopeptides, forms the activation cluster TLR2:TLR6:CD14:CD36, this cluster triggers signaling from the cell surface and subsequently is targeted to the Golgi in a lipid-raft dependent pathway. Acts via MYD88 and TRAF6, leading to NF-kappa-B activation, cytokine secretion and the inflammatory response. …

**Summary**, from NCBI Gene [10333](https://www.ncbi.nlm.nih.gov/gene/10333):

> The protein encoded by this gene is a member of the Toll-like receptor (TLR) family which plays a fundamental role in pathogen recognition and activation of innate immunity. TLRs are highly conserved from Drosophila to humans and share structural and functional similarities. They recognize pathogen-associated molecular patterns (PAMPs) that are expressed on infectious agents, and mediate the production of cytokines necessary for the development of effective immunity. The various TLRs exhibit …

**Accessions** — [HGNC:16711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16711) · Entrez [10333](https://www.ncbi.nlm.nih.gov/gene/10333) · UniProt [Q9Y2C9](https://www.uniprot.org/uniprotkb/Q9Y2C9) · Ensembl [ENSG00000174130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174130)

## Data

Gene col 10463: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10463); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10463, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10463]; `tensor/DDL_lfc|DDL_z.npy` [10463]; `embed/gene_vectors.npy` [10463]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10463 or target_col == 10463). Every well: [[TLR6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLR6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
