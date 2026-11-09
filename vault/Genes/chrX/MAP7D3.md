---
symbol: "MAP7D3"
type: "gene"
col: 4997
ensembl_id: "ENSG00000129680"
name: "MAP7 domain containing 3"
location: "Xq26.3"
module: 20
arm: "-"
pooled_cpm: 48.72
n_lines_expressing: 44
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# MAP7D3

*MAP7 domain containing 3* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.42× (z +5.5, q 3e-05, up in 23 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Peretinoin (drug)]] 0.5 µM: 1.24× (z +3.4, q 0.064, up in 16 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 3.52×; ⚠ cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 3.82×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.383× (z -7.8, q 4e-12, down in 29 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF5B]] (+0.64, fdr 7e-06), [[NIFK]] (+0.63, fdr 7e-06), [[CEP290]] (+0.61, fdr 1e-05); moves opposite to [[USF1]] (-0.54, fdr 3e-05), [[ANKRD30BL]] (-0.52, fdr 3e-05), [[RUSC1-AS1]] (-0.51, fdr 2e-04).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AKAP12]] → it (grade B ⚠); 1 goes from it, the strongest it → [[XNDC1N-ZNF705EP-ALG1L9P]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4997.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 3.52×; ⚠ cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW 900 3.82×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.42×** | +5.5 | 3e-05 | 23/42 (NCI-H23, NCI-H1573, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.42×** | +5.2 | 6e-05 | 19/37 (SW 900, NCI-H23, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.36×** | +4.8 | 3e-04 | 22/41 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.29×** | +3.9 | 0.011 | 22/41 (SW 900, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.27×** | +3.6 | 0.027 | 15/42 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.28×** | +3.6 | 0.027 | 20/42 (SNU-423, HOP62, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.064 | 16/41 (H4, SW 900, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.23×** | +3.2 | 0.084 | 19/42 (A498, Panc 03.27, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.1 | 0.13 | 11/42 (LS 180, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4997.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.383×** | -7.8 | 4e-12 | 29/42 (PANC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.453×** | -6.4 | 4e-08 | 32/42 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.707×** | -5.4 | 1e-05 | 24/41 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.725×** | -5.0 | 9e-05 | 23/42 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.757×** | -4.3 | 0.002 | 25/42 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.778×** | -3.9 | 0.009 | 23/42 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.838× | -3.9 | 0.009 | 20/42 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.7 | 0.016 | 18/42 (LOX-IMVI, SW48, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | 0.862× | -3.3 | 0.070 | 14/42 (J82, Hs 766T, …) | top dose only | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4997. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 67.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.397× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 70.4 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0590× (z -15.3) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.205× (z -8.6) |
| [[PANC-1 (line)]] | alt | 103 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.240× (z -10.2) |
| [[J82 (line)]] | alt | 72.7 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.473× (z -10.8) ⚠ cell-cycle shift, explains ~97% of this change |
| [[SW480 (line)]] | alt | 57.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.391× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.409× (z -9.8) |
| [[A-427 (line)]] | wt | 65.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.52× (z +9.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H661 (line)]] | alt | 43.9 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0959× (z -8.5) |
| [[RKO (line)]] | wt | 56.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.337× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 46.3 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.308× (z -10.7) |
| [[SW 900 (line)]] | alt | 29.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A-172 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.56 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 99.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.08 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4997), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF5B]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[NIFK]] | +0.63 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[CEP290]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[DDX50]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[PHF20]] | +0.59 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[ZNF354A]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[FRA10AC1]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ESF1]] | +0.57 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ZC3H8]] | +0.57 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ZNF146]] | +0.56 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TIPRL]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[SMC6]] | +0.53 | +0.55 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USF1]] | -0.54 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ANKRD30BL]] | -0.52 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[RUSC1-AS1]] | -0.51 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | -0.51 | -0.28 / -0.30 | both halves | 3e-04 |  |
| [[SLC16A4-AS1]] | -0.50 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[H3-3A]] | -0.50 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[ZNF410]] | -0.50 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[LAPTM4A]] | -0.50 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[LAMTOR5-AS1]] | -0.49 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[HIPK1]] | -0.49 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[AKT2]] | -0.49 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[RTCA-AS1]] | -0.49 | -0.28 / -0.18 | ⚠ not reproduced | 0.001 |  |
| [[DDOST]] | -0.49 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKAP12]] | B | AKAP12 activity raises MAP7D3's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 2.18× lower at baseline in the lines without AKAP12 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[HDAC6]] | B | HDAC6 activity lowers MAP7D3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XNDC1N-ZNF705EP-ALG1L9P]] | B | MAP7D3 activity lowers XNDC1N-ZNF705EP-ALG1L9P's level | lines that do not express MAP7D3 (6) vs lines expressing it (44) | 1.51× higher at baseline in the lines without MAP7D3 | 0.022 | ⚠ within organs, on part of the lines; also absent: ROBO3, KIRREL1, ANKRD44 |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.407). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.3, -0.2); signed map (-2.1, -19.8). **Vector** length 85.4, 21.1% of its response variance represented; |z| ≥ 3 in 674 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.5 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.7 | +2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | +2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.8 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +1.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.2 | -7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.1 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -3.0 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | MAP7 domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:136,213,220-136,256,482 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12649 |
| Gene groups (HGNC) | Microtubule associated protein 7 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWC1](https://www.uniprot.org/uniprotkb/Q8IWC1) (MAP7 domain-containing protein 3):

> Promotes the assembly and stability of microtubules.

**Summary**, from NCBI Gene [79649](https://www.ncbi.nlm.nih.gov/gene/79649):

> The protein encoded by this gene belongs to the MAP7 (microtubule-associated protein 7) family. Alternatively spliced transcript variants encoding different isoforms have been found. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:25742](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25742) · Entrez [79649](https://www.ncbi.nlm.nih.gov/gene/79649) · UniProt [Q8IWC1](https://www.uniprot.org/uniprotkb/Q8IWC1) · Ensembl [ENSG00000129680](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129680)

## Data

Gene col 4997: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4997); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4997, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4997]; `tensor/DDL_lfc|DDL_z.npy` [4997]; `embed/gene_vectors.npy` [4997]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4997 or target_col == 4997). Every well: [[MAP7D3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP7D3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
