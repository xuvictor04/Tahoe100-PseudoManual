---
symbol: "PCDHB2"
type: "gene"
col: 3412
ensembl_id: "ENSG00000112852"
name: "protocadherin beta 2"
location: "5q31.3"
module: 29
arm: "+"
pooled_cpm: 2.08
n_lines_expressing: 28
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PCDHB2

*protocadherin beta 2* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.69× (z +8.0, q 8e-13, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.76× (z +6.7, q 5e-09, up in 6 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.331× (z -9.3, q 8e-18, down in 15 of 18 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFI]] (+0.56, fdr 3e-05), [[ARHGEF25]] (+0.56, fdr 4e-05), [[PRDX3]] (+0.56, fdr 2e-05); moves opposite to [[TNRC6C]] (-0.46, fdr 1e-04), [[GATAD1]] (-0.46, fdr 4e-05), [[PPP1R13L]] (-0.45, fdr 2e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HGF]] → it (grade C ⚠); 2 go from it, the strongest it → [[ATF4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3412.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.69×** | +8.0 | 8e-13 | 1/3 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +6.7 | 5e-09 | 6/24 (RKO, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +6.4 | 3e-08 | 5/12 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +4.6 | 7e-04 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.015 | 2/18 (LS 180, C32) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.11×** | +3.3 | 0.098 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.48× | +3.2 | 0.12 | 2/8 (A498, C32) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3412.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.331×** | -9.3 | 8e-18 | 15/18 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.504×** | -8.2 | 8e-14 | 18/20 (NCI-H2030, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.394×** | -7.6 | 8e-12 | 15/22 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.531×** | -5.3 | 2e-05 | 9/23 (C32, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.601×** | -4.3 | 0.002 | 12/25 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.622×** | -4.0 | 0.006 | 5/24 (RKO, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.633×** | -3.9 | 0.009 | 9/24 (A549, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.645×** | -3.7 | 0.015 | 7/23 (C32, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.663×** | -3.5 | 0.033 | 8/24 (KATO III, LS 180, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -3.3 | 0.058 | 6/14 (LOX-IMVI, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Verteporfin (drug)]] 0.5 µM |  | **0.690×** | -3.1 | 0.091 | 6/24 (SK-MEL-2, RKO, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.698× | -3.0 | 0.11 | 5/24 (H4, RKO, …) | all doses, flat | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3412. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 23.3 | 0 | 2 | — | [[Captopril (drug)]] 0.5 µM 0.0681× (z -9.0) |
| [[C32 (line)]] | wt | 6.81 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -15.3) |
| [[HepG2_C3A (line)]] | wt | 4.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -8.6) |
| [[PANC-1 (line)]] | alt | 1.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0409× (z -10.5) |
| [[SHP-77 (line)]] | alt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -12.7) |
| [[A-172 (line)]] | wt | 0.273 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.194 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.164 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.139 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.945 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.185 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.166 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3412), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFI]] | +0.56 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[ARHGEF25]] | +0.56 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[PRDX3]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[LAPTM4B]] | +0.55 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[MMP2]] | +0.54 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[FUCA2]] | +0.53 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[PPT1]] | +0.51 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[GPX3]] | +0.51 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[APP]] | +0.51 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[VAV3]] | +0.50 | +0.38 / +0.41 | both halves | 6e-05 |  |
| [[GSTA4]] | +0.49 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[COL3A1]] | +0.49 | +0.37 / +0.39 | both halves | 8e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.46 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[GATAD1]] | -0.46 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[PPP1R13L]] | -0.45 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[TRIOBP]] | -0.43 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[INAFM1]] | -0.43 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ATF4]] | -0.42 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[SMC6]] | -0.42 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[IKBKB]] | -0.42 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[PDCD7]] | -0.41 | -0.37 / -0.46 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HGF]] | C | HGF activity raises PCDHB2's level | lines that do not express HGF (38) vs lines expressing it (12) | 2.35× lower at baseline in the lines without HGF | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATF4]] | B | PCDHB2 activity raises ATF4's level | lines that do not express PCDHB2 (22) vs lines expressing it (28) | 1.12× lower at baseline in the lines without PCDHB2 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, VCAN, IHO1 |
| [[HGF]] | C | PCDHB2 activity raises HGF's level | lines that do not express PCDHB2 (22) vs lines expressing it (28) | 2.15× lower at baseline in the lines without PCDHB2 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000290931, VCAN, IHO1; co-absent with the target |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.512). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.7, 41.6); signed map (25.2, -44.6). **Vector** length 33.8, 4.85% of its response variance represented; |z| ≥ 3 in 612 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.3 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +6.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.8 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | -0.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.6 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.1 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.7 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | protocadherin beta 2 |
| Locus type | complex locus constituent (other) |
| Location | 5q31.3 — chr5:141,094,606-141,098,703 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCDH-BETA2 |
| Gene groups (HGNC) | Clustered protocadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5E7](https://www.uniprot.org/uniprotkb/Q9Y5E7) (Protocadherin beta-2):

> Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain.

**Summary**, from NCBI Gene [56133](https://www.ncbi.nlm.nih.gov/gene/56133):

> This gene is a member of the protocadherin beta gene cluster, one of three related gene clusters tandemly linked on chromosome five. The gene clusters demonstrate an unusual genomic organization similar to that of B-cell and T-cell receptor gene clusters. The beta cluster contains 16 genes and 3 pseudogenes, each encoding 6 extracellular cadherin domains and a cytoplasmic tail that deviates from others in the cadherin superfamily. The extracellular domains interact in a homophilic manner to …

**Accessions** — [HGNC:8687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8687) · Entrez [56133](https://www.ncbi.nlm.nih.gov/gene/56133) · UniProt [Q9Y5E7](https://www.uniprot.org/uniprotkb/Q9Y5E7) · Ensembl [ENSG00000112852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112852)

## Data

Gene col 3412: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3412); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3412, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3412]; `tensor/DDL_lfc|DDL_z.npy` [3412]; `embed/gene_vectors.npy` [3412]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3412 or target_col == 3412). Every well: [[PCDHB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCDHB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
