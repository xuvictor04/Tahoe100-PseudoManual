---
symbol: "CCDC144A"
type: "gene"
col: 9910
ensembl_id: "ENSG00000170160"
name: "coiled-coil domain containing 144A"
location: "17p11.2"
module: 177
arm: "+"
pooled_cpm: 2.94
n_lines_expressing: 32
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# CCDC144A

*coiled-coil domain containing 144A* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.31× (z +14.6, q 1e-45, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +8.1, q 1e-13, up in 5 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Oxaprozin (drug)]] 0.05 µM in 1 line (CHP-212 0.0531×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC144BP]] (+0.64, fdr 7e-06), [[ENPP2]] (+0.52, fdr 3e-05), [[ATRNL1]] (+0.51, fdr 1e-05); moves opposite to [[FAM118B]] (-0.44, fdr 3e-04), [[RAN]] (-0.42, fdr 3e-04), [[MCM9]] (-0.40, fdr 2e-04).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SULF1]] → it (grade B ⚠); 2 go from it, the strongest it → [[ST8SIA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9910.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.31×** | +14.6 | 1e-45 | 1/5 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.88×** | +10.2 | 5e-22 | 2/8 (A498, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +8.1 | 1e-13 | 5/22 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +6.7 | 2e-09 | 5/20 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +5.0 | 7e-05 | 8/27 (C32, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +4.8 | 2e-04 | 6/28 (SW 900, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.72×** | +4.0 | 0.004 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +3.9 | 0.006 | 2/11 (NCI-H1792, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.69×** | +3.9 | 0.006 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.023 | 2/27 (SW 900, J82) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.024 | 3/23 (SW480, SHP-77, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +3.5 | 0.024 | 1/5 (A-172) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.4 | 0.034 | 0/6 | top dose only | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.035 | 1/27 (C-33 A) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.048 | 2/27 (HS-578T, SW 900) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.048 | 8/25 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.50×** | +3.0 | 0.088 | 1/17 (COLO 205) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Canagliflozin (drug)]] 5 µM |  | **1.34×** | +2.9 | 0.096 | 1/21 (C32) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9910.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Oxaprozin (drug)]] 0.05 µM in 1 line (CHP-212 0.0531×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | 0.743× | -3.1 | 0.97 | 5/26 (H4, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9910. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 25.7 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0531× (z -9.6) |
| [[A-172 (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.792 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.989 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.822 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.690 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.878 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9910), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC144BP]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ENPP2]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[ATRNL1]] | +0.51 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ZNF471]] | +0.51 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[CCDC144NL-AS1]] | +0.50 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[LINC01266]] | +0.49 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[LDB2]] | +0.49 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[PASD1]] | +0.47 | +0.36 / +0.41 | both halves | 1e-04 |  |
| [[UTY]] | +0.47 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[LINC02476]] | +0.47 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[PKNOX2]] | +0.46 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[HAND2-AS1]] | +0.46 | +0.47 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118B]] | -0.44 | -0.28 / -0.32 | both halves | 3e-04 |  |
| [[RAN]] | -0.42 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[MCM9]] | -0.40 | -0.37 / -0.29 | both halves | 2e-04 |  |
| [[CTCF]] | -0.40 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[ASH2L]] | -0.39 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[TRAPPC13]] | -0.38 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[SGF29]] | -0.37 | -0.29 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SULF1]] | B | SULF1 activity raises CCDC144A's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 1.89× lower at baseline in the lines without SULF1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT |
| [[CCDC144BP]] | C | CCDC144BP activity raises CCDC144A's level | lines that do not express CCDC144BP (23) vs lines expressing it (27) | 3.34× lower at baseline in the lines without CCDC144BP | 1e-04 | ⚠ within organs, on part of the lines; also absent: FAM106A, ENSG00000266302, CCDC144A; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST8SIA1]] | B | CCDC144A activity raises ST8SIA1's level | lines that do not express CCDC144A (18) vs lines expressing it (32) | 1.36× lower at baseline in the lines without CCDC144A | 0.054 | ⚠ within organs, on part of the lines; also absent: CCDC144BP, MCOLN3, ENSG00000266302; maybe low, not absent |
| [[CCDC144BP]] | C | CCDC144A activity raises CCDC144BP's level | lines that do not express CCDC144A (18) vs lines expressing it (32) | 5.56× lower at baseline in the lines without CCDC144A | 0.005 | ⚠ within organs, on part of the lines; also absent: CCDC144BP, MCOLN3, ENSG00000266302; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.4, 29.3); signed map (35.5, 35.3). **Vector** length 19.8, 1.62% of its response variance represented; |z| ≥ 3 in 564 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.7 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +3.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.7 | -0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.5 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.5 | +3.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.8 | +0.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -0.8 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.7 | -1.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.7 | -0.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.6 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -0.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 144A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:16,689,537-16,777,881 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0565, FLJ43983 |
| Matched by | ensembl_id |

**Function**, from UniProt [A2RUR9](https://www.uniprot.org/uniprotkb/A2RUR9) (Coiled-coil domain-containing protein 144A):

> May play a role in preventing the formation of kidney stones through inhibition of calcium oxalate monohydrate (COM) crystallization, attenuating COM-induced apoptotic injury to renal epithelial cells. May exhibit antilithiatic (preventing the formation of kidney stones) activity through crystal binding, hindering the crystal attachment to renal epithelial cells, a pre-requisite to initiate inflammatory response.

**Summary**, from NCBI Gene [9720](https://www.ncbi.nlm.nih.gov/gene/9720):

> Predicted to enable calcium oxalate binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29072) · Entrez [9720](https://www.ncbi.nlm.nih.gov/gene/9720) · UniProt [A2RUR9](https://www.uniprot.org/uniprotkb/A2RUR9) · Ensembl [ENSG00000170160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170160)

## Data

Gene col 9910: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9910); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9910, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9910]; `tensor/DDL_lfc|DDL_z.npy` [9910]; `embed/gene_vectors.npy` [9910]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9910 or target_col == 9910). Every well: [[CCDC144A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC144A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
