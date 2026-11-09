---
symbol: "COQ10B"
type: "gene"
col: 3687
ensembl_id: "ENSG00000115520"
name: "coenzyme Q10B"
location: "2q33.1"
module: 41
arm: "+"
pooled_cpm: 77.0
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# COQ10B

*coenzyme Q10B* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.09× (z +10.0, q 6e-21, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.648× (z -5.7, q 7e-06, down in 35 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.707× (z -4.5, q 0.002, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB5A]] (+0.79, fdr 7e-06), [[ARF4]] (+0.79, fdr 7e-06), [[SPTY2D1]] (+0.73, fdr 7e-06); moves opposite to [[ZC3HAV1L]] (-0.58, fdr 2e-05), [[HDAC2]] (-0.58, fdr 3e-05), [[TUBGCP4]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3687.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.09×** | +10.0 | 6e-21 | 48/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.50×** | +7.6 | 7e-12 | 35/48 (A-172, NCI-H460, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.66×** | +7.0 | 5e-10 | 39/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.58×** | +6.2 | 8e-08 | 37/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.45×** | +5.1 | 5e-05 | 33/48 (LS 180, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +4.4 | 9e-04 | 30/48 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.40×** | +4.4 | 9e-04 | 33/48 (AsPC-1, NCI-H460, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.37×** | +4.3 | 0.001 | 27/48 (NCI-H2030, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +4.3 | 0.001 | 30/48 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.006 | 28/49 (A498, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.30×** | +3.6 | 0.016 | 26/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.019 | 27/48 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.4 | 0.032 | 22/45 (A-427, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.032 | 22/48 (COLO 205, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.28×** | +3.3 | 0.033 | 25/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.035 | 24/49 (PANC-1, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.048 | 21/48 (HT-29, LS 180, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.054 | 24/48 (HT-29, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3687.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -5.7 | 7e-06 | 35/43 (H4, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -4.5 | 0.002 | 29/48 (hTERT-HPNE, C32, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.723×** | -4.4 | 0.002 | 31/48 (hTERT-HPNE, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.724×** | -4.4 | 0.002 | 32/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.804×** | -4.1 | 0.006 | 25/48 (A498, NCI-H2347, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.820×** | -3.7 | 0.017 | 22/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.833×** | -3.4 | 0.052 | 25/48 (AsPC-1, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.783×** | -3.2 | 0.094 | 24/48 (RKO, BT-474, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.798× | -3.1 | 0.13 | 18/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3687. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 114 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.59× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -11.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.494× (z -9.9) ⚠ cell-cycle shift, explains ~78% of this change |
| [[NCI-H460 (line)]] | wt | 74.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.4) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[A-172 (line)]] | wt | 73.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +11.0) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[A549 (line)]] | wt | 92.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.8) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[AN3 CA (line)]] | alt | 56.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -9.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 91.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -12.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 99.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.528× (z -8.6) ⚠ cell-cycle shift, explains ~78% of this change |
| [[HT-29 (line)]] | alt | 83.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.81× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 89.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 42.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.2) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 100 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +8.5) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H2347 (line)]] | alt | 68.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -10.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 73.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.13× (z +10.4) | — |
| [[RKO (line)]] | wt | 98.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.22× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 74.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.4) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[SW 1271 (line)]] | alt | 93.2 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.104× (z -9.0) |
| [[SW1417 (line)]] | alt | 91.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -11.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 61.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.12× (z +8.9) | — |
| [[A-427 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 70.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 85.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 79.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3687), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB5A]] | +0.79 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[ARF4]] | +0.79 | +0.83 / +0.70 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.73 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[BLZF1]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[STX5]] | +0.69 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[OSBP]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[YIPF5]] | +0.67 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[GTF2B]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SEC24A]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[STX5-DT]] | +0.64 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[SRA1]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[ACBD3]] | +0.64 | +0.68 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3HAV1L]] | -0.58 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[HDAC2]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TUBGCP4]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[IDH3A]] | -0.58 | -0.64 / -0.54 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[ANKRD52]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[RPE]] | -0.55 | -0.40 / -0.60 | both halves | 4e-05 |  |
| [[VMA21]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[CAD]] | -0.54 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[OTUD6B]] | -0.54 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[NAE1]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises COQ10B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.5, -36.9); signed map (-50.1, 14.4). **Vector** length 98.5, 28.9% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.54 to 8); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.4 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.3 | +0.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.1 | +0.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.6 | +6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.4 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | coenzyme Q10B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:197,453,493-197,475,310 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13448 |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8M1](https://www.uniprot.org/uniprotkb/Q9H8M1) (Coenzyme Q-binding protein COQ10 homolog B, mitochondrial):

> Required for the function of coenzyme Q in the respiratory chain. May serve as a chaperone or may be involved in the transport of Q6 from its site of synthesis to the catalytic sites of the respiratory complexes (By similarity).

**Summary**, from NCBI Gene [80219](https://www.ncbi.nlm.nih.gov/gene/80219):

> Predicted to enable ubiquinone binding activity. Predicted to be involved in cellular respiration. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25819](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25819) · Entrez [80219](https://www.ncbi.nlm.nih.gov/gene/80219) · UniProt [Q9H8M1](https://www.uniprot.org/uniprotkb/Q9H8M1) · Ensembl [ENSG00000115520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115520)

## Data

Gene col 3687: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3687); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3687, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3687]; `tensor/DDL_lfc|DDL_z.npy` [3687]; `embed/gene_vectors.npy` [3687]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3687 or target_col == 3687). Every well: [[COQ10B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COQ10B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
