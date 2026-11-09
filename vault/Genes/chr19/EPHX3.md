---
symbol: "EPHX3"
type: "gene"
col: 2549
ensembl_id: "ENSG00000105131"
name: "epoxide hydrolase 3"
location: "19p13.12"
module: 47
arm: "+"
pooled_cpm: 3.24
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# EPHX3

*epoxide hydrolase 3* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +7.5, q 4e-11, up in 16 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.370× (z -9.2, q 1e-17, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKL4]] (+0.87, fdr 7e-06), [[MYOCOS]] (+0.85, fdr 7e-06), [[TTC36]] (+0.80, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2549.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +7.5 | 4e-11 | 16/36 (HS-578T, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +6.0 | 6e-07 | 1/4 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.025 | 9/47 (SW480, SW1417, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.079 | 9/42 (NCI-H2030, BT-474, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.44× | +3.1 | 0.17 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.40× | +3.1 | 0.17 | 5/42 (H4, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2549.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.370×** | -9.2 | 1e-17 | 28/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.408×** | -8.0 | 3e-13 | 14/18 (LoVo, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.507×** | -6.1 | 2e-07 | 23/40 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.538×** | -5.8 | 1e-06 | 19/27 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.564×** | -5.1 | 3e-05 | 21/43 (NCI-H2030, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.569×** | -5.1 | 4e-05 | 17/42 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.622×** | -4.2 | 0.002 | 16/36 (HOP62, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.644×** | -4.1 | 0.003 | 16/45 (SK-MEL-2, NCI-H23, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.642×** | -4.0 | 0.005 | 16/40 (A-427, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.676×** | -3.6 | 0.016 | 14/41 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Penfluridol (drug)]] 0.5 µM |  | **0.688×** | -3.5 | 0.027 | 4/43 (C32, RKO, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.673×** | -3.4 | 0.032 | 8/44 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.681×** | -3.4 | 0.032 | 14/38 (NCI-H1573, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **0.524×** | -3.1 | 0.069 | 2/39 (HepG2/C3A, PANC-1) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2549. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.07 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0562× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0748× (z -11.2) |
| [[LoVo (line)]] | wt | 3.66 | 0 | 3 (1 ⚠) | — | [[Brimonidine (drug)]] 0.5 µM 0.0630× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 4.52 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0976× (z -9.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Orlistat (drug)]] 0.05 µM 0.104× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 3.54 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0446× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 6.20 | 0 | 2 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0698× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 2.92 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0365× (z -13.4) |
| [[A498 (line)]] | wt | 2.47 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0567× (z -9.5) ⚠ cell-cycle shift, explains ~86% of this change |
| [[KATO III (line)]] | alt | 3.38 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0715× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 5.04 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.102× (z -9.0) |
| [[A-172 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.992 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.849 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2549), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL4]] | +0.87 | +0.84 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[MYOCOS]] | +0.85 | +0.86 / +0.78 | both halves | 7e-06 |  |
| [[TTC36]] | +0.80 | +0.78 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[MSANTD1]] | +0.80 | +0.82 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[SLC22A14]] | +0.80 | +0.82 / +0.72 | both halves | 7e-06 |  |
| [[ARL9]] | +0.80 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.79 | +0.83 / +0.72 | both halves | 7e-06 |  |
| [[PILRA]] | +0.79 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[CHRNA10]] | +0.78 | +0.78 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LINC02803]] | +0.78 | +0.82 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[RAPSN]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.78 | +0.76 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2]] | B | F2 activity raises EPHX3's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.41× lower at baseline in the lines without F2 | 0.030 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[C5AR1]] | C | C5AR1 activity raises EPHX3's level | lines that do not express C5AR1 (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without C5AR1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FARP1, PER3, NECAB2; maybe low, not absent; its own permutation p |
| [[MATN1-AS1]] | C | MATN1-AS1 activity lowers EPHX3's level | lines that do not express MATN1-AS1 (4) vs lines expressing it (46) | 1.41× higher at baseline in the lines without MATN1-AS1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CYB561, LINC01569, E2F8; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.812). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.9, -15.1); signed map (16.4, 9.1). **Vector** length 69.4, 11.1% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +3.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.6 | +1.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -3.7 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -9.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -6.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.9 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | epoxide hydrolase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:15,226,919-15,233,435 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22408; previously ABHD9 |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6B9](https://www.uniprot.org/uniprotkb/Q9H6B9) (Epoxide hydrolase 3):

> Catalyzes the hydrolysis of epoxide-containing fatty acids. Active in vitro against epoxyeicosatrienoic acids (EETs) including 8,9-EET, 9,10-EET, 11,12-EET and 14,15-EET and leukotoxin.

**Summary**, from NCBI Gene [79852](https://www.ncbi.nlm.nih.gov/gene/79852):

> Enables epoxide hydrolase activity. Involved in epoxide metabolic process. Located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23760) · Entrez [79852](https://www.ncbi.nlm.nih.gov/gene/79852) · UniProt [Q9H6B9](https://www.uniprot.org/uniprotkb/Q9H6B9) · Ensembl [ENSG00000105131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105131)

## Data

Gene col 2549: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2549); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2549, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2549]; `tensor/DDL_lfc|DDL_z.npy` [2549]; `embed/gene_vectors.npy` [2549]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2549 or target_col == 2549). Every well: [[EPHX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
