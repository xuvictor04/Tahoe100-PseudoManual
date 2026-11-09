---
symbol: "JMJD8"
type: "gene"
col: 8470
ensembl_id: "ENSG00000161999"
name: "jumonji domain containing 8"
location: "16p13.3"
module: 29
arm: "+"
pooled_cpm: 3.92
n_lines_expressing: 47
n_dd_up: 7
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# JMJD8

*jumonji domain containing 8* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.82× (z +15.1, q 0e+00, up in 21 of 21 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 5.27×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 5.15×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.601× (z -4.2, q 0.016, down in 16 of 35 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC37A4]] (+0.57, fdr 1e-05), [[LRRC45]] (+0.57, fdr 1e-05), [[ARSA]] (+0.56, fdr 3e-05); moves opposite to [[ATG12]] (-0.50, fdr 4e-05), [[EIF1]] (-0.46, fdr 1e-04), [[NOXRED1]] (-0.43, fdr 2e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC39A4]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PCYOX1L]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8470.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 5.27×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 5.15×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.82×** | +15.1 | 0e+00 | 21/21 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.70×** | +12.8 | 5e-35 | 6/6 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.38×** | +11.7 | 2e-29 | 9/10 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +5.6 | 4e-06 | 6/19 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.76×** | +4.9 | 1e-04 | 10/21 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.67×** | +4.2 | 0.002 | 11/27 (A498, NCI-H1573, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.36×** | +3.8 | 0.013 | 9/41 (SW1417, SHP-77, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.43× | +3.1 | 0.14 | 4/42 (PANC-1, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.601×** | -4.2 | 0.016 | 16/35 (SW48, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.624×** | -4.0 | 0.016 | 14/39 (A498, RPMI-7951, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.659×** | -3.6 | 0.067 | 10/33 (SW48, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.686× | -3.2 | 0.14 | 9/39 (HS-578T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.671× | -3.2 | 0.14 | 10/36 (J82, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.701× | -3.0 | 0.23 | 12/41 (NCI-H23, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.63 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 4.23 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0570× (z -8.7) |
| [[J82 (line)]] | alt | 6.99 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 5.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 3.68 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.05 µM 0.0556× (z -8.6) |
| [[SHP-77 (line)]] | alt | 7.02 | 0 | 1 | — | [[vincristine (drug)]] 0.05 µM 0.0708× (z -9.0) |
| [[SW1417 (line)]] | alt | 5.02 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.926 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC37A4]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[LRRC45]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ARSA]] | +0.56 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[MLST8]] | +0.56 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[UCP2]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[CDK5]] | +0.55 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[CELSR2]] | +0.54 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[HYAL2]] | +0.53 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[SNRNP25]] | +0.53 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[GSTM4]] | +0.53 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[NME4]] | +0.52 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[PODXL2]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG12]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[EIF1]] | -0.46 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[NOXRED1]] | -0.43 | -0.39 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC39A4]] | B | SLC39A4 activity raises JMJD8's level | lines that do not express SLC39A4 (6) vs lines expressing it (44) | 2.01× lower at baseline in the lines without SLC39A4 | 0.026 | ⚠ within organs, on part of the lines; also absent: LRRC8B |
| [[MEST]] | B | MEST activity raises JMJD8's level | lines that do not express MEST (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without MEST | 0.087 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCYOX1L]] | C | JMJD8 activity lowers PCYOX1L's level | lines that do not express JMJD8 (3) vs lines expressing it (47) | 1.96× higher at baseline in the lines without JMJD8 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PIM2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.368). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.8, -42.7); signed map (-32.5, -38.7). **Vector** length 42.1, 5.21% of its response variance represented; |z| ≥ 3 in 706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +11.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | +3.2 | +4.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | +2.1 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +2.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.5 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[Ciclopirox (drug)]] 5 µM |  | -1.1 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | jumonji domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:681,670-684,528 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C16orf20 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S16](https://www.uniprot.org/uniprotkb/Q96S16) (JmjC domain-containing protein 8):

> Functions as a positive regulator of TNF-induced NF-kappa-B signaling. Regulates angiogenesis and cellular metabolism through interaction with PKM.

**Summary**, from NCBI Gene [339123](https://www.ncbi.nlm.nih.gov/gene/339123):

> Predicted to enable cis-regulatory region sequence-specific DNA binding activity. Involved in several processes, including positive regulation of canonical NF-kappaB signal transduction; positive regulation of sprouting angiogenesis; and regulation of pyruvate kinase activity. Located in endoplasmic reticulum lumen and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14148) · Entrez [339123](https://www.ncbi.nlm.nih.gov/gene/339123) · UniProt [Q96S16](https://www.uniprot.org/uniprotkb/Q96S16) · Ensembl [ENSG00000161999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161999)

## Data

Gene col 8470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8470); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8470]; `tensor/DDL_lfc|DDL_z.npy` [8470]; `embed/gene_vectors.npy` [8470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8470 or target_col == 8470). Every well: [[JMJD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JMJD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
