---
symbol: "IL1RAPL2"
type: "gene"
col: 12091
ensembl_id: "ENSG00000189108"
name: "interleukin 1 receptor accessory protein like 2"
location: "Xq22.3"
module: 90
arm: "+"
pooled_cpm: 6.1
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# IL1RAPL2

*interleukin 1 receptor accessory protein like 2* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.15× (z +23.8, q 0e+00, up in 27 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 0.184×); [[Pemigatinib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0524×); [[Bortezomib (drug)]] 0.05 µM in 1 line (BT-474 0.0980×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCHLAP1]] (+0.79, fdr 7e-06), [[USH2A]] (+0.78, fdr 7e-06), [[CNTNAP5]] (+0.77, fdr 1e-05).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12091.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.15×** | +23.8 | 0e+00 | 27/31 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.32×** | +14.5 | 6e-45 | 3/5 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +11.4 | 6e-28 | 12/15 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.05×** | +11.3 | 1e-27 | 29/42 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +11.1 | 1e-26 | 22/34 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +10.1 | 5e-22 | 5/7 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +8.4 | 4e-15 | 25/44 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +6.8 | 7e-10 | 13/44 (SW480, J82, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +5.8 | 5e-07 | 11/27 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +5.0 | 3e-05 | 14/39 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +4.8 | 9e-05 | 12/34 (KATO III, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.002 | 6/33 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.0 | 0.003 | 4/15 (A498, NCI-H1573, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.7 | 0.008 | 8/33 (LOX-IMVI, LS 180, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.010 | 7/38 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +3.5 | 0.015 | 1/28 (HS-578T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.051 | 8/44 (RKO, AN3 CA, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12091.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 0.184×); [[Pemigatinib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0524×); [[Bortezomib (drug)]] 0.05 µM in 1 line (BT-474 0.0980×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ranolazine (drug)]] 0.5 µM |  | 0.703× | -3.6 | 0.18 | 9/43 (RKO, COLO 205, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.719× | -3.2 | 0.35 | 5/40 (NCI-H2030, A549, …) | top dose only |  |
| [[Sinomenine (drug)]] 0.5 µM |  | 0.739× | -3.1 | 0.43 | 3/44 (SNU-1, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 214 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 2.13 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.06× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 2.25 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.06× (z +9.1) | [[Pemigatinib (drug)]] 0.05 µM 0.0524× (z -9.9) |
| [[SW480 (line)]] | alt | 2.38 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.98× (z +13.0) | — |
| [[A498 (line)]] | wt | 2.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.90× (z +8.9) | — |
| [[A549 (line)]] | wt | 1.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 2.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.78× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 1.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +9.7) | — |
| [[A-172 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCHLAP1]] | +0.79 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[USH2A]] | +0.78 | +0.69 / +0.83 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.77 | +0.56 / +0.83 | both halves | 1e-05 |  |
| [[PTPRT]] | +0.73 | +0.51 / +0.82 | both halves | 1e-05 | same gene group |
| [[PWRN1]] | +0.73 | +0.66 / +0.81 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.71 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[TTN]] | +0.70 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[MIR4300HG]] | +0.70 | +0.57 / +0.76 | both halves | 1e-05 |  |
| [[RELN]] | +0.69 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.69 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[C8orf34]] | +0.69 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[LINC00861]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IL1RAPL2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.4, 29.2); signed map (32.9, 14.2). **Vector** length 51.8, 6.44% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +23.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -0.2 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -1.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 1 receptor accessory protein like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:104,566,199-105,767,829 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IL-1R9, TIGIRR-1, IL1RAPL-2, IL1R9 |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Interleukin receptors; TIR domain containing |
| Reactome | 3 pathways, smallest: Receptor-type tyrosine-protein phosphatases; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

UniProt [Q9NP60](https://www.uniprot.org/uniprotkb/Q9NP60) carries no function annotation.

**Summary**, from NCBI Gene [26280](https://www.ncbi.nlm.nih.gov/gene/26280):

> The protein encoded by this gene is a member of the interleukin 1 receptor family. This protein is similar to the interleukin 1 accessory proteins, and is most closely related to interleukin 1 receptor accessory protein-like 1 (IL1RAPL1). This gene and IL1RAPL1 are located at a region on chromosome X that is associated with X-linked non-syndromic cognitive disability. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5997) · Entrez [26280](https://www.ncbi.nlm.nih.gov/gene/26280) · UniProt [Q9NP60](https://www.uniprot.org/uniprotkb/Q9NP60) · Ensembl [ENSG00000189108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189108)

## Data

Gene col 12091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12091); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12091]; `tensor/DDL_lfc|DDL_z.npy` [12091]; `embed/gene_vectors.npy` [12091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12091 or target_col == 12091). Every well: [[IL1RAPL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL1RAPL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
