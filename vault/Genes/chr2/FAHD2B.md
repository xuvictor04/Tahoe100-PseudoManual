---
symbol: "FAHD2B"
type: "gene"
col: 6852
ensembl_id: "ENSG00000144199"
name: "fumarylacetoacetate hydrolase domain containing 2B"
location: "2q11.2"
module: 12
arm: "+"
pooled_cpm: 4.95
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# FAHD2B

*fumarylacetoacetate hydrolase domain containing 2B* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.78× (z +6.3, q 1e-07, up in 20 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.264× (z -7.2, q 3e-10, down in 24 of 33 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDPF1]] (+0.65, fdr 1e-05), [[AARS2]] (+0.59, fdr 2e-05), [[POLR2I]] (+0.59, fdr 8e-04, ⚠ one half only (not replicated)), [[POLM]] (+0.59, fdr 1e-04); moves opposite to [[HCG17]] (-0.57, fdr 2e-04), [[FAM81A]] (-0.54, fdr 2e-04), [[SAXO1]] (-0.52, fdr 9e-04, ⚠ not reproduced), [[LAMTOR5-AS1]] (-0.51, fdr 4e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NSUN5]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6852.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +6.3 | 1e-07 | 20/45 (SW 900, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +6.2 | 1e-07 | 5/9 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +5.8 | 1e-06 | 19/44 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.3 | 2e-05 | 11/25 (SW1417, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.07×** | +4.2 | 0.004 | 5/24 (NCI-H460, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +4.0 | 0.006 | 9/25 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.38×** | +3.6 | 0.029 | 6/20 (SW480, A498, …) | rises with dose | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.029 | 7/40 (HOP62, A-427, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.029 | 9/44 (HOP62, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.037 | 2/42 (LS 180, COLO 205) | top dose only | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.3 | 0.050 | 0/11 | rises with dose | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.2 | 0.063 | 6/35 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.34×** | +3.2 | 0.063 | 11/43 (NCI-H23, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.2 | 0.065 | 7/32 (NCI-H2030, NCI-H23, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6852.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.264×** | -7.2 | 3e-10 | 24/33 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.547×** | -6.6 | 1e-08 | 20/44 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.638×** | -4.9 | 2e-04 | 16/45 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -4.8 | 2e-04 | 13/34 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.644×** | -4.8 | 2e-04 | 16/41 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.635×** | -4.7 | 3e-04 | 17/43 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.493×** | -3.8 | 0.011 | 13/42 (NCI-H1792, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.728×** | -3.5 | 0.037 | 10/35 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.806×** | -3.3 | 0.052 | 20/38 (SHP-77, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.738×** | -3.3 | 0.052 | 9/45 (BT-474, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | **0.732×** | -3.3 | 0.054 | 8/44 (LoVo, A-172, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.754×** | -3.1 | 0.098 | 11/43 (HT-29, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6852. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 7.81 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0581× (z -12.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 6.93 | 0 | 1 | — | [[Zileuton (drug)]] 0.5 µM 0.0592× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 3.88 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0620× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 6.20 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.3) ⚠ cell-cycle shift, explains ~5% of this change |
| [[A-172 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6852), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 10 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDPF1]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[AARS2]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[POLR2I]] | +0.59 | +0.20 / +0.63 | ⚠ one half (not replicated) | 8e-04 |  |
| [[POLM]] | +0.59 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[PET117]] | +0.58 | +0.31 / +0.64 | both halves | 2e-04 |  |
| [[ISCA2]] | +0.56 | +0.21 / +0.59 | both halves | 6e-04 |  |
| [[GRHPR]] | +0.56 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[WRAP73]] | +0.56 | +0.30 / +0.59 | both halves | 2e-04 |  |
| [[FAM241B]] | +0.56 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[HPF1]] | +0.55 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[AGTRAP]] | +0.55 | +0.53 / +0.49 | both halves | 2e-05 |  |
| [[C18orf21]] | +0.54 | +0.24 / +0.65 | both halves | 4e-04 |  |
| [[LSM10]] | +0.54 | +0.34 / +0.64 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCG17]] | -0.57 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[FAM81A]] | -0.54 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[SAXO1]] | -0.52 | -0.18 / -0.41 | ⚠ not reproduced | 9e-04 |  |
| [[LAMTOR5-AS1]] | -0.51 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[C2orf88]] | -0.50 | -0.18 / -0.32 | ⚠ not reproduced | 1e-03 |  |
| [[LINC01208]] | -0.50 | -0.17 / -0.39 | ⚠ not reproduced | 0.001 |  |
| [[PSMD7-DT]] | -0.50 | -0.15 / -0.37 | ⚠ not reproduced | 0.001 |  |
| [[CASC11]] | -0.49 | -0.32 / -0.22 | both halves | 6e-04 |  |
| [[PPP1R15B-AS1]] | -0.48 | -0.18 / -0.39 | ⚠ not reproduced | 9e-04 |  |
| [[PCBP1-AS1]] | -0.48 | -0.10 / -0.52 | ⚠ one half (not replicated) | 0.003 |  |
| [[NUP210L]] | -0.47 | -0.20 / -0.42 | ⚠ not reproduced | 8e-04 |  |
| [[ALOX12-AS1]] | -0.47 | -0.20 / -0.38 | both halves | 7e-04 |  |
| [[FAM184B]] | -0.47 | -0.22 / -0.29 | both halves | 6e-04 |  |
| [[RRH]] | -0.47 | -0.32 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NSUN5]] | C | NSUN5 activity raises FAHD2B's level | lines that do not express NSUN5 (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without NSUN5 | 0.099 | ⚠ few lines (3 vs 47); across organs; also absent: PDCD6P1, PTPN3, FOXRED2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.481). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-44.1, -6.7); signed map (-19.1, -8.0). **Vector** length 42.8, 5.03% of its response variance represented; |z| ≥ 3 in 743 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.7 | +4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.5 | +5.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.4 | +6.3 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +1.2 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +4.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.0 | +0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.9 | +3.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.9 | +2.2 |
|  | [[NVP-BHG712 (drug)]] 0.5 µM |  | +0.9 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -7.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -4.7 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | fumarylacetoacetate hydrolase domain containing 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:97,083,583-97,094,882 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434N062 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P2I3](https://www.uniprot.org/uniprotkb/Q6P2I3) (Oxaloacetate tautomerase FAHD2B, mitochondrial):

> Tautomerase that converts enol-oxaloacetate, a strong inhibitor of succinate dehydrogenase, to the physiological keto form of oxaloacetate. It is thereby required to maximize aerobic respiration efficiency by preventing succinate dehydrogenase inhibition.

**Summary**, from NCBI Gene [151313](https://www.ncbi.nlm.nih.gov/gene/151313):

> Enables oxaloacetate tautomerase activity. Involved in oxaloacetate metabolic process. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25318](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25318) · Entrez [151313](https://www.ncbi.nlm.nih.gov/gene/151313) · UniProt [Q6P2I3](https://www.uniprot.org/uniprotkb/Q6P2I3) · Ensembl [ENSG00000144199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144199)

## Data

Gene col 6852: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6852); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6852, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6852]; `tensor/DDL_lfc|DDL_z.npy` [6852]; `embed/gene_vectors.npy` [6852]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6852 or target_col == 6852). Every well: [[FAHD2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAHD2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
