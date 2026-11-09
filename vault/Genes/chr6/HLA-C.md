---
symbol: "HLA-C"
type: "gene"
col: 12884
ensembl_id: "ENSG00000204525"
name: "major histocompatibility complex, class I, C"
location: "6p21.33"
module: 70
arm: "+"
pooled_cpm: 110.17
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# HLA-C

*major histocompatibility complex, class I, C* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.07× (z +9.6, q 5e-19, up in 34 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.52× (z +5.5, q 5e-06, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.521× (z -8.6, q 4e-15, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-H]] (+0.79, fdr 7e-06), [[HLA-B]] (+0.73, fdr 7e-06), [[HLA-A]] (+0.72, fdr 7e-06); moves opposite to [[MIS18A]] (-0.51, fdr 1e-04).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CD74]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +9.6 | 5e-19 | 34/47 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +7.2 | 1e-10 | 29/39 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +5.7 | 2e-06 | 23/43 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +5.5 | 5e-06 | 28/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.4 | 6e-06 | 26/46 (LOX-IMVI, RKO, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.4 | 7e-06 | 27/47 (LOX-IMVI, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +5.3 | 9e-06 | 29/46 (KATO III, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.020 | 14/46 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.020 | 14/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[venetoclax (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.100 | 8/47 (C-33 A, HS-578T, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.100 | 15/45 (HEC-1-A, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | 1.26× | +3.0 | 0.13 | 17/46 (NCI-H460, HCT15, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12884.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.521×** | -8.6 | 4e-15 | 41/46 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.651×** | -8.0 | 3e-13 | 29/45 (KATO III, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.574×** | -7.3 | 4e-11 | 36/46 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.703×** | -6.6 | 6e-09 | 30/47 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.635×** | -6.0 | 2e-07 | 26/45 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.640×** | -5.9 | 3e-07 | 33/46 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.650×** | -5.7 | 1e-06 | 30/46 (NCI-H1792, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.652×** | -5.7 | 1e-06 | 33/46 (NCI-H2347, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.685×** | -4.8 | 9e-05 | 27/47 (HS-578T, SW1417, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.720×** | -4.4 | 8e-04 | 20/46 (HS-578T, SW1417, …) | top dose only | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.809×** | -4.0 | 0.004 | 19/47 (C-33 A, HS-578T, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.571×** | -3.9 | 0.005 | 16/47 (HS-578T, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.773×** | -3.4 | 0.028 | 10/46 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.780×** | -3.3 | 0.039 | 20/47 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.785×** | -3.0 | 0.090 | 16/46 (RPMI-7951, BT-474, …) | inconsistent across doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.852× | -3.0 | 0.092 | 6/46 (BT-474, SW48, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 62.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 117 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.345× (z -9.0) |
| [[AN3 CA (line)]] | alt | 36.8 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0738× (z -8.7) |
| [[BT-474 (line)]] | alt | 248 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.183× (z -8.5) |
| [[C-33 A (line)]] | alt | 89.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.160× (z -9.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 64.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -9.2) |
| [[SNU-1 (line)]] | wt | 43.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0876× (z -11.8) |
| [[A-172 (line)]] | wt | 399 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.5 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 287 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 254 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 86.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 116 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 333 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 187 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 333 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 636 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 81.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-H]] | +0.79 | +0.70 / +0.76 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC |
| [[HLA-B]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 998 |
| [[HLA-A]] | +0.72 | +0.62 / +0.70 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 998 |
| [[B2M]] | +0.71 | +0.59 / +0.75 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 999 |
| [[TAP1]] | +0.69 | +0.56 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 699 |
| [[TAPBP]] | +0.69 | +0.57 / +0.69 | both halves | 1e-05 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 981 |
| [[MOV10]] | +0.68 | +0.59 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[HLA-F]] | +0.68 | +0.55 / +0.75 | both halves | 1e-05 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 990 |
| [[HLA-E]] | +0.68 | +0.52 / +0.70 | both halves | 1e-05 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 989 |
| [[RNF213]] | +0.68 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[USF1]] | +0.66 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[ERAP1]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 | pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 887 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS18A]] | -0.51 | -0.47 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD74]] | B | CD74 activity raises HLA-C's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.57× lower at baseline in the lines without CD74 | 0.033 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[SECTM1]] | B | SECTM1 activity raises HLA-C's level | lines that do not express SECTM1 (10) vs lines expressing it (40) | 2.18× lower at baseline in the lines without SECTM1 | 0.034 | ⚠ within organs, on part of the lines |
| [[CTSS]] | B | CTSS activity raises HLA-C's level | lines that do not express CTSS (15) vs lines expressing it (35) | 1.81× lower at baseline in the lines without CTSS | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[OASL]] | B | OASL activity raises HLA-C's level | lines that do not express OASL (10) vs lines expressing it (40) | 2.22× lower at baseline in the lines without OASL | 0.074 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[IDO1]] | B | IDO1 activity raises HLA-C's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 2.21× lower at baseline in the lines without IDO1 | 0.082 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[CASP10]] | B | CASP10 activity raises HLA-C's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.60× lower at baseline in the lines without CASP10 | 0.088 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[PHF11]] | C | PHF11 activity raises HLA-C's level | lines that do not express PHF11 (3) vs lines expressing it (47) | 4.32× lower at baseline in the lines without PHF11 | 0.037 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[APOBEC3F]] | C | APOBEC3F activity raises HLA-C's level | lines that do not express APOBEC3F (3) vs lines expressing it (47) | 3.54× lower at baseline in the lines without APOBEC3F | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PORCN, HOMER3, UGDH; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.6, 49.8); signed map (64.3, 27.4). **Vector** length 99.0, 24.3% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.51 to 25); *allograft rejection* (hallmark, mean cos +0.56 to 11); *complement* (hallmark, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.6 | +5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.3 | +3.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.3 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.8 | -4.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.4 | -6.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.5 | -2.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -5.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | major histocompatibility complex, class I, C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,268,749-31,272,130 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HLA-JY3, D6S204, PSORS1 |
| Gene groups (HGNC) | Histocompatibility complex; C1-set domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Reactome | 19 pathways, smallest: Endosomal/Vacuolar pathway; DAP12 interactions; Antigen Presentation: Folding, assembly and peptide loading of class I MHC |
| Matched by | ensembl_id |

**Function**, from UniProt [P10321](https://www.uniprot.org/uniprotkb/P10321) (HLA class I histocompatibility antigen, C alpha chain):

> Antigen-presenting major histocompatibility complex class I (MHCI) molecule with an important role in reproduction and antiviral immunity. In complex with B2M/beta 2 microglobulin displays a restricted repertoire of self and viral peptides and acts as a dominant ligand for inhibitory and activating killer immunoglobulin receptors (KIRs) expressed on NK cells. In an allogeneic setting, such as during pregnancy, mediates interaction of extravillous trophoblasts with KIR on uterine NK cells and …

**Summary**, from NCBI Gene [3107](https://www.ncbi.nlm.nih.gov/gene/3107):

> HLA-C belongs to the HLA class I heavy chain paralogues. This class I molecule is a heterodimer consisting of a heavy chain and a light chain (beta-2 microglobulin). The heavy chain is anchored in the membrane. Class I molecules play a central role in the immune system by presenting peptides derived from endoplasmic reticulum lumen. They are expressed in nearly all cells. The heavy chain is approximately 45 kDa and its gene contains 8 exons. Exon one encodes the leader peptide, exons 2 and 3 …

**Accessions** — [HGNC:4933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4933) · Entrez [3107](https://www.ncbi.nlm.nih.gov/gene/3107) · UniProt [P10321](https://www.uniprot.org/uniprotkb/P10321) · Ensembl [ENSG00000204525](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204525)

## Data

Gene col 12884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12884); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12884]; `tensor/DDL_lfc|DDL_z.npy` [12884]; `embed/gene_vectors.npy` [12884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12884 or target_col == 12884). Every well: [[HLA-C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLA-C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
