---
symbol: "GNAS-AS1"
type: "gene"
col: 14027
ensembl_id: "ENSG00000235590"
name: "GNAS antisense RNA 1"
location: "20q13.32"
module: 40
arm: "+"
pooled_cpm: 7.2
n_lines_expressing: 29
n_dd_up: 1
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# GNAS-AS1

*GNAS antisense RNA 1* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 2.95× (z +10.2, q 1e-21, up in 21 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 2 lines (SK-MEL-2 4.71×, NCI-H23 3.41×).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.439× (z -10.9, q 5e-25, down in 21 of 24 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.303× (z -10.8, q 1e-24, down in 21 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02693]] (+0.61, fdr 1e-05), [[XPNPEP3]] (+0.61, fdr 3e-05), [[TOP3A]] (+0.60, fdr 1e-05); moves opposite to [[ELF1]] (-0.61, fdr 1e-05), [[CD2AP]] (-0.50, fdr 1e-04), [[BAMBI]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[DENND3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14027.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 2 lines (SK-MEL-2 4.71×, NCI-H23 3.41×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.95×** | +10.2 | 1e-21 | 21/24 (SK-MEL-2, NCI-H23, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14027.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.439×** | -10.9 | 5e-25 | 21/24 (HS-578T, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.303×** | -10.8 | 1e-24 | 21/25 (RPMI-7951, A498, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.452×** | -7.5 | 2e-11 | 18/27 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.559×** | -5.4 | 7e-06 | 16/21 (NCI-H1573, SK-MEL-2, …) | all doses, flat | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.571×** | -5.3 | 2e-05 | 10/27 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.609×** | -4.6 | 3e-04 | 16/25 (HS-578T, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -4.0 | 0.006 | 15/25 (SK-MEL-2, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | 0.720× | -3.1 | 0.15 | 9/24 (SW1417, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 25.9 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0435× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.132× (z -12.0) |
| [[A498 (line)]] | wt | 20.7 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0912× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -12.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.164× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 33.9 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 4.71× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -10.0) |
| [[A-172 (line)]] | wt | 6.81 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0861× (z -10.9) |
| [[H4 (line)]] | wt | 30.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -12.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0556× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 17.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0998× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.177× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 16.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.161× (z -9.9) |
| [[COLO 205 (line)]] | alt | 8.89 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0420× (z -10.9) |
| [[HOP62 (line)]] | alt | 7.22 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[NCI-H23 (line)]] | alt | 42.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.41× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0224× (z -14.7) |
| [[SW1417 (line)]] | alt | 4.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0955× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[A-427 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.980 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02693]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[XPNPEP3]] | +0.61 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[TOP3A]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[ZNF587]] | +0.59 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[RNF216P1]] | +0.58 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ARFGAP1]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[NT5DC2]] | +0.58 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[EIF1AD]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[MOGS]] | +0.57 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[GPR107]] | +0.57 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[DPH7]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[DCUN1D2]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELF1]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[CD2AP]] | -0.50 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[BAMBI]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[BAZ2B]] | -0.49 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[THG1L]] | -0.49 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[DENND3-AS1]] | -0.49 | -0.52 / -0.39 | both halves | 5e-05 | same gene group |
| [[NUTM2E]] | -0.48 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[TMEM47]] | -0.48 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[AGL]] | -0.48 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[CEBPD]] | -0.48 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[TRAM2-AS1]] | -0.48 | -0.64 / -0.32 | both halves | 2e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DENND3-AS1]] | B | GNAS-AS1 activity lowers DENND3-AS1's level | lines that do not express GNAS-AS1 (21) vs lines expressing it (29) | 1.18× higher at baseline in the lines without GNAS-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: FAP, PTPRD, EGF |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (20.2, -31.2); signed map (-47.9, 3.1). **Vector** length 54.8, 11.2% of its response variance represented; |z| ≥ 3 in 611 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +10.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.3 | +0.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.3 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | +0.8 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +0.7 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +0.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.4 | -10.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -10.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.3 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -7.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.9 | -0.4 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | GNAS antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q13.32 — chr20:58,818,918-58,850,903 (-) |
| Ensembl biotype | lncRNA |
| Also known as | SANG, NESP-AS, NESPAS, GNAS1AS, NCRNA00075; previously GNASAS, GNAS-AS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [149775](https://www.ncbi.nlm.nih.gov/gene/149775):

> This gene produces a paternally-imprinted antisense RNA transcript that helps regulate the GNAS complex locus, which encodes the alpha subunit of the stimulatory G protein. Defects in this gene are a cause of pseudohypoparathyroidism type Ib.[provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:24872](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24872) · Entrez [149775](https://www.ncbi.nlm.nih.gov/gene/149775) · Ensembl [ENSG00000235590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235590)

## Data

Gene col 14027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14027); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14027]; `tensor/DDL_lfc|DDL_z.npy` [14027]; `embed/gene_vectors.npy` [14027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14027 or target_col == 14027). Every well: [[GNAS-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNAS-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
