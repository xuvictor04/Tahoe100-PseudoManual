---
symbol: "ELOB"
type: "gene"
col: 2360
ensembl_id: "ENSG00000103363"
name: "elongin B"
location: "16p13.3"
module: 48
arm: "+"
pooled_cpm: 32.97
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ELOB

*elongin B* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.78× (z +6.4, q 9e-08, up in 42 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.634× (z -4.0, q 0.037, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX6A1]] (+0.84, fdr 7e-06), [[ATP5MJ]] (+0.84, fdr 7e-06), [[MRPL41]] (+0.83, fdr 7e-06, ⚠ MRPL41 in the vector space only through flagged drug-doses), [[ANAPC11]] (+0.83, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.72, fdr 7e-06), [[PSME3IP1]] (-0.67, fdr 1e-05), [[DDX39B]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MT2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.78×** | +6.4 | 9e-08 | 42/43 (NCI-H1792, PANC-1, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.80×** | +6.0 | 4e-07 | 33/36 (NCI-H1792, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.53×** | +5.2 | 3e-05 | 37/41 (SW 900, PANC-1, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **2.09×** | +4.5 | 0.001 | 41/46 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +4.4 | 0.001 | 41/46 (COLO 205, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.98×** | +4.2 | 0.003 | 36/48 (HOP62, SW480, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.87×** | +3.8 | 0.011 | 39/46 (PANC-1, NCI-H460, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2360.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.634×** | -4.0 | 0.037 | 36/47 (AsPC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6A1]] | +0.84 | +0.78 / +0.77 | both halves | 7e-06 |  |
| [[ATP5MJ]] | +0.84 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[MRPL41]] ⚠ | +0.83 | +0.73 / +0.81 | both halves | 7e-06 | STRING 422; ⚠ in the vector space only through flagged drug-doses |
| [[ANAPC11]] | +0.83 | +0.75 / +0.76 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 661 |
| [[TMEM256]] | +0.80 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[UQCR11]] | +0.80 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[ROMO1]] | +0.80 | +0.71 / +0.81 | both halves | 7e-06 | STRING 622 |
| [[C4orf48]] | +0.80 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[BBLN]] | +0.78 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[SNRPD2]] | +0.77 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[TOMM7]] | +0.77 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[COX7C]] | +0.77 | +0.68 / +0.80 | both halves | 7e-06 |  |
| [[ATP5MK]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.72 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[PSME3IP1]] | -0.67 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[DDX39B]] | -0.67 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[HNRNPU]] | -0.65 | -0.53 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MT2A]] | B | MT2A activity lowers ELOB's level | lines that do not express MT2A (9) vs lines expressing it (41) | 1.33× higher at baseline in the lines without MT2A | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.822). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.4, -19.5); signed map (-33.8, 7.9). **Vector** length 63.5, 21.5% of its response variance represented; |z| ≥ 3 in 441 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.64 to 31); *Respiratory electron transport* (reactome, mean cos +0.63 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.64 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.3 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +2.7 | +3.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | -0.2 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM |  | +1.0 | +0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +0.9 | +0.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -3.8 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -3.7 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -3.4 | +6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -0.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | +0.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.8 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | elongin B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,771,414-2,777,289 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SIII; previously TCEB2 |
| Gene groups (HGNC) | Elongin complex |
| Reactome | 44 pathways, smallest: Evasion by RSV of host interferon responses; Inactivation of CSF3 (G-CSF) signaling; Signaling by CSF3 (G-CSF) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15370](https://www.uniprot.org/uniprotkb/Q15370) (Elongin-B):

> Component of the Elongin complex, also known as SIII, a general transcription elongation factor that increases the RNA polymerase II transcription elongation past template-encoded arresting sites; subunit A is transcriptionally active and its transcription activity is strongly enhanced by binding to the dimeric complex of the SIII regulatory subunits B and C (Elongin BC complex). In embryonic stem cells, the elongin BC complex is recruited by EPOP to Polycomb group (PcG) target genes in order …

**Summary**, from NCBI Gene [6923](https://www.ncbi.nlm.nih.gov/gene/6923):

> This gene encodes the protein elongin B, which is a subunit of the transcription factor B (SIII) complex. The SIII complex is composed of elongins A/A2, B and C. It activates elongation by RNA polymerase II by suppressing transient pausing of the polymerase at many sites within transcription units. Elongin A functions as the transcriptionally active component of the SIII complex, whereas elongins B and C are regulatory subunits. Elongin A2 is specifically expressed in the testis, and capable of …

**Accessions** — [HGNC:11619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11619) · Entrez [6923](https://www.ncbi.nlm.nih.gov/gene/6923) · UniProt [Q15370](https://www.uniprot.org/uniprotkb/Q15370) · Ensembl [ENSG00000103363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103363)

## Data

Gene col 2360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2360); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2360]; `tensor/DDL_lfc|DDL_z.npy` [2360]; `embed/gene_vectors.npy` [2360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2360 or target_col == 2360). Every well: [[ELOB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELOB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
