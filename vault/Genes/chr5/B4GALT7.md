---
symbol: "B4GALT7"
type: "gene"
col: 379
ensembl_id: "ENSG00000027847"
name: "beta-1,4-galactosyltransferase 7"
location: "5q35.3"
module: 52
arm: "+"
pooled_cpm: 8.68
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# B4GALT7

*beta-1,4-galactosyltransferase 7* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.43× (z +4.3, q 0.008, up in 10 of 26 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.413× (z -11.6, q 4e-28, down in 36 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.422× (z -11.3, q 5e-27, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C11orf24]] (+0.74, fdr 7e-06), [[TMEM214]] (+0.70, fdr 7e-06), [[IPO13]] (+0.68, fdr 2e-05); moves opposite to [[PNISR]] (-0.59, fdr 1e-05), [[SPPL3]] (-0.55, fdr 2e-05), [[DENND5B]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[UST]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 379.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +4.3 | 0.008 | 10/26 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.0 | 0.016 | 12/33 (SNU-423, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.5 | 0.093 | 12/42 (KATO III, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ritonavir (drug)]] 0.5 µM |  | 1.27× | +3.2 | 0.21 | 7/44 (J82, KATO III, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 379.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.413×** | -11.6 | 4e-28 | 36/43 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.422×** | -11.3 | 5e-27 | 35/48 (J82, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.592×** | -9.7 | 6e-20 | 30/43 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.487×** | -9.4 | 7e-19 | 32/46 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.506×** | -8.9 | 6e-17 | 30/46 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.542×** | -7.7 | 1e-12 | 28/47 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.690×** | -6.8 | 6e-10 | 30/47 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.594×** | -6.8 | 7e-10 | 22/43 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.676×** | -4.9 | 6e-05 | 18/38 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.694×** | -4.8 | 1e-04 | 19/44 (SNU-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.703×** | -4.6 | 2e-04 | 19/46 (SNU-1, C32, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.702×** | -4.5 | 4e-04 | 17/43 (C-33 A, RKO, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.721×** | -4.3 | 8e-04 | 16/47 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.724×** | -4.2 | 1e-03 | 11/48 (SW 900, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | **0.810×** | -3.9 | 0.004 | 13/47 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.753×** | -3.7 | 0.007 | 12/44 (C32, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.754×** | -3.7 | 0.007 | 15/46 (SNU-1, C32, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 8.88 | 0 | 3 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0473× (z -13.3) |
| [[C32 (line)]] | wt | 11.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0898× (z -14.0) |
| [[J82 (line)]] | alt | 12.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -16.7) |
| [[A-172 (line)]] | wt | 12.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -12.6) |
| [[H4 (line)]] | wt | 17.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0744× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.212× (z -8.8) |
| [[HS-578T (line)]] | alt | 16.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -16.0) |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0792× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 7.42 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.174× (z -9.8) |
| [[A549 (line)]] | wt | 5.64 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.105× (z -8.5) |
| [[HCT15 (line)]] | alt | 8.48 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0550× (z -9.8) ⚠ toxic |
| [[HOP62 (line)]] | alt | 9.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.8) |
| [[KATO III (line)]] | alt | 9.50 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -8.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 6.20 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 8.21 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -8.5) |
| [[PANC-1 (line)]] | alt | 7.26 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 8.30 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0728× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 6.80 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0567× (z -8.5) |
| [[SNU-423 (line)]] | alt | 6.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -10.4) |
| [[SW 900 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -11.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 4.67 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.183× (z -8.6) |
| [[A-427 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf24]] | +0.74 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[TMEM214]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[IPO13]] | +0.68 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[LRRC59]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[YKT6]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[MAPK7]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[GMPPB]] | +0.64 | +0.59 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[RER1]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[TBL3]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[PCNX3]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[CHFR]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[BLTP2]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNISR]] | -0.59 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SPPL3]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[DENND5B]] | -0.54 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[CAMK2D]] | -0.52 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[GKAP1]] | -0.52 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[NR1D2]] | -0.51 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[WDSUB1]] | -0.50 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[RAB9A]] | -0.50 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[ITSN2]] | -0.50 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[RNPC3]] | -0.50 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[HMGN5]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UST]] | B | UST activity raises B4GALT7's level | lines that do not express UST (12) vs lines expressing it (38) | 1.33× lower at baseline in the lines without UST | 0.092 | ⚠ within organs, on part of the lines; also absent: SLC1A1, SH3GL3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.712). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.6, -28.5); signed map (-51.5, 3.5). **Vector** length 79.5, 14.4% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +2.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.0 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[Isocorydine (drug)]] 5 µM |  | +1.5 | +0.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.8 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -11.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.3 | -9.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,4-galactosyltransferase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,600,132-177,610,330 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XGALT-1, beta4Gal-T7 |
| Gene groups (HGNC) | Beta 4-glycosyltransferases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 7 pathways, smallest: Defective B4GALT7 causes EDS, progeroid type; Glycosaminoglycan-protein linkage region biosynthesis; Diseases associated with glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBV7](https://www.uniprot.org/uniprotkb/Q9UBV7) (Beta-1,4-galactosyltransferase 7):

> Required for the biosynthesis of the tetrasaccharide linkage region of proteoglycans, especially for small proteoglycans in skin fibroblasts.

**Summary**, from NCBI Gene [11285](https://www.ncbi.nlm.nih.gov/gene/11285):

> This gene is a member of the beta-1,4-galactosyltransferase (beta4GalT) family. Family members encode type II membrane-bound glycoproteins that appear to have exclusive specificity for the donor substrate UDP-galactose. Each beta4GalT member has a distinct function in the biosynthesis of different glycoconjugates and saccharide structures. As type II membrane proteins, they have an N-terminal hydrophobic signal sequence that directs the protein to the Golgi apparatus which then remains …

**Accessions** — [HGNC:930](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:930) · Entrez [11285](https://www.ncbi.nlm.nih.gov/gene/11285) · UniProt [Q9UBV7](https://www.uniprot.org/uniprotkb/Q9UBV7) · Ensembl [ENSG00000027847](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000027847)

## Data

Gene col 379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 379); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 379]; `tensor/DDL_lfc|DDL_z.npy` [379]; `embed/gene_vectors.npy` [379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 379 or target_col == 379). Every well: [[B4GALT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B4GALT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
