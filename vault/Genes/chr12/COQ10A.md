---
symbol: "COQ10A"
type: "gene"
col: 5710
ensembl_id: "ENSG00000135469"
name: "coenzyme Q10A"
location: "12q13.3"
module: 59
arm: "+"
pooled_cpm: 4.18
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# COQ10A

*coenzyme Q10A* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.02× (z +12.4, q 1e-32, up in 26 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.418× (z -5.4, q 4e-05, down in 17 of 40 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRA2A]] (+0.54, fdr 3e-05), [[CNNM4]] (+0.51, fdr 9e-05), [[SDR39U1]] (+0.51, fdr 4e-05); moves opposite to [[LARP4B]] (-0.50, fdr 4e-05), [[VTI1A]] (-0.48, fdr 3e-05), [[SEC14L1]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5710.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.02×** | +12.4 | 1e-32 | 26/44 (SW480, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +9.2 | 1e-17 | 24/45 (SW480, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +7.2 | 1e-10 | 10/23 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +6.9 | 6e-10 | 22/46 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +6.5 | 1e-08 | 16/45 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +6.2 | 6e-08 | 4/8 (HOP62, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +5.9 | 3e-07 | 14/44 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +5.9 | 3e-07 | 1/11 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.8 | 5e-07 | 14/33 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.6 | 1e-06 | 10/40 (HT-29, J82, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.4 | 4e-06 | 13/36 (Panc 03.27, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.53×** | +5.3 | 7e-06 | 7/20 (HEC-1-A, J82, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +5.1 | 2e-05 | 14/39 (Panc 03.27, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +4.7 | 1e-04 | 12/38 (J82, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +4.6 | 2e-04 | 2/21 (HEC-1-A, J82) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 6e-04 | 12/39 (Panc 03.27, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +4.2 | 9e-04 | 2/30 (SW480, SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.2 | 9e-04 | 9/45 (SW480, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.44×** | +4.1 | 0.001 | 8/30 (J82, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.010 | 2/25 (LoVo, SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5710.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -5.4 | 4e-05 | 17/40 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.656×** | -5.3 | 4e-05 | 19/43 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.442×** | -5.0 | 1e-04 | 14/34 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.696×** | -4.5 | 8e-04 | 16/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.751×** | -3.6 | 0.036 | 15/34 (Panc 03.27, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.771× | -3.3 | 0.10 | 11/43 (H4, SNU-423, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.782× | -3.1 | 0.17 | 13/41 (NCI-H1573, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5710. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 4.03 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.123× (z -8.6) |
| [[HOP62 (line)]] | alt | 2.72 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0790× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 7.34 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0955× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 5.72 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0565× (z -11.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5710), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRA2A]] | +0.54 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[CNNM4]] | +0.51 | +0.37 / +0.65 | both halves | 9e-05 |  |
| [[SDR39U1]] | +0.51 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[ENY2]] | +0.50 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[CHCHD7]] | +0.49 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[IMPA1]] | +0.49 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[MYLIP]] | +0.49 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[AMACR]] | +0.49 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[NAT14]] | +0.49 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[COMMD3]] | +0.48 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[TXNDC16]] | +0.48 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[RETSAT]] | +0.48 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP4B]] | -0.50 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[VTI1A]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SEC14L1]] | -0.47 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[YWHAB]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[FBXO36]] | -0.46 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[NDUFA10]] | -0.45 | -0.35 / -0.48 | both halves | 1e-04 | pathway: Aerobic respiration and respiratory electron transport |
| [[BCAP31]] | -0.45 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[VPS53]] | -0.45 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[DPP9]] | -0.44 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[DNAH1]] | -0.44 | -0.12 / -0.59 | ⚠ one half (not replicated) | 0.002 |  |
| [[EIF3I]] | -0.44 | -0.20 / -0.46 | both halves | 7e-04 |  |
| [[ZNF731P]] | -0.44 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TIMM23B-AGAP6]] | -0.43 | -0.22 / -0.46 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers COQ10A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NEURL3]] | B | NEURL3 activity lowers COQ10A's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 1.33× higher at baseline in the lines without NEURL3 | 0.038 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.4, 18.0); signed map (-8.8, 9.1). **Vector** length 49.1, 6.06% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.7 | +12.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.7 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +7.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.2 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +4.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +4.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +3.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.7 | -5.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.4 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -2.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -5.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.0 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | coenzyme Q10A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,266,890-56,270,966 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32452 |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MF6](https://www.uniprot.org/uniprotkb/Q96MF6) (Coenzyme Q-binding protein COQ10 homolog A, mitochondrial):

> Required for the function of coenzyme Q in the respiratory chain. May serve as a chaperone or may be involved in the transport of Q6 from its site of synthesis to the catalytic sites of the respiratory complexes (Probable).

**Summary**, from NCBI Gene [93058](https://www.ncbi.nlm.nih.gov/gene/93058):

> Predicted to enable ubiquinone binding activity. Predicted to be involved in cellular respiration. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26515) · Entrez [93058](https://www.ncbi.nlm.nih.gov/gene/93058) · UniProt [Q96MF6](https://www.uniprot.org/uniprotkb/Q96MF6) · Ensembl [ENSG00000135469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135469)

## Data

Gene col 5710: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5710); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5710, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5710]; `tensor/DDL_lfc|DDL_z.npy` [5710]; `embed/gene_vectors.npy` [5710]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5710 or target_col == 5710). Every well: [[COQ10A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COQ10A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
