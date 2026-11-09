---
symbol: "NME9"
type: "gene"
col: 11179
ensembl_id: "ENSG00000181322"
name: "NME/NM23 family member 9"
location: "3q22.3"
module: 21
arm: "+"
pooled_cpm: 2.54
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# NME9

*NME/NM23 family member 9* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.09× (z +7.2, q 3e-10, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +6.4, q 3e-08, up in 12 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.676× (z -4.0, q 0.025, down in 8 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLJ40194]] (+0.66, fdr 7e-06), [[FAM217A]] (+0.65, fdr 1e-05), [[TMEM266]] (+0.64, fdr 7e-06); moves opposite to [[RNASEH1]] (-0.54, fdr 4e-05), [[POGK]] (-0.53, fdr 2e-05), [[APEX2]] (-0.53, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CHST9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +7.2 | 3e-10 | 1/2 (HOP62) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +6.7 | 7e-09 | 0/4 | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.4 | 3e-08 | 12/32 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.87×** | +6.4 | 3e-08 | 20/45 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +5.9 | 3e-07 | 18/46 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +5.3 | 1e-05 | 14/45 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.65×** | +5.1 | 3e-05 | 13/42 (A-427, H4, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +4.7 | 2e-04 | 13/46 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +4.6 | 3e-04 | 9/39 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +3.9 | 0.005 | 2/12 (HOP62, HS-578T) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.005 | 9/46 (NCI-H23, LoVo, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +3.6 | 0.016 | 2/11 (SHP-77, A-427) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.019 | 7/39 (SW480, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.025 | 4/41 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.056 | 8/45 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.37×** | +3.2 | 0.056 | 1/44 (NCI-H2030) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.062 | 2/43 (NCI-H2347, LS 180) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.073 | 8/29 (NCI-H1573, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.090 | 6/41 (SW480, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11179.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.676×** | -4.0 | 0.025 | 8/44 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.672×** | -3.9 | 0.025 | 11/42 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.690×** | -3.8 | 0.026 | 13/42 (NCI-H23, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.694×** | -3.7 | 0.026 | 3/47 (HCT15, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.721×** | -3.4 | 0.090 | 8/46 (NCI-H1792, AN3 CA, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | 0.743× | -3.1 | 0.21 | 7/31 (A-172, COLO 205, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLJ40194]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[FAM217A]] | +0.65 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[TMEM266]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[MAL2-AS1]] | +0.64 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SLC26A5]] | +0.62 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[SCN1A-AS1]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ZBTB20-AS5]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[RN7SL2]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[RN7SL1]] | +0.59 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[SLC23A1]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SPTBN4]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[EFHD1]] | +0.58 | +0.51 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNASEH1]] | -0.54 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[POGK]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[APEX2]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ELK4]] | -0.52 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[NIP7]] | -0.51 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[MTOR]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHST9]] | B | CHST9 activity raises NME9's level | lines that do not express CHST9 (18) vs lines expressing it (32) | 1.19× lower at baseline in the lines without CHST9 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC02015, PRKD1, MYO18B; maybe low, not absent |
| [[NRG4]] | B | NRG4 activity raises NME9's level | lines that do not express NRG4 (10) vs lines expressing it (40) | 1.28× lower at baseline in the lines without NRG4 | 0.074 | ⚠ within organs, on part of the lines; also absent: LHFPL6, ENSG00000288583; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, 30.6); signed map (35.1, 7.4). **Vector** length 37.6, 3.38% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +7.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +3.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -0.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | NME/NM23 family member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:138,261,437-138,329,886 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TXL-2, NM23-H9; previously TXNDC6 |
| Gene groups (HGNC) | NME/NM23 family; Thioredoxin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XW9](https://www.uniprot.org/uniprotkb/Q86XW9) (Thioredoxin domain-containing protein 6):

> May be a regulator of microtubule physiology.

**Summary**, from NCBI Gene [347736](https://www.ncbi.nlm.nih.gov/gene/347736):

> Predicted to enable nucleoside diphosphate kinase activity. Predicted to be involved in CTP biosynthetic process; GTP biosynthetic process; and UTP biosynthetic process. Predicted to be located in dynein axonemal particle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21343) · Entrez [347736](https://www.ncbi.nlm.nih.gov/gene/347736) · UniProt [Q86XW9](https://www.uniprot.org/uniprotkb/Q86XW9) · Ensembl [ENSG00000181322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181322)

## Data

Gene col 11179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11179); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11179]; `tensor/DDL_lfc|DDL_z.npy` [11179]; `embed/gene_vectors.npy` [11179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11179 or target_col == 11179). Every well: [[NME9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NME9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
