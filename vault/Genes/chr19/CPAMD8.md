---
symbol: "CPAMD8"
type: "gene"
col: 8300
ensembl_id: "ENSG00000160111"
name: "C3 and PZP like alpha-2-macroglobulin domain containing 8"
location: "19p13.11"
module: 14
arm: "+"
pooled_cpm: 7.57
n_lines_expressing: 31
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CPAMD8

*C3 and PZP like alpha-2-macroglobulin domain containing 8* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.45× (z +18.2, q 0e+00, up in 17 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Lumateperone (tosylate) (drug)]] 0.5 µM: 0.649× (z -3.7, q 0.072, down in 8 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELOVL7]] (+0.68, fdr 7e-06), [[HSD11B1-AS1]] (+0.68, fdr 7e-06), [[RASGRP1]] (+0.67, fdr 7e-06).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C15orf48]] → it (grade B ⚠); 1 goes from it, the strongest it → [[IL23A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8300.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.45×** | +18.2 | 0e+00 | 17/24 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +11.7 | 3e-29 | 13/23 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.91×** | +9.2 | 7e-18 | 9/15 (SW 900, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +8.8 | 2e-16 | 6/12 (NCI-H2347, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.04×** | +8.7 | 4e-16 | 17/27 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.70×** | +8.6 | 9e-16 | 13/25 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +6.9 | 5e-10 | 1/9 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +6.1 | 9e-08 | 17/26 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +5.8 | 4e-07 | 12/23 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +5.3 | 8e-06 | 13/26 (Panc 03.27, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.60×** | +4.3 | 9e-04 | 12/25 (Panc 03.27, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.052 | 1/25 (NCI-H2030) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +3.1 | 0.098 | 3/20 (NCI-H1573, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8300.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | **0.649×** | -3.7 | 0.072 | 8/28 (NCI-H2347, AN3 CA, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.640×** | -3.6 | 0.072 | 9/24 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.663×** | -3.6 | 0.072 | 8/26 (SNU-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 24.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 43.9× (z +27.3) | [[Belinostat (drug)]] 5 µM 0.190× (z -8.5) ⚠ cell-cycle shift, explains ~76% of this change |
| [[NCI-H2347 (line)]] | alt | 5.94 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 36.3× (z +19.8) | — |
| [[A549 (line)]] | wt | 24.9 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.123× (z -10.9) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.148× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 112 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 6.08 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +12.5) | [[Ferulic acid (drug)]] 5 µM 0.0475× (z -9.5) |
| [[BT-474 (line)]] | alt | 42.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +15.7) | — |
| [[CFPAC-1 (line)]] | alt | 3.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +13.2) | — |
| [[HS-578T (line)]] | alt | 12.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 3.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.5× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +10.9) | — |
| [[A-172 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOVL7]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[HSD11B1-AS1]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[RASGRP1]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[DNAH17]] | +0.65 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CRTAC1]] | +0.65 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[NPHS1]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[HMGN2P46]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RBFOX3]] | +0.64 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[STX11]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[SERPINB7]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[GATM]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C15orf48]] | B | C15orf48 activity strengthens CPAMD8's drug response | lines that do not express C15orf48 (11) vs lines expressing it (17) | the lines without C15orf48 respond 0.21× as strongly (z diff +1.68); strongest at Homoharringtonine 0.5 µM: 0.56x vs 2.93x (z diff +4.6) | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG; target measured in part of the lines; the reference differs; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL23A]] | B | CPAMD8 activity raises IL23A's level | lines that do not express CPAMD8 (19) vs lines expressing it (31) | 1.32× lower at baseline in the lines without CPAMD8 | 0.073 | ⚠ within organs, on part of the lines; also absent: ZSCAN18, GNAO1, C11orf96; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.6, 0.4); signed map (40.1, 11.1). **Vector** length 71.8, 17.8% of its response variance represented; |z| ≥ 3 in 701 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +18.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +6.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -3.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -2.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | C3 and PZP like alpha-2-macroglobulin domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:16,892,951-17,026,815 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1283, VIP, K-CAP |
| Gene groups (HGNC) | C3 and PZP like, alpha-2-macroglobulin domain containing |
| Matched by | ensembl_id |

UniProt [Q8IZJ3](https://www.uniprot.org/uniprotkb/Q8IZJ3) carries no function annotation.

**Summary**, from NCBI Gene [27151](https://www.ncbi.nlm.nih.gov/gene/27151):

> This gene encodes a member of the protease inhibitor I39 (alpha-2-macroglobulin) family of proteins. These proteins are important in innate and acquired immunity. The encoded protein is membrane-associated and proteolytically processed to generate two chains. Mutations in this gene cause a form of anterior segment dysgenesis, a developmental disorder of the eye. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:23228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23228) · Entrez [27151](https://www.ncbi.nlm.nih.gov/gene/27151) · UniProt [Q8IZJ3](https://www.uniprot.org/uniprotkb/Q8IZJ3) · Ensembl [ENSG00000160111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160111)

## Data

Gene col 8300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8300); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8300]; `tensor/DDL_lfc|DDL_z.npy` [8300]; `embed/gene_vectors.npy` [8300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8300 or target_col == 8300). Every well: [[CPAMD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPAMD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
