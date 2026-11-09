---
symbol: "ENO4"
type: "gene"
col: 12003
ensembl_id: "ENSG00000188316"
name: "enolase 4"
location: "10q25.3"
module: 21
arm: "+"
pooled_cpm: 4.46
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ENO4

*enolase 4* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.67× (z +11.5, q 4e-28, up in 18 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +7.5, q 1e-11, up in 22 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ritonavir (drug)]] 0.5 µM: 0.725× (z -3.8, q 0.083, down in 12 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (A549 0.119×; ⚠ transcription drop); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0926×); [[Saquinavir (drug)]] 0.5 µM in 1 line (HT-29 0.101×); [[Canagliflozin (drug)]] 5 µM in 1 line (NCI-H1792 0.0771×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2CD5-AS1]] (+0.78, fdr 7e-06), [[SYNM-AS1]] (+0.74, fdr 7e-06), [[HSPA2-AS1]] (+0.73, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02269]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +11.5 | 4e-28 | 18/23 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +10.9 | 2e-25 | 6/6 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +7.5 | 1e-11 | 22/40 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +6.9 | 5e-10 | 2/10 (A498, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +5.1 | 4e-05 | 10/26 (HEC-1-A, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.021 | 6/36 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.023 | 2/44 (KATO III, SW480) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.5 | 0.035 | 0/10 | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.035 | 2/34 (A-172, Panc 03.27) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.22×** | +3.3 | 0.051 | 11/38 (SNU-423, NCI-H23, …) | rises with dose | composition shift |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.051 | 6/42 (CFPAC-1, HT-29, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.051 | 3/42 (SNU-423, BT-474, …) | rises with dose | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.077 | 7/42 (SNU-1, H4, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.088 | 5/45 (A549, HEC-1-A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12003.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (A549 0.119×; ⚠ transcription drop); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0926×); [[Saquinavir (drug)]] 0.5 µM in 1 line (HT-29 0.101×); [[Canagliflozin (drug)]] 5 µM in 1 line (NCI-H1792 0.0771×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ritonavir (drug)]] 0.5 µM |  | **0.725×** | -3.8 | 0.083 | 12/43 (LS 180, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.03 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.119× (z -8.9) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 4.50 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.101× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 3.62 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0771× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 2.88 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0926× (z -8.8) |
| [[A-172 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2CD5-AS1]] | +0.78 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[SYNM-AS1]] | +0.74 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.73 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.71 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[ZBTB20-AS5]] | +0.71 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[LINC02951]] | +0.71 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[CNGB3]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[C1orf56]] | +0.70 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[TTC36-AS1]] | +0.69 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[C12orf40]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02269]] | B | LINC02269 activity raises ENO4's level | lines that do not express LINC02269 (17) vs lines expressing it (33) | 1.17× lower at baseline in the lines without LINC02269 | 0.066 | ⚠ within organs, on part of the lines; also absent: HAND2-AS1, C19orf81, TUSC3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.743). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, 26.3); signed map (32.5, 4.3). **Vector** length 34.4, 2.83% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +2.4 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.1 | +2.8 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +1.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.5 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.9 | +0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -1.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | enolase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:116,849,499-116,911,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AC023283.3; previously C10orf134 |
| Gene groups (HGNC) | Enolases |
| Reactome | 4 pathways, smallest: Gluconeogenesis; Glycolysis; Glucose metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NNW6](https://www.uniprot.org/uniprotkb/A6NNW6) (Enolase 4):

> Enolase that catalyzes the conversion of 2-phosphoglycerate to phosphoenolpyruvate in glycolysis and the reverse reaction in gluconeogenesis (By similarity). May be required for sperm motility and function.

**Summary**, from NCBI Gene [387712](https://www.ncbi.nlm.nih.gov/gene/387712):

> Predicted to enable phosphopyruvate hydratase activity. Predicted to be involved in glycolytic process. Predicted to act upstream of or within cilium organization and flagellated sperm motility. Predicted to be located in sperm principal piece. Predicted to be part of phosphopyruvate hydratase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31670) · Entrez [387712](https://www.ncbi.nlm.nih.gov/gene/387712) · UniProt [A6NNW6](https://www.uniprot.org/uniprotkb/A6NNW6) · Ensembl [ENSG00000188316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188316)

## Data

Gene col 12003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12003); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12003]; `tensor/DDL_lfc|DDL_z.npy` [12003]; `embed/gene_vectors.npy` [12003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12003 or target_col == 12003). Every well: [[ENO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
