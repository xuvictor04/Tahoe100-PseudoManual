---
symbol: "DDX54"
type: "gene"
col: 4394
ensembl_id: "ENSG00000123064"
name: "DEAD-box helicase 54"
location: "12q24.13"
module: 18
arm: "+"
pooled_cpm: 33.44
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# DDX54

*DEAD-box helicase 54* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.24× (z +10.0, q 6e-21, up in 39 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.54× (z +5.1, q 4e-05, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.557× (z -9.8, q 8e-20, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF3B]] (+0.77, fdr 7e-06), [[MDN1]] (+0.75, fdr 7e-06), [[KLHDC4]] (+0.71, fdr 7e-06); moves opposite to [[SHOC2]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LAMC3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4394.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +10.0 | 6e-21 | 39/45 (A498, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +7.7 | 3e-12 | 30/37 (A498, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +6.8 | 2e-09 | 34/44 (A-427, A-172, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.54×** | +5.1 | 4e-05 | 31/47 (J82, LoVo, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.52×** | +5.0 | 6e-05 | 32/47 (NCI-H1573, A-427, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.89×** | +4.0 | 0.006 | 29/47 (NCI-H460, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.37×** | +3.9 | 0.009 | 28/46 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.013 | 28/47 (SNU-423, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.76×** | +3.6 | 0.024 | 23/47 (C32, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.74×** | +3.5 | 0.029 | 21/48 (COLO 205, SHP-77, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +3.2 | 0.064 | 23/47 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.2 | 0.076 | 20/46 (CFPAC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4394.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.557×** | -9.8 | 8e-20 | 32/47 (SNU-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.635×** | -5.7 | 4e-06 | 30/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.655×** | -5.3 | 3e-05 | 27/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.659×** | -5.2 | 3e-05 | 27/47 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.702×** | -4.3 | 0.002 | 26/48 (LoVo, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.732×** | -3.9 | 0.010 | 24/47 (SW48, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.547×** | -3.8 | 0.011 | 21/48 (A-427, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.729×** | -3.8 | 0.011 | 23/47 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -3.5 | 0.030 | 21/48 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (drug)]] 5 µM |  | **0.822×** | -3.3 | 0.057 | 17/48 (SHP-77, AsPC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.771×** | -3.2 | 0.062 | 17/47 (LS 180, NCI-H2030, …) | rises with dose | low cells (technical?); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -3.1 | 0.092 | 3/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 38.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 34.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 42.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -8.8) |
| [[PANC-1 (line)]] | alt | 40.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -8.5) |
| [[SW48 (line)]] | wt | 51.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -13.8) |
| [[BT-474 (line)]] | alt | 43.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -9.0) |
| [[C-33 A (line)]] | alt | 37.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -8.5) |
| [[CHP-212 (line)]] | wt | 34.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM 0.0766× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 43.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.279× (z -9.1) |
| [[HOP62 (line)]] | alt | 23.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -8.8) |
| [[LoVo (line)]] | wt | 40.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 48.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 50.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.6) |
| [[RKO (line)]] | wt | 45.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -13.1) ⚠ cell-cycle shift, explains ~4% of this change |
| [[SHP-77 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -11.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 41.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -14.2) |
| [[SW480 (line)]] | alt | 42.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -12.6) |
| [[A-172 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF3B]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 | STRING 459 |
| [[MDN1]] | +0.75 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[KLHDC4]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[DHX33]] | +0.70 | +0.71 / +0.72 | both halves | 7e-06 | STRING 596 |
| [[UTP18]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 | STRING 511 |
| [[UCK2]] | +0.70 | +0.70 / +0.61 | both halves | 7e-06 | same gene group |
| [[DKC1]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 | same gene group; STRING 773 |
| [[TCOF1]] | +0.68 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.68 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[URB1]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 | STRING 677 |
| [[WDR43]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 | STRING 844 |
| [[NAA25]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHOC2]] | -0.57 | -0.64 / -0.49 | both halves | 1e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC3]] | B | LAMC3 activity raises DDX54's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.29× lower at baseline in the lines without LAMC3 | 0.003 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[WNK2]] | B | WNK2 activity raises DDX54's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.45× lower at baseline in the lines without WNK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[LTBR]] | B | LTBR activity lowers DDX54's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.14× higher at baseline in the lines without LTBR | 0.063 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[MVB12B]] | B | MVB12B activity raises DDX54's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without MVB12B | 0.064 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[WNK2]] | B | WNK2 activity strengthens DDX54's drug response | lines that do not express WNK2 (16) vs lines expressing it (32) | the lines without WNK2 respond 0.86× as strongly (z diff +0.75); strongest at Homoharringtonine 5 µM: 0.70x vs 0.54x (z diff +2.8) | 0.093 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.9, -38.0); signed map (-5.6, -51.1). **Vector** length 77.2, 19.5% of its response variance represented; |z| ≥ 3 in 757 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -9.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.3 | -0.5 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 54 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:113,157,173-113,185,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2835, APR-5, DP97 |
| Gene groups (HGNC) | DEAD-box helicases; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDD1](https://www.uniprot.org/uniprotkb/Q8TDD1) (ATP-dependent RNA helicase DDX54):

> Nucleolar RNA helicase that is involved in diverse cellular processes including ribosome biogenesis, DNA damage response, RNA splicing, transcriptional regulation, innate immunity, and nervous system development. Plays an essential role in the formation of the ribosome active site by remodeling rRNA structure and initiating peptidyl transferase center formation. Represses the transcriptional activity of several nuclear receptors. Regulates transcriptome dynamics during DNA damage response. …

**Summary**, from NCBI Gene [79039](https://www.ncbi.nlm.nih.gov/gene/79039):

> This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, …

**Accessions** — [HGNC:20084](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20084) · Entrez [79039](https://www.ncbi.nlm.nih.gov/gene/79039) · UniProt [Q8TDD1](https://www.uniprot.org/uniprotkb/Q8TDD1) · Ensembl [ENSG00000123064](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123064)

## Data

Gene col 4394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4394); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4394]; `tensor/DDL_lfc|DDL_z.npy` [4394]; `embed/gene_vectors.npy` [4394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4394 or target_col == 4394). Every well: [[DDX54 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX54.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
