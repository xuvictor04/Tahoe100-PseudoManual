---
symbol: "CSTF3-DT"
type: "gene"
col: 14485
ensembl_id: "ENSG00000247151"
name: "CSTF3 divergent transcript"
location: "11p13"
module: 91
arm: "+"
pooled_cpm: 3.86
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 12
n_dd_up_clean: 22
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# CSTF3-DT

*CSTF3 divergent transcript* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.57× (z +14.0, q 2e-41, up in 27 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.624× (z -4.7, q 0.002, down in 13 of 38 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C5orf34]] (+0.61, fdr 2e-05), [[NSMCE1-DT]] (+0.59, fdr 1e-05), [[NLRX1]] (+0.59, fdr 2e-05); moves opposite to [[NAPG]] (-0.54, fdr 5e-05), [[EIF3H]] (-0.54, fdr 2e-05), [[PDHA1]] (-0.50, fdr 7e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14485.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +14.0 | 2e-41 | 27/34 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +9.1 | 3e-17 | 19/30 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +6.2 | 9e-08 | 14/36 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +5.8 | 7e-07 | 7/16 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.48×** | +5.8 | 7e-07 | 18/43 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.44×** | +5.4 | 8e-06 | 14/36 (NCI-H2347, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +5.1 | 2e-05 | 13/44 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +4.9 | 6e-05 | 13/44 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.63×** | +4.9 | 6e-05 | 1/5 (A498) | inconsistent across doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.8 | 1e-04 | 8/46 (SW480, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +4.8 | 1e-04 | 13/41 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +4.5 | 4e-04 | 12/43 (SW48, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +4.2 | 0.001 | 13/42 (SNU-423, C-33 A, …) | rises with dose |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.005 | 4/35 (A549, C32, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.006 | 9/45 (RKO, KATO III, …) | rises with dose |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.013 | 7/43 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Radotinib (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.014 | 6/27 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.2 | 0.037 | 5/41 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14485.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.624×** | -4.7 | 0.002 | 13/38 (Hs 766T, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.457×** | -4.3 | 0.005 | 9/29 (C-33 A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -4.0 | 0.010 | 18/42 (PANC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.684×** | -4.0 | 0.010 | 7/45 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.691×** | -3.9 | 0.012 | 10/45 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.683×** | -3.8 | 0.012 | 9/24 (C-33 A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | **0.688×** | -3.8 | 0.014 | 10/43 (CFPAC-1, C32, …) | top dose only |  |
| [[Naproxen (drug)]] 0.5 µM |  | **0.714×** | -3.5 | 0.029 | 4/45 (CFPAC-1, RPMI-7951, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.529×** | -3.5 | 0.029 | 12/39 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.718×** | -3.5 | 0.029 | 13/43 (PANC-1, HS-578T, …) | two highest doses |  |
| [[palbociclib (drug)]] 0.5 µM |  | **0.654×** | -3.2 | 0.080 | 7/45 (CFPAC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.566×** | -3.1 | 0.089 | 2/44 (RPMI-7951, BT-474) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14485. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 27.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 2.30 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0643× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[HOP62 (line)]] | alt | 6.90 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[PANC-1 (line)]] | alt | 7.97 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.193× (z -9.5) |
| [[A-172 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.976 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14485), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C5orf34]] | +0.61 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[NSMCE1-DT]] | +0.59 | +0.60 / +0.49 | both halves | 1e-05 | same gene group |
| [[NLRX1]] | +0.59 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ZNF85]] | +0.58 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[DICER1-AS1]] | +0.56 | +0.58 / +0.35 | both halves | 1e-04 |  |
| [[LIN9]] | +0.56 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[ING2-DT]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 | same gene group |
| [[MGME1]] | +0.56 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[SMC1B]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[DLEU2]] | +0.55 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[NUCKS1]] | +0.55 | +0.58 / +0.36 | both halves | 9e-05 |  |
| [[C1orf112]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPG]] | -0.54 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[EIF3H]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[PDHA1]] | -0.50 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[RMC1]] | -0.49 | -0.37 / -0.25 | both halves | 4e-04 |  |
| [[ST6GALNAC4]] | -0.49 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[APMAP]] | -0.47 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[TBC1D16]] | -0.46 | -0.34 / -0.22 | both halves | 6e-04 |  |
| [[RSU1]] | -0.46 | -0.40 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CSTF3-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-43.5, -46.6); signed map (33.8, -13.0). **Vector** length 58.2, 8.42% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +9.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +14.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +5.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +2.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.1 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | CSTF3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p13 — chr11:33,161,657-33,191,598 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously CSTF3-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27882) · Entrez [338739](https://www.ncbi.nlm.nih.gov/gene/338739) · Ensembl [ENSG00000247151](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247151)

## Data

Gene col 14485: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14485); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14485, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14485]; `tensor/DDL_lfc|DDL_z.npy` [14485]; `embed/gene_vectors.npy` [14485]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14485 or target_col == 14485). Every well: [[CSTF3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSTF3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
