---
symbol: "TMSB10"
type: "gene"
col: 421
ensembl_id: "ENSG00000034510"
name: "thymosin beta 10"
location: "2p11.2"
module: 48
arm: "+"
pooled_cpm: 932.69
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# TMSB10

*thymosin beta 10* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.65× (z +6.1, q 5e-07, up in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 2.70× (z +3.9, q 0.012, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.327× (z -9.9, q 3e-20, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COMMD6]] (+0.74, fdr 7e-06), [[ATP5MK]] (+0.73, fdr 7e-06), [[COX6A1]] (+0.72, fdr 7e-06); moves opposite to [[HSPB8]] (-0.66, fdr 1e-05), [[PDAP1]] (-0.66, fdr 1e-05), [[PSMC3]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FKBP1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 421.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +6.1 | 5e-07 | 46/48 (SNU-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +4.7 | 6e-04 | 37/43 (HT-29, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **2.02×** | +4.4 | 0.002 | 45/47 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.94×** | +4.2 | 0.004 | 45/47 (NCI-H1573, AsPC-1, …) | top dose only | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.70×** | +3.9 | 0.012 | 47/47 (HT-29, COLO 205, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.41×** | +3.4 | 0.052 | 47/47 (SNU-423, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.40×** | +3.4 | 0.052 | 45/47 (A498, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.28×** | +3.2 | 0.092 | 46/46 (NCI-H23, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **2.25×** | +3.2 | 0.095 | 46/48 (LoVo, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 2.22× | +3.1 | 0.10 | 46/47 (BT-474, AsPC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.327×** | -9.9 | 3e-20 | 45/47 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.439×** | -5.1 | 8e-05 | 41/47 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.548×** | -3.8 | 0.033 | 41/47 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.581×** | -3.4 | 0.092 | 39/47 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.562×** | -3.3 | 0.092 | 43/47 (LoVo, SW480, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.576×** | -3.3 | 0.092 | 34/47 (KATO III, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.577× | -3.2 | 0.13 | 45/47 (C-33 A, SW1417, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.582× | -3.1 | 0.13 | 45/47 (hTERT-HPNE, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.614× | -3.0 | 0.15 | 34/47 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.85 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1,729 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -13.2) |
| [[C-33 A (line)]] | alt | 432 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.7) |
| [[H4 (line)]] | wt | 1,130 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 1,055 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -15.4) |
| [[A-427 (line)]] | wt | 1,373 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -15.6) |
| [[A549 (line)]] | wt | 1,390 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -11.1) |
| [[BT-474 (line)]] | alt | 373 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 1,450 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -10.2) |
| [[CHP-212 (line)]] | wt | 359 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -9.1) |
| [[COLO 205 (line)]] | alt | 273 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 834 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 923 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 511 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -12.6) |
| [[HOP62 (line)]] | alt | 1,386 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.9) |
| [[HS-578T (line)]] | alt | 1,017 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.8) |
| [[HT-29 (line)]] | alt | 689 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +8.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 536 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -8.6) |
| [[KATO III (line)]] | alt | 1,125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 1,148 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.5) |
| [[LS 180 (line)]] | wt | 1,201 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 1,262 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 1,563 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 853 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -8.7) |
| [[NCI-H661 (line)]] | alt | 883 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 814 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -13.8) |
| [[PANC-1 (line)]] | alt | 771 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.5) |
| [[RKO (line)]] | wt | 504 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -11.8) |
| [[SNU-1 (line)]] | wt | 234 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.76× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 1,723 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -9.3) |
| [[SW48 (line)]] | wt | 1,048 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.0) |
| [[SW480 (line)]] | alt | 735 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -10.9) |
| [[A498 (line)]] | wt | 981 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 423 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1,601 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 548 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 666 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1,080 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 847 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 939 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1,011 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 721 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 807 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 869 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 693 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 179 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 480 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 755 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 886 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 673 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 776 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 17 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD6]] | +0.74 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[ATP5MK]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[COX6A1]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[ATP5F1E]] | +0.70 | +0.53 / +0.74 | both halves | 1e-05 |  |
| [[UBL5]] | +0.70 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[RPL36]] | +0.69 | +0.58 / +0.70 | both halves | 7e-06 | STRING 479 |
| [[ROMO1]] | +0.69 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[B3GAT3]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[UBA52]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[NDUFA2]] | +0.68 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | +0.68 | +0.58 / +0.70 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL37A]] ⚠ | +0.67 | +0.56 / +0.67 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ARID3A]] | +0.67 | +0.57 / +0.68 | both halves | 9e-06 |  |
| [[RPLP2]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPB8]] | -0.66 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.66 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[PSMC3]] | -0.64 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[RNF6]] | -0.63 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[ZNF460]] | -0.63 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[PSMD11]] | -0.63 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[PSME3IP1]] | -0.62 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[C17orf80]] | -0.62 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[PNPO]] | -0.62 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[CEP41]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.60 | -0.39 / -0.67 | both halves | 6e-05 |  |
| [[DCLRE1A]] | -0.60 | -0.67 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP1B]] | B | FKBP1B activity raises TMSB10's level | lines that do not express FKBP1B (14) vs lines expressing it (36) | 1.57× lower at baseline in the lines without FKBP1B | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000234139, IGDCC4, C19orf18; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.4, -22.6); signed map (-34.5, 11.2). **Vector** length 99.0, 55.4% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.53 to 31); *Respiratory electron transport* (reactome, mean cos +0.51 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.54 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +4.8 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | -3.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.0 | +1.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.9 | +1.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.9 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.2 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | +2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -1.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | thymosin beta 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:84,905,656-84,906,671 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TB10 |
| Gene groups (HGNC) | Thymosin beta family |
| Matched by | ensembl_id |

**Function**, from UniProt [P63313](https://www.uniprot.org/uniprotkb/P63313) (Thymosin beta-10):

> Plays an important role in the organization of the cytoskeleton. Binds to and sequesters actin monomers (G actin) and therefore inhibits actin polymerization (By similarity).

**Summary**, from NCBI Gene [9168](https://www.ncbi.nlm.nih.gov/gene/9168):

> Predicted to enable actin monomer binding activity and protein sequestering activity. Predicted to be involved in regulation of cell migration. Predicted to be located in cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11879) · Entrez [9168](https://www.ncbi.nlm.nih.gov/gene/9168) · UniProt [P63313](https://www.uniprot.org/uniprotkb/P63313) · Ensembl [ENSG00000034510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000034510)

## Data

Gene col 421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 421); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 421]; `tensor/DDL_lfc|DDL_z.npy` [421]; `embed/gene_vectors.npy` [421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 421 or target_col == 421). Every well: [[TMSB10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMSB10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
