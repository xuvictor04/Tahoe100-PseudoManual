---
symbol: "WTIP"
type: "gene"
col: 6614
ensembl_id: "ENSG00000142279"
name: "WT1 interacting protein"
location: "19q13.11"
module: 38
arm: "+"
pooled_cpm: 15.55
n_lines_expressing: 45
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# WTIP

*WT1 interacting protein* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.66× (z +11.8, q 2e-29, up in 25 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.706× (z -5.7, q 6e-06, down in 21 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFSD2B]] (+0.67, fdr 7e-06), [[NLGN3]] (+0.66, fdr 1e-05), [[ORAI2]] (+0.65, fdr 7e-06); moves opposite to [[MDH1]] (-0.54, fdr 5e-05), [[RIPK4]] (-0.52, fdr 3e-05), [[ATP5F1C]] (-0.51, fdr 6e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ASGR1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PILRA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6614.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +11.8 | 2e-29 | 25/41 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +6.0 | 6e-07 | 15/35 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +5.5 | 6e-06 | 14/42 (C-33 A, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.5 | 6e-06 | 17/41 (A549, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.9 | 1e-04 | 8/27 (A-172, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +4.8 | 1e-04 | 11/38 (A-427, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 1e-04 | 17/41 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.7 | 2e-04 | 12/40 (BT-474, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.1 | 0.003 | 9/32 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.007 | 10/40 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.008 | 4/39 (RKO, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.068 | 7/42 (LS 180, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.078 | 13/42 (SNU-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.091 | 10/40 (PANC-1, HS-578T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.092 | 8/39 (BT-474, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6614.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.706×** | -5.7 | 6e-06 | 21/42 (SNU-1, SW480, …) | two highest doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.723×** | -5.3 | 3e-05 | 21/42 (A-427, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.732×** | -5.1 | 5e-05 | 20/42 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.729×** | -4.9 | 1e-04 | 13/40 (SW 900, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.754×** | -4.7 | 4e-04 | 14/42 (A-427, SNU-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.758×** | -4.4 | 0.001 | 17/39 (C-33 A, BT-474, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.769×** | -4.3 | 0.001 | 19/42 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.851× | -3.8 | 0.011 | 9/43 (COLO 205, LS 180, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.801×** | -3.5 | 0.027 | 18/41 (LOX-IMVI, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.811×** | -3.5 | 0.030 | 18/36 (J82, KATO III, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.677×** | -3.4 | 0.040 | 8/38 (HT-29, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.819×** | -3.3 | 0.045 | 11/42 (LOX-IMVI, BT-474, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.876× | -3.1 | 0.084 | 6/43 (KATO III, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6614. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 62.7 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -12.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.339× (z -10.6) |
| [[BT-474 (line)]] | alt | 17.1 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.162× (z -9.3) ⚠ toxic |
| [[C-33 A (line)]] | alt | 63.3 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.229× (z -11.5) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 31.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.233× (z -11.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SNU-1 (line)]] | wt | 77.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[venetoclax (drug)]] 5 µM 0.131× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 23.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +8.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0794× (z -10.2) ⚠ transcription drop; unreliable plate only |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0943× (z -8.9) ⚠ transcription drop |
| [[J82 (line)]] | alt | 8.03 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0961× (z -11.6) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 8.87 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.171× (z -9.4) ⚠ transcription drop |
| [[NCI-H460 (line)]] | wt | 6.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 30.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.0) | — |
| [[RKO (line)]] | wt | 8.07 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0850× (z -9.0) |
| [[SNU-423 (line)]] | alt | 4.90 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM 0.0672× (z -9.3) |
| [[SW480 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.303× (z -9.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6614), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD2B]] | +0.67 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[NLGN3]] | +0.66 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ORAI2]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[CCNP]] | +0.62 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[DNMT3A]] | +0.62 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[TGIF2-RAB5IF]] | +0.61 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[SYCE2]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CDKL1]] | +0.60 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[PILRA]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[WNK4]] | +0.59 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[PRX]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[SLC23A3]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDH1]] | -0.54 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[RIPK4]] | -0.52 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ATP5F1C]] | -0.51 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[MPP1]] | -0.51 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[CAT]] | -0.51 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[VPS33B]] | -0.50 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASGR1]] | B | ASGR1 activity raises WTIP's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.94× lower at baseline in the lines without ASGR1 | 0.032 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[SLC2A9]] | B | SLC2A9 activity lowers WTIP's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 2.93× higher at baseline in the lines without SLC2A9 | 0.042 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[KIFC3]] | C | KIFC3 activity lowers WTIP's level | lines that do not express KIFC3 (3) vs lines expressing it (47) | 5.04× higher at baseline in the lines without KIFC3 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PILRA]] | B | WTIP activity raises PILRA's level | lines that do not express WTIP (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without WTIP | 0.099 | ⚠ within organs, on part of the lines; also absent: C5, BTG3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.5, -14.0); signed map (18.0, 5.3). **Vector** length 84.2, 16.4% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +2.2 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.8 | -5.1 |
|  | [[NG25 (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.5 | -5.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -2.8 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | WT1 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:34,481,758-34,512,304 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ajuba family |
| Reactome | 4 pathways, smallest: Oxygen-dependent proline hydroxylation of Hypoxia-inducible Factor Alpha; Cellular response to hypoxia; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NIX2](https://www.uniprot.org/uniprotkb/A6NIX2) (Wilms tumor protein 1-interacting protein):

> Adapter or scaffold protein which participates in the assembly of numerous protein complexes and is involved in several cellular processes such as cell fate determination, cytoskeletal organization, repression of gene transcription, cell-cell adhesion, cell differentiation, proliferation and migration. Positively regulates microRNA (miRNA)-mediated gene silencing. Negatively regulates Hippo signaling pathway and antagonizes phosphorylation of YAP1. Acts as a transcriptional corepressor for …

**Summary**, from NCBI Gene [126374](https://www.ncbi.nlm.nih.gov/gene/126374):

> Predicted to enable transcription corepressor activity. Involved in miRNA-mediated gene silencing by inhibition of translation; negative regulation of hippo signaling; and response to hypoxia. Acts upstream of or within miRNA-mediated post-transcriptional gene silencing. Located in P-body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20964](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20964) · Entrez [126374](https://www.ncbi.nlm.nih.gov/gene/126374) · UniProt [A6NIX2](https://www.uniprot.org/uniprotkb/A6NIX2) · Ensembl [ENSG00000142279](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142279)

## Data

Gene col 6614: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6614); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6614, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6614]; `tensor/DDL_lfc|DDL_z.npy` [6614]; `embed/gene_vectors.npy` [6614]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6614 or target_col == 6614). Every well: [[WTIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WTIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
