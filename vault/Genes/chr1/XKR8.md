---
symbol: "XKR8"
type: "gene"
col: 8136
ensembl_id: "ENSG00000158156"
name: "XK related 8"
location: "1p35.3"
module: 30
arm: "+"
pooled_cpm: 2.68
n_lines_expressing: 44
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# XKR8

*XK related 8* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.94× (z +6.6, q 3e-08, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Hydroxyurea (drug)]] 0.05 µM: 1.48× (z +3.8, q 0.026, up in 3 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.514× (z -9.8, q 9e-20, down in 27 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OTX1]] (+0.78, fdr 7e-06), [[UNC45A]] (+0.64, fdr 1e-05), [[MRPL34]] (+0.63, fdr 1e-05); moves opposite to [[ALG13]] (-0.58, fdr 1e-04), [[SDCBP2-AS1]] (-0.56, fdr 4e-05), [[LEKR1]] (-0.56, fdr 6e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[EFNA4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8136.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +6.6 | 3e-08 | 0/5 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.34×** | +4.2 | 0.006 | 3/39 (RKO, NCI-H460, …) | top dose only | low cells (technical?) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.026 | 3/23 (LS 180, SW1417, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.66×** | +3.7 | 0.026 | 2/7 (HEC-1-A, PANC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.5 | 0.044 | 2/15 (A-427, SW1417) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.42×** | +3.3 | 0.064 | 2/23 (HOP62, PANC-1) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.42×** | +3.3 | 0.064 | 4/23 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.064 | 2/39 (A498, PANC-1) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.52× | +3.1 | 0.13 | 5/30 (LS 180, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.51× | +3.0 | 0.14 | 2/23 (A498, LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8136.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.514×** | -9.8 | 9e-20 | 27/34 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.440×** | -7.4 | 4e-11 | 19/34 (hTERT-HPNE, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.484×** | -7.2 | 8e-11 | 22/37 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.596×** | -5.4 | 1e-05 | 17/40 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.637×** | -4.7 | 3e-04 | 16/37 (Panc 03.27, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.427×** | -4.6 | 4e-04 | 8/27 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.657×** | -4.4 | 0.001 | 10/37 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -3.8 | 0.011 | 13/35 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Imiquimod (maleate) (drug)]] 0.5 µM |  | **0.720×** | -3.4 | 0.039 | 6/34 (SW48, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.66 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0872× (z -17.8) |
| [[A498 (line)]] | wt | 6.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -13.2) |
| [[HOP62 (line)]] | alt | 3.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 4.51 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0639× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.859 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.329 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.205 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OTX1]] | +0.78 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[UNC45A]] | +0.64 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MRPL34]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.63 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[C1orf174]] | +0.63 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[SLC9A6]] | +0.62 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[MTMR12]] | +0.61 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[XYLT2]] | +0.61 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[ZNF174]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[RNF41]] | +0.61 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SUFU]] | +0.61 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PHAF1]] | +0.60 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG13]] | -0.58 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[SDCBP2-AS1]] | -0.56 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[LEKR1]] | -0.56 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[HNRNPA2B1]] | -0.55 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[ARRDC3-AS1]] | -0.54 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[RGS5]] | -0.54 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[ZNF655]] | -0.54 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[LINC01135]] | -0.53 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[HNRNPU]] | -0.52 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[TASOR]] | -0.52 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[SSUH2]] | -0.52 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[RAB30-DT]] | -0.51 | -0.44 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNA4]] | B | XKR8 activity raises EFNA4's level | lines that do not express XKR8 (6) vs lines expressing it (44) | 1.56× lower at baseline in the lines without XKR8 | 0.064 | ⚠ within organs, on part of the lines; also absent: MORC4 |
| [[HSDL1]] | B | XKR8 activity lowers HSDL1's level | lines that do not express XKR8 (6) vs lines expressing it (44) | 1.31× higher at baseline in the lines without XKR8 | 0.084 | ⚠ within organs, on part of the lines; also absent: MORC4 |
| [[CXXC1]] | B | XKR8 activity lowers CXXC1's level | lines that do not express XKR8 (6) vs lines expressing it (44) | 1.33× higher at baseline in the lines without XKR8 | 0.087 | ⚠ within organs, on part of the lines; also absent: MORC4 |
| [[WRAP73]] | B | XKR8 activity lowers WRAP73's level | lines that do not express XKR8 (6) vs lines expressing it (44) | 1.24× higher at baseline in the lines without XKR8 | 0.087 | ⚠ within organs, on part of the lines; also absent: MORC4 |
| [[CCZ1]] | B | XKR8 activity lowers CCZ1's level | lines that do not express XKR8 (6) vs lines expressing it (44) | 1.43× higher at baseline in the lines without XKR8 | 0.089 | ⚠ within organs, on part of the lines; also absent: MORC4 |
| [[MALSU1]] | B | XKR8 activity lowers MALSU1's level | lines that do not express XKR8 (6) vs lines expressing it (44) | 1.34× higher at baseline in the lines without XKR8 | 0.093 | ⚠ within organs, on part of the lines; also absent: MORC4 |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.673). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.5, -5.2); signed map (-35.5, -3.5). **Vector** length 43.2, 5.42% of its response variance represented; |z| ≥ 3 in 773 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +1.9 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.0 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -4.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.1 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Brimonidine (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Hydroxyurea (drug)]] 0.5 µM |  | -0.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | XK related 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:27,959,588-27,968,093 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10307 |
| Gene groups (HGNC) | XK related family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6D3](https://www.uniprot.org/uniprotkb/Q9H6D3) (XK-related protein 8):

> [XK-related protein 8, processed form]: Phospholipid scramblase that promotes phosphatidylserine exposure on apoptotic cell surface. Phosphatidylserine is a specific marker only present at the surface of apoptotic cells and acts as a specific signal for engulfment. Required for the clearance of apoptotic cells, such as engulfment of apoptotic germ cells by Sertoli cells, clearance of senescent neutrophils or regulation of bipolar cell numbers in the retina (By similarity). In the hippocampus, …

**Summary**, from NCBI Gene [55113](https://www.ncbi.nlm.nih.gov/gene/55113):

> Enables phospholipid scramblase activity. Involved in engulfment of apoptotic cell; phosphatidylserine exposure on apoptotic cell surface; and positive regulation of myoblast differentiation. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25508) · Entrez [55113](https://www.ncbi.nlm.nih.gov/gene/55113) · UniProt [Q9H6D3](https://www.uniprot.org/uniprotkb/Q9H6D3) · Ensembl [ENSG00000158156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158156)

## Data

Gene col 8136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8136); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8136]; `tensor/DDL_lfc|DDL_z.npy` [8136]; `embed/gene_vectors.npy` [8136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8136 or target_col == 8136). Every well: [[XKR8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XKR8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
