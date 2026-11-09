---
symbol: "SPIN4"
type: "gene"
col: 11851
ensembl_id: "ENSG00000186767"
name: "spindlin family member 4"
location: "Xq11.1"
module: 6
arm: "+"
pooled_cpm: 10.03
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# SPIN4

*spindlin family member 4* — Xq11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.71× (z +6.4, q 7e-08, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.558× (z -6.6, q 2e-08, down in 23 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[E2F8]] (+0.71, fdr 7e-06), [[ESCO2]] (+0.68, fdr 7e-06), [[ZWINT]] (+0.64, fdr 7e-06); moves opposite to [[ALDH2]] (-0.56, fdr 1e-05), [[NSA2]] (-0.56, fdr 1e-05), [[KIZ-AS1]] (-0.55, fdr 2e-05, ⚠ KIZ-AS1 in the vector space only through flagged drug-doses), [[RHOQ-AS1]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11851.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.71×** | +6.4 | 7e-08 | 21/47 (PANC-1, J82, …) | two highest doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +5.7 | 3e-06 | 11/48 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.25×** | +3.7 | 0.030 | 6/48 (HT-29, SNU-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.38×** | +3.7 | 0.030 | 14/34 (SW480, HCT15, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.31× | +3.2 | 0.13 | 7/46 (AsPC-1, SNU-423, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | 1.30× | +3.2 | 0.13 | 11/36 (SW1417, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 1.31× | +3.1 | 0.14 | 5/17 (SW1417, LS 180, …) | inconsistent across doses | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11851.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.558×** | -6.6 | 2e-08 | 23/44 (SK-MEL-2, HT-29, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.604×** | -6.1 | 4e-07 | 21/47 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.752×** | -4.8 | 2e-04 | 19/47 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.722×** | -4.8 | 3e-04 | 16/47 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.731×** | -3.8 | 0.019 | 13/46 (C32, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.735×** | -3.7 | 0.020 | 15/47 (SNU-1, AsPC-1, …) | two highest doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.665×** | -3.5 | 0.035 | 10/37 (BT-474, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.767×** | -3.5 | 0.035 | 11/47 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.588×** | -3.3 | 0.054 | 10/41 (AsPC-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.829×** | -3.2 | 0.082 | 10/47 (AN3 CA, Hs 766T, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.619× | -3.0 | 0.13 | 14/43 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 28.4 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.235× (z -9.1) |
| [[A-172 (line)]] | wt | 6.46 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.110× (z -9.1) ⚠ toxic |
| [[A-427 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.266× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 1 | — | [[Larotrectinib (drug)]] 5 µM 0.267× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 9.02 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 9.36 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0912× (z -9.3) |
| [[SNU-423 (line)]] | alt | 7.67 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.125× (z -9.4) |
| [[A498 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F8]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[ESCO2]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ZWINT]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[FAM111B]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[HELLS]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[MCM4]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[C18orf54]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[HASPIN]] | +0.62 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[RRM2]] | +0.61 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[UHRF1]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 | same gene group |
| [[E2F2]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CDC7]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH2]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[NSA2]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[KIZ-AS1]] ⚠ | -0.55 | -0.48 / -0.51 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RHOQ-AS1]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ZFAS1]] | -0.54 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[EPB41L4A-AS1]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[RPL34]] | -0.53 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[SNHG6]] | -0.52 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[TBCA]] | -0.52 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[RPL21]] ⚠ | -0.52 | -0.45 / -0.55 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NACA]] ⚠ | -0.52 | -0.45 / -0.52 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL37]] ⚠ | -0.52 | -0.48 / -0.51 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF565]] | -0.51 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[RNF10]] | -0.51 | -0.48 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises SPIN4's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-39.9, -46.6); signed map (-38.8, -48.5). **Vector** length 87.3, 16.6% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Unwinding of DNA* (reactome, mean cos +0.52 to 12); *Orc1 removal from chromatin* (reactome, mean cos +0.50 to 12); *TP53 Regulates Transcription of Genes Involved in G1 Cell Cycle Arrest* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | +2.9 | +3.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | +2.3 | +3.2 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.9 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +1.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.9 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -6.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.3 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | spindlin family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq11.1 — chrX:63,347,228-63,351,332 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ44984, TDRD28 |
| Gene groups (HGNC) | Tudor domain containing; Spindlin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q56A73](https://www.uniprot.org/uniprotkb/Q56A73) (Spindlin-4):

> Binds to acetylated and methylated histones, including H3K4me3 and H4K20me3, probably acting as a histone reader that recognizes chromatin marks and mediates downstream cellular effects. Promotes canonical WNT signaling, and is involved in the down-regulation of cell proliferation.

**Summary**, from NCBI Gene [139886](https://www.ncbi.nlm.nih.gov/gene/139886):

> Enables histone H3K4me3 reader activity. Involved in negative regulation of cell population proliferation and positive regulation of canonical Wnt signaling pathway. Located in chromatin; cytoplasm; and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27040) · Entrez [139886](https://www.ncbi.nlm.nih.gov/gene/139886) · UniProt [Q56A73](https://www.uniprot.org/uniprotkb/Q56A73) · Ensembl [ENSG00000186767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186767)

## Data

Gene col 11851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11851); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11851]; `tensor/DDL_lfc|DDL_z.npy` [11851]; `embed/gene_vectors.npy` [11851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11851 or target_col == 11851). Every well: [[SPIN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPIN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
