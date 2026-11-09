---
symbol: "SREBF1"
type: "gene"
col: 1015
ensembl_id: "ENSG00000072310"
name: "sterol regulatory element binding transcription factor 1"
location: "17p11.2"
module: 86
arm: "+"
pooled_cpm: 47.19
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# SREBF1

*sterol regulatory element binding transcription factor 1* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Retinoic acid (drug)]] 5 µM: 1.50× (z +6.1, q 6e-07, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.536× (z -6.7, q 9e-09, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SREBF2]] (+0.66, fdr 1e-05), [[DHCR7]] (+0.65, fdr 7e-06), [[SCD]] (+0.65, fdr 7e-06); moves opposite to [[SRGAP1]] (-0.53, fdr 2e-05), [[MOSMO]] (-0.52, fdr 3e-05), [[EGFR]] (-0.51, fdr 3e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NXPH4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1015.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 5 µM |  | **1.50×** | +6.1 | 6e-07 | 36/49 (C-33 A, SW480, …) | rises with dose |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **1.69×** | +5.7 | 5e-06 | 39/48 (SW480, C-33 A, …) | all doses, flat | position effect removed |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.68×** | +5.6 | 5e-06 | 42/48 (SW480, C-33 A, …) | all doses, flat | position effect removed |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 0.002 | 26/48 (C-33 A, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.004 | 29/47 (RKO, AsPC-1, …) | rises with dose | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.004 | 31/48 (LoVo, A549, …) | top dose only | position effect removed |
| [[Bexarotene (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.004 | 28/48 (SW480, PANC-1, …) | all doses, flat | position effect removed |
| [[Posaconazole (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.010 | 29/48 (LoVo, COLO 205, …) | top dose only | plate-row cell shift |
| [[Berbamine (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.058 | 20/49 (LoVo, A549, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.79×** | +3.3 | 0.058 | 23/49 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.077 | 18/47 (SW480, SNU-1, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1015.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.536×** | -6.7 | 9e-09 | 32/48 (C32, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.662×** | -6.3 | 8e-08 | 35/48 (Panc 03.27, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.723×** | -5.0 | 1e-04 | 27/49 (HT-29, C32, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.724×** | -4.9 | 1e-04 | 36/48 (SNU-1, A-427, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.633×** | -4.7 | 4e-04 | 24/42 (C-33 A, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.658×** | -4.5 | 6e-04 | 29/47 (CHP-212, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.665×** | -4.4 | 8e-04 | 24/48 (LoVo, KATO III, …) | two highest doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Clotrimazole (drug)]] 5 µM |  | **0.755×** | -4.3 | 0.001 | 30/49 (KATO III, C-33 A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.775×** | -3.9 | 0.005 | 24/48 (C32, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.775×** | -3.9 | 0.005 | 34/48 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.684×** | -3.9 | 0.005 | 30/49 (C-33 A, HT-29, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.699×** | -3.9 | 0.005 | 25/47 (NCI-H23, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.691×** | -3.8 | 0.007 | 26/47 (SW48, COLO 205, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.543×** | -3.5 | 0.023 | 24/49 (MIA PaCa-2, SW 900, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.725×** | -3.2 | 0.049 | 23/44 (Panc 03.27, HS-578T, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1015. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 95.9 | 1 | 2 (2 ⚠) | [[Retinoic acid (drug)]] 5 µM 3.01× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[C32 (line)]] | wt | 76.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -13.2) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -12.7) |
| [[HCT15 (line)]] | alt | 74.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -9.7) |
| [[HT-29 (line)]] | alt | 54.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.0) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.295× (z -9.7) |
| [[SNU-1 (line)]] | wt | 89.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.304× (z -10.5) |
| [[A-427 (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[CHP-212 (line)]] | wt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0909× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[Hs 766T (line)]] | wt | 45.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[KATO III (line)]] | alt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -8.5) |
| [[LoVo (line)]] | wt | 63.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -10.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[MIA PaCa-2 (line)]] | alt | 97.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H23 (line)]] | alt | 47.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[PANC-1 (line)]] | alt | 33.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.434× (z -8.7) |
| [[SW480 (line)]] | alt | 41.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.450× (z -9.4) |
| [[A-172 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1015), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SREBF2]] | +0.66 | +0.73 / +0.55 | both halves | 1e-05 | same gene group; pathway: Activation of gene expression by SREBF (SREBP); STRING 933 |
| [[DHCR7]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 | pathway: Activation of gene expression by SREBF (SREBP); STRING 848 |
| [[SCD]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 | pathway: Activation of gene expression by SREBF (SREBP); STRING 976 |
| [[FDFT1]] | +0.62 | +0.64 / +0.52 | both halves | 1e-05 | pathway: Activation of gene expression by SREBF (SREBP); STRING 782 |
| [[INSIG1]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 | pathway: Metabolism of steroids; STRING 969 |
| [[MVD]] | +0.61 | +0.65 / +0.46 | both halves | 3e-05 | pathway: Activation of gene expression by SREBF (SREBP); STRING 835 |
| [[STARD4]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 | pathway: Metabolism of steroids; STRING 671 |
| [[GPI]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PCSK9]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 | STRING 635 |
| [[C20orf96]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[LSS]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 | pathway: Activation of gene expression by SREBF (SREBP); STRING 857 |
| [[SLC26A6]] | +0.58 | +0.61 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP1]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[MOSMO]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[EGFR]] | -0.51 | -0.52 / -0.46 | both halves | 3e-05 | pathway: Signaling by Nuclear Receptors |
| [[C10orf88]] | -0.50 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[PRKG1-AS1]] | -0.48 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[CKMT2-AS1]] | -0.48 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[ELK3]] | -0.48 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[WNK4]] | -0.47 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[ABL2]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[UTP3]] | -0.47 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[KIFBP]] | -0.47 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[FBXO38]] | -0.46 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NXPH4]] | B | NXPH4 activity raises SREBF1's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.43× lower at baseline in the lines without NXPH4 | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises SREBF1's level | compounds that target TOP2A: 3 of 5 lower it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ELK3]] | C | ELK3's natural level weakens SREBF1's drug response | ELK3's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.55; direction not clear | 0.0995 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.9, -48.3); signed map (-53.2, 31.3). **Vector** length 122, 35.6% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Lanosterol biosynthesis* (reactome, mean cos +0.50 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | -0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +2.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +5.4 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +4.5 | -4.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.4 | -0.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.3 | +2.5 |
|  | [[Berbamine (drug)]] 5 µM |  | +4.2 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -6.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.2 | -6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.1 | -3.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.7 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -3.4 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | sterol regulatory element binding transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:17,810,399-17,837,002 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SREBP1, bHLHd1, SREBP-1c, SREBP1a |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; MicroRNA protein coding host genes; Sterol regulatory element binding transcription factor family |
| Reactome | 17 pathways, smallest: NR1H2 & NR1H3 regulate gene expression linked to lipogenesis; Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway); FOXO-mediated transcription of oxidative stress, metabolic and neuronal genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P36956](https://www.uniprot.org/uniprotkb/P36956) (Sterol regulatory element-binding protein 1):

> [Sterol regulatory element-binding protein 1]: Precursor of the transcription factor form (Processed sterol regulatory element-binding protein 1), which is embedded in the endoplasmic reticulum membrane. Low sterol concentrations promote processing of this form, releasing the transcription factor form that translocates into the nucleus and activates transcription of genes involved in cholesterol biosynthesis and lipid homeostasis (By similarity).; [Processed sterol regulatory element-binding …

**Summary**, from NCBI Gene [6720](https://www.ncbi.nlm.nih.gov/gene/6720):

> This gene encodes a basic helix-loop-helix-leucine zipper (bHLH-Zip) transcription factor that binds to the sterol regulatory element-1 (SRE1), which is a motif that is found in the promoter of the low density lipoprotein receptor gene and other genes involved in sterol biosynthesis. The encoded protein is synthesized as a precursor that is initially attached to the nuclear membrane and endoplasmic reticulum. Following cleavage, the mature protein translocates to the nucleus and activates …

**Accessions** — [HGNC:11289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11289) · Entrez [6720](https://www.ncbi.nlm.nih.gov/gene/6720) · UniProt [P36956](https://www.uniprot.org/uniprotkb/P36956) · Ensembl [ENSG00000072310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072310)

## Data

Gene col 1015: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1015); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1015, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1015]; `tensor/DDL_lfc|DDL_z.npy` [1015]; `embed/gene_vectors.npy` [1015]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1015 or target_col == 1015). Every well: [[SREBF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SREBF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
