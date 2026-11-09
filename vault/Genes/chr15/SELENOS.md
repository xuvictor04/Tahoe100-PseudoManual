---
symbol: "SELENOS"
type: "gene"
col: 5253
ensembl_id: "ENSG00000131871"
name: "selenoprotein S"
location: "15q26.3"
module: 49
arm: "+"
pooled_cpm: 60.44
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SELENOS

*selenoprotein S* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.72× (z +4.4, q 0.006, up in 38 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1573 3.39×, COLO 205 5.52×; ⚠ cell-cycle shift, explains ~38% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.723× (z -4.4, q 0.005, down in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2347 0.443×, A-172 0.438×, NCI-H2030 0.457×, A498 0.508×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HM13]] (+0.80, fdr 7e-06), [[SEC61B]] (+0.76, fdr 7e-06), [[MYDGF]] (+0.73, fdr 7e-06); moves opposite to [[SUMO3]] (-0.57, fdr 6e-05), [[PPP2R1B]] (-0.57, fdr 3e-05), [[ZNF300]] (-0.56, fdr 2e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TMEM92-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5253.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1573 3.39×, COLO 205 5.52×; ⚠ cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +4.4 | 0.006 | 38/49 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.51×** | +3.9 | 0.023 | 34/48 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +3.8 | 0.023 | 19/39 (HepG2/C3A, C32, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.41× | +3.3 | 0.15 | 29/48 (C-33 A, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5253.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2347 0.443×, A-172 0.438×, NCI-H2030 0.457×, A498 0.508×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.723×** | -4.4 | 0.005 | 29/47 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.775× | -3.5 | 0.13 | 27/48 (NCI-H2347, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.780× | -3.3 | 0.13 | 28/48 (NCI-H661, AsPC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.786× | -3.3 | 0.13 | 23/48 (NCI-H1573, H4, …) | top dose only | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 61.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.0) |
| [[A498 (line)]] | wt | 112 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -8.7) |
| [[COLO 205 (line)]] | alt | 65.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.52× (z +9.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1573 (line)]] | alt | 92.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.39× (z +9.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2030 (line)]] | alt | 68.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 65.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.2) |
| [[A-427 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 69.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 128 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 97.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 80.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HM13]] | +0.80 | +0.75 / +0.77 | both halves | 7e-06 | STRING 729 |
| [[SEC61B]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[MYDGF]] | +0.73 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[SSR2]] | +0.73 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[OSBP]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ARFGAP3]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[SERP1]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[SLC33A1]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[COG3]] | +0.71 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[DNAJB9]] | +0.70 | +0.75 / +0.70 | both halves | 7e-06 | STRING 522 |
| [[ERLEC1]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 | STRING 472 |
| [[BET1L]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMO3]] | -0.57 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[PPP2R1B]] | -0.57 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[ZNF300]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TBL1XR1]] | -0.56 | -0.45 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity raises SELENOS's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without TMEM92-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[ADM2]] | B | ADM2 activity raises SELENOS's level | lines that do not express ADM2 (9) vs lines expressing it (41) | 1.26× lower at baseline in the lines without ADM2 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: CXADR, ARHGAP26, CFL1P1-1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.797). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.4, -35.7); signed map (-49.8, 12.1). **Vector** length 101, 36.3% of its response variance represented; |z| ≥ 3 in 556 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.62 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.62 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.62 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.3 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -4.0 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | +2.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Adenine (drug)]] 5 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | selenoprotein S |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:101,270,817-101,277,500 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SELS, MGC2553, SBBI8, AD-015, SEPS1; previously VIMP |
| Gene groups (HGNC) | Selenoproteins |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, INFLAMMATORY_RESPONSE |
| Reactome | 2 pathways, smallest: E3 ubiquitin ligases ubiquitinate target proteins; Protein ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQE4](https://www.uniprot.org/uniprotkb/Q9BQE4) (Selenoprotein S):

> Involved in the degradation process of misfolded endoplasmic reticulum (ER) luminal proteins. Participates in the transfer of misfolded proteins from the ER to the cytosol, where they are destroyed by the proteasome in a ubiquitin-dependent manner. Probably acts by serving as a linker between DERL1, which mediates the retrotranslocation of misfolded proteins into the cytosol, and the ATPase complex VCP, which mediates the translocation and ubiquitination.

**Summary**, from NCBI Gene [55829](https://www.ncbi.nlm.nih.gov/gene/55829):

> This gene encodes a transmembrane protein that is localized in the endoplasmic reticulum (ER). It is involved in the degradation process of misfolded proteins in the ER, and may also have a role in inflammation control. This protein is a selenoprotein, containing the rare amino acid selenocysteine (Sec). Sec is encoded by the UGA codon, which normally signals translation termination. The 3' UTRs of selenoprotein mRNAs contain a conserved stem-loop structure, designated the Sec insertion …

**Accessions** — [HGNC:30396](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30396) · Entrez [55829](https://www.ncbi.nlm.nih.gov/gene/55829) · UniProt [Q9BQE4](https://www.uniprot.org/uniprotkb/Q9BQE4) · Ensembl [ENSG00000131871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131871)

## Data

Gene col 5253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5253); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5253]; `tensor/DDL_lfc|DDL_z.npy` [5253]; `embed/gene_vectors.npy` [5253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5253 or target_col == 5253). Every well: [[SELENOS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SELENOS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
