---
symbol: "DDA1"
type: "gene"
col: 5050
ensembl_id: "ENSG00000130311"
name: "DET1 and DDB1 associated 1"
location: "19p13.11"
module: 2
arm: "+"
pooled_cpm: 18.9
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# DDA1

*DET1 and DDB1 associated 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +9.3, q 5e-18, up in 32 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.84× (z +8.6, q 2e-15, up in 35 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHKBP1]] (+0.59, fdr 7e-06), [[SAMD4B]] (+0.57, fdr 2e-05), [[PNPLA6]] (+0.56, fdr 4e-05); moves opposite to [[NCL]] (-0.52, fdr 7e-05), [[TFAM]] (-0.49, fdr 4e-05), [[SLC12A2-DT]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF516]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5050.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.94×** | +9.3 | 5e-18 | 32/38 (Panc 03.27, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.97×** | +9.2 | 9e-18 | 28/33 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +8.6 | 2e-15 | 35/47 (C32, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +6.9 | 9e-10 | 32/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +6.7 | 2e-09 | 27/41 (SW1417, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.58×** | +6.4 | 1e-08 | 33/46 (SW480, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +6.4 | 1e-08 | 31/47 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.61×** | +6.3 | 2e-08 | 30/47 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.56×** | +6.2 | 3e-08 | 28/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.57×** | +6.1 | 6e-08 | 24/42 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.33×** | +5.6 | 1e-06 | 24/47 (A-172, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +5.5 | 2e-06 | 23/48 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~25% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +5.0 | 3e-05 | 28/48 (PANC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.42×** | +4.9 | 3e-05 | 20/44 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.50×** | +4.5 | 2e-04 | 20/36 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 0.001 | 13/45 (MIA PaCa-2, NCI-H1792, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.005 | 17/45 (HOP62, SW480, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.029 | 12/48 (LS 180, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.34×** | +2.9 | 0.080 | 13/43 (HS-578T, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5050.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.859× | -3.1 | 0.51 | 9/48 (NCI-H1792, Hs 766T, …) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 0.05 µM |  | 0.811× | -3.0 | 0.51 | 5/48 (RPMI-7951, NCI-H2030, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5050. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 27.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +8.5) ⚠ cell-cycle shift, explains ~86% of this change | — |
| [[PANC-1 (line)]] | alt | 12.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5050), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHKBP1]] | +0.59 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[SAMD4B]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PNPLA6]] | +0.56 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[CACFD1]] | +0.54 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[PANX2]] | +0.53 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[WBP2]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[MKNK1]] | +0.53 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[ATOSB]] | +0.53 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[CLN8]] | +0.52 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[GDI1]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CYB5R1]] | +0.52 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[PSMD3]] | +0.51 | +0.41 / +0.44 | both halves | 4e-05 | pathway: Neddylation |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCL]] | -0.52 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[TFAM]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[SLC12A2-DT]] | -0.48 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[ANKRD18A]] | -0.46 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[DUT]] | -0.45 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[RMI1]] | -0.44 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[SYNCRIP]] | -0.43 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[TMA16]] | -0.42 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[DDX11-AS1]] | -0.42 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[PRIMPOL]] | -0.42 | -0.39 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF516]] | B | ZNF516 activity lowers DDA1's level | lines that do not express ZNF516 (5) vs lines expressing it (45) | 1.19× higher at baseline in the lines without ZNF516 | 0.081 | ⚠ within organs, on part of the lines; also absent: UAP1L1, LINC00847; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.425). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.6, -21.3); signed map (-28.3, -1.0). **Vector** length 56.4, 9.39% of its response variance represented; |z| ≥ 3 in 732 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.7 | +8.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.9 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.7 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +2.3 | +9.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.5 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | DET1 and DDB1 associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,309,518-17,323,298 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCIA1, MGC2594; previously C19orf58 |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BW61](https://www.uniprot.org/uniprotkb/Q9BW61) (DET1- and DDB1-associated protein 1):

> Functions as a component of numerous distinct DCX (DDB1-CUL4-X-box) E3 ubiquitin-protein ligase complexes which mediate the ubiquitination and subsequent proteasomal degradation of target proteins. In the DCX complexes, acts as a scaffolding subunit required to stabilize the complex.

**Summary**, from NCBI Gene [79016](https://www.ncbi.nlm.nih.gov/gene/79016):

> Involved in protein polyubiquitination. Part of Cul4-RING E3 ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28360) · Entrez [79016](https://www.ncbi.nlm.nih.gov/gene/79016) · UniProt [Q9BW61](https://www.uniprot.org/uniprotkb/Q9BW61) · Ensembl [ENSG00000130311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130311)

## Data

Gene col 5050: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5050); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5050, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5050]; `tensor/DDL_lfc|DDL_z.npy` [5050]; `embed/gene_vectors.npy` [5050]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5050 or target_col == 5050). Every well: [[DDA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
