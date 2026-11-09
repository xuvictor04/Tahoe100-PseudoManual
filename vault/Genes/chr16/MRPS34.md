---
symbol: "MRPS34"
type: "gene"
col: 1069
ensembl_id: "ENSG00000074071"
name: "mitochondrial ribosomal protein S34"
location: "16p13.3"
module: 54
arm: "+"
pooled_cpm: 21.61
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# MRPS34

*mitochondrial ribosomal protein S34* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.91× (z +7.1, q 6e-10, up in 35 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.431× (z -7.9, q 2e-12, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFB10]] (+0.77, fdr 1e-05), [[MRPS26]] (+0.77, fdr 7e-06), [[POP7]] (+0.73, fdr 7e-06); moves opposite to [[WSB2]] (-0.68, fdr 2e-05), [[TUG1]] (-0.67, fdr 2e-05), [[UBE2A]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SYBU]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1069.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.91×** | +7.1 | 6e-10 | 35/41 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.09×** | +4.7 | 6e-04 | 27/33 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.83×** | +4.0 | 0.011 | 34/44 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.7 | 0.026 | 30/43 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | 1.61× | +3.1 | 0.24 | 26/46 (HT-29, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1069.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.431×** | -7.9 | 2e-12 | 43/47 (AsPC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.556×** | -5.5 | 1e-05 | 35/47 (RPMI-7951, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.452×** | -5.2 | 3e-05 | 38/48 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.523×** | -4.3 | 0.003 | 31/47 (NCI-H1573, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.587×** | -3.5 | 0.050 | 29/47 (A-427, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.623× | -3.1 | 0.17 | 22/46 (BT-474, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.411× | -3.1 | 0.17 | 27/48 (AsPC-1, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1069. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 22.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.6) |
| [[SW48 (line)]] | wt | 37.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -10.1) |
| [[A-427 (line)]] | wt | 23.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -11.1) |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.136× (z -8.5) |
| [[Hs 766T (line)]] | wt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 18.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.139× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 27.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -8.9) |
| [[PANC-1 (line)]] | alt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.3) |
| [[RKO (line)]] | wt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 17.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -11.3) |
| [[A-172 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1069), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFB10]] | +0.77 | +0.54 / +0.72 | both halves | 1e-05 | STRING 502 |
| [[MRPS26]] | +0.77 | +0.65 / +0.79 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 998 |
| [[POP7]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[POLR2I]] | +0.73 | +0.45 / +0.69 | both halves | 3e-05 | STRING 450 |
| [[C15orf61]] ⚠ | +0.73 | +0.48 / +0.76 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SAC3D1]] | +0.71 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[MRPL34]] | +0.71 | +0.58 / +0.73 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 907 |
| [[PET117]] | +0.70 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[WRAP73]] | +0.69 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[RHOT1]] | +0.68 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MPHOSPH10]] | +0.68 | +0.41 / +0.75 | both halves | 4e-05 |  |
| [[LSM2]] | +0.68 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[ATG4C]] | +0.68 | +0.48 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WSB2]] | -0.68 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[TUG1]] | -0.67 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[UBE2A]] | -0.64 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[CCDC200]] | -0.64 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[WDR45]] | -0.64 | -0.61 / -0.37 | both halves | 8e-05 |  |
| [[LYRM1]] | -0.63 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[EIF4G2]] | -0.63 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[CHMP3]] | -0.63 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CCNT2-AS1]] | -0.63 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[CROCC]] | -0.63 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[ATXN1L]] | -0.63 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[PBLD]] | -0.62 | -0.50 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYBU]] | B | SYBU activity raises MRPS34's level | lines that do not express SYBU (18) vs lines expressing it (32) | 1.21× lower at baseline in the lines without SYBU | 0.060 | ⚠ within organs, on part of the lines; also absent: CRIP1, MAP7, CHMP4C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.752). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-44.4, -13.4); signed map (-20.3, -7.4). **Vector** length 76.8, 24.5% of its response variance represented; |z| ≥ 3 in 561 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | -0.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.4 | -0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -6.2 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.9 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -5.7 | +7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.3 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.1 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,771,890-1,773,150 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-S12, MGC2616, mS34 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [P82930](https://www.uniprot.org/uniprotkb/P82930) (Small ribosomal subunit protein mS34):

> Required for mitochondrial translation, plays a role in maintaining the stability of the small ribosomal subunit and the 12S rRNA that are required for mitoribosome formation.

**Summary**, from NCBI Gene [65993](https://www.ncbi.nlm.nih.gov/gene/65993):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:16618](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16618) · Entrez [65993](https://www.ncbi.nlm.nih.gov/gene/65993) · UniProt [P82930](https://www.uniprot.org/uniprotkb/P82930) · Ensembl [ENSG00000074071](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074071)

## Data

Gene col 1069: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1069); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1069, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1069]; `tensor/DDL_lfc|DDL_z.npy` [1069]; `embed/gene_vectors.npy` [1069]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1069 or target_col == 1069). Every well: [[MRPS34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
