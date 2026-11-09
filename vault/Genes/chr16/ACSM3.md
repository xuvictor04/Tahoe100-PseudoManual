---
symbol: "ACSM3"
type: "gene"
col: 71
ensembl_id: "ENSG00000005187"
name: "acyl-CoA synthetase medium chain family member 3"
location: "16p12.3"
module: 21
arm: "+"
pooled_cpm: 4.82
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ACSM3

*acyl-CoA synthetase medium chain family member 3* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.41× (z +13.8, q 1e-40, up in 33 of 39 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.5 µM in 1 line (SW1417 0.0546×); [[Ligustrazine (drug)]] 5 µM in 1 line (A-427 0.0543×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC3A1]] (+0.70, fdr 7e-06), [[SLC23A1]] (+0.66, fdr 1e-05), [[BCL2L14]] (+0.65, fdr 2e-05); moves opposite to [[MPHOSPH6]] (-0.50, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ARSL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 71.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +13.8 | 1e-40 | 33/39 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +10.2 | 4e-22 | 18/25 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +8.9 | 2e-16 | 5/9 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +7.6 | 3e-12 | 6/11 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +6.4 | 2e-08 | 22/44 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +5.5 | 3e-06 | 22/45 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +5.4 | 5e-06 | 20/47 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +4.9 | 5e-05 | 6/23 (A549, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.4 | 6e-04 | 7/44 (SK-MEL-2, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.4 | 7e-04 | 10/33 (MIA PaCa-2, SW 900, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.001 | 13/45 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.1 | 0.002 | 5/25 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +3.5 | 0.017 | 2/19 (NCI-H1573, PANC-1) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.022 | 10/38 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.54×** | +3.4 | 0.022 | 3/19 (LS 180, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.025 | 9/44 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.037 | 6/41 (HepG2/C3A, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 71.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.5 µM in 1 line (SW1417 0.0546×); [[Ligustrazine (drug)]] 5 µM in 1 line (A-427 0.0543×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.751× | -3.2 | 0.40 | 9/45 (HT-29, A498, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.756× | -3.1 | 0.40 | 10/44 (RPMI-7951, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 71. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 3.32 | 0 | 1 | — | [[Ligustrazine (drug)]] 5 µM 0.0543× (z -9.0) |
| [[A549 (line)]] | wt | 5.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 3.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 3.58 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0546× (z -9.6) |
| [[A-172 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 71), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC3A1]] | +0.70 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.66 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[BCL2L14]] | +0.65 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[AKAP1-DT]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[TSPOAP1-AS1]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[FLJ40194]] | +0.64 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[FAM217A]] | +0.64 | +0.35 / +0.70 | both halves | 1e-04 |  |
| [[C2CD5-AS1]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[IST1]] | +0.63 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[ZBTB20-AS5]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[FAM151B-DT]] | +0.61 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[TRAPPC6A]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPHOSPH6]] | -0.50 | -0.30 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARSL]] | B | ARSL activity raises ACSM3's level | lines that do not express ARSL (26) vs lines expressing it (24) | 1.46× lower at baseline in the lines without ARSL | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4 |
| [[HNF1A-AS1]] | B | HNF1A-AS1 activity raises ACSM3's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 1.41× lower at baseline in the lines without HNF1A-AS1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[ELF3]] | B | ELF3 activity raises ACSM3's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 1.34× lower at baseline in the lines without ELF3 | 0.064 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[LINC00992]] | B | LINC00992 activity raises ACSM3's level | lines that do not express LINC00992 (28) vs lines expressing it (22) | 1.36× lower at baseline in the lines without LINC00992 | 0.065 | ⚠ within organs, on part of the lines; also absent: LINC02147, INPP5D, LGR5 |
| [[BCAS1]] | B | BCAS1 activity raises ACSM3's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 1.30× lower at baseline in the lines without BCAS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ |
| [[MSLN]] | B | MSLN activity raises ACSM3's level | lines that do not express MSLN (33) vs lines expressing it (17) | 1.34× lower at baseline in the lines without MSLN | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.8, 28.9); signed map (36.0, 2.9). **Vector** length 42.0, 4.45% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +10.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -2.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA synthetase medium chain family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:20,610,243-20,797,581 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SA; previously SAH |
| Gene groups (HGNC) | Acyl-CoA synthetase family |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 5 pathways, smallest: Beta oxidation of butanoyl-CoA to acetyl-CoA; mitochondrial fatty acid beta-oxidation of saturated fatty acids; Mitochondrial Fatty Acid Beta-Oxidation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53FZ2](https://www.uniprot.org/uniprotkb/Q53FZ2) (Acyl-coenzyme A synthetase ACSM3, mitochondrial):

> Catalyzes the activation of fatty acids by CoA to produce an acyl-CoA, the first step in fatty acid metabolism. Capable of activating medium-chain fatty acids with a preference for isobutyrate among fatty acids with 2-6 carbon atoms (By similarity).

**Summary**, from NCBI Gene [6296](https://www.ncbi.nlm.nih.gov/gene/6296):

> Enables medium-chain fatty acid-CoA ligase activity. Predicted to be involved in acyl-CoA metabolic process and fatty acid biosynthetic process. Located in mitochondrion. Implicated in IgA glomerulonephritis. Biomarker of ulcerative colitis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10522](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10522) · Entrez [6296](https://www.ncbi.nlm.nih.gov/gene/6296) · UniProt [Q53FZ2](https://www.uniprot.org/uniprotkb/Q53FZ2) · Ensembl [ENSG00000005187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005187)

## Data

Gene col 71: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 71); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 71, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 71]; `tensor/DDL_lfc|DDL_z.npy` [71]; `embed/gene_vectors.npy` [71]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 71 or target_col == 71). Every well: [[ACSM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACSM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
