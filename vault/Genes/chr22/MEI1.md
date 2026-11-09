---
symbol: "MEI1"
type: "gene"
col: 9409
ensembl_id: "ENSG00000167077"
name: "meiotic double-stranded break formation protein 1"
location: "22q13.2"
module: 53
arm: "+"
pooled_cpm: 3.26
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# MEI1

*meiotic double-stranded break formation protein 1* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.64× (z +12.3, q 5e-32, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +10.9, q 6e-25, up in 18 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.560× (z -6.4, q 7e-08, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC26A4]] (+0.71, fdr 7e-06), [[GRIK5]] (+0.66, fdr 7e-06), [[FAM66C]] (+0.65, fdr 1e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SSC5D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.64×** | +12.3 | 5e-32 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +10.9 | 6e-25 | 18/33 (NCI-H2347, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +9.8 | 3e-20 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +8.6 | 8e-16 | 2/10 (J82, HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.003 | 6/35 (SHP-77, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.40×** | +3.7 | 0.021 | 2/23 (A549, HEC-1-A) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9409.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.560×** | -6.4 | 7e-08 | 18/46 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.678×** | -4.3 | 0.004 | 12/43 (NCI-H1792, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.691×** | -4.1 | 0.008 | 13/38 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.517×** | -3.8 | 0.019 | 7/23 (PANC-1, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.714×** | -3.7 | 0.021 | 14/43 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.681×** | -3.7 | 0.022 | 11/41 (NCI-H2030, NCI-H1792, …) | two highest doses | composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | **0.725×** | -3.5 | 0.032 | 8/43 (A-172, HCT15, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.742×** | -3.3 | 0.066 | 9/43 (NCI-H1792, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.734×** | -3.2 | 0.074 | 11/39 (LOX-IMVI, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.724× | -3.1 | 0.11 | 2/44 (NCI-H23, MIA PaCa-2) | top dose only | plate-row cell shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.759× | -3.1 | 0.11 | 11/37 (NCI-H2030, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 3.21 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0807× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 4.01 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.0503× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 1.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0558× (z -9.6) |
| [[A-172 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.957 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.923 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.879 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC26A4]] | +0.71 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[FAM66C]] | +0.65 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[XG]] | +0.64 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PPEF1]] | +0.63 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[MYO15A]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[AZU1]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MYO1F]] | +0.62 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[HVCN1]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[TMPRSS9]] | +0.62 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[RELA-DT]] | +0.62 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[ASGR1]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSC5D]] | B | SSC5D activity lowers MEI1's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.37× higher at baseline in the lines without SSC5D | 0.071 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[LINC02026]] | B | LINC02026 activity raises MEI1's level | lines that do not express LINC02026 (8) vs lines expressing it (42) | 1.48× lower at baseline in the lines without LINC02026 | 0.091 | ⚠ within organs, on part of the lines; also absent: ASRGL1, ENSG00000256673 |
| [[PSMB5]] | B | PSMB5 activity raises MEI1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NRAS]] | C | NRAS activity raises MEI1's level | recorded gain-of-function mutation of NRAS in 7 lines vs 43 not recorded | 2.63× higher at baseline in the NRAS-altered lines | 0.499 over the table, 0.062 within its group | ⚠ within its group only (a lead); within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.5, -12.6); signed map (23.0, 12.9). **Vector** length 41.7, 4.35% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +0.4 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.9 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -6.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.9 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.6 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | meiotic double-stranded break formation protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,699,503-41,799,456 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC40042, SPATA38 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TIA1](https://www.uniprot.org/uniprotkb/Q5TIA1) (Meiosis inhibitor protein 1):

> Required for normal meiotic chromosome synapsis. May be involved in the formation of meiotic double-strand breaks (DSBs) in spermatocytes (By similarity).

**Summary**, from NCBI Gene [150365](https://www.ncbi.nlm.nih.gov/gene/150365):

> Predicted to be involved in meiosis I. Predicted to act upstream of or within germ cell development; meiotic nuclear division; and meiotic spindle organization. Implicated in gestational trophoblastic neoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28613](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28613) · Entrez [150365](https://www.ncbi.nlm.nih.gov/gene/150365) · UniProt [Q5TIA1](https://www.uniprot.org/uniprotkb/Q5TIA1) · Ensembl [ENSG00000167077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167077)

## Data

Gene col 9409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9409); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9409]; `tensor/DDL_lfc|DDL_z.npy` [9409]; `embed/gene_vectors.npy` [9409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9409 or target_col == 9409). Every well: [[MEI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
