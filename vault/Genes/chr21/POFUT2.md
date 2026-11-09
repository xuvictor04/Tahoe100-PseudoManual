---
symbol: "POFUT2"
type: "gene"
col: 11864
ensembl_id: "ENSG00000186866"
name: "protein O-fucosyltransferase 2"
location: "21q22.3"
module: 56
arm: "+"
pooled_cpm: 42.08
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# POFUT2

*protein O-fucosyltransferase 2* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.62× (z +7.5, q 5e-11, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.600× (z -8.0, q 1e-12, down in 25 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.700× (z -7.5, q 1e-11, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPE]] (+0.77, fdr 7e-06), [[ARFIP2]] (+0.77, fdr 7e-06), [[SLC35A2]] (+0.76, fdr 7e-06); moves opposite to [[KLHL42]] (-0.57, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GPR173]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +7.5 | 5e-11 | 37/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +4.5 | 0.002 | 23/47 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +4.5 | 0.002 | 25/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +4.3 | 0.002 | 23/49 (A498, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.005 | 23/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.5 | 0.038 | 20/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.040 | 14/48 (PANC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.045 | 19/48 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.11 | 20/48 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 1.46× | +3.1 | 0.11 | 15/44 (RPMI-7951, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 1.45× | +3.0 | 0.12 | 16/47 (MIA PaCa-2, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11864.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.600×** | -8.0 | 1e-12 | 25/46 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -7.5 | 1e-11 | 35/48 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -6.2 | 1e-07 | 35/48 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -6.0 | 3e-07 | 23/39 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.705×** | -5.4 | 6e-06 | 27/48 (HOP62, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -5.1 | 4e-05 | 30/48 (RPMI-7951, H4, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.723×** | -4.9 | 1e-04 | 27/48 (NCI-H1573, hTERT-HPNE, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.738×** | -4.4 | 8e-04 | 21/40 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.763×** | -4.2 | 0.002 | 24/48 (A-172, H4, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.765×** | -4.2 | 0.002 | 24/48 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.764×** | -4.0 | 0.003 | 22/46 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.777×** | -3.9 | 0.004 | 22/48 (LS 180, H4, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.791×** | -3.7 | 0.011 | 19/48 (A549, NCI-H1573, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.803×** | -3.4 | 0.024 | 19/48 (HOP62, KATO III, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.813×** | -3.2 | 0.046 | 20/48 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.816×** | -3.2 | 0.051 | 14/48 (NCI-H2030, HepG2/C3A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.859× | -3.2 | 0.051 | 17/48 (A498, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 50.2 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -17.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 96.8 | 0 | 3 | — | [[Flutamide (drug)]] 5 µM 0.0685× (z -9.5) |
| [[A-172 (line)]] | wt | 68.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 57.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -9.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 42.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -11.5) |
| [[A498 (line)]] | wt | 82.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 42.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 47.7 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.128× (z -9.2) |
| [[HOP62 (line)]] | alt | 87.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.2) |
| [[Hs 766T (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0776× (z -9.3) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 70.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -9.8) |
| [[LoVo (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0903× (z -17.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 40.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.02× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2347 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[PANC-1 (line)]] | alt | 36.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 66.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 48.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -12.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPE]] | +0.77 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[ARFIP2]] | +0.77 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[SLC35A2]] | +0.76 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.74 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[ARFGAP1]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[SEC13]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[BET1L]] | +0.68 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[KCNQ1OT1]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SEC22B]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.67 | +0.70 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL42]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR173]] | B | GPR173 activity raises POFUT2's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 1.46× lower at baseline in the lines without GPR173 | 0.089 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.8, -36.8); signed map (-51.5, 14.7). **Vector** length 107, 28.0% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.55 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.56 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.56 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.5 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | -6.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +0.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.6 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.5 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -6.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -4.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.9 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -1.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -2.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | protein O-fucosyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:45,263,928-45,287,898 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0958, FUT13; previously C21orf80 |
| Gene groups (HGNC) | Fucosyltransferases |
| Reactome | 2 pathways, smallest: O-glycosylation of TSR domain-containing proteins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2G5](https://www.uniprot.org/uniprotkb/Q9Y2G5) (GDP-fucose protein O-fucosyltransferase 2):

> GDP-fucose protein O-fucosyltransferase involved in one of the two pathways responsible for protein O-linked fucosylation, a unique post-translational modification of cysteine-knotted proteins that regulates various biological functions. This pathway targets proteins with Thrombospondin type-1 (TSP1) repeats (TSR) in the endoplasmic reticulum. Catalyzes the reaction that attaches fucose through an O-glycosidic linkage to a conserved serine or threonine residue in the consensus sequence …

**Summary**, from NCBI Gene [23275](https://www.ncbi.nlm.nih.gov/gene/23275):

> Fucose is typically found as a terminal modification of branched chain glycoconjugates, but it also exists in direct O-linkage to serine or threonine residues within cystine knot motifs in epidermal growth factor (EGF; MIM 131530)-like repeats or thrombospondin (THBS; see MIM 188060) type-1 repeats. POFUT2 is an O-fucosyltransferase that use THBS type-1 repeats as substrates (Luo et al., 2006 [PubMed 16464857]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:14683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14683) · Entrez [23275](https://www.ncbi.nlm.nih.gov/gene/23275) · UniProt [Q9Y2G5](https://www.uniprot.org/uniprotkb/Q9Y2G5) · Ensembl [ENSG00000186866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186866)

## Data

Gene col 11864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11864); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11864]; `tensor/DDL_lfc|DDL_z.npy` [11864]; `embed/gene_vectors.npy` [11864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11864 or target_col == 11864). Every well: [[POFUT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POFUT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
