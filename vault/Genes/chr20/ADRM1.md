---
symbol: "ADRM1"
type: "gene"
col: 5101
ensembl_id: "ENSG00000130706"
name: "ADRM1 26S proteasome ubiquitin receptor"
location: "20q13.33"
module: 7
arm: "+"
pooled_cpm: 50.54
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ADRM1

*ADRM1 26S proteasome ubiquitin receptor* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.79× (z +8.6, q 6e-15, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.204×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB6]] (+0.66, fdr 7e-06), [[BRF2]] (+0.65, fdr 1e-05), [[FADD]] (+0.64, fdr 7e-06); moves opposite to [[TMEM123]] (-0.59, fdr 1e-05), [[AGPAT1]] (-0.58, fdr 1e-05), [[PRCP]] (-0.58, fdr 7e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5101.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.79×** | +8.6 | 6e-15 | 47/48 (HOP62, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.71×** | +8.3 | 2e-14 | 47/48 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.70×** | +8.3 | 2e-14 | 47/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.52×** | +7.4 | 2e-11 | 46/48 (LS 180, NCI-H1792, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.44×** | +7.2 | 8e-11 | 45/47 (KATO III, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.29×** | +6.5 | 7e-09 | 48/48 (NCI-H2030, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.30×** | +6.3 | 3e-08 | 44/48 (NCI-H1792, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +6.1 | 6e-08 | 43/48 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.62×** | +5.7 | 9e-07 | 37/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **2.07×** | +5.5 | 2e-06 | 37/44 (NCI-H1792, SNU-423, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.89×** | +5.3 | 5e-06 | 40/48 (COLO 205, SW480, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.88×** | +5.3 | 7e-06 | 41/46 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.91×** | +5.0 | 2e-05 | 33/43 (PANC-1, SNU-423, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.75×** | +4.6 | 1e-04 | 36/48 (SW480, COLO 205, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.61×** | +4.0 | 0.003 | 32/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +3.2 | 0.044 | 27/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.49×** | +3.0 | 0.072 | 26/48 (J82, RPMI-7951, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.072 | 24/48 (NCI-H1792, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.204×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 31.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.57× (z +8.6) | — |
| [[C32 (line)]] | wt | 39.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.87× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +9.4) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[HOP62 (line)]] | alt | 38.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.60× (z +9.1) | — |
| [[KATO III (line)]] | alt | 53.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.87× (z +8.7) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 30.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.84× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 27.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +9.3) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[NCI-H23 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 51.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 132 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 100.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 45.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB6]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 945 |
| [[BRF2]] | +0.65 | +0.67 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[FADD]] | +0.64 | +0.69 / +0.59 | both halves | 7e-06 | pathway: Apoptosis |
| [[PSMA7]] | +0.63 | +0.70 / +0.60 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 937 |
| [[NSUN5]] | +0.63 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[DNTTIP2]] | +0.63 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[UBC]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 | pathway: ABC transporter disorders; STRING 993 |
| [[PSMD7]] | +0.62 | +0.73 / +0.62 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[NT5C]] | +0.60 | +0.56 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[ZFAND2A]] | +0.60 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[LENG1]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[RAB35]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM123]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[AGPAT1]] | -0.58 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[PRCP]] | -0.58 | -0.37 / -0.67 | both halves | 7e-05 |  |
| [[HMGN1]] | -0.56 | -0.25 / -0.58 | both halves | 4e-04 |  |
| [[GGH]] | -0.56 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[SH3BGRL]] | -0.55 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[PON2]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[SUMF2]] | -0.55 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[STT3B]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 | pathway: Co-inhibition by PD-1 |
| [[RCN2]] | -0.54 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[ATL2]] | -0.54 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[CREG1]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.493). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-42.7, -4.7); signed map (-22.2, -25.7). **Vector** length 82.2, 28.4% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | -5.2 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.1 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | -4.6 | +5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.2 | +0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ADRM1 26S proteasome ubiquitin receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,302,093-62,308,862 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GP110, Rpn13, ARM1, PSMD16 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | ANDROGEN_RESPONSE, INFLAMMATORY_RESPONSE, DNA_REPAIR |
| Reactome | 169 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16186](https://www.uniprot.org/uniprotkb/Q16186) (Proteasomal ubiquitin receptor ADRM1):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair. Within the …

**Summary**, from NCBI Gene [11047](https://www.ncbi.nlm.nih.gov/gene/11047):

> This gene encodes a member of the adhesion regulating molecule 1 protein family. The encoded protein is a component of the proteasome where it acts as a ubiquitin receptor and recruits the deubiquitinating enzyme, ubiquitin carboxyl-terminal hydrolase L5. Increased levels of the encoded protein are associated with increased cell adhesion, which is likely an indirect effect of this intracellular protein. Dysregulation of this gene has been implicated in carcinogenesis. Alternative splicing …

**Accessions** — [HGNC:15759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15759) · Entrez [11047](https://www.ncbi.nlm.nih.gov/gene/11047) · UniProt [Q16186](https://www.uniprot.org/uniprotkb/Q16186) · Ensembl [ENSG00000130706](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130706)

## Data

Gene col 5101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5101); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5101]; `tensor/DDL_lfc|DDL_z.npy` [5101]; `embed/gene_vectors.npy` [5101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5101 or target_col == 5101). Every well: [[ADRM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADRM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
