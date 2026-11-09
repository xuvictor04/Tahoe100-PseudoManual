---
symbol: "FLNB-AS1"
type: "gene"
col: 14392
ensembl_id: "ENSG00000244161"
name: "FLNB antisense RNA 1"
location: "3p14.3"
module: 136
arm: "+"
pooled_cpm: 2.21
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# FLNB-AS1

*FLNB antisense RNA 1* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.57× (z +8.6, q 5e-15, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.76× (z +3.8, q 0.017, up in 4 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.560× (z -5.5, q 2e-05, down in 14 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLNB]] (+0.78, fdr 7e-06, ⚠ same locus), [[LRRFIP1]] (+0.66, fdr 7e-06), [[TMEM184B]] (+0.66, fdr 8e-06), [[PLEK2]] (+0.64, fdr 1e-05); moves opposite to [[JADE2]] (-0.62, fdr 1e-05), [[UBAP2L]] (-0.59, fdr 4e-05), [[C5orf15]] (-0.56, fdr 9e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[F3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14392.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +8.6 | 5e-15 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +7.3 | 8e-11 | 4/13 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +4.7 | 4e-04 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.76×** | +3.8 | 0.017 | 4/21 (NCI-H460, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.75×** | +3.8 | 0.017 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.3 | 0.095 | 1/8 (NCI-H460) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here); position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | 1.40× | +3.2 | 0.12 | 3/29 (Hs 766T, A-427, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.89× | +3.1 | 0.12 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.40× | +3.1 | 0.13 | 3/37 (LoVo, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.84× | +3.0 | 0.14 | 1/6 (LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14392.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.560×** | -5.5 | 2e-05 | 14/42 (COLO 205, C32, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.595×** | -4.7 | 6e-04 | 10/33 (A498, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.602×** | -4.6 | 7e-04 | 17/39 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.720× | -3.1 | 0.27 | 11/29 (NCI-H460, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 5.22 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cepharanthine (drug)]] 0.05 µM 0.0769× (z -9.1) |
| [[A-172 (line)]] | wt | 3.24 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0628× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 2.44 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0797× (z -9.9) |
| [[A-427 (line)]] | wt | 0.890 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLNB]] | +0.78 | +0.74 / +0.71 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[LRRFIP1]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TMEM184B]] | +0.66 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[PLEK2]] | +0.64 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[PLEKHG5]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[ARID3B]] | +0.63 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[PBX4]] | +0.61 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[PAQR5]] | +0.59 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[CSNK1E]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[PLEKHM1P1]] | +0.59 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[LYPD3]] | +0.59 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[SLC8B1]] | +0.59 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[ETHE1]] | +0.59 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JADE2]] | -0.62 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[UBAP2L]] | -0.59 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[C5orf15]] | -0.56 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[SP1]] | -0.56 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[FAM111A]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[MED12]] | -0.55 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[SPG21]] | -0.55 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ARFGAP2]] | -0.55 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TMEM126B]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[TAPBP]] | -0.54 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[LACTB2]] | -0.53 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[HFE]] | -0.53 | -0.44 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity raises FLNB-AS1's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.27× lower at baseline in the lines without F3 | 0.052 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[S100A16]] | B | S100A16 activity raises FLNB-AS1's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 1.26× lower at baseline in the lines without S100A16 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[SERPINB1]] | B | SERPINB1 activity raises FLNB-AS1's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 1.31× lower at baseline in the lines without SERPINB1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[PLEK2]] | B | PLEK2 activity raises FLNB-AS1's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.17× lower at baseline in the lines without PLEK2 | 0.077 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[NDRG1]] | B | NDRG1 activity raises FLNB-AS1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.29× lower at baseline in the lines without NDRG1 | 0.078 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[BACE2]] | B | BACE2 activity raises FLNB-AS1's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 1.21× lower at baseline in the lines without BACE2 | 0.099 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.0, 5.3); signed map (-5.2, 44.4). **Vector** length 39.0, 4.25% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -2.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.0 | +1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.0 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.7 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -5.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | FLNB antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p14.3 — chr3:58,162,547-58,170,636 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40239) · Entrez [105377105](https://www.ncbi.nlm.nih.gov/gene/105377105) · Ensembl [ENSG00000244161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244161)

## Data

Gene col 14392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14392); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14392]; `tensor/DDL_lfc|DDL_z.npy` [14392]; `embed/gene_vectors.npy` [14392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14392 or target_col == 14392). Every well: [[FLNB-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLNB-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
