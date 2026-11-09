---
symbol: "PSMB4"
type: "gene"
col: 8250
ensembl_id: "ENSG00000159377"
name: "proteasome 20S subunit beta 4"
location: "1q21.3"
module: 72
arm: "+"
pooled_cpm: 45.74
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PSMB4

*proteasome 20S subunit beta 4* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.16× (z +9.5, q 1e-18, up in 46 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.45× (z +7.4, q 3e-11, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.690× (z -4.0, q 0.038, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.263×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOD1]] (+0.75, fdr 7e-06), [[BABAM1]] (+0.73, fdr 1e-05), [[PSMB6]] (+0.72, fdr 7e-06); moves opposite to [[SYNCRIP]] (-0.53, fdr 4e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ALDH2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.16×** | +9.5 | 1e-18 | 46/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.64×** | +7.7 | 4e-12 | 39/41 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.45×** | +7.4 | 3e-11 | 48/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.39×** | +7.2 | 9e-11 | 48/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.44×** | +6.3 | 2e-08 | 36/44 (A498, C32, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.11×** | +5.8 | 5e-07 | 44/48 (NCI-H1573, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +5.5 | 2e-06 | 44/46 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.6 | 2e-04 | 33/48 (NCI-H2347, SNU-423, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.66×** | +4.2 | 0.002 | 37/46 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.029 | 33/48 (C32, HT-29, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.52×** | +3.3 | 0.050 | 27/47 (C32, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8250.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.263×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.690×** | -4.0 | 0.038 | 32/48 (A-427, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 59.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H460 (line)]] | wt | 47.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 99.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-427 (line)]] | wt | 83.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -11.6) |
| [[C32 (line)]] | wt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.59× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[Hs 766T (line)]] | wt | 41.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.86× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HS-578T (line)]] | alt | 33.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[KATO III (line)]] | alt | 42.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LOX-IMVI (line)]] | wt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 40.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1573 (line)]] | alt | 33.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.05× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.34× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H23 (line)]] | alt | 58.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 48.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[RPMI-7951 (line)]] | alt | 35.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SNU-423 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SW480 (line)]] | alt | 38.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A549 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOD1]] | +0.75 | +0.76 / +0.66 | both halves | 7e-06 | pathway: Cellular response to chemical stress; STRING 726 |
| [[BABAM1]] | +0.73 | +0.79 / +0.53 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[PSMB6]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[ANKRD39]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[PSMB5]] | +0.70 | +0.74 / +0.65 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[MRPL18]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[PSMA2]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMA1]] | +0.67 | +0.71 / +0.58 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMB3]] | +0.67 | +0.73 / +0.52 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[UBB]] | +0.66 | +0.57 / +0.71 | both halves | 9e-06 | pathway: ABC transporter disorders; STRING 957 |
| [[EMC4]] | +0.65 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[MED31]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNCRIP]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALDH2]] | B | ALDH2 activity lowers PSMB4's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without ALDH2 | 0.087 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.831). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.8, -9.9); signed map (-24.6, -25.5). **Vector** length 64.0, 20.7% of its response variance represented; |z| ≥ 3 in 568 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.61 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.2 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.1 | +7.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.9 | +5.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.0 | +1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | -0.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -4.9 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -4.7 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -4.5 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.1 | +0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.1 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit beta 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,399,560-151,401,937 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HN3, PROS26 |
| Gene groups (HGNC) | Proteasome |
| Reactome | 170 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P28070](https://www.uniprot.org/uniprotkb/P28070) (Proteasome subunit beta type-4):

> Non-catalytic component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or …

**Summary**, from NCBI Gene [5692](https://www.ncbi.nlm.nih.gov/gene/5692):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. An essential function of a modified proteasome, the …

**Accessions** — [HGNC:9541](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9541) · Entrez [5692](https://www.ncbi.nlm.nih.gov/gene/5692) · UniProt [P28070](https://www.uniprot.org/uniprotkb/P28070) · Ensembl [ENSG00000159377](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159377)

## Data

Gene col 8250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8250); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8250]; `tensor/DDL_lfc|DDL_z.npy` [8250]; `embed/gene_vectors.npy` [8250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8250 or target_col == 8250). Every well: [[PSMB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
