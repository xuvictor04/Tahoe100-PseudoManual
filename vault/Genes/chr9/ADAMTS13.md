---
symbol: "ADAMTS13"
type: "gene"
col: 8340
ensembl_id: "ENSG00000160323"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 13"
location: "9q34.2"
module: 10
arm: "+"
pooled_cpm: 6.12
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 22
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ADAMTS13

*ADAM metallopeptidase with thrombospondin type 1 motif 13* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 1.41× (z +3.7, q 0.075, up in 7 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.298× (z -13.1, q 3e-36, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TKFC]] (+0.65, fdr 1e-05), [[IDUA]] (+0.62, fdr 1e-05), [[FTCDNL1]] (+0.59, fdr 5e-05); moves opposite to [[LSP1P5-1]] (-0.48, fdr 6e-05), [[FBXO34]] (-0.45, fdr 1e-04), [[PRKRA]] (-0.43, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TRPM2-AS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +3.7 | 0.075 | 7/43 (NCI-H23, A498, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.075 | 8/46 (A498, Hs 766T, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.082 | 6/45 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.098 | 8/45 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.35× | +3.3 | 0.12 | 6/42 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | 1.35× | +3.2 | 0.12 | 9/46 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Arbutin (drug)]] 0.05 µM |  | 1.35× | +3.0 | 0.19 | 7/42 (SW480, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8340.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.298×** | -13.1 | 3e-36 | 41/46 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.364×** | -10.9 | 4e-25 | 34/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.484×** | -7.8 | 1e-12 | 29/45 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.487×** | -7.8 | 1e-12 | 27/38 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.505×** | -7.4 | 2e-11 | 28/45 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.547×** | -6.5 | 8e-09 | 23/45 (CHP-212, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.513×** | -6.5 | 9e-09 | 22/33 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.561×** | -5.6 | 2e-06 | 19/44 (PANC-1, SK-MEL-2, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.703×** | -5.4 | 6e-06 | 20/40 (AsPC-1, PANC-1, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.611×** | -5.3 | 7e-06 | 25/45 (NCI-H23, C-33 A, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.648×** | -4.7 | 2e-04 | 19/42 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.667×** | -4.3 | 7e-04 | 18/44 (Hs 766T, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.658×** | -4.2 | 9e-04 | 17/43 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.492×** | -4.0 | 0.003 | 14/35 (NCI-H1573, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.712×** | -3.6 | 0.010 | 10/45 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.524×** | -3.6 | 0.010 | 17/37 (NCI-H23, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.798×** | -3.4 | 0.020 | 16/45 (HepG2/C3A, Hs 766T, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.563×** | -3.2 | 0.036 | 9/41 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.814×** | -3.1 | 0.051 | 2/46 (SW 1271, CHP-212) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.725×** | -3.0 | 0.072 | 9/46 (C32, AsPC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.731×** | -2.9 | 0.090 | 8/43 (NCI-H23, NCI-H460, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0520× (z -16.1) |
| [[PANC-1 (line)]] | alt | 5.76 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.155× (z -10.8) |
| [[RKO (line)]] | wt | 11.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0648× (z -11.4) |
| [[SHP-77 (line)]] | alt | 7.87 | 0 | 2 (1 ⚠) | — | [[Pimitespib (drug)]] 0.05 µM 0.0661× (z -9.8) |
| [[SW1417 (line)]] | alt | 5.62 | 0 | 2 (1 ⚠) | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0617× (z -11.2) |
| [[SW480 (line)]] | alt | 6.38 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.147× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 2.49 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0898× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 17.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.123× (z -9.8) |
| [[LoVo (line)]] | wt | 9.86 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 5.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 5.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.104× (z -11.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 4.59 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0482× (z -9.5) |
| [[A-172 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TKFC]] | +0.65 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[IDUA]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[FTCDNL1]] | +0.59 | +0.69 / +0.40 | both halves | 5e-05 |  |
| [[ZNF839]] | +0.57 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[D2HGDH]] | +0.57 | +0.61 / +0.40 | both halves | 4e-05 |  |
| [[SSPOP]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 | pathway: Defective B3GALTL causes PpS |
| [[LINC01569]] | +0.56 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[LYRM9]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CYP4A22-AS1]] | +0.56 | +0.64 / +0.35 | both halves | 1e-04 |  |
| [[C1QTNF6]] | +0.55 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[FAM174A-DT]] | +0.55 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[ZFP41]] | +0.54 | +0.55 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSP1P5-1]] | -0.48 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[FBXO34]] | -0.45 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[PRKRA]] | -0.43 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[TARS3]] | -0.43 | -0.47 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPM2-AS]] | B | TRPM2-AS activity raises ADAMTS13's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 1.35× lower at baseline in the lines without TRPM2-AS | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[NOXA1]] | B | NOXA1 activity raises ADAMTS13's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without NOXA1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-29.0, 24.1); signed map (18.2, -42.5). **Vector** length 49.8, 6.25% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.1 | +2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | -1.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | -1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.4 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +0.9 | +1.6 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +0.8 | +1.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.1 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.0 | -6.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:133,414,358-133,459,402 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VWFCP, TTP, vWF-CP, FLJ42993, MGC118899, MGC118900, DKFZp434C2322; previously C9orf8 |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 14 pathways, smallest: Defective VWF cleavage by ADAMTS13 variant; Defects of platelet adhesion to exposed collagen; Enhanced cleavage of VWF variant by ADAMTS13 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q76LX8](https://www.uniprot.org/uniprotkb/Q76LX8) (A disintegrin and metalloproteinase with thrombospondin motifs 13):

> Cleaves the vWF multimers in plasma into smaller forms thereby controlling vWF-mediated platelet thrombus formation.

**Summary**, from NCBI Gene [11093](https://www.ncbi.nlm.nih.gov/gene/11093):

> This gene encodes a member of a family of proteins containing several distinct regions, including a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. The enzyme encoded by this gene specifically cleaves von Willebrand Factor (vWF). Defects in this gene are associated with thrombotic thrombocytopenic purpura. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:1366](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1366) · Entrez [11093](https://www.ncbi.nlm.nih.gov/gene/11093) · UniProt [Q76LX8](https://www.uniprot.org/uniprotkb/Q76LX8) · Ensembl [ENSG00000160323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160323)

## Data

Gene col 8340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8340); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8340]; `tensor/DDL_lfc|DDL_z.npy` [8340]; `embed/gene_vectors.npy` [8340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8340 or target_col == 8340). Every well: [[ADAMTS13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
