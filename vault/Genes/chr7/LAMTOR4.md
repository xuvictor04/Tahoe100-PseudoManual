---
symbol: "LAMTOR4"
type: "gene"
col: 11985
ensembl_id: "ENSG00000188186"
name: "late endosomal/lysosomal adaptor, MAPK and MTOR activator 4"
location: "7q22.1"
module: 24
arm: "+"
pooled_cpm: 25.4
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# LAMTOR4

*late endosomal/lysosomal adaptor, MAPK and MTOR activator 4* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.75× (z +4.8, q 6e-04, up in 29 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.07× (z +3.6, q 0.044, up in 31 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 3.72×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.122×; ⚠ toxic; cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.237×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.209×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAT2]] (+0.76, fdr 7e-06), [[DPM3]] (+0.75, fdr 7e-06), [[MIEN1]] (+0.73, fdr 7e-06); moves opposite to [[EIF4G1]] (-0.65, fdr 7e-06), [[MAPRE1]] (-0.60, fdr 3e-05), [[LRRC59]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NEMP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11985.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 3.72×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.8 | 6e-04 | 29/44 (H4, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +4.7 | 6e-04 | 31/42 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~14% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +4.7 | 6e-04 | 35/46 (NCI-H2347, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.07×** | +3.6 | 0.044 | 31/46 (NCI-H460, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +3.5 | 0.050 | 25/47 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +3.4 | 0.056 | 19/36 (SW480, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~15% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.93×** | +3.3 | 0.093 | 27/48 (NCI-H1792, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.91× | +3.2 | 0.10 | 22/45 (NCI-H1792, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11985.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.122×; ⚠ toxic; cell-cycle shift, explains ~40% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.237×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.209×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.449× | -3.3 | 0.39 | 30/48 (LOX-IMVI, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.701× | -3.2 | 0.39 | 21/47 (MIA PaCa-2, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.122× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~40% of this change |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 14 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAT2]] | +0.76 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[DPM3]] | +0.75 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[MIEN1]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[SNHG25]] | +0.71 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | +0.70 | +0.57 / +0.77 | both halves | 1e-05 |  |
| [[SNHG9]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[ALKBH7]] | +0.66 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[BRI3]] | +0.66 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[ATP5MC2]] | +0.66 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[TOMM7]] | +0.65 | +0.52 / +0.73 | both halves | 1e-05 | pathway: Autophagy |
| [[LAMTOR5]] | +0.65 | +0.46 / +0.75 | both halves | 3e-05 | same gene group; pathway: Amino acids regulate mTORC1; STRING 999 |
| [[UQCC3]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.65 | -0.64 / -0.63 | both halves | 7e-06 | pathway: MTOR signalling |
| [[MAPRE1]] | -0.60 | -0.44 / -0.70 | both halves | 3e-05 |  |
| [[LRRC59]] | -0.59 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[XRCC5]] | -0.59 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.59 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[PUS7L]] | -0.58 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[NOLC1]] | -0.57 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[NCBP1]] | -0.56 | -0.46 / -0.63 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEMP2]] | B | NEMP2 activity lowers LAMTOR4's level | lines that do not express NEMP2 (7) vs lines expressing it (43) | 1.16× higher at baseline in the lines without NEMP2 | 0.094 | ⚠ within organs, on part of the lines; also absent: EML6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.748). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.3, -21.2); signed map (-30.2, 8.4). **Vector** length 77.0, 20.9% of its response variance represented; |z| ≥ 3 in 434 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +3.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +3.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.0 | -2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.3 | +1.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.2 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | late endosomal/lysosomal adaptor, MAPK and MTOR activator 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,148,912-100,155,944 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C7orf59 |
| Gene groups (HGNC) | Ragulator complex |
| Reactome | 15 pathways, smallest: mTORC1-mediated signalling; Energy dependent regulation of mTOR by LKB1-AMPK; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0VGL1](https://www.uniprot.org/uniprotkb/Q0VGL1) (Ragulator complex protein LAMTOR4):

> As part of the Ragulator complex it is involved in amino acid sensing and activation of mTORC1, a signaling complex promoting cell growth in response to growth factors, energy levels, and amino acids. Activated by amino acids through a mechanism involving the lysosomal V-ATPase, the Ragulator plays a dual role for the small GTPases Rag (RagA/RRAGA, RagB/RRAGB, RagC/RRAGC and/or RagD/RRAGD): it (1) acts as a guanine nucleotide exchange factor (GEF), activating the small GTPases Rag and (2) …

**Summary**, from NCBI Gene [389541](https://www.ncbi.nlm.nih.gov/gene/389541):

> Contributes to guanyl-nucleotide exchange factor activity and molecular adaptor activity. Involved in several processes, including cellular response to amino acid stimulus; positive regulation of TORC1 signaling; and protein localization to lysosome. Located in lysosome. Part of FNIP-folliculin RagC/D GAP and Ragulator complex. Is active in lysosomal membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33772) · Entrez [389541](https://www.ncbi.nlm.nih.gov/gene/389541) · UniProt [Q0VGL1](https://www.uniprot.org/uniprotkb/Q0VGL1) · Ensembl [ENSG00000188186](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188186)

## Data

Gene col 11985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11985); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11985]; `tensor/DDL_lfc|DDL_z.npy` [11985]; `embed/gene_vectors.npy` [11985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11985 or target_col == 11985). Every well: [[LAMTOR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMTOR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
