---
symbol: "LIPT1"
type: "gene"
col: 6851
ensembl_id: "ENSG00000144182"
name: "lipoyltransferase 1"
location: "2q11.2"
module: 51
arm: "+"
pooled_cpm: 6.7
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# LIPT1

*lipoyltransferase 1* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +14.9, q 0e+00, up in 35 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.648× (z -6.0, q 1e-06, down in 18 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.673× (z -5.5, q 1e-05, down in 16 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THUMPD2]] (+0.73, fdr 7e-06), [[COIL]] (+0.73, fdr 7e-06), [[TRMT10B]] (+0.70, fdr 7e-06); moves opposite to [[TPM3]] (-0.67, fdr 7e-06), [[GRB2]] (-0.65, fdr 1e-05), [[ATP2C1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6851.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +14.9 | 0e+00 | 35/43 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.19×** | +10.8 | 1e-24 | 31/39 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.17×** | +10.3 | 2e-22 | 34/45 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +9.0 | 2e-17 | 20/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +7.8 | 6e-13 | 24/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +7.8 | 7e-13 | 25/42 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +7.1 | 1e-10 | 22/46 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +5.8 | 4e-07 | 19/46 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +5.5 | 2e-06 | 16/33 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.016 | 4/47 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.042 | 7/41 (NCI-H1573, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.042 | 3/46 (C32, AsPC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.27×** | +3.3 | 0.043 | 8/34 (SW480, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.056 | 8/35 (SK-MEL-2, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6851.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.648×** | -6.0 | 1e-06 | 18/47 (PANC-1, RKO, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.673×** | -5.5 | 1e-05 | 16/46 (SW480, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.675×** | -5.4 | 1e-05 | 20/46 (LoVo, NCI-H23, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.708×** | -4.8 | 3e-04 | 13/47 (PANC-1, H4, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.701×** | -4.7 | 3e-04 | 14/36 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.727×** | -4.4 | 1e-03 | 11/42 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.806×** | -4.2 | 0.002 | 14/41 (NCI-H2030, SHP-77, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.755×** | -3.7 | 0.013 | 15/42 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.827×** | -3.7 | 0.013 | 15/48 (SW1417, PANC-1, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.773×** | -3.6 | 0.021 | 7/45 (HEC-1-A, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 5.37 | 0 | 2 | — | [[Megestrol (drug)]] 0.5 µM 0.0727× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.174× (z -14.5) ⚠ toxic |
| [[A549 (line)]] | wt | 6.94 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 5 µM 0.112× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 4.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 4.08 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -8.8) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HT-29 (line)]] | alt | 5.68 | 0 | 1 | — | [[Nafamostat (mesylate) (drug)]] 0.5 µM 0.114× (z -9.1) |
| [[LoVo (line)]] | wt | 4.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 5.73 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0961× (z -9.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H2030 (line)]] | alt | 6.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 6.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +10.7) | — |
| [[RKO (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -8.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SK-MEL-2 (line)]] | alt | 8.65 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.113× (z -9.7) ⚠ toxic |
| [[SW480 (line)]] | alt | 7.28 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THUMPD2]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[COIL]] | +0.73 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[TRMT10B]] | +0.70 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[ARL14EP]] | +0.69 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[MED18]] | +0.69 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[EPC1]] | +0.68 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[GMEB2]] | +0.68 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[NFYC]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[FNTA]] | +0.67 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[THAP6]] | +0.67 | +0.77 / +0.48 | both halves | 2e-05 |  |
| [[CLK4]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPM3]] | -0.67 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[GRB2]] | -0.65 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[ATP2C1]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.62 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[AHSA1]] | -0.62 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[GDAP2]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[VDAC2]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[ADAM15]] | -0.61 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[RECQL]] | -0.60 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[CDC42BPB]] | -0.60 | -0.63 / -0.57 | both halves | 9e-06 |  |
| [[SETD3]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ACLY]] | -0.59 | -0.47 / -0.65 | both halves | 2e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LIPT1's level | compounds that target TOP2A: 3 of 5 lower it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TXNIP]] | B | TXNIP activity lowers LIPT1's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.30× higher at baseline in the lines without TXNIP | 0.065 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[GIHCG]] | B | GIHCG activity raises LIPT1's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.26× lower at baseline in the lines without GIHCG | 0.072 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-30.7, 7.0); signed map (6.0, -19.4). **Vector** length 73.5, 11.9% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +14.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +10.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +3.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.6 | +0.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.6 | +2.9 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.4 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -2.9 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -0.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | lipoyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:99,154,955-99,163,157 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC12290, MGC13378 |
| Gene groups (HGNC) | Acyltransferases |
| Reactome | 1 pathways, smallest: Protein lipoylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y234](https://www.uniprot.org/uniprotkb/Q9Y234) (Lipoyl amidotransferase LIPT1, mitochondrial):

> Lipoyl amidotransferase that catalyzes the transfer of lipoyl moieties from lipoyl-protein H of the glycine cleavage system (lipoyl-GCSH) to E2 subunits of the pyruvate dehydrogenase complex (PDCE2). Unable to catalyze the transfer of octanoyl from octanoyl-GCSH to PDCE2. In vitro, it is also able to catalyze the transfer of the lipoyl group from lipoyl-AMP to the specific lysine residue of lipoyl domains of lipoate-dependent enzymes but this reaction may not be physiologically relevant …

**Summary**, from NCBI Gene [51601](https://www.ncbi.nlm.nih.gov/gene/51601):

> The process of transferring lipoic acid to proteins is a two-step process. The first step is the activation of lipoic acid by lipoate-activating enzyme to form lipoyl-AMP. For the second step, the protein encoded by this gene transfers the lipoyl moiety to apoproteins. Alternative splicing results in multiple transcript variants. A related pseudogene has been identified on chromosome 13. Read-through transcription also exists between this gene and the neighboring downstream mitochondrial …

**Accessions** — [HGNC:29569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29569) · Entrez [51601](https://www.ncbi.nlm.nih.gov/gene/51601) · UniProt [Q9Y234](https://www.uniprot.org/uniprotkb/Q9Y234) · Ensembl [ENSG00000144182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144182)

## Data

Gene col 6851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6851); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6851]; `tensor/DDL_lfc|DDL_z.npy` [6851]; `embed/gene_vectors.npy` [6851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6851 or target_col == 6851). Every well: [[LIPT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIPT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
