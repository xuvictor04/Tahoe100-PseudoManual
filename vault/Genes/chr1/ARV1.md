---
symbol: "ARV1"
type: "gene"
col: 10380
ensembl_id: "ENSG00000173409"
name: "ARV1 fatty acid homeostasis modulator"
location: "1q42.2"
module: 41
arm: "+"
pooled_cpm: 11.07
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ARV1

*ARV1 fatty acid homeostasis modulator* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.52× (z +13.0, q 4e-36, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.432× (z -11.8, q 2e-29, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUPT20H]] (+0.64, fdr 1e-05), [[VAMP4]] (+0.59, fdr 2e-05), [[TRUB1]] (+0.58, fdr 4e-05); moves opposite to [[DTNB]] (-0.48, fdr 6e-04), [[NUTM2A-AS1]] (-0.45, fdr 2e-04), [[SFXN5]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10380.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.52×** | +13.0 | 4e-36 | 42/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +13.0 | 4e-36 | 38/43 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.47×** | +12.8 | 5e-35 | 42/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +11.4 | 7e-28 | 29/33 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +10.8 | 7e-25 | 38/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.96×** | +9.1 | 6e-18 | 18/22 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +9.1 | 1e-17 | 36/43 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +8.6 | 5e-16 | 31/44 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +6.8 | 9e-10 | 24/46 (SHP-77, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +6.2 | 3e-08 | 21/48 (Panc 03.27, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.63×** | +5.8 | 3e-07 | 17/28 (A-172, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +5.4 | 3e-06 | 20/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +4.8 | 8e-05 | 16/46 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.7 | 1e-04 | 16/46 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.6 | 2e-04 | 19/46 (LS 180, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.010 | 9/47 (A-172, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.017 | 12/42 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.2 | 0.032 | 14/48 (LOX-IMVI, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10380.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.432×** | -11.8 | 2e-29 | 35/47 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.434×** | -11.7 | 3e-29 | 36/46 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.526×** | -9.0 | 3e-17 | 32/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.529×** | -8.9 | 5e-17 | 31/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.544×** | -8.6 | 1e-15 | 31/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.658×** | -5.6 | 3e-06 | 22/43 (SNU-423, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **0.824×** | -3.8 | 0.010 | 8/48 (NCI-H661, HepG2/C3A, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.694×** | -3.7 | 0.017 | 9/48 (Panc 03.27, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.620×** | -3.5 | 0.027 | 16/43 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.632×** | -3.4 | 0.042 | 11/35 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.802×** | -3.1 | 0.098 | 13/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.2 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.82× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Digitoxin (drug)]] 5 µM 0.178× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -12.6) |
| [[SW480 (line)]] | alt | 12.7 | 3 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.221× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.257× (z -10.8) |
| [[PANC-1 (line)]] | alt | 15.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 12.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.41× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Bosentan (hydrate) (drug)]] 5 µM 0.196× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 6.49 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0895× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.148× (z -8.5) |
| [[A-172 (line)]] | wt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +10.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 9.03 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0909× (z -10.8) ⚠ toxic |
| [[H4 (line)]] | wt | 11.4 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0771× (z -9.5) |
| [[Hs 766T (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -10.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 8.55 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0769× (z -11.9) |
| [[KATO III (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 8.82 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.25× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SNU-1 (line)]] | wt | 9.13 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0761× (z -9.2) |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0850× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUPT20H]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[VAMP4]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[TRUB1]] | +0.58 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[TMEM128]] | +0.58 | +0.76 / +0.42 | both halves | 4e-05 |  |
| [[FAM114A2]] | +0.58 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[FAM220A]] | +0.57 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[RUSF1]] | +0.57 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[ZBTB37]] | +0.56 | +0.60 / +0.35 | both halves | 1e-04 |  |
| [[ALG5]] | +0.56 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[ELP3]] | +0.55 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[MMUT]] | +0.55 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[SLC25A46]] | +0.54 | +0.60 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTNB]] | -0.48 | -0.39 / -0.22 | both halves | 6e-04 |  |
| [[NUTM2A-AS1]] | -0.45 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[SFXN5]] | -0.45 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[FARP2]] | -0.44 | -0.59 / -0.25 | both halves | 4e-04 |  |
| [[RAD9A]] | -0.44 | -0.57 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises ARV1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.383). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.3, -6.5); signed map (-18.4, -13.1). **Vector** length 61.0, 9.75% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.8 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +11.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.4 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +1.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.4 | +1.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.2 | -9.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.9 | -5.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -8.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -11.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.2 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | ARV1 fatty acid homeostasis modulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:230,978,981-231,000,733 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 3 pathways, smallest: Cholesterol biosynthesis; Metabolism of steroids; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2C2](https://www.uniprot.org/uniprotkb/Q9H2C2) (Protein ARV1):

> Plays a role as a mediator in the endoplasmic reticulum (ER) cholesterol and bile acid homeostasis. Participates in sterol transport out of the ER and distribution into plasma membranes.

**Summary**, from NCBI Gene [64801](https://www.ncbi.nlm.nih.gov/gene/64801):

> this gene encodes a transmembrane protein that contains a conserved zinc ribbon motif at the N- terminus. A similar protein in mouse is thought to function in fatty acid homeostasis. Mutations in this gene are associated with early infantile epileptic encephalopathy 38. [provided by RefSeq, Nov 2016]

**Accessions** — [HGNC:29561](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29561) · Entrez [64801](https://www.ncbi.nlm.nih.gov/gene/64801) · UniProt [Q9H2C2](https://www.uniprot.org/uniprotkb/Q9H2C2) · Ensembl [ENSG00000173409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173409)

## Data

Gene col 10380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10380); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10380]; `tensor/DDL_lfc|DDL_z.npy` [10380]; `embed/gene_vectors.npy` [10380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10380 or target_col == 10380). Every well: [[ARV1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARV1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
