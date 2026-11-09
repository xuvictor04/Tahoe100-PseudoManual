---
symbol: "TMEM231"
type: "gene"
col: 12946
ensembl_id: "ENSG00000205084"
name: "transmembrane protein 231"
location: "16q23.1"
module: 18
arm: "+"
pooled_cpm: 8.7
n_lines_expressing: 47
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TMEM231

*transmembrane protein 231* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.90× (z +14.5, q 4e-45, up in 28 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.601× (z -8.2, q 1e-13, down in 23 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW1417 0.157×, A-172 0.200×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 0.102×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A498 0.190×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.462×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HS-578T 0.182×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCTN3]] (+0.57, fdr 9e-05), [[PMS2P1]] (+0.56, fdr 1e-05), [[PRMT7]] (+0.55, fdr 3e-05); moves opposite to [[FSIP2]] (-0.59, fdr 4e-05), [[TOR1AIP2]] (-0.51, fdr 3e-04), [[AFF4]] (-0.48, fdr 2e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12946.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +14.5 | 4e-45 | 28/40 (NCI-H1792, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +8.7 | 8e-16 | 25/44 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +8.3 | 3e-14 | 27/44 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +6.3 | 5e-08 | 18/34 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +5.7 | 1e-06 | 16/44 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +5.2 | 2e-05 | 17/44 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +5.2 | 2e-05 | 15/44 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.005 | 10/39 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.009 | 7/45 (LoVo, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.024 | 6/45 (NCI-H23, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.25×** | +3.3 | 0.047 | 4/21 (NCI-H460, SHP-77, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +3.1 | 0.096 | 5/43 (NCI-H23, A-427, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +3.0 | 0.096 | 5/38 (SW480, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.096 | 4/44 (A-172, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12946.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW1417 0.157×, A-172 0.200×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (J82 0.102×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A498 0.190×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.462×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HS-578T 0.182×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.601×** | -8.2 | 1e-13 | 23/42 (PANC-1, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.736×** | -7.0 | 7e-10 | 23/45 (MIA PaCa-2, J82, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.690× | -3.1 | 0.32 | 13/39 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 9.78 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 9.45 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.182× (z -8.5) |
| [[J82 (line)]] | alt | 9.00 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[NCI-H1792 (line)]] | alt | 9.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -8.8) |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCTN3]] | +0.57 | +0.37 / +0.67 | both halves | 9e-05 | STRING 880 |
| [[PMS2P1]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PRMT7]] | +0.55 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[SFXN2]] | +0.52 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[MIPEP]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[EXOSC7]] | +0.51 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[EBPL]] | +0.51 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[DTD2]] | +0.51 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[MTERF3]] | +0.51 | +0.37 / +0.55 | both halves | 9e-05 |  |
| [[PEX11B]] | +0.50 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[PACRGL]] | +0.50 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[PEMT]] | +0.50 | +0.43 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSIP2]] | -0.59 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[TOR1AIP2]] | -0.51 | -0.29 / -0.57 | both halves | 3e-04 |  |
| [[AFF4]] | -0.48 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[SYNM]] | -0.44 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[SPTAN1]] | -0.44 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[FMO4]] | -0.44 | -0.20 / -0.45 | ⚠ not reproduced | 8e-04 |  |
| [[CPEB4]] | -0.43 | -0.26 / -0.49 | both halves | 3e-04 |  |
| [[RAB31]] | -0.43 | -0.20 / -0.52 | ⚠ one half (not replicated) | 7e-04 |  |
| [[DNAJA1]] | -0.42 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[OGDH]] | -0.42 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[LRIF1]] | -0.42 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[RASSF2]] | -0.42 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[PHEX]] | -0.41 | -0.26 / -0.46 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises TMEM231's level | lines that do not express NT5M (7) vs lines expressing it (43) | 2.44× lower at baseline in the lines without NT5M | 0.014 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[SYNM]] | B | SYNM activity raises TMEM231's level | lines that do not express SYNM (14) vs lines expressing it (36) | 1.54× lower at baseline in the lines without SYNM | 0.031 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.417). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.6, -15.1); signed map (-37.5, -22.2). **Vector** length 60.8, 9.19% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +14.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.3 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.9 | +6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | +1.8 | +3.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +0.9 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.9 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 231 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:75,536,741-75,556,289 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22167, ALYE870, PRO1886, JBTS20, MKS11 |
| Gene groups (HGNC) | MKS complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6L2](https://www.uniprot.org/uniprotkb/Q9H6L2) (Transmembrane protein 231):

> Transmembrane component of the tectonic-like complex, a complex localized at the transition zone of primary cilia and acting as a barrier that prevents diffusion of transmembrane proteins between the cilia and plasma membranes. Required for ciliogenesis and sonic hedgehog/SHH signaling (By similarity).

**Summary**, from NCBI Gene [79583](https://www.ncbi.nlm.nih.gov/gene/79583):

> This gene encodes a transmembrane protein, which is a component of the B9 complex involved in the formation of the diffusion barrier between the cilia and plasma membrane. Mutations in this gene cause Joubert syndrome (JBTS). Multiple alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:37234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37234) · Entrez [79583](https://www.ncbi.nlm.nih.gov/gene/79583) · UniProt [Q9H6L2](https://www.uniprot.org/uniprotkb/Q9H6L2) · Ensembl [ENSG00000205084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205084)

## Data

Gene col 12946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12946); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12946]; `tensor/DDL_lfc|DDL_z.npy` [12946]; `embed/gene_vectors.npy` [12946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12946 or target_col == 12946). Every well: [[TMEM231 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM231.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
