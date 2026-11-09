---
symbol: "WDR54"
type: "gene"
col: 82
ensembl_id: "ENSG00000005448"
name: "WD repeat domain 54"
location: "2p13.1"
module: 79
arm: "+"
pooled_cpm: 18.77
n_lines_expressing: 46
n_dd_up: 1
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 8
direction_downstream: 4
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# WDR54

*WD repeat domain 54* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[XRK3F2 (drug)]] 0.5 µM: 1.86× (z +3.9, q 0.050, up in 21 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.213× (z -19.3, q 0e+00, down in 41 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKR7A2]] (+0.79, fdr 7e-06), [[VKORC1]] (+0.77, fdr 7e-06), [[PEX3]] (+0.69, fdr 7e-06); moves opposite to [[DPH5-DT]] (-0.61, fdr 1e-05), [[AVEN]] (-0.57, fdr 3e-05), [[ARAP2]] (-0.57, fdr 5e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MPP2]] → it (grade B ⚠); 4 go from it, the strongest it → [[C17orf58]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 82.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.86×** | +3.9 | 0.050 | 21/40 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.74× | +3.5 | 0.10 | 25/43 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.56× | +3.5 | 0.10 | 15/27 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 82.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.213×** | -19.3 | 0e+00 | 41/43 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.302×** | -10.6 | 1e-23 | 42/43 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.390×** | -7.3 | 6e-11 | 34/43 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -5.8 | 1e-06 | 35/43 (CFPAC-1, C32, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.527×** | -5.7 | 2e-06 | 31/43 (SW 1271, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.539×** | -5.5 | 4e-06 | 32/44 (C-33 A, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.505×** | -5.3 | 1e-05 | 28/42 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.578×** | -4.8 | 9e-05 | 28/43 (HOP62, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.593×** | -4.6 | 3e-04 | 29/44 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.604×** | -4.5 | 5e-04 | 27/44 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.607×** | -4.4 | 5e-04 | 27/44 (C-33 A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.611×** | -4.4 | 6e-04 | 26/43 (SW 900, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.594×** | -4.1 | 0.002 | 27/44 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.666×** | -3.6 | 0.013 | 21/43 (HS-578T, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.653×** | -3.6 | 0.014 | 21/44 (HCT15, H4, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.658×** | -3.5 | 0.017 | 23/43 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -3.4 | 0.025 | 19/43 (SNU-423, C32, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.444×** | -3.0 | 0.089 | 20/44 (H4, SW 900, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 82. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 24.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0638× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 14.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 32.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -13.0) |
| [[H4 (line)]] | wt | 25.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0497× (z -13.3) |
| [[HCT15 (line)]] | alt | 27.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -13.6) |
| [[HS-578T (line)]] | alt | 16.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0646× (z -14.7) |
| [[LoVo (line)]] | wt | 6.91 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 25.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 33.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 27.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0452× (z -25.8) |
| [[NCI-H460 (line)]] | wt | 20.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0674× (z -24.7) |
| [[SK-MEL-2 (line)]] | alt | 19.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0634× (z -11.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.0968× (z -9.9) |
| [[SW480 (line)]] | alt | 15.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -15.3) |
| [[A-172 (line)]] | wt | 30.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -13.5) |
| [[A-427 (line)]] | wt | 48.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.9) |
| [[A549 (line)]] | wt | 30.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -15.7) |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.174× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -12.6) |
| [[HOP62 (line)]] | alt | 35.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -15.9) |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -12.0) |
| [[HT-29 (line)]] | alt | 6.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0662× (z -10.0) ⚠ toxic |
| [[J82 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0973× (z -19.0) |
| [[NCI-H2030 (line)]] | alt | 33.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -20.3) |
| [[NCI-H2347 (line)]] | alt | 9.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -14.1) |
| [[PANC-1 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 28.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -8.8) |
| [[SHP-77 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -9.5) |
| [[SNU-423 (line)]] | alt | 21.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0637× (z -21.8) |
| [[SW 900 (line)]] | alt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -13.5) |
| [[SW1417 (line)]] | alt | 7.37 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0378× (z -12.1) |
| [[SW48 (line)]] | wt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -9.7) |
| [[A498 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.51 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.84 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 82), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKR7A2]] | +0.79 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.77 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[PEX3]] | +0.69 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.67 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[PDK3]] | +0.67 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[CABIN1]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[GAPDH]] | +0.66 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[PFKFB4]] | +0.66 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[SAP30-DT]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[MLLT3]] | +0.65 | +0.57 / +0.64 | both halves | 8e-06 |  |
| [[ABCB9]] | +0.64 | +0.63 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH5-DT]] | -0.61 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[AVEN]] | -0.57 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ARAP2]] | -0.57 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[CFAP161]] | -0.57 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ARMCX4]] | -0.56 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PTPRK]] | -0.55 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[EPM2A]] | -0.54 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[PCBD2]] | -0.53 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP2]] | B | MPP2 activity raises WDR54's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 3.05× lower at baseline in the lines without MPP2 | 0.012 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[GPR155]] | B | GPR155 activity raises WDR54's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 3.06× lower at baseline in the lines without GPR155 | 0.018 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[SLC2A3]] | B | SLC2A3 activity raises WDR54's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.97× lower at baseline in the lines without SLC2A3 | 0.043 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[SLC22A3]] | B | SLC22A3 activity lowers WDR54's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 1.86× higher at baseline in the lines without SLC22A3 | 0.048 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[LIX1L]] | B | LIX1L activity raises WDR54's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 2.19× lower at baseline in the lines without LIX1L | 0.054 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[KDM2B-DT]] | B | KDM2B-DT activity raises WDR54's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 2.05× lower at baseline in the lines without KDM2B-DT | 0.072 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[ISM2]] | B | ISM2 activity raises WDR54's level | lines that do not express ISM2 (9) vs lines expressing it (41) | 2.18× lower at baseline in the lines without ISM2 | 0.085 | ⚠ within organs, on part of the lines; also absent: DYSF, CSRP2, LINC02609; maybe low, not absent |
| [[UPK1A-AS1]] | B | UPK1A-AS1 activity raises WDR54's level | lines that do not express UPK1A-AS1 (18) vs lines expressing it (32) | 2.03× lower at baseline in the lines without UPK1A-AS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: CERS4, SUSD5, WIPF1 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C17orf58]] | C | WDR54 activity raises C17orf58's level | lines that do not express WDR54 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without WDR54 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: COPZ2, CNTLN, KLF9; maybe low, not absent; its own permutation p |
| [[MPP2]] | C | WDR54 activity raises MPP2's level | lines that do not express WDR54 (4) vs lines expressing it (46) | 2.96× lower at baseline in the lines without WDR54 | 0.072 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: COPZ2, CNTLN, KLF9; maybe low, not absent |
| [[TMEM39B]] | C | WDR54 activity raises TMEM39B's level | lines that do not express WDR54 (4) vs lines expressing it (46) | 1.81× lower at baseline in the lines without WDR54 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: COPZ2, CNTLN, KLF9; maybe low, not absent; its own permutation p |
| [[MRNIP]] | C | WDR54 activity raises MRNIP's level | lines that do not express WDR54 (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without WDR54 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: COPZ2, CNTLN, KLF9; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.8, -14.9); signed map (-35.1, 22.2). **Vector** length 88.2, 23.8% of its response variance represented; |z| ≥ 3 in 715 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.52 to 16); *hypoxia* (control, mean cos +0.56 to 5); *glycolysis* (hallmark, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | -4.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | -4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | -1.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +0.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.1 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -19.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | -0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.6 | -1.9 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.1 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 54 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,421,678-74,425,755 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12953 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H977](https://www.uniprot.org/uniprotkb/Q9H977) (WD repeat-containing protein 54):

> Plays a role in the adhesion and fusion of the sperm-oocyte membrane through its interactions with IZUMO1 and IZUMO1R/JUNO (By similarity). When cross-linked to form dimers and trimers, it has a regulatory effect on ERK signaling pathway activity in response to EGF stimulation. Colocalizes with the EGF receptor in WDR54-specific vesicle where it sustains the internalization and controls the degradation of the EGF receptor after EGF stimulation.

**Summary**, from NCBI Gene [84058](https://www.ncbi.nlm.nih.gov/gene/84058):

> Enables protein homodimerization activity. Involved in negative regulation of receptor internalization and regulation of epidermal growth factor receptor signaling pathway. Located in vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25770](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25770) · Entrez [84058](https://www.ncbi.nlm.nih.gov/gene/84058) · UniProt [Q9H977](https://www.uniprot.org/uniprotkb/Q9H977) · Ensembl [ENSG00000005448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005448)

## Data

Gene col 82: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 82); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 82, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 82]; `tensor/DDL_lfc|DDL_z.npy` [82]; `embed/gene_vectors.npy` [82]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 82 or target_col == 82). Every well: [[WDR54 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR54.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
