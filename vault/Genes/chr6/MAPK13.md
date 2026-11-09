---
symbol: "MAPK13"
type: "gene"
col: 8010
ensembl_id: "ENSG00000156711"
name: "mitogen-activated protein kinase 13"
location: "6p21.31"
module: 55
arm: "+"
pooled_cpm: 20.85
n_lines_expressing: 35
n_dd_up: 13
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 20
direction_downstream: 21
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# MAPK13

*mitogen-activated protein kinase 13* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.03× (z +10.7, q 6e-24, up in 10 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.53× (z +4.8, q 2e-04, up in 8 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.582× (z -12.1, q 1e-30, down in 23 of 28 measured lines).
> Its strongest partners by |cos| (78 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPINT1-AS1]] (+0.56, fdr 4e-05), [[ARHGEF5]] (+0.53, fdr 2e-04), [[SYK]] (+0.49, fdr 5e-04); moves opposite to [[COL5A2]] (-0.50, fdr 2e-04), [[DCLK2]] (-0.44, fdr 6e-04), [[ID3]] (-0.43, fdr 1e-04).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[TNFSF15]] → it (grade B ⚠); 21 go from it, the strongest it → [[EAF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8010.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +10.7 | 6e-24 | 10/19 (NCI-H2347, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +9.7 | 7e-20 | 18/27 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +6.3 | 5e-08 | 13/24 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +4.8 | 2e-04 | 9/27 (SW480, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +4.8 | 2e-04 | 8/28 (NCI-H2347, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.48×** | +4.4 | 9e-04 | 16/30 (SW480, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.3 | 0.002 | 9/32 (NCI-H2347, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.0 | 0.004 | 8/23 (SW480, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.006 | 13/29 (SHP-77, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.010 | 9/31 (KATO III, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.019 | 9/30 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.4 | 0.027 | 0/33 | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.069 | 4/30 (HepG2/C3A, SW1417, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.084 | 8/30 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8010.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.582×** | -12.1 | 1e-30 | 23/28 (CFPAC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.531×** | -10.0 | 5e-21 | 23/32 (Panc 03.27, SW480, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.548×** | -9.5 | 5e-19 | 23/32 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.605×** | -7.9 | 3e-13 | 22/32 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.624×** | -7.4 | 1e-11 | 23/32 (HT-29, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.444×** | -6.7 | 2e-09 | 19/32 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.666×** | -6.4 | 1e-08 | 19/32 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.711×** | -5.4 | 5e-06 | 18/32 (NCI-H1792, BT-474, …) | all doses, flat | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.723×** | -5.1 | 2e-05 | 17/30 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.716×** | -5.1 | 2e-05 | 18/31 (SW 900, J82, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.706×** | -4.9 | 4e-05 | 16/30 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.763×** | -4.3 | 9e-04 | 12/31 (HOP62, LS 180, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.775×** | -4.0 | 0.003 | 17/31 (SW480, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.790×** | -3.7 | 0.008 | 16/32 (H4, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[NG25 (drug)]] 5 µM |  | **0.683×** | -3.2 | 0.057 | 6/28 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.806×** | -3.1 | 0.057 | 6/32 (RKO, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 115 | 0 | 12 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.112× (z -17.1) |
| [[HT-29 (line)]] | alt | 37.7 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -15.9) |
| [[LoVo (line)]] | wt | 35.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.130× (z -20.1) |
| [[LS 180 (line)]] | wt | 40.5 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -19.3) |
| [[Panc 03.27 (line)]] | alt | 61.6 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0998× (z -20.0) |
| [[SW480 (line)]] | alt | 30.6 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.149× (z -20.3) |
| [[BT-474 (line)]] | alt | 29.1 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 51.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -18.7) |
| [[HepG2_C3A (line)]] | wt | 142 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -10.3) |
| [[KATO III (line)]] | alt | 35.0 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.122× (z -17.4) |
| [[HCT15 (line)]] | alt | 42.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.1) |
| [[SW48 (line)]] | wt | 34.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0653× (z -15.3) |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0642× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 27.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 72.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -13.1) |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -11.0) |
| [[SW1417 (line)]] | alt | 21.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -9.1) |
| [[HS-578T (line)]] | alt | 5.66 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0728× (z -9.7) |
| [[J82 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.182× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~57% of this change |
| [[NCI-H1792 (line)]] | alt | 6.24 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0589× (z -11.7) |
| [[SW 900 (line)]] | alt | 5.98 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0579× (z -9.3) |
| [[A-172 (line)]] | wt | 4.68 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.73 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.34 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.03 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.73 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPINT1-AS1]] | +0.56 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[ARHGEF5]] | +0.53 | +0.61 / +0.30 | both halves | 2e-04 |  |
| [[SYK]] | +0.49 | +0.61 / +0.24 | both halves | 5e-04 | pathway: HALLMARK_APICAL_JUNCTION |
| [[TNFRSF14-AS1]] | +0.49 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[BDH1]] | +0.49 | +0.54 / +0.34 | both halves | 1e-04 |  |
| [[TMEM30B]] | +0.49 | +0.56 / +0.28 | both halves | 3e-04 |  |
| [[TMC4]] | +0.48 | +0.61 / +0.31 | both halves | 2e-04 |  |
| [[BCAR3-AS1]] | +0.48 | +0.43 / +0.24 | both halves | 5e-04 |  |
| [[LINC01277]] | +0.47 | +0.39 / +0.28 | both halves | 3e-04 |  |
| [[CASC8]] | +0.47 | +0.46 / +0.30 | both halves | 2e-04 |  |
| [[FAM83E]] | +0.47 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[DBNDD2]] | +0.46 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL5A2]] | -0.50 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[DCLK2]] | -0.44 | -0.53 / -0.21 | both halves | 6e-04 |  |
| [[ID3]] | -0.43 | -0.34 / -0.38 | both halves | 1e-04 | pathway: Signaling by NTRK1 (TRKA) |
| [[SAMD11]] | -0.42 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[PGM2L1]] | -0.40 | -0.40 / -0.24 | both halves | 4e-04 |  |
| [[DZIP1L]] | -0.40 | -0.49 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[KATNAL1]] | -0.40 | -0.38 / -0.27 | both halves | 3e-04 |  |
| [[GNB4]] | -0.39 | -0.44 / -0.17 | ⚠ not reproduced | 0.001 | STRING 737 |
| [[SOX12]] | -0.39 | -0.48 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[NOS1AP]] | -0.38 | -0.32 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 15, C 5. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFSF15]] | B | TNFSF15 activity raises MAPK13's level | lines that do not express TNFSF15 (31) vs lines expressing it (19) | 4.19× lower at baseline in the lines without TNFSF15 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[SYK]] | B | SYK activity raises MAPK13's level | lines that do not express SYK (30) vs lines expressing it (20) | 3.61× lower at baseline in the lines without SYK | 0.006 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[TMEM30B]] | B | TMEM30B activity raises MAPK13's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 3.94× lower at baseline in the lines without TMEM30B | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[FUT3]] | B | FUT3 activity raises MAPK13's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 2.53× lower at baseline in the lines without FUT3 | 0.008 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[MPZL2]] | B | MPZL2 activity raises MAPK13's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 3.62× lower at baseline in the lines without MPZL2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[TSPAN1]] | B | TSPAN1 activity raises MAPK13's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 3.10× lower at baseline in the lines without TSPAN1 | 0.018 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[MROH3P]] | B | MROH3P activity raises MAPK13's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 3.25× lower at baseline in the lines without MROH3P | 0.020 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[TSPOAP1]] | B | TSPOAP1 activity raises MAPK13's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 2.74× lower at baseline in the lines without TSPOAP1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2 |
| [[EPS8L1]] | B | EPS8L1 activity raises MAPK13's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.36× lower at baseline in the lines without EPS8L1 | 0.038 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[B3GNT3]] | B | B3GNT3 activity raises MAPK13's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.28× lower at baseline in the lines without B3GNT3 | 0.041 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[COL5A2]] | B | COL5A2 activity lowers MAPK13's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 2.91× higher at baseline in the lines without COL5A2 | 0.048 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2 |
| [[CHMP4C]] | B | CHMP4C activity raises MAPK13's level | lines that do not express CHMP4C (16) vs lines expressing it (34) | 3.35× lower at baseline in the lines without CHMP4C | 0.063 | ⚠ within organs, on part of the lines; also absent: TSTD1, BTC, TNK1 |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 16, C 5. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EAF1]] | B | MAPK13 activity weakens EAF1's drug response | lines that do not express MAPK13 (15) vs lines expressing it (33) | the lines without MAPK13 respond 1.14× as strongly (z diff -0.68); strongest at Homoharringtonine 5 µM: 2.11x vs 1.66x (z diff -2.4) | 0.039 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TMC4]] | B | MAPK13 activity raises TMC4's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 3.26× lower at baseline in the lines without MAPK13 | 0.042 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[SOX12]] | B | MAPK13 activity lowers SOX12's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 1.72× higher at baseline in the lines without MAPK13 | 0.058 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[SAMD11]] | B | MAPK13 activity lowers SAMD11's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 2.48× higher at baseline in the lines without MAPK13 | 0.058 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[MROH3P]] | B | MAPK13 activity raises MROH3P's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 2.87× lower at baseline in the lines without MAPK13 | 0.058 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[SYK]] | B | MAPK13 activity raises SYK's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 3.83× lower at baseline in the lines without MAPK13 | 0.060 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[ADAM8]] | B | MAPK13 activity raises ADAM8's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 2.02× lower at baseline in the lines without MAPK13 | 0.060 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[TNFSF15]] | B | MAPK13 activity raises TNFSF15's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 3.16× lower at baseline in the lines without MAPK13 | 0.065 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[CHMP4C]] | B | MAPK13 activity raises CHMP4C's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 3.77× lower at baseline in the lines without MAPK13 | 0.073 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[TNFRSF14-AS1]] | B | MAPK13 activity raises TNFRSF14-AS1's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without MAPK13 | 0.080 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[MUC20]] | B | MAPK13 activity raises MUC20's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 2.38× lower at baseline in the lines without MAPK13 | 0.080 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[COL5A2]] | B | MAPK13 activity lowers COL5A2's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 3.42× higher at baseline in the lines without MAPK13 | 0.083 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.366). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.6, 54.5); signed map (57.2, 10.1). **Vector** length 67.7, 14.2% of its response variance represented; |z| ≥ 3 in 764 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +0.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -3.1 |
|  | [[NG25 (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.2 | -1.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:36,127,809-36,144,524 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAPK4, p38delta; previously PRKM13 |
| Gene groups (HGNC) | Mitogen-activated protein kinase 11-14 (p38) family |
| Hallmark sets | APICAL_JUNCTION, ESTROGEN_RESPONSE_LATE |
| Reactome | 11 pathways, smallest: p38MAPK events; Signalling to RAS; NOD1/2 Signaling Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O15264](https://www.uniprot.org/uniprotkb/O15264) (Mitogen-activated protein kinase 13):

> Serine/threonine kinase which acts as an essential component of the MAP kinase signal transduction pathway. MAPK13 is one of the four p38 MAPKs which play an important role in the cascades of cellular responses evoked by extracellular stimuli such as pro-inflammatory cytokines or physical stress leading to direct activation of transcription factors such as ELK1 and ATF2. Accordingly, p38 MAPKs phosphorylate a broad range of proteins and it has been estimated that they may have approximately 200 …

**Summary**, from NCBI Gene [5603](https://www.ncbi.nlm.nih.gov/gene/5603):

> This gene encodes a member of the mitogen-activated protein (MAP) kinase family. MAP kinases act as an integration point for multiple biochemical signals, and are involved in a wide variety of cellular processes such as proliferation, differentiation, transcription regulation and development. The encoded protein is a p38 MAP kinase and is activated by proinflammatory cytokines and cellular stress. Substrates of the encoded protein include the transcription factor ATF2 and the microtubule …

**Accessions** — [HGNC:6875](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6875) · Entrez [5603](https://www.ncbi.nlm.nih.gov/gene/5603) · UniProt [O15264](https://www.uniprot.org/uniprotkb/O15264) · Ensembl [ENSG00000156711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156711)

## Data

Gene col 8010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8010); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8010]; `tensor/DDL_lfc|DDL_z.npy` [8010]; `embed/gene_vectors.npy` [8010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8010 or target_col == 8010). Every well: [[MAPK13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
