---
symbol: "COG2"
type: "gene"
col: 5755
ensembl_id: "ENSG00000135775"
name: "component of oligomeric golgi complex 2"
location: "1q42.2"
module: 1
arm: "+"
pooled_cpm: 16.28
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# COG2

*component of oligomeric golgi complex 2* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.12× (z +11.6, q 4e-28, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.391× (z -20.4, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS31P4]] (+0.74, fdr 7e-06), [[TMEM177]] (+0.73, fdr 7e-06), [[AGK]] (+0.73, fdr 7e-06); moves opposite to [[C2]] (-0.65, fdr 7e-05), [[CD27-AS1]] (-0.65, fdr 3e-04), [[GNAS]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF569]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5755.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +11.6 | 4e-28 | 41/47 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +11.1 | 3e-26 | 42/47 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.92×** | +10.0 | 2e-21 | 42/47 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.30×** | +6.7 | 3e-09 | 26/45 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +6.5 | 7e-09 | 24/48 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +6.2 | 5e-08 | 23/46 (A-427, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +5.7 | 8e-07 | 27/47 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.24×** | +4.6 | 3e-04 | 18/48 (NCI-H1573, J82, …) | rises with dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +4.3 | 0.001 | 17/47 (SK-MEL-2, NCI-H2347, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.004 | 13/48 (SW 900, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.0 | 0.004 | 15/46 (CHP-212, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.004 | 12/47 (LS 180, LOX-IMVI, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.9 | 0.004 | 11/48 (A498, Panc 03.27, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.012 | 12/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.012 | 14/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.035 | 6/47 (CFPAC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5755.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.391×** | -20.4 | 0e+00 | 44/47 (PANC-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.403×** | -13.9 | 1e-41 | 36/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.407×** | -13.8 | 7e-41 | 40/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.526×** | -9.8 | 1e-20 | 32/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.575×** | -8.5 | 2e-15 | 30/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.568×** | -8.4 | 6e-15 | 30/46 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -7.5 | 7e-12 | 25/46 (SW480, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.673×** | -6.1 | 9e-08 | 25/47 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.724×** | -5.0 | 5e-05 | 22/47 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.753×** | -4.4 | 7e-04 | 21/47 (SW480, HT-29, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.598×** | -4.1 | 0.002 | 17/46 (RKO, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.759×** | -4.0 | 0.003 | 16/46 (NCI-H2347, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.788×** | -3.6 | 0.012 | 11/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.785×** | -3.4 | 0.024 | 14/33 (NCI-H460, BT-474, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5755. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.4 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -16.4) |
| [[PANC-1 (line)]] | alt | 18.4 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -18.1) |
| [[SW480 (line)]] | alt | 24.3 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.206× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 17.8 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.128× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -11.9) |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0815× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -10.6) |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -9.8) |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -10.6) |
| [[HS-578T (line)]] | alt | 9.83 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -10.6) |
| [[KATO III (line)]] | alt | 12.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -10.7) |
| [[LoVo (line)]] | wt | 19.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -9.9) |
| [[RKO (line)]] | wt | 17.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -10.9) |
| [[A-172 (line)]] | wt | 12.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -8.9) |
| [[A498 (line)]] | wt | 14.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -13.4) |
| [[A549 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.240× (z -9.8) |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0497× (z -12.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -10.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 13.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 19.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -12.4) |
| [[SHP-77 (line)]] | alt | 29.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -16.7) |
| [[SK-MEL-2 (line)]] | alt | 25.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -8.5) |
| [[SNU-423 (line)]] | alt | 9.44 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -10.0) |
| [[SW48 (line)]] | wt | 14.4 | 0 | 1 | — | [[Thymopentin (drug)]] 0.05 µM 0.0684× (z -9.7) |
| [[A-427 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5755), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | +0.74 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[TMEM177]] | +0.73 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[AGK]] | +0.73 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[MSL3P1]] | +0.72 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[TAMM41]] | +0.71 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SAAL1]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[DRG2]] | +0.69 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ZNF180]] | +0.68 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[KBTBD6]] | +0.68 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[N6AMT1]] | +0.68 | +0.64 / +0.69 | both halves | 7e-06 | STRING 453 |
| [[TTC5]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[RIOK1]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2]] | -0.65 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[CD27-AS1]] | -0.65 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[GNAS]] | -0.62 | -0.50 / -0.59 | both halves | 1e-05 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[BCL2L2-PABPN1]] | -0.61 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[SWT1]] | -0.60 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[PRDM10]] | -0.60 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[SLC25A53]] | -0.59 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[CSRP2]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[PPP1R15B-AS1]] | -0.58 | -0.15 / -0.65 | ⚠ one half (not replicated) | 0.001 |  |
| [[YPEL5]] | -0.58 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[DARS1-AS1]] | -0.58 | -0.32 / -0.53 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF569]] | B | ZNF569 activity raises COG2's level | lines that do not express ZNF569 (14) vs lines expressing it (36) | 1.08× lower at baseline in the lines without ZNF569 | 0.041 | ⚠ within organs, on part of the lines; also absent: ZNF570, PEG10, DNAAF9 |
| [[TOP2A]] | B | TOP2A activity raises COG2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GRTP1]] | B | GRTP1 activity raises COG2's level | lines that do not express GRTP1 (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without GRTP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: MLXIPL, PLS1, SLC37A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.590). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.4, -2.9); signed map (-22.2, -16.8). **Vector** length 95.7, 21.7% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.7 | +6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +6.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +11.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.1 | -20.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -7.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -8.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | -13.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | component of oligomeric golgi complex 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:230,642,481-230,693,982 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LDLC |
| Gene groups (HGNC) | Components of oligomeric golgi complex |
| Hallmark sets | PROTEIN_SECRETION, GLYCOLYSIS |
| Reactome | 9 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14746](https://www.uniprot.org/uniprotkb/Q14746) (Conserved oligomeric Golgi complex subunit 2):

> Required for normal Golgi morphology and function.

**Summary**, from NCBI Gene [22796](https://www.ncbi.nlm.nih.gov/gene/22796):

> This gene encodes a subunit of the conserved oligomeric Golgi complex that is required for maintaining normal structure and activity of the Golgi complex. The encoded protein specifically interacts with the USO1 vesicle docking protein and may be necessary for normal Golgi ribbon formation and trafficking of Golgi enzymes. Mutations of this gene are associated with abnormal glycosylation within the Golgi apparatus. Alternative splicing results in multiple transcript variants.[provided by …

**Accessions** — [HGNC:6546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6546) · Entrez [22796](https://www.ncbi.nlm.nih.gov/gene/22796) · UniProt [Q14746](https://www.uniprot.org/uniprotkb/Q14746) · Ensembl [ENSG00000135775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135775)

## Data

Gene col 5755: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5755); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5755, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5755]; `tensor/DDL_lfc|DDL_z.npy` [5755]; `embed/gene_vectors.npy` [5755]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5755 or target_col == 5755). Every well: [[COG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
