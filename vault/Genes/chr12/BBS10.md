---
symbol: "BBS10"
type: "gene"
col: 11067
ensembl_id: "ENSG00000179941"
name: "Bardet-Biedl syndrome 10"
location: "12q21.2"
module: 16
arm: "+"
pooled_cpm: 5.34
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# BBS10

*Bardet-Biedl syndrome 10* — 12q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.85× (z +6.0, q 1e-06, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.492× (z -7.0, q 2e-09, down in 23 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.536× (z -6.1, q 3e-07, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VEZF1]] (+0.73, fdr 7e-06), [[C7orf25]] (+0.71, fdr 7e-06), [[CSTF2T]] (+0.70, fdr 7e-06); moves opposite to [[SDHAP2]] (-0.66, fdr 7e-06), [[EFCAB14-AS1]] (-0.64, fdr 4e-05), [[SDHAP4-1]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF221]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11067.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +6.0 | 1e-06 | 24/45 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +5.4 | 2e-05 | 19/46 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.73×** | +5.3 | 2e-05 | 16/45 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.1 | 4e-05 | 23/46 (A498, Hs 766T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +5.1 | 5e-05 | 14/46 (NCI-H460, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +4.7 | 2e-04 | 16/44 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +4.7 | 2e-04 | 12/46 (A549, J82, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +4.4 | 7e-04 | 16/38 (A549, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +4.3 | 0.001 | 16/46 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.002 | 14/42 (A498, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +4.0 | 0.004 | 4/14 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.023 | 4/46 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.030 | 12/43 (A-172, C-33 A, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.045 | 12/43 (HEC-1-A, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.2 | 0.047 | 2/8 (HOP62, HS-578T) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.087 | 9/42 (HOP62, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11067.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.492×** | -7.0 | 2e-09 | 23/38 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.536×** | -6.1 | 3e-07 | 23/45 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.638×** | -4.4 | 0.002 | 18/44 (HepG2/C3A, PANC-1, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.646×** | -4.1 | 0.007 | 18/42 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.681×** | -3.8 | 0.018 | 19/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.590×** | -3.7 | 0.019 | 13/44 (A-427, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.688×** | -3.7 | 0.019 | 19/45 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.702×** | -3.5 | 0.034 | 17/45 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.636×** | -3.2 | 0.094 | 13/43 (A498, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.730× | -3.1 | 0.11 | 15/45 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 6.69 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.100× (z -9.5) |
| [[HT-29 (line)]] | alt | 3.76 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0584× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 7.53 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0602× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 2.23 | 0 | 1 | — | [[Sildenafil (drug)]] 0.05 µM 0.0607× (z -8.8) |
| [[PANC-1 (line)]] | alt | 6.89 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.128× (z -10.9) |
| [[A-172 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[C7orf25]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.70 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[TMEM185B]] | +0.70 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[PABIR1]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ZNF816]] | +0.69 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.67 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[SLC35A4]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[RTL6]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[ZNF518B]] | +0.67 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[LIG4]] | +0.66 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[ZKSCAN2]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP2]] | -0.66 | -0.71 / -0.68 | both halves | 7e-06 |  |
| [[EFCAB14-AS1]] | -0.64 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[SDHAP4-1]] | -0.63 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[MZT2A]] | -0.63 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[SNHG25]] | -0.62 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[GNRH1]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[APTR]] | -0.62 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[FAM217A]] | -0.62 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[RAB6A]] | -0.62 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[NENF]] | -0.61 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[SMG1P5]] | -0.61 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[CCDC65]] | -0.61 | -0.31 / -0.68 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF221]] | B | ZNF221 activity raises BBS10's level | lines that do not express ZNF221 (5) vs lines expressing it (45) | 1.95× lower at baseline in the lines without ZNF221 | 0.064 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF540, ZNF529-AS1, AGK |
| [[PSMB5]] | B | PSMB5 activity raises BBS10's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.737). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.7, 13.9); signed map (0.9, -30.4). **Vector** length 63.7, 9.57% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +5.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +5.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.9 | -4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.0 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -4.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | Bardet-Biedl syndrome 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.2 — chr12:76,344,474-76,348,415 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23560; previously C12orf58 |
| Gene groups (HGNC) | Chaperonins |
| Reactome | 5 pathways, smallest: BBSome-mediated cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAM1](https://www.uniprot.org/uniprotkb/Q8TAM1) (BBSome complex assembly protein BBS10):

> Probable molecular chaperone that assists the folding of proteins upon ATP hydrolysis. Plays a role in the assembly of BBSome, a complex involved in ciliogenesis regulating transports vesicles to the cilia. Involved in adipogenic differentiation.

**Summary**, from NCBI Gene [79738](https://www.ncbi.nlm.nih.gov/gene/79738):

> This gene is a member of the Bardet-Biedl syndrome (BBS) gene family. Bardet-Biedl syndrome is an autosomal recessive disorder characterized by progressive retinal degeneration, obesity, polydactyly, renal malformation and cognitive disability. The proteins encoded by BBS gene family members are structurally diverse and the similar phenotypes exhibited by mutations in BBS gene family members is likely due to their shared roles in cilia formation and function. Many BBS proteins localize to the …

**Accessions** — [HGNC:26291](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26291) · Entrez [79738](https://www.ncbi.nlm.nih.gov/gene/79738) · UniProt [Q8TAM1](https://www.uniprot.org/uniprotkb/Q8TAM1) · Ensembl [ENSG00000179941](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179941)

## Data

Gene col 11067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11067); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11067]; `tensor/DDL_lfc|DDL_z.npy` [11067]; `embed/gene_vectors.npy` [11067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11067 or target_col == 11067). Every well: [[BBS10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BBS10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
