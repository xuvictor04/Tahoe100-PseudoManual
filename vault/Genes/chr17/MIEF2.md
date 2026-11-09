---
symbol: "MIEF2"
type: "gene"
col: 10822
ensembl_id: "ENSG00000177427"
name: "mitochondrial elongation factor 2"
location: "17p11.2"
module: 2
arm: "+"
pooled_cpm: 3.55
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MIEF2

*mitochondrial elongation factor 2* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +4.8, q 1e-03, up in 9 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.408× (z -9.8, q 4e-20, down in 31 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.405× (z -9.6, q 3e-19, down in 22 of 39 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TP53I13]] (+0.53, fdr 2e-05), [[CENPT]] (+0.51, fdr 3e-05), [[CNPPD1]] (+0.51, fdr 6e-05); moves opposite to [[FNDC3A]] (-0.49, fdr 2e-04), [[EREG]] (-0.49, fdr 1e-04), [[MTHFD2L]] (-0.49, fdr 7e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLEKHG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10822.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.8 | 1e-03 | 9/36 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.006 | 7/43 (A-172, A-427, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.006 | 8/40 (RPMI-7951, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.28×** | +3.9 | 0.016 | 7/45 (SW480, LoVo, …) | top dose only | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.020 | 4/46 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.031 | 6/33 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.57×** | +3.6 | 0.031 | 3/25 (NCI-H460, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.045 | 8/43 (RKO, AsPC-1, …) | two highest doses | position effect removed |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 1.22× | +3.1 | 0.11 | 6/44 (A549, A-172, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10822.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.408×** | -9.8 | 4e-20 | 31/46 (MIA PaCa-2, RKO, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.405×** | -9.6 | 3e-19 | 22/39 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.813×** | -7.8 | 2e-12 | 28/48 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.624×** | -7.3 | 4e-11 | 21/35 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.535×** | -6.6 | 4e-09 | 17/27 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.373×** | -5.7 | 1e-06 | 20/37 (CFPAC-1, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.648×** | -4.5 | 5e-04 | 12/40 (NCI-H23, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.665×** | -4.5 | 5e-04 | 16/36 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.482×** | -4.2 | 0.002 | 13/39 (PANC-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.615×** | -3.8 | 0.008 | 8/46 (SW 900, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.523×** | -3.7 | 0.010 | 13/32 (LoVo, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **0.723×** | -3.6 | 0.018 | 14/21 (LOX-IMVI, SNU-423, …) | inconsistent across doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.559×** | -3.3 | 0.036 | 7/33 (HCT15, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.740×** | -3.3 | 0.039 | 15/43 (SW480, J82, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.752×** | -3.1 | 0.068 | 14/45 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.744×** | -3.1 | 0.076 | 16/42 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.595×** | -3.0 | 0.096 | 10/33 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10822. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 4.45 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0730× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SNU-423 (line)]] | alt | 4.45 | 0 | 2 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0856× (z -8.6) |
| [[A-172 (line)]] | wt | 5.51 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0933× (z -10.5) |
| [[A498 (line)]] | wt | 3.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -9.4) |
| [[J82 (line)]] | alt | 3.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 4.71 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0738× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 2.56 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.116× (z -8.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10822), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TP53I13]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[CENPT]] | +0.51 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[CNPPD1]] | +0.51 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[ATG9A]] | +0.50 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[RAB5B]] | +0.49 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[BSDC1]] | +0.48 | +0.32 / +0.54 | both halves | 2e-04 |  |
| [[PPOX]] | +0.48 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[RETREG2]] | +0.48 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[PINK1]] | +0.47 | +0.38 / +0.50 | both halves | 6e-05 | STRING 586 |
| [[ANKZF1]] | +0.47 | +0.34 / +0.50 | both halves | 1e-04 |  |
| [[SERINC1]] | +0.47 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[MYL6]] | +0.47 | +0.38 / +0.52 | both halves | 6e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNDC3A]] | -0.49 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[EREG]] | -0.49 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[MTHFD2L]] | -0.49 | -0.37 / -0.56 | both halves | 7e-05 |  |
| [[EIF4G3]] | -0.46 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[PPA2]] | -0.45 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[HSD17B2-AS1]] | -0.43 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[EBI3]] | -0.43 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[GPHN]] | -0.42 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[ECHDC1]] | -0.41 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[TANK]] | -0.41 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[POGLUT1]] | -0.40 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[NEDD4]] | -0.40 | -0.31 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG2]] | B | PLEKHG2 activity raises MIEF2's level | lines that do not express PLEKHG2 (10) vs lines expressing it (40) | 1.05× lower at baseline in the lines without PLEKHG2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000225689; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.255). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (3.4, -37.4); signed map (-22.8, 8.5). **Vector** length 54.3, 7.30% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +1.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.0 | +2.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +1.9 | +1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.6 | +1.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.5 | -9.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -4.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial elongation factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:18,260,597-18,266,552 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC23130, MiD49, D3B; previously SMCR7 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C03](https://www.uniprot.org/uniprotkb/Q96C03) (Mitochondrial dynamics protein MID49):

> Mitochondrial outer membrane protein involved in the regulation of mitochondrial organization. It is required for mitochondrial fission and promotes the recruitment and association of the fission mediator dynamin-related protein 1 (DNM1L) to the mitochondrial surface independently of the mitochondrial fission FIS1 and MFF proteins. Regulates DNM1L GTPase activity.

**Summary**, from NCBI Gene [125170](https://www.ncbi.nlm.nih.gov/gene/125170):

> This gene encodes an outer mitochondrial membrane protein that functions in the regulation of mitochondrial morphology. It can directly recruit the fission mediator dynamin-related protein 1 (Drp1) to the mitochondrial surface. The gene is located within the Smith-Magenis syndrome region on chromosome 17. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:17920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17920) · Entrez [125170](https://www.ncbi.nlm.nih.gov/gene/125170) · UniProt [Q96C03](https://www.uniprot.org/uniprotkb/Q96C03) · Ensembl [ENSG00000177427](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177427)

## Data

Gene col 10822: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10822); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10822, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10822]; `tensor/DDL_lfc|DDL_z.npy` [10822]; `embed/gene_vectors.npy` [10822]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10822 or target_col == 10822). Every well: [[MIEF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIEF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
