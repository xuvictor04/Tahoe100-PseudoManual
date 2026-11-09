---
symbol: "SLC23A1"
type: "gene"
col: 9961
ensembl_id: "ENSG00000170482"
name: "solute carrier family 23 member 1"
location: "5q31.2"
module: 21
arm: "+"
pooled_cpm: 2.07
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SLC23A1

*solute carrier family 23 member 1* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.94× (z +12.7, q 6e-34, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.98× (z +9.3, q 3e-18, up in 19 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW480 0.108×); [[Phenylephrine (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.0558×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHMP3-AS1]] (+0.85, fdr 7e-06), [[PKD2L2]] (+0.83, fdr 7e-06), [[SLC3A1]] (+0.82, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[AMBP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.94×** | +12.7 | 6e-34 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.33×** | +11.5 | 2e-28 | 6/10 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +9.3 | 3e-18 | 19/31 (A549, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.07×** | +8.6 | 1e-15 | 1/4 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +6.6 | 3e-09 | 14/34 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +5.2 | 2e-05 | 6/24 (LoVo, AsPC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +4.8 | 1e-04 | 1/10 (A549) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +4.4 | 6e-04 | 3/10 (A498, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.37×** | +4.3 | 9e-04 | 1/5 (LoVo) | top dose only | noisy plate (z scaled); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.67×** | +3.5 | 0.026 | 1/3 (SW480) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.058 | 2/26 (MIA PaCa-2, PANC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.058 | 8/45 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.2 | 0.060 | 4/25 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.1 | 0.074 | 3/30 (A-427, Panc 03.27, …) | top dose only | position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.38×** | +3.1 | 0.074 | 6/30 (HEC-1-A, SW480, …) | inconsistent across doses | position effect removed |
| [[Zileuton (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.074 | 0/43 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9961.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SW480 0.108×); [[Phenylephrine (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.0558×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.839× | -6.1 | 8e-07 | 19/46 (C-33 A, HT-29, …) | inconsistent across doses |  |
| [[Rimonabant (drug)]] 5 µM |  | 0.793× | -3.1 | 0.40 | 7/44 (HT-29, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 2.10 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 0.0558× (z -8.5) |
| [[SW480 (line)]] | alt | 1.99 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.108× (z -8.8) |
| [[A-172 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP3-AS1]] | +0.85 | +0.71 / +0.83 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.83 | +0.65 / +0.84 | both halves | 7e-06 |  |
| [[SLC3A1]] | +0.82 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.82 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.82 | +0.73 / +0.81 | both halves | 7e-06 |  |
| [[PP2D1]] | +0.82 | +0.71 / +0.80 | both halves | 7e-06 |  |
| [[TOMM20L-DT]] | +0.80 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[A2ML1-AS1]] | +0.80 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.80 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[FLJ40194]] | +0.79 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.79 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[LRRC37A16P]] | +0.79 | +0.64 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMBP]] | B | AMBP activity raises SLC23A1's level | lines that do not express AMBP (41) vs lines expressing it (9) | 1.12× lower at baseline in the lines without AMBP | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2 |
| [[KLRD1]] | B | KLRD1 activity raises SLC23A1's level | lines that do not express KLRD1 (8) vs lines expressing it (42) | 1.10× lower at baseline in the lines without KLRD1 | 0.072 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RASGEF1B]] | B | RASGEF1B activity raises SLC23A1's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 1.10× lower at baseline in the lines without RASGEF1B | 0.073 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.874). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, 27.3); signed map (33.0, 5.5). **Vector** length 29.9, 2.40% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -2.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -6.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 23 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:139,367,196-139,384,553 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YSPL3, SVCT1; previously SLC23A2 |
| Gene groups (HGNC) | Solute carrier family 23 |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 3 pathways, smallest: Vitamin C (ascorbate) metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHI7](https://www.uniprot.org/uniprotkb/Q9UHI7) (Solute carrier family 23 member 1):

> Sodium:ascorbate cotransporter. Mediates electrogenic uptake of vitamin C, with a stoichiometry of 2 Na(+) for each ascorbate. Has retained some ancestral activity toward nucleobases such as urate, an oxidized purine. Low-affinity high-capacity sodium:urate cotransporter, may regulate serum urate levels by serving as a renal urate re-absorber.; [Isoform 2]: Inactive transporter.

**Summary**, from NCBI Gene [9963](https://www.ncbi.nlm.nih.gov/gene/9963):

> The absorption of vitamin C into the body and its distribution to organs requires two sodium-dependent vitamin C transporters. This gene encodes one of the two transporters. The encoded protein is active in bulk vitamin C transport involving epithelial surfaces. Previously, this gene had an official symbol of SLC23A2. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:10974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10974) · Entrez [9963](https://www.ncbi.nlm.nih.gov/gene/9963) · UniProt [Q9UHI7](https://www.uniprot.org/uniprotkb/Q9UHI7) · Ensembl [ENSG00000170482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170482)

## Data

Gene col 9961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9961); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9961]; `tensor/DDL_lfc|DDL_z.npy` [9961]; `embed/gene_vectors.npy` [9961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9961 or target_col == 9961). Every well: [[SLC23A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC23A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
