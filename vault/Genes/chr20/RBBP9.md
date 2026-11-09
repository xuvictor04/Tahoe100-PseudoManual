---
symbol: "RBBP9"
type: "gene"
col: 1563
ensembl_id: "ENSG00000089050"
name: "RB binding protein 9, serine hydrolase"
location: "20p11.23"
module: 25
arm: "+"
pooled_cpm: 7.15
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# RBBP9

*RB binding protein 9, serine hydrolase* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.92× (z +14.4, q 3e-44, up in 24 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.95× (z +12.7, q 1e-34, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.417× (z -11.7, q 1e-28, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRUB1]] (+0.74, fdr 7e-06), [[PNPO]] (+0.73, fdr 7e-06), [[DLD]] (+0.70, fdr 7e-06); moves opposite to [[HIC2]] (-0.69, fdr 7e-06), [[PITPNA]] (-0.63, fdr 7e-06), [[ZBTB7A]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[APOBEC3C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1563.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +14.4 | 3e-44 | 24/29 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.95×** | +12.7 | 1e-34 | 40/48 (HS-578T, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +11.5 | 3e-28 | 11/12 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +10.3 | 9e-23 | 14/20 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +4.9 | 1e-04 | 5/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.8 | 1e-04 | 7/34 (A-172, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.40×** | +4.5 | 5e-04 | 9/47 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 5e-04 | 14/44 (Hs 766T, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.3 | 0.001 | 6/38 (RPMI-7951, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.007 | 12/45 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.011 | 4/47 (AsPC-1, NCI-H2347, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +3.6 | 0.015 | 5/47 (KATO III, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.015 | 12/46 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +3.3 | 0.035 | 7/48 (LoVo, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.081 | 13/43 (CFPAC-1, J82, …) | two highest doses | cell-cycle shift (explains ~4% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1563.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.417×** | -11.7 | 1e-28 | 35/46 (SNU-423, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.463×** | -10.3 | 2e-22 | 36/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.541×** | -8.2 | 4e-14 | 30/47 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.543×** | -8.2 | 5e-14 | 25/44 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.641×** | -5.9 | 3e-07 | 21/46 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -4.8 | 1e-04 | 19/43 (Hs 766T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.740×** | -3.8 | 0.012 | 14/46 (SHP-77, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.765×** | -3.6 | 0.024 | 11/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.827×** | -3.6 | 0.024 | 15/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.775×** | -3.4 | 0.041 | 10/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -3.2 | 0.078 | 7/48 (H4, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.28 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.41× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.62× (z +9.2) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 6.55 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -8.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 7.74 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -8.9) |
| [[HT-29 (line)]] | alt | 4.13 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0646× (z -9.8) |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 1 | — | [[ULK-101 (drug)]] 0.5 µM 0.0696× (z -10.3) |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0615× (z -14.5) |
| [[SW 900 (line)]] | alt | 6.78 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 4.76 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -8.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 8.32 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRUB1]] | +0.74 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[PNPO]] | +0.73 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[DLD]] | +0.70 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[ALG10B]] | +0.70 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[SMG7]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[MANEA]] | +0.66 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[FECH]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[COPS6]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[PFKM]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ALG10]] | +0.65 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[COMMD8]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ZMYM3]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIC2]] | -0.69 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[PITPNA]] | -0.63 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[ZBTB7A]] | -0.62 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[EEF1D]] | -0.61 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[DRD4]] | -0.61 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[RAB11FIP3]] | -0.59 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[FBXL18]] | -0.59 | -0.43 / -0.68 | both halves | 3e-05 |  |
| [[SRGAP2D]] | -0.59 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[POLR2J4]] | -0.58 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.58 | -0.67 / -0.49 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMSB10]] | -0.58 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[UBL5]] | -0.57 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | -0.56 | -0.41 / -0.66 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOBEC3C]] | B | APOBEC3C activity raises RBBP9's level | lines that do not express APOBEC3C (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without APOBEC3C | 0.056 | ⚠ within organs, on part of the lines; also absent: MIR181A2HG, CRTAP |
| [[GSTM4]] | C | GSTM4 activity raises RBBP9's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 1.49× lower at baseline in the lines without GSTM4 | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.1, -17.0); signed map (-17.4, -41.0). **Vector** length 75.2, 12.5% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.1 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +10.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +3.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.9 | -11.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -8.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -4.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -1.5 | -0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | RB binding protein 9, serine hydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:18,486,540-18,497,225 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Bog |
| Matched by | ensembl_id |

**Function**, from UniProt [O75884](https://www.uniprot.org/uniprotkb/O75884) (Serine hydrolase RBBP9):

> Serine hydrolase (Probable). Catalyzes the hydrolytic activation of amino acid ester of the antiviral prodrug valacyclovir to its corresponding active drug, acyclovir. May negatively regulate basal or autocrine TGF-beta signaling by suppressing SMAD2-SMAD3 phosphorylation. May play a role in the transformation process due to its capacity to confer resistance to the growth-inhibitory effects of TGF-beta through interaction with RB1 and the subsequent displacement of E2F1.

**Summary**, from NCBI Gene [10741](https://www.ncbi.nlm.nih.gov/gene/10741):

> The protein encoded by this gene is a retinoblastoma binding protein that may play a role in the regulation of cell proliferation and differentiation. Two alternatively spliced transcript variants of this gene with identical predicted protein products have been reported, one of which is a nonsense-mediated decay candidate. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9892) · Entrez [10741](https://www.ncbi.nlm.nih.gov/gene/10741) · UniProt [O75884](https://www.uniprot.org/uniprotkb/O75884) · Ensembl [ENSG00000089050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089050)

## Data

Gene col 1563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1563); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1563]; `tensor/DDL_lfc|DDL_z.npy` [1563]; `embed/gene_vectors.npy` [1563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1563 or target_col == 1563). Every well: [[RBBP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBBP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
