---
symbol: "TMEM80"
type: "gene"
col: 10782
ensembl_id: "ENSG00000177042"
name: "transmembrane protein 80"
location: "11p15.5"
module: 23
arm: "+"
pooled_cpm: 5.55
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# TMEM80

*transmembrane protein 80* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.16× (z +9.3, q 8e-18, up in 19 of 28 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.64× (z +8.8, q 4e-16, up in 18 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.593× (z -6.6, q 3e-08, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZSCAN16-AS1]] (+0.63, fdr 2e-05), [[RBM26-AS1]] (+0.63, fdr 2e-05), [[HEXIM2-AS1]] (+0.62, fdr 9e-05); moves opposite to [[TMEM92]] (-0.61, fdr 2e-04), [[SPTLC2]] (-0.57, fdr 9e-04, ⚠ one half only (not replicated)), [[EDA]] (-0.54, fdr 3e-04), [[RASSF7]] (-0.53, fdr 7e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10782.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +9.3 | 8e-18 | 19/28 (NCI-H1573, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +9.2 | 8e-18 | 17/21 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +8.8 | 4e-16 | 18/37 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +8.7 | 4e-16 | 5/10 (NCI-H2347, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +8.5 | 2e-15 | 5/9 (SW480, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +5.7 | 1e-06 | 18/39 (KATO III, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.4 | 4e-06 | 18/40 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.5 | 6e-04 | 14/46 (HOP62, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.001 | 8/46 (HT-29, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.031 | 17/43 (HT-29, LoVo, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.031 | 4/44 (HCT15, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.3 | 0.044 | 7/27 (NCI-H460, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.050 | 5/43 (HT-29, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.071 | 12/44 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.079 | 3/26 (KATO III, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.097 | 1/47 (PANC-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10782.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.593×** | -6.6 | 3e-08 | 23/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.661×** | -5.2 | 4e-05 | 16/47 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.662×** | -5.2 | 4e-05 | 19/45 (C-33 A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Malotilate (drug)]] 0.05 µM |  | **0.701×** | -4.5 | 0.001 | 5/43 (HCT15, LoVo, …) | inconsistent across doses | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.718×** | -4.2 | 0.003 | 15/43 (SNU-423, HS-578T, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.747×** | -3.7 | 0.022 | 9/46 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.753×** | -3.6 | 0.027 | 6/47 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.764×** | -3.4 | 0.046 | 9/43 (SHP-77, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.778× | -3.0 | 0.17 | 11/42 (J82, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10782. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 17.9 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +24.6) | — |
| [[KATO III (line)]] | alt | 9.05 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +16.3) | — |
| [[COLO 205 (line)]] | alt | 7.57 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +13.2) | — |
| [[HT-29 (line)]] | alt | 12.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 8.62× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 4.20 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +14.1) | — |
| [[SW1417 (line)]] | alt | 12.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +13.9) | — |
| [[A-172 (line)]] | wt | 3.24 | 0 | 1 | — | [[Thymopentin (drug)]] 5 µM 0.0717× (z -8.6) |
| [[A498 (line)]] | wt | 4.03 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0942× (z -10.3) |
| [[HCT15 (line)]] | alt | 7.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +9.7) | — |
| [[RKO (line)]] | wt | 8.48 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0969× (z -9.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[SW48 (line)]] | wt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +9.0) | — |
| [[SW480 (line)]] | alt | 8.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +9.9) | — |
| [[A-427 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10782), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN16-AS1]] | +0.63 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[RBM26-AS1]] | +0.63 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[HEXIM2-AS1]] | +0.62 | +0.54 / +0.37 | both halves | 9e-05 |  |
| [[THBS4]] | +0.62 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[MFF-DT]] | +0.62 | +0.56 / +0.38 | both halves | 7e-05 |  |
| [[TSTD3]] | +0.62 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[SPTY2D1OS]] | +0.62 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[OXA1L-DT]] | +0.61 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[ZNF253]] | +0.61 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[PPP1R3F]] | +0.60 | +0.54 / +0.33 | both halves | 1e-04 |  |
| [[MAD2L1-DT]] | +0.60 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[PLBD1-AS1]] | +0.60 | +0.53 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM92]] | -0.61 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[SPTLC2]] | -0.57 | -0.58 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[EDA]] | -0.54 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[RASSF7]] | -0.53 | -0.56 / -0.20 | both halves | 7e-04 |  |
| [[CORO2A]] | -0.53 | -0.43 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TMEM80's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF594]] | B | ZNF594 activity lowers TMEM80's level | lines that do not express ZNF594 (6) vs lines expressing it (44) | 1.56× higher at baseline in the lines without ZNF594 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with NF1; also absent: ZNF594-DT, MIR3659HG, SYNGR1 |
| [[ATP2C2]] | B | ATP2C2 activity strengthens TMEM80's drug response | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2 respond 0.52× as strongly (z diff +1.24); strongest at Homoharringtonine 5 µM: 1.12x vs 4.77x (z diff +6.9) | 0.099 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.0, 15.8); signed map (26.8, -12.9). **Vector** length 62.5, 9.04% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.3 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +4.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.5 | +2.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.5 | -5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.0 | -6.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -1.1 | -4.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 80 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:695,591-705,028 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38216 |
| Matched by | ensembl_id |

UniProt [Q96HE8](https://www.uniprot.org/uniprotkb/Q96HE8) carries no function annotation.

**Summary**, from NCBI Gene [283232](https://www.ncbi.nlm.nih.gov/gene/283232):

> Predicted to be involved in non-motile cilium assembly. Predicted to be located in cilium and membrane. Predicted to be active in ciliary transition zone. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27453) · Entrez [283232](https://www.ncbi.nlm.nih.gov/gene/283232) · UniProt [Q96HE8](https://www.uniprot.org/uniprotkb/Q96HE8) · Ensembl [ENSG00000177042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177042)

## Data

Gene col 10782: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10782); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10782, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10782]; `tensor/DDL_lfc|DDL_z.npy` [10782]; `embed/gene_vectors.npy` [10782]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10782 or target_col == 10782). Every well: [[TMEM80 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM80.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
