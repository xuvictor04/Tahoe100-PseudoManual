---
symbol: "SLC9A3"
type: "gene"
col: 821
ensembl_id: "ENSG00000066230"
name: "solute carrier family 9 member A3"
location: "5p15.33"
module: 7
arm: "+"
pooled_cpm: 6.51
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SLC9A3

*solute carrier family 9 member A3* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.77× (z +10.4, q 2e-22, up in 3 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +8.0, q 4e-13, up in 16 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.680× (z -3.9, q 0.058, down in 11 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (LoVo 0.125×; ⚠ cell-cycle shift, explains ~0% of this change); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0541×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLPP6]] (+0.56, fdr 2e-05), [[RAB4A-AS1]] (+0.55, fdr 2e-05), [[SHH]] (+0.54, fdr 1e-05); moves opposite to [[ORC3]] (-0.42, fdr 3e-04), [[ABHD18]] (-0.41, fdr 9e-05), [[STX12]] (-0.40, fdr 4e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HR]] → it (grade B ⚠); 2 go from it, the strongest it → [[PRRC2A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +10.4 | 2e-22 | 3/8 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +8.0 | 4e-13 | 16/32 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.93×** | +7.0 | 5e-10 | 23/42 (SW480, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +6.1 | 1e-07 | 10/43 (A-172, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.5 | 5e-06 | 8/24 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.7 | 0.019 | 9/23 (A-427, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.2 | 0.13 | 3/45 (SW48, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 821.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (LoVo 0.125×; ⚠ cell-cycle shift, explains ~0% of this change); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0541×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.680×** | -3.9 | 0.058 | 11/38 (HCT15, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.716× | -3.6 | 0.11 | 11/40 (KATO III, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 16.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +11.9) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[Hs 766T (line)]] | wt | 6.44 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 54.8× (z +18.5) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[LoVo (line)]] | wt | 8.48 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.125× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 3.25 | 0 | 1 | — | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM 0.0541× (z -9.4) |
| [[SW480 (line)]] | alt | 5.28 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.28× (z +9.7) | — |
| [[A-172 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLPP6]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[RAB4A-AS1]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[SHH]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SFT2D3]] | +0.52 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[FNBP1P1]] | +0.51 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[AGMAT]] | +0.50 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[PHF23]] | +0.49 | +0.37 / +0.50 | both halves | 7e-05 |  |
| [[SLC9A3-AS1]] | +0.49 | +0.49 / +0.46 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TSC22D1]] | +0.49 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[HR]] | +0.48 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[HERPUD2-AS1]] | +0.48 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[LENG9]] | +0.47 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[TMEM251]] | +0.46 | +0.43 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORC3]] | -0.42 | -0.48 / -0.27 | both halves | 3e-04 |  |
| [[ABHD18]] | -0.41 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[STX12]] | -0.40 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[CBLB]] | -0.39 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[SRD5A1]] | -0.39 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[SEC23A]] | -0.39 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[ZCCHC17]] | -0.39 | -0.49 / -0.24 | both halves | 5e-04 |  |
| [[INTS10]] | -0.39 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[ATPAF1]] | -0.39 | -0.36 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HR]] | B | HR activity raises SLC9A3's level | lines that do not express HR (23) vs lines expressing it (27) | 1.73× lower at baseline in the lines without HR | 0.054 | ⚠ within organs, on part of the lines; also absent: SULF2, CEACAM1, HNF1A-AS1 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRRC2A]] | C | SLC9A3 activity lowers PRRC2A's level | lines that do not express SLC9A3 (3) vs lines expressing it (47) | 1.62× higher at baseline in the lines without SLC9A3 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AIFM2, TESK2, HBEGF; maybe low, not absent; its own permutation p |
| [[AMOTL2]] | C | SLC9A3 activity lowers AMOTL2's level | lines that do not express SLC9A3 (3) vs lines expressing it (47) | 3.06× higher at baseline in the lines without SLC9A3 | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AIFM2, TESK2, HBEGF; maybe low, not absent |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.316). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.5, 18.1); signed map (13.2, -11.1). **Vector** length 50.9, 6.60% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.4 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | +2.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.3 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.5 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.5 | -3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 9 member A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:470,456-524,449 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NHE-3; previously NHE3 |
| Gene groups (HGNC) | Solute carrier family 9 |
| Reactome | 4 pathways, smallest: Sodium/Proton exchangers; Metal ion SLC transporters; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P48764](https://www.uniprot.org/uniprotkb/P48764) (Sodium/hydrogen exchanger 3):

> Plasma membrane Na(+)/H(+) antiporter. Exchanges intracellular H(+) ions for extracellular Na(+) in 1:1 stoichiometry, playing a key role in salt and fluid absorption and pH homeostasis (By similarity). Major apical Na(+)/H(+) exchanger in kidney and intestine playing an important role in renal and intestine Na(+) absorption and blood pressure regulation.

**Summary**, from NCBI Gene [6550](https://www.ncbi.nlm.nih.gov/gene/6550):

> The protein encoded by this gene is an epithelial brush border Na/H exchanger that uses an inward sodium ion gradient to expel acids from the cell. Defects in this gene are a cause of congenital secretory sodium diarrhea. Pseudogenes of this gene exist on chromosomes 10 and 22. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:11073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11073) · Entrez [6550](https://www.ncbi.nlm.nih.gov/gene/6550) · UniProt [P48764](https://www.uniprot.org/uniprotkb/P48764) · Ensembl [ENSG00000066230](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066230)

## Data

Gene col 821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 821); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 821]; `tensor/DDL_lfc|DDL_z.npy` [821]; `embed/gene_vectors.npy` [821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 821 or target_col == 821). Every well: [[SLC9A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC9A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
