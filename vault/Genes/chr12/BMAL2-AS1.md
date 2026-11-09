---
symbol: "BMAL2-AS1"
type: "gene"
col: 14427
ensembl_id: "ENSG00000245311"
name: "BMAL2 antisense RNA 1"
location: "12p11.23"
module: 21
arm: "+"
pooled_cpm: 3.14
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# BMAL2-AS1

*BMAL2 antisense RNA 1* — 12p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.25× (z +11.6, q 2e-28, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +4.7, q 3e-04, up in 8 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (A549 0.0590×); [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H460 0.109×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0730×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC13A4]] (+0.71, fdr 7e-06), [[SMCO2]] (+0.70, fdr 7e-06, ⚠ same locus), [[TP53TG5]] (+0.70, fdr 8e-06), [[STARD13-AS]] (+0.68, fdr 7e-06); moves opposite to [[ILVBL]] (-0.55, fdr 2e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SMCO2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14427.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.25×** | +11.6 | 2e-28 | 5/5 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.41×** | +9.0 | 7e-17 | 7/18 (NCI-H460, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.4 | 7e-15 | 12/17 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +7.6 | 4e-12 | 5/9 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.7 | 3e-04 | 8/37 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.72×** | +3.9 | 0.008 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.29×** | +3.7 | 0.016 | 6/35 (CFPAC-1, HepG2/C3A, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +3.6 | 0.023 | 7/30 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.46×** | +3.6 | 0.023 | 6/27 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.053 | 5/41 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.78× | +3.1 | 0.10 | 0/7 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.37× | +3.1 | 0.10 | 3/34 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14427.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (A549 0.0590×); [[Thymol (drug)]] 0.5 µM in 1 line (NCI-H460 0.109×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0730×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.885× | -4.6 | 0.003 | 19/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.47 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0953× (z -8.8) |
| [[A549 (line)]] | wt | 4.32 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0590× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 3.01 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0700× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 4.78 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0730× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 2.84 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.109× (z -9.4) |
| [[A-172 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC13A4]] | +0.71 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[SMCO2]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[TP53TG5]] | +0.70 | +0.58 / +0.70 | both halves | 8e-06 |  |
| [[STARD13-AS]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 | same gene group |
| [[RETREG1-AS1]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 | same gene group |
| [[ATP13A3-DT]] | +0.66 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[OPCML]] | +0.66 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[AADACL2-AS1]] | +0.65 | +0.58 / +0.67 | both halves | 8e-06 | same gene group |
| [[LRRC8C-DT]] | +0.64 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[SPAG5-AS1]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 | same gene group |
| [[MTUS2]] | +0.64 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CFAP20DC-AS1]] | +0.64 | +0.57 / +0.62 | both halves | 9e-06 | same gene group |
| [[SLC9C1]] | +0.64 | +0.49 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILVBL]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMCO2]] | B | SMCO2 activity raises BMAL2-AS1's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.33× lower at baseline in the lines without SMCO2 | 0.006 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[LAMB3]] | B | LAMB3 activity raises BMAL2-AS1's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 1.23× lower at baseline in the lines without LAMB3 | 0.031 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[RIPOR3]] | B | RIPOR3 activity raises BMAL2-AS1's level | lines that do not express RIPOR3 (5) vs lines expressing it (45) | 1.26× lower at baseline in the lines without RIPOR3 | 0.055 | ⚠ within organs, on part of the lines; also absent: SYNPO2, PER3, ENSG00000274265; maybe low, not absent |
| [[DSCAM]] | B | DSCAM activity raises BMAL2-AS1's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 1.12× lower at baseline in the lines without DSCAM | 0.076 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent |
| [[BMAL2]] | B | BMAL2 activity raises BMAL2-AS1's level | lines that do not express BMAL2 (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without BMAL2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SMCO2, STXBP2, PDLIM1; maybe low, not absent; its own permutation p |
| [[KISS1]] | B | KISS1 activity raises BMAL2-AS1's level | lines that do not express KISS1 (35) vs lines expressing it (15) | 1.18× lower at baseline in the lines without KISS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SIM1, CALB1, PSG1 |
| [[XIRP2]] | C | XIRP2 activity raises BMAL2-AS1's level | lines that do not express XIRP2 (3) vs lines expressing it (47) | 1.31× lower at baseline in the lines without XIRP2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PDE11A, ENSG00000214803, ENSG00000228566; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.3, 26.6); signed map (30.8, 8.1). **Vector** length 39.1, 3.72% of its response variance represented; |z| ≥ 3 in 945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.3 | +3.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +3.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -4.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | +0.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | BMAL2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p11.23 — chr12:27,389,789-27,446,625 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously ARNTL2-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49892) · Entrez [101928646](https://www.ncbi.nlm.nih.gov/gene/101928646) · Ensembl [ENSG00000245311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245311)

## Data

Gene col 14427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14427); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14427]; `tensor/DDL_lfc|DDL_z.npy` [14427]; `embed/gene_vectors.npy` [14427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14427 or target_col == 14427). Every well: [[BMAL2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMAL2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
