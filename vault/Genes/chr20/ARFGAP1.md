---
symbol: "ARFGAP1"
type: "gene"
col: 2094
ensembl_id: "ENSG00000101199"
name: "ARF GTPase activating protein 1"
location: "20q13.33"
module: 40
arm: "+"
pooled_cpm: 49.78
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ARFGAP1

*ARF GTPase activating protein 1* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.51× (z +4.4, q 0.005, up in 34 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.50× (z +4.3, q 0.005, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.573× (z -5.7, q 5e-06, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BET1L]] (+0.82, fdr 7e-06), [[SYVN1]] (+0.77, fdr 7e-06), [[RER1]] (+0.76, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SH3D21]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2094.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +4.4 | 0.005 | 34/48 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +4.3 | 0.005 | 25/48 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.014 | 26/48 (SHP-77, C-33 A, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.026 | 29/48 (COLO 205, NCI-H23, …) | two highest doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.35× | +3.2 | 0.12 | 27/48 (PANC-1, A-427, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.35× | +3.2 | 0.12 | 22/48 (BT-474, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.24× | +3.2 | 0.12 | 23/48 (LoVo, Hs 766T, …) | two highest doses | position effect removed |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | 1.33× | +3.1 | 0.14 | 23/49 (SNU-423, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2094.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.573×** | -5.7 | 5e-06 | 36/48 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.612×** | -5.3 | 4e-05 | 30/47 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.704×** | -5.0 | 9e-05 | 31/47 (NCI-H2347, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.647×** | -4.5 | 9e-04 | 27/40 (A549, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.659×** | -4.5 | 9e-04 | 30/48 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.763×** | -3.9 | 0.008 | 29/48 (HS-578T, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.751× | -3.1 | 0.17 | 21/48 (hTERT-HPNE, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2094. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 40.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.2) |
| [[LoVo (line)]] | wt | 48.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -12.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0997× (z -13.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 57.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -11.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 63.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 59.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 56.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -10.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 53.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 82.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 88.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 53.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2094), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BET1L]] | +0.82 | +0.80 / +0.79 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SYVN1]] | +0.77 | +0.77 / +0.72 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation |
| [[RER1]] | +0.76 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.76 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[SDHAP1-1]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[POFUT2]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[SURF4]] | +0.72 | +0.74 / +0.72 | both halves | 7e-06 | pathway: COPI-dependent Golgi-to-ER retrograde traffic; STRING 567 |
| [[DPH7]] | +0.72 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[CHPF2]] | +0.72 | +0.73 / +0.75 | both halves | 7e-06 | same gene group |
| [[TMED9]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 588 |
| [[SEC61A1]] | +0.71 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[NPRL2]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH3D21]] | C | SH3D21 activity raises ARFGAP1's level | lines that do not express SH3D21 (4) vs lines expressing it (46) | 1.28× lower at baseline in the lines without SH3D21 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000286677; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.695). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.2, -30.6); signed map (-49.9, 4.5). **Vector** length 130, 41.9% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.3 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.5 | +2.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.4 | +1.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +4.3 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +4.0 | +1.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.7 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.5 | +3.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.3 | +1.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.4 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -4.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.1 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.8 | -1.3 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -3.4 | -2.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.2 | -2.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.1 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ARF GTPase activating protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,272,785-63,289,790 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10767, bA261N11.3; previously ARF1GAP |
| Gene groups (HGNC) | ArfGAPs; MicroRNA protein coding host genes |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 15 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; COPI-dependent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6T3](https://www.uniprot.org/uniprotkb/Q8N6T3) (ADP-ribosylation factor GTPase-activating protein 1):

> GTPase-activating protein (GAP) for the ADP ribosylation factor 1 (ARF1). Involved in membrane trafficking and /or vesicle transport. Promotes hydrolysis of the ARF1-bound GTP and thus, is required for the dissociation of coat proteins from Golgi-derived membranes and vesicles, a prerequisite for vesicle's fusion with target compartment. Probably regulates ARF1-mediated transport via its interaction with the KDELR proteins and TMED2. Overexpression induces the redistribution of the entire Golgi …

**Summary**, from NCBI Gene [55738](https://www.ncbi.nlm.nih.gov/gene/55738):

> The protein encoded by this gene is a GTPase-activating protein, which associates with the Golgi apparatus and which interacts with ADP-ribosylation factor 1. The encoded protein promotes hydrolysis of ADP-ribosylation factor 1-bound GTP and is required for the dissociation of coat proteins from Golgi-derived membranes and vesicles. Dissociation of the coat proteins is required for the fusion of these vesicles with target compartments. The activity of this protein is stimulated by …

**Accessions** — [HGNC:15852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15852) · Entrez [55738](https://www.ncbi.nlm.nih.gov/gene/55738) · UniProt [Q8N6T3](https://www.uniprot.org/uniprotkb/Q8N6T3) · Ensembl [ENSG00000101199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101199)

## Data

Gene col 2094: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2094); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2094, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2094]; `tensor/DDL_lfc|DDL_z.npy` [2094]; `embed/gene_vectors.npy` [2094]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2094 or target_col == 2094). Every well: [[ARFGAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARFGAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
