---
symbol: "CHGB"
type: "gene"
col: 1577
ensembl_id: "ENSG00000089199"
name: "chromogranin B"
location: "20p12.3"
module: 61
arm: "+"
pooled_cpm: 12.34
n_lines_expressing: 17
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 14
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# CHGB

*chromogranin B* — 20p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.61× (z +14.6, q 1e-45, up in 8 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.194×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.145×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.299×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCG3]] (+0.66, fdr 1e-05), [[VGF]] (+0.58, fdr 4e-05), [[ADARB2]] (+0.54, fdr 3e-05); moves opposite to [[TMPRSS5]] (-0.49, fdr 5e-05), [[MCM9]] (-0.48, fdr 4e-05), [[AGAP4]] (-0.46, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[NELL1]] → it (grade B ⚠); 14 go from it, the strongest it → [[DLX2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1577.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.61×** | +14.6 | 1e-45 | 8/11 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.86×** | +13.0 | 3e-36 | 7/7 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.23×** | +11.4 | 6e-28 | 5/5 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.78×** | +10.1 | 6e-22 | 6/6 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +8.0 | 2e-13 | 7/13 (SW480, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.19×** | +6.5 | 1e-08 | 6/10 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.15×** | +6.3 | 3e-08 | 10/11 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +6.2 | 4e-08 | 9/14 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +6.0 | 1e-07 | 6/10 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.01×** | +5.5 | 2e-06 | 8/12 (SW480, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +4.8 | 9e-05 | 6/14 (SW1417, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.79×** | +4.8 | 9e-05 | 1/11 (SW1417) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.59×** | +3.8 | 0.006 | 8/14 (SW480, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +3.8 | 0.006 | 5/12 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.58×** | +3.7 | 0.007 | 1/10 (A-427) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.53×** | +3.3 | 0.031 | 0/12 | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.034 | 2/11 (SHP-77, PANC-1) | rises with dose | position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.034 | 6/13 (SW 900, NCI-H1573, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.70×** | +3.1 | 0.053 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.071 | 0/12 | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +2.9 | 0.082 | 0/11 | top dose only | cell-cycle shift (explains ~6% here) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.43×** | +2.9 | 0.082 | 2/11 (NCI-H1573, A-427) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1577.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.194×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.145×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.299×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | 0.741× | -3.5 | 0.12 | 2/15 (A-427, C-33 A) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.640× | -3.4 | 0.12 | 1/14 (SW 1271) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.666× | -3.4 | 0.12 | 1/14 (NCI-H661) | inconsistent across doses |  |
| [[Pimozide (drug)]] 5 µM |  | 0.670× | -3.3 | 0.12 | 2/14 (NCI-H661, PANC-1) | top dose only | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.681× | -3.2 | 0.15 | 3/11 (C-33 A, SW1417, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.761× | -3.2 | 0.15 | 1/12 (HepG2/C3A) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.767× | -3.1 | 0.17 | 7/13 (SW1417, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.4 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +16.0) | — |
| [[NCI-H1573 (line)]] | alt | 7.24 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 17.7× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.45× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 456 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -17.0) |
| [[HepG2_C3A (line)]] | wt | 4.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.8× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.145× (z -9.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.9) | — |
| [[A-172 (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.25 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCG3]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 | same gene group; pathway: Post-translational protein phosphorylation; STRING 937 |
| [[VGF]] | +0.58 | +0.42 / +0.52 | both halves | 4e-05 | same gene group; pathway: Post-translational protein phosphorylation; STRING 698 |
| [[ADARB2]] | +0.54 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[FSTL4]] | +0.53 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[AFF2]] | +0.52 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[ONECUT2]] | +0.50 | +0.50 / +0.39 | both halves | 6e-05 |  |
| [[ANKRD20A9P]] | +0.50 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[SLITRK6]] | +0.50 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[LINC01194]] | +0.49 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[ELMO1]] | +0.49 | +0.46 / +0.37 | both halves | 8e-05 |  |
| [[LINC00408]] | +0.48 | +0.40 / +0.32 | both halves | 2e-04 |  |
| [[XKR7]] | +0.48 | +0.59 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMPRSS5]] | -0.49 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[MCM9]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[AGAP4]] | -0.46 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[ORC2]] | -0.44 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[LRRC69]] | -0.44 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[TMEM11-DT]] | -0.43 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[NFATC3]] | -0.42 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[SCLY]] | -0.42 | -0.25 / -0.36 | both halves | 4e-04 |  |
| [[TCEANC2]] | -0.42 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[HIRA]] | -0.42 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[FAM135A]] | -0.41 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[METTL4]] | -0.41 | -0.40 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NELL1]] | B | NELL1 activity raises CHGB's level | lines that do not express NELL1 (19) vs lines expressing it (31) | 2.25× lower at baseline in the lines without NELL1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ID4, RBM20, ENSG00000225096; maybe low, not absent |
| [[KCNH7]] | C | KCNH7 activity raises CHGB's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 2.83× lower at baseline in the lines without KCNH7 | 0.013 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[XKR7]] | C | XKR7 activity raises CHGB's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 3.81× lower at baseline in the lines without XKR7 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5; co-absent with the target |
| [[VGF]] | C | VGF activity raises CHGB's level | lines that do not express VGF (32) vs lines expressing it (18) | 2.82× lower at baseline in the lines without VGF | 0.018 | ⚠ within organs, on part of the lines; also absent: RAB3C, KCNH5, CSMD3; co-absent with the target |
| [[RAB3C]] | C | RAB3C activity raises CHGB's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 2.92× lower at baseline in the lines without RAB3C | 0.020 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[AFF2]] | C | AFF2 activity raises CHGB's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 2.40× lower at baseline in the lines without AFF2 | 0.029 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent; co-absent with the target |
| [[SCG3]] | C | SCG3 activity raises CHGB's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 3.53× lower at baseline in the lines without SCG3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA; co-absent with the target |
| [[SCG2]] | C | SCG2 activity raises CHGB's level | lines that do not express SCG2 (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without SCG2 | 0.085 | ⚠ within organs, on part of the lines; also absent: RNF175, ENSG00000225649, MIR3681HG; co-absent with the target |
| [[FREM2]] | C | FREM2 activity raises CHGB's level | lines that do not express FREM2 (26) vs lines expressing it (24) | 2.10× lower at baseline in the lines without FREM2 | 0.089 | ⚠ within organs, on part of the lines; also absent: NELL2, ANKRD20A11P, KCNH7; maybe low, not absent; co-absent with the target |
| [[LINC02197]] | C | LINC02197 activity raises CHGB's level | lines that do not express LINC02197 (35) vs lines expressing it (15) | 2.52× lower at baseline in the lines without LINC02197 | 0.089 | ⚠ within organs, on part of the lines; also absent: RIT2, SNTG1, CALCA; maybe low, not absent; co-absent with the target |
| [[COL22A1]] | C | COL22A1 activity raises CHGB's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 1.99× lower at baseline in the lines without COL22A1 | 0.098 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 7, C 7. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLX2]] | B | CHGB activity raises DLX2's level | lines that do not express CHGB (33) vs lines expressing it (17) | 2.78× lower at baseline in the lines without CHGB | 0.042 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |
| [[MCM9]] | B | CHGB activity raises MCM9's level | lines that do not express CHGB (33) vs lines expressing it (17) | 1.34× lower at baseline in the lines without CHGB | 0.048 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |
| [[SCLY]] | B | CHGB activity raises SCLY's level | lines that do not express CHGB (33) vs lines expressing it (17) | 1.53× lower at baseline in the lines without CHGB | 0.050 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |
| [[POLR3E]] | B | CHGB activity raises POLR3E's level | lines that do not express CHGB (33) vs lines expressing it (17) | 1.28× lower at baseline in the lines without CHGB | 0.053 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |
| [[ID2-AS1]] | B | CHGB activity raises ID2-AS1's level | lines that do not express CHGB (33) vs lines expressing it (17) | 2.10× lower at baseline in the lines without CHGB | 0.058 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |
| [[MAN1C1]] | B | CHGB activity raises MAN1C1's level | lines that do not express CHGB (33) vs lines expressing it (17) | 1.88× lower at baseline in the lines without CHGB | 0.063 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |
| [[NFATC3]] | B | CHGB activity raises NFATC3's level | lines that do not express CHGB (33) vs lines expressing it (17) | 1.42× lower at baseline in the lines without CHGB | 0.089 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |
| [[SRRM3]] | C | CHGB activity raises SRRM3's level | lines that do not express CHGB (33) vs lines expressing it (17) | 2.58× lower at baseline in the lines without CHGB | 0.006 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2; co-absent with the target |
| [[XKR7]] | C | CHGB activity raises XKR7's level | lines that do not express CHGB (33) vs lines expressing it (17) | 2.08× lower at baseline in the lines without CHGB | 0.028 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2; co-absent with the target |
| [[SCG3]] | C | CHGB activity raises SCG3's level | lines that do not express CHGB (33) vs lines expressing it (17) | 2.80× lower at baseline in the lines without CHGB | 0.029 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2; co-absent with the target |
| [[LINC01194]] | C | CHGB activity raises LINC01194's level | lines that do not express CHGB (33) vs lines expressing it (17) | 2.81× lower at baseline in the lines without CHGB | 0.041 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2; co-absent with the target |
| [[OLFM1]] | C | CHGB activity raises OLFM1's level | lines that do not express CHGB (33) vs lines expressing it (17) | 3.16× lower at baseline in the lines without CHGB | 0.044 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.473). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.9, 34.5); signed map (27.5, 33.2). **Vector** length 35.5, 9.79% of its response variance represented; |z| ≥ 3 in 262 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +14.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +1.3 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.0 | +1.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | +2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -3.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | chromogranin B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.3 — chr20:5,911,510-5,925,353 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SgI; previously SCG1 |
| Gene groups (HGNC) | Granins |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [P05060](https://www.uniprot.org/uniprotkb/P05060) (Secretogranin-1):

> Secretogranin-1 is a neuroendocrine secretory granule protein, which may be the precursor for other biologically active peptides.

**Summary**, from NCBI Gene [1114](https://www.ncbi.nlm.nih.gov/gene/1114):

> This gene encodes a tyrosine-sulfated secretory protein abundant in peptidergic endocrine cells and neurons. This protein may serve as a precursor for regulatory peptides. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:1930](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1930) · Entrez [1114](https://www.ncbi.nlm.nih.gov/gene/1114) · UniProt [P05060](https://www.uniprot.org/uniprotkb/P05060) · Ensembl [ENSG00000089199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089199)

## Data

Gene col 1577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1577); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1577]; `tensor/DDL_lfc|DDL_z.npy` [1577]; `embed/gene_vectors.npy` [1577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1577 or target_col == 1577). Every well: [[CHGB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHGB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
