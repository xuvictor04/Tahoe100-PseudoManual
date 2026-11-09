---
symbol: "SPRYD7"
type: "gene"
col: 4412
ensembl_id: "ENSG00000123178"
name: "SPRY domain containing 7"
location: "13q14.2"
module: 12
arm: "+"
pooled_cpm: 20.46
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# SPRYD7

*SPRY domain containing 7* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.62× (z +9.0, q 2e-16, up in 26 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.56× (z +8.2, q 5e-14, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.894× (z -7.2, q 4e-10, down in 7 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.504× (z -6.6, q 1e-08, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABRAXAS2]] (+0.61, fdr 1e-05), [[PHC3]] (+0.59, fdr 1e-05), [[SNRNP27]] (+0.57, fdr 3e-05); moves opposite to [[PRSS22]] (-0.50, fdr 4e-05), [[PODXL2]] (-0.48, fdr 2e-04), [[DCAF16]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4412.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.62×** | +9.0 | 2e-16 | 26/39 (A-427, SW480, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +8.2 | 5e-14 | 33/48 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +8.2 | 5e-14 | 18/34 (A549, SW 900, …) | two highest doses | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +7.4 | 2e-11 | 34/47 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +7.3 | 5e-11 | 30/48 (A-427, RKO, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +6.8 | 1e-09 | 29/48 (KATO III, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +6.2 | 3e-08 | 22/43 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +6.1 | 9e-08 | 29/48 (KATO III, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.25×** | +5.9 | 2e-07 | 23/47 (NCI-H23, RPMI-7951, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.3 | 7e-06 | 20/47 (A-427, A549, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.32×** | +4.9 | 4e-05 | 20/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.20× | +4.7 | 1e-04 | 20/47 (HT-29, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.016 | 20/47 (A-427, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +3.5 | 0.021 | 13/47 (NCI-H1792, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4412.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -7.2 | 4e-10 | 7/48 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.504×** | -6.6 | 1e-08 | 24/48 (HT-29, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.630×** | -4.4 | 0.002 | 19/47 (RPMI-7951, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.798×** | -4.1 | 0.005 | 15/48 (SW 900, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 5 µM |  | **0.825×** | -3.5 | 0.046 | 10/48 (SW 1088, SHP-77, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.835× | -3.3 | 0.085 | 4/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Baicalin (drug)]] 5 µM |  | 0.885× | -3.2 | 0.12 | 3/48 (NCI-H23, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4412. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0992× (z -10.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 20.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 18.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 19.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.104× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.334× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +8.9) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.184× (z -10.5) |
| [[SW480 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4412), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABRAXAS2]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[PHC3]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[SNRNP27]] | +0.57 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[ZNF197]] | +0.57 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[CEP290]] | +0.56 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[NFU1]] | +0.56 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[BLTP3B]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[LRSAM1]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[WDR41]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ZFR]] | +0.54 | +0.64 / +0.40 | both halves | 5e-05 |  |
| [[DNAJB2]] | +0.53 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[TIPRL]] | +0.53 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRSS22]] | -0.50 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[PODXL2]] | -0.48 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[DCAF16]] | -0.47 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[MARCKSL1]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[C16orf95]] | -0.46 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[ACTN4]] | -0.45 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[TNFRSF21]] | -0.44 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[GPC3]] | -0.44 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[SMAD6]] | -0.44 | -0.47 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers SPRYD7's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.477). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-30.4, 5.5); signed map (-4.2, -7.8). **Vector** length 70.9, 12.2% of its response variance represented; |z| ≥ 3 in 763 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.1 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +6.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +2.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.9 | -6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | -0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.0 | +0.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -0.9 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | SPRY domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:49,912,702-49,936,490 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLLD6; previously C13orf1 |
| Matched by | ensembl_id |

UniProt [Q5W111](https://www.uniprot.org/uniprotkb/Q5W111) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:14297](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14297) · Entrez [57213](https://www.ncbi.nlm.nih.gov/gene/57213) · UniProt [Q5W111](https://www.uniprot.org/uniprotkb/Q5W111) · Ensembl [ENSG00000123178](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123178)

## Data

Gene col 4412: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4412); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4412, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4412]; `tensor/DDL_lfc|DDL_z.npy` [4412]; `embed/gene_vectors.npy` [4412]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4412 or target_col == 4412). Every well: [[SPRYD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPRYD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
