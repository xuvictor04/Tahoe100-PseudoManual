---
symbol: "GABARAP"
type: "gene"
col: 9931
ensembl_id: "ENSG00000170296"
name: "GABA type A receptor-associated protein"
location: "17p13.1"
module: 59
arm: "+"
pooled_cpm: 45.73
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# GABARAP

*GABA type A receptor-associated protein* — 17p13.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.76× (z +7.4, q 1e-10, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 4.86×, A549 5.01×, PANC-1 4.42×, HS-578T 4.65×, …; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 3.76×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.94×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.596× (z -4.1, q 0.026, down in 36 of 48 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.189×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPC2]] (+0.77, fdr 7e-06), [[NEU1]] (+0.73, fdr 7e-06), [[SIRT2]] (+0.72, fdr 7e-06); moves opposite to [[CCT5]] (-0.69, fdr 7e-06), [[NSUN2]] (-0.66, fdr 7e-06), [[CCT6A]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRABD2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9931.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 4.86×, A549 5.01×, PANC-1 4.42×, HS-578T 4.65×, …; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 3.76×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.94×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +7.4 | 1e-10 | 45/49 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +6.0 | 4e-07 | 36/39 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.75×** | +4.4 | 0.002 | 40/48 (PANC-1, NCI-H460, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.71×** | +4.2 | 0.004 | 38/47 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +3.5 | 0.055 | 30/43 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.2 | 0.11 | 6/49 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9931.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.189×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.596×** | -4.1 | 0.026 | 36/48 (AsPC-1, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.66 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9931. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 59.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 51.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 70.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 43.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 66.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 72.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 48.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9931), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPC2]] | +0.77 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[NEU1]] | +0.73 | +0.79 / +0.59 | both halves | 7e-06 |  |
| [[SIRT2]] | +0.72 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[CUTA]] | +0.71 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[KLHL24]] | +0.71 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[GPX4]] | +0.69 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.68 | +0.67 / +0.68 | both halves | 7e-06 | pathway: Autophagy |
| [[HDAC5]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[SAT2]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[PLAG1]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[MICU1]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SMDT1]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | -0.69 | -0.72 / -0.58 | both halves | 7e-06 |  |
| [[NSUN2]] | -0.66 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[CCT6A]] | -0.66 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[PSMD14]] | -0.65 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[NUP205]] | -0.65 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[BEND3]] | -0.64 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[EBNA1BP2]] | -0.63 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[METTL3]] | -0.63 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[WDR77]] | -0.63 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[GALNT14]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[WDR4]] | -0.62 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[DCTD]] | -0.62 | -0.58 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRABD2B]] | B | TRABD2B activity lowers GABARAP's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.21× higher at baseline in the lines without TRABD2B | 0.061 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-7.8, -46.1); signed map (-10.6, 7.0). **Vector** length 84.9, 31.7% of its response variance represented; |z| ≥ 3 in 445 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Amino acids regulate mTORC1* (reactome, mean cos +0.54 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +3.3 | +4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.9 | +2.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.6 | +0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +0.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.9 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.1 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | +0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | GABA type A receptor-associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,240,008-7,242,449 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MM46, ATG8A |
| Gene groups (HGNC) | Autophagy related; GABA type A receptor-associated protein family |
| Reactome | 6 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Macroautophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [O95166](https://www.uniprot.org/uniprotkb/O95166) (Gamma-aminobutyric acid receptor-associated protein):

> Ubiquitin-like modifier that plays a role in intracellular transport of GABA(A) receptors and its interaction with the cytoskeleton. Involved in autophagy: while LC3s are involved in elongation of the phagophore membrane, the GABARAP/GATE-16 subfamily is essential for a later stage in autophagosome maturation. Through its interaction with the reticulophagy receptor TEX264, participates in the remodeling of subdomains of the endoplasmic reticulum into autophagosomes upon nutrient stress, which …

**Summary**, from NCBI Gene [11337](https://www.ncbi.nlm.nih.gov/gene/11337):

> Gamma-aminobutyric acid A receptors [GABA(A) receptors] are ligand-gated chloride channels that mediate inhibitory neurotransmission. This gene encodes GABA(A) receptor-associated protein, which is highly positively charged in its N-terminus and shares sequence similarity with light chain-3 of microtubule-associated proteins 1A and 1B. This protein clusters neurotransmitter receptors by mediating interaction with the cytoskeleton. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4067) · Entrez [11337](https://www.ncbi.nlm.nih.gov/gene/11337) · UniProt [O95166](https://www.uniprot.org/uniprotkb/O95166) · Ensembl [ENSG00000170296](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170296)

## Data

Gene col 9931: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9931); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9931, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9931]; `tensor/DDL_lfc|DDL_z.npy` [9931]; `embed/gene_vectors.npy` [9931]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9931 or target_col == 9931). Every well: [[GABARAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABARAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
