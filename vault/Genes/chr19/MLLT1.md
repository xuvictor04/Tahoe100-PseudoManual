---
symbol: "MLLT1"
type: "gene"
col: 5060
ensembl_id: "ENSG00000130382"
name: "MLLT1 super elongation complex subunit"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 19.13
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MLLT1

*MLLT1 super elongation complex subunit* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.94× (z +9.5, q 2e-18, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.644× (z -7.4, q 7e-11, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTBP1]] (+0.67, fdr 1e-05), [[SETD1A]] (+0.67, fdr 7e-06), [[PCNX3]] (+0.65, fdr 7e-06); moves opposite to [[H3-3B]] (-0.49, fdr 4e-05), [[BTG1]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → cells under [[SBI-0640756 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5060.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.94×** | +9.5 | 2e-18 | 41/48 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +4.6 | 0.001 | 18/45 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +4.0 | 0.015 | 15/45 (SHP-77, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.8 | 0.016 | 15/47 (NCI-H2030, LoVo, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.016 | 13/48 (A498, SHP-77, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.030 | 11/47 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.030 | 9/47 (NCI-H460, SHP-77, …) | all doses, flat |  |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.18 | 12/47 (Hs 766T, HS-578T, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5060.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.644×** | -7.4 | 7e-11 | 30/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.709×** | -5.8 | 2e-06 | 25/47 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.794×** | -3.9 | 0.019 | 18/47 (C32, SK-MEL-2, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.782×** | -3.6 | 0.039 | 16/45 (A-172, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.666×** | -3.6 | 0.039 | 14/39 (Hs 766T, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.785×** | -3.5 | 0.041 | 15/48 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.798×** | -3.3 | 0.085 | 9/47 (SW48, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5060. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 75.5 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0767× (z -9.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.227× (z -10.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 23.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.398× (z -9.6) |
| [[A549 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[AsPC-1 (line)]] | alt | 10.4 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0972× (z -11.5) |
| [[C-33 A (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0927× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[COLO 205 (line)]] | alt | 17.9 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.5 µM 0.190× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[SNU-1 (line)]] | wt | 20.8 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.169× (z -8.7) |
| [[SNU-423 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.182× (z -11.4) ⚠ toxic |
| [[SW48 (line)]] | wt | 21.6 | 0 | 1 | — | [[Arbutin (drug)]] 5 µM 0.112× (z -9.1) |
| [[SW480 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5060), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTBP1]] | +0.67 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[SETD1A]] | +0.67 | +0.77 / +0.58 | both halves | 7e-06 | STRING 441 |
| [[PCNX3]] | +0.65 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[NOP9]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[TUBGCP6]] | +0.64 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[MTA1]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[UPF1]] | +0.63 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[CPSF1]] | +0.63 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ANAPC2]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[ZNF865]] | +0.59 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[TBC1D10B]] | +0.59 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[E2F4]] | +0.58 | +0.55 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H3-3B]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 | STRING 811 |
| [[BTG1]] | -0.49 | -0.40 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[SBI-0640756 (drug)]] 5 µM | C | MLLT1's natural level raises the cells' numbers under SBI-0640756 5 µM (protects the cells) | MLLT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.73 | 0.186 over the table, 0.008 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[palbociclib (drug)]] 5 µM | C | MLLT1's natural level lowers the cells' numbers under palbociclib 5 µM (makes them more sensitive) | MLLT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.361 over the table, 0.070 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | MLLT1's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | MLLT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.58 | 0.491 over the table, 0.086 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-17.5, -26.4); signed map (-13.1, -31.2). **Vector** length 74.3, 12.9% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.0 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.5 | +1.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.2 | +4.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.1 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.0 | +3.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.4 | -3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | MLLT1 super elongation complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:6,210,381-6,279,975 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ENL, LTG19, YEATS1 |
| Gene groups (HGNC) | Super elongation complex; YEATS domain containing |
| Reactome | 7 pathways, smallest: Formation of RNA Pol II elongation complex; RNA Polymerase II Transcription Elongation; RNA Polymerase II Pre-transcription Events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03111](https://www.uniprot.org/uniprotkb/Q03111) (Protein ENL):

> Chromatin reader component of the super elongation complex (SEC), a complex required to increase the catalytic rate of RNA polymerase II transcription by suppressing transient pausing by the polymerase at multiple sites along the DNA. Specifically recognizes and binds acetylated and crotonylated histones, with a preference for histones that are crotonylated. Has a slightly higher affinity for binding histone H3 crotonylated at 'Lys-27' (H3K27cr) than 'Lys-20' (H3K9cr20). May play a role in …

**Summary**, from NCBI Gene [4298](https://www.ncbi.nlm.nih.gov/gene/4298):

> Predicted to enable chromatin binding activity. Predicted to be involved in positive regulation of DNA-templated transcription. Predicted to act upstream of or within negative regulation of protein kinase activity. Located in fibrillar center and nucleoplasm. Part of transcription elongation factor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7134](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7134) · Entrez [4298](https://www.ncbi.nlm.nih.gov/gene/4298) · UniProt [Q03111](https://www.uniprot.org/uniprotkb/Q03111) · Ensembl [ENSG00000130382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130382)

## Data

Gene col 5060: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5060); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5060, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5060]; `tensor/DDL_lfc|DDL_z.npy` [5060]; `embed/gene_vectors.npy` [5060]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5060 or target_col == 5060). Every well: [[MLLT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLLT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
