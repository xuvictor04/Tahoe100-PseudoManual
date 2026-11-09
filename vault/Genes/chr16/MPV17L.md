---
symbol: "MPV17L"
type: "gene"
col: 8029
ensembl_id: "ENSG00000156968"
name: "MPV17 mitochondrial inner membrane protein like"
location: "16p13.11"
module: 33
arm: "+"
pooled_cpm: 2.45
n_lines_expressing: 24
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# MPV17L

*MPV17 mitochondrial inner membrane protein like* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.06× (z +12.9, q 2e-35, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.87× (z +6.6, q 7e-09, up in 11 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.149×, LoVo 0.223×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.102×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SNU-1 0.0615×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adenine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0620×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CGREF1]] (+0.63, fdr 1e-05), [[CNNM1]] (+0.62, fdr 1e-05), [[ALDH5A1]] (+0.59, fdr 1e-05); moves opposite to [[UPF2]] (-0.54, fdr 2e-05), [[C6orf62]] (-0.53, fdr 3e-05), [[TRNAU1AP]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ZP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8029.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.06×** | +12.9 | 2e-35 | 3/3 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.58×** | +12.8 | 3e-35 | 10/11 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.45×** | +8.5 | 3e-15 | 5/6 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.87×** | +6.6 | 7e-09 | 11/19 (NCI-H1792, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +6.3 | 4e-08 | 11/19 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.08×** | +5.4 | 5e-06 | 1/9 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.56×** | +5.0 | 5e-05 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.5 | 5e-04 | 2/18 (A-427, AsPC-1) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.9 | 0.006 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.88×** | +3.4 | 0.043 | 1/12 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +3.3 | 0.049 | 1/8 (CFPAC-1) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8029.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.149×, LoVo 0.223×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.102×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SNU-1 0.0615×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adenine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0620×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clopidogrel (drug)]] 0.5 µM |  | 0.612× | -3.7 | 0.12 | 1/19 (CFPAC-1) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.882× | -3.5 | 0.12 | 5/20 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.643× | -3.3 | 0.16 | 6/19 (NCI-H2347, A-427, …) | inconsistent across doses | position effect removed |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.647× | -3.3 | 0.16 | 2/19 (NCI-H2347, J82) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.647× | -3.0 | 0.29 | 1/19 (MIA PaCa-2) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 19.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -17.5) |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0615× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 2.99 | 0 | 1 | — | [[Adenine (drug)]] 0.5 µM 0.0620× (z -8.8) |
| [[LoVo (line)]] | wt | 7.68 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.274 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.451 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.846 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.944 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.614 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.235 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGREF1]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[CNNM1]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ALDH5A1]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ASIC1]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[FXN]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ASB13]] | +0.56 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[MCOLN2]] | +0.55 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[TMEM177]] | +0.54 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[CHST10]] | +0.54 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[MRPL3]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[MERTK]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[FZD4]] | +0.53 | +0.50 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UPF2]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[C6orf62]] | -0.53 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[TRNAU1AP]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[LINC00310]] | -0.52 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[ZKSCAN1]] | -0.49 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[SHOC2]] | -0.49 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[GPS2]] | -0.49 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[CFAP53]] | -0.48 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[ARL17B]] | -0.48 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[DNASE1]] | -0.47 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[ZNF335]] | -0.47 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[LINC02936]] | -0.47 | -0.38 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZP3]] | B | MPV17L activity raises ZP3's level | lines that do not express MPV17L (26) vs lines expressing it (24) | 1.41× lower at baseline in the lines without MPV17L | 0.036 | ⚠ within organs, on part of the lines; also absent: THBD, NR2E3, CYP24A1 |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-0.4, 42.2); signed map (-6.7, -58.2). **Vector** length 35.2, 6.52% of its response variance represented; |z| ≥ 3 in 432 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +8.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.2 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.8 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.8 | +1.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -3.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | +0.3 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.9 | -0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -0.8 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | MPV17 mitochondrial inner membrane protein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:15,395,754-15,413,271 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39599, M-LPH, M-LPH1, M-LPH2, MPV17L1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2QL34](https://www.uniprot.org/uniprotkb/Q2QL34) (Mpv17-like protein):

> [Isoform 1]: Participates in reactive oxygen species metabolism by up- or down-regulation of the genes of antioxidant enzymes. Protective against the mitochondrial apoptotic cascade.

**Summary**, from NCBI Gene [255027](https://www.ncbi.nlm.nih.gov/gene/255027):

> Involved in negative regulation of hydrogen peroxide biosynthetic process; negative regulation of mitochondrial outer membrane permeabilization involved in apoptotic signaling pathway; and reactive oxygen species metabolic process. Located in peroxisome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26827](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26827) · Entrez [255027](https://www.ncbi.nlm.nih.gov/gene/255027) · UniProt [Q2QL34](https://www.uniprot.org/uniprotkb/Q2QL34) · Ensembl [ENSG00000156968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156968)

## Data

Gene col 8029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8029); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8029]; `tensor/DDL_lfc|DDL_z.npy` [8029]; `embed/gene_vectors.npy` [8029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8029 or target_col == 8029). Every well: [[MPV17L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPV17L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
