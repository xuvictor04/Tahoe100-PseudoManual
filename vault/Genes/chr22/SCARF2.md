---
symbol: "SCARF2"
type: "gene"
col: 14406
ensembl_id: "ENSG00000244486"
name: "scavenger receptor class F member 2"
location: "22q11.21"
module: 47
arm: "+"
pooled_cpm: 3.45
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# SCARF2

*scavenger receptor class F member 2* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.73× (z +6.0, q 9e-07, up in 3 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.45× (z +4.3, q 0.003, up in 14 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.619× (z -5.5, q 2e-05, down in 14 of 45 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C-33 A 0.128×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WTIP]] (+0.52, fdr 3e-05), [[ERFL]] (+0.49, fdr 4e-05), [[FAAH]] (+0.48, fdr 3e-05); moves opposite to [[ARHGAP28]] (-0.36, fdr 6e-04), [[EPHA3]] (-0.36, fdr 3e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ASGR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14406.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.0 | 9e-07 | 3/7 (hTERT-HPNE, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +5.7 | 4e-06 | 2/6 (PANC-1, hTERT-HPNE) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +4.7 | 4e-04 | 4/16 (Hs 766T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +4.3 | 0.003 | 14/42 (C-33 A, HOP62, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.063 | 4/36 (HOP62, RKO, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.077 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.31× | +3.1 | 0.16 | 5/29 (A-172, C32, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14406.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C-33 A 0.128×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.619×** | -5.5 | 2e-05 | 14/45 (KATO III, NCI-H1573, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.721×** | -3.8 | 0.050 | 8/44 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.585× | -3.2 | 0.24 | 5/27 (BT-474, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.764× | -3.1 | 0.29 | 9/44 (A549, SNU-1, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 16.8 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.128× (z -9.0) |
| [[A-172 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.920 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WTIP]] | +0.52 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[ERFL]] | +0.49 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[FAAH]] | +0.48 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[TBKBP1]] | +0.48 | +0.49 / +0.31 | both halves | 2e-04 |  |
| [[MYO15A]] | +0.48 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[MSI1]] | +0.46 | +0.39 / +0.45 | both halves | 6e-05 |  |
| [[PHF2]] | +0.45 | +0.45 / +0.37 | both halves | 8e-05 |  |
| [[KNDC1]] | +0.44 | +0.40 / +0.45 | both halves | 4e-05 |  |
| [[KIAA1614]] | +0.44 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[B4GALT2]] | +0.43 | +0.31 / +0.43 | both halves | 2e-04 |  |
| [[GDPD3]] | +0.43 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[ARHGEF19]] | +0.43 | +0.42 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP28]] | -0.36 | -0.25 / -0.22 | both halves | 6e-04 |  |
| [[EPHA3]] | -0.36 | -0.28 / -0.33 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASGR1]] | B | ASGR1 activity raises SCARF2's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.48× lower at baseline in the lines without ASGR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[MLXIPL]] | B | MLXIPL activity lowers SCARF2's level | lines that do not express MLXIPL (13) vs lines expressing it (37) | 1.77× higher at baseline in the lines without MLXIPL | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: GRTP1, PLS1, LAMP3; maybe low, not absent |
| [[GAS6]] | B | GAS6 activity raises SCARF2's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without GAS6 | 0.057 | ⚠ within organs, on part of the lines |
| [[EBF4]] | B | EBF4 activity raises SCARF2's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without EBF4 | 0.091 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.399). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.8, -22.0); signed map (12.7, 13.5). **Vector** length 41.1, 3.98% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +4.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.4 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +0.9 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -1.5 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.5 | -5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.4 | -3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.0 | -0.0 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | scavenger receptor class F member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,424,584-20,437,826 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SREC-II, SREC2, HUMZD58C02 |
| Gene groups (HGNC) | Scavenger receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GP6](https://www.uniprot.org/uniprotkb/Q96GP6) (Scavenger receptor class F member 2):

> Probable adhesion protein, which mediates homophilic and heterophilic interactions. In contrast to SCARF1, it poorly mediates the binding and degradation of acetylated low density lipoprotein (Ac-LDL) (By similarity).

**Summary**, from NCBI Gene [91179](https://www.ncbi.nlm.nih.gov/gene/91179):

> The protein encoded by this gene is similar to SCARF1/SREC-I, a scavenger receptor protein that mediates the binding and degradation of acetylated low density lipoprotein (Ac-LDL). This protein has only little activity of internalizing modified low density lipoproteins (LDL), but it can interact with SCARF1 through its extracellular domain. The association of this protein with SCARF1 is suppressed by the presence of scavenger ligands. Alternatively spliced transcript variants encoding distinct …

**Accessions** — [HGNC:19869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19869) · Entrez [91179](https://www.ncbi.nlm.nih.gov/gene/91179) · UniProt [Q96GP6](https://www.uniprot.org/uniprotkb/Q96GP6) · Ensembl [ENSG00000244486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244486)

## Data

Gene col 14406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14406); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14406]; `tensor/DDL_lfc|DDL_z.npy` [14406]; `embed/gene_vectors.npy` [14406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14406 or target_col == 14406). Every well: [[SCARF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCARF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
