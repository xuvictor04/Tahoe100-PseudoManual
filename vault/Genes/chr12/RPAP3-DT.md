---
symbol: "RPAP3-DT"
type: "gene"
col: 15040
ensembl_id: "ENSG00000257433"
name: "RPAP3 divergent transcript"
location: "12q13.11"
module: 35
arm: "+"
pooled_cpm: 2.33
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# RPAP3-DT

*RPAP3 divergent transcript* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.74× (z +9.8, q 4e-20, up in 9 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.68× (z +9.6, q 2e-19, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.477× (z -7.3, q 2e-10, down in 21 of 45 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRP14-DT]] (+0.58, fdr 7e-06), [[RTCA-AS1]] (+0.55, fdr 1e-05), [[ZNF236-DT]] (+0.54, fdr 2e-05); moves opposite to [[SERBP1]] (-0.48, fdr 4e-04), [[SMARCA4]] (-0.47, fdr 1e-04), [[CEP83]] (-0.45, fdr 9e-04, ⚠ not reproduced), [[NLN]] (-0.45, fdr 9e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +9.8 | 4e-20 | 9/11 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.68×** | +9.6 | 2e-19 | 32/44 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.47×** | +8.8 | 2e-16 | 29/42 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +8.0 | 2e-13 | 1/2 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +7.3 | 4e-11 | 14/32 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.96×** | +6.6 | 5e-09 | 17/41 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +6.5 | 6e-09 | 7/12 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +6.5 | 6e-09 | 15/37 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +6.3 | 2e-08 | 1/3 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +6.0 | 1e-07 | 8/26 (SW480, C-33 A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.84×** | +5.9 | 2e-07 | 17/43 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.39×** | +4.6 | 2e-04 | 4/43 (NCI-H2347, SNU-1, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +4.5 | 4e-04 | 7/43 (A498, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.36×** | +4.2 | 9e-04 | 6/42 (SW 900, BT-474, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.42×** | +4.1 | 0.002 | 3/41 (SW480, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.003 | 4/44 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.018 | 5/43 (SW480, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.018 | 6/40 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.46×** | +3.4 | 0.018 | 1/19 (CFPAC-1) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.042 | 3/43 (SNU-423, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.477×** | -7.3 | 2e-10 | 21/45 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.524×** | -6.3 | 6e-08 | 20/40 (A-427, A549, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.599×** | -5.0 | 9e-05 | 14/44 (Hs 766T, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.607×** | -4.9 | 1e-04 | 10/38 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.488×** | -3.7 | 0.023 | 10/26 (PANC-1, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.489×** | -3.7 | 0.023 | 8/38 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.695×** | -3.6 | 0.028 | 10/44 (COLO 205, SW48, …) | inconsistent across doses |  |
| [[Fumaric acid (drug)]] 5 µM |  | **0.700×** | -3.4 | 0.052 | 3/43 (HOP62, LoVo, …) | top dose only | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.801× | -3.1 | 0.11 | 10/42 (MIA PaCa-2, SW 900, …) | top dose only |  |
| [[Asciminib (drug)]] 0.5 µM |  | 0.731× | -3.1 | 0.11 | 5/43 (C-33 A, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 2.99 | 0 | 1 | — | [[Bendamustine (drug)]] 0.05 µM 0.0744× (z -8.7) |
| [[LoVo (line)]] | wt | 2.27 | 0 | 1 | — | [[Darolutamide (drug)]] 0.5 µM 0.0766× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 2.61 | 0 | 1 | — | [[Busulfan (drug)]] 0.05 µM 0.0615× (z -8.7) |
| [[A-172 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.906 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP14-DT]] | +0.58 | +0.59 / +0.58 | both halves | 7e-06 | same gene group |
| [[RTCA-AS1]] | +0.55 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ZNF236-DT]] | +0.54 | +0.49 / +0.52 | both halves | 2e-05 | same gene group |
| [[RAB21]] | +0.53 | +0.55 / +0.36 | both halves | 9e-05 |  |
| [[SLC16A13]] | +0.53 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[HSPE1-MOB4]] | +0.52 | +0.28 / +0.58 | both halves | 3e-04 |  |
| [[C8orf44-SGK3]] | +0.52 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[ABCC11]] | +0.52 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ARMH1]] | +0.51 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[LINC01273]] | +0.50 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[DMXL1-DT]] | +0.50 | +0.44 / +0.63 | both halves | 3e-05 | same gene group |
| [[MYL6B-AS1]] | +0.50 | +0.43 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERBP1]] | -0.48 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[SMARCA4]] | -0.47 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[CEP83]] | -0.45 | -0.18 / -0.36 | ⚠ not reproduced | 9e-04 |  |
| [[NLN]] | -0.45 | -0.43 / -0.37 | both halves | 9e-05 |  |
| [[DCBLD1]] | -0.44 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[ADARB1]] | -0.44 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[UBAP2]] | -0.43 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[EHBP1]] | -0.43 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[PFN1]] | -0.43 | -0.25 / -0.35 | both halves | 4e-04 |  |
| [[MAP7D3]] | -0.42 | -0.28 / -0.19 | ⚠ not reproduced | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RPAP3-DT's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EHBP1]] | C | EHBP1's natural level strengthens RPAP3-DT's drug response | EHBP1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.66, reverse -0.05; direction not clear | 0.059 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.424). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.8, 26.5); signed map (34.5, -2.6). **Vector** length 36.0, 3.43% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +4.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.3 | -7.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | +0.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | RPAP3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q13.11 — chr12:47,706,058-47,742,294 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55477) · Entrez [105369748](https://www.ncbi.nlm.nih.gov/gene/105369748) · Ensembl [ENSG00000257433](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257433)

## Data

Gene col 15040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15040); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15040]; `tensor/DDL_lfc|DDL_z.npy` [15040]; `embed/gene_vectors.npy` [15040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15040 or target_col == 15040). Every well: [[RPAP3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPAP3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
