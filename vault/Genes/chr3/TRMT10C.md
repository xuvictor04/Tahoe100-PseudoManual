---
symbol: "TRMT10C"
type: "gene"
col: 10469
ensembl_id: "ENSG00000174173"
name: "tRNA methyltransferase 10C, mitochondrial RNase P subunit"
location: "3q12.3"
module: 7
arm: "+"
pooled_cpm: 21.16
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TRMT10C

*tRNA methyltransferase 10C, mitochondrial RNase P subunit* — 3q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.28× (z +7.7, q 6e-12, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.755× (z -4.1, q 0.022, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.219×, RPMI-7951 0.172×, LoVo 0.251×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.213×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LLPH]] (+0.78, fdr 7e-06), [[KTI12]] (+0.76, fdr 7e-06), [[CEBPZ]] (+0.75, fdr 7e-06); moves opposite to [[SEPTIN2]] (-0.61, fdr 7e-06), [[HDAC6]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAGEA4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10469.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.28×** | +7.7 | 6e-12 | 42/48 (PANC-1, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +7.5 | 2e-11 | 40/45 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +6.7 | 4e-09 | 39/47 (HS-578T, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +6.7 | 4e-09 | 33/47 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.83×** | +5.5 | 3e-06 | 34/44 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.76×** | +5.5 | 3e-06 | 34/47 (NCI-H1792, HS-578T, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.70×** | +5.3 | 8e-06 | 33/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +5.1 | 2e-05 | 32/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +4.7 | 1e-04 | 29/47 (SNU-423, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +4.4 | 6e-04 | 25/47 (A498, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +4.3 | 8e-04 | 24/48 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.59×** | +4.3 | 8e-04 | 25/38 (NCI-H1573, A549, …) | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.50×** | +4.1 | 0.002 | 27/44 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.003 | 26/48 (C32, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.45×** | +3.7 | 0.007 | 20/47 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.034 | 17/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.041 | 21/47 (NCI-H2347, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.041 | 16/48 (HS-578T, SW 900, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.38×** | +3.0 | 0.071 | 14/47 (NCI-H460, SW480, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10469.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (KATO III 0.219×, RPMI-7951 0.172×, LoVo 0.251×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.213×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.755×** | -4.1 | 0.022 | 28/48 (Panc 03.27, A-172, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.716× | -3.5 | 0.15 | 16/48 (A498, CFPAC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 36.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -14.2) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LLPH]] | +0.78 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[KTI12]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CEBPZ]] | +0.75 | +0.75 / +0.78 | both halves | 7e-06 |  |
| [[DDX28]] | +0.75 | +0.76 / +0.72 | both halves | 7e-06 | STRING 518 |
| [[REXO4]] | +0.75 | +0.84 / +0.71 | both halves | 7e-06 |  |
| [[UTP3]] | +0.75 | +0.77 / +0.77 | both halves | 7e-06 | pathway: rRNA processing |
| [[DNTTIP2]] | +0.74 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[MRM2]] | +0.74 | +0.77 / +0.71 | both halves | 7e-06 | same gene group; pathway: rRNA processing; STRING 611 |
| [[MRTO4]] | +0.73 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[SURF6]] | +0.73 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[YTHDF2]] | +0.72 | +0.73 / +0.77 | both halves | 7e-06 | STRING 512 |
| [[EXOSC4]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 | pathway: rRNA processing |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN2]] | -0.61 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[HDAC6]] | -0.58 | -0.60 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAGEA4]] | B | MAGEA4 activity raises TRMT10C's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.29× lower at baseline in the lines without MAGEA4 | 0.095 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[TP53]] | C | TP53 activity weakens TRMT10C's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 1.32× as strongly (z diff -0.86); strongest at Ixazomib citrate 5 µM: 1.65x vs 1.35x (z diff -1.4) | 0.907 over the table, 0.086 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-41.0, 2.0); signed map (-3.3, -23.9). **Vector** length 85.0, 22.3% of its response variance represented; |z| ≥ 3 in 740 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.7 | +5.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.8 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.8 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | -3.0 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 10C, mitochondrial RNase P subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.3 — chr3:101,561,868-101,566,446 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20432, MRPP1; previously RG9MTD1 |
| Gene groups (HGNC) | SPOUT methyltransferase domain containing; Mitochondrial RNase P complex; DNA/RNA methyltransferases |
| Reactome | 6 pathways, smallest: tRNA modification in the mitochondrion; tRNA processing in the mitochondrion; rRNA processing in the mitochondrion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L0Y3](https://www.uniprot.org/uniprotkb/Q7L0Y3) (tRNA methyltransferase 10 homolog C):

> Mitochondrial tRNA N(1)-methyltransferase involved in mitochondrial tRNA maturation. Component of mitochondrial ribonuclease P, a complex composed of TRMT10C/MRPP1, HSD17B10/MRPP2 and PRORP/MRPP3, which cleaves tRNA molecules in their 5'-ends. Together with HSD17B10/MRPP2, forms a subcomplex of the mitochondrial ribonuclease P, named MRPP1-MRPP2 subcomplex, which displays functions that are independent of the ribonuclease P activity. The MRPP1-MRPP2 subcomplex catalyzes the formation of …

**Summary**, from NCBI Gene [54931](https://www.ncbi.nlm.nih.gov/gene/54931):

> This gene encodes the precursor of a subunit of the mitochondrial ribonuclease P, which is involved in 5' processing of mitochondrial tRNAs. The encoded protein may confer RNA-binding capacity to mitochondrial ribonuclease P and may be essential for transcript processing, RNA modification, translation and mitochondrial respiration. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:26022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26022) · Entrez [54931](https://www.ncbi.nlm.nih.gov/gene/54931) · UniProt [Q7L0Y3](https://www.uniprot.org/uniprotkb/Q7L0Y3) · Ensembl [ENSG00000174173](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174173)

## Data

Gene col 10469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10469); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10469]; `tensor/DDL_lfc|DDL_z.npy` [10469]; `embed/gene_vectors.npy` [10469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10469 or target_col == 10469). Every well: [[TRMT10C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT10C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
