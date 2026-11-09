---
symbol: "TMSB15B"
type: "gene"
col: 8160
ensembl_id: "ENSG00000158427"
name: "thymosin beta 15B"
location: "Xq22.2"
module: 33
arm: "+"
pooled_cpm: 2.81
n_lines_expressing: 39
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# TMSB15B

*thymosin beta 15B* — Xq22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.58× (z +5.9, q 2e-06, up in 8 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AADAT]] (+0.70, fdr 7e-06), [[STK32B]] (+0.56, fdr 1e-05), [[ZFP69]] (+0.53, fdr 2e-05); moves opposite to [[MYO9A]] (-0.57, fdr 2e-05), [[DYNC2I1]] (-0.54, fdr 1e-05), [[TBCK]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MGAT5B]] → it (grade B ⚠); 2 go from it, the strongest it → [[KATNIP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +5.9 | 2e-06 | 8/34 (NCI-H23, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +5.0 | 1e-04 | 12/34 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +4.9 | 1e-04 | 1/6 (SNU-423) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +4.9 | 2e-04 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.68×** | +4.8 | 2e-04 | 3/14 (A-427, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +4.3 | 0.002 | 5/22 (A498, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +4.3 | 0.002 | 5/26 (SW1417, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.31×** | +4.0 | 0.004 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.030 | 4/18 (Panc 03.27, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +3.3 | 0.060 | 6/34 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.2 | 0.060 | 0/10 | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.075 | 2/31 (NCI-H460, HepG2/C3A) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.091 | 2/32 (NCI-H2030, A498) | inconsistent across doses |  |
| [[Imiquimod (maleate) (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.096 | 4/24 (SNU-423, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8160.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | 0.668× | -3.5 | 0.20 | 3/34 (HCT15, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.680× | -3.4 | 0.20 | 7/22 (NCI-H23, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | 0.716× | -3.1 | 0.41 | 8/17 (SW480, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.559 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.209 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.892 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.794 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.293 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AADAT]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[STK32B]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ZFP69]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[CHST10]] | +0.50 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ZNF232]] | +0.50 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[TTPA]] | +0.50 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[LCP1]] | +0.49 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[VASH2]] | +0.49 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[MGAT5B]] | +0.49 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[MPV17L]] | +0.48 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[OPRD1]] | +0.48 | +0.40 / +0.29 | both halves | 2e-04 |  |
| [[RNF2]] | +0.48 | +0.39 / +0.53 | both halves | 6e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9A]] | -0.57 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[DYNC2I1]] | -0.54 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[TBCK]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[UMAD1]] | -0.48 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[TOM1L2]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[HECTD4]] | -0.48 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[ANKHD1]] | -0.47 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[UPF2]] | -0.47 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[CCDC18-AS1]] | -0.47 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[PDPK1]] | -0.46 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[NBEAL1]] | -0.46 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[ATF7]] | -0.46 | -0.35 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGAT5B]] | B | MGAT5B activity raises TMSB15B's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 2.12× lower at baseline in the lines without MGAT5B | 0.013 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL |
| [[STK32B]] | B | STK32B activity raises TMSB15B's level | lines that do not express STK32B (24) vs lines expressing it (26) | 1.52× lower at baseline in the lines without STK32B | 0.048 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6 |
| [[CHST10]] | B | CHST10 activity raises TMSB15B's level | lines that do not express CHST10 (12) vs lines expressing it (38) | 2.05× lower at baseline in the lines without CHST10 | 0.062 | ⚠ within organs, on part of the lines; also absent: SNRPN, DNAAF9, ENSG00000268163; its own permutation p |
| [[LHX1-DT]] | B | LHX1-DT activity raises TMSB15B's level | lines that do not express LHX1-DT (28) vs lines expressing it (22) | 1.41× lower at baseline in the lines without LHX1-DT | 0.070 | ⚠ within organs, on part of the lines; also absent: LHX1, EYA4, CDH4 |
| [[ARNT2-DT]] | B | ARNT2-DT activity raises TMSB15B's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 1.46× lower at baseline in the lines without ARNT2-DT | 0.073 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNIP]] | B | TMSB15B activity raises KATNIP's level | lines that do not express TMSB15B (11) vs lines expressing it (39) | 1.20× lower at baseline in the lines without TMSB15B | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000288597, PRKD1, GRIK4 |
| [[RNF2]] | B | TMSB15B activity lowers RNF2's level | lines that do not express TMSB15B (11) vs lines expressing it (39) | 1.27× higher at baseline in the lines without TMSB15B | 0.0997 | ⚠ within organs, on part of the lines; also absent: ENSG00000288597, PRKD1, GRIK4 |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.227). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.9, 30.4); signed map (23.5, 54.3). **Vector** length 41.8, 6.27% of its response variance represented; |z| ≥ 3 in 726 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.3 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.1 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.0 | +1.2 |
|  | [[Ferulic acid (drug)]] 0.5 µM |  | +0.9 | +1.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -0.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | thymosin beta 15B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.2 — chrX:103,918,896-103,966,712 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC39900 |
| Gene groups (HGNC) | Thymosin beta family |
| Matched by | ensembl_id |

**Function**, from UniProt [P0CG35](https://www.uniprot.org/uniprotkb/P0CG35) (Thymosin beta-15B):

> Plays an important role in the organization of the cytoskeleton. Binds to and sequesters actin monomers (G actin) and therefore inhibits actin polymerization (By similarity). May be involved in cell migration.

**Summary**, from NCBI Gene [286527](https://www.ncbi.nlm.nih.gov/gene/286527):

> Predicted to enable actin monomer binding activity and protein sequestering activity. Involved in positive regulation of cell migration. Predicted to be located in cytoskeleton. Predicted to be part of filamentous actin. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28612](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28612) · Entrez [286527](https://www.ncbi.nlm.nih.gov/gene/286527) · UniProt [P0CG35](https://www.uniprot.org/uniprotkb/P0CG35) · Ensembl [ENSG00000158427](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158427)

## Data

Gene col 8160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8160); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8160]; `tensor/DDL_lfc|DDL_z.npy` [8160]; `embed/gene_vectors.npy` [8160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8160 or target_col == 8160). Every well: [[TMSB15B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMSB15B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
