---
symbol: "MCRIP2"
type: "gene"
col: 10247
ensembl_id: "ENSG00000172366"
name: "MAPK regulated corepressor interacting protein 2"
location: "16p13.3"
module: 58
arm: "+"
pooled_cpm: 7.69
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# MCRIP2

*MAPK regulated corepressor interacting protein 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.43× (z +7.3, q 1e-10, up in 25 of 30 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 5.05×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.593× (z -6.1, q 5e-07, down in 23 of 39 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAGHL]] (+0.69, fdr 1e-05), [[NME3]] (+0.66, fdr 1e-05), [[MRPL34]] (+0.61, fdr 1e-05); moves opposite to [[LAMC1]] (-0.52, fdr 3e-04), [[CCDC50]] (-0.51, fdr 6e-05), [[TARDBP]] (-0.47, fdr 3e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CAMKK1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10247.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 5.05×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +7.3 | 1e-10 | 25/30 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +6.2 | 2e-07 | 12/15 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.89×** | +5.3 | 3e-05 | 21/35 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +4.5 | 0.001 | 11/22 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | 1.52× | +3.2 | 0.15 | 13/44 (LS 180, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10247.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.593×** | -6.1 | 5e-07 | 23/39 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.559×** | -4.8 | 4e-04 | 25/45 (RKO, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.364×** | -4.1 | 0.009 | 19/40 (KATO III, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.394×** | -3.7 | 0.025 | 16/45 (A498, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.656×** | -3.5 | 0.053 | 12/45 (AsPC-1, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.671×** | -3.3 | 0.088 | 18/43 (SHP-77, HS-578T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pyridoxine (drug)]] 5 µM |  | 0.765× | -3.2 | 0.13 | 13/44 (H4, NCI-H1792, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.465× | -3.1 | 0.14 | 13/43 (BT-474, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.0) |
| [[HOP62 (line)]] | alt | 4.00 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0652× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 6.68 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0945× (z -9.4) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H460 (line)]] | wt | 9.48 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.05× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.2) |
| [[SW48 (line)]] | wt | 12.9 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0600× (z -9.2) |
| [[A-172 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 16 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAGHL]] | +0.69 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[NME3]] | +0.66 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[MRPL34]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[PUSL1]] | +0.60 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[ANTKMT]] | +0.59 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[MINCR]] | +0.57 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[C15orf61]] ⚠ | +0.56 | +0.43 / +0.53 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS34]] | +0.56 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[NTHL1]] | +0.55 | +0.24 / +0.60 | both halves | 4e-04 |  |
| [[AKR1A1]] | +0.55 | +0.27 / +0.54 | both halves | 3e-04 |  |
| [[RANGRF]] | +0.55 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[PDP2]] | +0.55 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[NR2F6]] | +0.54 | +0.33 / +0.53 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMC1]] | -0.52 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[CCDC50]] | -0.51 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[TARDBP]] | -0.47 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[DDX5]] | -0.46 | -0.26 / -0.42 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMKK1]] | C | CAMKK1 activity raises MCRIP2's level | lines that do not express CAMKK1 (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without CAMKK1 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CKAP4, ADGRB2, POGLUT3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.2, -16.2); signed map (-31.0, 4.9). **Vector** length 48.5, 7.33% of its response variance represented; |z| ≥ 3 in 564 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | -1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | -0.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +1.7 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.4 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -2.9 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | MAPK regulated corepressor interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:636,817-648,474 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15416; previously C16orf14, FAM195A |
| Matched by | ensembl_id |

UniProt [Q9BUT9](https://www.uniprot.org/uniprotkb/Q9BUT9) carries no function annotation.

**Summary**, from NCBI Gene [84331](https://www.ncbi.nlm.nih.gov/gene/84331):

> Predicted to enable RNA binding activity. Predicted to act upstream of or within several processes, including cold-induced thermogenesis; oxoacid metabolic process; and response to cold. Located in cytoplasmic stress granule and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14142) · Entrez [84331](https://www.ncbi.nlm.nih.gov/gene/84331) · UniProt [Q9BUT9](https://www.uniprot.org/uniprotkb/Q9BUT9) · Ensembl [ENSG00000172366](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172366)

## Data

Gene col 10247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10247); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10247]; `tensor/DDL_lfc|DDL_z.npy` [10247]; `embed/gene_vectors.npy` [10247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10247 or target_col == 10247). Every well: [[MCRIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCRIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
