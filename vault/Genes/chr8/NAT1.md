---
symbol: "NAT1"
type: "gene"
col: 10104
ensembl_id: "ENSG00000171428"
name: "N-acetyltransferase 1"
location: "8p22"
module: 12
arm: "+"
pooled_cpm: 2.74
n_lines_expressing: 47
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NAT1

*N-acetyltransferase 1* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.33× (z +12.9, q 3e-35, up in 34 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.488× (z -7.7, q 9e-12, down in 22 of 42 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNASEL]] (+0.57, fdr 1e-05), [[TRAFD1]] (+0.54, fdr 4e-05), [[NRBF2]] (+0.52, fdr 3e-05); moves opposite to [[PKP4]] (-0.53, fdr 1e-04), [[ADGRA3]] (-0.48, fdr 1e-04), [[CCDC40]] (-0.47, fdr 6e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DAPP1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZRANB3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.33×** | +12.9 | 3e-35 | 34/41 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.11×** | +12.1 | 2e-31 | 31/42 (AsPC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.85×** | +9.3 | 2e-18 | 12/41 (SW480, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.88×** | +6.8 | 2e-09 | 21/41 (SHP-77, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +6.4 | 1e-08 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.0 | 2e-07 | 9/41 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.0 | 2e-07 | 11/32 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +5.2 | 1e-05 | 9/18 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +5.1 | 2e-05 | 9/35 (SW480, RKO, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.0 | 4e-05 | 11/32 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +4.6 | 2e-04 | 9/41 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +4.3 | 7e-04 | 7/33 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 9e-04 | 6/39 (LS 180, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.3 | 9e-04 | 6/23 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.023 | 5/36 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.042 | 3/37 (HEC-1-A, A549, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.083 | 2/27 (A498, RKO) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10104.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.488×** | -7.7 | 9e-12 | 22/42 (SNU-423, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.508×** | -7.3 | 1e-10 | 24/40 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -5.5 | 6e-06 | 13/25 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.599×** | -5.5 | 6e-06 | 15/38 (A-172, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -4.2 | 0.002 | 13/43 (SK-MEL-2, H4, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.736× | -3.2 | 0.13 | 9/17 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.739× | -3.1 | 0.13 | 7/42 (H4, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 4.61 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0684× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 3.90 | 0 | 1 | — | [[Verapamil (drug)]] 5 µM 0.0590× (z -8.9) |
| [[COLO 205 (line)]] | alt | 6.05 | 0 | 1 | — | [[Artemether (drug)]] 0.5 µM 0.0587× (z -9.1) |
| [[LoVo (line)]] | wt | 3.81 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0918× (z -9.9) |
| [[SW480 (line)]] | alt | 5.37 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.801 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.981 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNASEL]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[TRAFD1]] | +0.54 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[NRBF2]] | +0.52 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[CGRRF1]] | +0.52 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[BCAS2]] | +0.51 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[NKIRAS2]] | +0.51 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[DAPP1]] | +0.51 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[SECISBP2L]] | +0.50 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[ZKSCAN4]] | +0.49 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[SAP18]] | +0.49 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[SCNM1]] | +0.48 | +0.32 / +0.41 | both halves | 2e-04 |  |
| [[SNRPB2]] | +0.48 | +0.37 / +0.47 | both halves | 8e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKP4]] | -0.53 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[ADGRA3]] | -0.48 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[CCDC40]] | -0.47 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[NSD2]] | -0.47 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ZRANB3]] | -0.46 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[NUP210]] | -0.45 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[HNRNPAB]] | -0.45 | -0.23 / -0.39 | both halves | 5e-04 |  |
| [[GART]] | -0.45 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[NUDT3]] | -0.45 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[GSPT1]] | -0.44 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[ARHGAP4]] | -0.44 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[CCND1]] | -0.43 | -0.38 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAPP1]] | B | DAPP1 activity raises NAT1's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 1.59× lower at baseline in the lines without DAPP1 | 0.019 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[TOP2A]] | B | TOP2A activity lowers NAT1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FRK]] | B | FRK activity raises NAT1's level | lines that do not express FRK (22) vs lines expressing it (28) | 1.45× lower at baseline in the lines without FRK | 0.073 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZRANB3]] | C | NAT1 activity lowers ZRANB3's level | lines that do not express NAT1 (3) vs lines expressing it (47) | 2.08× higher at baseline in the lines without NAT1 | 0.093 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IKBKE, RASSF5, FUCA2 |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.434). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (25.6, -32.3); signed map (-9.9, -8.6). **Vector** length 36.0, 3.47% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.0 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.4 | +5.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | -0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | -0.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.9 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +4.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -7.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.7 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.5 | -5.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.4 | -3.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.9 | +0.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -0.9 | -1.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -0.8 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.7 | +0.9 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | N-acetyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:18,170,477-18,223,689 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously AAC1 |
| Gene groups (HGNC) | Arylamine N-acetyltransferases |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 4 pathways, smallest: Paracetamol ADME; Phase II - Conjugation of compounds; Drug ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P18440](https://www.uniprot.org/uniprotkb/P18440) (Arylamine N-acetyltransferase 1):

> Xenobiotic-metabolizing enzyme that catalyzes both N-acetylation (usually detoxification) and O-acetylation (usually bioactivation) of a wide range of species-specific substrates including hydrazines, aromatic amine drugs and aromatic amine carcinogens (Probable). Transfers an acetyl group from acetyl-coenzyme A to arylamine and N-hydroxyarylamine acceptor substrates (Probable). Can also transfer an N-acetyl group from an N-hydroxy acetylamine to either N-hydroxyarylamine or arylamine in the …

**Summary**, from NCBI Gene [9](https://www.ncbi.nlm.nih.gov/gene/9):

> This gene is one of two arylamine N-acetyltransferase (NAT) genes in the human genome, and is orthologous to the mouse and rat Nat2 genes. The enzyme encoded by this gene catalyzes the transfer of an acetyl group from acetyl-CoA to various arylamine and hydrazine substrates. This enzyme helps metabolize drugs and other xenobiotics, and functions in folate catabolism. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:7645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7645) · Entrez [9](https://www.ncbi.nlm.nih.gov/gene/9) · UniProt [P18440](https://www.uniprot.org/uniprotkb/P18440) · Ensembl [ENSG00000171428](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171428)

## Data

Gene col 10104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10104); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10104]; `tensor/DDL_lfc|DDL_z.npy` [10104]; `embed/gene_vectors.npy` [10104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10104 or target_col == 10104). Every well: [[NAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
