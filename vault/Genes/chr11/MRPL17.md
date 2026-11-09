---
symbol: "MRPL17"
type: "gene"
col: 8125
ensembl_id: "ENSG00000158042"
name: "mitochondrial ribosomal protein L17"
location: "11p15.4"
module: 3
arm: "+"
pooled_cpm: 19.47
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MRPL17

*mitochondrial ribosomal protein L17* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.70× (z +4.5, q 0.004, up in 28 of 44 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~45% of this change.
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.431× (z -10.2, q 2e-21, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A11]] (+0.71, fdr 7e-06), [[MRPL55]] (+0.70, fdr 1e-05), [[PUSL1]] (+0.69, fdr 9e-05); moves opposite to [[CYB5D2]] (-0.68, fdr 2e-05), [[CROCC]] (-0.64, fdr 8e-05), [[LYRM1]] (-0.62, fdr 7e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PGM5P2-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8125.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.70×** | +4.5 | 0.004 | 28/44 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.46× | +3.2 | 0.32 | 24/47 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.49× | +3.1 | 0.32 | 17/44 (HS-578T, A549, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8125.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.431×** | -10.2 | 2e-21 | 44/47 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.351×** | -8.9 | 1e-16 | 44/48 (BT-474, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.432×** | -7.2 | 1e-10 | 33/45 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.458×** | -6.7 | 4e-09 | 41/47 (BT-474, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.583×** | -6.5 | 8e-09 | 35/46 (BT-474, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.481×** | -6.2 | 4e-08 | 38/47 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.381×** | -4.0 | 0.005 | 14/26 (A-427, NCI-H1792, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.628×** | -4.0 | 0.005 | 30/47 (NCI-H1573, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.667×** | -3.3 | 0.057 | 21/44 (BT-474, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.670×** | -3.2 | 0.071 | 22/47 (LOX-IMVI, SW48, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | 0.476× | -3.1 | 0.10 | 24/47 (H4, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.693× | -3.0 | 0.12 | 19/46 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8125. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 22.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -12.5) |
| [[SNU-1 (line)]] | wt | 28.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -10.9) |
| [[A-427 (line)]] | wt | 25.5 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.324× (z -8.9) |
| [[J82 (line)]] | alt | 48.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 14.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -14.7) |
| [[RKO (line)]] | wt | 22.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -9.6) |
| [[C-33 A (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.137× (z -10.1) ⚠ toxic |
| [[H4 (line)]] | wt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -9.5) |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.152× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 21.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -14.8) |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.151× (z -8.6) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0933× (z -10.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 35.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 29.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -8.7) |
| [[A-172 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8125), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A11]] | +0.71 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[MRPL55]] | +0.70 | +0.55 / +0.59 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 922 |
| [[PUSL1]] | +0.69 | +0.36 / +0.61 | both halves | 9e-05 | STRING 791 |
| [[MEA1]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ATG4C]] | +0.67 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[CBR1]] | +0.67 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[MTLN]] ⚠ | +0.66 | +0.46 / +0.65 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[YIF1B]] | +0.66 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[PET117]] | +0.66 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[NUDT22]] | +0.65 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[OCEL1]] | +0.65 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[MED8]] | +0.65 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[PREB]] | +0.65 | +0.47 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5D2]] | -0.68 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[CROCC]] | -0.64 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[LYRM1]] | -0.62 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[ACYP2]] | -0.61 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[MSTO1]] | -0.60 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[RAD51-AS1]] | -0.60 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[POU6F1]] | -0.60 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[IQCH-AS1]] | -0.60 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[VSIG10]] | -0.59 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[RRAGC-DT]] | -0.59 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[SRSF5]] | -0.59 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[CHMP3]] | -0.58 | -0.33 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGM5P2-1]] | B | PGM5P2-1 activity raises MRPL17's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 1.52× lower at baseline in the lines without PGM5P2-1 | 0.038 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (9.8, -13.2); signed map (-36.7, 17.9). **Vector** length 95.1, 26.5% of its response variance represented; |z| ≥ 3 in 717 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.0 | +3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | -0.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.6 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.3 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.7 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -6.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -2.3 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:6,680,385-6,683,340 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPML26, MRP-L26, bL17m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9NRX2](https://www.uniprot.org/uniprotkb/Q9NRX2) carries no function annotation.

**Summary**, from NCBI Gene [63875](https://www.ncbi.nlm.nih.gov/gene/63875):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14053) · Entrez [63875](https://www.ncbi.nlm.nih.gov/gene/63875) · UniProt [Q9NRX2](https://www.uniprot.org/uniprotkb/Q9NRX2) · Ensembl [ENSG00000158042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158042)

## Data

Gene col 8125: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8125); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8125, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8125]; `tensor/DDL_lfc|DDL_z.npy` [8125]; `embed/gene_vectors.npy` [8125]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8125 or target_col == 8125). Every well: [[MRPL17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
