---
symbol: "HROB"
type: "gene"
col: 4601
ensembl_id: "ENSG00000125319"
name: "homologous recombination factor with OB-fold"
location: "17q21.31"
module: 91
arm: "+"
pooled_cpm: 11.91
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 22
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# HROB

*homologous recombination factor with OB-fold* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 2.37× (z +13.3, q 1e-37, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.457× (z -12.8, q 7e-35, down in 28 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.689× (z -8.6, q 1e-15, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF24]] (+0.76, fdr 7e-06), [[ZGRF1]] (+0.74, fdr 7e-06), [[RFWD3]] (+0.74, fdr 7e-06).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AURKB]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **2.37×** | +13.3 | 1e-37 | 41/45 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +10.6 | 8e-24 | 26/44 (A549, J82, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +7.2 | 1e-10 | 24/46 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +5.8 | 8e-07 | 19/43 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.24×** | +4.9 | 8e-05 | 15/46 (A549, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.35×** | +4.9 | 8e-05 | 12/45 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM |  | **1.33×** | +4.4 | 7e-04 | 9/46 (HOP62, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.30×** | +4.0 | 0.005 | 9/46 (LS 180, A-427, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.27×** | +3.9 | 0.007 | 8/46 (LS 180, A549, …) | rises with dose | composition shift |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.010 | 3/46 (LS 180, NCI-H23, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.25×** | +3.7 | 0.011 | 13/46 (A-427, SW480, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.17× | +3.6 | 0.016 | 6/47 (MIA PaCa-2, LS 180, …) | top dose only |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.24×** | +3.6 | 0.016 | 9/46 (KATO III, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.22×** | +3.2 | 0.055 | 11/46 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.064 | 3/46 (A-427, A549, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.090 | 2/35 (SW480, SHP-77) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4601.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.457×** | -12.8 | 7e-35 | 28/33 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -9.7 | 9e-20 | 16/21 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.689×** | -8.6 | 1e-15 | 30/47 (H4, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -7.0 | 3e-10 | 23/46 (A-427, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.675×** | -6.1 | 1e-07 | 22/46 (NCI-H1792, H4, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.693×** | -6.0 | 2e-07 | 24/46 (CFPAC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.739×** | -4.6 | 4e-04 | 15/28 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.772×** | -4.2 | 0.002 | 16/46 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 5 µM |  | **0.624×** | -4.0 | 0.003 | 15/44 (A549, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.787×** | -3.9 | 0.005 | 14/46 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.847× | -3.8 | 0.006 | 12/47 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.792×** | -3.8 | 0.007 | 15/46 (HOP62, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.791×** | -3.6 | 0.013 | 11/46 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.805×** | -3.5 | 0.015 | 12/46 (A-172, A-427, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.806×** | -3.5 | 0.015 | 12/46 (COLO 205, HCT15, …) | two highest doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.865× | -3.3 | 0.029 | 9/47 (A-427, C-33 A, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.816×** | -3.1 | 0.052 | 10/46 (A-172, HOP62, …) | top dose only |  |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **0.696×** | -3.1 | 0.054 | 7/43 (C32, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.850× | -3.1 | 0.057 | 10/47 (NCI-H23, A-427, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0353× (z -16.2) |
| [[A-172 (line)]] | wt | 14.9 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.200× (z -8.9) |
| [[A-427 (line)]] | wt | 17.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 27.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -15.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 16.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -8.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 8.68 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.143× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 25.1 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0891× (z -15.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 9.00 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.239× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 11.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -15.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 6.96 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0729× (z -9.6) |
| [[C32 (line)]] | wt | 6.79 | 0 | 1 | — | [[Filgotinib (drug)]] 0.5 µM 0.0385× (z -12.0) |
| [[H4 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0568× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -11.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 6.92 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM 0.0620× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -12.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 6.82 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -13.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 9.86 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0844× (z -11.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF24]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[ZGRF1]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[RFWD3]] | +0.74 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[POLA2]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[RFC2]] | +0.73 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[PLK4]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[ESPL1]] | +0.71 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[SUV39H1]] | +0.70 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[ATAD5]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[WDHD1]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[CDCA5]] | +0.69 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[ZNF724]] | +0.69 | +0.58 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AURKB]] | C | AURKB activity raises HROB's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.01× lower at baseline in the lines without AURKB | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[DIAPH3]], [[MELK]] | C | DIAPH3, MELK activity raises HROB's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 2.20× lower at baseline in the lines without DIAPH3, MELK | 0.098 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.797). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-37.6, -49.0); signed map (-42.7, -44.8). **Vector** length 95.0, 19.9% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.54 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.58 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +10.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.7 | +3.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | +0.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +2.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +5.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.7 | -12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.7 | -6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.4 | -6.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.5 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | homologous recombination factor with OB-fold |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,141,906-44,162,476 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3130, MCM8IP; previously C17orf53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3J3](https://www.uniprot.org/uniprotkb/Q8N3J3) (Homologous recombination OB-fold protein):

> DNA-binding protein involved in homologous recombination that acts by recruiting the MCM8-MCM9 helicase complex to sites of DNA damage to promote DNA repair synthesis. A C-terminal region including the OB-fold stimulates the helicase activity of MCM8-MCM9 probably by altering its conformation.

**Summary**, from NCBI Gene [78995](https://www.ncbi.nlm.nih.gov/gene/78995):

> Predicted to enable single-stranded DNA binding activity. Involved in DNA synthesis involved in DNA repair and interstrand cross-link repair. Located in site of DNA damage. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28460) · Entrez [78995](https://www.ncbi.nlm.nih.gov/gene/78995) · UniProt [Q8N3J3](https://www.uniprot.org/uniprotkb/Q8N3J3) · Ensembl [ENSG00000125319](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125319)

## Data

Gene col 4601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4601); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4601]; `tensor/DDL_lfc|DDL_z.npy` [4601]; `embed/gene_vectors.npy` [4601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4601 or target_col == 4601). Every well: [[HROB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HROB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
