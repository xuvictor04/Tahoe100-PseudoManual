---
symbol: "GLOD4"
type: "gene"
col: 9521
ensembl_id: "ENSG00000167699"
name: "glyoxalase domain containing 4"
location: "17p13.3"
module: 28
arm: "+"
pooled_cpm: 38.71
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# GLOD4

*glyoxalase domain containing 4* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.51× (z +7.5, q 3e-11, up in 29 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.34× (z +5.3, q 3e-05, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.846× (z -4.2, q 0.012, down in 19 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD50]] (+0.64, fdr 7e-06), [[NOL8]] (+0.63, fdr 7e-06), [[NOP14]] (+0.63, fdr 1e-05); moves opposite to [[NDUFA4]] (-0.57, fdr 5e-05), [[ZNF277]] (-0.55, fdr 3e-05), [[COX6A1]] (-0.53, fdr 6e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GPX3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9521.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +7.5 | 3e-11 | 29/47 (A498, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.6 | 8e-06 | 25/38 (A549, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.3 | 3e-05 | 26/48 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +5.0 | 6e-05 | 23/40 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.21×** | +5.0 | 6e-05 | 24/48 (H4, SNU-423, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.7 | 2e-04 | 21/48 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.003 | 23/48 (PANC-1, HOP62, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.005 | 22/47 (SW48, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Belzutifan (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.054 | 15/46 (KATO III, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.068 | 10/48 (MIA PaCa-2, J82, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.12× | +3.0 | 0.13 | 5/48 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9521.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -4.2 | 0.012 | 19/48 (RPMI-7951, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.804×** | -3.9 | 0.023 | 20/47 (BT-474, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.810×** | -3.8 | 0.023 | 21/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.658×** | -3.8 | 0.023 | 19/48 (SNU-1, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.676×** | -3.5 | 0.048 | 19/48 (AsPC-1, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.685×** | -3.4 | 0.062 | 15/43 (KATO III, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -3.2 | 0.11 | 0/48 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.830× | -3.1 | 0.12 | 17/48 (LS 180, SK-MEL-2, …) | inconsistent across doses |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.888× | -3.0 | 0.17 | 3/48 (C-33 A, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 56.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.7) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[A498 (line)]] | wt | 52.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -13.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 36.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.1) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[J82 (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.3) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[SNU-423 (line)]] | alt | 36.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.7) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[A-427 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 57.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD50]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[NOL8]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[NOP14]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[RNF214]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ICE2]] | +0.55 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[HPS4]] | +0.55 | +0.40 / +0.61 | both halves | 4e-05 |  |
| [[CCDC25]] | +0.55 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[MTIF2]] | +0.55 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[RIMOC1]] | +0.54 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[MRPS16]] | +0.54 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[DUS4L]] | +0.54 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[BDP1]] | +0.53 | +0.45 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA4]] | -0.57 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[ZNF277]] | -0.55 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[COX6A1]] | -0.53 | -0.64 / -0.38 | both halves | 6e-05 |  |
| [[COX6C]] | -0.52 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[UBL5]] | -0.51 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[MYO1F]] | -0.50 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[CST3]] | -0.49 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ATOX1]] | -0.49 | -0.58 / -0.28 | both halves | 3e-04 |  |
| [[ATP5F1E]] | -0.48 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[PROCR]] | -0.48 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[SERF2]] | -0.47 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[HINT1]] | -0.47 | -0.54 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPX3]] | B | GPX3 activity lowers GLOD4's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.30× higher at baseline in the lines without GPX3 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.4, 3.4); signed map (6.0, -27.0). **Vector** length 67.8, 12.9% of its response variance represented; |z| ≥ 3 in 586 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +4.3 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +5.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +4.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | +0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | glyoxalase domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:757,097-782,294 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-150, HC71; previously C17orf25 |
| Gene groups (HGNC) | Glyoxalase domain containing |
| Matched by | ensembl_id |

UniProt [Q9HC38](https://www.uniprot.org/uniprotkb/Q9HC38) carries no function annotation.

**Summary**, from NCBI Gene [51031](https://www.ncbi.nlm.nih.gov/gene/51031):

> Enables cadherin binding activity. Located in extracellular exosome and mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14111](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14111) · Entrez [51031](https://www.ncbi.nlm.nih.gov/gene/51031) · UniProt [Q9HC38](https://www.uniprot.org/uniprotkb/Q9HC38) · Ensembl [ENSG00000167699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167699)

## Data

Gene col 9521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9521); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9521]; `tensor/DDL_lfc|DDL_z.npy` [9521]; `embed/gene_vectors.npy` [9521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9521 or target_col == 9521). Every well: [[GLOD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLOD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
