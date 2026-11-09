---
symbol: "STX5-DT"
type: "gene"
col: 15005
ensembl_id: "ENSG00000256690"
name: "STX5 divergent transcript"
location: "11q12.3"
module: 41
arm: "+"
pooled_cpm: 3.03
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# STX5-DT

*STX5 divergent transcript* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.25× (z +17.0, q 0e+00, up in 33 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 0.561× (z -4.1, q 0.014, down in 18 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.0778×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRP54]] (+0.75, fdr 7e-06), [[DNAJC25]] (+0.73, fdr 7e-06), [[STX5]] (+0.71, fdr 7e-06, ⚠ same locus), [[TMEM263]] (+0.70, fdr 7e-06); moves opposite to [[ATIC]] (-0.66, fdr 1e-05), [[TMEM33]] (-0.66, fdr 7e-06), [[INTS7]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15005.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.25×** | +17.0 | 0e+00 | 33/33 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.83×** | +7.0 | 9e-10 | 4/9 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.55×** | +6.8 | 2e-09 | 31/45 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.53×** | +6.7 | 2e-09 | 30/44 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.27×** | +6.0 | 3e-07 | 27/43 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.17×** | +5.6 | 2e-06 | 20/38 (SNU-423, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +5.0 | 6e-05 | 1/7 (HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +4.7 | 2e-04 | 15/27 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +4.5 | 5e-04 | 8/43 (J82, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.028 | 13/33 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +3.3 | 0.044 | 6/18 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +3.2 | 0.076 | 2/15 (SW1417, NCI-H2347) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.082 | 9/30 (SW1417, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15005.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.0778×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.561×** | -4.1 | 0.014 | 18/41 (Hs 766T, RPMI-7951, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.568×** | -4.1 | 0.014 | 18/40 (BT-474, KATO III, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.620× | -3.4 | 0.12 | 14/46 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.637× | -3.2 | 0.18 | 16/43 (C-33 A, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.645× | -3.1 | 0.20 | 10/44 (LoVo, LS 180, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15005. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 4.34 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.08× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0778× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 4.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.64× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 6.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.13× (z +8.8) | — |
| [[J82 (line)]] | alt | 2.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.95× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 3.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 2.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.56× (z +9.0) | — |
| [[SW480 (line)]] | alt | 2.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.33× (z +9.4) | — |
| [[A-172 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15005), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54]] | +0.75 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.73 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[STX5]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 | ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[TMEM263]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[IFT20]] | +0.70 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[DPM1]] | +0.69 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[SELENOK]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[DNAJB9]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[TMEM106A]] | +0.67 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[KDELR1]] | +0.67 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[EOGT-DT]] | +0.67 | +0.60 / +0.71 | both halves | 7e-06 | same gene group |
| [[QPCTL]] | +0.67 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[EAF2]] | +0.67 | +0.71 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATIC]] | -0.66 | -0.54 / -0.73 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.66 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[INTS7]] | -0.64 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.63 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[GFM1]] | -0.63 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[UBE2E3]] | -0.62 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[FARSB]] | -0.62 | -0.50 / -0.74 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.61 | -0.58 / -0.72 | both halves | 7e-06 |  |
| [[ELAC2]] | -0.61 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[IPO9]] | -0.61 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[MRPL42]] | -0.61 | -0.51 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers STX5-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[C5orf63]] | B | C5orf63 activity raises STX5-DT's level | lines that do not express C5orf63 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without C5orf63 | 0.087 | ⚠ within organs, on part of the lines; also absent: TSPAN15, TNFRSF10A, ABCC3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.695). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.8, -39.4); signed map (-48.1, 14.6). **Vector** length 71.3, 13.2% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +17.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +5.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +4.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.3 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -4.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.2 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | STX5 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q12.3 — chr11:62,832,234-62,834,043 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [105369332](https://www.ncbi.nlm.nih.gov/gene/105369332):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:55488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55488) · Entrez [105369332](https://www.ncbi.nlm.nih.gov/gene/105369332) · Ensembl [ENSG00000256690](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256690)

## Data

Gene col 15005: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15005); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15005, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15005]; `tensor/DDL_lfc|DDL_z.npy` [15005]; `embed/gene_vectors.npy` [15005]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15005 or target_col == 15005). Every well: [[STX5-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX5-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
