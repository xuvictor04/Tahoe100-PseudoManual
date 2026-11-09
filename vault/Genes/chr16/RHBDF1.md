---
symbol: "RHBDF1"
type: "gene"
col: 145
ensembl_id: "ENSG00000007384"
name: "rhomboid 5 homolog 1"
location: "16p13.3"
module: 138
arm: "+"
pooled_cpm: 8.19
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# RHBDF1

*rhomboid 5 homolog 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +7.6, q 2e-11, up in 27 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Darinaparsin (drug)]] 5 µM: 0.741× (z -4.5, q 0.004, down in 18 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP170B]] (+0.68, fdr 7e-06), [[FLNA]] (+0.61, fdr 1e-05), [[DMWD]] (+0.61, fdr 1e-05); moves opposite to [[SHPRH]] (-0.50, fdr 2e-05), [[NCK1]] (-0.49, fdr 8e-05), [[HEATR6]] (-0.47, fdr 1e-04).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPHA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 145.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +7.6 | 2e-11 | 27/41 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.03×** | +7.4 | 3e-11 | 30/46 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +6.9 | 9e-10 | 25/42 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.7 | 3e-04 | 18/40 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +4.7 | 4e-04 | 4/17 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +4.3 | 0.002 | 21/45 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +3.8 | 0.014 | 14/42 (HCT15, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.053 | 8/47 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 145.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Darinaparsin (drug)]] 5 µM |  | **0.741×** | -4.5 | 0.004 | 18/47 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.673×** | -4.0 | 0.015 | 18/45 (A-427, LOX-IMVI, …) | top dose only | position effect removed |
| [[Sulfatinib (drug)]] 5 µM |  | **0.683×** | -3.9 | 0.019 | 14/45 (hTERT-HPNE, AN3 CA, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.723×** | -3.4 | 0.082 | 15/45 (RPMI-7951, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.727×** | -3.4 | 0.082 | 10/44 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.804×** | -3.3 | 0.097 | 13/47 (HT-29, LoVo, …) | rises with dose | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | 0.813× | -3.1 | 0.14 | 9/44 (Hs 766T, C32, …) | top dose only |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | 0.748× | -3.1 | 0.14 | 16/45 (NCI-H460, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.48 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +9.1) | — |
| [[A549 (line)]] | wt | 6.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0848× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 7.25 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0657× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 7.71 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.119× (z -9.8) |
| [[PANC-1 (line)]] | alt | 4.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +10.7) | — |
| [[RKO (line)]] | wt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.16× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 4.80 | 0 | 1 | — | [[Adagrasib (drug)]] 5 µM 0.0342× (z -10.3) |
| [[SW480 (line)]] | alt | 9.07 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP170B]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[FLNA]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[DMWD]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[RIPOR1]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[IRGQ]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ZYX]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[IPO13]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[TRIM8]] | +0.57 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[CRTC2]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[TEPSIN]] | +0.57 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[SLC12A4]] | +0.56 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[AGRN]] | +0.55 | +0.55 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHPRH]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[NCK1]] | -0.49 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[HEATR6]] | -0.47 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[SDHB]] | -0.46 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[IQCB1]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[EDRF1]] | -0.45 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[UBE3D]] | -0.45 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHA2]] | B | EPHA2 activity raises RHBDF1's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 1.40× lower at baseline in the lines without EPHA2 | 0.070 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.2, -26.2); signed map (-8.5, 30.9). **Vector** length 75.2, 13.2% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.8 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +7.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | rhomboid 5 homolog 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:58,059-76,355 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EGFR-RS, FLJ2235, Dist1, iRhom1; previously C16orf8 |
| Gene groups (HGNC) | Rhomboid family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CC6](https://www.uniprot.org/uniprotkb/Q96CC6) (Inactive rhomboid protein 1):

> Regulates ADAM17 protease, a sheddase of the epidermal growth factor (EGF) receptor ligands and TNF, thereby plays a role in sleep, cell survival, proliferation, migration and inflammation. Does not exhibit any protease activity on its own. Regulator of proteosomal assembly by promoting formation of the proteosome assembly chaperone PSMG1-PSMG2 heterodimer, positively regulating proteosome activity.

**Summary**, from NCBI Gene [64285](https://www.ncbi.nlm.nih.gov/gene/64285):

> Predicted to enable growth factor binding activity and serine-type endopeptidase activity. Involved in several processes, including negative regulation of protein secretion; regulation of epidermal growth factor receptor signaling pathway; and regulation of proteasomal protein catabolic process. Located in Golgi membrane and endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20561](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20561) · Entrez [64285](https://www.ncbi.nlm.nih.gov/gene/64285) · UniProt [Q96CC6](https://www.uniprot.org/uniprotkb/Q96CC6) · Ensembl [ENSG00000007384](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007384)

## Data

Gene col 145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 145); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 145]; `tensor/DDL_lfc|DDL_z.npy` [145]; `embed/gene_vectors.npy` [145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 145 or target_col == 145). Every well: [[RHBDF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHBDF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
