---
symbol: "STX16-NPEPL1"
type: "gene"
col: 14906
ensembl_id: "ENSG00000254995"
name: "STX16-NPEPL1 readthrough (NMD candidate)"
location: "20q13.32"
module: 52
arm: "+"
pooled_cpm: 8.5
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# STX16-NPEPL1

*STX16-NPEPL1 readthrough (NMD candidate)* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +5.0, q 3e-04, up in 25 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.385× (z -14.5, q 1e-44, down in 36 of 46 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 3 lines (A498 0.0622×, hTERT-HPNE 0.0349×, PANC-1 0.162×; ⚠ cell-cycle shift, explains ~35% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HOP62 0.186×, hTERT-HPNE 0.109×, HT-29 0.193×; ⚠ cell-cycle shift, explains ~50% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (BT-474 0.0399×, KATO III 0.0788×; ⚠ cell-cycle shift, explains ~46% of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (A498 0.152×); [[Isocorydine (drug)]] 0.5 µM in 1 line (HCT15 0.0986×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUBP3]] (+0.67, fdr 1e-05), [[PGS1]] (+0.64, fdr 1e-05), [[TMED7-TICAM2]] (+0.63, fdr 7e-06); moves opposite to [[ARL4A]] (-0.60, fdr 1e-05), [[NEDD9]] (-0.57, fdr 3e-05), [[SFR1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.0 | 3e-04 | 25/42 (NCI-H1792, SHP-77, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.050 | 14/48 (A-172, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.050 | 13/44 (HS-578T, NCI-H23, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.092 | 13/47 (SHP-77, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 1.33× | +3.1 | 0.23 | 7/40 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.23 | 10/48 (NCI-H2030, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 10 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14906.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 3 lines (A498 0.0622×, hTERT-HPNE 0.0349×, PANC-1 0.162×; ⚠ cell-cycle shift, explains ~35% of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (HOP62 0.186×, hTERT-HPNE 0.109×, HT-29 0.193×; ⚠ cell-cycle shift, explains ~50% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (BT-474 0.0399×, KATO III 0.0788×; ⚠ cell-cycle shift, explains ~46% of this change); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (A498 0.152×); [[Isocorydine (drug)]] 0.5 µM in 1 line (HCT15 0.0986×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.385×** | -14.5 | 1e-44 | 36/46 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.327×** | -11.5 | 2e-28 | 38/46 (A498, hTERT-HPNE, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.468×** | -8.2 | 7e-14 | 28/44 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.473×** | -7.7 | 1e-12 | 31/40 (NCI-H2030, COLO 205, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.520×** | -7.0 | 3e-10 | 27/47 (BT-474, KATO III, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.548×** | -6.5 | 1e-08 | 27/43 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.589×** | -5.7 | 1e-06 | 25/46 (NCI-H1573, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **0.639×** | -4.8 | 1e-04 | 22/37 (KATO III, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.723×** | -3.3 | 0.052 | 12/36 (NCI-H2030, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.706×** | -3.2 | 0.074 | 14/46 (BT-474, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.71 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.02 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0622× (z -13.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.152× (z -9.1) |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0399× (z -14.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[PANC-1 (line)]] | alt | 7.60 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0994× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 5.93 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0811× (z -9.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[COLO 205 (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0712× (z -11.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 11.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -11.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[hTERT-HPNE (line)]] | wt | 9.31 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0349× (z -11.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 8.49 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0540× (z -13.5) ⚠ transcription drop; cell-cycle shift, explains ~69% of this change |
| [[NCI-H1573 (line)]] | alt | 4.92 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0799× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 8.90 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0612× (z -12.8) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 6.35 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 8.50 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -10.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 7.40 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -10.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[CFPAC-1 (line)]] | alt | 4.15 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -8.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0986× (z -8.7) |
| [[Hs 766T (line)]] | wt | 8.54 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -8.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HT-29 (line)]] | alt | 7.75 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -10.4) ⚠ cell-cycle shift, explains ~50% of this change |
| [[J82 (line)]] | alt | 5.81 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.118× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~69% of this change |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.152× (z -9.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.127× (z -8.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 8.19 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -9.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUBP3]] | +0.67 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[PGS1]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TMED7-TICAM2]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[UBOX5]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[APTX]] | +0.63 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[TMEM248]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[XPNPEP3]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TMPRSS5]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SNRPD3]] | +0.62 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[UQCC1]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[TIMM23B-AGAP6]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[TMEM11-DT]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL4A]] | -0.60 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[NEDD9]] | -0.57 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[SFR1]] | -0.56 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[PTGER4]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[TMEM42]] | -0.55 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[ISOC1]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[KLF4]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[LGALS3]] | -0.54 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[MAK]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[PIM3]] | -0.54 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[BIK]] | -0.53 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[MYLIP]] | -0.53 | -0.49 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STX16-NPEPL1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers STX16-NPEPL1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.440). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-11.3, 20.6); signed map (-47.0, 2.2). **Vector** length 63.4, 9.87% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.1 | +2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -5.6 | -14.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.2 | -11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.4 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.9 | -5.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.3 | -2.6 |
|  | [[Ritonavir (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | STX16-NPEPL1 readthrough (NMD candidate) |
| Locus type | readthrough (other) |
| Location | 20q13.32 — chr20:58,651,434-58,715,410 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100534593](https://www.ncbi.nlm.nih.gov/gene/100534593):

> This locus represents naturally occurring read-through transcription between the neighboring syntaxin 16 (STX16) and aminopeptidase-like 1 (NPEPL1) genes on chromosome 20. The read-through transcript is a candidate for nonsense-mediated mRNA decay (NMD), and is thus unlikely to produce a protein product. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:41993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41993) · Entrez [100534593](https://www.ncbi.nlm.nih.gov/gene/100534593) · Ensembl [ENSG00000254995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254995)

## Data

Gene col 14906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14906); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14906]; `tensor/DDL_lfc|DDL_z.npy` [14906]; `embed/gene_vectors.npy` [14906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14906 or target_col == 14906). Every well: [[STX16-NPEPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX16-NPEPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
