---
symbol: "PRPF38A"
type: "gene"
col: 5596
ensembl_id: "ENSG00000134748"
name: "pre-mRNA processing factor 38A"
location: "1p32.3"
module: 41
arm: "+"
pooled_cpm: 41.49
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# PRPF38A

*pre-mRNA processing factor 38A* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.29× (z +15.0, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.811× (z -5.4, q 4e-05, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNIP1]] (+0.60, fdr 1e-05), [[RNF40]] (+0.53, fdr 3e-05), [[EDC3]] (+0.52, fdr 2e-05); moves opposite to [[EPS15]] (-0.55, fdr 2e-05), [[JADE3]] (-0.52, fdr 1e-05), [[CTIF]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5596.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.29×** | +15.0 | 0e+00 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.61×** | +12.2 | 7e-32 | 42/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +11.7 | 3e-29 | 41/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.90×** | +10.1 | 1e-21 | 43/49 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +9.2 | 5e-18 | 36/47 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +8.1 | 5e-14 | 34/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +8.1 | 5e-14 | 37/48 (SW480, LoVo, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +8.1 | 6e-14 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +6.1 | 5e-08 | 33/48 (RKO, HT-29, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +6.0 | 9e-08 | 0/48 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 5e-07 | 29/48 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +5.2 | 9e-06 | 31/46 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +5.2 | 9e-06 | 28/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.0 | 2e-05 | 24/47 (HT-29, SNU-1, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.4 | 4e-04 | 22/48 (PANC-1, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +4.4 | 4e-04 | 24/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.034 | 9/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.037 | 17/48 (SW480, LS 180, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.050 | 9/48 (MIA PaCa-2, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.091 | 13/48 (SW480, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5596.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.811×** | -5.4 | 4e-05 | 25/48 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.750×** | -5.2 | 5e-05 | 27/48 (HOP62, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.785×** | -4.2 | 0.005 | 19/47 (H4, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.801×** | -4.0 | 0.008 | 26/48 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.861× | -3.7 | 0.023 | 14/48 (A549, NCI-H23, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.816×** | -3.6 | 0.035 | 16/48 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.821×** | -3.4 | 0.046 | 16/48 (HS-578T, J82, …) | top dose only |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.847× | -3.0 | 0.18 | 15/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.0 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.19× (z +20.1) | — |
| [[PANC-1 (line)]] | alt | 40.9 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.20× (z +16.6) | — |
| [[SW480 (line)]] | alt | 51.8 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +15.8) | — |
| [[NCI-H1573 (line)]] | alt | 50.9 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.07× (z +13.0) | — |
| [[A-172 (line)]] | wt | 23.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 50.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +9.7) | — |
| [[J82 (line)]] | alt | 49.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +9.7) | — |
| [[KATO III (line)]] | alt | 35.2 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.46× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +12.6) | — |
| [[LoVo (line)]] | wt | 37.3 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 37.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.84× (z +13.8) | — |
| [[AsPC-1 (line)]] | alt | 45.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.18× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 28.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.69× (z +10.5) | — |
| [[CHP-212 (line)]] | wt | 26.5 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0836× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 41.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.11× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 31.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 44.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 51.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LOX-IMVI (line)]] | wt | 41.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 33.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 50.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +8.8) | — |
| [[NCI-H661 (line)]] | alt | 48.9 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0785× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 42.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 33.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.0) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW1417 (line)]] | alt | 34.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +9.4) | — |
| [[A-427 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNIP1]] | +0.60 | +0.67 / +0.56 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 987 |
| [[RNF40]] | +0.53 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[EDC3]] | +0.52 | +0.47 / +0.56 | both halves | 2e-05 | STRING 513 |
| [[SENP2]] | +0.52 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[ECD]] | +0.51 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[ZNF548]] | +0.51 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[SMU1]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 995 |
| [[MED6]] | +0.51 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[RTF2]] | +0.50 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[MAGOH]] | +0.50 | +0.43 / +0.54 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[SDE2]] | +0.49 | +0.55 / +0.53 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ZNF417]] | +0.49 | +0.45 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS15]] | -0.55 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[JADE3]] | -0.52 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[CTIF]] | -0.48 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[CDK8]] | -0.48 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[MFHAS1]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[CCSER2]] | -0.47 | -0.32 / -0.61 | both halves | 2e-04 |  |
| [[DENND5A]] | -0.47 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[MAP4]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[CDYL]] | -0.46 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[KPNA1]] | -0.45 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[KPNA3]] | -0.45 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[SGMS1]] | -0.45 | -0.51 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PRPF38A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.403). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.8, -11.5); signed map (-13.2, -27.1). **Vector** length 76.2, 16.7% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +8.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | +3.0 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +5.0 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.7 | +0.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +0.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.4 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | +0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.2 | -2.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.2 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -2.9 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | +3.2 |

## What is on record

|  |  |
|---|---|
| Name | pre-mRNA processing factor 38A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:52,404,602-52,420,836 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14936, Prp38 |
| Gene groups (HGNC) | Spliceosomal B complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NAV1](https://www.uniprot.org/uniprotkb/Q8NAV1) (Pre-mRNA-splicing factor 38A):

> Involved in pre-mRNA splicing as a component of the spliceosome.

**Summary**, from NCBI Gene [84950](https://www.ncbi.nlm.nih.gov/gene/84950):

> Enables RNA binding activity. Involved in mRNA splicing, via spliceosome. Located in nucleoplasm. Part of U2-type precatalytic spliceosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25930](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25930) · Entrez [84950](https://www.ncbi.nlm.nih.gov/gene/84950) · UniProt [Q8NAV1](https://www.uniprot.org/uniprotkb/Q8NAV1) · Ensembl [ENSG00000134748](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134748)

## Data

Gene col 5596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5596); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5596]; `tensor/DDL_lfc|DDL_z.npy` [5596]; `embed/gene_vectors.npy` [5596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5596 or target_col == 5596). Every well: [[PRPF38A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPF38A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
