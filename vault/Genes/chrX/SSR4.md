---
symbol: "SSR4"
type: "gene"
col: 11141
ensembl_id: "ENSG00000180879"
name: "signal sequence receptor subunit 4"
location: "Xq28"
module: 48
arm: "+"
pooled_cpm: 31.97
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# SSR4

*signal sequence receptor subunit 4* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.71× (z +8.5, q 1e-14, up in 39 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.13× (z +6.8, q 3e-09, up in 44 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 5.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.499× (z -6.1, q 8e-07, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HS-578T 0.213×, SK-MEL-2 0.233×, SHP-77 0.251×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OST4]] (+0.85, fdr 7e-06), [[RABAC1]] (+0.81, fdr 7e-06), [[SPCS1]] (+0.78, fdr 7e-06); moves opposite to [[GTF2H3]] (-0.68, fdr 7e-06), [[SRSF3]] (-0.64, fdr 1e-05), [[GMFB]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AGR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11141.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 5.18×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.71×** | +8.5 | 1e-14 | 39/42 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.14×** | +7.2 | 2e-10 | 34/36 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +6.8 | 3e-09 | 44/47 (A-172, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **2.16×** | +5.0 | 7e-05 | 42/47 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.22×** | +4.8 | 2e-04 | 33/38 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.97×** | +4.4 | 1e-03 | 37/46 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.2 | 0.003 | 33/45 (CFPAC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.61× | +3.1 | 0.14 | 28/46 (C32, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11141.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HS-578T 0.213×, SK-MEL-2 0.233×, SHP-77 0.251×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.499×** | -6.1 | 8e-07 | 39/48 (HS-578T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | 0.355× | -3.3 | 0.25 | 36/48 (CHP-212, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.593× | -3.1 | 0.25 | 32/48 (LoVo, NCI-H23, …) | inconsistent across doses |  |
| [[Baicalin (drug)]] 5 µM |  | 0.702× | -3.1 | 0.25 | 32/48 (RKO, HT-29, …) | top dose only | position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.598× | -3.1 | 0.25 | 32/48 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.05 µM |  | 0.603× | -3.0 | 0.25 | 30/48 (A-172, LoVo, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11141. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 49.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SHP-77 (line)]] | alt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 30.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -9.9) |
| [[A-172 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11141), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OST4]] | +0.85 | +0.80 / +0.85 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 904 |
| [[RABAC1]] | +0.81 | +0.67 / +0.85 | both halves | 7e-06 | STRING 424 |
| [[SPCS1]] | +0.78 | +0.66 / +0.81 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 739 |
| [[UBL5]] | +0.78 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[UQCRQ]] ⚠ | +0.77 | +0.73 / +0.76 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SEC61G]] | +0.76 | +0.71 / +0.80 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 961 |
| [[NDUFA2]] | +0.76 | +0.54 / +0.80 | both halves | 1e-05 |  |
| [[SERF2]] | +0.75 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[NDUFA1]] | +0.74 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[ROMO1]] | +0.74 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[COX6B1]] | +0.74 | +0.57 / +0.79 | both halves | 1e-05 |  |
| [[UQCR11]] | +0.73 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[HIGD2A]] | +0.73 | +0.65 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H3]] | -0.68 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[SRSF3]] | -0.64 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[GMFB]] | -0.63 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[U2SURP]] | -0.63 | -0.58 / -0.57 | both halves | 8e-06 |  |
| [[FKTN]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.62 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[SFPQ]] | -0.61 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[RIF1]] | -0.61 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[COA7]] | -0.60 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[SLC25A24]] | -0.60 | -0.42 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR2]] | B | AGR2 activity raises SSR4's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.31× lower at baseline in the lines without AGR2 | 0.033 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.827). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.7, -21.7); signed map (-34.1, 10.4). **Vector** length 67.3, 22.7% of its response variance represented; |z| ≥ 3 in 487 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.62 to 31); *Respiratory electron transport* (reactome, mean cos +0.61 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.62 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +6.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +3.5 | +4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +0.9 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -3.0 | +4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -2.8 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | signal sequence receptor subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,793,516-153,798,499 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRAPD |
| Gene groups (HGNC) | Translocon associated protein complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [P51571](https://www.uniprot.org/uniprotkb/P51571) (Translocon-associated protein subunit delta):

> TRAP proteins are part of a complex whose function is to bind calcium to the ER membrane and thereby regulate the retention of ER resident proteins.

**Summary**, from NCBI Gene [6748](https://www.ncbi.nlm.nih.gov/gene/6748):

> This gene encodes the delta subunit of the translocon-associated protein complex which is involved in translocating proteins across the endoplasmic reticulum membrane. The encoded protein is located in the Xq28 region and is arranged in a compact head-to-head manner with the isocitrate dehydrogenase 3 (NAD+) gamma gene and both genes are driven by a CpG-embedded bidirectional promoter. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:11326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11326) · Entrez [6748](https://www.ncbi.nlm.nih.gov/gene/6748) · UniProt [P51571](https://www.uniprot.org/uniprotkb/P51571) · Ensembl [ENSG00000180879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180879)

## Data

Gene col 11141: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11141); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11141, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11141]; `tensor/DDL_lfc|DDL_z.npy` [11141]; `embed/gene_vectors.npy` [11141]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11141 or target_col == 11141). Every well: [[SSR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
