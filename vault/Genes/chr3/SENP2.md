---
symbol: "SENP2"
type: "gene"
col: 8805
ensembl_id: "ENSG00000163904"
name: "SUMO specific peptidase 2"
location: "3q27.2"
module: 41
arm: "+"
pooled_cpm: 73.4
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SENP2

*SUMO specific peptidase 2* — 3q27.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.02× (z +15.9, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.732× (z -6.7, q 9e-09, down in 28 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Vilanterol (drug)]] 0.5 µM: 0.821× (z -4.4, q 0.001, down in 19 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAP29]] (+0.68, fdr 1e-05), [[MMUT]] (+0.68, fdr 7e-06), [[INIP]] (+0.63, fdr 1e-05); moves opposite to [[UCK2]] (-0.61, fdr 1e-05), [[KTN1-AS1]] (-0.58, fdr 2e-05), [[GALNT14]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8805.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.02×** | +15.9 | 0e+00 | 46/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +15.9 | 0e+00 | 47/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +15.5 | 0e+00 | 39/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +12.2 | 2e-32 | 44/48 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.26×** | +5.3 | 1e-05 | 28/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.46×** | +4.5 | 7e-04 | 22/49 (SW480, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.15× | +4.5 | 7e-04 | 19/48 (LoVo, RKO, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 0.002 | 23/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.20× | +4.1 | 0.002 | 18/48 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.732×** | -6.7 | 9e-09 | 28/47 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -6.1 | 4e-07 | 1/50 (NCI-H661) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.808×** | -4.8 | 3e-04 | 23/49 (SW480, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.821×** | -4.4 | 0.001 | 19/48 (NCI-H1792, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.831×** | -4.2 | 0.003 | 21/49 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | **0.830×** | -4.0 | 0.006 | 21/42 (KATO III, C-33 A, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.894× | -3.6 | 0.026 | 13/48 (NCI-H2347, LoVo, …) | two highest doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.802×** | -3.5 | 0.026 | 20/48 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.849× | -3.5 | 0.026 | 18/48 (NCI-H1792, A-172, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.858× | -3.4 | 0.033 | 13/48 (NCI-H1792, COLO 205, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.809×** | -3.4 | 0.033 | 15/48 (hTERT-HPNE, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.852× | -3.4 | 0.033 | 10/47 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.864× | -3.3 | 0.044 | 14/48 (LoVo, SK-MEL-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **0.816×** | -3.3 | 0.044 | 13/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.826×** | -3.2 | 0.051 | 22/45 (NCI-H23, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 113 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.542× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[H4 (line)]] | wt | 81.4 | 0 | 5 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Sonidegib (drug)]] 5 µM 0.126× (z -8.7) |
| [[A-427 (line)]] | wt | 65.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 80.3 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +14.3) | — |
| [[LoVo (line)]] | wt | 62.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +13.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 83.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.07× (z +12.5) | — |
| [[PANC-1 (line)]] | alt | 71.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +13.5) | — |
| [[A-172 (line)]] | wt | 67.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.14× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 49.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.97× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[NCI-H460 (line)]] | wt | 47.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +12.0) | — |
| [[BT-474 (line)]] | alt | 67.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +8.6) | — |
| [[C32 (line)]] | wt | 50.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.2) | [[Lonafarnib (drug)]] 5 µM 0.151× (z -8.5) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 49.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.51× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 58.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 76.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.78× (z +10.9) | — |
| [[SW48 (line)]] | wt | 49.7 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.34× (z +8.7) | [[Megestrol (drug)]] 0.5 µM 0.301× (z -8.6) |
| [[A498 (line)]] | wt | 73.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.12× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 56.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 70.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 65.0 | 0 | 1 | — | [[Futibatinib (drug)]] 5 µM 0.179× (z -8.8) |
| [[HT-29 (line)]] | alt | 68.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 51.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 95.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.8) | — |
| [[KATO III (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[NCI-H1573 (line)]] | alt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 44.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -11.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 51.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 63.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[SW 1088 (line)]] | alt | 78.3 | 0 | 1 | — | [[Cyclosporin A (drug)]] 5 µM 0.0670× (z -9.8) |
| [[A549 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAP29]] | +0.68 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[MMUT]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[INIP]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[FAM161B]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ALDH6A1]] | +0.60 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[RAD17]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ZMYM6]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[STEEP1]] | +0.57 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[C6orf89]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[LTN1]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[DIABLO]] | +0.56 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[GOLGA2]] | +0.56 | +0.59 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UCK2]] | -0.61 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[KTN1-AS1]] | -0.58 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[GALNT14]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CHD7]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[PPARGC1B]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[TULP4]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TBC1D4]] | -0.53 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[ZDHHC14]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[TTC39C]] | -0.52 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[KANK1]] | -0.52 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[ABCC4]] | -0.51 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[DOCK9]] | -0.51 | -0.57 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SENP2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KCNIP3]] | B | KCNIP3 activity raises SENP2's level | lines that do not express KCNIP3 (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without KCNIP3 | 0.086 | ⚠ within organs, on part of the lines; also absent: MCF2L2, GOLGA2P5-1, DMBX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.1, -34.2); signed map (-13.2, 2.5). **Vector** length 94.9, 22.9% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.8 | +15.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +15.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +15.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.6 | +0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.5 | +0.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.0 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.9 | -6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | SUMO specific peptidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.2 — chr3:185,582,496-185,633,551 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SMT3IP2, KIAA1331, DKFZp762A2316, AXAM2 |
| Gene groups (HGNC) | SUMO specific peptidases |
| Reactome | 3 pathways, smallest: SUMO is proteolytically processed; Processing and activation of SUMO; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC62](https://www.uniprot.org/uniprotkb/Q9HC62) (Sentrin-specific protease 2):

> Protease that catalyzes two essential functions in the SUMO pathway. The first is the hydrolysis of an alpha-linked peptide bond at the C-terminal end of the small ubiquitin-like modifier (SUMO) propeptides, SUMO1, SUMO2 and SUMO3 leading to the mature form of the proteins. The second is the deconjugation of SUMO1, SUMO2 and SUMO3 from targeted proteins, by cleaving an epsilon-linked peptide bond between the C-terminal glycine of the mature SUMO and the lysine epsilon-amino group of the target …

**Summary**, from NCBI Gene [59343](https://www.ncbi.nlm.nih.gov/gene/59343):

> SUMO1 (UBL1; MIM 601912) is a small ubiquitin-like protein that can be covalently conjugated to other proteins. SENP2 is one of a group of enzymes that process newly synthesized SUMO1 into the conjugatable form and catalyze the deconjugation of SUMO1-containing species.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:23116](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23116) · Entrez [59343](https://www.ncbi.nlm.nih.gov/gene/59343) · UniProt [Q9HC62](https://www.uniprot.org/uniprotkb/Q9HC62) · Ensembl [ENSG00000163904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163904)

## Data

Gene col 8805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8805); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8805]; `tensor/DDL_lfc|DDL_z.npy` [8805]; `embed/gene_vectors.npy` [8805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8805 or target_col == 8805). Every well: [[SENP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SENP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
