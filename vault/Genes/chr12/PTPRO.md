---
symbol: "PTPRO"
type: "gene"
col: 7527
ensembl_id: "ENSG00000151490"
name: "protein tyrosine phosphatase receptor type O"
location: "12p12.3"
module: 140
arm: "+"
pooled_cpm: 6.69
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# PTPRO

*protein tyrosine phosphatase receptor type O* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.10× (z +18.6, q 0e+00, up in 27 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.697× (z -4.2, q 0.015, down in 10 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNTL6]] (+0.75, fdr 7e-06), [[SGCZ]] (+0.70, fdr 7e-06), [[C8orf34]] (+0.67, fdr 2e-05).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7527.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +18.6 | 0e+00 | 27/34 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.69×** | +11.5 | 3e-28 | 7/19 (SW 900, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.94×** | +10.9 | 2e-25 | 23/44 (NCI-H460, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +8.2 | 3e-14 | 1/9 (HOP62) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +8.0 | 2e-13 | 22/40 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.94×** | +7.7 | 1e-12 | 17/42 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +7.4 | 8e-12 | 2/11 (PANC-1, J82) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +6.4 | 9e-09 | 13/35 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.3 | 8e-06 | 14/38 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +5.2 | 1e-05 | 3/18 (NCI-H460, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.0 | 3e-05 | 10/30 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.3 | 8e-04 | 11/44 (J82, HOP62, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.55×** | +3.6 | 0.012 | 4/32 (HEC-1-A, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.013 | 3/43 (SW48, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.35×** | +3.5 | 0.017 | 8/33 (LS 180, NCI-H460, …) | top dose only |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.027 | 1/44 (NCI-H2347) | inconsistent across doses | position effect removed |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.33×** | +3.0 | 0.080 | 3/33 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.080 | 0/40 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7527.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.697×** | -4.2 | 0.015 | 10/42 (LoVo, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ferulic acid (drug)]] 0.5 µM |  | **0.741×** | -3.5 | 0.073 | 7/42 (A498, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -3.5 | 0.073 | 11/46 (NCI-H1792, SW1417, …) | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.745×** | -3.4 | 0.073 | 6/45 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.05 µM |  | **0.729×** | -3.4 | 0.073 | 6/44 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.743×** | -3.3 | 0.097 | 13/41 (NCI-H1573, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.744× | -3.2 | 0.11 | 6/44 (SK-MEL-2, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 20.3 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -10.5) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.162× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -15.5) |
| [[J82 (line)]] | alt | 11.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +11.8) | — |
| [[C-33 A (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 3.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 2.92 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.48× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.322× (z -8.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SW48 (line)]] | wt | 21.8 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0432× (z -9.8) |
| [[SW480 (line)]] | alt | 1.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.45× (z +9.0) | — |
| [[A-172 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNTL6]] | +0.75 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.70 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[C8orf34]] | +0.67 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[GALNT17]] | +0.67 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[PRDM6]] | +0.66 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[USH2A]] | +0.66 | +0.48 / +0.70 | both halves | 2e-05 | same gene group |
| [[FAT3]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[GRID2]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.65 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[THSD7B]] | +0.65 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SORCS3]] | +0.65 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[MYO3B]] | +0.65 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PTPRO's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.0, 29.4); signed map (33.4, 13.5). **Vector** length 57.9, 8.10% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +18.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +1.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -3.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -4.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type O |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:15,322,257-15,602,175 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTPU2, GLEPP1, PTP-U2, PTP-oc, NPHS6 |
| Gene groups (HGNC) | Fibronectin type III domain containing; Protein tyrosine phosphatases receptor type |
| Reactome | 3 pathways, smallest: Signaling by NTRK3 (TRKC); Signaling by NTRKs; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16827](https://www.uniprot.org/uniprotkb/Q16827) (Receptor-type tyrosine-protein phosphatase O):

> Possesses tyrosine phosphatase activity. Plays a role in regulating the glomerular pressure/filtration rate relationship through an effect on podocyte structure and function (By similarity).

**Summary**, from NCBI Gene [5800](https://www.ncbi.nlm.nih.gov/gene/5800):

> This gene encodes a member of the R3 subtype family of receptor-type protein tyrosine phosphatases. These proteins are localized to the apical surface of polarized cells and may have tissue-specific functions through activation of Src family kinases. This gene contains two distinct promoters, and alternatively spliced transcript variants encoding multiple isoforms have been observed. The encoded proteins may have multiple isoform-specific and tissue-specific functions, including the regulation …

**Accessions** — [HGNC:9678](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9678) · Entrez [5800](https://www.ncbi.nlm.nih.gov/gene/5800) · UniProt [Q16827](https://www.uniprot.org/uniprotkb/Q16827) · Ensembl [ENSG00000151490](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151490)

## Data

Gene col 7527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7527); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7527]; `tensor/DDL_lfc|DDL_z.npy` [7527]; `embed/gene_vectors.npy` [7527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7527 or target_col == 7527). Every well: [[PTPRO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
