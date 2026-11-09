---
symbol: "CYB5R2"
type: "gene"
col: 9295
ensembl_id: "ENSG00000166394"
name: "cytochrome b5 reductase 2"
location: "11p15.4"
module: 112
arm: "+"
pooled_cpm: 3.78
n_lines_expressing: 29
n_dd_up: 11
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# CYB5R2

*cytochrome b5 reductase 2* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.02× (z +13.1, q 3e-36, up in 13 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.482× (z -5.4, q 4e-05, down in 11 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNT6]] (+0.64, fdr 7e-06), [[TRAF1]] (+0.64, fdr 7e-06), [[GATM]] (+0.63, fdr 1e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[TFPI2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9295.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.02×** | +13.1 | 3e-36 | 13/22 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +8.2 | 7e-14 | 15/25 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.73×** | +8.1 | 1e-13 | 1/5 (PANC-1) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.54×** | +7.8 | 9e-13 | 7/13 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.31×** | +6.7 | 2e-09 | 15/24 (HS-578T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +6.0 | 2e-07 | 4/6 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +5.8 | 5e-07 | 9/16 (NCI-H23, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.1 | 3e-05 | 7/22 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.51×** | +3.4 | 0.032 | 6/14 (A-427, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.032 | 8/24 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.071 | 4/24 (NCI-H1573, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.45× | +3.1 | 0.10 | 7/21 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9295.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.482×** | -5.4 | 4e-05 | 11/25 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.598×** | -4.0 | 0.016 | 6/25 (NCI-H460, SK-MEL-2, …) | all doses, flat | position effect removed |
| [[RMC-6236 (drug)]] 5 µM |  | **0.408×** | -3.9 | 0.016 | 8/24 (SK-MEL-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.426×** | -3.7 | 0.025 | 7/24 (SK-MEL-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.758× | -3.2 | 0.12 | 7/25 (SK-MEL-2, PANC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | 0.683× | -3.2 | 0.12 | 3/25 (HS-578T, Hs 766T, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.672× | -3.2 | 0.12 | 5/24 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.688× | -3.1 | 0.12 | 7/25 (Hs 766T, H4, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.687× | -3.0 | 0.14 | 11/24 (SK-MEL-2, NCI-H460, …) | all doses, flat | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.776× | -3.0 | 0.14 | 8/25 (NCI-H23, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9295. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 25.9 | 0 | 4 | — | [[Binimetinib (drug)]] 5 µM 0.153× (z -10.1) |
| [[HS-578T (line)]] | alt | 11.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +14.0) | — |
| [[A-172 (line)]] | wt | 2.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.7× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 2.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +10.0) | — |
| [[A-427 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.795 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9295), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT6]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[TRAF1]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[GATM]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[IL31RA]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[SLC45A3]] | +0.61 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[GOLGA7B]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[B4GALT6]] | +0.61 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[LIF]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[IL1A]] | +0.60 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[ICAM2]] | +0.59 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[CXCL8]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[BCL2A1]] | +0.59 | +0.45 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TFPI2]] | B | CYB5R2 activity raises TFPI2's level | lines that do not express CYB5R2 (21) vs lines expressing it (29) | 2.34× lower at baseline in the lines without CYB5R2 | 0.099 | ⚠ within organs, on part of the lines; also absent: RP1, PI3, LINC02968 |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.0, 1.9); signed map (8.6, 38.8). **Vector** length 44.2, 8.56% of its response variance represented; |z| ≥ 3 in 527 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.53 to 11); *Interleukin-10 signaling* (reactome, mean cos +0.55 to 5); *KRAS signaling up* (hallmark, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +13.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.8 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +2.8 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.9 | +0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.8 | +0.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.0 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.3 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome b5 reductase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:7,665,100-7,677,222 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cytochrome b5 reductases; Flavoproteins |
| Reactome | 3 pathways, smallest: Erythrocytes take up carbon dioxide and release oxygen; O2/CO2 exchange in erythrocytes; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6BCY4](https://www.uniprot.org/uniprotkb/Q6BCY4) (NADH-cytochrome b5 reductase 2):

> NADH-cytochrome b5 reductases are involved in desaturation and elongation of fatty acids, cholesterol biosynthesis, drug metabolism, and, in erythrocyte, methemoglobin reduction (By similarity). Responsible for NADH-dependent lucigenin chemiluminescence in spermatozoa by reducing both lucigenin and 2-[4-iodophenyl]-3-[4-nitrophenyl]-5-[2,4-disulfophenyl]-2H tetrazolium monosodium salt (WST-1).

**Summary**, from NCBI Gene [51700](https://www.ncbi.nlm.nih.gov/gene/51700):

> The protein encoded by this gene belongs to the flavoprotein pyridine nucleotide cytochrome reductase family of proteins. Cytochrome b-type NAD(P)H oxidoreductases are implicated in many processes including cholesterol biosynthesis, fatty acid desaturation and elongation, and respiratory burst in neutrophils and macrophages. Cytochrome b5 reductases have soluble and membrane-bound forms that are the product of alternative splicing. In animal cells, the membrane-bound form binds to the …

**Accessions** — [HGNC:24376](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24376) · Entrez [51700](https://www.ncbi.nlm.nih.gov/gene/51700) · UniProt [Q6BCY4](https://www.uniprot.org/uniprotkb/Q6BCY4) · Ensembl [ENSG00000166394](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166394)

## Data

Gene col 9295: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9295); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9295, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9295]; `tensor/DDL_lfc|DDL_z.npy` [9295]; `embed/gene_vectors.npy` [9295]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9295 or target_col == 9295). Every well: [[CYB5R2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYB5R2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
