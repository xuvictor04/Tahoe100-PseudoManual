---
symbol: "PITX2"
type: "gene"
col: 8865
ensembl_id: "ENSG00000164093"
name: "paired like homeodomain 2"
location: "4q25"
module: 59
arm: "+"
pooled_cpm: 2.85
n_lines_expressing: 36
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# PITX2

*paired like homeodomain 2* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +8.6, q 6e-15, up in 14 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 0.670× (z -3.8, q 0.079, down in 10 of 29 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 0.124×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPAN12]] (+0.59, fdr 3e-05), [[FMO5]] (+0.56, fdr 1e-05), [[HOXA5]] (+0.54, fdr 1e-05); moves opposite to [[KPNA4]] (-0.52, fdr 6e-05), [[ZNF731P]] (-0.49, fdr 9e-05), [[GNB1]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LNX1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ERVK13-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8865.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +8.6 | 6e-15 | 14/21 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +7.9 | 1e-12 | 14/30 (LoVo, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +6.1 | 2e-07 | 6/11 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +5.3 | 1e-05 | 11/22 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +4.9 | 1e-04 | 10/29 (NCI-H1573, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +4.4 | 9e-04 | 10/30 (HOP62, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.021 | 9/30 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.023 | 6/23 (HCT15, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.032 | 6/30 (NCI-H2347, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.032 | 5/22 (A-172, RKO, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.3 | 0.051 | 1/12 (LS 180) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.051 | 6/27 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.051 | 7/31 (HOP62, LoVo, …) | rises with dose |  |
| [[Vortioxetine (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.1 | 0.069 | 3/25 (LS 180, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +3.1 | 0.069 | 8/30 (NCI-H1573, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8865.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 0.124×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.670×** | -3.8 | 0.079 | 10/29 (HT-29, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.530× | -3.1 | 0.47 | 4/27 (NCI-H2347, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.378 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.973 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.379 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.838 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.636 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.873 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN12]] | +0.59 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[FMO5]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[HOXA5]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[KBTBD3]] | +0.54 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[HOXA3]] | +0.54 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[HOXA10]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[FRMPD3]] | +0.53 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[ZBTB18]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[RAB30]] | +0.53 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[FRK]] | +0.52 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[SATB2-AS1]] | +0.52 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[CXXC5]] | +0.52 | +0.37 / +0.48 | both halves | 8e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA4]] | -0.52 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[ZNF731P]] | -0.49 | -0.37 / -0.60 | both halves | 9e-05 |  |
| [[GNB1]] | -0.48 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[BRD9]] | -0.48 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[WDR27]] | -0.47 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[ERVK13-1]] | -0.47 | -0.18 / -0.52 | ⚠ one half (not replicated) | 1e-03 |  |
| [[SEC14L1]] | -0.47 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[C13orf46]] | -0.47 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[GHRLOS]] | -0.46 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[MSS51]] | -0.46 | -0.27 / -0.36 | both halves | 3e-04 |  |
| [[DCAKD]] | -0.45 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[GATAD2A]] | -0.45 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[MICAL2]] | -0.45 | -0.45 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LNX1]] | B | LNX1 activity raises PITX2's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 1.58× lower at baseline in the lines without LNX1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERVK13-1]] | B | PITX2 activity weakens ERVK13-1's drug response | lines that do not express PITX2 (14) vs lines expressing it (34) | the lines without PITX2 respond 1.14× as strongly (z diff -0.40); strongest at Dinaciclib 0.05 µM: 2.56x vs 1.96x (z diff -1.6) | 0.090 | ⚠ within organs, on part of the lines; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.496). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (31.3, 48.7); signed map (-5.0, 7.6). **Vector** length 33.6, 4.21% of its response variance represented; |z| ≥ 3 in 619 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.0 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.9 | +2.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | +1.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -1.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -0.8 | -0.2 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | paired like homeodomain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:110,617,423-110,642,123 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IGDS, RS, Brx1, Otlx2, ARP1; previously IRID2, IHG2, RIEG, RIEG1, RGS |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 2 pathways, smallest: TFAP2 (AP-2) family regulates transcription of other transcription factors; Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99697](https://www.uniprot.org/uniprotkb/Q99697) (Pituitary homeobox 2):

> May play a role in myoblast differentiation. When unphosphorylated, associates with an ELAVL1-containing complex, which stabilizes cyclin mRNA and ensuring cell proliferation. Phosphorylation by AKT2 impairs this association, leading to CCND1 mRNA destabilization and progression towards differentiation.; [Isoform PTX2C]: Involved in the establishment of left-right asymmetry in the developing embryo.

**Summary**, from NCBI Gene [5308](https://www.ncbi.nlm.nih.gov/gene/5308):

> This gene encodes a member of the RIEG/PITX homeobox family, which is in the bicoid class of homeodomain proteins. The encoded protein acts as a transcription factor and regulates procollagen lysyl hydroxylase gene expression. This protein plays a role in the terminal differentiation of somatotroph and lactotroph cell phenotypes, is involved in the development of the eye, tooth and abdominal organs, and acts as a transcriptional regulator involved in basal and hormone-regulated activity of …

**Accessions** — [HGNC:9005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9005) · Entrez [5308](https://www.ncbi.nlm.nih.gov/gene/5308) · UniProt [Q99697](https://www.uniprot.org/uniprotkb/Q99697) · Ensembl [ENSG00000164093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164093)

## Data

Gene col 8865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8865); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8865]; `tensor/DDL_lfc|DDL_z.npy` [8865]; `embed/gene_vectors.npy` [8865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8865 or target_col == 8865). Every well: [[PITX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PITX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
