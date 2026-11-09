---
symbol: "PSMA7"
type: "gene"
col: 2086
ensembl_id: "ENSG00000101182"
name: "proteasome 20S subunit alpha 7"
location: "20q13.33"
module: 24
arm: "+"
pooled_cpm: 165.53
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# PSMA7

*proteasome 20S subunit alpha 7* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.33× (z +7.1, q 1e-09, up in 43 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.31× (z +5.1, q 5e-05, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOL7]] (+0.69, fdr 1e-05, ⚠ NOL7 in the vector space only through flagged drug-doses), [[SSNA1]] (+0.67, fdr 7e-06), [[PSMB6]] (+0.64, fdr 7e-06), [[FAM241B]] (+0.63, fdr 1e-05); moves opposite to [[PTBP1]] (-0.60, fdr 6e-05), [[GANAB]] (-0.60, fdr 1e-05), [[DDX39B]] (-0.60, fdr 4e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2086.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.33×** | +7.1 | 1e-09 | 43/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **4.12×** | +6.5 | 2e-08 | 48/49 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.31×** | +5.1 | 5e-05 | 47/48 (COLO 205, HT-29, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.38×** | +4.9 | 1e-04 | 43/45 (NCI-H1792, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.01×** | +4.3 | 0.002 | 46/48 (COLO 205, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +4.1 | 0.004 | 43/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +3.9 | 0.007 | 42/48 (COLO 205, LoVo, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.76×** | +3.3 | 0.061 | 39/48 (AsPC-1, SW1417, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.76×** | +3.3 | 0.061 | 41/48 (HT-29, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.71×** | +3.2 | 0.088 | 38/47 (NCI-H1792, COLO 205, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.43×** | +3.1 | 0.093 | 46/48 (HT-29, NCI-H460, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.71 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 112 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.71× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HCT15 (line)]] | alt | 88.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.88× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[KATO III (line)]] | alt | 241 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.48× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 122 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 120 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.74× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 144 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.53× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 194 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 222 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 165 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 216 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 91.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 131 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 192 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 253 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 216 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 116 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 134 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 331 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 167 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 312 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 151 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 15 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOL7]] ⚠ | +0.69 | +0.53 / +0.72 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SSNA1]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 | pathway: G2/M Transition; STRING 484 |
| [[PSMB6]] | +0.64 | +0.66 / +0.68 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[FAM241B]] | +0.63 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ADRM1]] | +0.63 | +0.70 / +0.60 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 937 |
| [[PFDN4]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[NDUFB9]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | +0.61 | +0.30 / +0.72 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[LSM10]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[POLR2J]] ⚠ | +0.59 | +0.32 / +0.66 | both halves | 2e-04 | pathway: HIV Infection; ⚠ in the vector space only through flagged drug-doses |
| [[GADD45GIP1]] | +0.59 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | +0.59 | +0.24 / +0.71 | both halves | 5e-04 | pathway: Metabolism of amino acids and derivatives; ⚠ in the vector space only through flagged drug-doses |
| [[RPP21]] | +0.59 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[SNHG6]] | +0.59 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[POLR2I]] | +0.58 | +0.34 / +0.63 | both halves | 1e-04 | pathway: HIV Infection |
| [[PIGBOS1]] | +0.58 | +0.39 / +0.69 | both halves | 5e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTBP1]] | -0.60 | -0.39 / -0.63 | both halves | 6e-05 |  |
| [[GANAB]] | -0.60 | -0.54 / -0.60 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[DDX39B]] | -0.60 | -0.25 / -0.64 | both halves | 4e-04 |  |
| [[SRSF1]] | -0.59 | -0.32 / -0.62 | both halves | 2e-04 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[EMC1]] | -0.58 | -0.34 / -0.67 | both halves | 1e-04 |  |
| [[PTPN18]] | -0.58 | -0.38 / -0.55 | both halves | 7e-05 | pathway: Interleukin-1 family signaling |
| [[U2AF2]] | -0.58 | -0.25 / -0.62 | both halves | 4e-04 |  |
| [[ATP13A1]] | -0.58 | -0.21 / -0.70 | both halves | 6e-04 |  |
| [[PRMT1]] | -0.57 | -0.34 / -0.56 | both halves | 1e-04 | pathway: Transcriptional regulation by RUNX1 |
| [[AGPAT1]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[MTA2]] | -0.56 | -0.34 / -0.53 | both halves | 1e-04 | pathway: Intracellular signaling by second messengers |
| [[GPAA1]] | -0.56 | -0.34 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-44.3, -14.5); signed map (-18.8, -5.7). **Vector** length 64.2, 37.3% of its response variance represented; |z| ≥ 3 in 559 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +5.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +1.9 | +3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | -0.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -5.4 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -5.0 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -4.9 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.6 | +1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | +0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit alpha 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,136,733-62,143,440 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XAPC7, C6, HSPC, RC6-1 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 170 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [O14818](https://www.uniprot.org/uniprotkb/O14818) (Proteasome subunit alpha type-7):

> Component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged …

**Summary**, from NCBI Gene [5688](https://www.ncbi.nlm.nih.gov/gene/5688):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. This gene encodes a member of the …

**Accessions** — [HGNC:9536](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9536) · Entrez [5688](https://www.ncbi.nlm.nih.gov/gene/5688) · UniProt [O14818](https://www.uniprot.org/uniprotkb/O14818) · Ensembl [ENSG00000101182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101182)

## Data

Gene col 2086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2086); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2086]; `tensor/DDL_lfc|DDL_z.npy` [2086]; `embed/gene_vectors.npy` [2086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2086 or target_col == 2086). Every well: [[PSMA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
