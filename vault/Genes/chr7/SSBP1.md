---
symbol: "SSBP1"
type: "gene"
col: 2710
ensembl_id: "ENSG00000106028"
name: "single stranded DNA binding protein 1"
location: "7q34"
module: 23
arm: "+"
pooled_cpm: 81.51
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SSBP1

*single stranded DNA binding protein 1* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.32× (z +14.2, q 3e-43, up in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.53× (z +7.2, q 7e-11, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.719× (z -5.6, q 1e-05, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YAE1]] (+0.69, fdr 1e-05), [[AIMP1]] (+0.69, fdr 7e-06), [[METTL6]] (+0.60, fdr 1e-05); moves opposite to [[ECE1]] (-0.51, fdr 4e-05), [[GAS2L1]] (-0.49, fdr 2e-04), [[INPP5A]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2710.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.32×** | +14.2 | 3e-43 | 44/49 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +12.3 | 2e-32 | 38/44 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +8.9 | 7e-17 | 33/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +7.2 | 7e-11 | 43/48 (NCI-H23, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +6.5 | 7e-09 | 36/48 (NCI-H1792, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~25% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +5.1 | 3e-05 | 24/48 (C32, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.33×** | +4.7 | 3e-04 | 28/47 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.31×** | +4.6 | 3e-04 | 27/48 (SW480, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.9 | 0.005 | 26/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.5 | 0.029 | 23/48 (SW48, Hs 766T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.21× | +3.1 | 0.11 | 18/47 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.11 | 18/48 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2710.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.719×** | -5.6 | 1e-05 | 34/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.741×** | -5.1 | 9e-05 | 33/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.774×** | -4.4 | 0.002 | 27/48 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.780×** | -4.2 | 0.003 | 27/48 (CFPAC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.800×** | -3.8 | 0.016 | 26/48 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2710. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 58.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.72× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 130 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.23× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 80.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +13.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 122 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +13.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 63.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +13.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 98.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 66.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +10.2) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 92.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +12.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 71.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 65.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 46.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 77.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 136 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +10.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 73.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 119 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.19× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 87.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 51.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 63.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 77.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +10.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 75.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 85.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +11.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 70.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 71.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +8.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 69.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 95.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 92.5 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0778× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 87.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 85.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 120 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 94.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2710), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YAE1]] | +0.69 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[AIMP1]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 | STRING 416 |
| [[METTL6]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TAS2R4]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 | ⚠ **readthrough risk**: TAS2R4 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[COPS5]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[ZRANB2]] | +0.59 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[ZNF596]] | +0.58 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[MKRN3]] | +0.57 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ZNF283]] | +0.57 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[THAP6]] | +0.56 | +0.60 / +0.37 | both halves | 8e-05 |  |
| [[TRMT13]] | +0.56 | +0.62 / +0.34 | both halves | 1e-04 |  |
| [[OCIAD1]] | +0.56 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[MSTO1]] | +0.56 | +0.55 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECE1]] | -0.51 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[GAS2L1]] | -0.49 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[INPP5A]] | -0.49 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[INPP5F]] | -0.49 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[PBX4]] | -0.48 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[APLP2]] | -0.48 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[CYTH3]] | -0.47 | -0.52 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SSBP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.513). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-23.5, 7.1); signed map (9.2, -23.6). **Vector** length 77.8, 20.6% of its response variance represented; |z| ≥ 3 in 646 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.1 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +7.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +2.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.9 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | -4.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.5 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.3 | -4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.3 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | +0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -0.6 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | single stranded DNA binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:141,738,334-141,787,922 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SSBP, mtSSB |
| Gene groups (HGNC) | Mitochondrial nucleoid associated proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 6 pathways, smallest: Strand-asynchronous mitochondrial DNA replication; Transcriptional activation of mitochondrial biogenesis; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04837](https://www.uniprot.org/uniprotkb/Q04837) (Single-stranded DNA-binding protein, mitochondrial):

> Binds preferentially and cooperatively to pyrimidine rich single-stranded DNA (ss-DNA). In vitro, required to maintain the copy number of mitochondrial DNA (mtDNA) and plays a crucial role during mtDNA replication by stimulating the activity of the replisome components POLG and TWNK at the replication fork. Promotes the activity of the gamma complex polymerase POLG, largely by organizing the template DNA and eliminating secondary structures to favor ss-DNA conformations that facilitate POLG …

**Summary**, from NCBI Gene [6742](https://www.ncbi.nlm.nih.gov/gene/6742):

> SSBP1 is a housekeeping gene involved in mitochondrial biogenesis (Tiranti et al., 1995 [PubMed 7789991]). It is also a subunit of a single-stranded DNA (ssDNA)-binding complex involved in the maintenance of genome stability (Huang et al., 2009) [PubMed 19683501].[supplied by OMIM, Feb 2010]

**Accessions** — [HGNC:11317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11317) · Entrez [6742](https://www.ncbi.nlm.nih.gov/gene/6742) · UniProt [Q04837](https://www.uniprot.org/uniprotkb/Q04837) · Ensembl [ENSG00000106028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106028)

## Data

Gene col 2710: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2710); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2710, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2710]; `tensor/DDL_lfc|DDL_z.npy` [2710]; `embed/gene_vectors.npy` [2710]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2710 or target_col == 2710). Every well: [[SSBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
