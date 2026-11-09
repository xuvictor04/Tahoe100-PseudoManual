---
symbol: "MSANTD1"
type: "gene"
col: 12070
ensembl_id: "ENSG00000188981"
name: "Myb/SANT DNA binding domain containing 1"
location: "4p16.3"
module: 47
arm: "+"
pooled_cpm: 2.55
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# MSANTD1

*Myb/SANT DNA binding domain containing 1* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.48× (z +6.4, q 8e-08, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.27× (z +6.1, q 2e-07, up in 26 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.309× (z -8.8, q 6e-16, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHX3]] (+0.80, fdr 7e-06), [[RAPSN]] (+0.79, fdr 7e-06), [[LINC02803]] (+0.79, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[XG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +6.4 | 8e-08 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.27×** | +6.1 | 2e-07 | 26/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +6.1 | 2e-07 | 14/35 (HT-29, A498, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.90×** | +4.8 | 3e-04 | 13/41 (HT-29, NCI-H1573, …) | two highest doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.87×** | +4.7 | 3e-04 | 12/47 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +4.6 | 5e-04 | 1/5 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.90×** | +4.5 | 5e-04 | 13/39 (A498, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +4.2 | 0.001 | 14/43 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.76×** | +4.2 | 0.001 | 13/43 (NCI-H1573, HOP62, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.74×** | +3.9 | 0.005 | 7/42 (A-172, C32, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +3.9 | 0.005 | 15/45 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.062 | 8/35 (HCT15, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12070.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.309×** | -8.8 | 6e-16 | 30/45 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.331×** | -8.3 | 3e-14 | 29/44 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.394×** | -7.0 | 5e-10 | 22/27 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.576×** | -4.2 | 0.004 | 18/43 (NCI-H1573, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Bexarotene (drug)]] 5 µM |  | **0.626×** | -3.5 | 0.046 | 10/45 (AN3 CA, NCI-H460, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.617×** | -3.4 | 0.054 | 14/39 (J82, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.424×** | -3.4 | 0.058 | 13/38 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.651×** | -3.2 | 0.077 | 10/45 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.653×** | -3.2 | 0.077 | 9/44 (A-172, AN3 CA, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.579×** | -3.1 | 0.097 | 15/44 (AsPC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.665× | -3.1 | 0.10 | 16/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.76 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 3.97 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0662× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 5.17 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0863× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 4.45 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0797× (z -8.8) |
| [[A-172 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.966 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.748 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHX3]] | +0.80 | +0.82 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[RAPSN]] | +0.79 | +0.78 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[LINC02803]] | +0.79 | +0.83 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TMEM25]] | +0.78 | +0.76 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[TTC36]] | +0.78 | +0.75 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[MPP4]] | +0.77 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[LINC02133]] | +0.77 | +0.75 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[OIT3]] | +0.76 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[SPTBN5]] | +0.76 | +0.71 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[SLC22A20P]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[CDKL4]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[LINC02236]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XG]] | B | XG activity raises MSANTD1's level | lines that do not express XG (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without XG | 0.019 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[ADORA1]] | B | ADORA1 activity raises MSANTD1's level | lines that do not express ADORA1 (7) vs lines expressing it (43) | 1.38× lower at baseline in the lines without ADORA1 | 0.049 | ⚠ within organs, on part of the lines; also absent: DRAM1, HHAT, SUGCT; maybe low, not absent |
| [[SPOCK2]] | B | SPOCK2 activity raises MSANTD1's level | lines that do not express SPOCK2 (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without SPOCK2 | 0.083 | ⚠ within organs, on part of the lines; also absent: UACA, MPP4, GLIPR2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.831). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.0, -14.5); signed map (17.7, 11.3). **Vector** length 63.3, 9.49% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.6 | +4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.5 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +1.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | -8.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -8.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -4.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.5 | -3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | Myb/SANT DNA binding domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:3,244,369-3,271,738 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOC345222; previously C4orf44 |
| Gene groups (HGNC) | Myb/SANT domain containing |
| Matched by | ensembl_id |

UniProt [Q6ZTZ1](https://www.uniprot.org/uniprotkb/Q6ZTZ1) carries no function annotation.

**Summary**, from NCBI Gene [345222](https://www.ncbi.nlm.nih.gov/gene/345222):

> Predicted to be involved in positive regulation of DNA-templated transcription. Predicted to be active in nuclear body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33741](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33741) · Entrez [345222](https://www.ncbi.nlm.nih.gov/gene/345222) · UniProt [Q6ZTZ1](https://www.uniprot.org/uniprotkb/Q6ZTZ1) · Ensembl [ENSG00000188981](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188981)

## Data

Gene col 12070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12070); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12070]; `tensor/DDL_lfc|DDL_z.npy` [12070]; `embed/gene_vectors.npy` [12070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12070 or target_col == 12070). Every well: [[MSANTD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSANTD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
