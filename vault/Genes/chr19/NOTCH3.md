---
symbol: "NOTCH3"
type: "gene"
col: 1070
ensembl_id: "ENSG00000074181"
name: "notch receptor 3"
location: "19p13.12"
module: 47
arm: "+"
pooled_cpm: 20.05
n_lines_expressing: 36
n_dd_up: 5
n_dd_down: 38
n_dd_up_clean: 3
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# NOTCH3

*notch receptor 3* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.49× (z +8.1, q 4e-13, up in 17 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.379× (z -13.9, q 6e-41, down in 29 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FER1L4]] (+0.63, fdr 1e-05), [[SAMD14]] (+0.58, fdr 1e-05), [[PIP5KL1]] (+0.54, fdr 1e-05); moves opposite to [[DECR1]] (-0.46, fdr 6e-05), [[RAB11FIP2]] (-0.45, fdr 8e-05), [[SLC12A2-DT]] (-0.44, fdr 1e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ZNF471]] → it (grade B ⚠); 3 go from it, the strongest it → [[SLC25A51]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +8.1 | 4e-13 | 17/34 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +6.0 | 5e-07 | 16/34 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +3.7 | 0.041 | 4/17 (NCI-H1573, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.041 | 9/34 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.6 | 0.043 | 7/22 (A-172, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.23 | 9/34 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1070.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.379×** | -13.9 | 6e-41 | 29/34 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.429×** | -11.6 | 1e-28 | 24/33 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.450×** | -11.4 | 8e-28 | 28/34 (RPMI-7951, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.454×** | -11.3 | 3e-27 | 25/34 (hTERT-HPNE, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.468×** | -10.8 | 2e-25 | 26/32 (RPMI-7951, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.478×** | -10.5 | 6e-24 | 25/34 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.507×** | -9.3 | 9e-19 | 25/34 (RPMI-7951, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.576×** | -7.9 | 3e-13 | 25/34 (RPMI-7951, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -7.8 | 3e-13 | 23/33 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.608×** | -7.1 | 7e-11 | 16/34 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.608×** | -6.8 | 4e-10 | 22/31 (RPMI-7951, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -6.3 | 1e-08 | 19/34 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.656×** | -6.0 | 8e-08 | 17/33 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.677×** | -5.6 | 1e-06 | 20/34 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.693×** | -5.0 | 2e-05 | 14/32 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.709×** | -4.9 | 3e-05 | 15/32 (NCI-H2347, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.720×** | -4.7 | 1e-04 | 15/33 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.722×** | -4.4 | 4e-04 | 7/33 (NCI-H23, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -3.9 | 0.003 | 14/34 (A-172, BT-474, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 49.0 | 0 | 16 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0618× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0686× (z -15.4) |
| [[BT-474 (line)]] | alt | 97.1 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -13.0) |
| [[HOP62 (line)]] | alt | 34.4 | 0 | 9 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.142× (z -11.2) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.154× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 117 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -11.0) |
| [[A-172 (line)]] | wt | 83.3 | 1 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 62.4 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -16.3) |
| [[NCI-H23 (line)]] | alt | 17.3 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 33.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 42.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.314× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 39.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -10.0) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.197× (z -8.5) |
| [[H4 (line)]] | wt | 14.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0660× (z -9.6) |
| [[LoVo (line)]] | wt | 13.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 16.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.246× (z -8.8) |
| [[PANC-1 (line)]] | alt | 7.27 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.207× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 8.45 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.98 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.28 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FER1L4]] | +0.63 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[SAMD14]] | +0.58 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[PIP5KL1]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ASMTL]] | +0.54 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[ADSS1]] | +0.53 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[PLEKHG4B]] | +0.51 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[NTRK1]] | +0.50 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[APC2]] | +0.50 | +0.46 / +0.38 | both halves | 6e-05 |  |
| [[ITGA2B]] | +0.50 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[NPAS1]] | +0.50 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[SPATA32]] | +0.49 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[MYO15A]] | +0.49 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.46 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[RAB11FIP2]] | -0.45 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[SLC12A2-DT]] | -0.44 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[RNASEH2B]] | -0.44 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[NUP50-DT]] | -0.43 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[ATR]] | -0.43 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[HNF4G]] | -0.43 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[ZNG1E]] | -0.42 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[ORMDL1]] | -0.42 | -0.47 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[HSPBAP1]] | -0.42 | -0.35 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF471]] | B | ZNF471 activity raises NOTCH3's level | lines that do not express ZNF471 (28) vs lines expressing it (22) | 2.84× lower at baseline in the lines without ZNF471 | 0.022 | ⚠ within organs, on part of the lines; also absent: TRIML2, ZNF667, ZNF667-AS1 |
| [[PDGFRB]] | B | PDGFRB activity raises NOTCH3's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.97× lower at baseline in the lines without PDGFRB | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[SLC22A17]] | B | SLC22A17 activity raises NOTCH3's level | lines that do not express SLC22A17 (21) vs lines expressing it (29) | 2.97× lower at baseline in the lines without SLC22A17 | 0.057 | ⚠ within organs, on part of the lines; also absent: APBA2, TUB, COLEC12 |
| [[TOP2A]] | B | TOP2A activity raises NOTCH3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity raises NOTCH3's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.91× lower at baseline in the lines without TMEM92-AS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[TNFSF9]] | B | TNFSF9 activity lowers NOTCH3's level | lines that do not express TNFSF9 (6) vs lines expressing it (44) | 3.74× higher at baseline in the lines without TNFSF9 | 0.089 | ⚠ within organs, on part of the lines; also absent: SNAI1; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A51]] | B | NOTCH3 activity raises SLC25A51's level | lines that do not express NOTCH3 (14) vs lines expressing it (36) | 1.46× lower at baseline in the lines without NOTCH3 | 0.067 | ⚠ within organs, on part of the lines; also absent: WNT5B, GPR68, RNF150; maybe low, not absent |
| [[MRC2]] | B | NOTCH3 activity raises MRC2's level | lines that do not express NOTCH3 (14) vs lines expressing it (36) | 3.29× lower at baseline in the lines without NOTCH3 | 0.073 | ⚠ within organs, on part of the lines; also absent: WNT5B, GPR68, RNF150; maybe low, not absent |
| [[KIF17]] | B | NOTCH3 activity raises KIF17's level | lines that do not express NOTCH3 (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without NOTCH3 | 0.083 | ⚠ within organs, on part of the lines; also absent: WNT5B, GPR68, RNF150; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.457). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.1, -17.3); signed map (16.5, 17.3). **Vector** length 85.2, 19.1% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.5 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | -2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -13.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -10.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -11.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.7 | -6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -11.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | notch receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:15,159,038-15,200,995 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CASIL; previously CADASIL |
| Gene groups (HGNC) | Notch receptors; MicroRNA protein coding host genes |
| Hallmark sets | NOTCH_SIGNALING |
| Reactome | 14 pathways, smallest: Defective LFNG causes SCDO3; Pre-NOTCH Processing in the Endoplasmic Reticulum; Noncanonical activation of NOTCH3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UM47](https://www.uniprot.org/uniprotkb/Q9UM47) (Neurogenic locus notch homolog protein 3):

> Functions as a receptor for membrane-bound ligands Jagged1, Jagged2 and Delta1 to regulate cell-fate determination. Upon ligand activation through the released notch intracellular domain (NICD), it forms a transcriptional activator complex with RBPJ/RBPSUH and activates genes of the enhancer of split locus. Affects the implementation of differentiation, proliferation and apoptotic programs (By similarity).

**Summary**, from NCBI Gene [4854](https://www.ncbi.nlm.nih.gov/gene/4854):

> This gene encodes the third discovered human homologue of the Drosophilia melanogaster type I membrane protein notch. In Drosophilia, notch interaction with its cell-bound ligands (delta, serrate) establishes an intercellular signalling pathway that plays a key role in neural development. Homologues of the notch-ligands have also been identified in human, but precise interactions between these ligands and the human notch homologues remains to be determined. Mutations in NOTCH3 have been …

**Accessions** — [HGNC:7883](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7883) · Entrez [4854](https://www.ncbi.nlm.nih.gov/gene/4854) · UniProt [Q9UM47](https://www.uniprot.org/uniprotkb/Q9UM47) · Ensembl [ENSG00000074181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074181)

## Data

Gene col 1070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1070); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1070]; `tensor/DDL_lfc|DDL_z.npy` [1070]; `embed/gene_vectors.npy` [1070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1070 or target_col == 1070). Every well: [[NOTCH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOTCH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
