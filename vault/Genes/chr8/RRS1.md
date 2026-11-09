---
symbol: "RRS1"
type: "gene"
col: 10991
ensembl_id: "ENSG00000179041"
name: "regulator of ribosome synthesis 1"
location: "8q13.1"
module: 1
arm: "+"
pooled_cpm: 5.13
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 4
n_dd_up_clean: 25
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RRS1

*regulator of ribosome synthesis 1* — 8q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (14 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 3.67× (z +11.6, q 3e-28, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.737× (z -3.9, q 0.053, down in 13 of 46 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Cytarabine (drug)]] 0.05 µM: 0.639× (z -3.7, q 0.053, down in 11 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BYSL]] (+0.86, fdr 7e-06), [[PAK1IP1]] (+0.81, fdr 7e-06), [[LTV1]] (+0.81, fdr 7e-06); moves opposite to [[GNAS]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EIF4E]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10991.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **3.67×** | +11.6 | 3e-28 | 43/45 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.61×** | +11.4 | 1e-27 | 31/37 (LOX-IMVI, A549, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.44×** | +10.2 | 5e-22 | 9/13 (SW1417, NCI-H460, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.08×** | +9.6 | 9e-20 | 3/6 (A498, HS-578T, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.95×** | +9.2 | 3e-18 | 34/44 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.64×** | +8.6 | 5e-16 | 34/44 (PANC-1, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.67×** | +8.4 | 3e-15 | 22/27 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.50×** | +8.1 | 3e-14 | 15/24 (LoVo, KATO III, …) | all doses, flat | composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **2.37×** | +7.4 | 1e-11 | 31/43 (PANC-1, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.25×** | +7.2 | 3e-11 | 32/46 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.59×** | +5.8 | 3e-07 | 21/40 (A549, A498, …) | all doses, flat | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.46×** | +5.8 | 4e-07 | 22/37 (NCI-H2030, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.91×** | +5.8 | 4e-07 | 12/25 (SW1417, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.7 | 4e-07 | 19/45 (A498, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.87×** | +5.6 | 1e-06 | 18/39 (J82, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.82×** | +4.8 | 4e-05 | 15/44 (KATO III, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.47×** | +4.2 | 7e-04 | 8/34 (A498, A549, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.003 | 18/45 (MIA PaCa-2, AN3 CA, …) | top dose only | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **2.30×** | +3.9 | 0.003 | 7/29 (PANC-1, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.28×** | +3.8 | 0.003 | 8/38 (PANC-1, A549, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.22×** | +3.7 | 0.005 | 10/33 (MIA PaCa-2, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.008 | 12/46 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10991.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.737×** | -3.9 | 0.053 | 13/46 (Hs 766T, HCT15, …) | rises with dose | position effect removed |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.639×** | -3.7 | 0.053 | 11/46 (SW48, H4, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.667×** | -3.6 | 0.053 | 8/46 (KATO III, HEC-1-A, …) | rises with dose | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.481×** | -3.4 | 0.088 | 13/42 (A498, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10991. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.87 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.103× (z -9.6) ⚠ toxic |
| [[KATO III (line)]] | alt | 5.64 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0615× (z -9.5) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 8.26 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.78× (z +9.3) | — |
| [[A-172 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10991), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BYSL]] | +0.86 | +0.86 / +0.82 | both halves | 7e-06 | STRING 945 |
| [[PAK1IP1]] | +0.81 | +0.82 / +0.81 | both halves | 7e-06 | STRING 852 |
| [[LTV1]] | +0.81 | +0.81 / +0.77 | both halves | 7e-06 | STRING 797 |
| [[DDX10]] | +0.80 | +0.79 / +0.79 | both halves | 7e-06 | STRING 554 |
| [[EXOSC2]] | +0.79 | +0.78 / +0.80 | both halves | 7e-06 |  |
| [[NDUFAF4]] | +0.79 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[MAK16]] | +0.79 | +0.84 / +0.74 | both halves | 7e-06 | STRING 957 |
| [[MRTO4]] | +0.79 | +0.82 / +0.76 | both halves | 7e-06 | same gene group; STRING 992 |
| [[GPATCH4]] | +0.78 | +0.81 / +0.83 | both halves | 7e-06 | STRING 656 |
| [[NIP7]] | +0.78 | +0.77 / +0.83 | both halves | 7e-06 | same gene group; STRING 987 |
| [[COA4]] | +0.78 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[RRP1]] | +0.77 | +0.68 / +0.76 | both halves | 7e-06 | same gene group; STRING 949 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.68 | -0.71 / -0.73 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EIF4E]] | C | EIF4E's natural level weakens RRS1's drug response | EIF4E's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.22; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.822). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.6, -37.4); signed map (-0.7, -44.0). **Vector** length 73.3, 13.5% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.59 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.61 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.62 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +8.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +7.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +11.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +5.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.7 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -3.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -1.6 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.6 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | regulator of ribosome synthesis 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.1 — chr8:66,429,014-66,430,733 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0112 |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15050](https://www.uniprot.org/uniprotkb/Q15050) (Ribosome biogenesis regulatory protein homolog):

> Involved in ribosomal large subunit assembly. May regulate the localization of the 5S RNP/5S ribonucleoprotein particle to the nucleolus.

**Summary**, from NCBI Gene [23212](https://www.ncbi.nlm.nih.gov/gene/23212):

> Enables 5S rRNA binding activity. Involved in several processes, including mitotic metaphase chromosome alignment; protein localization to nucleolus; and ribosomal large subunit assembly. Located in condensed nuclear chromosome and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17083) · Entrez [23212](https://www.ncbi.nlm.nih.gov/gene/23212) · UniProt [Q15050](https://www.uniprot.org/uniprotkb/Q15050) · Ensembl [ENSG00000179041](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179041)

## Data

Gene col 10991: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10991); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10991, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10991]; `tensor/DDL_lfc|DDL_z.npy` [10991]; `embed/gene_vectors.npy` [10991]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10991 or target_col == 10991). Every well: [[RRS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
