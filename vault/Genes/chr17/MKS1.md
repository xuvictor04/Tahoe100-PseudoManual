---
symbol: "MKS1"
type: "gene"
col: 226
ensembl_id: "ENSG00000011143"
name: "MKS transition zone complex subunit 1"
location: "17q22"
module: 28
arm: "+"
pooled_cpm: 5.61
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# MKS1

*MKS transition zone complex subunit 1* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.46× (z +7.6, q 2e-11, up in 18 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.576× (z -10.9, q 4e-25, down in 33 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC113]] (+0.71, fdr 7e-06), [[RNF214]] (+0.71, fdr 7e-06), [[MDM1]] (+0.69, fdr 7e-06); moves opposite to [[TXN]] (-0.62, fdr 1e-05), [[FBXW7]] (-0.56, fdr 2e-05), [[UBE2F-SCLY]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLHL29]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +7.6 | 2e-11 | 18/40 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +5.2 | 4e-05 | 13/34 (NCI-H23, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.0 | 1e-04 | 8/31 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 1e-04 | 12/45 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +4.7 | 3e-04 | 12/44 (KATO III, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 0.001 | 12/39 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +4.1 | 0.003 | 10/44 (HOP62, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.1 | 0.004 | 6/39 (A-427, H4, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.7 | 0.016 | 4/9 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.20× | +3.6 | 0.018 | 7/46 (CFPAC-1, RKO, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.071 | 3/45 (KATO III, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 226.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.576×** | -10.9 | 4e-25 | 33/40 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.528×** | -9.0 | 8e-17 | 27/45 (LS 180, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.560×** | -8.1 | 8e-14 | 22/44 (HEC-1-A, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.579×** | -7.7 | 2e-12 | 22/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.681×** | -7.6 | 3e-12 | 25/45 (MIA PaCa-2, J82, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.633×** | -6.4 | 1e-08 | 20/46 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -6.0 | 2e-07 | 21/41 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.449×** | -5.9 | 3e-07 | 18/43 (A549, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.663×** | -5.8 | 5e-07 | 18/45 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.695×** | -5.1 | 2e-05 | 14/46 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.520×** | -4.8 | 8e-05 | 21/40 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -4.7 | 1e-04 | 14/39 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.749×** | -4.1 | 0.002 | 19/44 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -3.7 | 0.008 | 17/37 (Panc 03.27, SNU-423, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.610×** | -3.6 | 0.011 | 5/37 (RKO, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.850× | -3.2 | 0.044 | 5/46 (HS-578T, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.664×** | -3.0 | 0.085 | 9/44 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.54 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 7.03 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.151× (z -9.5) ⚠ transcription drop |
| [[HOP62 (line)]] | alt | 8.39 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -10.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 5.03 | 0 | 1 | — | [[Monocrotaline (drug)]] 5 µM 0.0581× (z -10.8) |
| [[HT-29 (line)]] | alt | 3.49 | 0 | 1 | — | [[Rifaximin (drug)]] 0.05 µM 0.0618× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 5.71 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0623× (z -8.6) ⚠ cell-cycle shift, explains ~20% of this change |
| [[MIA PaCa-2 (line)]] | alt | 5.23 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 5.17 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 5.92 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0533× (z -10.9) |
| [[SNU-423 (line)]] | alt | 5.65 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0770× (z -9.7) |
| [[A-172 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC113]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[RNF214]] | +0.71 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[MDM1]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[COPS5]] | +0.69 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.69 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[SEPSECS]] | +0.68 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[NUDT12]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ABITRAM]] | +0.67 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[TTC8]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium; STRING 814 |
| [[GEMIN2]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SMARCE1]] | +0.65 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[DBT]] | +0.65 | +0.65 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXN]] | -0.62 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[FBXW7]] | -0.56 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[UBE2F-SCLY]] | -0.55 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PRDX1]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ADGRE3]] | -0.54 | -0.38 / -0.51 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL29]] | B | KLHL29 activity raises MKS1's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without KLHL29 | 0.091 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.733). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.1, 2.3); signed map (-20.5, -16.6). **Vector** length 64.7, 9.41% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.2 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.3 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MKS transition zone complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:58,205,441-58,219,605 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20345, POC12, BBS13; previously MKS |
| Gene groups (HGNC) | B9 domain containing; MKS complex |
| Reactome | 6 pathways, smallest: Hedgehog 'off' state; Anchoring of the basal body to the plasma membrane; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXB0](https://www.uniprot.org/uniprotkb/Q9NXB0) (Tectonic-like complex member MKS1):

> Component of the tectonic-like complex, a complex localized at the transition zone of primary cilia and acting as a barrier that prevents diffusion of transmembrane proteins between the cilia and plasma membranes. Involved in centrosome migration to the apical cell surface during early ciliogenesis. Required for ciliary structure and function, including a role in regulating length and appropriate number through modulating centrosome duplication. Required for cell branching morphology.

**Summary**, from NCBI Gene [54903](https://www.ncbi.nlm.nih.gov/gene/54903):

> The protein encoded by this gene localizes to the basal body and is required for formation of the primary cilium in ciliated epithelial cells. Mutations in this gene result in Meckel syndrome type 1 and in Bardet-Biedl syndrome type 13. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:7121](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7121) · Entrez [54903](https://www.ncbi.nlm.nih.gov/gene/54903) · UniProt [Q9NXB0](https://www.uniprot.org/uniprotkb/Q9NXB0) · Ensembl [ENSG00000011143](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011143)

## Data

Gene col 226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 226); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 226]; `tensor/DDL_lfc|DDL_z.npy` [226]; `embed/gene_vectors.npy` [226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 226 or target_col == 226). Every well: [[MKS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MKS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
