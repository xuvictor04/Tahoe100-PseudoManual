---
symbol: "GOLGA6L9"
type: "gene"
col: 12505
ensembl_id: "ENSG00000197978"
name: "golgin A6 family like 9"
location: "15q25.2"
module: 180
arm: "+"
pooled_cpm: 8.75
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# GOLGA6L9

*golgin A6 family like 9* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.07× (z +5.9, q 2e-06, up in 21 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.88× (z +5.1, q 7e-05, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.287× (z -4.4, q 0.006, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2Q2P2]] (+0.71, fdr 1e-05, ⚠ same locus), [[MAP2K2]] (+0.71, fdr 7e-06), [[UBE2Q2P2-1]] (+0.66, fdr 1e-05, ⚠ same locus), [[ENO2]] (+0.65, fdr 3e-05), [[SLC25A29]] (+0.64, fdr 1e-05); moves opposite to [[DR1]] (-0.66, fdr 7e-06), [[FGD5-AS1]] (-0.60, fdr 1e-05), [[C6orf120]] (-0.60, fdr 4e-05).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EPIC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +5.9 | 2e-06 | 21/33 (HEC-1-A, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +5.1 | 7e-05 | 29/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +5.1 | 7e-05 | 9/13 (A498, J82, …) | two highest doses | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +4.0 | 0.007 | 22/47 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.018 | 17/47 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +3.5 | 0.042 | 23/44 (LoVo, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.52×** | +3.4 | 0.062 | 17/45 (SW48, NCI-H460, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.66×** | +3.3 | 0.065 | 6/42 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +3.3 | 0.065 | 11/36 (NCI-H2030, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.46× | +3.0 | 0.13 | 9/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 2.36× | +3.0 | 0.13 | 3/21 (KATO III, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12505.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.287×** | -4.4 | 0.006 | 26/47 (HT-29, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.351×** | -3.7 | 0.060 | 24/43 (KATO III, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.656×** | -3.4 | 0.096 | 18/47 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.659×** | -3.4 | 0.096 | 20/47 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.671× | -3.2 | 0.13 | 16/47 (NCI-H2347, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 6.66 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0961× (z -8.7) |
| [[A-172 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2Q2P2]] | +0.71 | +0.52 / +0.71 | both halves | 1e-05 | ⚠ same locus (9.7 kb, same strand: neighbours can correlate without regulation) |
| [[MAP2K2]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[UBE2Q2P2-1]] | +0.66 | +0.52 / +0.58 | both halves | 1e-05 | ⚠ same locus (10.4 kb, same strand: neighbours can correlate without regulation) |
| [[ENO2]] | +0.65 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[SLC25A29]] | +0.64 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MKNK2]] | +0.63 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[PKD1]] | +0.61 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[PTPRF]] | +0.60 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[PPP2R5B]] | +0.60 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[LIN7B]] | +0.59 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[PPFIA1]] | +0.59 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[SNHG7]] | +0.58 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[PHF1]] | +0.58 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[ATG4B]] | +0.58 | +0.36 / +0.56 | both halves | 1e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DR1]] | -0.66 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[FGD5-AS1]] | -0.60 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[C6orf120]] | -0.60 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[TFAM]] | -0.59 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[TMEM9B]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[MBNL3]] | -0.59 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.57 | -0.29 / -0.57 | both halves | 3e-04 |  |
| [[CHRAC1]] | -0.56 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[LEPROT]] | -0.56 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[MOB1A]] | -0.55 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[ERLIN2]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[SF3B4]] | -0.55 | -0.40 / -0.58 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPIC1]] | B | EPIC1 activity raises GOLGA6L9's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 1.40× lower at baseline in the lines without EPIC1 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[HDAC6]] | B | HDAC6 activity lowers GOLGA6L9's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-4.0, -19.3); signed map (-28.2, 2.0). **Vector** length 74.0, 16.3% of its response variance represented; |z| ≥ 3 in 569 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.8 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +2.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.2 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +0.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +2.8 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -0.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | golgin A6 family like 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:82,429,816-82,439,153 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously GOLGA6L20 |
| Gene groups (HGNC) | Golgin A6 and A8 families |
| Matched by | ensembl_id |

UniProt [A6NEM1](https://www.uniprot.org/uniprotkb/A6NEM1) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:37229](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37229) · Entrez [440295](https://www.ncbi.nlm.nih.gov/gene/440295) · UniProt [A6NEM1](https://www.uniprot.org/uniprotkb/A6NEM1) · Ensembl [ENSG00000197978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197978)

## Data

Gene col 12505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12505); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12505]; `tensor/DDL_lfc|DDL_z.npy` [12505]; `embed/gene_vectors.npy` [12505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12505 or target_col == 12505). Every well: [[GOLGA6L9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA6L9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
