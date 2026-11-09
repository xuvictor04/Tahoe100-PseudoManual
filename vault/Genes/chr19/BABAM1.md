---
symbol: "BABAM1"
type: "gene"
col: 2595
ensembl_id: "ENSG00000105393"
name: "BRISC and BRCA1 A complex member 1"
location: "19p13.11"
module: 72
arm: "+"
pooled_cpm: 18.53
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# BABAM1

*BRISC and BRCA1 A complex member 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.52× (z +14.0, q 2e-41, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.497× (z -14.9, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB3]] (+0.74, fdr 7e-06), [[PSMB4]] (+0.73, fdr 1e-05), [[PSMB2]] (+0.72, fdr 7e-06); moves opposite to [[PFN1]] (-0.57, fdr 1e-04), [[PTGER4]] (-0.56, fdr 1e-05), [[IER2]] (-0.55, fdr 2e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IL2RG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2595.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.52×** | +14.0 | 2e-41 | 46/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +12.3 | 2e-32 | 38/42 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.23×** | +12.1 | 1e-31 | 44/47 (LS 180, A-172, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.17×** | +10.0 | 3e-21 | 42/48 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +9.5 | 2e-19 | 27/32 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +6.9 | 4e-10 | 36/47 (SW480, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +6.4 | 2e-08 | 23/37 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.2 | 5e-08 | 23/47 (HS-578T, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +5.4 | 4e-06 | 25/44 (SW 900, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.6 | 3e-04 | 18/43 (LOX-IMVI, KATO III, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.9 | 0.006 | 17/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.017 | 11/48 (A-172, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.024 | 9/48 (SW480, H4, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.027 | 18/48 (AsPC-1, MIA PaCa-2, …) | top dose only | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.2 | 0.050 | 12/40 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2595.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.497×** | -14.9 | 0e+00 | 44/47 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.683×** | -5.7 | 3e-06 | 25/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.783×** | -5.2 | 4e-05 | 26/48 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.593×** | -4.1 | 0.005 | 19/45 (SW48, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -4.0 | 0.006 | 1/48 (hTERT-HPNE) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.785×** | -3.7 | 0.024 | 18/47 (SW480, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.800× | -3.2 | 0.10 | 15/47 (Panc 03.27, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2595. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 26.1 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.08× (z +9.5) | — |
| [[A498 (line)]] | wt | 26.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 13.9 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.92× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.320× (z -9.2) |
| [[LS 180 (line)]] | wt | 22.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.59× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 14.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.43× (z +9.8) | — |
| [[SW480 (line)]] | alt | 20.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.67× (z +9.6) | — |
| [[A-427 (line)]] | wt | 25.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.2) |
| [[CFPAC-1 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -11.4) |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.4) |
| [[J82 (line)]] | alt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.3) |
| [[LoVo (line)]] | wt | 14.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.53× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -22.4) |
| [[NCI-H1573 (line)]] | alt | 7.70 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.38× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.4) |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.131× (z -10.3) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.35× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -14.7) |
| [[A549 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2595), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB3]] | +0.74 | +0.80 / +0.64 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[PSMB4]] | +0.73 | +0.79 / +0.53 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[PSMB2]] | +0.72 | +0.75 / +0.60 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[UFD1]] | +0.72 | +0.79 / +0.68 | both halves | 7e-06 | pathway: Deubiquitination |
| [[MRPS15]] | +0.71 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[MRPL18]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[UBFD1]] | +0.70 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[TMEM161A]] | +0.70 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[ANKRD39]] | +0.70 | +0.74 / +0.65 | both halves | 7e-06 | STRING 554 |
| [[USP5]] | +0.69 | +0.77 / +0.54 | both halves | 1e-05 | pathway: Deubiquitination |
| [[PSMD13]] | +0.68 | +0.66 / +0.72 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[ALKBH6]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFN1]] | -0.57 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[PTGER4]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[IER2]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[JUNB]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL2RG]] | B | IL2RG activity lowers BABAM1's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.22× higher at baseline in the lines without IL2RG | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.856). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.6, -9.8); signed map (-26.1, -25.9). **Vector** length 80.6, 16.3% of its response variance represented; |z| ≥ 3 in 765 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of DVL* (reactome, mean cos +0.59 to 12); *proteasome* (control, mean cos +0.61 to 11); *NIK-->noncanonical NF-kB signaling* (reactome, mean cos +0.60 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.5 | +14.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.5 | +12.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.8 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +6.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -14.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -3.2 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -4.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | BRISC and BRCA1 A complex member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,267,376-17,281,249 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20571, HSPC142, NBA1, MERIT40; previously C19orf62 |
| Gene groups (HGNC) | BRCA1 A complex; BRISC complex |
| Reactome | 14 pathways, smallest: Metalloprotease DUBs; Nonhomologous End-Joining (NHEJ); Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWV8](https://www.uniprot.org/uniprotkb/Q9NWV8) (BRISC and BRCA1-A complex member 1):

> Component of the BRCA1-A complex, a complex that specifically recognizes 'Lys-63'-linked ubiquitinated histones H2A and H2AX at DNA lesions sites, leading to target the BRCA1-BARD1 heterodimer to sites of DNA damage at double-strand breaks (DSBs). The BRCA1-A complex also possesses deubiquitinase activity that specifically removes 'Lys-63'-linked ubiquitin on histones H2A and H2AX. In the BRCA1-A complex, it is required for the complex integrity and its localization at DSBs. Component of the …

**Summary**, from NCBI Gene [29086](https://www.ncbi.nlm.nih.gov/gene/29086):

> Enables identical protein binding activity. Involved in several processes, including DNA repair-dependent chromatin remodeling; mitotic G2 DNA damage checkpoint signaling; and positive regulation of DNA repair. Located in cytoplasm and nuclear body. Part of BRCA1-A complex and BRISC complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25008) · Entrez [29086](https://www.ncbi.nlm.nih.gov/gene/29086) · UniProt [Q9NWV8](https://www.uniprot.org/uniprotkb/Q9NWV8) · Ensembl [ENSG00000105393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105393)

## Data

Gene col 2595: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2595); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2595, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2595]; `tensor/DDL_lfc|DDL_z.npy` [2595]; `embed/gene_vectors.npy` [2595]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2595 or target_col == 2595). Every well: [[BABAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BABAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
