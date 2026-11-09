---
symbol: "DDX12P"
type: "gene"
col: 13226
ensembl_id: "ENSG00000214826"
name: "DEAD/H-box helicase 12, pseudogene"
location: "12p13.31"
module: 6
arm: "+"
pooled_cpm: 4.59
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# DDX12P

*DEAD/H-box helicase 12, pseudogene* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.90× (z +6.0, q 1e-06, up in 18 of 45 measured lines) ⚠ cell-cycle shift, explains ~66% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.49× (z +3.7, q 0.022, up in 10 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.605× (z -4.7, q 0.001, down in 17 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX11]] (+0.88, fdr 7e-06), [[RAD54L]] (+0.87, fdr 7e-06), [[FANCI]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.90×** | +6.0 | 1e-06 | 18/45 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.68×** | +4.8 | 3e-04 | 13/44 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.66×** | +4.7 | 5e-04 | 14/44 (LOX-IMVI, NCI-H1792, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.57×** | +4.0 | 0.008 | 12/28 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.022 | 10/44 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | **1.47×** | +3.5 | 0.051 | 0/5 | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13226.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.605×** | -4.7 | 0.001 | 17/43 (HEC-1-A, C-33 A, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.611×** | -4.6 | 0.001 | 13/44 (HEC-1-A, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.662×** | -3.8 | 0.022 | 13/42 (MIA PaCa-2, A-427, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.753×** | -3.7 | 0.022 | 12/37 (NCI-H23, SW480, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.669×** | -3.7 | 0.022 | 17/37 (SW480, A498, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | 0.782× | -3.2 | 0.12 | 15/44 (LS 180, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.71 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[A498 (line)]] | wt | 4.61 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0972× (z -9.4) |
| [[KATO III (line)]] | alt | 4.52 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0600× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 7.61 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -9.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW1417 (line)]] | alt | 4.29 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0625× (z -8.8) |
| [[A-172 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.887 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX11]] | +0.88 | +0.85 / +0.87 | both halves | 7e-06 | same gene group |
| [[RAD54L]] | +0.87 | +0.87 / +0.83 | both halves | 7e-06 |  |
| [[FANCI]] | +0.86 | +0.85 / +0.82 | both halves | 7e-06 |  |
| [[RFC4]] | +0.84 | +0.85 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[FANCA]] | +0.84 | +0.81 / +0.82 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.84 | +0.82 / +0.79 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.83 | +0.78 / +0.82 | both halves | 7e-06 |  |
| [[EXO1]] | +0.83 | +0.80 / +0.80 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.83 | +0.80 / +0.82 | both halves | 7e-06 |  |
| [[BLM]] | +0.83 | +0.81 / +0.80 | both halves | 7e-06 |  |
| [[CENPK]] | +0.83 | +0.79 / +0.81 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.82 | +0.78 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises DDX12P's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.07× lower at baseline in the lines without E2F8 | 0.035 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises DDX12P's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.17× lower at baseline in the lines without CDC25A | 0.066 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises DDX12P's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.71× lower at baseline in the lines without E2F2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers DDX12P's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LYPD6]] | B | LYPD6 activity raises DDX12P's level | lines that do not express LYPD6 (15) vs lines expressing it (35) | 1.75× lower at baseline in the lines without LYPD6 | 0.091 | ⚠ within organs, on part of the lines; also absent: LYPD6B, JPH1, NRN1 |
| [[DSCC1]] | C | DSCC1 activity raises DDX12P's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.63× lower at baseline in the lines without DSCC1 | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.875). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.0, -44.6); signed map (-36.8, -43.1). **Vector** length 70.2, 12.2% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.65 to 65); *DNA strand elongation* (reactome, mean cos +0.69 to 28); *DNA Replication* (reactome, mean cos +0.67 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +2.0 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.7 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +1.7 | +6.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | +2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.2 | +2.4 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.1 | +2.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.1 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.1 | -3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.7 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.9 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -3.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | DEAD/H-box helicase 12, pseudogene |
| Locus type | pseudogene |
| Location | 12p13.31 — chr12:9,418,673-9,448,229 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Also known as | CHLR2; previously DDX12 |
| Gene groups (HGNC) | DEAD-box helicases; Unitary pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92771](https://www.uniprot.org/uniprotkb/Q92771) (Putative ATP-dependent DNA helicase DDX12):

> DNA helicase involved in cellular proliferation. Probably required for maintaining the chromosome segregation (By similarity).

**Summary**, from NCBI Gene [440081](https://www.ncbi.nlm.nih.gov/gene/440081):

> Predicted to enable DNA helicase activity. Predicted to be involved in establishment of sister chromatid cohesion. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:2737](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2737) · Entrez [440081](https://www.ncbi.nlm.nih.gov/gene/440081) · UniProt [Q92771](https://www.uniprot.org/uniprotkb/Q92771) · Ensembl [ENSG00000214826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214826)

## Data

Gene col 13226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13226); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13226]; `tensor/DDL_lfc|DDL_z.npy` [13226]; `embed/gene_vectors.npy` [13226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13226 or target_col == 13226). Every well: [[DDX12P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX12P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
