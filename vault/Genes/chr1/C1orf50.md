---
symbol: "C1orf50"
type: "gene"
col: 8831
ensembl_id: "ENSG00000164008"
name: "chromosome 1 open reading frame 50"
location: "1p34.2"
module: 17
arm: "+"
pooled_cpm: 7.28
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# C1orf50

*chromosome 1 open reading frame 50* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.43× (z +12.9, q 1e-35, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.743× (z -4.3, q 0.009, down in 11 of 47 measured lines) ⚠ unreliable plate only. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 0.145×, MIA PaCa-2 0.208×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.193×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.124×); [[Valdecoxib (drug)]] 0.05 µM in 1 line (BT-474 0.0916×); [[Apalutamide (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0736×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACOT8]] (+0.74, fdr 7e-06), [[FRG1DP]] (+0.68, fdr 7e-06), [[TRIM23]] (+0.63, fdr 1e-05); moves opposite to [[MAPRE1]] (-0.59, fdr 3e-05), [[RBBP8]] (-0.53, fdr 4e-05), [[HNRNPA2B1]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC28A2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8831.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.43×** | +12.9 | 1e-35 | 41/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.29×** | +12.1 | 3e-31 | 40/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.28×** | +12.0 | 4e-31 | 37/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +11.5 | 3e-28 | 30/44 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.17×** | +5.9 | 4e-07 | 16/46 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +5.1 | 3e-05 | 14/41 (SW480, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.8 | 1e-04 | 14/42 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 4e-04 | 14/41 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +4.4 | 5e-04 | 4/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.3 | 8e-04 | 17/43 (PANC-1, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.003 | 11/42 (C-33 A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +4.0 | 0.003 | 13/47 (A498, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.033 | 5/42 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.17× | +3.3 | 0.039 | 3/48 (NCI-H2030, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8831.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 0.145×, MIA PaCa-2 0.208×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.193×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.124×); [[Valdecoxib (drug)]] 0.05 µM in 1 line (BT-474 0.0916×); [[Apalutamide (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0736×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.743×** | -4.3 | 0.009 | 11/47 (SW 1271, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.781×** | -3.6 | 0.095 | 12/30 (NCI-H460, MIA PaCa-2, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8831. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 5.40 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.72× (z +10.1) | [[Nevirapine (drug)]] 0.05 µM 0.0708× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 5.41 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 5.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 5.80 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0916× (z -9.1) |
| [[H4 (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0980× (z -8.6) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.103× (z -8.7) ⚠ transcription drop |
| [[hTERT-HPNE (line)]] | wt | 6.50 | 0 | 1 | — | [[Apalutamide (drug)]] 5 µM 0.0736× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 7.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SHP-77 (line)]] | alt | 9.18 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.124× (z -9.5) |
| [[SW480 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[A-172 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8831), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOT8]] | +0.74 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[FRG1DP]] | +0.68 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[TRIM23]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[TTI2]] | +0.62 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[SECISBP2L]] | +0.62 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[EXOC1]] | +0.61 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ZNF14]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CWC15]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ZSWIM8]] | +0.60 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[MALSU1]] | +0.60 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ACTR10]] | +0.60 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[USP30]] | +0.60 | +0.41 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.59 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[RBBP8]] | -0.53 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[HNRNPA2B1]] | -0.52 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[XRCC5]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC28A2-AS1]] | B | SLC28A2-AS1 activity raises C1orf50's level | lines that do not express SLC28A2-AS1 (9) vs lines expressing it (41) | 1.22× lower at baseline in the lines without SLC28A2-AS1 | 0.051 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.446). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-23.6, -5.5); signed map (-23.9, -9.7). **Vector** length 50.2, 6.00% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +11.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +1.6 | +5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.5 | +12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.5 | +4.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.5 | +12.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +5.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Carbamazepine (drug)]] 0.5 µM |  | +1.0 | +1.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -4.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.2 | -2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 1 open reading frame 50 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:42,767,245-42,779,491 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC955 |
| Matched by | ensembl_id |

UniProt [Q9BV19](https://www.uniprot.org/uniprotkb/Q9BV19) carries no function annotation.

**Summary**, from NCBI Gene [79078](https://www.ncbi.nlm.nih.gov/gene/79078):

> Enables identical protein binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28795](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28795) · Entrez [79078](https://www.ncbi.nlm.nih.gov/gene/79078) · UniProt [Q9BV19](https://www.uniprot.org/uniprotkb/Q9BV19) · Ensembl [ENSG00000164008](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164008)

## Data

Gene col 8831: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8831); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8831, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8831]; `tensor/DDL_lfc|DDL_z.npy` [8831]; `embed/gene_vectors.npy` [8831]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8831 or target_col == 8831). Every well: [[C1orf50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1orf50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
