---
symbol: "RTL8A"
type: "gene"
col: 12803
ensembl_id: "ENSG00000203950"
name: "retrotransposon Gag like 8A"
location: "Xq26.3"
module: 54
arm: "+"
pooled_cpm: 14.44
n_lines_expressing: 42
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# RTL8A

*retrotransposon Gag like 8A* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.73× (z +4.4, q 0.005, up in 18 of 27 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.262× (z -15.8, q 0e+00, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTF1]] (+0.61, fdr 3e-05), [[MRPL55]] (+0.60, fdr 2e-05), [[A1BG]] (+0.59, fdr 1e-05); moves opposite to [[ELK4]] (-0.51, fdr 6e-05), [[LYRM1]] (-0.51, fdr 3e-05), [[MCM7]] (-0.49, fdr 2e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RTL8C]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12803.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +4.4 | 0.005 | 18/27 (A-172, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +4.3 | 0.005 | 22/32 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.57×** | +3.7 | 0.035 | 22/36 (PANC-1, H4, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.50× | +3.2 | 0.18 | 15/35 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12803.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.262×** | -15.8 | 0e+00 | 37/39 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.437×** | -6.9 | 1e-09 | 34/40 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.439×** | -6.9 | 1e-09 | 32/38 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.448×** | -6.4 | 2e-08 | 31/39 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.501×** | -5.8 | 9e-07 | 30/39 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.531×** | -5.0 | 5e-05 | 29/39 (C32, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.556×** | -4.9 | 8e-05 | 26/39 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.567×** | -4.7 | 2e-04 | 22/39 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.640×** | -3.7 | 0.012 | 24/39 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.632×** | -3.5 | 0.022 | 18/39 (C32, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.669×** | -3.4 | 0.040 | 21/40 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.663×** | -3.2 | 0.070 | 13/39 (NCI-H1573, J82, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.695× | -3.0 | 0.10 | 18/38 (SW 900, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -16.8) |
| [[A-427 (line)]] | wt | 38.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -14.0) |
| [[LoVo (line)]] | wt | 4.17 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0520× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 9.49 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 29.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0567× (z -24.2) |
| [[PANC-1 (line)]] | alt | 31.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -14.1) |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -12.5) |
| [[A-172 (line)]] | wt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -9.4) |
| [[C32 (line)]] | wt | 10.1 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.114× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.8) |
| [[H4 (line)]] | wt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -12.9) |
| [[HOP62 (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -10.9) |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0709× (z -19.1) |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -9.4) |
| [[J82 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0931× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -13.7) |
| [[SNU-423 (line)]] | alt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.2) |
| [[A498 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.881 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.882 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.852 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.720 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 9 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTF1]] | +0.61 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[MRPL55]] | +0.60 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[A1BG]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[RBBP5]] | +0.57 | +0.28 / +0.47 | both halves | 3e-04 |  |
| [[POP7]] | +0.56 | +0.31 / +0.63 | both halves | 2e-04 |  |
| [[ATG4B]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[GAS2L1]] | +0.56 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[OCEL1]] | +0.56 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[NCBP2AS2]] | +0.56 | +0.32 / +0.69 | both halves | 1e-04 |  |
| [[SDHAF1]] | +0.56 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[C1orf35]] | +0.56 | +0.36 / +0.65 | both halves | 1e-04 |  |
| [[ARSK]] | +0.56 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK4]] | -0.51 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[LYRM1]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[MCM7]] | -0.49 | -0.29 / -0.53 | both halves | 2e-04 |  |
| [[NOTCH2NLC]] | -0.48 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[SRSF1]] | -0.47 | -0.35 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RTL8C]] | C | RTL8C activity raises RTL8A's level | lines that do not express RTL8C (9) vs lines expressing it (41) | 5.64× lower at baseline in the lines without RTL8C | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000286964, RTL8A, EHD3; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.5, -13.1); signed map (-30.1, 12.2). **Vector** length 53.4, 11.3% of its response variance represented; |z| ≥ 3 in 563 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +3.2 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.6 | +0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.1 | +1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.9 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -2.9 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | -0.8 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.7 | -1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -0.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | retrotransposon Gag like 8A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:135,050,932-135,052,196 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564B147, MAR8A, CXX1b, SIRH6; previously FAM127B |
| Gene groups (HGNC) | Retrotransposon Gag like family |
| Matched by | ensembl_id |

UniProt [Q9BWD3](https://www.uniprot.org/uniprotkb/Q9BWD3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:24514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24514) · Entrez [26071](https://www.ncbi.nlm.nih.gov/gene/26071) · UniProt [Q9BWD3](https://www.uniprot.org/uniprotkb/Q9BWD3) · Ensembl [ENSG00000203950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203950)

## Data

Gene col 12803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12803); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12803]; `tensor/DDL_lfc|DDL_z.npy` [12803]; `embed/gene_vectors.npy` [12803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12803 or target_col == 12803). Every well: [[RTL8A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTL8A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
