---
symbol: "BOK"
type: "gene"
col: 10745
ensembl_id: "ENSG00000176720"
name: "BCL2 family apoptosis regulator BOK"
location: "2q37.3"
module: 5
arm: "+"
pooled_cpm: 5.7
n_lines_expressing: 45
n_dd_up: 3
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# BOK

*BCL2 family apoptosis regulator BOK* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.76× (z +5.8, q 4e-06, up in 4 of 11 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.514× (z -9.9, q 2e-20, down in 28 of 37 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RGS19]] (+0.57, fdr 2e-05), [[FAAP100]] (+0.57, fdr 4e-05), [[KIF26A]] (+0.56, fdr 4e-05); moves opposite to [[SAR1B]] (-0.48, fdr 7e-05), [[HNMT]] (-0.48, fdr 1e-04), [[COPZ1]] (-0.47, fdr 2e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[PAQR7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10745.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +5.8 | 4e-06 | 4/11 (HepG2/C3A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +5.7 | 4e-06 | 14/34 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +4.5 | 0.001 | 11/26 (HepG2/C3A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 1.37× | +3.2 | 0.18 | 11/39 (NCI-H23, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10745.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.514×** | -9.9 | 2e-20 | 28/37 (LS 180, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.424×** | -9.1 | 3e-17 | 30/42 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.436×** | -8.8 | 4e-16 | 30/41 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.240×** | -7.9 | 5e-13 | 28/39 (KATO III, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -7.8 | 6e-13 | 24/36 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.501×** | -7.3 | 3e-11 | 24/39 (C-33 A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.310×** | -6.5 | 8e-09 | 21/35 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.561×** | -6.1 | 8e-08 | 23/38 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.563×** | -6.1 | 9e-08 | 22/40 (NCI-H23, J82, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.588×** | -5.4 | 4e-06 | 21/40 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.605×** | -5.3 | 6e-06 | 16/38 (SW48, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.615×** | -5.1 | 1e-05 | 20/42 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.726×** | -4.8 | 9e-05 | 16/38 (MIA PaCa-2, BT-474, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.659×** | -4.4 | 4e-04 | 13/42 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.647×** | -4.3 | 6e-04 | 16/38 (HT-29, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.659×** | -4.2 | 0.001 | 16/40 (BT-474, SW48, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.668×** | -4.1 | 0.001 | 14/37 (A-427, LoVo, …) | top dose only | position effect removed |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **0.549×** | -3.3 | 0.026 | 3/41 (LoVo, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10745. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 13.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -12.0) |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0468× (z -12.9) |
| [[HOP62 (line)]] | alt | 5.58 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0657× (z -11.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 6.68 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0811× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0997× (z -9.5) |
| [[J82 (line)]] | alt | 11.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -11.1) |
| [[PANC-1 (line)]] | alt | 8.19 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.4) |
| [[A498 (line)]] | wt | 4.82 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[BT-474 (line)]] | alt | 7.68 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0939× (z -9.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HT-29 (line)]] | alt | 6.60 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0729× (z -11.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 6.81 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0661× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 3.75 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0644× (z -9.3) |
| [[LS 180 (line)]] | wt | 6.07 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0549× (z -16.0) |
| [[NCI-H23 (line)]] | alt | 9.80 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -9.0) |
| [[RKO (line)]] | wt | 10.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0806× (z -10.7) |
| [[SNU-423 (line)]] | alt | 6.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0828× (z -13.7) |
| [[SW480 (line)]] | alt | 3.01 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0819× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.447 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10745), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS19]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[FAAP100]] | +0.57 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[KIF26A]] | +0.56 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[B3GALT6]] | +0.54 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[PLSCR3]] | +0.54 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[GPSM1]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[UBL4A]] | +0.52 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[PWP2]] | +0.52 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[FAM83H]] | +0.52 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[DVL1]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ALDH1B1]] | +0.51 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[MPP3]] | +0.51 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAR1B]] | -0.48 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[HNMT]] | -0.48 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[COPZ1]] | -0.47 | -0.37 / -0.30 | both halves | 2e-04 |  |
| [[FAM151B-DT]] | -0.46 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[COG4]] | -0.45 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[TMED10]] | -0.44 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[GPALPP1]] | -0.44 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[ARL6IP5]] | -0.44 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[MTCP1]] | -0.44 | -0.32 / -0.26 | both halves | 3e-04 |  |
| [[NDUFS1]] | -0.43 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[EMC7]] | -0.43 | -0.42 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAQR7]] | B | BOK activity raises PAQR7's level | lines that do not express BOK (5) vs lines expressing it (45) | 2.48× lower at baseline in the lines without BOK | 0.031 | ⚠ within organs, on part of the lines; also absent: SLC35F2, PLEC, IL4R |
| [[DVL1]] | B | BOK activity raises DVL1's level | lines that do not express BOK (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without BOK | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC35F2, PLEC, IL4R |
| [[MFSD10]] | B | BOK activity raises MFSD10's level | lines that do not express BOK (5) vs lines expressing it (45) | 1.60× lower at baseline in the lines without BOK | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC35F2, PLEC, IL4R |
| [[PAQR5]] | B | BOK activity raises PAQR5's level | lines that do not express BOK (5) vs lines expressing it (45) | 3.42× lower at baseline in the lines without BOK | 0.094 | ⚠ within organs, on part of the lines; also absent: SLC35F2, PLEC, IL4R |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.306). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.7, 37.4); signed map (-6.6, 30.0). **Vector** length 50.9, 7.24% of its response variance represented; |z| ≥ 3 in 857 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +1.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +1.6 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +1.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -9.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -7.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -8.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.1 | -7.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -6.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 family apoptosis regulator BOK |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,551,424-241,574,131 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BCL2L9, BOKL, MGC4631 |
| Gene groups (HGNC) | BCL2 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMX3](https://www.uniprot.org/uniprotkb/Q9UMX3) (Bcl-2-related ovarian killer protein):

> [Isoform 1]: Apoptosis regulator that functions through different apoptotic signaling pathways. Plays a roles as pro-apoptotic protein that positively regulates intrinsic apoptotic process in a BAX- and BAK1-dependent manner or in a BAX- and BAK1-independent manner. In response to endoplasmic reticulum stress promotes mitochondrial apoptosis through downstream BAX/BAK1 activation and positive regulation of PERK-mediated unfolded protein response (By similarity). Activates apoptosis …

**Summary**, from NCBI Gene [666](https://www.ncbi.nlm.nih.gov/gene/666):

> The protein encoded by this gene belongs to the BCL2 family, members of which form homo- or heterodimers, and act as anti- or proapoptotic regulators that are involved in a wide variety of cellular processes. Studies in rat show that this protein has restricted expression in reproductive tissues, interacts strongly with some antiapoptotic BCL2 proteins, not at all with proapoptotic BCL2 proteins, and induces apoptosis in transfected cells. Thus, this protein represents a proapoptotic member of …

**Accessions** — [HGNC:1087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1087) · Entrez [666](https://www.ncbi.nlm.nih.gov/gene/666) · UniProt [Q9UMX3](https://www.uniprot.org/uniprotkb/Q9UMX3) · Ensembl [ENSG00000176720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176720)

## Data

Gene col 10745: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10745); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10745, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10745]; `tensor/DDL_lfc|DDL_z.npy` [10745]; `embed/gene_vectors.npy` [10745]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10745 or target_col == 10745). Every well: [[BOK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BOK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
